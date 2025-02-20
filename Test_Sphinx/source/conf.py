# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Test-Example-Project'
copyright = '2025, Reyhan'
author = 'Reyhan'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme', 'sphinx_copybutton', 'sphinx_code_tabs', 'sphinxcontrib.plantuml', 'sphinx_needs']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'
html_theme_options = {
    'logo_only': True,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'includehidden': True,
    'navigation_depth': 4,
    'titles_only': False
}

html_static_path = ['_static']

def setup(app):
    app.add_css_file("css/custom.css")

import os

on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    plantuml = 'java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar'
else:
    plantuml = 'java -jar %s' % os.path.join(os.path.dirname(__file__), "utils", "plantuml.jar")

    plantuml_output_format = 'png'

needs_types = [
    {
        "directive": "can-be-anything-and-is-used-further",
        "title": "Project",
        "prefix": "P_",  # prefix for auto-generated IDs
        "style": "square", # style for the type in diagrams
        "color": "#BFDD83", # color for the type in diagrams
    }]