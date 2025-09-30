"""
Overlap analysis module for PLASTRO scores.

This module provides functions for computing overlap-based plasticity scores
from character matrices and single-cell data. The PLASTRO score quantifies
the relationship between lineage and phenotypic distances.
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tqdm import tqdm
from tqdm.contrib.concurrent import process_map
import multiprocessing
import heapq
import os
from sklearn.metrics.pairwise import pairwise_distances
from typing import Optional, Tuple
import anndata

def PLASTRO_score(
    character_matrix: pd.DataFrame,
    ad: 'anndata.AnnData',
    threshold: float = 0.95,
    maximum_radius: int = 500,
    interval: int = 1,
    latent_space_key: str = 'X_dm',
    flavor: str = 'gini',
    parallel: bool = False,
    save_to: Optional[str] = None,
    show_plots: bool = True
) -> pd.DataFrame:
    """
    Compute the PLASTRO overlap plasticity score.
    
    The PLASTRO score quantifies cellular plasticity by measuring the overlap
    between lineage relationships (from character matrix) and phenotypic 
    relationships (from latent space) at multiple spatial scales.

    Parameters
    ----------
    character_matrix : pd.DataFrame
        Character matrix with cells as rows and CRISPR mutation sites as columns.
        Values represent mutation states (0=unmutated, >0=mutated states).
    ad : anndata.AnnData
        Annotated data object containing latent representation of phenotype.
    threshold : float, optional
        Threshold for variance in overlap (proportion of max peak variance), by default 0.95.
        Only used when flavor='variable_radii'. Radii with variance >= threshold * max_variance 
        are used for computing the final score.
    maximum_radius : int, optional
        Maximum radius for computing overlap, by default 500.
    interval : int, optional
        Interval between radii for overlap computation, by default 1.
    latent_space_key : str, optional
        Key in `ad.obsm` where latent space coordinates are stored, by default 'X_dm'.
    flavor : str, optional
        Method for computing PLASTRO score, by default 'gini'.
        
        - 'gini': Computes Gini inequality index for each cell's overlap distribution across radii.
          Measures how concentrated the overlap is at specific spatial scales.
          
          * High Gini (→1): Overlap concentrated at few radii (unequal distribution)
          * Low Gini (→0): Overlap evenly distributed across radii (equal distribution)
          * Uses ALL radii from 1 to maximum_radius
          
        - 'variable_radii': Computes area under overlap curve using variance-filtered radii.
          Measures strength of lineage-phenotype concordance at most informative scales.
          
          * High score: Strong lineage-phenotype concordance (low plasticity)
          * Low score: Weak lineage-phenotype concordance (high plasticity)  
          * Uses SELECTED radii based on variance threshold
    parallel : bool, optional
        Whether to use parallel processing, by default False.
    save_to : str, optional
        Directory path to save results, by default None.
    show_plots : bool, optional
        Whether to display variance analysis plots (only for flavor='variable_radii'), by default True.

    Returns
    -------
    pd.DataFrame
        PLASTRO plasticity scores for each cell. Column name depends on flavor:
        
        - flavor='gini': Column 'Gini_Index' with values [0,1]
        - flavor='variable_radii': Column 'PLASTRO_score' with positive values

    Examples
    --------
    >>> import plastro
    >>> 
    >>> # Compute Gini-based plasticity scores
    >>> gini_scores = plastro.PLASTRO_score(char_matrix, ad, flavor='gini')
    >>> print(f"Mean Gini index: {gini_scores['Gini_Index'].mean():.3f}")
    >>> 
    >>> # Compute variance-based plasticity scores
    >>> var_scores = plastro.PLASTRO_score(char_matrix, ad, flavor='variable_radii', threshold=0.95)
    >>> print(f"Mean PLASTRO score: {var_scores['PLASTRO_score'].mean():.3f}")

    Notes
    -----
    The PLASTRO analysis workflow:
    
    1. **Overlap Computation**: For each cell and radius r, compute overlap between:
       - Lineage neighbors: r cells most similar by CRISPR mutations
       - Phenotype neighbors: r cells most similar in latent space
       
    2. **Score Computation**: Two complementary approaches:
    
       **Gini Approach** (flavor='gini'):
       - Computes Gini inequality coefficient for each cell's overlap profile
       - Measures how overlap varies with spatial scale for individual cells
       - Interpretation: Distribution pattern of lineage-phenotype concordance
       
       **Variable Radii Approach** (flavor='variable_radii'):
       - Identifies radii with high variance in overlap across cells
       - Computes area under overlap curve for informative radii only
       - Interpretation: Overall strength of lineage-phenotype concordance
       
    **When to use each flavor:**
    
    - Use **'gini'** to understand overlap distribution patterns per cell
    - Use **'variable_radii'** to measure overall plasticity strength
    - Both provide complementary views of the same underlying relationships
    """
    overlaps = PLASTRO_overlaps(
        character_matrix, ad, 
        maximum_radius=maximum_radius, 
        interval=interval, 
        latent_space_key=latent_space_key, 
        parallel=parallel, 
        save_to=save_to
    )
    
    if flavor not in ['gini', 'variable_radii']:
        raise ValueError("Flavor must be 'gini' or 'variable_radii'")
    
    if flavor == 'gini':
        overlap_score = compute_gini_plasticity_score(overlaps)
        return overlap_score
    else:
        print('Selecting radius based on variance threshold...')
        print('WARNING: This approach is VERY sensitive to threshold choice!')
        overlap_score = compute_variable_radii_plasticity_score(
            overlaps, 
            threshold=threshold, 
            plot_variance=show_plots, 
            save_to=save_to
        )
    
    print('Computed overlap score.')
    return overlap_score



def PLASTRO_overlaps(
    character_matrix: pd.DataFrame,
    ad: 'anndata.AnnData',
    maximum_radius: int = 500,
    interval: int = 1,
    latent_space_key: str = 'X_dm',
    parallel: bool = False,
    save_to: Optional[str] = None
) -> pd.DataFrame:
    """
    Compute overlaps between lineage and phenotypic neighborhoods.
    
    For each cell and radius, computes the overlap between cells that are
    lineage neighbors (similar character states) and phenotypic neighbors
    (close in latent space).

    Parameters
    ----------
    character_matrix : pd.DataFrame
        Character matrix with mutation data.
    ad : anndata.AnnData
        Annotated data object with phenotypic information.
    maximum_radius : int, optional
        Maximum neighborhood radius, by default 500.
    interval : int, optional
        Radius increment, by default 1.
    latent_space_key : str, optional
        Key for latent space coordinates, by default 'X_dm'.
    parallel : bool, optional
        Use parallel processing, by default False.
    save_to : str, optional
        Save directory, by default None.

    Returns
    -------
    pd.DataFrame
        Overlap values for each cell (rows) at each radius (columns).
    """
    print(f'Computing overlaps with maximum radius {maximum_radius}')
    
    # Ensure consistent cell ordering
    common_cells = character_matrix.index.intersection(ad.obs_names)
    character_matrix = character_matrix.loc[common_cells]
    ad_subset = ad[common_cells].copy()
    
    # Compute distance matrices
    lineage_distances = compute_lineage_distances(character_matrix)
    phenotype_distances = compute_phenotype_distances(ad_subset, latent_space_key)
    
    radii = np.arange(1, maximum_radius + 1, interval)
    
    # Use optimized computation method
    overlaps = _compute_overlaps_precomputed_optimized(
        lineage_distances, 
        phenotype_distances, 
        radii
    )
    
    # Convert to DataFrame with proper indexing
    overlaps_df = pd.DataFrame(overlaps, index=common_cells, columns=radii)
    
    if save_to is not None:
        overlaps_df.to_csv(os.path.join(save_to, 'overlaps.csv'))
        print(f'Saved overlaps to {save_to}')
    
    return overlaps_df



def compute_variable_radii_plasticity_score(
    overlaps: pd.DataFrame,
    threshold: float = 0.95,
    plot_variance: bool = True,
    save_to: Optional[str] = None
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Compute PLASTRO scores using variable radii approach.
    
    This method identifies optimal radius ranges based on variance in overlap
    across cells, then computes area under the overlap curve for selected radii.
    It focuses on the most informative spatial scales for plasticity analysis.

    Parameters
    ----------
    overlaps : pd.DataFrame
        Overlap matrix with cells as rows and radii as columns.
        Each value represents overlap between lineage and phenotype neighborhoods.
    threshold : float, optional
        Variance threshold for radius selection (0-1), by default 0.95.
        Radii with variance >= threshold * max_variance are considered informative.
    plot_variance : bool, optional
        Whether to plot variance analysis for radius selection, by default True.
    save_to : str, optional
        Directory to save variance analysis plots, by default None.

    Returns
    -------
    Tuple[pd.DataFrame, pd.Series]
        - PLASTRO scores for each cell (column: 'PLASTRO_score')
        - Variance values across all radii
        
    Notes
    -----
    **Algorithm:**
    1. Compute variance in overlap **across cells** for each radius
    2. Identify radii with variance >= threshold * max_variance
    3. Compute mean overlap across selected radii for each cell
    
    **Interpretation:**
    - **High scores**: Strong concordance between lineage and phenotype (low plasticity)
    - **Low scores**: Weak concordance between lineage and phenotype (high plasticity)
    - **Selected radii**: Spatial scales that best differentiate cells by plasticity
    
    **Comparison to Gini approach:**
    - Variable radii: Measures overall strength using informative scales
    - Gini: Measures distribution pattern across all scales
    """
    # Compute variance across cells for each radius
    variance_across_cells = overlaps.var(axis=0)
    max_variance = variance_across_cells.max()
    threshold_variance = threshold * max_variance
    
    # Identify optimal radius range
    valid_radii = variance_across_cells[variance_across_cells >= threshold_variance]
    
    if len(valid_radii) == 0:
        print(f"Warning: No radii meet variance threshold {threshold}")
        valid_radii = variance_across_cells.nlargest(10)  # Use top 10 radii
    
    print(f"Using {len(valid_radii)} radii for score computation")
    print(f"Radius range: {valid_radii.index.min()} - {valid_radii.index.max()}")
    
    # Compute area under curve for valid radii
    overlap_scores = overlaps[valid_radii.index].sum(axis=1) / len(valid_radii)
    overlap_scores = pd.DataFrame({'PLASTRO_score': overlap_scores})
    
    if plot_variance:
        _plot_variance_analysis(variance_across_cells, threshold_variance, valid_radii, save_to)
    
    return overlap_scores


