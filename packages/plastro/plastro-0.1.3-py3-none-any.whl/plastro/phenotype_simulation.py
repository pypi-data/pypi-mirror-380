"""
Phenotype simulation module for generating synthetic single-cell data.

This module provides functions for creating synthetic single-cell datasets with
branching differentiation trajectories, simulating realistic cellular development
patterns and phenotypic transitions for testing plasticity algorithms.
"""

import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from anndata import AnnData
import scanpy as sc
from typing import Tuple, List, Optional

# Note: HIDE_PLOTS is now controlled per function via show_plots parameter


def create_random_binary_tree(n_leaves: int, sample_res: int) -> Tuple:
    """
    Create a binary tree with random distribution of leaves.
    
    Generates a random binary tree structure for simulating cellular differentiation
    hierarchies. Each node represents a cellular state with a certain number of cells,
    and the tree structure represents the developmental relationships.

    Parameters
    ----------
    n_leaves : int
        Total number of terminal branches (leaf nodes) in the tree.
    sample_res : int
        Sample resolution multiplier that determines the number of cells per node.
        Each node will have between 1-10 times this value as the number of cells.

    Returns
    -------
    Tuple
        A tuple representing the binary tree structure:
        - First element: number of samples at this node (int)
        - Second element: list of child branches (empty for leaf nodes)

    Examples
    --------
    >>> tree = create_random_binary_tree(n_leaves=4, sample_res=50)
    >>> # Creates a tree with 4 terminal branches, each with ~50-500 cells
    
    Notes
    -----
    The tree structure is represented as nested tuples where:
    - Leaf nodes: (sample_count, [])
    - Internal nodes: (sample_count, [left_child, right_child])
    
    This creates a realistic branching structure similar to cellular development
    where progenitor cells give rise to more specialized cell types.
    """
    if n_leaves == 1:
        # Terminal node - return as leaf with random sample count
        return (random.randint(1, 10) * sample_res, [])

    # Randomly distribute leaves between left and right branches
    left_leaves = random.randint(1, n_leaves - 1)
    right_leaves = n_leaves - left_leaves

    # Recursively create child branches
    left_branch = create_random_binary_tree(left_leaves, sample_res)
    right_branch = create_random_binary_tree(right_leaves, sample_res)

    # Current node's sample count
    node_samples = random.randint(1, 10) * sample_res

    return (node_samples, [left_branch, right_branch])


def sample_branch(
    base: np.ndarray,
    velocity: np.ndarray,
    sample_structure: Tuple,
    curvature: float = 0.2,
    var_decay: float = 1.5,
    dens_decay: float = 0.9,
    n_dim: int = 15,
    branch_name: str = 'b'
) -> Tuple[List[np.ndarray], List, List[int], List[np.ndarray]]:
    """
    Sample cells along a differentiation branch with realistic noise structure.
    
    Generates synthetic single-cell data along a branching trajectory that mimics
    cellular differentiation. Uses a physics-inspired model where cells follow
    curved paths through gene expression space with decreasing variance over time.

    Parameters
    ----------
    base : np.ndarray
        Starting position in gene expression space (n_dim,).
    velocity : np.ndarray
        Initial direction vector for trajectory (n_dim,).
    sample_structure : Tuple
        Tree structure from create_random_binary_tree defining sampling.
    curvature : float, optional
        Amount of random curvature in trajectory (0-1), by default 0.2.
        Higher values create more curved, realistic paths.
    var_decay : float, optional
        Rate of variance decay along trajectory, by default 1.5.
        Higher values create more focused terminal populations.
    dens_decay : float, optional
        Rate of density decay (cell loss), by default 0.9.
        Models cell death during differentiation.
    n_dim : int, optional
        Number of dimensions (genes) in expression space, by default 15.
    branch_name : str, optional
        Name identifier for this branch, by default 'b'.

    Returns
    -------
    Tuple[List[np.ndarray], List, List[int], List[np.ndarray]]
        - samples: List of cell expression matrices for each sub-branch
        - distributions: List of multivariate normal distributions used
        - n_draws: List of cell counts for each sub-branch  
        - names: List of branch name arrays for each sub-branch

    Examples
    --------
    >>> base = np.zeros(10)
    >>> velocity = np.ones(10)
    >>> structure = (100, [])  # Simple leaf with 100 cells
    >>> samples, dists, counts, names = sample_branch(base, velocity, structure)
    
    Notes
    -----
    The sampling model creates realistic gene expression patterns by:
    - Adding curved random walk behavior via curvature parameter
    - Implementing variance decay to model cellular commitment
    - Using QR decomposition to create proper covariance structure
    - Applying density decay to model cell loss during development
    """
    n_draws, sub_struct = sample_structure
    
    # Calculate trajectory curvature and noise
    scale = np.sqrt(np.sum(velocity**2))
    delta = np.random.normal(0, scale, n_dim)
    new_velocity = (velocity * (1 - curvature) + delta * curvature) * dens_decay
    
    # Update position along trajectory
    mu = base + (new_velocity / 2)
    
    # Create proper covariance structure using QR decomposition
    q, r = np.linalg.qr(new_velocity[:, None], mode='complete')
    mr = 5e-1 * np.exp(-np.arange(n_dim) * var_decay / 2) * np.abs(r[0])
    mr = np.clip(mr, 1e-4 * np.abs(r[0]), None)
    bases = q * mr[None, :]
    cov = bases.dot(bases.T)
    
    # Sample cells from multivariate normal distribution
    dist = multivariate_normal(mu, cov)
    samples = dist.rvs(n_draws)
    
    # Initialize return lists
    samp_list = [samples]
    dist_list = [dist]
    draws_list = [n_draws]
    name_list = [np.repeat(branch_name, n_draws)]
    
    # Update base position for child branches
    new_base = base + new_velocity
    
    # Recursively sample child branches
    for i, ss in enumerate(sub_struct):
        child_samples, child_dist, child_n_draws, child_names = sample_branch(
            new_base, new_velocity, ss, 
            curvature=curvature, 
            var_decay=var_decay,
            n_dim=n_dim, 
            branch_name=f'{branch_name}-{i}',
        )
        samp_list += child_samples
        dist_list += child_dist
        draws_list += child_n_draws
        name_list += child_names
        
    return samp_list, dist_list, draws_list, name_list


