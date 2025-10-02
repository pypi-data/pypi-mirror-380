"""
Command-Line Interface for Gauge Neural Network Interpretability

Usage:
    gauge-analyze <model_name> [options]
    gauge-analyze --help
"""

import argparse
import sys
import os
from pathlib import Path

import torch
from transformers import AutoModel, AutoTokenizer

from .transformer_analyzer import TransformerGaugeAnalyzer
from .visualizer import GaugeVisualizer


def main():
    """Main CLI entry point"""

    parser = argparse.ArgumentParser(
        description='Analyze neural networks using computational gauge theory',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze BERT model
  gauge-analyze bert-base-uncased

  # Analyze with custom output
  gauge-analyze bert-base-uncased --output my_analysis

  # Analyze with specific text input
  gauge-analyze bert-base-uncased --text "Your text here" --mode activations

  # Quick analysis (faster, less detailed)
  gauge-analyze bert-base-uncased --quick

Author: Michael J. Pendleton (michael.pendleton.20@gmail.com)
Organization: The AI Cowboys / George Washington University
        """
    )

    # Required arguments
    parser.add_argument(
        'model_name',
        type=str,
        help='HuggingFace model name or path to local model'
    )

    # Optional arguments
    parser.add_argument(
        '--output', '-o',
        type=str,
        default='gauge_analysis',
        help='Output file prefix (default: gauge_analysis)'
    )

    parser.add_argument(
        '--mode', '-m',
        type=str,
        choices=['weights', 'activations'],
        default='weights',
        help='Analysis mode: weights (fast) or activations (input-specific)'
    )

    parser.add_argument(
        '--text', '-t',
        type=str,
        default=None,
        help='Text input for activation-based analysis'
    )

    parser.add_argument(
        '--quick', '-q',
        action='store_true',
        help='Quick analysis (skip some computations for speed)'
    )

    parser.add_argument(
        '--no-viz',
        action='store_true',
        help='Skip visualization generation'
    )

    parser.add_argument(
        '--no-html',
        action='store_true',
        help='Skip HTML report generation'
    )

    parser.add_argument(
        '--device',
        type=str,
        default='cpu',
        choices=['cpu', 'cuda', 'mps'],
        help='Device to use for computation'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )

    args = parser.parse_args()

    # Print header
    print("="*80)
    print("GAUGE-THEORETIC NEURAL NETWORK ANALYSIS")
    print("="*80)
    print(f"\nModel: {args.model_name}")
    print(f"Mode: {args.mode}")
    print(f"Device: {args.device}")
    print(f"Output: {args.output}.*")

    # Load model
    try:
        print(f"\n📦 Loading model '{args.model_name}'...")
        model = AutoModel.from_pretrained(args.model_name)
        print("✅ Model loaded successfully")

        # Load tokenizer if needed
        if args.mode == 'activations' or args.text:
            tokenizer = AutoTokenizer.from_pretrained(args.model_name)
            print("✅ Tokenizer loaded")
    except Exception as e:
        print(f"\n❌ Error loading model: {e}")
        print("\nTroubleshooting:")
        print("  1. Check model name spelling")
        print("  2. Ensure internet connection (for downloading)")
        print("  3. Try a different model (e.g., 'distilbert-base-uncased')")
        sys.exit(1)

    # Prepare input if needed
    input_ids = None
    if args.mode == 'activations':
        if args.text:
            text = args.text
        else:
            text = "This is a sample text for gauge-theoretic analysis of neural network reasoning."

        print(f"\n📝 Input text: \"{text[:60]}...\"")
        input_ids = tokenizer(text, return_tensors='pt')['input_ids']

    # Create analyzer
    print(f"\n🔬 Initializing gauge-theoretic analyzer...")
    analyzer = TransformerGaugeAnalyzer(model, device=args.device)

    # Run analysis
    print(f"\n⚙️  Running full analysis...")
    print("   (This may take 1-2 minutes for large models)")

    try:
        analysis = analyzer.full_analysis(
            input_ids=input_ids,
            extract_mode=args.mode
        )
        print("✅ Analysis complete!")
    except Exception as e:
        print(f"\n❌ Analysis failed: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

    # Print results
    print("\n" + "="*80)
    print("ANALYSIS RESULTS")
    print("="*80)

    print(f"\n📊 Overall Metrics:")
    print(f"  Model:              {analysis.model_name}")
    print(f"  Total Curvature:    {analysis.total_curvature:.2f}")
    print(f"  Ricci Scalar:       {analysis.ricci_scalar:.2f}")
    print(f"  Non-Abelian:        {analysis.non_abelian_measure:.2%}")
    print(f"  Stability Score:    {analysis.stability_score:.2%}")
    print(f"  Chern Number:       {analysis.chern_number:.6f}")
    print(f"  Reasoning Paths:    {len(analysis.reasoning_paths)}")

    # Assessment
    print(f"\n🎯 Model Assessment:")

    if analysis.non_abelian_measure > 0.7:
        print("  ✅ Strong non-linear reasoning structure")
    elif analysis.non_abelian_measure > 0.4:
        print("  ⚠️  Moderate non-linear structure")
    else:
        print("  ❌ WARNING: Significant abelian collapse detected")
        print("     → Model has become mostly linear (bad!)")

    if analysis.stability_score > 0.7:
        print("  ✅ High stability - excellent generalization expected")
    elif analysis.stability_score > 0.4:
        print("  ⚠️  Moderate stability")
    else:
        print("  ❌ WARNING: Low stability - may not generalize well")

    if len(analysis.reasoning_paths) > 5:
        print(f"  ✅ Rich reasoning structure ({len(analysis.reasoning_paths)} paths)")
    else:
        print(f"  ⚠️  Limited reasoning diversity ({len(analysis.reasoning_paths)} paths)")

    # Abelian collapse detection
    abelian_heads = analyzer.detect_abelian_collapse()
    total_heads = len(analysis.attention_analyses)
    abelian_pct = len(abelian_heads) / total_heads * 100 if total_heads > 0 else 0

    print(f"\n📐 Attention Heads:")
    print(f"  Total heads:        {total_heads}")
    print(f"  Abelian (linear):   {len(abelian_heads)} ({abelian_pct:.1f}%)")
    print(f"  Non-abelian:        {total_heads - len(abelian_heads)} ({100-abelian_pct:.1f}%)")

    if abelian_pct > 50:
        print("  ⚠️  WARNING: Over half of heads are abelian!")

    # Visualizations
    if not args.no_viz:
        print(f"\n📊 Generating visualizations...")
        try:
            viz = GaugeVisualizer()

            viz_path = f"{args.output}.png"
            viz.plot_full_analysis(analysis, save_path=viz_path)
            print(f"  ✅ Saved visualization: {viz_path}")
        except Exception as e:
            print(f"  ⚠️  Visualization failed: {e}")

    # HTML report
    if not args.no_html:
        print(f"\n🌐 Generating interactive HTML report...")
        try:
            viz = GaugeVisualizer()
            html_path = f"{args.output}.html"
            viz.export_interactive_html(analysis, html_path)
            print(f"  ✅ Saved HTML report: {html_path}")
        except Exception as e:
            print(f"  ⚠️  HTML generation failed: {e}")

    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)

    print(f"\n📁 Generated files:")
    if not args.no_viz and os.path.exists(f"{args.output}.png"):
        print(f"  • {args.output}.png - Comprehensive visualization")
    if not args.no_html and os.path.exists(f"{args.output}.html"):
        print(f"  • {args.output}.html - Interactive report (open in browser)")

    print(f"\n💡 Interpretation:")
    print(f"  Your model shows {analysis.non_abelian_measure:.0%} non-abelian structure,")
    print(f"  meaning {analysis.non_abelian_measure:.0%} of reasoning is non-linear.")

    if analysis.stability_score > 0.6:
        print(f"  Stability score of {analysis.stability_score:.0%} suggests good generalization.")
    else:
        print(f"  Stability score of {analysis.stability_score:.0%} suggests caution.")

    print(f"\n📚 Next steps:")
    print(f"  • Open {args.output}.html in your browser for detailed analysis")
    print(f"  • Compare with other models using the same command")
    print(f"  • Read docs/MATHEMATICAL_FOUNDATION.md for theory")

    print("\n" + "="*80)
    print("Analysis complete! The black box is broken. 🎉")
    print("="*80)


if __name__ == '__main__':
    main()
