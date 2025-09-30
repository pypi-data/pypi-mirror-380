project = "throttle-it"
copyright = "2025, Alexandre Sonderegger"
author = "Alexandre Sonderegger"
release = "v0.1.0"

extensions = ["myst_nb", "sphinx.ext.autodoc", "sphinx.ext.napoleon"]

templates_path = ["_templates"]
exclude_patterns: list[str] = []


html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
