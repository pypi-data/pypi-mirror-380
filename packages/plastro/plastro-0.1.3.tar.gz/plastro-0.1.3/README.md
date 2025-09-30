# PLASTRO

[![PyPI version](https://badge.fury.io/py/plastro.svg)](https://badge.fury.io/py/plastro)
[![Conda version](https://img.shields.io/conda/vn/conda-forge/plastro.svg)](https://anaconda.org/conda-forge/plastro)
[![Documentation Status](https://readthedocs.org/projects/plastro/badge/?version=latest)](https://plastro.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**PLASTRO** is a Python package for simulating and analyzing cellular plasticity in single-cell data. It provides comprehensive tools for studying how cells transition between different phenotypic states and how these transitions relate to lineage relationships.

## Key Features

- **Plasticity Simulation**: Random walk plasticity and cluster-based transitions
- **Lineage Tracing Integration**: CRISPR-based lineage tracing simulation with Cassiopeia
- **PLASTRO Score**: Novel overlap-based metrics for quantifying cellular plasticity.
- **Phylogenetic Analysis**: Neighbor-joining tree construction from single-cell data
- **Data Simulation**: Generate realistic synthetic datasets with branching differentiation
- **High Performance**: Optimized overlap computation (10-100x speedup over naive methods)

## Installation

### Quick Install

PLASTRO requires `pybind11` to be installed first for building essential dependencies:

```bash
pip install pybind11
pip install plastro
```

### From TestPyPI (Latest Development Version)

```bash
pip install pybind11
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ plastro
```

### Development Install

```bash
git clone https://github.com/dpeerlab/PLASTRO.git
cd PLASTRO
pip install pybind11
pip install -e .
```

### Conda Install (coming soon)

```bash
conda install -c conda-forge plastro
```

## Quick Start

### Basic PLASTRO Score Computation

```python
import plastro
import pandas as pd

# Load your single-cell data and lineage tracing data
character_matrix = pd.read_csv('character_matrix.csv', index_col=0)
adata = plastro.load_data('single_cell_data.h5ad')

# Compute Gini-based plasticity scores (recommended)
gini_scores = plastro.PLASTRO_score(
    character_matrix=character_matrix,
    ad=adata,
    flavor='gini',
    latent_space_key='X_dc'  # or 'X_pca', 'X_umap'
)

print(f"Mean Gini plasticity score: {gini_scores['Gini_Index'].mean():.3f}")
```

### Generate Synthetic Data with Plasticity

```python
# Create synthetic single-cell dataset
n_leaves = 8
sample_res = 50  
n_dim = 20

# Generate branching structure
sample_structure = plastro.create_random_binary_tree(n_leaves, sample_res)
full_simulated_ad = plastro.generate_ad(sample_structure, n_dim)

# Subset to terminal branches
ad = plastro.subset_to_terminal_branches(full_simulated_ad)

# Simulate lineage tracing
cass_tree = plastro.simulate_lineage_tracing(
    sim_ad=full_simulated_ad, 
    terminal_ad=ad,
    latent_space_key='X_dc'
)
```

### Simulate Cellular Plasticity

```python
# Random walk plasticity
plastic_cells = {'6': 0.3, '5': 0.2}  # 30% of cluster 6, 20% of cluster 5
walk_lengths = {'6': 500, '5': 1000}
plastic_walk_ad = plastro.random_walk_plasticity(
    full_simulated_ad, ad, plastic_cells, walk_lengths
)

# Cluster switch plasticity  
destination_clusters = {
    '11': {'destination': '7', 'proportion': 0.4},
    '6': {'destination': '10', 'proportion': 0.2}
}
plastic_leiden_ad = plastro.cluster_switch_plasticity(
    full_simulated_ad, ad, destination_clusters, column='leiden'
)
```

## Documentation & Examples

### Example Notebooks

Complete example workflows are available in `docs/notebooks/`:

1. **[Plasticity Simulation Example](docs/notebooks/plasticity_simulation_example.ipynb)**: 
   - Generate synthetic single-cell data with branching differentiation
   - Simulate CRISPR-based lineage tracing
   - Apply random walk and cluster switch plasticity
   - Visualize phenotypic changes

2. **[PLASTRO Overlap Analysis](docs/notebooks/plastro_overlap_analysis.ipynb)**:
   - In-depth analysis of lineage-phenotype relationships
   - Detailed explanation of overlap computation methods
   - Interpretation of PLASTRO scores

### Key Documentation Sections

- **[Installation Guide](https://plastro.readthedocs.io/en/latest/installation.html)**: Detailed installation instructions
- **[API Reference](https://plastro.readthedocs.io/en/latest/api/)**: Complete function documentation
- **[Tutorials](https://plastro.readthedocs.io/en/latest/tutorials/)**: Step-by-step guides

## Core API

### Main Functions

```python
# PLASTRO Score Computation
plastro.PLASTRO_score(character_matrix, ad, flavor='gini')
plastro.PLASTRO_overlaps(character_matrix, ad, maximum_radius=500)

# Plasticity Simulation
plastro.random_walk_plasticity(full_ad, subset_ad, plastic_cells, walk_lengths)
plastro.cluster_switch_plasticity(full_ad, subset_ad, destination_clusters)

# Data Generation
plastro.create_random_binary_tree(n_leaves, sample_res)
plastro.generate_ad(sample_structure, n_dim)
plastro.simulate_lineage_tracing(sim_ad, terminal_ad)

# Distance Calculations  
plastro.euclidean_distance(coordinates)
plastro.cosine_distance(coordinates)
plastro.manhattan_distance(coordinates)
plastro.archetype_distance(data, archetypes)

# Phylogenetic Analysis
plastro.neighbor_joining(distance_matrix, outgroup=None)
```

### Core Modules

- **`plastro.overlap`**: PLASTRO score computation and overlap analysis
- **`plastro.plasticity`**: Cellular plasticity simulation methods  
- **`plastro.lineage_simulation`**: CRISPR-based lineage tracing simulation
- **`plastro.phenotype_simulation`**: Synthetic single-cell data generation
- **`plastro.phylo`**: Phylogenetic tree construction and analysis

## Complete Example Workflow

```python
import plastro
import pandas as pd

# 1. Generate synthetic data (or load your own)
sample_structure = plastro.create_random_binary_tree(n_leaves=8, sample_res=50)
full_simulated_ad = plastro.generate_ad(sample_structure, n_dim=20)
ad = plastro.subset_to_terminal_branches(full_simulated_ad)

# 2. Simulate lineage tracing
cass_tree = plastro.simulate_lineage_tracing(
    sim_ad=full_simulated_ad,
    terminal_ad=ad,
    latent_space_key='X_dc'
)
character_matrix = cass_tree.character_matrix

# 3. Simulate plasticity
plastic_cells = {'6': [cell1, cell2, cell3]}  # Specific cells to make plastic
walk_lengths = {'6': 500}
plastic_ad = plastro.random_walk_plasticity(
    full_simulated_ad, ad, plastic_cells, walk_lengths
)

# 4. Compute PLASTRO scores
original_scores = plastro.PLASTRO_score(
    character_matrix, ad, flavor='gini'
)
plastic_scores = plastro.PLASTRO_score(
    character_matrix, plastic_ad, flavor='gini'
)

# 5. Compare plasticity
print(f"Original mean Gini score: {original_scores['Gini_Index'].mean():.3f}")
print(f"Plastic mean Gini score: {plastic_scores['Gini_Index'].mean():.3f}")
```

## Dependencies

**Core requirements:**
- Python ≥ 3.10
- pybind11 ≥ 2.6.0 (required for building graph-walker)
- graph-walker ≥ 1.0.6 (essential for random walk functionality)
- NumPy ≥ 1.20.0
- Pandas ≥ 1.3.0
- SciPy ≥ 1.7.0
- scikit-learn ≥ 1.0.0
- scikit-bio ≥ 0.5.7 (for robust neighbor-joining trees)
- NetworkX ≥ 2.6.0
- matplotlib ≥ 3.4.0
- scanpy ≥ 1.8.0
- anndata ≥ 0.8.0
- ete3 ≥ 3.1.2 (for phylogenetic tree manipulation)
- tqdm ≥ 4.60.0
- seaborn ≥ 0.11.0
- icecream ≥ 2.1.0

**Optional dependencies:**
- `cassiopeia-lineage` (for advanced lineage tracing simulation)
- `igraph` (for Leiden clustering in phenotype simulation)

## Data Requirements

PLASTRO works with:
- **AnnData objects** containing single-cell data with dimensionality reduction coordinates
- **Character matrices** (pandas DataFrame) from CRISPR lineage tracing with cells as rows
- **Distance matrices** for lineage and phenotypic relationships
- **Cluster annotations** (leiden, louvain, etc.) for cluster-based plasticity

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [plastro.readthedocs.io](https://plastro.readthedocs.io/)
- **Issues**: [GitHub Issues](https://github.com/yourusername/plastro/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/plastro/discussions)

---

**PLASTRO** - Comprehensive analysis of cellular plasticity in single-cell data