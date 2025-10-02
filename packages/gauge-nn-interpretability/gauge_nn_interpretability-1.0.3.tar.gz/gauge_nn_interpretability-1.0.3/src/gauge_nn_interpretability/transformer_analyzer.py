"""
Transformer-Specific Gauge Theory Analyzer
===========================================

Applies computational gauge theory to transformer architectures,
extracting interpretable structure from attention mechanisms.

Author: Michael J. Pendleton
"""

import torch
import torch.nn as nn
import numpy as np
from typing import List, Dict, Tuple, Optional, Any
from dataclasses import dataclass, field
import warnings

from .gauge_operators import (
    CommutatorOperator,
    CurvatureOperator,
    JacobiatorOperator,
    BCHExpansion,
    WilsonLoop,
    HomotopyInvariant,
    GaugeFieldProperties
)


@dataclass
class AttentionAnalysis:
    """Results from analyzing attention as gauge field"""
    layer_idx: int
    head_idx: int
    curvature_norm: float
    commutator_strengths: Dict[int, float]
    jacobiator_norm: float
    reasoning_loops: List[Tuple[int, ...]]
    abelian_collapse: bool
    homotopy_class: int


@dataclass
class TransformerGaugeAnalysis:
    """Complete gauge-theoretic analysis of transformer"""
    model_name: str
    total_curvature: float
    ricci_scalar: float
    chern_number: float
    non_abelian_measure: float
    attention_analyses: List[AttentionAnalysis]
    bch_plaquettes: Dict[str, float]
    wilson_loops: Dict[Tuple[int, ...], float]
    reasoning_paths: List[List[int]]
    stability_score: float
    interpretability_metrics: Dict[str, float] = field(default_factory=dict)


