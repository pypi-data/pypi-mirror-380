from .datasets import anscombe
from .plots    import add_min_max_colorbar
from .plots    import barcode_plot
from .plots    import bar_chart
from .plots    import density_plot
from .plots    import galaxy_plot
from .plots    import histogram_plot
from .plots    import line_plot
from .plots    import pareto_chart
from .plots    import quartile_plot
from .plots    import rug_plot
from .plots    import scatter_plot
from .plots    import sparkline
from .plots    import stem_and_leaf_plot
from .plots    import time_series        
from .styles   import apply_tufte_style

# Public API in alphabetical order
__all__ = ["add_min_max_colorbar",
           "anscombe",
           "apply_tufte_style",
           "barcode_plot",
           "bar_chart",
           "density_plot",
           "histogram_plot",
           "galaxy_plot",
           "line_plot",
           "pareto_chart",
           "quartile_plot",
           "rug_plot",
           "scatter_plot",
           "sparkline",
           "stem_and_leaf_plot",
           "time_series"]
