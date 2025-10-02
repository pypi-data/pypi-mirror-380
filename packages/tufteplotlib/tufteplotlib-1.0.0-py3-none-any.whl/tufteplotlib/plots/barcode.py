import matplotlib.pyplot as plt
import numpy as np
from tufteplotlib.styles import apply_tufte_style
from tufteplotlib.utils import _intermediate_ticks

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def barcode_plot(categories, values, ax=None):
    """
    Plot unique observations across nominal categories to show data distribution.
    Best used for sparse data. For dense data, consider using a quartile plot.

    Parameters
    ----------
    categories : array-like
        Sequence of categorical labels for the x-axis.
    values : array-like
        Numerical data corresponding to each category.
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

    categories = np.asarray(categories)
    values = np.asarray(values)

    # Map categories to numeric positions
    unique_categories = sorted(list(set(categories)))
    cat_to_x = {cat: i for i, cat in enumerate(unique_categories)}
    x_positions = np.array([cat_to_x[cat] for cat in categories])

    # Draw horizontal barcode lines with default style
    for x, y in zip(x_positions, values):
        ax.hlines(y, x - 0.2, x + 0.2, color='black', alpha=0.5, linewidth=2.0)

    # Compute y-axis limits
    ymin = values.min()
    ymax = values.max()
    ax.set_ylim(ymin, ymax)

    # Set x-axis labels at category positions
    ax.set_xticks(range(len(unique_categories)))
    ax.set_xticklabels(unique_categories, fontsize=10)

    # Set nice y-axis ticks (min, intermediate, max)
    y_ticks = _intermediate_ticks(ymin, ymax)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels([f"{t:.2f}" for t in y_ticks])

    # Hide top, right, and bottom spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Apply Tufte style
    apply_tufte_style(ax)

    return fig, ax

####################################################################################################
#                                          Test / example code                                     #
####################################################################################################
def main():

    params = {
        "Lowenstein": {"mu": 5, "sigma": 3, "n": 50},
        "Zweig": {"mu": 7, "sigma": 1, "n": 50},
        "Sneed": {"mu": 6, "sigma": 2, "n": 50}
    }

    categories = []
    
    values = []

    for cat, p in params.items():
        data = np.random.normal(loc=p["mu"], scale=p["sigma"], size=p["n"])
        categories.extend([cat]*p["n"])
        values.extend(data)

    fig, ax = barcode_plot(categories, values)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

