# conf.py
# Sphinx configuration file for Read the Docs
# https://docs.readthedocs.com/platform/stable/intro/sphinx.html

# -----------------------------------------------------------
# 1. Project information
# -----------------------------------------------------------
project = 'Sysco'          # Shown in the left sidebar and HTML <title>
copyright = '2025, Eric Philbin'   # Used in the footer
author = 'Eric Philbin'
release = '1.0.0'             # Version shown in the docs (can be auto-updated with CI)

# -----------------------------------------------------------
# 2. General configuration
# -----------------------------------------------------------
# Minimum required extensions for most Python projects
extensions = [
    'sphinx.ext.autodoc',      # Auto-generate API docs from docstrings
    'sphinx.ext.viewcode',     # Add “[source]” links to every documented object
    'sphinx.ext.napoleon',     # Support Google/NumPy-style docstrings
    'sphinx.ext.intersphinx',  # Link to other projects’ docs
]

# File extensions to treat as source files
source_suffix = {
    '.rst': None,
    '.md': None,
}

# Master document (homepage)
master_doc = 'index'            # The filename (no extension) of the master document
source_suffix = {
    '.rst': None,             # or '.md' if you use MyST
}

# List of patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -----------------------------------------------------------
# 3. Intersphinx mapping (optional but very useful)
# -----------------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
}

# -----------------------------------------------------------
# 4. HTML output options
# -----------------------------------------------------------
# Choose a theme that also works locally and on RTD
html_theme = 'alabaster'        # or 'furo', 'pydata_sphinx_theme', etc.

# Static files (CSS overrides, images, etc.)
#html_static_path = ['_static']

# Custom CSS file (create _static/custom.css if you want styling tweaks)
html_css_files = ['custom.css']

# -----------------------------------------------------------
# 5. LaTeX output (for PDF builds)
# -----------------------------------------------------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
}

# -----------------------------------------------------------
# 6. Read the Docs-specific overrides
# -----------------------------------------------------------
# If you need to install extra packages on RTD, list them in
# `.readthedocs.yaml` under python.install.requirements.
