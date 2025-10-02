from matplotlib.ticker import MaxNLocator
import numpy as np

####################################################################################################
#                    Compute equispaced intermediate ticks between min and max values              #
####################################################################################################   
def _intermediate_ticks(min_val, max_val, max_ticks=5, tol=1e-03, edge_fraction=0.05):
    """
    Returns tick values including exact min and max,
    plus nicely rounded, equispaced interior ticks.
    
    Interior ticks that are too close to min or max (within edge_fraction of range) are removed.

    Parameters:
        min_val : float
        max_val : float
        max_ticks : approximate number of interior ticks
        tol : snapping tolerance to zero
        edge_fraction : fraction of range near min/max to ignore interior ticks

    Returns:
        list of tick values
    """
    if min_val == max_val:
        return [min_val]

    # Compute raw step size
    raw_step = (max_val - min_val) / (max_ticks + 1)  # +1 to leave room for min/max

    # Compute nice step: 1, 2, or 5 × 10^n
    magnitude = 10 ** np.floor(np.log10(raw_step))
    residual = raw_step / magnitude
    if residual <= 1:
        nice_step = 1 * magnitude
    elif residual <= 2:
        nice_step = 2 * magnitude
    elif residual <= 5:
        nice_step = 5 * magnitude
    else:
        nice_step = 10 * magnitude

    # Generate interior ticks
    start = np.ceil(min_val / nice_step) * nice_step
    end = np.floor(max_val / nice_step) * nice_step
    interior_ticks = list(np.arange(start, end + 0.5*nice_step, nice_step))

    # Remove duplicates and ensure strictly inside min/max
    interior_ticks = [t for t in interior_ticks if min_val < t < max_val]

    # Remove ticks too close to edges
    range_val = max_val - min_val
    interior_ticks = [t for t in interior_ticks 
                      if t - min_val > edge_fraction*range_val and max_val - t > edge_fraction*range_val]

    # Combine min, interior ticks, max
    ticks = [min_val] + interior_ticks + [max_val]
    
    # Snap near-zero values to 0
    ticks = [0 if abs(t) < tol else t for t in ticks]
    
    return ticks

