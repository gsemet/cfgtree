=====================================
cfgtree - App Configuration made easy
=====================================

.. image:: https://travis-ci.org/gsemet/cfgtree.svg?branch=master
    :target: https://travis-ci.org/gsemet/cfgtree
.. image:: https://readthedocs.org/projects/cfgtree/badge/?version=latest
   :target: http://cfgtree.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://coveralls.io/repos/github/gsemet/cfgtree/badge.svg
   :target: https://coveralls.io/github/gsemet/cfgtree
.. image:: https://badge.fury.io/py/cfgtree.svg
   :target: https://pypi.python.org/pypi/cfgtree/
   :alt: Pypi package
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: ./LICENSE
   :alt: MIT licensed

* Free software: MIT
* Documentation: https://cfgtree.readthedocs.org/en/latest/
* Source: https://github.com/gsemet/cfgtree


Description
===========

This package provides an easy yet comprehensive way of describing, storing, parsing, modifying
user configuration for a modern application.

It requires the following acknolegdments:

- Application settings are stored in a hierarchical structure, they can be organized into
  group of settings, subgroups, and they entierely depends on the application itself.

  This structure is called in cfgtree a "bare configuration", or "configuration tree", and is
  described by a "model".

- User settings may come from different inputs:

  - environment variables ("12-factors" approach). Example: ``MYAPP_VERBOSE``.
  - command line argument. Example: ``--verbose``
  - configuration storage such as file (json, yaml, ini) or configuration server. Example:

    .. code-block:: javascript

        {
            "verbose": true
        {

This allows you to define once your settings structure, and let the user of your application define
the settings throught different ways. For instance, your application can read some settings through
command line arguments, which is very useful for containerization of your application. It is indeed
recommended by `Heroku's 12 Factor Good Practices <https://12factor.net/fr/config>`_.

Describing your configuration through a model also allows to have a configuration validator without
having to maintain both a file schema (ex: JSON Schema) and the parsing logic code.

Access to settings
------------------

In your application, an xpath-like syntax allows you to reach any item of the configuration:
``cfg.get_cfg_value("key1.key2.key3.item")``.

To modify a key configuration, use ``cfg.set_cfg_value("key1.key2.key3.item", "new_value")``. File
is actually written on call of ``cfg.save_configuration()`` or automatically when autosave is set.

See the documentation for full explanation.


Similar opensource projects
===========================

* Openstack's `Olso.config <https://docs.openstack.org/oslo.config/latest/>`_


Documentation
=============

Full documentation is provided on `ReadTheDocs <https://cfgtree.readthedocs.org/en/latest/>`_.
