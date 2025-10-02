import numpy as np
import matplotlib.pyplot as plt
from tufteplotlib.styles import apply_tufte_style
from tufteplotlib.utils import _intermediate_ticks

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def quartile_plot(categories, values, ax=None):
    """
    Show the distribution of data across nominal categories. Illustrates the median, interquartile
    range, and outliers. Best used for dense data. If the data are sparse, consider using the
    barcode plot.

    Parameters
    ----------
    categories : array-like
        Category labels for x-axis.
    values : array-like
        Numeric values corresponding to each category.
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

    categories = np.asarray(categories)
    values = np.asarray(values)

    if categories.shape[0] != values.shape[0]:
        raise ValueError("categories and values must have the same length")

    unique_categories = list(dict.fromkeys(categories.tolist()))
    n_cat = len(unique_categories)
    cat_to_x = {cat: i for i, cat in enumerate(unique_categories)}

    whisker_mins = []
    whisker_maxs = []
    all_outliers = []

    bg_color = ax.get_facecolor()

    for cat in unique_categories:
        mask = (categories == cat)
        cat_vals = values[mask]
        if cat_vals.size == 0:
            continue

        q1, q2, q3 = np.percentile(cat_vals, [25, 50, 75])
        iqr = q3 - q1
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr

        non_outliers = cat_vals[(cat_vals >= lower_fence) & (cat_vals <= upper_fence)]
        whisker_min = non_outliers.min() if non_outliers.size > 0 else cat_vals.min()
        whisker_max = non_outliers.max() if non_outliers.size > 0 else cat_vals.max()

        whisker_mins.append(whisker_min)
        whisker_maxs.append(whisker_max)

        outliers = cat_vals[(cat_vals < lower_fence) | (cat_vals > upper_fence)]
        if outliers.size > 0:
            all_outliers.append(outliers)

        x = cat_to_x[cat]

        # whiskers
        ax.vlines(x, whisker_min, whisker_max, color='black', linewidth=1.0, zorder=1)

        # mask IQR
        ax.vlines(x, q1, q3, color=bg_color, linewidth=6.0, zorder=2)

        # median
        ax.scatter([x], [q2], s=36, color='black', zorder=3)

        # outliers
        if outliers.size > 0:
            ax.scatter(np.full(outliers.shape, x), outliers, s=1, color='black', zorder=4)

    # X-axis
    ax.set_xticks(range(n_cat))
    ax.set_xticklabels(unique_categories)
    ax.set_xlim(-0.5, n_cat - 0.5)

    # Y-axis including outliers
    if len(whisker_mins) == 0:
        ymin, ymax = values.min(), values.max()
    else:
        ymin = min(min(whisker_mins), *(o.min() for o in all_outliers)) if all_outliers else min(whisker_mins)
        ymax = max(max(whisker_maxs), *(o.max() for o in all_outliers)) if all_outliers else max(whisker_maxs)

    y_range = ymax - ymin if ymax > ymin else 1.0
    pad = 0.02 * y_range
    ax.set_ylim(ymin - pad, ymax + pad)

    y_ticks = _intermediate_ticks(ymin, ymax, max_ticks=5)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels([f"{t:.2f}" for t in y_ticks])

    # Tufte styling
    apply_tufte_style(ax)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    return fig, ax

####################################################################################################
#                                          Test / example code                                     #
####################################################################################################
def main():
    params = {
        "Lowenstein": {"mu": 5, "sigma": 3, "n": 100},
        "Sneed": {"mu": 6, "sigma": 2, "n": 100},
        "Zweig": {"mu": 7, "sigma": 1, "n": 100}
    }

    categories = []
    values = []

    for cat, p in params.items():
        data = np.random.normal(loc=p["mu"], scale=p["sigma"], size=p["n"])
        categories.extend([cat]*p["n"])
        values.extend(data)

    fig, ax = quartile_plot(categories, values)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

