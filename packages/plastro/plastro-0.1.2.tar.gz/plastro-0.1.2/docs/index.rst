PLASTRO Documentation
=====================

Welcome to PLASTRO's documentation! PLASTRO is a Python package for simulating and analyzing cellular plasticity in single-cell data.

.. image:: https://img.shields.io/pypi/v/plastro.svg
   :target: https://pypi.python.org/pypi/plastro
   :alt: PyPI version

.. image:: https://img.shields.io/conda/vn/conda-forge/plastro.svg
   :target: https://anaconda.org/conda-forge/plastro
   :alt: Conda version

.. image:: https://readthedocs.org/projects/plastro/badge/?version=latest
   :target: https://plastro.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Overview
--------

PLASTRO provides tools for:

* **Simulating cellular plasticity** through random walks and cluster switches
* **Analyzing phenotypic transitions** in single-cell datasets  
* **Computing plasticity overlap scores** from lineage tracing data
* **Constructing phylogenetic trees** from single-cell data

Key Features
------------

🔬 **Plasticity Simulation**
   Multiple methods for simulating cellular plasticity including random walk plasticity and discrete cluster switches.

🧬 **Lineage Tracing Integration**
   Full integration with CRISPR-based lineage tracing data and Cassiopeia trees.

📊 **PLASTRO Score**
   Novel overlap-based metric for quantifying cellular plasticity from combined lineage and phenotypic data.

🌳 **Phylogenetic Analysis**
   Neighbor-joining tree construction and phylogenetic distance calculations.

📈 **Comprehensive Analysis**
   Distance metrics, archetype analysis, and visualization tools for plasticity research.

Quick Start
-----------

Installation
~~~~~~~~~~~~

Install PLASTRO using pip:

.. code-block:: bash

   pip install plastro

Or using conda:

.. code-block:: bash

   conda install -c conda-forge plastro

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   import plastro
   import scanpy as sc
   
   # Load your single-cell data
   adata = sc.read_h5ad('your_data.h5ad')
   
   # Simulate random walk plasticity
   walk_params = {100: 0.1, 500: 0.05, 1000: 0.02}
   plastic_adata = plastro.random_walk_plasticity(adata, walk_params)
   
   # Compute PLASTRO scores (if you have lineage data)
   plastro_scores = plastro.PLASTRO_score(character_matrix, adata)

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