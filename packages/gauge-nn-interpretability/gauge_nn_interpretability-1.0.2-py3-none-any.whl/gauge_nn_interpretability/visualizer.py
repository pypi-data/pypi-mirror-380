"""
Gauge Theory Visualization System
==================================

Visualizes gauge-theoretic properties of neural networks:
- Curvature fields
- BCH plaquettes
- Wilson loops
- Reasoning paths

Author: Michael J. Pendleton
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.collections import LineCollection
import networkx as nx
from typing import List, Dict, Tuple, Optional
import torch

from .transformer_analyzer import TransformerGaugeAnalysis, AttentionAnalysis


class GaugeVisualizer:
    """
    Visualizes gauge-theoretic analysis results

    Creates publication-quality visualizations showing:
    1. Curvature field heatmaps
    2. BCH plaquette diagrams
    3. Wilson loop networks
    4. Reasoning path flows
    """

    def __init__(self, figsize: Tuple[int, int] = (16, 12), dpi: int = 150):
        """
        Args:
            figsize: Figure size in inches
            dpi: Resolution
        """
        self.figsize = figsize
        self.dpi = dpi

        # Color schemes
        self.curvature_cmap = 'viridis'
        self.plaquette_cmap = 'plasma'
        self.loop_cmap = 'coolwarm'

    def plot_full_analysis(self,
                          analysis: TransformerGaugeAnalysis,
                          save_path: Optional[str] = None) -> plt.Figure:
        """
        Create comprehensive visualization of gauge analysis

        Args:
            analysis: Complete gauge analysis results
            save_path: Optional path to save figure

        Returns:
            Matplotlib figure
        """
        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)

        # Create grid layout
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

        # 1. Overview metrics
        ax1 = fig.add_subplot(gs[0, :])
        self._plot_overview_metrics(ax1, analysis)

        # 2. Curvature field heatmap
        ax2 = fig.add_subplot(gs[1, 0])
        self._plot_curvature_field(ax2, analysis)

        # 3. BCH plaquettes network
        ax3 = fig.add_subplot(gs[1, 1])
        self._plot_bch_plaquettes(ax3, analysis)

        # 4. Wilson loops
        ax4 = fig.add_subplot(gs[1, 2])
        self._plot_wilson_loops(ax4, analysis)

        # 5. Attention head structure
        ax5 = fig.add_subplot(gs[2, 0:2])
        self._plot_attention_structure(ax5, analysis)

        # 6. Reasoning paths
        ax6 = fig.add_subplot(gs[2, 2])
        self._plot_reasoning_paths(ax6, analysis)

        # Main title
        fig.suptitle(
            f'Gauge-Theoretic Analysis: {analysis.model_name}\n'
            f'Non-Abelian Measure: {analysis.non_abelian_measure:.3f} | '
            f'Stability: {analysis.stability_score:.3f} | '
            f'Chern #: {analysis.chern_number:.3f}',
            fontsize=16, fontweight='bold'
        )

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=self.dpi, bbox_inches='tight')
            print(f"💾 Saved visualization to {save_path}")

        return fig

    def _plot_overview_metrics(self, ax: plt.Axes,
                               analysis: TransformerGaugeAnalysis) -> None:
        """Plot overview bar chart of key metrics"""
        metrics = {
            'Total\nCurvature': analysis.total_curvature,
            'Ricci\nScalar': analysis.ricci_scalar,
            'Non-Abelian\nMeasure': analysis.non_abelian_measure * 100,
            'Stability\nScore': analysis.stability_score * 100,
            'Reasoning\nChains': len(analysis.reasoning_paths),
            'Plaquette\nStrength': np.mean(list(analysis.bch_plaquettes.values())) if analysis.bch_plaquettes else 0
        }

        # Normalize for visualization
        max_val = max(metrics.values())
        normalized = {k: v / max_val for k, v in metrics.items()}

        bars = ax.barh(list(normalized.keys()), list(normalized.values()),
                      color=plt.cm.viridis(np.linspace(0.3, 0.9, len(metrics))))

        # Add value labels
        for i, (bar, (k, v)) in enumerate(zip(bars, metrics.items())):
            ax.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height() / 2,
                   f'{v:.2f}', va='center', fontsize=9, fontweight='bold')

        ax.set_xlim(0, 1.2)
        ax.set_xlabel('Normalized Value', fontsize=11, fontweight='bold')
        ax.set_title('Key Gauge-Theoretic Metrics', fontsize=12, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)
        ax.set_axisbelow(True)

    def _plot_curvature_field(self, ax: plt.Axes,
                              analysis: TransformerGaugeAnalysis) -> None:
        """Plot curvature field as heatmap"""
        # Extract layer-wise curvature
        n_layers = len(set(a.layer_idx for a in analysis.attention_analyses))

        # Create curvature matrix
        curvature_matrix = np.zeros((n_layers, n_layers))

        for attention_analysis in analysis.attention_analyses:
            layer = attention_analysis.layer_idx
            if layer < n_layers:
                for other_layer, strength in attention_analysis.commutator_strengths.items():
                    if other_layer < n_layers:
                        curvature_matrix[layer, other_layer] = strength

        # Make symmetric
        curvature_matrix = curvature_matrix + curvature_matrix.T

        # Plot heatmap
        im = ax.imshow(curvature_matrix, cmap=self.curvature_cmap,
                      aspect='auto', interpolation='nearest')

        ax.set_xlabel('Layer Index', fontsize=10, fontweight='bold')
        ax.set_ylabel('Layer Index', fontsize=10, fontweight='bold')
        ax.set_title('Curvature Field F_ij\n(Non-Commutativity)', fontsize=11, fontweight='bold')

        # Colorbar
        cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        cbar.set_label('||[A_i, A_j]||', rotation=270, labelpad=15, fontsize=9)

        # Grid
        ax.set_xticks(range(n_layers))
        ax.set_yticks(range(n_layers))
        ax.grid(False)

    def _plot_bch_plaquettes(self, ax: plt.Axes,
                            analysis: TransformerGaugeAnalysis) -> None:
        """Plot BCH plaquettes as network diagram"""
        # Create graph
        G = nx.Graph()

        # Extract nodes (layers)
        layers = set()
        for plaq_name, strength in analysis.bch_plaquettes.items():
            if 'triangle' in plaq_name:
                _, i, j, k = plaq_name.split('_')
                layers.update([int(i), int(j), int(k)])

                # Add edges with weights
                G.add_edge(int(i), int(j), weight=strength)
                G.add_edge(int(j), int(k), weight=strength)
                G.add_edge(int(k), int(i), weight=strength)

        if not G.nodes():
            ax.text(0.5, 0.5, 'No plaquettes computed', ha='center', va='center',
                   transform=ax.transAxes, fontsize=10, style='italic')
            ax.axis('off')
            return

        # Layout
        pos = nx.spring_layout(G, seed=42, k=2)

        # Draw nodes
        node_colors = plt.cm.plasma(np.linspace(0.2, 0.8, len(G.nodes())))
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors,
                              node_size=800, alpha=0.9)

        # Draw edges with varying thickness
        edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
        max_weight = max(edge_weights) if edge_weights else 1.0
        edge_widths = [3 * (w / max_weight) for w in edge_weights]

        nx.draw_networkx_edges(G, pos, ax=ax, width=edge_widths,
                              alpha=0.6, edge_color='gray')

        # Labels
        nx.draw_networkx_labels(G, pos, ax=ax, font_size=10,
                               font_weight='bold', font_color='white')

        ax.set_title('BCH Plaquettes\n(Compositional Structure)', fontsize=11, fontweight='bold')
        ax.axis('off')

    def _plot_wilson_loops(self, ax: plt.Axes,
                          analysis: TransformerGaugeAnalysis) -> None:
        """Plot Wilson loop strengths"""
        if not analysis.wilson_loops:
            ax.text(0.5, 0.5, 'No Wilson loops computed', ha='center', va='center',
                   transform=ax.transAxes, fontsize=10, style='italic')
            ax.axis('off')
            return

        # Sort by absolute strength
        sorted_loops = sorted(analysis.wilson_loops.items(),
                            key=lambda x: abs(x[1]), reverse=True)[:10]

        loop_names = [f"{path[0]}→{path[1]}→..." for path, _ in sorted_loops]
        strengths = [strength for _, strength in sorted_loops]

        # Color by sign
        colors = ['#e74c3c' if s < 0 else '#3498db' for s in strengths]

        bars = ax.barh(range(len(loop_names)), strengths, color=colors, alpha=0.7)

        ax.set_yticks(range(len(loop_names)))
        ax.set_yticklabels(loop_names, fontsize=8)
        ax.set_xlabel('tr(W(C))', fontsize=10, fontweight='bold')
        ax.set_title('Wilson Loops\n(Path Holonomy)', fontsize=11, fontweight='bold')
        ax.axvline(x=0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
        ax.grid(axis='x', alpha=0.3)

    def _plot_attention_structure(self, ax: plt.Axes,
                                  analysis: TransformerGaugeAnalysis) -> None:
        """Plot attention head structure colored by properties"""
        # Group by layer
        layers = {}
        for attn in analysis.attention_analyses:
            if attn.layer_idx not in layers:
                layers[attn.layer_idx] = []
            layers[attn.layer_idx].append(attn)

        n_layers = len(layers)
        max_heads = max(len(heads) for heads in layers.values())

        # Create scatter plot
        for layer_idx, heads in layers.items():
            for head_idx, head in enumerate(heads):
                # Position
                x = layer_idx
                y = head_idx

                # Size by curvature
                size = 200 + 800 * (head.curvature_norm / (max(h.curvature_norm for h in analysis.attention_analyses) + 1e-6))

                # Color by abelian collapse
                color = '#e74c3c' if head.abelian_collapse else '#2ecc71'

                # Alpha by Jacobiator
                max_jac = max(h.jacobiator_norm for h in analysis.attention_analyses)
                alpha = 0.3 + 0.7 * (head.jacobiator_norm / (max_jac + 1e-6))

                ax.scatter(x, y, s=size, c=color, alpha=alpha,
                          edgecolors='black', linewidths=1.5)

        ax.set_xlabel('Layer Index', fontsize=11, fontweight='bold')
        ax.set_ylabel('Head Index', fontsize=11, fontweight='bold')
        ax.set_title('Attention Head Structure\n'
                    '🟢 Non-Abelian (Good) | 🔴 Abelian Collapse (Bad)\n'
                    'Size ∝ Curvature | Opacity ∝ Jacobiator',
                    fontsize=11, fontweight='bold')
        ax.grid(True, alpha=0.3)

        ax.set_xticks(range(n_layers))
        ax.set_yticks(range(max_heads))

    def _plot_reasoning_paths(self, ax: plt.Axes,
                             analysis: TransformerGaugeAnalysis) -> None:
        """Plot reasoning paths as flow diagram"""
        if not analysis.reasoning_paths:
            ax.text(0.5, 0.5, 'No reasoning paths found', ha='center', va='center',
                   transform=ax.transAxes, fontsize=10, style='italic')
            ax.axis('off')
            return

        # Create directed graph
        G = nx.DiGraph()

        for path in analysis.reasoning_paths[:5]:  # Top 5 paths
            for i in range(len(path) - 1):
                if G.has_edge(path[i], path[i + 1]):
                    G[path[i]][path[i + 1]]['weight'] += 1
                else:
                    G.add_edge(path[i], path[i + 1], weight=1)

        if not G.nodes():
            ax.text(0.5, 0.5, 'No reasoning paths found', ha='center', va='center',
                   transform=ax.transAxes, fontsize=10, style='italic')
            ax.axis('off')
            return

        # Layout
        pos = nx.spring_layout(G, seed=42, k=1.5)

        # Draw
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color='#3498db',
                              node_size=600, alpha=0.8)

        # Edge weights
        edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
        max_weight = max(edge_weights)
        edge_widths = [2 + 4 * (w / max_weight) for w in edge_weights]

        nx.draw_networkx_edges(G, pos, ax=ax, width=edge_widths,
                              alpha=0.6, edge_color='gray',
                              arrows=True, arrowsize=15, arrowstyle='->')

        nx.draw_networkx_labels(G, pos, ax=ax, font_size=10,
                               font_weight='bold', font_color='white')

        ax.set_title('Reasoning Paths\n(High-Curvature Chains)', fontsize=11, fontweight='bold')
        ax.axis('off')

    def plot_curvature_evolution(self,
                                curvature_history: List[torch.Tensor],
                                save_path: Optional[str] = None) -> plt.Figure:
        """
        Plot evolution of curvature during training

        Args:
            curvature_history: List of curvature tensors over time
            save_path: Optional save path

        Returns:
            Figure
        """
        fig, axes = plt.subplots(2, 2, figsize=(12, 10), dpi=self.dpi)

        # Total curvature over time
        total_curv = [torch.sum(torch.abs(F)).item() for F in curvature_history]
        axes[0, 0].plot(total_curv, linewidth=2, color='#3498db')
        axes[0, 0].set_xlabel('Training Step', fontweight='bold')
        axes[0, 0].set_ylabel('Total Curvature', fontweight='bold')
        axes[0, 0].set_title('Curvature Evolution', fontweight='bold')
        axes[0, 0].grid(True, alpha=0.3)

        # Curvature heatmap at final step
        final_curv = curvature_history[-1]
        n = final_curv.shape[0]
        curv_matrix = torch.zeros(n, n)
        for i in range(n):
            for j in range(n):
                curv_matrix[i, j] = torch.linalg.matrix_norm(final_curv[i, j], ord='fro')

        im = axes[0, 1].imshow(curv_matrix.cpu().numpy(), cmap='viridis', aspect='auto')
        axes[0, 1].set_title('Final Curvature Field', fontweight='bold')
        axes[0, 1].set_xlabel('Layer i', fontweight='bold')
        axes[0, 1].set_ylabel('Layer j', fontweight='bold')
        plt.colorbar(im, ax=axes[0, 1])

        # Distribution of curvature values
        all_curvs = [curv_matrix[i, j].item()
                    for i in range(n) for j in range(n) if i != j]
        axes[1, 0].hist(all_curvs, bins=30, color='#2ecc71', alpha=0.7, edgecolor='black')
        axes[1, 0].set_xlabel('Curvature ||F_ij||', fontweight='bold')
        axes[1, 0].set_ylabel('Frequency', fontweight='bold')
        axes[1, 0].set_title('Curvature Distribution', fontweight='bold')
        axes[1, 0].grid(True, alpha=0.3, axis='y')

        # Variance over time (stability measure)
        curv_variance = [torch.var(torch.abs(F)).item() for F in curvature_history]
        axes[1, 1].plot(curv_variance, linewidth=2, color='#e74c3c')
        axes[1, 1].set_xlabel('Training Step', fontweight='bold')
        axes[1, 1].set_ylabel('Curvature Variance', fontweight='bold')
        axes[1, 1].set_title('Reasoning Stability', fontweight='bold')
        axes[1, 1].grid(True, alpha=0.3)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=self.dpi, bbox_inches='tight')

        return fig

    def export_interactive_html(self,
                               analysis: TransformerGaugeAnalysis,
                               output_path: str) -> None:
        """
        Export interactive HTML visualization

        Args:
            analysis: Analysis results
            output_path: Path to save HTML file
        """
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Gauge Theory Analysis - {analysis.model_name}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }}
        h1 {{
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .metrics {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        .metric-card {{
            background: rgba(255, 255, 255, 0.2);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.3s;
        }}
        .metric-card:hover {{
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.3);
        }}
        .metric-value {{
            font-size: 2em;
            font-weight: bold;
            margin: 10px 0;
        }}
        .metric-label {{
            font-size: 0.9em;
            opacity: 0.9;
        }}
        .explanation {{
            background: rgba(0, 0, 0, 0.3);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            line-height: 1.6;
        }}
        .status {{
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            margin: 5px;
        }}
        .status.good {{
            background: #2ecc71;
        }}
        .status.warning {{
            background: #f39c12;
        }}
        .status.bad {{
            background: #e74c3c;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔬 Gauge-Theoretic Analysis</h1>
        <h2 style="text-align: center; font-weight: normal; opacity: 0.9;">
            {analysis.model_name}
        </h2>

        <div class="metrics">
            <div class="metric-card">
                <div class="metric-label">Total Curvature</div>
                <div class="metric-value">{analysis.total_curvature:.2f}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Ricci Scalar</div>
                <div class="metric-value">{analysis.ricci_scalar:.2f}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Non-Abelian Measure</div>
                <div class="metric-value">{analysis.non_abelian_measure:.2%}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Stability Score</div>
                <div class="metric-value">{analysis.stability_score:.2%}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Chern Number</div>
                <div class="metric-value">{analysis.chern_number:.3f}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Reasoning Paths</div>
                <div class="metric-value">{len(analysis.reasoning_paths)}</div>
            </div>
        </div>

        <div class="explanation">
            <h3>📊 What These Metrics Mean</h3>
            <p><strong>Curvature:</strong> Measures non-linearity in reasoning. Higher = more complex, context-dependent thinking.</p>
            <p><strong>Ricci Scalar:</strong> Total "bending" of the reasoning space. Indicates overall complexity.</p>
            <p><strong>Non-Abelian Measure:</strong> Percentage of attention heads with non-commuting operations (good!).</p>
            <p><strong>Stability Score:</strong> Robustness of reasoning patterns. Higher = better generalization.</p>
            <p><strong>Chern Number:</strong> Topological invariant. Non-zero indicates non-trivial reasoning structure.</p>
            <p><strong>Reasoning Paths:</strong> Number of distinct high-curvature reasoning chains discovered.</p>
        </div>

        <div class="explanation">
            <h3>🎯 Model Assessment</h3>
            <p>
                {"<span class='status good'>✓ Strong Non-Linear Reasoning</span>" if analysis.non_abelian_measure > 0.7 else ""}
                {"<span class='status warning'>⚠ Moderate Linear Collapse</span>" if 0.3 <= analysis.non_abelian_measure <= 0.7 else ""}
                {"<span class='status bad'>✗ Severe Abelian Collapse</span>" if analysis.non_abelian_measure < 0.3 else ""}

                {"<span class='status good'>✓ High Stability</span>" if analysis.stability_score > 0.7 else ""}
                {"<span class='status warning'>⚠ Moderate Stability</span>" if 0.3 <= analysis.stability_score <= 0.7 else ""}
                {"<span class='status bad'>✗ Low Stability</span>" if analysis.stability_score < 0.3 else ""}

                {"<span class='status good'>✓ Rich Reasoning Structure</span>" if len(analysis.reasoning_paths) > 5 else ""}
                {"<span class='status warning'>⚠ Limited Reasoning Paths</span>" if 2 <= len(analysis.reasoning_paths) <= 5 else ""}
                {"<span class='status bad'>✗ Minimal Reasoning Diversity</span>" if len(analysis.reasoning_paths) < 2 else ""}
            </p>
        </div>

        <div class="explanation">
            <h3>💡 Recommendations</h3>
            <ul>
                {"<li>✓ Model shows strong non-abelian structure - good for complex reasoning tasks.</li>" if analysis.non_abelian_measure > 0.7 else "<li>⚠ Consider techniques to increase non-abelian structure (e.g., regularization on commutators).</li>"}
                {"<li>✓ High stability suggests robust generalization.</li>" if analysis.stability_score > 0.7 else "<li>⚠ Improve stability by training on more diverse data or using homotopy-based regularization.</li>"}
                {"<li>✓ Rich reasoning paths indicate versatile thinking.</li>" if len(analysis.reasoning_paths) > 5 else "<li>⚠ Limited reasoning paths may restrict model capability on complex tasks.</li>"}
            </ul>
        </div>

        <div class="explanation" style="text-align: center; font-size: 0.9em; opacity: 0.8;">
            <p>Generated by Gauge-Theoretic Neural Network Interpretability Framework</p>
            <p>Built by Michael J. Pendleton | The AI Cowboys</p>
            <p>george Washington University | Doctoral Candidate in AI/ML Engineering</p>
        </div>
    </div>
</body>
</html>
"""

        with open(output_path, 'w') as f:
            f.write(html_content)

        print(f"🌐 Exported interactive HTML to {output_path}")


__all__ = ['GaugeVisualizer']
