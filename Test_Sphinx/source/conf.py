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
    { "directive": "req",
      "title": "Requirement",
      "prefix": "R_",
      "color": "#BFD8D2",
      "style": "node" },
    { "directive": "spec",
      "title": "Specification",
      "prefix": "S_",
      "color": "#FEDCD2",
      "style": "node"},
    { "directive": "test",
      "title": "Test Case",
      "prefix": "T_",
      "color": "#DCB239",
      "style": "node"},
    {
        "directive": "can-be-anything-and-is-used-further",
        "title": "Project",
        "prefix": "P_",
        "style": "square",
        "color": "#BFDD83",
    },
    {
        "directive": "tutorial",
        "title": "Tutorial",
        "prefix": "TUT_",
        "style": "rectangle",
        "color": "#BFD8D2",
    },
    {
        "directive": "unit-test",
        "title": "Unit Test",
        "prefix": "UTC_",
        "style": "rectangle",
        "color": "#FFD700",
    }]

# Define own options
needs_extra_options = [ "integrity", "assignee" ]

# Define own link types
needs_extra_links = [
    { "option": "checks",
      "incoming": "is checked by",
      "outgoing": "checks" },
    { "option": "implements",
      "incoming": "is implemented by",
      "outgoing": "implements" },
      {
        "option": "verifies",        # Defines a "verifies" relationship
        "incoming": "is verified by",
        "outgoing": "verifies",
        "style": "#FFAA00",
    },
    {
        "option": "tests",           # Defines a "tests" relationship
        "incoming": "is tested by",
        "outgoing": "tests",
        "style": "#0000FF",
    },
    {
    "option": "tutorial_required_by",
    "incoming": "requires",  # text to describe incoming links
    "outgoing": "required by",  # text to describe outgoing links
    "style": "#00AA00",  # color for the link in diagrams
  }]

needs_id_regex = r'^[A-Z0-9_]{2,}$'

need_flow_configs = {
    "default": "TB",  # Default flow direction (Top to Bottom)
    "tutorial": "LR",  # Custom flow direction (Left to Right)
}