def _plot_variance_analysis(
    variance_across_cells: pd.Series,
    threshold_variance: float,
    valid_radii: pd.Series,
    save_to: Optional[str]
) -> None:
    """Plot variance analysis for radius selection."""
    plt.figure(figsize=(10, 6))
    plt.plot(variance_across_cells.index, variance_across_cells.values, 'b-', alpha=0.7)
    plt.axhline(y=threshold_variance, color='r', linestyle='--', 
                label=f'Threshold ({threshold_variance:.3f})')
    plt.scatter(valid_radii.index, valid_radii.values, color='red', s=20, 
                label='Selected radii', zorder=5)
    plt.xlabel('Radius')
    plt.ylabel('Variance in Overlap')
    plt.title('Variance Analysis for Radius Selection')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    if save_to is not None:
        plt.savefig(os.path.join(save_to, 'variance_analysis.png'), 
                   dpi=300, bbox_inches='tight')
    
    plt.show()


def gini_index(arr: np.ndarray) -> float:
    """
    Compute the Gini inequality index for a 1D array.
    
    The Gini index measures inequality in the distribution of values,
    commonly used in economics but applicable to any distribution analysis.
    For PLASTRO, it measures how concentrated overlap values are across radii.

    Parameters
    ----------
    arr : np.ndarray
        Array of overlap values between 0 and 1.
        Each value represents overlap at a different radius.

    Returns
    -------
    float
        Gini index value between 0 and 1.
        - 0: Perfect equality (all values identical)
        - 1: Perfect inequality (one value has everything, others have nothing)
        
    Notes
    -----
    **Mathematical definition:**
    Gini = 1 - Σ(p_i + p_{i-1}) * (x_i - x_{i-1})
    
    Where p_i is cumulative proportion and x_i are sorted values.
    
    **For PLASTRO interpretation:**
    - High Gini: Overlap concentrated at specific radii (scale-specific plasticity)
    - Low Gini: Overlap distributed across radii (scale-invariant plasticity)
    """
    if not (np.all(arr >= 0) and np.all(arr <= 1)):
        # Print the values that are out of bounds
        out_of_bounds = arr[(arr < 0) | (arr > 1)]
        print(f"Out of bounds values: {out_of_bounds}")
        raise ValueError("Array values must be between 0 and 1")
    
    arr = np.sort(arr)
    cumsum = np.cumsum(arr)
    cumprop = cumsum / cumsum[-1]
    gini = 1 - np.sum((cumprop[1:] + cumprop[:-1]) * (arr[1:] - arr[:-1]))
    
    return gini


