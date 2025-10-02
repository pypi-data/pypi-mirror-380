"""
Computational Gauge Theory for Neural Network Interpretability
==============================================================

A rigorous mathematical framework for understanding neural networks
as gauge fields, providing true interpretability with mathematical
guarantees.

Author: Michael J. Pendleton
Organization: The AI Cowboys / George Washington University
"""

from .gauge_operators import (
    CommutatorOperator,
    CurvatureOperator,
    JacobiatorOperator,
    BCHExpansion,
    WilsonLoop,
    HomotopyInvariant,
    GaugeFieldProperties
)

from .transformer_analyzer import (
    TransformerGaugeAnalyzer,
    TransformerGaugeAnalysis,
    AttentionAnalysis
)

from .visualizer import GaugeVisualizer

# Alias for convenience
GaugeAnalyzer = TransformerGaugeAnalyzer

__version__ = '1.0.3'
__author__ = 'Michael J. Pendleton'
__email__ = 'michael.pendleton.20@gmail.com'

__all__ = [
    'CommutatorOperator',
    'CurvatureOperator',
    'JacobiatorOperator',
    'BCHExpansion',
    'WilsonLoop',
    'HomotopyInvariant',
    'GaugeFieldProperties',
    'TransformerGaugeAnalyzer',
    'GaugeAnalyzer',  # Alias for TransformerGaugeAnalyzer
    'TransformerGaugeAnalysis',
    'AttentionAnalysis',
    'GaugeVisualizer'
]
