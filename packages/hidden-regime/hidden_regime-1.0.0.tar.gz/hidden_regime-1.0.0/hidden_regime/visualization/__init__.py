"""
Visualization utilities for hidden-regime package.

Provides consistent plotting functionality and styling across all components
including data loaders, HMM models, state standardizers, and technical indicators.
Features comprehensive charts for HMM vs indicators comparison and analysis.
"""

from .advanced_plots import (
    ComparisonPlotter,
    InteractivePlotter,
    PerformancePlotter,
    RegimePlotter,
    create_multi_asset_regime_comparison,
    create_regime_timeline_plot,
)
from .data_collection_plots import (
    DataCollectionVisualizationSuite,
)
from .indicators import (
    create_regime_transition_visualization,
    plot_hmm_vs_indicators_comparison,
    plot_indicator_performance_dashboard,
    plot_price_with_regimes_and_indicators,
)
from .plotting import (
    create_regime_legend,
    format_financial_axis,
    get_regime_colors,
    plot_regime_heatmap,
    plot_regime_statistics,
    plot_returns_with_regimes,
    setup_financial_plot_style,
)

__all__ = [
    # Core plotting functions
    "setup_financial_plot_style",
    "plot_returns_with_regimes",
    "plot_regime_heatmap",
    "plot_regime_statistics",
    "get_regime_colors",
    "format_financial_axis",
    "create_regime_legend",
    # Enhanced indicator visualizations
    "plot_price_with_regimes_and_indicators",
    "plot_hmm_vs_indicators_comparison",
    "plot_indicator_performance_dashboard",
    "create_regime_transition_visualization",
    # Advanced plotting classes
    "RegimePlotter",
    "PerformancePlotter",
    "ComparisonPlotter",
    "InteractivePlotter",
    # Utility plotting functions
    "create_regime_timeline_plot",
    "create_multi_asset_regime_comparison",
    # Data collection visualization
    "DataCollectionVisualizationSuite",
]
