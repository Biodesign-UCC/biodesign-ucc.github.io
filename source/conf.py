# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
#import sphinx_bootstrap_theme


# -- Project information -----------------------------------------------------

project = 'Biodesign UCC'
copyright = '2024, Biodesign-UCC'
author = 'Biodesign-UCC'

html_logo = "_static/group-logo.png"

# The full version, including alpha/beta/rc tags
release = '1.0'

html_title = 'Biodesign UCC Homepage'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinx_panels',
'sphinxcontrib.bibtex',
'sphinxcontrib.youtube',
'sphinxcontrib.video',
]
bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrtalpha'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
#html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Biodesign-UCC/biodesign-ucc.github.io",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/cantillonmurphy",
            "icon": "fab fa-twitter-square",
        },
    ],
    "navbar_end": ["navbar-icon-links.html", "search-field.html"],

    "external_links": [
      {"name": "Group Github", "url": "https://github.com/Biodesign-UCC"}
  ]
}