def generate_ad(sample_structure: Tuple, n_dim: int, show_plots: bool = False) -> AnnData:
    """
    Generate a complete AnnData object with simulated single-cell data.
    
    Creates a comprehensive single-cell dataset with realistic gene expression
    patterns, UMAP embedding, clustering annotations, and proper metadata for
    studying cellular plasticity and differentiation.

    Parameters
    ----------
    sample_structure : Tuple
        Binary tree structure from create_random_binary_tree.
    n_dim : int
        Number of dimensions (genes) in the expression space.
    show_plots : bool, optional
        Whether to display plots during computation, by default False.

    Returns
    -------
    AnnData
        Complete annotated dataset containing:
        - X: Gene expression matrix (n_cells × n_genes)
        - obs: Cell metadata with ground truth, branch labels, colors
        - obsm: Dimensionality reductions (UMAP, diffusion components)
        - uns: Cluster colors and other metadata

    Examples
    --------
    >>> structure = create_random_binary_tree(n_leaves=6, sample_res=100)
    >>> adata = generate_ad(structure, n_dim=20)
    >>> print(f"Generated {adata.n_obs} cells with {adata.n_vars} genes")
    >>> 
    >>> # Visualize the simulated data
    >>> import scanpy as sc
    >>> sc.pl.umap(adata, color='branch')
    >>> 
    >>> # Generate with plots enabled
    >>> adata_with_plots = generate_ad(structure, n_dim=20, show_plots=True)

    Notes
    -----
    The generated dataset includes:
    - Realistic branching trajectories in gene expression space
    - Ground truth probability densities for each cell
    - UMAP coordinates for visualization
    - Leiden clustering annotations
    - Color maps for consistent plotting
    - Diffusion components for plasticity analysis
    
    This provides a complete testing framework for plasticity algorithms
    with known ground truth cellular relationships.
    """
    # Generate samples along all branches
    sample_list, distributions, draws_list, name_list = sample_branch(
        np.zeros(n_dim), np.ones(n_dim), sample_structure, n_dim=n_dim
    )

    # Combine all samples
    samples = np.concatenate(sample_list, axis=0)
    n_draws = np.array(draws_list)
    weights = n_draws / np.sum(n_draws)
    
    # Compute ground truth probability density
    pdf = np.zeros(np.sum(n_draws))
    for w, dist in zip(weights, distributions):
        pdf += w * dist.pdf(samples)

    # Create AnnData object
    sim_ad = AnnData(
        samples,
        obs=pd.DataFrame({
            'ground_truth': pdf,
            'log_ground_truth': np.log10(pdf),
            'branch': np.concatenate(name_list, axis=0),
        }, index=np.arange(np.sum(n_draws)).astype(str))
    )
    
    # Set proper cell and branch names
    sim_ad.obs['branch_name'] = sim_ad.obs['branch'].astype('category')
    sim_ad.obs_names = 'Cell_' + sim_ad.obs_names.astype(str)
    sim_ad.obsm['X_dc'] = sim_ad.to_df().values

    # Compute UMAP embedding
    sc.pp.neighbors(sim_ad, n_neighbors=30, use_rep='X')
    sc.tl.umap(sim_ad)

    # Generate branch colors using tab20 colormap
    unique_branches = sim_ad.obs['branch'].unique()
    tab20_colors = plt.cm.get_cmap('tab20', len(unique_branches))
    colors = {
        cell_type: rgba_to_hex(tab20_colors(i)) 
        for i, cell_type in enumerate(unique_branches)
    }

    sim_ad.uns['branch_colors'] = [colors[branch] for branch in unique_branches]
    sim_ad.obs['branch_colors'] = [colors[branch] for branch in sim_ad.obs['branch']]

    # Compute Leiden clustering (optional, requires igraph)
    try:
        sc.pp.neighbors(sim_ad, n_neighbors=30)
        sc.tl.leiden(sim_ad)
    except ImportError:
        print("Warning: igraph not available, skipping Leiden clustering")
        print("Install with: pip install igraph")
        # Create dummy leiden clusters based on branches
        unique_branches = sim_ad.obs['branch'].unique()
        branch_to_leiden = {branch: str(i) for i, branch in enumerate(unique_branches)}
        sim_ad.obs['leiden'] = sim_ad.obs['branch'].map(branch_to_leiden)

    # Generate leiden cluster colors
    unique_clusters = sim_ad.obs['leiden'].unique()
    set2_colors = plt.cm.get_cmap('tab20', len(unique_clusters))
    colors = {
        cell_type: rgba_to_hex(set2_colors(i)) 
        for i, cell_type in enumerate(unique_clusters)
    }

    sim_ad.uns['leiden_colors'] = [colors[cluster] for cluster in unique_clusters]
    sim_ad.obs['leiden_colors'] = [colors[cluster] for cluster in sim_ad.obs['leiden']]

    return sim_ad


