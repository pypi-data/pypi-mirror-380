# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
#  nova documentation build configuration file
#
# Refer to the Sphinx documentation for advice on configuring this file:
#
#   http://www.sphinx-doc.org/en/stable/config.html

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../'))

# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.graphviz',
    'openstackdocstheme',
    'sphinx_feature_classification.support_matrix',
    'oslo_config.sphinxconfiggen',
    'oslo_config.sphinxext',
    'oslo_policy.sphinxpolicygen',
    'oslo_policy.sphinxext',
    'ext.versioned_notifications',
    'ext.feature_matrix',
    'ext.extra_specs',
    'sphinxcontrib.rsvgconverter',
]


config_generator_config_file = '../../etc/nova/nova-config-generator.conf'
sample_config_basename = '_static/nova'

policy_generator_config_file = [
    ('../../etc/nova/nova-policy-generator.conf', '_static/nova'),
]

todo_include_todos = True

# The master toctree document.
master_doc = 'index'

# General information about the project.
copyright = u'2010-present, OpenStack Foundation'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'native'

# -- Options for man page output ----------------------------------------------

# Grouping the document tree for man pages.
# List of tuples 'sourcefile', 'target', u'title', u'Authors name', 'manual'

_man_pages = [
    ('nova-api', 'Server for the OpenStack Compute API service.'),
    (
        'nova-api-metadata',
        'Server for the OpenStack Compute metadata API service.',
    ),
    (
        'nova-api-os-compute',
        'Server for the OpenStack Compute API service.',
    ),
    ('nova-compute', 'Server for the OpenStack Compute compute service.'),
    ('nova-conductor', 'Server for the OpenStack Compute conductor service.'),
    ('nova-manage', 'Management tool for the OpenStack Compute services.'),
    (
        'nova-novncproxy',
        'Server for the OpenStack Compute VNC console proxy service.'
    ),
    (
        'nova-rootwrap',
        'Root wrapper daemon for the OpenStack Compute service.',
    ),
    (
        'nova-policy',
        'Inspect policy configuration for the OpenStack Compute services.',
    ),
    (
        'nova-scheduler',
        'Server for the OpenStack Compute scheduler service.',
    ),
    (
        'nova-serialproxy',
        'Server for the OpenStack Compute serial console proxy service.',
    ),
    (
        'nova-spicehtml5proxy',
        'Server for the OpenStack Compute SPICE console proxy service.',
    ),
    (
        'nova-status',
        'Inspect configuration status for the OpenStack Compute services.',
    ),
]

man_pages = [
    ('cli/%s' % name, name, description, ['openstack@lists.openstack.org'], 1)
    for name, description in _man_pages]

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'openstackdocs'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any paths that contain "extra" files, such as .htaccess or
# robots.txt.
html_extra_path = ['_extra']


# -- Options for LaTeX output -------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ('index', 'doc-nova.tex', u'Nova Documentation',
     u'OpenStack Foundation', 'manual'),
]

# Allow deeper levels of nesting for \begin...\end stanzas
latex_elements = {
    'maxlistdepth': 10,
    'extraclassoptions': 'openany,oneside',
    'preamble': r'''
\setcounter{tocdepth}{3}
\setcounter{secnumdepth}{3}
''',
}

# Disable use of xindy since that's another binary dependency that's not
# available on all platforms
latex_use_xindy = False

# -- Options for openstackdocstheme -------------------------------------------

# openstackdocstheme options
openstackdocs_repo_name = 'openstack/nova'
openstackdocs_bug_project = 'nova'
openstackdocs_bug_tag = 'doc'
openstackdocs_pdf_link = True

# keep this ordered to keep mriedem happy
#
# NOTE(stephenfin): Projects that don't have a release branch, like TripleO and
# reno, should not be included here
openstackdocs_projects = [
    'ceilometer',
    'cinder',
    'cyborg',
    'glance',
    'horizon',
    'ironic',
    'keystone',
    'neutron',
    'nova',
    'oslo.log',
    'oslo.messaging',
    'oslo.i18n',
    'oslo.versionedobjects',
    'placement',
    'python-novaclient',
    'python-openstackclient',
    'watcher',
]
# -- Custom extensions --------------------------------------------------------
