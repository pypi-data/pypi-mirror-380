import numpy as np
import matplotlib.pyplot as plt
from tufteplotlib.styles import apply_tufte_style

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def rug_plot(x, y, ax=None):
    """
    A scatter plot, with a rug plot on each axis to illustrate the marginal distributions.

    Parameters
    ----------
    x, y : array-like
        Coordinates of the rug ticks.
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

    # Scatter points
    ax.scatter(x, y, color='black', alpha=1.0)

    # Compute min/max
    xmin, xmax = x.min(), x.max()
    ymin, ymax = y.min(), y.max()
    x_range = xmax - xmin
    y_range = ymax - ymin

    # Set limits with small margin
    margin = 0.05
    ax.set_xlim(xmin - margin*x_range, xmax + margin*x_range)
    ax.set_ylim(ymin - margin*y_range, ymax + margin*y_range)

    # Apply Tufte style
    apply_tufte_style(ax)

    # Hide all spines
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Barcode-style ticks
    ax.set_xticks(x)
    ax.set_yticks(y)
    ax.set_xticklabels([''] * len(x))
    ax.set_yticklabels([''] * len(y))
    ax.tick_params(axis='x', length=10.0, width=1.0, colors='black')
    ax.tick_params(axis='y', length=10.0, width=1.0, colors='black')

    # Optional min/median/max labels
    for val, axis in zip([xmin, np.median(x), xmax], ['x', 'x', 'x']):
        nearest = x[np.argmin(np.abs(x - val))]
        ax.text(nearest, ymin - 0.12*y_range, f"{val:.2f}",
                ha='center', va='top', fontsize=10, color='black')
    for val in [ymin, np.median(y), ymax]:
        nearest = y[np.argmin(np.abs(y - val))]
        ax.text(xmin - 0.08*x_range, nearest, f"{val:.2f}",
                ha='right', va='center', fontsize=10, color='black')

    return fig, ax

####################################################################################################
#                                          Test / example code                                     #
####################################################################################################
def main():
    x = np.random.normal(loc=0, scale=1, size=200)
    y = np.random.normal(loc=0, scale=1, size=200)

    fig, ax = rug_plot(x, y)
    
    ax.set_xlabel("Gastronomic Capacity", labelpad=20)
    ax.set_ylabel("Satiety", labelpad=30)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

