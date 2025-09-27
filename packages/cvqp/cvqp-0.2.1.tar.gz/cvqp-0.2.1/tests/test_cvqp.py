"""
Tests for the CVQP solver and projection functions.
"""

import pytest
import numpy as np
import scipy as sp
import cvxpy as cp

from cvqp import CVQP, CVQPParams, proj_sum_largest, proj_cvar

# Test tolerances
OBJECTIVE_TOL = 1e-2
FEASIBILITY_TOL = 1e-3


def create_test_problem(matrix_type="dense", size=(50, 8)):
    """Create a standard test problem."""
    np.random.seed(42)
    m, d = size

    if matrix_type == "dense":
        P = np.eye(d)
        B = np.eye(d)
    elif matrix_type == "sparse":
        P = sp.sparse.eye(d)
        B = sp.sparse.eye(d)
    else:  # linear
        P = None
        B = np.eye(d)

    return CVQPParams(
        P=P,
        q=np.random.randn(d) * 0.1,
        A=np.random.randn(m, d) * 0.2 + 0.1,
        B=B,
        l=-np.ones(d) * 0.8,
        u=np.ones(d) * 0.8,
        beta=0.9,
        kappa=0.2,
    )


def assert_feasible(results, params):
    """Check that solution satisfies all constraints."""
    x = results.x

    # Box constraints
    assert np.all(x >= params.l - FEASIBILITY_TOL), "Lower bound violated"
    assert np.all(x <= params.u + FEASIBILITY_TOL), "Upper bound violated"

    # CVaR constraint
    sorted_vals = np.sort(params.A @ x)
    k = int(len(sorted_vals) * (1 - params.beta))
    cvar = np.mean(sorted_vals[-k:]) if k > 0 else 0
    assert cvar <= params.kappa + FEASIBILITY_TOL, f"CVaR {cvar:.3f} > {params.kappa}"


def solve_with_cvxpy(params):
    """Solve problem using CVXPY for comparison."""
    d = params.q.shape[0]
    x = cp.Variable(d)

    # Build objective: linear or quadratic
    if params.P is None:
        objective = cp.Minimize(params.q @ x)
    else:
        P_dense = params.P.toarray() if sp.sparse.issparse(params.P) else params.P
        objective = cp.Minimize(0.5 * cp.quad_form(x, P_dense) + params.q @ x)

    # Build constraints: CVaR + box constraints
    B_dense = params.B.toarray() if sp.sparse.issparse(params.B) else params.B
    constraints = [cp.cvar(params.A @ x, params.beta) <= params.kappa, params.l <= B_dense @ x, B_dense @ x <= params.u]

    prob = cp.Problem(objective, constraints)
    prob.solve(solver=cp.CLARABEL, verbose=False)

    if prob.status != cp.OPTIMAL:
        return None, None

    # Compute objective value to match CVQP's calculation
    if params.P is None:
        obj_val = params.q @ x.value
    else:
        P_dense = params.P.toarray() if sp.sparse.issparse(params.P) else params.P
        obj_val = 0.5 * np.dot(x.value, P_dense @ x.value) + params.q @ x.value

    return x.value, obj_val


