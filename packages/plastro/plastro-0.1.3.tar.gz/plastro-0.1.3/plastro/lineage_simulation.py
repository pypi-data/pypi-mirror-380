"""
Lineage simulation module for CRISPR-based lineage tracing.

This module provides functions for simulating lineage tracing data,
constructing phylogenetic trees from single-cell data, and introducing
CRISPR-based mutations to create realistic lineage relationships for 
plasticity analysis.
"""

import numpy as np
import pandas as pd
import os
from typing import Optional
from ete3 import Tree


def simulate_lineage_tracing(
    sim_ad: 'anndata.AnnData',
    terminal_ad: 'anndata.AnnData',
    latent_space_key: str = 'X_dc',
    number_of_cassettes: int = 100,
    save_to: Optional[str] = None
) -> 'cassiopeia.data.CassiopeiaTree':
    """
    Simulate lineage tracing using Cassiopeia on single-cell data.
    
    Builds a phylogenetic tree from latent space coordinates and simulates
    CRISPR-based lineage tracing to generate character matrices.

    Parameters
    ----------
    sim_ad : anndata.AnnData
        Complete simulated single-cell dataset.
    terminal_ad : anndata.AnnData
        Subset containing only terminal/observed cells.
    latent_space_key : str, optional
        Key in `sim_ad.obsm` containing latent space coordinates, by default 'X_dc'.
    number_of_cassettes : int, optional
        Number of mutation sites, by default 100 so we can accurately resolve lineage relationships.
    save_to : str, optional
        Directory to save tree and results, by default None.

    Returns
    -------
    cassiopeia.data.CassiopeiaTree
        Cassiopeia tree object with character matrix and phylogenetic structure.

    Examples
    --------
    >>> import plastro
    >>> # Assume sim_ad contains full simulated data and terminal_ad contains observed cells
    >>> cass_tree = plastro.simulate_lineage_tracing(sim_ad, terminal_ad, 'X_dc')
    >>> character_matrix = cass_tree.character_matrix
    >>> print(f"Character matrix shape: {character_matrix.shape}")

    Notes
    -----
    This function combines tree construction from phenotypic similarity with
    CRISPR mutation simulation to create realistic lineage tracing data that
    can be used for plasticity analysis.
    """
    # Construct initial tree from latent space
    tree = construct_tree(sim_ad, terminal_ad, latent_space_key=latent_space_key, save_to=save_to)
    
    # Add CRISPR mutations
    cass_tree = introduce_crispr_mutations(tree, number_of_cassettes=number_of_cassettes)
    
    return cass_tree


def construct_tree(
    sim_ad: 'anndata.AnnData',
    terminal_ad: 'anndata.AnnData',
    latent_space_key: str = 'X_dc',
    save_to: Optional[str] = None
) -> Tree:
    """
    Construct phylogenetic tree from latent space coordinates.
    
    Uses neighbor-joining algorithm on distances computed from latent space
    to build a phylogenetic tree representing cellular relationships.

    Parameters
    ----------
    sim_ad : anndata.AnnData
        Complete simulated dataset with latent space coordinates.
    terminal_ad : anndata.AnnData
        Terminal/observed cells to include in the tree.
    latent_space_key : str, optional
        Key for latent space coordinates in `sim_ad.obsm`, by default 'X_dc'.
    save_to : str, optional
        Directory to save the tree file, by default None.

    Returns
    -------
    ete3.Tree
        Phylogenetic tree of the cells.

    Raises
    ------
    KeyError
        If latent_space_key is not found in sim_ad.obsm.
    ValueError
        If no suitable root cell is found.

    Examples
    --------
    >>> tree = construct_tree(sim_ad, terminal_ad, latent_space_key='X_dc')
    >>> print(f"Tree has {len(tree.get_leaves())} leaves")
    >>> tree.show()  # Display tree visualization
    """
    if latent_space_key not in sim_ad.obsm:
        raise KeyError(f"Latent space key '{latent_space_key}' not found in sim_ad.obsm")
    
    # Extract latent space coordinates
    dcs = pd.DataFrame(sim_ad.obsm[latent_space_key])
    dcs.index = sim_ad.obs_names

    # Select random root cell from branch 'b' if available, otherwise from any branch
    try:
        root_candidates = sim_ad.obs_names[sim_ad.obs['branch_name'] == 'b']
        if len(root_candidates) == 0:
            # Fallback to any branch if 'b' doesn't exist
            root_candidates = sim_ad.obs_names
        root = np.random.choice(root_candidates)
    except KeyError:
        # If branch_name column doesn't exist, select random cell
        root = np.random.choice(sim_ad.obs_names)
        print("Warning: 'branch_name' column not found, selecting random root")

    # Subset to terminal cells + root
    cells_to_include = list(terminal_ad.obs_names) + [root]
    cells_to_include = list(set(cells_to_include))  # Remove duplicates
    dcs = dcs.loc[cells_to_include, :]

    # Compute pairwise distance matrix
    from scipy.spatial.distance import pdist, squareform
    dists = pd.DataFrame(squareform(pdist(dcs, metric='euclidean')))
    dists.index = dcs.index
    dists.columns = dcs.index

    # Import neighbor joining from phylo module
    from .phylo import neighbor_joining
    
    # Construct tree using neighbor joining
    tree = neighbor_joining(dists, outgroup=root)

    # Keep only terminal/observed cells
    terminal_names = list(terminal_ad.obs_names)
    tree.prune(terminal_names, preserve_branch_length=True)
    
    # Make tree ultrametric (equal distances from root to all leaves)
    tree.convert_to_ultrametric()
    
    if save_to is not None:
        tree_file = os.path.join(save_to, 'simulated_tree.nwk')
        tree.write(outfile=tree_file, format=1)
        print(f"Saved tree to {tree_file}")

    return tree


def introduce_crispr_mutations(tree: Tree, number_of_cassettes: int = 100) -> 'cassiopeia.data.CassiopeiaTree':
    """
    Simulate CRISPR mutations on a phylogenetic tree.
    
    Uses Cassiopeia's mutation simulation to add realistic CRISPR-based
    lineage tracing mutations to the tree structure.

    Parameters
    ----------
    tree : ete3.Tree
        Phylogenetic tree to add mutations to.
    number_of_cassettes : int, optional
        Number of mutation sites, by default 100 so we can accurately resolve lineage relationships.
    Returns
    -------
    cassiopeia.data.CassiopeiaTree
        Tree with simulated character matrix containing mutation data.

    Examples
    --------
    >>> from ete3 import Tree
    >>> tree = Tree("((A,B),C);")
    >>> cass_tree = introduce_crispr_mutations(tree)
    >>> print(cass_tree.character_matrix.shape)

    Notes
    -----
    This function requires the Cassiopeia package for mutation simulation.
    The resulting character matrix will have cells as rows and mutation
    sites as columns, with values representing different mutation states.
    """
    try:
        import cassiopeia as cas
    except ImportError:
        raise ImportError("Cassiopeia package required for mutation simulation. "
                         "Install with: pip install git+https://github.com/YosefLab/Cassiopeia@master#egg=cassiopeia-lineage")

    # Convert ete3 tree to Cassiopeia tree
    newick_string = tree.write(format=1)
    cass_tree = cas.data.CassiopeiaTree(tree=newick_string)

    # Simulate mutations using Cassiopeia's mutation simulator
    # Parameters can be adjusted based on experimental setup
    mutation_simulator = cas.simulator.Cas9LineageTracingDataSimulator(
        number_of_cassettes=number_of_cassettes,
    )

    # Apply mutations to the tree
    mutation_simulator.overlay_data(cass_tree)

    return cass_tree