def compute_gini_plasticity_score(overlaps: pd.DataFrame) -> pd.DataFrame:
    """
    Compute PLASTRO scores using Gini inequality index approach.
    
    This method computes a Gini coefficient for each cell's overlap distribution
    across all radii. The Gini index measures how concentrated or dispersed
    the lineage-phenotype concordance is across different spatial scales.

    Parameters
    ----------
    overlaps : pd.DataFrame
        Overlap matrix with cells as rows and radii as columns. This is the output
        from the PLASTRO_overlaps() function. Each value represents overlap between
        lineage and phenotype neighborhoods at a given radius.

    Returns
    -------
    pd.DataFrame
        Gini plasticity scores for each cell with column 'Gini_Index'.
        Values range from 0 to 1.
        
    Notes
    -----
    **Algorithm:**
    1. For each cell, compute Gini coefficient of overlap values across ALL radii
    2. Gini measures inequality in the overlap distribution
    
    **Interpretation:**
    - **High Gini (≈1)**: Overlap concentrated at few specific radii
      * Suggests scale-specific plasticity patterns
      * Lineage-phenotype concordance varies dramatically with spatial scale
      
    - **Low Gini (≈0)**: Overlap evenly distributed across radii  
      * Suggests scale-invariant plasticity patterns
      * Consistent lineage-phenotype relationship across scales
      
    **Comparison to Variable Radii approach:**
    - Gini: Characterizes the **pattern** of how concordance varies with scale
    - Variable radii: Measures the **strength** of concordance at optimal scales
    
    **Use cases:**
    - Understanding how plasticity manifests across spatial scales
    - Identifying cells with scale-specific vs scale-invariant plasticity
    - Complementary analysis to variable radii approach
    """
    cell_names = overlaps.index
    overlaps_values = overlaps.values

    if len(overlaps_values.shape) != 2:
        raise ValueError("Overlaps must be a 2D array")
    
    # Compute Gini index for each row
    gini_values = np.array([gini_index(overlaps_values[i]) for i in range(overlaps_values.shape[0])])
    
    return pd.DataFrame(gini_values, index=cell_names, columns=['Gini_Index'])


