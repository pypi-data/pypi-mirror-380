import numpy as np
import matplotlib.pyplot as plt
from tufteplotlib.styles import apply_tufte_style
from tufteplotlib.utils import _intermediate_ticks

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def scatter_plot(x, y, ax=None):
    """
    Plot individual observations between 2 data sets.

    Parameters
    ----------
    x, y : array-like
        Coordinates of the scatter points.
    ax : Optional axis.

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    """
     
    if ax is None:
        fig, ax = plt.subplots(figsize=(4*1.618, 4))
    else:
        fig = ax.figure

    x = np.asarray(x)
    y = np.asarray(y)

    # Plot scatter points
    ax.scatter(x, y, color='black', s=20, alpha=1.0)

    # Compute exact min/max
    xmin, xmax = x.min(), x.max()
    ymin, ymax = y.min(), y.max()
    x_range, y_range = xmax - xmin, ymax - ymin

    # Add small margin for axes limits
    margin = 0.05
    ax.set_xlim(xmin - margin * x_range, xmax + margin * x_range)
    ax.set_ylim(ymin - margin * y_range, ymax + margin * y_range)

    # Apply Tufte minimal style
    apply_tufte_style(ax)

    # Force spines to exactly match true min/max
    ax.spines['bottom'].set_bounds(xmin, xmax)
    ax.spines['left'].set_bounds(ymin, ymax)

    # Compute ticks including min/max and rounded interior ticks
    ax.set_xticks(_intermediate_ticks(xmin, xmax, max_ticks=5))
    ax.set_yticks(_intermediate_ticks(ymin, ymax, max_ticks=5))

    return fig, ax

####################################################################################################
#                                          Test / example code                                     #
####################################################################################################
def main():
    import random
    from tufteplotlib.datasets import anscombe

    # Pick a random dataset
    dataset = random.choice(list(anscombe.keys()))
    data = anscombe[dataset]

    # Split into x and y
    x, y = data[:, 0], data[:, 1]

    # Plot
    fig, ax = scatter_plot(x, y)
    ax.set_title(f"Anscombe's Quartet: {dataset}")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
