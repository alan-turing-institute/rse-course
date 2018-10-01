
import sys
import os

extensions = [
    'sphinx.ext.autodoc',  # Support automatic documentation
    'sphinx.ext.coverage', # Automatically check if functions are documented
    'sphinx.ext.mathjax',  # Allow support for algebra
    'sphinx.ext.viewcode', # Include the source code in documentation
    'numpydoc'             # Support NumPy style docstrings
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Greetings'
copyright = u'2014, James Hetherington'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'Greetingsdoc'
latex_elements = {
}

latex_documents = [
  ('index', 'Greetings.tex', u'Greetings Documentation',
   u'James Hetherington', 'manual'),
]

man_pages = [
    ('index', 'greetings', u'Greetings Documentation',
     [u'James Hetherington'], 1)
]

texinfo_documents = [
  ('index', 'Greetings', u'Greetings Documentation',
   u'James Hetherington', 'Greetings', 'One line description of project.',
   'Miscellaneous'),
]