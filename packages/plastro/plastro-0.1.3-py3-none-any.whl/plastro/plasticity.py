"""
Core plasticity simulation module.

This module provides functions for simulating different types of cellular plasticity
in single-cell datasets, including random walk plasticity and cluster-based switching.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import networkx as nx
try:
    import walker
    HAS_WALKER = True
except ImportError:
    HAS_WALKER = False
    walker = None 
import scanpy as sc
try:
    from ete3 import Tree, TreeStyle, NodeStyle, TextFace
except ImportError:
    # Handle different ete3 import structures
    try:
        from ete3 import Tree
        from ete3.treeview import TreeStyle, NodeStyle, TextFace
    except ImportError:
        from ete3 import Tree
        TreeStyle = NodeStyle = TextFace = None
from typing import Dict, List, Optional, Tuple, Union
import anndata

def random_walk_plasticity(
        full_simulated_ad: anndata.AnnData,
        subset_simulated_ad: anndata.AnnData,
        plastic_cells: Dict[str, List[str]],
        walk_lengths: Dict[str, int],
        latent_space_key: str = 'X_dc'
) -> anndata.AnnData:
    """
    Simulate random walk plasticity in single cells.
    
    Performs random walks on specified plastic cells to simulate phenotypic transitions.
    Plastic cells from different leiden clusters perform walks of specified lengths, 
    and their phenotypes are replaced with their walk targets.

    Parameters
    ----------
    full_simulated_ad : anndata.AnnData
        Complete simulated dataset used for performing random walks.
    subset_simulated_ad : anndata.AnnData
        Subset of the dataset containing cells to be analyzed.
    plastic_cells : Dict[str, List[str]]
        Dictionary mapping leiden cluster identifiers to lists of cell names
        that will undergo plastic transitions.
    walk_lengths : Dict[str, int]
        Dictionary mapping leiden cluster identifiers to walk lengths.
        Must contain entries for all keys in plastic_cells.
    latent_space_key : str, optional
        Key in the obsm attribute of the AnnData object that contains the latent space representation.
        Default is 'X_dc'.

    Returns
    -------
    anndata.AnnData
        Modified dataset with plastic cells replaced by their walk targets.
        Non-plastic cells remain unchanged.

    Raises
    ------
    AssertionError
        If walk_lengths keys don't match plastic_cells keys.

    Examples
    --------
    >>> plastic_cells = {'0': ['Cell_1', 'Cell_2'], '1': ['Cell_3']}
    >>> walk_lengths = {'0': 100, '1': 50}
    >>> result = random_walk_plasticity(full_ad, subset_ad, plastic_cells, walk_lengths)
    
    Notes
    -----
    This function modifies cell phenotypes by replacing plastic cells with cells
    that represent their final positions after random walks. The walk parameters
    (p, q) are set within the perform_random_walk function.
    """

    assert set(walk_lengths.keys()) == set(plastic_cells.keys()), "Walk lengths must be specified for each selected leiden cluster"
    all_plastic_cells = [cell for cells in plastic_cells.values() for cell in cells]
    updated_ad_list = []
    for lc in plastic_cells:
        print(f"Leiden cluster {lc}: {len(plastic_cells[lc])} plastic cells will perform random walks of length {walk_lengths[lc]}")
        input_ad = full_simulated_ad.copy()
        # Allow these cells to perform a random walk
        targets, change_in_phenotype, walks = perform_random_walk(
            input_ad,
            plastic_cells=plastic_cells[lc],
            walk_length=walk_lengths[lc],
            latent_space_key=latent_space_key,
        )

        # We will replace the phenotypes of these plastic cells with their target phenotypes
        updated_phenotypes = input_ad[targets['target']].copy()
        updated_phenotypes.obs_names = targets.index.values
        updated_ad_list.append(updated_phenotypes)

    # Combine all updated phenotypes with the non-plastic cells. We will remove all the plastic cells from the original ad and combine with the updated ones
    non_plastic_cells = subset_simulated_ad.obs_names[~subset_simulated_ad.obs_names.isin(all_plastic_cells)].to_list()
    non_plastic_ad = subset_simulated_ad[non_plastic_cells].copy()
    # Concatenate the non-plastic cells with the updated plastic cells
    final_ad = anndata.concat([non_plastic_ad] + updated_ad_list)
    final_ad.obs['leiden'] = final_ad.obs['leiden'].astype(str)

    # Remove the -0 suffix from obs_names
    final_ad.obs_names = [x.split('-')[0] for x in final_ad.obs_names]

    assert final_ad.shape[0] == subset_simulated_ad.shape[0], "Final dataset should have the same number of cells as the input subset"
    assert set(final_ad.obs_names) == set(subset_simulated_ad.obs_names), "Final dataset should have the same cells as the input subset"

    final_ad = final_ad[final_ad.obs_names]
    subset_simulated_ad = subset_simulated_ad[final_ad.obs_names]

    # Compute change_in_phenotype: Euclidean distance between original and new latent space coordinates
    if latent_space_key in subset_simulated_ad.obsm and latent_space_key in final_ad.obsm:
        # Since we know the datasets have identical cell names, we can align directly
        original_coords = subset_simulated_ad.obsm[latent_space_key]
        new_coords = final_ad.obsm[latent_space_key]
        
        # Vectorized computation for all cells at once
        change_distances = np.linalg.norm(new_coords - original_coords, axis=1)
        
        # Assign distances to all cells
        final_ad.obs['change_in_phenotype'] = change_distances

    return final_ad

def perform_random_walk(
    ad,
    plastic_cells: Optional[List[str]] = None,
    latent_space_key: str = 'X_dc',
    walk_length: int = 100,
    p: float = 0.9,
    q: float = 1e-10,
    save_dir: Optional[str] = None
) -> Tuple[pd.DataFrame, pd.DataFrame, np.ndarray]:
    """
    Perform random walks on a phenotypic graph.
    
    Constructs a k-nearest neighbor graph from the latent space representation
    and performs random walks to simulate cellular transitions.

    Parameters
    ----------
    ad : anndata.AnnData
        Annotated data object containing latent space annotations.
    plastic_cells : List[str], optional
        List of cell names to perform random walks on. If None, all cells
        are considered, by default None.
    latent_space_key : str, optional
        Key in `ad.obsm` where latent space coordinates are stored, by default 'X_dc'.
    walk_length : int, optional
        Length of each random walk, by default 100.
    p : float, optional
        Return probability - controls likelihood of revisiting previous node, by default 0.9.
    q : float, optional
        In-out probability - controls exploration vs exploitation, by default 1e-10.
    save_dir : str, optional
        Directory to save walk results, by default None.

    Returns
    -------
    Tuple[pd.DataFrame, pd.DataFrame, np.ndarray]
        - walk_df: DataFrame with start and target cells for each walk
        - change_in_phenotype: DataFrame with graph distances moved
        - walks: Array of walk indices for each cell

    Examples
    --------
    >>> targets, changes, walks = perform_random_walk(ad, ['Cell_1', 'Cell_2'], walk_length=50)
    >>> print(f"Cell_1 moved to: {targets.loc['Cell_1', 'target']}")
    
    Notes
    -----
    - Uses Node2Vec-style random walks with parameters p and q
    - Higher p values encourage returning to previous nodes
    - Lower q values encourage exploration of new regions
    """
    F = construct_phenotypic_graph(ad, latent_space_key, n_nbrs=10)

    # Perform random walks
    walks = walker.random_walks(F, n_walks=1, walk_len=walk_length, p=p, q=q)
    final_nodes = np.array(F.nodes)[walks[:, -1]]
    start_nodes = np.array(F.nodes)[walks[:, 0]]

    # Create result dataframes
    walk_df = pd.DataFrame({'start': start_nodes, 'target': final_nodes}).set_index('start')
    change_in_phenotype = pd.DataFrame(get_distances_of_moves(F, start_nodes, final_nodes))
    change_in_phenotype.columns = ['change_in_phenotype']
    change_in_phenotype.index = walk_df.index

    # Filter to specified plastic cells if provided
    if plastic_cells is not None:
        cell_ix = [ad.obs_names.get_loc(cell) for cell in plastic_cells]
        walk_df = walk_df.loc[plastic_cells]
        change_in_phenotype = change_in_phenotype.loc[plastic_cells]
        walks = walks[cell_ix, :]

    return walk_df, change_in_phenotype, walks

def get_distances_of_moves(
    G: nx.Graph,
    sources: List[str],
    targets: List[str]
) -> np.ndarray:
    """
    Compute shortest path distances between source and target nodes.

    Parameters
    ----------
    G : networkx.Graph
        Graph representing phenotypic connectivity.
    sources : List[str]
        List of source node names.
    targets : List[str]
        List of target node names.

    Returns
    -------
    np.ndarray
        Array of shortest path distances between corresponding source-target pairs.

    Raises
    ------
    AssertionError
        If sources and targets have different lengths.
    """
    if len(sources) != len(targets):
        raise ValueError("Sources and targets must have the same length")

    dists = []
    for source, target in zip(sources, targets):
        dists.append(len(nx.shortest_path(G, source=source, target=target)))
    return np.array(dists)

def construct_phenotypic_graph(
    ad: anndata.AnnData,
    latent_space_key: str,
    n_nbrs: int = 10
) -> nx.Graph:
    """
    Construct a k-nearest neighbor graph from latent space coordinates.

    Parameters
    ----------
    ad : anndata.AnnData
        Annotated data object.
    latent_space_key : str
        Key in `ad.obsm` containing latent space coordinates.
    n_nbrs : int, optional
        Number of nearest neighbors for graph construction, by default 10.

    Returns
    -------
    networkx.Graph
        Graph where nodes are cells and edges connect nearest neighbors.
    """
    ad = ad.copy()
    sc.pp.neighbors(ad, n_neighbors=n_nbrs, use_rep=latent_space_key)
    
    F = graph_from_connectivities(ad.obsp['connectivities'], ad.obs_names)
    return F

def graph_from_connectivities(adj_matrix, cell_names: List[str]) -> nx.Graph:
    """
    Convert sparse adjacency matrix to NetworkX graph.

    Parameters
    ----------
    adj_matrix : scipy.sparse.csr_matrix
        Sparse adjacency matrix where 1 indicates connected nodes.
    cell_names : List[str]
        List of cell names corresponding to matrix rows/columns.

    Returns
    -------
    networkx.Graph
        Graph with nodes labeled by cell names.

    Raises
    ------
    AttributeError
        If adj_matrix is not a supported sparse matrix type.
    """
    from scipy.sparse import csr_matrix
    
    if isinstance(adj_matrix, csr_matrix):
        H = nx.from_scipy_sparse_array(adj_matrix)
        nx.relabel_nodes(H, dict(zip(H.nodes(), cell_names)), copy=False)
        return H
    else:
        raise AttributeError(f'graph_from_connectivities not implemented for {type(adj_matrix)}')

def visualize_walk(
    ad: anndata.AnnData,
    walk_indices: np.ndarray,
    save_to: Optional[str] = None,
    show_plots: bool = False
) -> None:
    """
    Visualize a random walk path on UMAP coordinates.
    
    Creates a scatter plot showing the path of a single random walk,
    with origin and target cells highlighted.

    Parameters
    ----------
    ad : anndata.AnnData
        AnnData object containing UMAP coordinates in `obsm['X_umap']`.
    walk_indices : np.ndarray
        1D array of cell indices representing the walk path.
    save_to : str, optional
        Directory to save the plot, by default None.
    show_plots : bool, optional
        Whether to display plots interactively, by default False.

    Examples
    --------
    >>> _, _, walks = perform_random_walk(ad, ['Cell_1'])
    >>> visualize_walk(ad, walks[0])
    
    Notes
    -----
    - Requires UMAP coordinates in ad.obsm['X_umap']
    - Origin cell is marked with a black star
    - Target cell is marked with a red star
    - Intermediate cells are colored with a gradient
    """
    if 'X_umap' not in ad.obsm.keys():
        raise KeyError('UMAP coordinates not found in AnnData object')
    
    if not isinstance(walk_indices, np.ndarray):
        raise TypeError('walk_indices must be a numpy array')
    
    if len(walk_indices.shape) != 1 or walk_indices.shape[0] == 0:
        if walk_indices.shape[1] == 1:
            walk_indices = walk_indices.flatten()
        elif walk_indices.shape[0] == 1:
            walk_indices = walk_indices.flatten()
        else:
            raise ValueError('walk_indices must be a 1D array')

    umap_coords = ad.obsm['X_umap']
    colors = sns.color_palette("Wistia", len(walk_indices))

    plt.figure(figsize=(10, 8))
    plt.scatter(umap_coords[:, 0], umap_coords[:, 1], color='grey', s=1, alpha=0.5)

    # Plot walk path
    for idx, cell_idx in enumerate(walk_indices):
        if idx == 0:
            continue
        elif idx == len(walk_indices) - 1:
            plt.scatter(umap_coords[cell_idx, 0], umap_coords[cell_idx, 1], 
                       s=100, color='red', label='Target', marker='*')
        else:
            plt.scatter(umap_coords[cell_idx, 0], umap_coords[cell_idx, 1], 
                       s=5, color=colors[idx])

    # Plot origin
    cell_idx = walk_indices[0]
    plt.scatter(umap_coords[cell_idx, 0], umap_coords[cell_idx, 1], 
               s=100, color='black', label='Origin', marker='*')

    plt.title('UMAP plot with Highlighted Walk')
    plt.legend()
    plt.xlabel('UMAP 1')
    plt.ylabel('UMAP 2')

    if save_to is not None:
        plt.savefig(os.path.join(save_to, 'random_walk.svg'), bbox_inches='tight', dpi=300)
        print(f'Saved plot to {os.path.join(save_to, "random_walk.svg")}')
    
    if show_plots:
        plt.show()
    plt.close()
    
def cluster_switch_plasticity(
    full_simulated_ad: anndata.AnnData,
    subset_simulated_ad: anndata.AnnData,
    plastic_cells: Dict[str, Dict[str, List[str]]],
    column: str = 'leiden',
    latent_space_key: str = 'X_dc'
) -> anndata.AnnData:
    """
    Simulate plasticity through direct cluster switches.

    Replaces plastic cells with randomly selected cells from their target clusters,
    simulating direct phenotypic transitions without intermediate states.

    Parameters
    ----------
    full_simulated_ad : anndata.AnnData
        Complete simulated dataset used for selecting replacement cells.
    subset_simulated_ad : anndata.AnnData
        Subset of the dataset containing cells to be analyzed.
    plastic_cells : Dict[str, Dict[str, List[str]]]
        Dictionary mapping cluster IDs (as strings) to a dictionary with keys 'destination' (target cluster ID as string)
        and 'cells' (list of cell names that will undergo plastic transitions).
    column : str, optional
        Column in obs containing cluster annotations, by default 'leiden'.
    latent_space_key : str, optional
        Key in `obsm` containing latent space coordinates for distance calculation, by default 'X_dc'.

    Returns
    -------
    anndata.AnnData
        Modified dataset with plastic cells replaced by cells from target clusters.
        Includes 'change_in_phenotype' column with Euclidean distance changes in latent space.

    Raises
    ------
    ValueError
        If plastic cells are not found in subset_simulated_ad.

    Examples
    --------
    >>> plastic_cells = {'5': {'destination': '4', 'cells': ['Cell_1', 'Cell_2']}}
    >>> result = cluster_switch_plasticity(full_ad, subset_ad, plastic_cells)

    Notes
    -----
    This function directly replaces plastic cells with cells from random target
    clusters, simulating abrupt phenotypic switches without gradual transitions.
    All cluster IDs are treated as strings for consistency. The 'change_in_phenotype'
    column contains the Euclidean distance between original and new positions in
    latent space (0 for non-plastic cells).
    """
    # Validate that all plastic cells exist in the subset
    all_plastic_cells = sum([plastic_cells[cl]['cells'] for cl in plastic_cells], [])
    missing = [c for c in all_plastic_cells if c not in subset_simulated_ad.obs_names]
    if missing:
        raise ValueError(f"Some plastic cells not found in subset_simulated_ad: {missing}")

    updated_ad_list = []
    for cluster in plastic_cells:
        input_ad = full_simulated_ad.copy()
        target_cluster = plastic_cells[cluster]['destination']

        # Randomly select the correct number of target cells  
        target_cells = input_ad.obs_names[input_ad.obs[column] == target_cluster].to_list()
        n_plastic = len(plastic_cells[cluster]['cells'])
        if len(target_cells) < n_plastic:
            print(f"Warning: Not enough cells in target cluster {target_cluster}. Limiting number of plastic cells to {len(target_cells)}.")
            n_plastic = len(target_cells)
        selected_target_cells = np.random.choice(target_cells, n_plastic, replace=False).tolist()
        targets = pd.DataFrame({'cell': plastic_cells[cluster]['cells'],
                                'target': selected_target_cells}).set_index('cell')

        # We will replace the phenotypes of these plastic cells with their target phenotypes
        updated_phenotypes = input_ad[targets['target']].copy()
        updated_phenotypes.obs_names = targets.index.values
        updated_ad_list.append(updated_phenotypes)

    # Combine all updated phenotypes with the non-plastic cells. We will remove all the plastic cells from the original ad and combine with the updated ones
    non_plastic_cells = subset_simulated_ad.obs_names[~subset_simulated_ad.obs_names.isin(all_plastic_cells)].to_list()
    non_plastic_ad = subset_simulated_ad[non_plastic_cells].copy()
    # Concatenate the non-plastic cells with the updated plastic cells
    final_ad = anndata.concat([non_plastic_ad] + updated_ad_list)
    final_ad.obs['leiden'] = final_ad.obs['leiden'].astype(str)

    # Remove the -0 suffix from obs_names
    final_ad.obs_names = [x.split('-')[0] for x in final_ad.obs_names]

    # Compute change_in_phenotype: Euclidean distance between original and new latent space coordinates
    assert final_ad.shape[0] == subset_simulated_ad.shape[0], "Final dataset should have the same number of cells as the input subset"
    assert set(final_ad.obs_names) == set(subset_simulated_ad.obs_names), "Final dataset should have the same cells as the input subset"

    final_ad = final_ad[final_ad.obs_names]
    subset_simulated_ad = subset_simulated_ad[final_ad.obs_names]

    # Compute change_in_phenotype: Euclidean distance between original and new latent space coordinates
    if latent_space_key in subset_simulated_ad.obsm and latent_space_key in final_ad.obsm:
        # Since we know the datasets have identical cell names, we can align directly
        original_coords = subset_simulated_ad.obsm[latent_space_key]
        new_coords = final_ad.obsm[latent_space_key]
        
        # Vectorized computation for all cells at once
        change_distances = np.linalg.norm(new_coords - original_coords, axis=1)
        
        # Assign distances to all cells
        final_ad.obs['change_in_phenotype'] = change_distances
    return final_ad

def plot_leiden_transitions(full_simulated_ad: anndata.AnnData, 
                             destination_clusters: dict, 
                             show_plots: bool = True,
                             save_to: str = None
                             ) -> None:
    """
    Plots UMAP with arrows indicating transitions between specified leiden clusters.
 
    Parameters
    ----------
    full_simulated_ad : AnnData
        The AnnData object containing the single-cell data with UMAP coordinates and leiden cluster annotations.
    destination_clusters : dict
        A dictionary where keys are source leiden cluster IDs (str) and values are dictionaries with keys:
            - 'destination': target leiden cluster ID (str)
            - 'proportion': proportion of cells to transition (float between 0 and 1)
    show_plots : bool, optional
        Whether to display the plot immediately. Default is True.
    save_to : str, optional
        If provided, the path to save the plot image. Default is None (do not save
    """
    # Ensure UMAP has been computed
    if 'X_umap' not in full_simulated_ad.obsm:
        raise ValueError("UMAP coordinates not found in 'obsm'. Please compute UMAP before plotting.")
    
    # Ensure leiden clustering has been performed
    if 'leiden' not in full_simulated_ad.obs:
        raise ValueError("Leiden clustering not found in 'obs'. Please perform clustering before plotting.")
    
    ##############
    # Plotting
    ##############

    # Plot without immediate display
    sc.pl.umap(
        full_simulated_ad, 
        color='leiden', 
        title='Leiden Clusters', 
        size=40, 
        frameon=False, 
        edges=True, 
        edges_color='black',
        show=False
    )

    ax = plt.gca()

    # Extract UMAP coordinates and Leiden labels
    umap_coords = full_simulated_ad.obsm['X_umap']
    leiden = full_simulated_ad.obs['leiden'].astype(str)

    # Compute centroids
    centroids = {
        cluster: umap_coords[leiden == cluster].mean(axis=0)
        for cluster in np.unique(leiden)
    }

    # Source → Target
    for src in destination_clusters.keys():
        tgt = destination_clusters[src]['destination']
        src_pt, tgt_pt = centroids[src], centroids[tgt]

        # Draw custom arrow
        ax.annotate(
            '',
            xy=tgt_pt, xycoords='data',
            xytext=src_pt, textcoords='data',
            arrowprops=dict(
                lw=2,
                facecolor="black",             # fill color
                edgecolor="white",         # outline color
                mutation_scale=25,         # bigger arrowhead
                shrinkA=5, shrinkB=5       # space around arrow ends
            )
        )

    plt.tight_layout()
    if show_plots:
        plt.show()
    if save_to:
        plt.savefig(save_to)
    
    plt.close()
    return 

def plot_change_in_phenotype(
    ad: anndata.AnnData,
    plastic_ad: anndata.AnnData, 
    all_plastic_cells: List[str],
    latent_space_key: str = 'X_dc',
    show_plots: bool = False,
    save_to: Optional[str] = None
) -> pd.Series:
    """
    Visualize phenotypic changes in plastic cells before and after plasticity simulation.
    
    Creates a three-panel plot showing:
    1. Original data with plastic cells highlighted
    2. Data after plasticity with plastic cells highlighted  
    3. Distribution of phenotypic change distances
    
    Parameters
    ----------
    ad : anndata.AnnData
        Original AnnData object before plasticity simulation.
    plastic_ad : anndata.AnnData
        AnnData object after plasticity simulation.
    all_plastic_cells : List[str]
        List of cell names that underwent plastic transitions.
    latent_space_key : str, optional
        Key in `obsm` containing latent space coordinates for distance calculation, by default 'X_dc'.
    show_plots : bool, optional
        Whether to display plots interactively, by default False.
    save_to : str, optional
        Directory to save the plot, by default None.
        
    Returns
    -------
    pd.Series
        Series containing phenotypic change distances for each plastic cell.
        
    Raises
    ------
    KeyError
        If required keys are not found in the AnnData objects.
    ValueError
        If plastic cells are not found in both datasets.
        
    Examples
    --------
    >>> change_distances = plot_change_in_phenotype(
    ...     original_ad, plastic_ad, ['Cell_1', 'Cell_2'], show_plots=True
    ... )
    >>> print(f"Mean change: {change_distances.mean():.3f}")
    
    Notes
    -----
    - Requires UMAP coordinates in both AnnData objects
    - Requires latent space coordinates for distance calculation
    - Plastic cells must be present in both original and plastic datasets
    """
    # Validate inputs
    if 'X_umap' not in ad.obsm:
        raise KeyError("UMAP coordinates not found in original data. Run sc.tl.umap() first.")
    if 'X_umap' not in plastic_ad.obsm:
        raise KeyError("UMAP coordinates not found in plastic data. Run sc.tl.umap() first.")
    if latent_space_key not in ad.obsm:
        raise KeyError(f"Latent space key '{latent_space_key}' not found in original data.")
    if latent_space_key not in plastic_ad.obsm:
        raise KeyError(f"Latent space key '{latent_space_key}' not found in plastic data.")
    if 'leiden' not in ad.obs:
        raise KeyError("Leiden clustering not found in original data. Run sc.tl.leiden() first.")
    if 'leiden' not in plastic_ad.obs:
        raise KeyError("Leiden clustering not found in plastic data. Run sc.tl.leiden() first.")
    
    # Check if plastic cells exist in both datasets
    original_cells = set(ad.obs_names)
    plastic_cells_set = set(all_plastic_cells)
    plastic_dataset_cells = set(plastic_ad.obs_names)
    
    missing_original = plastic_cells_set - original_cells
    missing_plastic = plastic_cells_set - plastic_dataset_cells
    
    if missing_original:
        raise ValueError(f"Plastic cells not found in original dataset: {list(missing_original)[:5]}...")
    if missing_plastic:
        raise ValueError(f"Plastic cells not found in plastic dataset: {list(missing_plastic)[:5]}...")

    # Compute diffusion change distances
    prev_coords = pd.DataFrame(ad.obsm[latent_space_key], index=ad.obs_names).loc[all_plastic_cells]
    new_coords = pd.DataFrame(plastic_ad.obsm[latent_space_key], index=plastic_ad.obs_names).loc[all_plastic_cells]
    change_distances = np.linalg.norm(new_coords.values - prev_coords.values, axis=1)
    change_distances_series = pd.Series(change_distances, index=all_plastic_cells, name='phenotypic_change_distance')

    # Set up custom subplot widths
    fig, axs = plt.subplots(
        1, 3, figsize=(20, 6), 
        gridspec_kw={"width_ratios": [2, 2, 1]}  # make last panel narrower
    )

    # Panel 1: original data with plastic cells outlined
    sc.pl.umap(
        ad,
        color="leiden",
        title="Original Data with Plastic Cells Highlighted",
        size=40,
        frameon=False,
        edges=True,
        edges_color="black",
        ax=axs[0],
        show=False
    )

    umap1 = pd.DataFrame(ad.obsm['X_umap'], index=ad.obs_names)
    axs[0].scatter(
        umap1.loc[all_plastic_cells, 0],
        umap1.loc[all_plastic_cells, 1],
        s=40, facecolors='none', edgecolors='black', linewidth=1,
        label=f'Plastic cells (n={len(all_plastic_cells)})'
    )

    # Panel 2: after plasticity with plastic cells outlined
    sc.pl.umap(
        plastic_ad,
        color="leiden",
        title="After Plasticity (Plastic Cells Outlined)",
        size=40,
        frameon=False,
        edges=True,
        edges_color="black",
        ax=axs[1],
        show=False
    )

    umap2 = pd.DataFrame(plastic_ad.obsm['X_umap'], index=plastic_ad.obs_names)
    axs[1].scatter(
        umap2.loc[all_plastic_cells, 0],
        umap2.loc[all_plastic_cells, 1],
        s=40, facecolors='none', edgecolors='black', linewidth=1,
        label=f'Plastic cells (n={len(all_plastic_cells)})'
    )

    # Panel 3: distribution of phenotypic change distances
    sns.histplot(change_distances, bins=30, kde=True, ax=axs[2], alpha=0.7)
    axs[2].set_title("Phenotypic Change Distribution")
    axs[2].set_xlabel(f"Change Distance ({latent_space_key})")
    axs[2].set_ylabel("Count")
    
    # Add summary statistics to the histogram
    mean_change = change_distances.mean()
    median_change = np.median(change_distances)
    axs[2].axvline(mean_change, color='red', linestyle='--', label=f'Mean: {mean_change:.3f}')
    axs[2].axvline(median_change, color='orange', linestyle=':', label=f'Median: {median_change:.3f}')

    plt.tight_layout()
    if show_plots:
        plt.show()
    if save_to:
        plt.savefig(save_to)
    
    plt.close()
    return 