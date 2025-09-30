"""Configuration file for the Sphinx documentation builder."""

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'PLASTRO'
copyright = '2024, Sitara Persad'
author = 'Sitara Persad'
release = '0.1.0'
version = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'nbsphinx',
    'sphinx_rtd_theme',
]

# Templates path
templates_path = ['_templates']

# List of patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# -- Extension configuration -------------------------------------------------

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Autosummary settings
autosummary_generate = True

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
    'scanpy': ('https://scanpy.readthedocs.io/en/stable/', None),
    'anndata': ('https://anndata.readthedocs.io/en/latest/', None),
    'networkx': ('https://networkx.org/documentation/stable/', None),
}

# NBSphinx settings
nbsphinx_execute = 'never'  # Don't execute notebooks during build
nbsphinx_allow_errors = True

# Math settings
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# HTML settings
html_title = f"{project} v{version}"
html_short_title = project
html_favicon = None
html_logo = None
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# Output file base name for HTML help builder
htmlhelp_basename = 'PLASTROdoc'

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
    'fncychap': '',
    'maketitle': '',
    'printindex': '',
}

# Grouping the document tree into LaTeX files
latex_documents = [
    ('index', 'PLASTRO.tex', 'PLASTRO Documentation',
     'Sitara Persad', 'manual'),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    ('index', 'plastro', 'PLASTRO Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    ('index', 'PLASTRO', 'PLASTRO Documentation',
     author, 'PLASTRO', 'A Python package for simulating cellular plasticity.',
     'Miscellaneous'),
]