class TransformerGaugeAnalyzer:
    """
    Main analyzer for treating transformers as gauge fields

    This class extracts gauge-theoretic structure from transformers:
    - Attention heads as Lie algebra elements
    - Layer transitions as connections
    - Forward pass as parallel transport
    - Reasoning as Wilson loops

    Key Insight:
    ------------
    Query, Key, Value matrices (Q, K, V) are treated as elements of
    a non-abelian Lie algebra. Their commutators reveal reasoning structure.

    Attention(Q,K,V) = softmax(QK^T/√d)V is a gauge transformation
    """

    def __init__(self, model: nn.Module, device: str = 'cpu'):
        """
        Args:
            model: Transformer model (HuggingFace or custom)
            device: Computation device
        """
        self.model = model
        self.device = device

        # Initialize gauge operators
        self.commutator = CommutatorOperator()
        self.curvature = CurvatureOperator()
        self.jacobiator = JacobiatorOperator()
        self.bch = BCHExpansion(max_order=4)
        self.wilson = WilsonLoop()
        self.homotopy = HomotopyInvariant()

        # Storage for extracted operators
        self.attention_operators: Dict[Tuple[int, int], torch.Tensor] = {}
        self.layer_operators: List[torch.Tensor] = []

    def extract_attention_operators(self,
                                   input_ids: Optional[torch.Tensor] = None,
                                   extract_mode: str = 'weights') -> None:
        """
        Extract Lie algebra operators from attention mechanism

        Two modes:
        1. 'weights': Use Q, K, V weight matrices directly
        2. 'activations': Use actual Q, K, V values from forward pass

        Args:
            input_ids: Input tokens (required for 'activations' mode)
            extract_mode: 'weights' or 'activations'
        """
        self.model.eval()

        if extract_mode == 'weights':
            self._extract_from_weights()
        elif extract_mode == 'activations':
            if input_ids is None:
                raise ValueError("input_ids required for activations mode")
            self._extract_from_activations(input_ids)
        else:
            raise ValueError(f"Unknown mode: {extract_mode}")

    def _extract_from_weights(self) -> None:
        """
        Extract operators from weight matrices

        For each attention head, we construct operators from Q, K, V weights.
        """
        # Find attention layers (HuggingFace style)
        attention_layers = []

        for name, module in self.model.named_modules():
            if 'attention' in name.lower() or 'attn' in name.lower():
                if hasattr(module, 'query') or hasattr(module, 'q_proj'):
                    attention_layers.append((name, module))

        # Extract operators from each layer/head
        for layer_idx, (name, attn_module) in enumerate(attention_layers):
            # Get Q, K, V weight matrices
            if hasattr(attn_module, 'query'):
                W_q = attn_module.query.weight.data
                W_k = attn_module.key.weight.data
                W_v = attn_module.value.weight.data
            elif hasattr(attn_module, 'q_proj'):
                W_q = attn_module.q_proj.weight.data
                W_k = attn_module.k_proj.weight.data
                W_v = attn_module.v_proj.weight.data
            else:
                continue

            # Number of heads
            if hasattr(attn_module, 'num_attention_heads'):
                num_heads = attn_module.num_attention_heads
            elif hasattr(attn_module, 'num_heads'):
                num_heads = attn_module.num_heads
            else:
                num_heads = 1

            d_model = W_q.shape[0]
            d_head = d_model // num_heads

            # Split into heads and create operators
            for head_idx in range(num_heads):
                start = head_idx * d_head
                end = (head_idx + 1) * d_head

                Q_head = W_q[start:end, :]
                K_head = W_k[start:end, :]
                V_head = W_v[start:end, :]

                # Create operator: O = Q @ K^T (attention pattern generator)
                # This captures how the head relates queries to keys
                operator = torch.matmul(Q_head, K_head.T)

                self.attention_operators[(layer_idx, head_idx)] = operator

            # Create layer-level operator (average over heads)
            layer_op = torch.mean(torch.stack([
                self.attention_operators[(layer_idx, h)]
                for h in range(num_heads)
            ]), dim=0)

            self.layer_operators.append(layer_op)

    def _extract_from_activations(self, input_ids: torch.Tensor) -> None:
        """
        Extract operators from actual forward pass activations

        This captures the INPUT-DEPENDENT gauge field structure.
        """
        # Hook to capture attention weights
        attention_weights = {}

        def hook_fn(module, input, output, layer_name):
            if isinstance(output, tuple):
                # (attention_output, attention_weights)
                if len(output) > 1:
                    attention_weights[layer_name] = output[1]

        # Register hooks
        hooks = []
        for name, module in self.model.named_modules():
            if 'attention' in name.lower():
                hook = module.register_forward_hook(
                    lambda m, i, o, n=name: hook_fn(m, i, o, n)
                )
                hooks.append(hook)

        # Forward pass
        with torch.no_grad():
            _ = self.model(input_ids, output_attentions=True)

        # Remove hooks
        for hook in hooks:
            hook.remove()

        # Convert attention weights to operators
        for layer_idx, (layer_name, attn_weights) in enumerate(attention_weights.items()):
            # attn_weights: (batch, num_heads, seq_len, seq_len)
            batch_size, num_heads, seq_len, _ = attn_weights.shape

            # Use first batch item
            attn = attn_weights[0]  # (num_heads, seq_len, seq_len)

            for head_idx in range(num_heads):
                # Attention matrix for this head
                A = attn[head_idx]  # (seq_len, seq_len)

                # Treat as Lie algebra element (remove identity)
                operator = A - torch.eye(seq_len, device=A.device)

                self.attention_operators[(layer_idx, head_idx)] = operator

            # Layer operator (average over heads)
            layer_op = torch.mean(attn, dim=0) - torch.eye(seq_len, device=attn.device)
            self.layer_operators.append(layer_op)

    def compute_curvature_field(self) -> torch.Tensor:
        """
        Compute full curvature tensor F_ij for all attention heads

        Returns:
            Curvature field tensor
        """
        if not self.layer_operators:
            raise ValueError("Must call extract_attention_operators first")

        F_field = self.curvature.compute_full_field(self.layer_operators)
        return F_field

    def compute_bch_plaquettes(self, max_order: int = 4) -> Dict[str, float]:
        """
        Compute BCH plaquettes showing compositional structure

        Plaquettes reveal how attention heads compose beyond simple addition.

        Returns:
            Dictionary mapping plaquette descriptions to strengths
        """
        plaquettes = {}

        n_layers = len(self.layer_operators)

        # Compute triangular plaquettes
        for i in range(n_layers - 2):
            for j in range(i + 1, n_layers - 1):
                for k in range(j + 1, n_layers):
                    loop = [i, j, k]
                    strength = self.bch.plaquette_strength(
                        self.layer_operators, loop
                    )
                    plaquettes[f"triangle_{i}_{j}_{k}"] = strength

        # Compute rectangular plaquettes
        for i in range(n_layers - 3):
            for j in range(i + 1, n_layers - 2):
                for k in range(j + 1, n_layers - 1):
                    for l in range(k + 1, n_layers):
                        loop = [i, j, k, l]
                        strength = self.bch.plaquette_strength(
                            self.layer_operators, loop
                        )
                        plaquettes[f"square_{i}_{j}_{k}_{l}"] = strength

        return plaquettes

    def compute_wilson_loops(self, max_length: int = 4) -> Dict[Tuple[int, ...], float]:
        """
        Compute Wilson loops for all reasoning paths

        Wilson loops measure path-dependent reasoning:
        - Does the order of layers matter?
        - Are there preferred reasoning paths?
        - How much curvature do we enclose?

        Returns:
            Dictionary mapping paths to loop strengths
        """
        loops = self.wilson.all_loops(self.layer_operators, max_length)
        return loops

    def detect_abelian_collapse(self, threshold: float = 1e-4) -> List[Tuple[int, int]]:
        """
        Detect attention heads that have collapsed to abelian (commuting)

        Abelian collapse indicates LINEAR reasoning - usually bad!

        Returns:
            List of (layer, head) pairs that are approximately abelian
        """
        abelian_heads = []

        layers = list(set(k[0] for k in self.attention_operators.keys()))

        for layer_idx in layers:
            heads = [k[1] for k in self.attention_operators.keys()
                    if k[0] == layer_idx]

            # Check all pairs of heads in this layer
            for i, head_i in enumerate(heads):
                for head_j in heads[i + 1:]:
                    op_i = self.attention_operators[(layer_idx, head_i)]
                    op_j = self.attention_operators[(layer_idx, head_j)]

                    if self.commutator.is_abelian(op_i, op_j, tol=threshold):
                        abelian_heads.append((layer_idx, head_i))
                        abelian_heads.append((layer_idx, head_j))

        return list(set(abelian_heads))

    def compute_jacobiator_field(self) -> torch.Tensor:
        """
        Compute Jacobiator for all head triples

        Reveals hierarchical reasoning structure.

        Returns:
            Jacobiator field tensor
        """
        J_field = self.jacobiator.compute_all_triangles(self.layer_operators)
        return J_field

    def find_reasoning_chains(self, min_strength: float = 0.5) -> List[List[int]]:
        """
        Find dominant reasoning chains via Wilson loop analysis

        Reasoning chains are paths with high curvature (strong loops).

        Args:
            min_strength: Minimum loop strength to consider

        Returns:
            List of reasoning paths (sequences of layer indices)
        """
        loops = self.compute_wilson_loops(max_length=6)

        # Filter strong loops
        strong_loops = [
            list(path) for path, strength in loops.items()
            if abs(strength) > min_strength
        ]

        # Remove duplicates (same path, different starting point)
        unique_chains = []
        for chain in strong_loops:
            # Normalize to start with minimum index
            min_idx = chain.index(min(chain))
            normalized = chain[min_idx:] + chain[:min_idx]

            if normalized not in unique_chains:
                unique_chains.append(normalized)

        return unique_chains

    def compute_homotopy_classes(self) -> Dict[int, List[List[int]]]:
        """
        Group reasoning paths into homotopy equivalence classes

        Paths in the same class can be continuously deformed into each other.
        They represent "equivalent reasoning strategies".

        Returns:
            Dictionary mapping class ID to list of equivalent paths
        """
        chains = self.find_reasoning_chains(min_strength=0.3)

        classes = {}
        class_id = 0

        for chain in chains:
            # Check if homotopic to any existing class
            found_class = False

            for cid, class_chains in classes.items():
                representative = class_chains[0]

                if self.homotopy.homotopy_equivalence(
                    chain, representative, self.layer_operators, tol=0.1
                ):
                    classes[cid].append(chain)
                    found_class = True
                    break

            # New class
            if not found_class:
                classes[class_id] = [chain]
                class_id += 1

        return classes

    def compute_stability_score(self) -> float:
        """
        Compute overall stability score from homotopy invariants

        High stability = robust reasoning patterns
        Low stability = brittle, input-sensitive reasoning

        Returns:
            Stability score in [0, 1]
        """
        # Compute Chern number (topological invariant)
        F_field = self.compute_curvature_field()
        chern = abs(self.homotopy.compute_chern_number(F_field))

        # Compute ratio of non-abelian to total heads
        abelian_heads = self.detect_abelian_collapse()
        total_heads = len(self.attention_operators)
        non_abelian_ratio = 1.0 - (len(abelian_heads) / total_heads) if total_heads > 0 else 0

        # Number of homotopy classes (more = more diverse strategies)
        homotopy_classes = self.compute_homotopy_classes()
        n_classes = len(homotopy_classes)

        # Stability = combination of topological invariance and diversity
        stability = (0.3 * min(chern, 1.0) +
                    0.4 * non_abelian_ratio +
                    0.3 * min(n_classes / 5.0, 1.0))

        return stability

    def full_analysis(self,
                     input_ids: Optional[torch.Tensor] = None,
                     extract_mode: str = 'weights') -> TransformerGaugeAnalysis:
        """
        Perform complete gauge-theoretic analysis

        Args:
            input_ids: Input tokens (optional, for activation-based analysis)
            extract_mode: 'weights' or 'activations'

        Returns:
            Complete analysis results
        """
        print("🔬 Extracting gauge field operators...")
        self.extract_attention_operators(input_ids, extract_mode)

        print("📐 Computing curvature field...")
        F_field = self.compute_curvature_field()
        total_curvature = torch.sum(torch.abs(F_field)).item()
        ricci_scalar = self.curvature.ricci_scalar(F_field).item()

        print("🔺 Computing BCH plaquettes...")
        plaquettes = self.compute_bch_plaquettes()

        print("➰ Computing Wilson loops...")
        wilson_loops = self.compute_wilson_loops()

        print("🎯 Detecting abelian collapse...")
        abelian_heads = self.detect_abelian_collapse()

        print("🧬 Finding reasoning chains...")
        reasoning_paths = self.find_reasoning_chains()

        print("🌀 Computing homotopy invariants...")
        chern_number = self.homotopy.compute_chern_number(F_field)

        print("💎 Computing stability score...")
        stability = self.compute_stability_score()

        # Per-layer analysis
        attention_analyses = []
        for (layer_idx, head_idx), operator in self.attention_operators.items():
            # Compute commutators with other heads in same layer
            same_layer_heads = [
                (l, h) for (l, h) in self.attention_operators.keys()
                if l == layer_idx and h != head_idx
            ]

            commutator_strengths = {}
            for (_, other_head_idx) in same_layer_heads:
                other_op = self.attention_operators[(layer_idx, other_head_idx)]
                strength = self.commutator.norm(operator, other_op).item()
                commutator_strengths[other_head_idx] = strength

            # Check abelian collapse
            abelian_collapse = (layer_idx, head_idx) in abelian_heads

            # Jacobiator (if enough heads)
            if len(same_layer_heads) >= 2:
                op1 = self.attention_operators[same_layer_heads[0]]
                op2 = self.attention_operators[same_layer_heads[1]]
                jacobiator_norm = self.jacobiator.norm(operator, op1, op2).item()
            else:
                jacobiator_norm = 0.0

            analysis = AttentionAnalysis(
                layer_idx=layer_idx,
                head_idx=head_idx,
                curvature_norm=torch.linalg.matrix_norm(operator, ord='fro').item(),
                commutator_strengths=commutator_strengths,
                jacobiator_norm=jacobiator_norm,
                reasoning_loops=[],  # Populated below
                abelian_collapse=abelian_collapse,
                homotopy_class=0  # Populated below
            )

            attention_analyses.append(analysis)

        # Compute interpretability metrics
        interpretability_metrics = {
            'curvature_per_layer': total_curvature / len(self.layer_operators),
            'non_abelian_ratio': 1.0 - len(abelian_heads) / len(self.attention_operators),
            'avg_plaquette_strength': np.mean(list(plaquettes.values())),
            'reasoning_chain_diversity': len(reasoning_paths),
            'topological_charge': chern_number
        }

        total_heads = len(self.attention_operators)
        non_abelian_measure = 1.0 - (len(abelian_heads) / total_heads) if total_heads > 0 else 0

        result = TransformerGaugeAnalysis(
            model_name=self.model.__class__.__name__,
            total_curvature=total_curvature,
            ricci_scalar=ricci_scalar,
            chern_number=chern_number,
            non_abelian_measure=non_abelian_measure,
            attention_analyses=attention_analyses,
            bch_plaquettes=plaquettes,
            wilson_loops=wilson_loops,
            reasoning_paths=reasoning_paths,
            stability_score=stability,
            interpretability_metrics=interpretability_metrics
        )

        print("\n✅ Analysis complete!")
        return result

    def explain_prediction(self,
                          input_ids: torch.Tensor,
                          output_token_idx: int) -> Dict[str, Any]:
        """
        Explain a specific prediction using gauge theory

        Shows which reasoning paths led to the output.

        Args:
            input_ids: Input tokens
            output_token_idx: Output token to explain

        Returns:
            Explanation dictionary with reasoning paths and contributions
        """
        # Extract activation-based operators
        self.extract_attention_operators(input_ids, extract_mode='activations')

        # Compute Wilson loops from input to output
        n_layers = len(self.layer_operators)
        paths_to_output = []

        # All paths from layer 0 to final layer
        for path_length in range(2, min(6, n_layers + 1)):
            loops = self.wilson.all_loops(self.layer_operators[:path_length + 1],
                                         max_length=path_length)

            for path, strength in loops.items():
                if path[-2] == n_layers - 1:  # Ends at final layer
                    paths_to_output.append({
                        'path': path,
                        'strength': strength,
                        'interpretation': self._interpret_path(path)
                    })

        # Sort by strength
        paths_to_output.sort(key=lambda x: abs(x['strength']), reverse=True)

        explanation = {
            'dominant_paths': paths_to_output[:5],
            'curvature_contribution': self._compute_path_curvature(paths_to_output[0]['path']),
            'non_linearity_score': self._compute_non_linearity(paths_to_output[0]['path']),
            'reasoning_type': self._classify_reasoning(paths_to_output[0])
        }

        return explanation

    def _interpret_path(self, path: Tuple[int, ...]) -> str:
        """Generate human-readable interpretation of reasoning path"""
        if len(path) <= 3:
            return "Direct reasoning (few layers)"
        elif len(set(path)) < len(path) * 0.5:
            return "Recursive reasoning (revisiting layers)"
        else:
            return "Linear reasoning (sequential layers)"

    def _compute_path_curvature(self, path: Tuple[int, ...]) -> float:
        """Compute total curvature along path"""
        total_curv = 0.0
        for i in range(len(path) - 1):
            if path[i] < len(self.layer_operators) and path[i+1] < len(self.layer_operators):
                F_ij = self.commutator.compute(
                    self.layer_operators[path[i]],
                    self.layer_operators[path[i + 1]]
                )
                total_curv += torch.linalg.matrix_norm(F_ij, ord='fro').item()
        return total_curv

    def _compute_non_linearity(self, path: Tuple[int, ...]) -> float:
        """Measure non-linearity of reasoning path"""
        # Compare forward and backward paths
        if len(path) < 3:
            return 0.0

        forward = list(path)
        backward = list(reversed(path))

        Z_forward = self.layer_operators[forward[0]]
        for idx in forward[1:]:
            if idx < len(self.layer_operators):
                Z_forward = self.bch.compute(Z_forward, self.layer_operators[idx])

        Z_backward = self.layer_operators[backward[0]]
        for idx in backward[1:]:
            if idx < len(self.layer_operators):
                Z_backward = self.bch.compute(Z_backward, self.layer_operators[idx])

        diff = torch.linalg.matrix_norm(Z_forward - Z_backward, ord='fro').item()
        return diff

    def _classify_reasoning(self, path_info: Dict) -> str:
        """Classify type of reasoning based on gauge properties"""
        strength = abs(path_info['strength'])
        path = path_info['path']

        if strength < 0.1:
            return "Weak/Linear reasoning"
        elif len(set(path)) < len(path) * 0.7:
            return "Recursive/Iterative reasoning"
        elif strength > 1.0:
            return "Strong non-linear reasoning"
        else:
            return "Moderate compositional reasoning"


__all__ = ['TransformerGaugeAnalyzer', 'TransformerGaugeAnalysis', 'AttentionAnalysis']
