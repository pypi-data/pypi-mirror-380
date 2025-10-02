import numpy as np
import matplotlib.pyplot as plt
from tufteplotlib.styles import apply_tufte_style
from tufteplotlib.utils import _intermediate_ticks

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def pareto_chart(categories, values, ax=None):
    """
    Show the contribution of nominal categories to a quantity. It contains a bar chart where categories
    are ordered from the largest quantity, to the smallest. A cumulative percentage line is overlayed
    to convey contribution to the whole.

    Parameters
    ----------
    categories : list-like
        Category names.
    values : array-like
        Bar heights (can be floats).
    ax : Optional axis

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : list of matplotlib.axes.Axes [ax_bar, ax_cumulative]
    """
    
    if ax is None:
        fig, ax_bar = plt.subplots(figsize=(4*1.618, 4))
    else:
        fig = ax_bar.figure

    categories = np.asarray(categories)
    values = np.asarray(values, dtype=float)

    # Sort descending
    sort_idx = np.argsort(values)[::-1]
    categories = categories[sort_idx]
    values = values[sort_idx]
    x_pos = np.arange(len(categories))

    # Draw bars
    ax_bar.bar(x_pos, values, color=[0.5, 0.5, 0.5], alpha=1.0, width=0.6, bottom=0)

    # Cumulative percentage line with dots
    cumulative = np.cumsum(values)
    cumulative_pct = 100 * cumulative / cumulative[-1]

    ax_cum = ax_bar.twinx()
    ax_cum.plot(x_pos, cumulative_pct, color=[0,0,0], linewidth=1.5, alpha=0.8, zorder=3)
    ax_cum.scatter(x_pos, cumulative_pct, color=[0,0,0], s=40,
                    edgecolor='white', linewidth=1.0, zorder=4)

    # Percentage labels above dots
    for i, pct in enumerate(cumulative_pct):
        ax_cum.text(x_pos[i], pct + 1, f"{pct:.1f}%", ha='center', va='bottom', fontsize=9, color=[0,0,0])

    # Y-axis ticks for bars
    ymin, ymax = values.min(), values.max()
    y_ticks = _intermediate_ticks(ymin, ymax, max_ticks=5)
    if ymin < y_ticks[0]:
        y_ticks = np.insert(y_ticks, 0, ymin)

    # Determine decimal places automatically
    magnitude = max(abs(values))
    if magnitude < 1:
        fmt = ".3f"
    elif magnitude < 10:
        fmt = ".2f"
    else:
        fmt = ".1f"

    ax_bar.set_ylim(0, ymax * 1.1)
    ax_bar.set_yticks([])

    # Draw horizontal lines and manual labels
    for i, yt in enumerate(y_ticks):
        if i == 0 and yt == ymin and yt != 0:
            ax_bar.text(-0.6, yt, f"{yt:{fmt}}", ha='left', va='center', fontsize=9, color='black')
        else:
            ax_bar.hlines(yt, -0.5, len(categories)-0.5, color='white', linewidth=1)
            ax_bar.text(-0.6, yt, f"{yt:{fmt}}", ha='left', va='center', fontsize=9, color='black')

    # X-axis labels manually
    ax_bar.tick_params(axis='x', length=0)
    for i, label in enumerate(categories):
        ax_bar.text(i, -0.02*ymax, label, ha='center', va='top', rotation=0.0, fontsize=9)

    # Bottom spine
    ax_bar.spines['bottom'].set_bounds(x_pos[0]-0.3, x_pos[-1]+0.3)
    ax_bar.spines['bottom'].set_color([0.4,0.4,0.4])

    # Hide other spines
    for spine_name, spine in ax_bar.spines.items():
        if spine_name != 'bottom':
            spine.set_visible(False)
    for spine in ax_cum.spines.values():
        spine.set_visible(False)

    # Hide ax_cum ticks
    ax_cum.set_yticks([])
    ax_cum.set_xticks([])
    ax_cum.set_ylim(0, 110)  # independent scale 0-100%

    # Apply Tufte style
    apply_tufte_style(ax_bar)
    apply_tufte_style(ax_cum)
    
    return fig, [ax_bar, ax_cum]


####################################################################################################
#                                          Test / example code                                     #
####################################################################################################
def main():

    categories = ["Jimbo", "Nelson", "Dolph", "Kearny", "Kearny Jnr."]
    
    np.random.seed()
    
    values = np.random.rand(len(categories)) * 20  # float values
    
    fig, ax = pareto_chart(categories, values)
    
    # Example: modify cumulative axis independently
    ax[1].set_ylim(-10, 110)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