# Optimized overlap computation functions
def _compute_overlaps_precomputed_optimized(
    lineage_distances: pd.DataFrame,
    phenotype_distances: pd.DataFrame,
    radii: np.ndarray
) -> np.ndarray:
    """Optimized overlap computation using pre-computed rankings."""
    # Pre-compute partial rankings - only up to max_radius, not entire distance matrix
    lineage_rankings = _get_all_neighbors_exact_optimized(lineage_distances.values, radii.max())
    phenotype_rankings = _get_all_neighbors_exact_optimized(phenotype_distances.values, radii.max())
    
    n_cells = len(lineage_distances)
    n_radii = len(radii)
    overlaps = np.zeros((n_cells, n_radii))
    
    # Compute overlaps with pre-computed rankings
    for i, radius in enumerate(tqdm(radii, desc="Computing overlaps")):
        overlaps[:, i] = _compute_overlap_from_rankings_optimized(lineage_rankings, phenotype_rankings, radius)
    
    return overlaps


def _get_all_neighbors_exact_optimized(distance_matrix: np.ndarray, max_k: int) -> np.ndarray:
    """Get all k-nearest neighbors up to max_k for all cells using partial sorting."""
    n_cells = distance_matrix.shape[0]
    
    # Only partition up to max_k+1 (including self) - O(n) instead of O(n log n)
    neighbors = np.argpartition(distance_matrix, max_k, axis=1)[:, :max_k+1]
    
    # Sort only within the k-smallest subset for consistent ordering - O(k log k)
    for i in range(n_cells):
        k_smallest_indices = neighbors[i, :max_k+1]
        k_smallest_dists = distance_matrix[i, k_smallest_indices]
        sorted_order = np.argsort(k_smallest_dists)
        neighbors[i, :max_k+1] = k_smallest_indices[sorted_order]
        
        # Ensure self is at position 0 (should have distance 0)
        if neighbors[i, 0] != i:
            # Find self in the neighbors and move to position 0
            self_pos = np.where(neighbors[i, :max_k+1] == i)[0]
            if len(self_pos) > 0:
                # Swap self to position 0
                neighbors[i, [0, self_pos[0]]] = neighbors[i, [self_pos[0], 0]]
    
    return neighbors


