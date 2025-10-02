def apply_tufte_style(ax):
    """Apply minimal Tufte-style aesthetics to a matplotlib Axes."""

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(direction='out', length=0)
    ax.grid(False)
