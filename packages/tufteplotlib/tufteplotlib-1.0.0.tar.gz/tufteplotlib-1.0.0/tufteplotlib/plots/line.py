import matplotlib.pyplot as plt
from tufteplotlib.styles import apply_tufte_style
from tufteplotlib.utils import _intermediate_ticks
import numpy as np

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def line_plot(x, y, ax=None):
    """
    Plot a line defined by a 2-dimensional data set. Best used for functions, or dense time series
    data.

    Parameters
    ----------
    x : array-like
        x-values of the line.
    y : array-like
        y-values of the line.
    ax: Optional axis

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    """

    if ax is None:
        fig, ax = plt.subplots(figsize=(4*1.618, 2))
    else:
        fig = ax.figure

    x = np.asarray(x)
    y = np.asarray(y)

    # Draw the line with default styling
    ax.plot(x, y, color='black', linewidth=1.0, alpha=1.0)

    # Compute exact min/max and margin
    xmin, xmax = x.min(), x.max()
    ymin, ymax = y.min(), y.max()
    x_range = xmax - xmin
    y_range = ymax - ymin
    margin = 0.05
    ax.set_xlim(xmin - margin*x_range, xmax + margin*x_range)
    ax.set_ylim(ymin - margin*y_range, ymax + margin*y_range)

    # Apply Tufte minimal style
    apply_tufte_style(ax)

    # Force spines to match min/max
    ax.spines['bottom'].set_bounds(xmin, xmax)
    ax.spines['left'].set_bounds(ymin, ymax)

    # Set nicely rounded ticks including min/max
    ax.set_xticks(_intermediate_ticks(xmin, xmax, max_ticks=5))
    ax.set_yticks(_intermediate_ticks(ymin, ymax, max_ticks=5))

    return fig, ax

####################################################################################################
#                                          Test / example code                                     #
####################################################################################################
def main():
    t = np.linspace(0, 10, 200)
    y = np.sin(t)
    y_noisy = y + np.random.normal(0, 0.1, size=t.shape)

    fig, ax = line_plot(t, y_noisy)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
