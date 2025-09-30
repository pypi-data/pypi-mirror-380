"""
Phylogenetic analysis tools.

This module provides functions for phylogenetic tree construction and analysis,
including neighbor-joining algorithms and tree manipulation utilities.
"""

import pandas as pd
import numpy as np
import networkx as nx
from typing import Optional
from ete3 import TreeNode


def neighbor_joining(
    distance_matrix: pd.DataFrame,
    outgroup: Optional[str] = None
) -> TreeNode:
    """
    Construct phylogenetic tree using neighbor-joining algorithm.
    
    Uses scikit-bio's robust neighbor-joining implementation to build an 
    unrooted tree from a distance matrix. This is much more reliable than
    a custom implementation.

    Parameters
    ----------
    distance_matrix : pd.DataFrame
        Symmetric matrix of pairwise distances between leaves.
        Index and columns should contain leaf names.
    outgroup : str, optional
        Name of outgroup leaf for rooting the tree, by default None.

    Returns
    -------
    ete3.TreeNode
        Phylogenetic tree constructed using neighbor-joining.

    Examples
    --------
    >>> import numpy as np
    >>> import pandas as pd
    >>> from plastro import neighbor_joining
    >>> 
    >>> # Create sample distance matrix
    >>> cells = ['A', 'B', 'C', 'D']
    >>> dists = np.random.rand(4, 4)
    >>> dists = (dists + dists.T) / 2  # Make symmetric
    >>> np.fill_diagonal(dists, 0)
    >>> dist_df = pd.DataFrame(dists, index=cells, columns=cells)
    >>> 
    >>> # Build tree
    >>> tree = neighbor_joining(dist_df, outgroup='A')
    >>> print(tree.get_ascii())

    Notes
    -----
    This function uses scikit-bio's neighbor-joining implementation, which is:
    - Well-tested and robust
    - O(n³) time complexity
    - Handles edge cases properly
    - Produces accurate phylogenetic trees

    The result is converted from scikit-bio format to ETE3 format for
    compatibility with other PLASTRO functions.

    Raises
    ------
    ImportError
        If scikit-bio is not installed.
    ValueError
        If distance matrix is invalid or outgroup not found.
    """
    try:
        from skbio import DistanceMatrix
        from skbio.tree import nj
    except ImportError:
        raise ImportError(
            "scikit-bio is required for neighbor-joining. "
            "Install with: pip install scikit-bio"
        )
    
    # Validate inputs
    if outgroup is not None and outgroup not in distance_matrix.index:
        raise ValueError(f'Outgroup {outgroup} not found in distance matrix')
    
    # Clean and validate distance matrix
    dist_values = distance_matrix.values.copy()
    
    # Replace NaNs with large distance (max distance + 1)
    if np.isnan(dist_values).any():
        max_finite = np.nanmax(dist_values)
        if np.isfinite(max_finite):
            dist_values[np.isnan(dist_values)] = max_finite + 1.0
        else:
            dist_values[np.isnan(dist_values)] = 10.0
        print(f"Warning: NaN values found in distance matrix, replaced with {max_finite + 1.0 if np.isfinite(max_finite) else 10.0}")
    
    # Ensure matrix is symmetric
    dist_values = (dist_values + dist_values.T) / 2
    
    # Ensure diagonal is zero (hollow matrix)
    np.fill_diagonal(dist_values, 0.0)
    
    # Create cleaned DataFrame
    clean_distance_matrix = pd.DataFrame(dist_values, 
                                       index=distance_matrix.index, 
                                       columns=distance_matrix.columns)
    
    print(f"Starting neighbor-joining with {len(clean_distance_matrix)} taxa using scikit-bio")
    
    # Convert to scikit-bio DistanceMatrix
    skbio_dm = DistanceMatrix(clean_distance_matrix.values, ids=clean_distance_matrix.index)
    
    # Perform neighbor-joining
    skbio_tree = nj(skbio_dm)
    
    # Convert to ETE3 format
    ete_tree = _skbio_to_ete3(skbio_tree)
    
    # Root tree if outgroup specified
    if outgroup is not None:
        try:
            # Find the outgroup leaf
            outgroup_leaves = [leaf for leaf in ete_tree.get_leaves() if leaf.name == outgroup]
            if outgroup_leaves:
                ete_tree.set_outgroup(outgroup_leaves[0])
                print(f"Tree rooted with outgroup: {outgroup}")
            else:
                print(f"Warning: Outgroup {outgroup} not found in tree leaves")
        except Exception as e:
            print(f"Warning: Could not root tree with outgroup {outgroup}: {e}")
    
    print("Neighbor-joining completed successfully")
    return ete_tree


def _skbio_to_ete3(skbio_tree):
    """
    Convert scikit-bio tree to ETE3 TreeNode format.
    
    Parameters
    ----------
    skbio_tree : skbio.TreeNode
        Tree in scikit-bio format.
        
    Returns
    -------
    ete3.TreeNode
        Tree converted to ETE3 format.
    """
    def convert_node(skbio_node):
        """Recursively convert scikit-bio node to ETE3."""
        ete_node = TreeNode()
        
        # Set node name
        if skbio_node.name is not None:
            ete_node.name = skbio_node.name
        
        # Set branch length
        if skbio_node.length is not None:
            ete_node.dist = skbio_node.length
        else:
            ete_node.dist = 0.0
        
        # Convert children recursively
        for child in skbio_node.children:
            child_node = convert_node(child)
            ete_node.add_child(child_node)
        
        return ete_node
    
    return convert_node(skbio_tree)
