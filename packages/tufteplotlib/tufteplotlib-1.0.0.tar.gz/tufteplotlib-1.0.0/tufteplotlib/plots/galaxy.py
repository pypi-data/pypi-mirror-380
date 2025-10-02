import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from tufteplotlib.styles import apply_tufte_style

####################################################################################################
#                                         Core function                                            #
####################################################################################################
def galaxy_plot(x, y, z, *,
                nx_bins=100,
                ny_bins=100,
                cmap='Greys',
                ax=None):
    """
    Tufte-style galaxy plot: discretize (x, y) into bins, take max(z) per bin,
    and plot as a grayscale intensity map.

    Parameters
    ----------
    x, y, z : array-like
        1D arrays of the same length.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on. If None, a new figure is created.
    nx_bins : int
        Number of bins along x-axis.
    ny_bins : int
        Number of bins along y-axis.
    cmap : str or Colormap
        Colormap to use (grayscale recommended).
    ax : Optional axis

    Returns
    -------
    ax : matplotlib.axes.Axes
    im : matplotlib.image.AxesImage
    """
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(4,3.5))
    else:
        fig = ax.figure

    x = np.asarray(x)
    y = np.asarray(y)
    z = np.asarray(z)

    # Create empty grid
    z_grid = np.full((ny_bins, nx_bins), np.nan)
    x_edges = np.linspace(x.min(), x.max(), nx_bins + 1)
    y_edges = np.linspace(y.min(), y.max(), ny_bins + 1)

    # Assign max z to each bin
    for i in range(nx_bins):
        for j in range(ny_bins):
            mask = ((x >= x_edges[i]) & (x < x_edges[i+1]) &
                    (y >= y_edges[j]) & (y < y_edges[j+1]))
            if np.any(mask):
                z_grid[j, i] = np.max(z[mask])

    # Handle any bins with no data
    z_grid = np.nan_to_num(z_grid, nan=np.nanmin(z_grid))

    z_min, z_max = np.nanmin(z_grid), np.nanmax(z_grid)

    im = ax.imshow(z_grid, origin='lower',
                   extent=(x.min(), x.max(), y.min(), y.max()),
                   cmap=cmap,
                   norm=Normalize(vmin=z_min, vmax=z_max),
                   aspect='auto')

    # Apply Tufte style
    apply_tufte_style(ax)

    # Hide all spines
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_aspect('equal')
    
    plt.tight_layout()

    return ax, im
    
####################################################################################################
#                                    Generate minimal color bar                                    #
####################################################################################################
####################################################################################################
#                                    Minimal colorbar utility                                      #
####################################################################################################
def add_min_max_colorbar(im, ax=None):
    """
    Add a minimalist colorbar showing only the min and max of an AxesImage.

    Parameters
    ----------
    im : matplotlib.image.AxesImage
        The image returned by imshow or similar.
    ax : matplotlib.axes.Axes, optional
        Axes to associate the colorbar with. If None, uses the current axes.

    Returns
    -------
    cbar : matplotlib.colorbar.Colorbar
        The created colorbar object.
    """
    if ax is None:
        ax = plt.gca()

    # Get data range
    vmin, vmax = im.get_array().min(), im.get_array().max()

    # Create colorbar
    cbar = plt.colorbar(im, ax=ax, fraction=0.05, pad=0.05)
    cbar.set_ticks([vmin, vmax])
    cbar.set_ticklabels([f"{vmin:.2f}", f"{vmax:.2f}"])
    cbar.outline.set_visible(False)
    
    return cbar
    
####################################################################################################
#                                          Test / example code                                     #
####################################################################################################     
def main():

    # Generate random galaxy data
    n_points = 10000

    # x and y positions
    x = np.random.uniform(low=-1.0, high=1.0, size=n_points)
    y = np.random.uniform(low=-1.0, high=1.0, size=n_points)
    z = np.random.uniform(low= 0.0, high=1.0, size=n_points)

    # Create plot
    ax, im = galaxy_plot(x, y, z,
                         nx_bins=100,
                         ny_bins=100)
                         
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_title("Space")
        
    # Create the colorbar (minimal)
    cbar = add_min_max_colorbar(im, ax=ax)

    # Add label outside the function
    cbar.set_label('Ant Density', fontsize=10, labelpad=-10)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
