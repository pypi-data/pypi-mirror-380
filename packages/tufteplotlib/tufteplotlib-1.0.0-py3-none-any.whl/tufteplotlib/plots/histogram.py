import numpy as np
import matplotlib.pyplot as plt
from tufteplotlib.styles import apply_tufte_style
from tufteplotlib.utils import _intermediate_ticks

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def histogram_plot(data, bins=10, ax=None):
    """
    Plot the frequency of observations for a 1-dimensional data set, distributed across discretized
    numerical categories. If the data are dense, consider using the density plot instead.

    Parameters
    ----------
    data : array-like
        Input data to histogram.
    bins : int or sequence, optional
        Number of bins or explicit bin edges. Default 10.
    ax : matplotlib.axes.Axes, optional
        Axis to draw on. If None, a new figure is created.

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    """
    if ax is None:
        fig, ax_hist = plt.subplots(figsize=(4*1.618, 4))
    else:
        fig = ax.figure
        ax_hist = ax

    # Compute histogram
    counts, bin_edges, patches = ax_hist.hist(
        data,
        bins=bins,
        alpha=1.0,
        color=[0.4, 0.4, 0.4],
        edgecolor='white',
        linewidth=0.5,
        rwidth=0.6
    )

    # Y-axis: compute intermediate ticks
    ymin, ymax = counts.min(), counts.max()
    y_ticks = _intermediate_ticks(ymin, ymax, max_ticks=5)

    # Ensure min and max are included
    if ymin not in y_ticks:
        y_ticks = np.insert(y_ticks, 0, ymin)
    if ymax not in y_ticks:
        y_ticks = np.append(y_ticks, ymax)

    # Determine decimal places automatically
    magnitude = max(abs(counts))
    if magnitude < 1:
        fmt = ".3f"
    elif magnitude < 10:
        fmt = ".2f"
    else:
        fmt = ".1f"

    # Set y-ticks and horizontal lines
    ax_hist.set_yticks(y_ticks)
    ax_hist.set_yticklabels([f"{yt:{fmt}}" for yt in y_ticks])
    for yt in y_ticks[1:]:
        ax_hist.hlines(yt, xmin=bin_edges[0], xmax=bin_edges[-1], color='white', linewidth=1)

    # X-axis default ticks
    ax_hist.tick_params(axis='x', rotation=0)

    # Bottom spine spans bars
    ax_hist.spines['bottom'].set_bounds(bin_edges[0], bin_edges[-1])
    ax_hist.spines['bottom'].set_color([0.4, 0.4, 0.4])

    # Hide left, top, right spines
    ax_hist.spines['left'].set_visible(False)
    ax_hist.spines['top'].set_visible(False)
    ax_hist.spines['right'].set_visible(False)

    # Apply Tufte style
    apply_tufte_style(ax_hist)
    
    ax_hist.set_ylim(0, y_ticks[-1])
    
    return fig, [ax_hist]


####################################################################################################
#                                          Test / example code                                     #
####################################################################################################     
def main():

    data = np.random.normal(loc=0.0, scale=1.0, size=100)
    
    fig, ax = histogram_plot(data)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