class TestProjections:
    """Test projection functions."""

    def test_proj_sum_largest_basic(self):
        """Test basic sum-of-k-largest projection."""
        x = np.array([6.0, 2.0, 5.0, 4.0, 1.0])
        k, alpha = 2, 7.0

        result = proj_sum_largest(x, k, alpha)

        # Verify constraint satisfaction
        sum_k_largest = sum(sorted(result, reverse=True)[:k])
        assert sum_k_largest <= alpha + FEASIBILITY_TOL

        # Cross-check against CVXPY reference solution
        y = cp.Variable(x.shape)
        prob = cp.Problem(cp.Minimize(cp.sum_squares(y - x)), [cp.sum_largest(y, k) <= alpha])
        prob.solve(solver=cp.CLARABEL, verbose=False)

        if prob.status == cp.OPTIMAL:
            assert np.linalg.norm(result - y.value) <= 1e-3

    def test_proj_sum_largest_no_projection_needed(self):
        """Test when constraint is already satisfied."""
        x = np.array([1.0, 2.0, 3.0, 4.0])
        k, alpha = 2, 10.0  # Sum of 2 largest (4+3=7) < alpha

        result = proj_sum_largest(x, k, alpha)
        np.testing.assert_array_almost_equal(result, x)

    def test_proj_sum_largest_edge_cases(self):
        """Test edge cases for sum-of-k-largest projection."""
        x = np.array([5.0, 4.0, 3.0, 2.0, 1.0])

        # k=1 case
        result = proj_sum_largest(x, 1, 3.0)
        assert max(result) <= 3.0 + FEASIBILITY_TOL

        # alpha=0 case
        result = proj_sum_largest(x, 2, 0.0)
        sum_k_largest = sum(sorted(result, reverse=True)[:2])
        assert sum_k_largest <= FEASIBILITY_TOL

        # k=len(x) case
        result = proj_sum_largest(x, len(x), 10.0)
        assert np.sum(result) <= 10.0 + FEASIBILITY_TOL

    def test_proj_cvar_basic(self):
        """Test basic CVaR projection."""
        x = np.array([6.0, 2.0, 5.0, 4.0, 1.0])
        beta, kappa = 0.6, 4.0  # k = int((1-0.6)*5) = 2

        result = proj_cvar(x, beta, kappa)

        sorted_x = np.sort(result)
        k = int((1 - beta) * len(x))
        cvar = np.mean(sorted_x[-k:]) if k > 0 else 0
        assert cvar <= kappa + FEASIBILITY_TOL

    def test_proj_cvar_equivalence(self):
        """Test that proj_cvar gives same result as proj_sum_largest."""
        x = np.array([6.0, 2.0, 5.0, 4.0, 1.0])
        beta, kappa = 0.6, 3.0

        result_cvar = proj_cvar(x, beta, kappa)

        # CVaR projection should be equivalent to sum-of-k-largest
        k = int((1 - beta) * len(x))
        alpha = kappa * k
        result_sum = proj_sum_largest(x, k, alpha)

        np.testing.assert_array_almost_equal(result_cvar, result_sum)

    def test_projection_validation(self):
        """Test input validation for projection functions."""
        x = np.array([1.0, 2.0, 3.0])

        # proj_sum_largest validation
        with pytest.raises(ValueError, match="k must be between"):
            proj_sum_largest(x, 0, 1.0)

        with pytest.raises(ValueError, match="alpha must be non-negative"):
            proj_sum_largest(x, 1, -1.0)

        with pytest.raises(ValueError, match="1D array"):
            proj_sum_largest(np.array([[1, 2], [3, 4]]), 1, 1.0)

        # proj_cvar validation
        with pytest.raises(ValueError, match="beta must be between 0 and 1"):
            proj_cvar(x, 0.0, 1.0)

        with pytest.raises(ValueError, match="beta must be between 0 and 1"):
            proj_cvar(x, 1.0, 1.0)

        with pytest.raises(ValueError, match="kappa must be non-negative"):
            proj_cvar(x, 0.5, -1.0)


class TestCVQPSolver:
    """Test CVQP solver functionality."""

    @pytest.mark.parametrize("matrix_type", ["dense", "sparse", "linear"])
    def test_solver_basic(self, matrix_type):
        """Test solver with different matrix types."""
        params = create_test_problem(matrix_type)

        cvqp = CVQP(params)
        results = cvqp.solve()

        assert results.problem_status == "optimal"
        assert_feasible(results, params)

        # Verify objective value matches CVXPY reference
        cvxpy_sol, cvxpy_obj = solve_with_cvxpy(params)
        if cvxpy_sol is not None and cvxpy_obj is not None:
            rel_obj_gap = abs(cvxpy_obj - results.objval[-1]) / abs(cvxpy_obj)
            assert rel_obj_gap <= OBJECTIVE_TOL, f"Objective gap {rel_obj_gap:.2e} > {OBJECTIVE_TOL}"

    def test_solver_warm_start(self):
        """Test warm start functionality."""
        np.random.seed(123)
        params = create_test_problem(size=(30, 5))

        cvqp = CVQP(params)

        # Cold start from zero
        results_cold = cvqp.solve(verbose=False)

        # Warm start from random initialization
        warm_start = np.random.randn(5) * 0.1
        results_warm = cvqp.solve(warm_start=warm_start, verbose=False)

        # Both should converge to optimal solutions
        assert results_cold.problem_status == "optimal"
        assert results_warm.problem_status == "optimal"
        assert_feasible(results_cold, params)
        assert_feasible(results_warm, params)


class TestValidation:
    """Test parameter validation."""

    def test_cvqp_params_validation(self):
        """Test CVQPParams validation."""
        d = 3
        valid_params = dict(P=np.eye(d), q=np.ones(d), A=np.ones((5, d)), B=np.eye(d), l=-np.ones(d), u=np.ones(d), beta=0.9, kappa=0.1)

        CVQPParams(**valid_params)
        with pytest.raises(ValueError, match="beta must be between 0 and 1"):
            CVQPParams(**{**valid_params, "beta": 0.0})

        with pytest.raises(ValueError, match="Incompatible dimensions"):
            CVQPParams(**{**valid_params, "q": np.ones(d + 1)})
