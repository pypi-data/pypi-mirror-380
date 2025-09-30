PLASTRO
=======

.. image:: https://badge.fury.io/py/plastro.svg
   :target: https://badge.fury.io/py/plastro
   :alt: PyPI version

.. image:: https://img.shields.io/conda/vn/conda-forge/plastro.svg
   :target: https://anaconda.org/conda-forge/plastro
   :alt: Conda version

.. image:: https://readthedocs.org/projects/plastro/badge/?version=latest
   :target: https://plastro.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

**PLASTRO** is a Python package for simulating and analyzing cellular plasticity in single-cell data. It provides comprehensive tools for studying how cells transition between different phenotypic states and how these transitions relate to lineage relationships.

Key Features
------------

- **Plasticity Simulation**: Random walk plasticity and cluster-based transitions
- **Lineage Tracing Integration**: CRISPR-based lineage tracing simulation with Cassiopeia
- **PLASTRO Score**: Novel overlap-based metrics for quantifying cellular plasticity
- **Phylogenetic Analysis**: Neighbor-joining tree construction from single-cell data
- **Data Simulation**: Generate realistic synthetic datasets with branching differentiation
- **High Performance**: Optimized overlap computation (10-100x speedup over naive methods)

Installation
------------

Quick Install
~~~~~~~~~~~~~

PLASTRO requires ``pybind11`` to be installed first for building essential dependencies:

.. code-block:: bash

   pip install pybind11
   pip install plastro

From TestPyPI (Latest Development Version)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install pybind11
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ plastro

Development Install
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/dpeerlab/PLASTRO.git
   cd PLASTRO
   pip install pybind11
   pip install -e .

Conda Install (coming soon)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   conda install -c conda-forge plastro

Quick Start
-----------

Basic PLASTRO Score Computation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

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

Generate Synthetic Data with Plasticity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

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

Simulate Cellular Plasticity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Random walk plasticity (uses latent space embedding, defaults to X_dc diffusion components)
   plastic_cells = {'6': 0.3, '5': 0.2}  # 30% of cluster 6, 20% of cluster 5
   walk_lengths = {'6': 500, '5': 1000}
   plastic_walk_ad = plastro.random_walk_plasticity(
       full_simulated_ad, ad, plastic_cells, walk_lengths,
       latent_space_key='X_dc'  # Default: uses diffusion components
   )

   # Cluster switch plasticity  
   destination_clusters = {
       '11': {'destination': '7', 'proportion': 0.4},
       '6': {'destination': '10', 'proportion': 0.2}
   }
   plastic_leiden_ad = plastro.cluster_switch_plasticity(
       full_simulated_ad, ad, destination_clusters, column='leiden'
   )

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   tutorials/index
   api/index
   examples/index
   contributing
   changelog

.. toctree::
   :maxdepth: 1
   :caption: Example Notebooks:

   notebooks/plasticity_simulation_example

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`