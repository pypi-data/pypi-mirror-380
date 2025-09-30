"""
PLASTRO: A Python package for simulating cellular plasticity in single-cell data.

PLASTRO provides tools for:
- Simulating cellular plasticity through random walks and cluster switches
- Analyzing phenotypic transitions in single-cell datasets
- Computing plasticity overlap scores from lineage tracing data
- Constructing phylogenetic trees from single-cell data

Modules:
    plasticity: Core plasticity simulation functions
    lineage_simulation: CRISPR-based lineage tracing simulation
    phenotype_simulation: Synthetic phenotypic data generation
    overlap: Overlap score computation and analysis
    distances: Phenotypic distance calculation methods
    phylo: Phylogenetic analysis tools
"""

__version__ = "0.1.2"
__author__ = "Sitara Persad"
__email__ = "sitara.persad@example.com"

# Import main functionality
from .plasticity import (
    random_walk_plasticity,
    cluster_switch_plasticity,
    perform_random_walk,
    visualize_walk,
    construct_phenotypic_graph,
    plot_leiden_transitions,
    plot_change_in_phenotype
)

from .overlap import (
    PLASTRO_score,
    PLASTRO_overlaps,
    compute_lineage_distances,
    compute_phenotype_distances,
    compute_gini_plasticity_score,
    compute_variable_radii_plasticity_score
)

# Optimized overlap functions are now integrated into the main overlap module

from .lineage_simulation import (
    simulate_lineage_tracing,
    construct_tree,
    introduce_crispr_mutations
)

from .phylo import (
    neighbor_joining
)

from .phenotype_simulation import (
    create_random_binary_tree,
    sample_branch,
    generate_ad,
    subset_to_terminal_branches,
    simulate_realistic_dataset,
    rgba_to_hex
)

__all__ = [
    # Plasticity functions
    'random_walk_plasticity',
    'cluster_switch_plasticity',
    'perform_random_walk',
    'visualize_walk',
    'construct_phenotypic_graph',
    'plot_leiden_transitions',
    'plot_change_in_phenotype',
    
    # Overlap functions
    'PLASTRO_score',
    'PLASTRO_overlaps',
    'compute_lineage_distances',
    'compute_phenotype_distances',
    'compute_gini_plasticity_score',
    'compute_variable_radii_plasticity_score',
    
    # Note: Optimized overlap functions are now integrated into the main overlap functions above

    # Lineage simulation functions
    'simulate_lineage_tracing',
    'construct_tree',
    'introduce_crispr_mutations',
    
    # Phylo functions
    'neighbor_joining',
    
    # Phenotype simulation functions
    'create_random_binary_tree',
    'sample_branch',
    'generate_ad',
    'subset_to_terminal_branches',
    'simulate_realistic_dataset',
    'rgba_to_hex'
]