def subset_to_terminal_branches(ad: AnnData, show_plots: bool = False) -> AnnData:
    """
    Extract only terminal branches from simulated differentiation data.
    
    Identifies and extracts cells from terminal (leaf) branches of the 
    differentiation tree. These represent fully differentiated cell types
    and are commonly used for lineage tracing analysis.

    Parameters
    ----------
    ad : AnnData
        Annotated data object with branch annotations in obs['branch'].
    show_plots : bool, optional
        Whether to display the terminal branches visualization, by default False.

    Returns
    -------
    AnnData
        Subset containing only cells from terminal branches.

    Examples
    --------
    >>> # Generate full differentiation tree
    >>> structure = create_random_binary_tree(n_leaves=4, sample_res=100)
    >>> full_data = generate_ad(structure, n_dim=15)
    >>> 
    >>> # Extract only terminal cell types
    >>> terminal_data = subset_to_terminal_branches(full_data)
    >>> print(f"Reduced from {full_data.n_obs} to {terminal_data.n_obs} cells")
    >>> 
    >>> # Show terminal branch visualization
    >>> terminal_data = subset_to_terminal_branches(full_data, show_plots=True)

    Notes
    -----
    Terminal branches are identified as branch names that are not prefixes
    of any other branch names. For example, in branches ['b', 'b-0', 'b-0-1'],
    only 'b-0-1' would be considered terminal.
    
    This function also creates a visualization showing the terminal branches
    highlighted in red on the UMAP embedding.
    """
    sim_ad = ad.copy()
    
    # Get all branch names
    branch_names = sim_ad.obs['branch'].unique()
    
    # Find terminal branches (not prefixes of other branches)
    terminal_branches = []
    for branch_name in branch_names:
        # Check if this branch name is a prefix of any other branch
        is_terminal = not any(
            other_branch_name.startswith(branch_name) and branch_name != other_branch_name
            for other_branch_name in branch_names
        )
        if is_terminal:
            terminal_branches.append(branch_name)

    # Visualize terminal vs intermediate branches
    plt.figure(figsize=(5, 5))
    plt.scatter(sim_ad.obsm['X_umap'][:, 0], sim_ad.obsm['X_umap'][:, 1], 
               c='grey', s=0.5, alpha=0.5, label='Intermediate')
    
    terminal_mask = sim_ad.obs['branch'].isin(terminal_branches)
    plt.scatter(sim_ad.obsm['X_umap'][terminal_mask, 0],
                sim_ad.obsm['X_umap'][terminal_mask, 1], 
                c='red', s=0.5, label='Terminal')
    
    plt.axis('off')
    plt.legend()
    plt.title('Terminal Branches (Red)')
    
    if show_plots:
        plt.show()
    else:
        plt.close()

    # Subset to only terminal branches
    sim_ad = sim_ad[terminal_mask, :].copy()
    
    print(f"Selected {len(terminal_branches)} terminal branches:")
    for branch in terminal_branches:
        n_cells = sum(sim_ad.obs['branch'] == branch)
        print(f"  {branch}: {n_cells} cells")

    return sim_ad


