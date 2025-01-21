# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GEOGLOWS Developer Guide'
copyright = '2024, Aquaveo'
author = 'Aquaveo'

# -- Mock imports -------------------------------------------------------------

autodoc_mock_imports = [
    # RAPIDpy Imports
    "rtree",
    "dateutil.parser",
    "numpy",
    "numpy.ma",
    "numpy.testing",
    "xarray",
    "netCDF4",
    "pandas",
    "past.builtins",
    "pangaea",
    "osgeo",
    "pyproj",
    "shapely",
    "shapely.geometry",
    "shapely.geos",
    "shapely.ops",
    "shapely.wkb",
    "gazar",
    "gazar.grid",
    "scipy",
    "scipy.spatial",
]


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

rst_epilog = f"""
.. |project| replace:: {project}
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