def _compute_overlap_from_rankings_optimized(
    lineage_rankings: np.ndarray,
    phenotype_rankings: np.ndarray, 
    radius: int
) -> np.ndarray:
    """Compute overlaps from pre-computed neighbor rankings."""
    n_cells = lineage_rankings.shape[0]
    overlaps = np.zeros(n_cells)
    
    for cell in range(n_cells):
        # Only use first 'radius' neighbors (excluding self at index 0)
        lineage_neighbors = lineage_rankings[cell, 1:radius+1]  # Skip self
        phenotype_neighbors = phenotype_rankings[cell, 1:radius+1]  # Skip self
        
        # Compute intersection size for the radius-specific neighbors
        overlap_size = len(np.intersect1d(lineage_neighbors, phenotype_neighbors))
        overlaps[cell] = overlap_size / radius
    
    return overlaps


def compute_lineage_distances(character_matrix: pd.DataFrame) -> pd.DataFrame:
    """
    Compute pairwise lineage distances from character matrix.
    
    Uses modified Hamming distance that accounts for different mutation states.

    Parameters
    ----------
    character_matrix : pd.DataFrame
        Character matrix with mutation states.

    Returns
    -------
    pd.DataFrame
        Pairwise lineage distance matrix.
    """
    def modified_hamming_distance(x, y):
        """Modified Hamming distance for character states."""
        dists = 2 * (x != y).astype(float) - np.logical_xor(x == 0, y == 0).astype(float)
        nan_mask = np.logical_or(np.isnan(x), np.isnan(y))
        dists[nan_mask] = np.nan
        return np.nanmean(dists)
    
    distances = pairwise_distances(
        character_matrix.values, 
        metric=modified_hamming_distance
    )
    
    return pd.DataFrame(
        distances, 
        index=character_matrix.index, 
        columns=character_matrix.index
    )


def compute_phenotype_distances(
    ad: 'anndata.AnnData',
    latent_space_key: str
) -> pd.DataFrame:
    """
    Compute pairwise phenotypic distances from latent space.

    Parameters
    ----------
    ad : anndata.AnnData
        Annotated data object.
    latent_space_key : str
        Key for latent space coordinates in ad.obsm.

    Returns
    -------
    pd.DataFrame
        Pairwise phenotypic distance matrix.
    """
    if latent_space_key not in ad.obsm:
        raise KeyError(f"Latent space key '{latent_space_key}' not found in ad.obsm")
    
    distances = pairwise_distances(ad.obsm[latent_space_key], metric='euclidean')
    
    return pd.DataFrame(
        distances, 
        index=ad.obs_names, 
        columns=ad.obs_names
    )


def compute_radius_overlaps(
    lineage_distances: pd.DataFrame,
    phenotype_distances: pd.DataFrame,
    radius: int
) -> pd.Series:
    """
    Compute overlaps for a specific radius.

    Parameters
    ----------
    lineage_distances : pd.DataFrame
        Pairwise lineage distances.
    phenotype_distances : pd.DataFrame
        Pairwise phenotypic distances.
    radius : int
        Neighborhood radius.

    Returns
    -------
    pd.Series
        Overlap values for each cell at the specified radius.
    """
    overlaps = []
    
    for cell in lineage_distances.index:
        # Get k-nearest neighbors by lineage
        lineage_neighbors = get_k_nearest_neighbors(lineage_distances, cell, radius)
        
        # Get k-nearest neighbors by phenotype
        phenotype_neighbors = get_k_nearest_neighbors(phenotype_distances, cell, radius)
        
        # Compute overlap
        overlap = len(lineage_neighbors.intersection(phenotype_neighbors)) / radius
        overlaps.append(overlap)
    
    return pd.Series(overlaps, index=lineage_distances.index)


def get_k_nearest_neighbors(
    distance_matrix: pd.DataFrame,
    cell: str,
    k: int
) -> set:
    """
    Get k-nearest neighbors for a cell.

    Parameters
    ----------
    distance_matrix : pd.DataFrame
        Pairwise distance matrix.
    cell : str
        Query cell name.
    k : int
        Number of neighbors to return.

    Returns
    -------
    set
        Set of k-nearest neighbor cell names.
    """
    distances = distance_matrix.loc[cell].drop(cell)  # Exclude self
    return set(distances.nsmallest(k).index)