def rgba_to_hex(rgba: Tuple) -> str:
    """
    Convert RGBA color to hexadecimal format.
    
    Utility function for converting matplotlib color tuples to hex strings
    for consistent color handling across different plotting libraries.

    Parameters
    ----------
    rgba : Tuple
        RGBA color tuple with values either as floats (0-1) or integers (0-255).

    Returns
    -------
    str
        Hexadecimal color string in format '#RRGGBBAA'.

    Examples
    --------
    >>> rgba_to_hex((1.0, 0.5, 0.0, 1.0))  # Orange, full opacity
    '#ff8000ff'
    >>> rgba_to_hex((255, 128, 0, 255))     # Same color, integer format  
    '#ff8000ff'
    """
    # Convert float values (0-1) to integers (0-255) if necessary
    if any(isinstance(component, float) for component in rgba):
        rgba = tuple(
            int(component * 255) if isinstance(component, float) else component 
            for component in rgba
        )

    return "#{:02x}{:02x}{:02x}{:02x}".format(*rgba)


def simulate_realistic_dataset(
    n_cell_types: int = 6,
    cells_per_type: int = 100,
    n_genes: int = 20,
    noise_level: float = 0.2,
    seed: Optional[int] = None,
    show_plots: bool = False
) -> AnnData:
    """
    Generate a realistic single-cell dataset for plasticity testing.
    
    Convenience function that combines tree generation and sampling to create
    a complete synthetic dataset with realistic parameters for testing
    plasticity simulation algorithms.

    Parameters
    ----------
    n_cell_types : int, optional
        Number of terminal cell types to generate, by default 6.
    cells_per_type : int, optional
        Approximate number of cells per cell type, by default 100.
    n_genes : int, optional
        Number of genes (dimensions) in expression space, by default 20.
    noise_level : float, optional
        Amount of noise in trajectories (0-1), by default 0.2.
    seed : int, optional
        Random seed for reproducibility, by default None.
    show_plots : bool, optional
        Whether to display plots during dataset generation, by default False.

    Returns
    -------
    AnnData
        Complete annotated dataset ready for plasticity analysis.

    Examples
    --------
    >>> # Generate a standard test dataset
    >>> adata = simulate_realistic_dataset(
    ...     n_cell_types=8, 
    ...     cells_per_type=150,
    ...     n_genes=25,
    ...     seed=42,
    ...     show_plots=True  # Display terminal branch plots
    ... )
    >>> 
    >>> # Visualize the dataset
    >>> import scanpy as sc
    >>> sc.pl.umap(adata, color=['branch', 'leiden'])
    
    Notes
    -----
    This function provides sensible defaults for most plasticity simulation
    experiments and ensures reproducible results when a seed is provided.
    """
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    
    # Create tree structure
    sample_res = cells_per_type // 5  # Adjust for realistic cell counts
    tree_structure = create_random_binary_tree(n_cell_types, sample_res)
    
    # Generate the dataset
    adata = generate_ad(tree_structure, n_genes, show_plots=show_plots)
    
    print(f"Generated realistic dataset:")
    print(f"  {adata.n_obs} cells")
    print(f"  {adata.n_vars} genes") 
    print(f"  {len(adata.obs['branch'].unique())} branches")
    print(f"  {len(adata.obs['leiden'].unique())} leiden clusters")
    
    return adata