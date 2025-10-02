import numpy as np
import matplotlib.pyplot as plt
from tufteplotlib.styles import apply_tufte_style

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def sparkline(y, *,
              show_dots=True,
              show_labels=True,
              start_end_color="black",
              min_max_color="red",
              dot_size=12,
              ax=None):
    """
    Illustrates the change in data across time. No x-axis labels are used. Best used for dense data.

    Parameters
    ----------
    y : array-like
        Sequence of values to plot.
    show_dots : bool, default True
        Whether to show start/end and min/max dots.
    show_labels : bool, default True
        Whether to label the start and end values.
    start_end_color : str, default "black"
        Color of start and end dots.
    min_max_color : str, default "red"
        Color of min and max dots.
    dot_size : float, default 12
        Marker size for the dots.
    ax : Optional axis.

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    """
    y = np.asarray(y)
    x = np.arange(len(y))
  
    if ax is None:
        fig, ax = plt.subplots(figsize=(4*1.618, 1))
    else:
        fig = ax.figure

    # Draw sparkline
    ax.plot(x, y, color="black", linewidth=1.0, zorder=1)

    if show_dots:
        # Start and end
        ax.scatter([x[0], x[-1]], [y[0], y[-1]], color=start_end_color, s=dot_size, zorder=2)
        # Min and max
        ymin_idx, ymax_idx = np.argmin(y), np.argmax(y)
        ax.scatter([x[ymin_idx], x[ymax_idx]], [y[ymin_idx], y[ymax_idx]], color=min_max_color, s=dot_size, zorder=2)

    if show_labels:
        ax.text(x[0] - 0.2, y[0], f"{y[0]:.2f}", ha="right", va="center")
        ax.text(x[-1] + 0.2, y[-1], f"{y[-1]:.2f}", ha="left", va="center")

    # Axis limits
    ymin, ymax = y.min(), y.max()
    yrange = ymax - ymin
    ax.set_ylim(ymin - 0.05*yrange, ymax + 0.05*yrange)
    x_margin = 0.05 * (x[-1] - x[0]) if len(x) > 1 else 0.5
    ax.set_xlim(x[0] - x_margin, x[-1] + x_margin)

    # Minimal axes
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    apply_tufte_style(ax)

    return fig, ax

####################################################################################################
#                                          Test / example code                                     #
####################################################################################################     
def main():

    y = np.random.normal(0, 1, 30).cumsum()
    
    fig, ax = sparkline(y)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
