# Configuration file for the Sphinx documentation builder.

import os
import sys

# sys.path.insert(0, os.path.abspath('../..'))
# sys.path.insert(1, os.path.abspath('..'))

# -- Project information

project = 'infodesreg'
copyright = '2023, Anonymous'
author = 'Anonymous'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx-mathjax-offline'
]

# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
# }
# intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output
add_module_names = False
html_show_copyright = False 
html_show_sphinx = False  

html_theme = "sphinx_rtd_theme"
# html_theme = "sphinx_thunlp_theme"
html_codeblock_linenos_style = "table" 

autodoc_member_order = "groupwise"
autodoc_typehints = "description"
html_static_path = ['_static']
html_css_files = ["css/custom.css"]
master_doc = 'index' 

