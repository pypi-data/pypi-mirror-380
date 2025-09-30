Installation
============

PLASTRO can be installed via pip or conda. We recommend using conda for easier dependency management.

Requirements
------------

PLASTRO requires Python 3.10 or higher and the following core dependencies:

* pybind11 >= 2.6.0 (required for building graph-walker)
* graph-walker >= 1.0.6 (essential for random walk functionality)
* NumPy >= 1.20.0
* Pandas >= 1.3.0  
* SciPy >= 1.7.0
* Matplotlib >= 3.4.0
* Scanpy >= 1.8.0
* AnnData >= 0.8.0
* NetworkX >= 2.6.0
* scikit-learn >= 1.0.0
* scikit-bio >= 0.5.7
* ete3 >= 3.1.2
* seaborn >= 0.11.0
* tqdm >= 4.60.0
* icecream >= 2.1.0

Install via Pip
---------------

PLASTRO requires pybind11 to be installed first for building essential dependencies:

.. code-block:: bash

   pip install pybind11
   pip install plastro

To install with all optional dependencies:

.. code-block:: bash

   pip install pybind11
   pip install plastro[all]

Install via Conda
-----------------

You can also install PLASTRO using conda:

.. code-block:: bash

   conda install -c conda-forge plastro

Development Installation
------------------------

For development, clone the repository and install in editable mode:

.. code-block:: bash

   git clone https://github.com/dpeerlab/PLASTRO.git
   cd PLASTRO
   pip install pybind11
   pip install -e ".[dev]"

Using Environment Files
------------------------

We provide environment files for easy setup:

**Using conda:**

.. code-block:: bash

   conda env create -f environment.yml
   conda activate plastro

**Using pip:**

.. code-block:: bash

   pip install -r requirements.txt

Optional Dependencies
---------------------

Some features require additional packages:

**Lineage Tracing:**

.. code-block:: bash

   pip install cassiopeia-lineage


**Development Tools:**

.. code-block:: bash

   pip install plastro[dev]

**Documentation:**

.. code-block:: bash

   pip install plastro[docs]

Verification
------------

Test your installation:

.. code-block:: python

   import plastro
   print(plastro.__version__)

   # Test basic functionality
   print("Available functions:", dir(plastro))

Troubleshooting
---------------

**Common Issues:**

1. **ETE3 Installation Problems**
   
   If you encounter issues with ETE3:
   
   .. code-block:: bash
   
      conda install -c etetoolkit ete3

2. **Graph-Walker Build Issues**
   
   If graph-walker fails to build, ensure pybind11 is installed first:
   
   .. code-block:: bash
   
      pip install pybind11
      pip install graph-walker

3. **Memory Issues with Large Datasets**
   
   For large datasets, consider:
   
   * Using a machine with more RAM
   * Processing data in chunks
   * Using sparse matrix representations

**Getting Help:**

If you encounter issues:

1. Check the `Issues page <https://github.com/username/plastro/issues>`_
2. Search existing issues for solutions
3. Create a new issue with detailed error information