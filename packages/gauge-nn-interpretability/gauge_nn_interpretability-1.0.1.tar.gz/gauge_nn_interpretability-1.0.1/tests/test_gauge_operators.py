"""
Unit tests for gauge operators

Run with: pytest tests/
"""

import sys
sys.path.append('../src')

import torch
import numpy as np
import pytest

from gauge_operators import (
    CommutatorOperator,
    CurvatureOperator,
    JacobiatorOperator,
    BCHExpansion,
    WilsonLoop,
    HomotopyInvariant
)


@pytest.fixture
def test_operators():
    """Create test operators"""
    torch.manual_seed(42)
    d = 16
    n = 3

    operators = []
    for i in range(n):
        A = torch.randn(d, d)
        A = (A + A.T) / 2  # Make Hermitian
        operators.append(A)

    return operators


class TestCommutatorOperator:
    """Test CommutatorOperator class"""

    def test_antisymmetry(self, test_operators):
        """Test [A,B] = -[B,A]"""
        comm = CommutatorOperator()
        A, B = test_operators[0], test_operators[1]

        comm_AB = comm.compute(A, B)
        comm_BA = comm.compute(B, A)

        assert torch.allclose(comm_AB, -comm_BA, atol=1e-5)

    def test_bilinearity(self, test_operators):
        """Test [αA+βB, C] = α[A,C] + β[B,C]"""
        comm = CommutatorOperator()
        A, B, C = test_operators

        alpha, beta = 2.0, 3.0

        lhs = comm.compute(alpha * A + beta * B, C)
        rhs = alpha * comm.compute(A, C) + beta * comm.compute(B, C)

        assert torch.allclose(lhs, rhs, atol=1e-4)

    def test_jacobi_identity(self, test_operators):
        """Test [[A,B],C] + [[B,C],A] + [[C,A],B] ≈ 0"""
        comm = CommutatorOperator()
        A, B, C = test_operators

        term1 = comm.compute(comm.compute(A, B), C)
        term2 = comm.compute(comm.compute(B, C), A)
        term3 = comm.compute(comm.compute(C, A), B)

        jacobi = term1 + term2 + term3
        jacobi_norm = torch.linalg.matrix_norm(jacobi, ord='fro')

        # Should be small (approximate Lie algebra)
        assert jacobi_norm < 1.0

    def test_norm(self, test_operators):
        """Test norm computation"""
        comm = CommutatorOperator()
        A, B = test_operators[0], test_operators[1]

        norm = comm.norm(A, B)

        assert norm >= 0
        assert isinstance(norm.item(), float)


class TestCurvatureOperator:
    """Test CurvatureOperator class"""

    def test_antisymmetry(self, test_operators):
        """Test F_ij = -F_ji"""
        curv = CurvatureOperator()
        A, B = test_operators[0], test_operators[1]

        F_AB = curv.compute_discrete(A, B)
        F_BA = curv.compute_discrete(B, A)

        assert torch.allclose(F_AB, -F_BA, atol=1e-5)

    def test_full_field(self, test_operators):
        """Test full curvature field computation"""
        curv = CurvatureOperator()

        F_field = curv.compute_full_field(test_operators)

        n = len(test_operators)
        d = test_operators[0].shape[0]

        assert F_field.shape == (n, n, d, d)

        # Check antisymmetry
        for i in range(n):
            for j in range(n):
                assert torch.allclose(F_field[i, j], -F_field[j, i], atol=1e-5)

    def test_ricci_scalar(self, test_operators):
        """Test Ricci scalar computation"""
        curv = CurvatureOperator()

        F_field = curv.compute_full_field(test_operators)
        R = curv.ricci_scalar(F_field)

        assert R >= 0  # Should be non-negative
        assert isinstance(R.item(), float)


class TestJacobiatorOperator:
    """Test JacobiatorOperator class"""

    def test_compute(self, test_operators):
        """Test Jacobiator computation"""
        jac = JacobiatorOperator()
        A, B, C = test_operators

        J = jac.compute(A, B, C)

        d = A.shape[0]
        assert J.shape == (d, d)

    def test_norm(self, test_operators):
        """Test Jacobiator norm"""
        jac = JacobiatorOperator()
        A, B, C = test_operators

        norm = jac.norm(A, B, C)

        assert norm >= 0
        assert isinstance(norm.item(), float)


class TestBCHExpansion:
    """Test BCHExpansion class"""

    def test_order_2(self, test_operators):
        """Test 2nd order BCH"""
        bch = BCHExpansion(max_order=2)
        A, B = test_operators[0], test_operators[1]

        Z = bch.compute_order_2(A, B)

        d = A.shape[0]
        assert Z.shape == (d, d)

    def test_order_3(self, test_operators):
        """Test 3rd order BCH"""
        bch = BCHExpansion(max_order=3)
        A, B = test_operators[0], test_operators[1]

        Z = bch.compute_order_3(A, B)

        d = A.shape[0]
        assert Z.shape == (d, d)

    def test_plaquette_strength(self, test_operators):
        """Test plaquette strength computation"""
        bch = BCHExpansion()

        loop = [0, 1, 2]
        strength = bch.plaquette_strength(test_operators, loop)

        assert strength >= 0
        assert isinstance(strength, float)


class TestWilsonLoop:
    """Test WilsonLoop class"""

    def test_compute_discrete(self, test_operators):
        """Test discrete Wilson loop"""
        wilson = WilsonLoop()
        path = [0, 1, 2, 0]

        W = wilson.compute_discrete(test_operators, path)

        d = test_operators[0].shape[0]
        assert W.shape == (d, d)

    def test_trace_invariant(self, test_operators):
        """Test trace invariant"""
        wilson = WilsonLoop()
        path = [0, 1, 0]

        trace = wilson.trace_invariant(test_operators, path)

        assert isinstance(trace, float)


class TestHomotopyInvariant:
    """Test HomotopyInvariant class"""

    def test_chern_number(self, test_operators):
        """Test Chern number computation"""
        curv = CurvatureOperator()
        homotopy = HomotopyInvariant()

        F_field = curv.compute_full_field(test_operators)
        chern = homotopy.compute_chern_number(F_field)

        assert isinstance(chern, float)

    def test_fundamental_group_generators(self, test_operators):
        """Test fundamental group generators"""
        homotopy = HomotopyInvariant()

        generators = homotopy.fundamental_group_generators(test_operators, max_loops=3)

        assert isinstance(generators, list)


# Integration tests
class TestIntegration:
    """Integration tests"""

    def test_full_analysis_pipeline(self, test_operators):
        """Test full analysis pipeline"""
        # Commutators
        comm = CommutatorOperator()
        comm_norm = comm.norm(test_operators[0], test_operators[1])
        assert comm_norm > 0

        # Curvature
        curv = CurvatureOperator()
        F_field = curv.compute_full_field(test_operators)
        R = curv.ricci_scalar(F_field)
        assert R >= 0

        # Jacobiator
        jac = JacobiatorOperator()
        J_norm = jac.norm(*test_operators)
        assert J_norm >= 0

        # BCH
        bch = BCHExpansion()
        Z = bch.compute(test_operators[0], test_operators[1])
        assert Z.shape == test_operators[0].shape

        # Wilson
        wilson = WilsonLoop()
        trace = wilson.trace_invariant(test_operators, [0, 1, 0])
        assert isinstance(trace, float)

        # Homotopy
        homotopy = HomotopyInvariant()
        chern = homotopy.compute_chern_number(F_field)
        assert isinstance(chern, float)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
