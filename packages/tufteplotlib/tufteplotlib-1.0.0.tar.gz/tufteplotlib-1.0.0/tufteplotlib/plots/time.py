import matplotlib.pyplot as plt
from tufteplotlib.styles import apply_tufte_style
from tufteplotlib.utils import _intermediate_ticks
import numpy as np

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def time_series(x, y, ax=None):
    """
    Show the change in a value across individual observations, or time. Best used for sparse data.
    For dense data, consider using a line plot.
    
    Parameters
    ----------
    x, y : array-like
        Data points.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on. If None, a new figure is created.

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    """
    x = np.asarray(x)
    y = np.asarray(y)

    if ax is None:
        fig, ax = plt.subplots(figsize=(4*1.618, 2))
    else:
        fig = ax.figure

    # Draw line
    ax.plot(x, y, color='black', linewidth=1.0, alpha=1.0)

    # Dots
    ax.scatter(x, y, s=25, color='black', alpha=1.0, zorder=3)
    ax.scatter(x, y, s=125, color='white', alpha=1.0, zorder=2)

    # Axis limits with margin
    xmin, xmax = x.min(), x.max()
    ymin, ymax = y.min(), y.max()
    x_range, y_range = xmax - xmin, ymax - ymin
    ax.set_xlim(xmin - 0.05*x_range, xmax + 0.05*x_range)
    ax.set_ylim(ymin - 0.05*y_range, ymax + 0.05*y_range)

    # Minimal Tufte style
    apply_tufte_style(ax)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Ticks
    ax.set_xticks(x)
    ax.set_yticks(_intermediate_ticks(ymin, ymax, max_ticks=5))
    ax.tick_params(axis='y', which='both', length=5, direction='out', color='black', width=1, pad=5)
    ax.tick_params(axis='x', which='both', length=5)

    return fig, ax

####################################################################################################
#                                          Test / example code                                     #
####################################################################################################     
def main():

    t = np.linspace(0, 10, 10)
    y = 5.0 * np.sin(t) + 1.0 * np.random.randn(10)
    
    fig, ax = time_series(t, y)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
