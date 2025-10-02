"""
Gauge Theory Operators for Neural Network Interpretability
===========================================================

Core mathematical implementation of gauge-theoretic operators for analyzing
neural networks as non-abelian computational gauge fields.

Author: Michael J. Pendleton
Email: michael.pendleton.20@gmail.com
Organization: The AI Cowboys / George Washington University
"""

import numpy as np
import torch
import torch.nn as nn
from typing import List, Tuple, Dict, Optional, Callable
from dataclasses import dataclass
from scipy.linalg import expm, logm
import warnings


@dataclass
class GaugeFieldProperties:
    """Container for gauge field measurements"""
    curvature: torch.Tensor
    commutator_norm: float
    jacobiator_norm: float
    non_abelian_measure: float
    homotopy_invariant: float


class CommutatorOperator:
    """
    Computes Lie bracket [A, B] = AB - BA

    The commutator measures non-commutativity, which is essential for:
    - Detecting order-dependent reasoning
    - Measuring non-linearity in transformations
    - Finding gauge field curvature

    Mathematical Foundation:
    ------------------------
    For operators A, B in a Lie algebra g:
        [A, B] = AB - BA

    Properties:
        - Antisymmetry: [A, B] = -[B, A]
        - Bilinearity: [αA + βB, C] = α[A,C] + β[B,C]
        - Jacobi identity: [A,[B,C]] + [B,[C,A]] + [C,[A,B]] = 0
    """

    def __init__(self, epsilon: float = 1e-10):
        """
        Args:
            epsilon: Numerical stability threshold
        """
        self.epsilon = epsilon

    def compute(self, A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
        """
        Compute [A, B] = AB - BA

        Args:
            A, B: Operators (matrices) of shape (..., n, n)

        Returns:
            Commutator [A, B] of same shape
        """
        return torch.matmul(A, B) - torch.matmul(B, A)

    def norm(self, A: torch.Tensor, B: torch.Tensor, ord: str = 'fro') -> torch.Tensor:
        """
        Compute ||[A, B]|| - measures non-commutativity strength

        Args:
            A, B: Operators
            ord: Matrix norm type ('fro', 2, 'nuc', etc.)

        Returns:
            Scalar norm value
        """
        comm = self.compute(A, B)
        return torch.linalg.matrix_norm(comm, ord=ord)

    def is_abelian(self, A: torch.Tensor, B: torch.Tensor, tol: float = None) -> bool:
        """
        Check if [A, B] ≈ 0 (commuting operators)

        Abelian structures indicate LINEAR reasoning - often undesirable!

        Args:
            A, B: Operators to test
            tol: Tolerance (defaults to self.epsilon)

        Returns:
            True if approximately commuting
        """
        tol = tol or self.epsilon
        return self.norm(A, B).item() < tol

    def nested_commutator(self, operators: List[torch.Tensor],
                          structure: List[int]) -> torch.Tensor:
        """
        Compute nested commutators like [[A, B], C]

        Args:
            operators: List of operators
            structure: Nesting structure as list of indices
                      e.g., [0, 1, 2] -> [[A, B], C]

        Returns:
            Nested commutator result
        """
        if len(structure) < 2:
            return operators[structure[0]]

        result = self.compute(operators[structure[0]], operators[structure[1]])

        for i in range(2, len(structure)):
            result = self.compute(result, operators[structure[i]])

        return result


class CurvatureOperator:
    """
    Computes gauge field strength tensor (curvature)

    F_ij = [∇_i, ∇_j] = ∂_i A_j - ∂_j A_i + [A_i, A_j]

    Curvature measures how reasoning paths depend on traversal order.
    High curvature = rich, context-dependent reasoning
    Low curvature = linear, predictable computation

    Mathematical Foundation:
    ------------------------
    In gauge theory, the curvature 2-form:
        F = dA + A ∧ A

    For neural networks:
        - A_i = weight matrices at layer i
        - F_ij = field strength between layers i, j
        - ||F|| = overall non-linear reasoning capacity
    """

    def __init__(self):
        self.commutator = CommutatorOperator()

    def compute_discrete(self, A_i: torch.Tensor, A_j: torch.Tensor,
                        finite_diff: bool = False) -> torch.Tensor:
        """
        Compute discrete curvature F_ij ≈ [A_i, A_j]

        For neural networks without continuous parameterization,
        we use the commutator as curvature proxy.

        Args:
            A_i, A_j: Weight operators at different layers/positions
            finite_diff: If True, include finite difference terms

        Returns:
            Curvature tensor F_ij
        """
        # Primary curvature from non-commutativity
        F = self.commutator.compute(A_i, A_j)

        return F

    def compute_full_field(self, operators: List[torch.Tensor]) -> torch.Tensor:
        """
        Compute full curvature field F_ij for all pairs

        Args:
            operators: List of n operators (e.g., attention heads, layers)

        Returns:
            Tensor of shape (n, n, d, d) containing F_ij for all pairs
        """
        n = len(operators)
        d = operators[0].shape[-1]

        F_field = torch.zeros(n, n, d, d, dtype=operators[0].dtype,
                             device=operators[0].device)

        for i in range(n):
            for j in range(i + 1, n):
                F_ij = self.compute_discrete(operators[i], operators[j])
                F_field[i, j] = F_ij
                F_field[j, i] = -F_ij  # Antisymmetry

        return F_field

    def ricci_scalar(self, F_field: torch.Tensor) -> torch.Tensor:
        """
        Compute Ricci scalar R = tr(F^T F) - total curvature

        This gives a single number measuring overall non-linearity.

        Args:
            F_field: Full curvature field (n, n, d, d)

        Returns:
            Scalar Ricci curvature
        """
        n, _, d, _ = F_field.shape
        R = 0.0

        for i in range(n):
            for j in range(n):
                F_ij = F_field[i, j]
                R += torch.trace(F_ij.T @ F_ij)

        return R


class JacobiatorOperator:
    """
    Computes Jacobiator: J(A,B,C) = [[A,B],C] + [[B,C],A] + [[C,A],B]

    The Jacobiator measures FAILURE of the Jacobi identity.
    - J = 0: Perfect Lie algebra structure
    - J ≠ 0: Higher-order non-associativity (deep hierarchical structure)

    This captures whether the network can perform hierarchical composition
    or is limited to flat, associative operations.

    Mathematical Foundation:
    ------------------------
    In a Lie algebra, Jacobi identity always holds:
        [[A,B],C] + [[B,C],A] + [[C,A],B] = 0

    For approximate or truncated operators, measuring ||J|| reveals:
        - Hierarchical thinking capability
        - Higher-order reasoning structure
        - Conceptualization vs mere association
    """

    def __init__(self):
        self.commutator = CommutatorOperator()

    def compute(self, A: torch.Tensor, B: torch.Tensor,
                C: torch.Tensor) -> torch.Tensor:
        """
        Compute J(A,B,C) = [[A,B],C] + [[B,C],A] + [[C,A],B]

        Args:
            A, B, C: Three operators

        Returns:
            Jacobiator J(A,B,C)
        """
        # [[A,B],C]
        comm_AB = self.commutator.compute(A, B)
        term1 = self.commutator.compute(comm_AB, C)

        # [[B,C],A]
        comm_BC = self.commutator.compute(B, C)
        term2 = self.commutator.compute(comm_BC, A)

        # [[C,A],B]
        comm_CA = self.commutator.compute(C, A)
        term3 = self.commutator.compute(comm_CA, B)

        return term1 + term2 + term3

    def norm(self, A: torch.Tensor, B: torch.Tensor,
             C: torch.Tensor, ord: str = 'fro') -> torch.Tensor:
        """
        Compute ||J(A,B,C)|| - hierarchical structure measure

        Returns:
            Scalar norm of Jacobiator
        """
        J = self.compute(A, B, C)
        return torch.linalg.matrix_norm(J, ord=ord)

    def compute_all_triangles(self, operators: List[torch.Tensor]) -> torch.Tensor:
        """
        Compute Jacobiator for all triangular combinations

        This creates the "plaquettes" that reveal algebraic structure.

        Args:
            operators: List of n operators

        Returns:
            Tensor of shape (n, n, n, d, d) with J_ijk for all triples
        """
        n = len(operators)
        d = operators[0].shape[-1]

        J_field = torch.zeros(n, n, n, d, d, dtype=operators[0].dtype,
                             device=operators[0].device)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    J_ijk = self.compute(operators[i], operators[j], operators[k])
                    J_field[i, j, k] = J_ijk

        return J_field


class BCHExpansion:
    """
    Baker-Campbell-Hausdorff Formula Implementation

    e^A e^B = e^{Z(A,B)}
    where
    Z = A + B + 1/2[A,B] + 1/12([A,[A,B]] + [B,[B,A]]) + ...

    This reveals how sequential operations compose non-linearly.

    Mathematical Foundation:
    ------------------------
    The BCH formula shows that composition in Lie groups corresponds
    to addition + correction terms in Lie algebra:

    Z(A,B) = A + B + 1/2[A,B] + 1/12[A,[A,B]] - 1/12[B,[A,B]] + ...

    For neural networks, this explains:
        - How layers compose beyond simple addition
        - Why order matters (the [A,B] term)
        - Higher-order interaction effects

    Applications:
        - Understanding residual connections
        - Analyzing skip connections
        - Optimal layer ordering
    """

    def __init__(self, max_order: int = 5):
        """
        Args:
            max_order: Maximum BCH expansion order
        """
        self.max_order = max_order
        self.commutator = CommutatorOperator()

    def compute_order_2(self, A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
        """
        Z = A + B + 1/2[A,B]
        """
        return A + B + 0.5 * self.commutator.compute(A, B)

    def compute_order_3(self, A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
        """
        Z = A + B + 1/2[A,B] + 1/12([A,[A,B]] + [B,[B,A]])
        """
        comm_AB = self.commutator.compute(A, B)
        Z2 = self.compute_order_2(A, B)

        comm_A_AB = self.commutator.compute(A, comm_AB)
        comm_B_BA = self.commutator.compute(B, -comm_AB)

        Z3 = Z2 + (1.0/12.0) * (comm_A_AB + comm_B_BA)
        return Z3

    def compute_order_4(self, A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
        """
        4th order BCH expansion
        """
        Z3 = self.compute_order_3(A, B)
        comm_AB = self.commutator.compute(A, B)

        # [B,[A,[A,B]]]
        comm_A_AB = self.commutator.compute(A, comm_AB)
        term = self.commutator.compute(B, comm_A_AB)

        Z4 = Z3 - (1.0/24.0) * term
        return Z4

    def compute(self, A: torch.Tensor, B: torch.Tensor,
                order: Optional[int] = None) -> torch.Tensor:
        """
        Compute BCH expansion to specified order

        Args:
            A, B: Operators in Lie algebra
            order: Expansion order (defaults to self.max_order)

        Returns:
            Z(A,B) such that e^A e^B ≈ e^Z
        """
        order = order or self.max_order

        if order <= 2:
            return self.compute_order_2(A, B)
        elif order == 3:
            return self.compute_order_3(A, B)
        elif order >= 4:
            return self.compute_order_4(A, B)

    def plaquette_strength(self, operators: List[torch.Tensor],
                          indices: List[int]) -> float:
        """
        Compute BCH plaquette strength for a loop of operators

        A plaquette measures curvature around a closed loop.

        Args:
            operators: List of operators
            indices: Ordered indices forming a loop

        Returns:
            Plaquette strength (scalar)
        """
        # Compute forward path
        Z_forward = operators[indices[0]]
        for i in range(1, len(indices)):
            Z_forward = self.compute(Z_forward, operators[indices[i]])

        # Compute reverse path
        Z_reverse = operators[indices[-1]]
        for i in range(len(indices) - 2, -1, -1):
            Z_reverse = self.compute(Z_reverse, operators[indices[i]])

        # Plaquette = || Z_forward - Z_reverse ||
        plaquette = torch.linalg.matrix_norm(Z_forward - Z_reverse, ord='fro')

        return plaquette.item()


class WilsonLoop:
    """
    Computes Wilson loops W(C) = P exp(∮_C A_μ dx^μ)

    Wilson loops measure holonomy - how much a state changes when
    transported around a closed path.

    This reveals PATH-DEPENDENT reasoning:
        - Does A→B→C→A return to the same state?
        - How much does reasoning depend on the route taken?
        - Are there preferred reasoning paths?

    Mathematical Foundation:
    ------------------------
    The Wilson loop is the path-ordered exponential:
        W(C) = P exp(∮_C A)

    For discrete paths: W = U_n ... U_2 U_1
    where U_i = exp(A_i) are parallel transport operators.

    Properties:
        - Gauge invariant under transformations
        - Measures enclosed curvature (Stokes theorem)
        - Reveals topological structure of reasoning space
    """

    def __init__(self):
        self.commutator = CommutatorOperator()

    def compute_discrete(self, operators: List[torch.Tensor],
                        path: List[int]) -> torch.Tensor:
        """
        Compute Wilson loop along discrete path

        W = U_n ... U_2 U_1 where U_i = exp(A_i)

        Args:
            operators: List of Lie algebra elements A_i
            path: Ordered indices defining the loop

        Returns:
            Wilson loop operator W (matrix)
        """
        device = operators[0].device
        dtype = operators[0].dtype
        d = operators[0].shape[-1]

        # Initialize as identity
        W = torch.eye(d, dtype=dtype, device=device)

        # Path-ordered product
        for idx in path:
            # Convert Lie algebra element to group element
            U_i = torch.matrix_exp(operators[idx])
            W = torch.matmul(W, U_i)

        return W

    def holonomy(self, operators: List[torch.Tensor],
                 path: List[int]) -> torch.Tensor:
        """
        Compute holonomy = log(W)

        This returns to Lie algebra and measures total curvature.

        Args:
            operators: Lie algebra elements
            path: Loop path

        Returns:
            Holonomy h = log(W(C))
        """
        W = self.compute_discrete(operators, path)

        # Use logm for matrix logarithm
        W_np = W.detach().cpu().numpy()
        h_np = logm(W_np)
        h = torch.from_numpy(np.real(h_np)).to(W.device, W.dtype)

        return h

    def trace_invariant(self, operators: List[torch.Tensor],
                       path: List[int]) -> float:
        """
        Compute tr(W) - gauge invariant observable

        Returns:
            Real part of tr(W(C))
        """
        W = self.compute_discrete(operators, path)
        return torch.real(torch.trace(W)).item()

    def all_loops(self, operators: List[torch.Tensor],
                  max_length: int = 4) -> Dict[Tuple[int, ...], float]:
        """
        Compute Wilson loops for all closed paths up to max_length

        Args:
            operators: List of operators
            max_length: Maximum loop length

        Returns:
            Dictionary mapping paths to loop strengths
        """
        n = len(operators)
        loops = {}

        def generate_loops(current_path, remaining_length):
            if remaining_length == 0:
                if len(current_path) >= 3:  # Need at least 3 nodes for a loop
                    # Close the loop
                    full_path = current_path + [current_path[0]]
                    trace_val = self.trace_invariant(operators, full_path)
                    loops[tuple(full_path)] = trace_val
                return

            if len(current_path) == 0:
                start_node = 0
            else:
                start_node = current_path[-1] + 1

            for i in range(start_node, n):
                if i not in current_path:
                    generate_loops(current_path + [i], remaining_length - 1)

        for length in range(3, min(max_length + 1, n + 1)):
            generate_loops([], length)

        return loops


class HomotopyInvariant:
    """
    Computes homotopy invariants for reasoning chains

    Homotopy theory studies continuous deformations.
    Homotopy invariants are properties preserved under deformation.

    For neural networks, this means:
        - Robust features that survive perturbations
        - Stable reasoning patterns
        - Guaranteed generalization properties

    Mathematical Foundation:
    ------------------------
    Two paths γ₀, γ₁ are homotopic if there exists a continuous
    deformation H: [0,1] × [0,1] → M with:
        H(t,0) = γ₀(t)
        H(t,1) = γ₁(t)

    Homotopy invariants:
        - Fundamental group π₁(M)
        - Higher homotopy groups π_n(M)
        - Characteristic classes

    Application to NNs:
        - Decision boundary topology
        - Reasoning path equivalence classes
        - Stable feature manifolds
    """

    def __init__(self):
        self.wilson = WilsonLoop()
        self.commutator = CommutatorOperator()

    def fundamental_group_generators(self, operators: List[torch.Tensor],
                                    max_loops: int = 10) -> List[Tuple[int, ...]]:
        """
        Find generators of fundamental group π₁

        These are non-contractible loops in reasoning space.

        Args:
            operators: Operators defining the space
            max_loops: Maximum number of loops to check

        Returns:
            List of loop paths that generate π₁
        """
        all_loops = self.wilson.all_loops(operators, max_length=4)

        # Sort by trace value (strength)
        sorted_loops = sorted(all_loops.items(),
                            key=lambda x: abs(x[1]),
                            reverse=True)

        generators = []
        for loop_path, strength in sorted_loops[:max_loops]:
            if abs(strength - len(operators)) > 0.1:  # Non-trivial loop
                generators.append(loop_path)

        return generators

    def compute_chern_number(self, F_field: torch.Tensor) -> float:
        """
        Compute Chern number (topological invariant)

        C = (1/2π) ∫ tr(F ∧ F)

        For discrete case, sum over plaquettes.

        Args:
            F_field: Curvature field (n, n, d, d)

        Returns:
            Chern number (integer for physical systems)
        """
        n, _, d, _ = F_field.shape
        chern = 0.0

        # Sum over all plaquettes (rectangular loops)
        for i in range(n - 1):
            for j in range(i + 1, n):
                # Plaquette contribution: tr(F_ij)
                F_ij = F_field[i, j]
                chern += torch.trace(F_ij).item()

        chern /= (2 * np.pi)
        return chern

    def homotopy_equivalence(self, path1: List[int], path2: List[int],
                            operators: List[torch.Tensor],
                            tol: float = 1e-3) -> bool:
        """
        Check if two paths are homotopically equivalent

        Paths are homotopic if their Wilson loops are equal.

        Args:
            path1, path2: Two reasoning paths
            operators: Operators defining the space
            tol: Tolerance for equivalence

        Returns:
            True if paths are homotopically equivalent
        """
        W1 = self.wilson.compute_discrete(operators, path1)
        W2 = self.wilson.compute_discrete(operators, path2)

        diff_norm = torch.linalg.matrix_norm(W1 - W2, ord='fro')
        return diff_norm.item() < tol


# Export all operators
__all__ = [
    'CommutatorOperator',
    'CurvatureOperator',
    'JacobiatorOperator',
    'BCHExpansion',
    'WilsonLoop',
    'HomotopyInvariant',
    'GaugeFieldProperties'
]
