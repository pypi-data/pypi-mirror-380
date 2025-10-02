import numpy as np
import matplotlib.pyplot as plt
from tufteplotlib.styles import apply_tufte_style
from tufteplotlib.utils import _intermediate_ticks

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def bar_chart(categories, values, ax=None):
    """
    Plot quantities across nominal categories.

    Parameters
    ----------
    categories : array-like
        Sequence of category labels for the x-axis.
    values : array-like
        Heights of the bars corresponding to each category.
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
    x_pos = np.arange(len(categories))

    # Draw bars with default minimal color
    ax.bar(x_pos, values, color=[0.4, 0.4, 0.4])

    # Set y-axis limits
    ymin = 0
    ymax = max(values)
    ax.set_ylim(ymin, ymax)

    # Compute y-axis ticks
    y_ticks = [yt for yt in _intermediate_ticks(ymin, ymax, max_ticks=5) if yt != 0.0]

    # Decide if we need to add the smallest value
    min_val = values.min()
    add_min_label = y_ticks and (min_val < y_ticks[0])

    # Hide default ticks
    ax.set_yticks([])

    # Draw y-axis labels and horizontal lines
    for ytick in y_ticks:
        ax.text(-0.5, ytick, f"{ytick:.2f}", va='center', ha='right', color='black', fontsize=10)
        ax.hlines(ytick, -0.5, len(categories)-0.5, color='white', linewidth=1)

    if add_min_label:
        ax.text(-0.5, min_val, f"{min_val:.2f}", va='center', ha='right', color='black', fontsize=10)

    # Set x-axis labels
    ax.set_xticks(x_pos)
    ax.set_xticklabels(categories)

    # Hide left spine
    ax.spines['left'].set_visible(False)

    # Set bottom spine to span only the bars
    ax.spines['bottom'].set_bounds(x_pos[0]-0.3, x_pos[-1]+0.3)
    ax.spines['bottom'].set_color([0.4, 0.4, 0.4])

    # Apply Tufte style (removes top/right spines)
    apply_tufte_style(ax)

    return fig, ax

####################################################################################################
#                                          Test / example code                                     #
####################################################################################################
def main():

    categories = ["Satiety", "Triumvirate", "Gourmand", "Machiavellian", "Boudoir"]
    
    values = np.random.randint(3, 20, size=len(categories))

    fig, ax = bar_chart(categories, values)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
