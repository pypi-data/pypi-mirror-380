# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../conductor"))
sys.path.insert(0, os.path.abspath("../conductor/devices"))
sys.path.insert(0, os.path.abspath("../conductor/airfinder"))
sys.path.insert(0, os.path.abspath("../conductor/airfinder/devices"))

# -- Project information -----------------------------------------------------

project = "conductor-py"
copyright = "2019, Thomas Steinholz, Allen Welkie, Scott Wohler"
author = "Thomas Steinholz, Allen Welkie, Scott Wohler"

# The full version, including alpha/beta/rc tags
release = "1.6.0"

# -- General configuration ---------------------------------------------------

# Sort members by type
autodoc_member_order = "groupwise"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    # 'sphinxcontrib.asyncio',
]
# , 'sphinx.ext.todo' ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["__pycache__", "*.pyc"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_logo = "_static/ll-logo.png"
html_theme_options = {
    # 'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    "logo_only": True,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    # 'vcs_pageview_mode': '',
    "style_nav_header_background": "white",
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
