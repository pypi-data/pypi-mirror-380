API Reference
=============

This section contains the complete API reference for PLASTRO.

.. toctree::
   :maxdepth: 2

   plasticity
   overlap
   lineage_simulation
   phenotype_simulation
   distances
   phylo

Main Functions
--------------

The most commonly used functions are available directly from the main package:

.. currentmodule:: plastro

.. autosummary::
   :toctree: generated/

   random_walk_plasticity
   leiden_switch_plasticity
   PLASTRO_score
   simulate_lineage_tracing
   archetype_distance
   neighbor_joining
   generate_ad
   simulate_realistic_dataset