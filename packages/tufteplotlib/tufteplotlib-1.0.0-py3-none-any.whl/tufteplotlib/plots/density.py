import numpy as np
import matplotlib.pyplot as plt
from tufteplotlib.styles import apply_tufte_style
from tufteplotlib.utils import _intermediate_ticks
from scipy.stats import gaussian_kde

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def density_plot(data, ax=None):
    """
    Illustrate the distribution of values within a 1-dimensional data set.
    Best used for dense data sets. For sparse data, consider using a histogram.

    Parameters
    ----------
    data : array-like
        1D array of numeric values.
    ax : matplotlib.axes.Axes, optional
        Axis to draw on. If None, a new figure is created.

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    """
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(4*1.618, 4))
    else:
        fig = ax.figure

    data = np.asarray(data)
    kde = gaussian_kde(data)
    x_vals = np.linspace(data.min(), data.max(), 500)
    y_vals = kde(x_vals)

    # Plot shaded area
    ax.fill_between(x_vals, 0, y_vals, color=[0.4, 0.4, 0.4], alpha=1.0)

    # Y-axis: compute nice intermediate ticks
    ymin, ymax = 0, y_vals.max()
    ax.set_ylim(ymin, ymax)
    y_ticks = _intermediate_ticks(ymin, ymax, max_ticks=5)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels([f"{ytick:.2f}" for ytick in y_ticks])

    # X-axis: min, median, max
    x_ticks = [np.min(data), np.median(data), np.max(data)]
    ax.set_xticks(x_ticks)
    ax.set_xticklabels([f"{xtick:.2f}" for xtick in x_ticks])

    # Apply Tufte-style minimalism
    apply_tufte_style(ax)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    return fig, ax

####################################################################################################
#                                          Test / example code                                     #
####################################################################################################
def main():

    data = np.random.normal(loc=0, scale=1, size=500)
    fig, ax = density_plot(data)
    
    # Set title and axis labels
    ax.set_title("Sugar Pile")
    ax.set_xlabel("Distance")
    ax.set_ylabel("Height")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
