.. vim: set fileencoding=utf-8:
.. -*- coding: utf-8 -*-
.. +--------------------------------------------------------------------------+
   |                                                                          |
   | Licensed under the Apache License, Version 2.0 (the "License");          |
   | you may not use this file except in compliance with the License.         |
   | You may obtain a copy of the License at                                  |
   |                                                                          |
   |     http://www.apache.org/licenses/LICENSE-2.0                           |
   |                                                                          |
   | Unless required by applicable law or agreed to in writing, software      |
   | distributed under the License is distributed on an "AS IS" BASIS,        |
   | WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. |
   | See the License for the specific language governing permissions and      |
   | limitations under the License.                                           |
   |                                                                          |
   +--------------------------------------------------------------------------+

*******************************************************************************
                                  emcd-appcore
*******************************************************************************

.. image:: https://img.shields.io/pypi/v/emcd-appcore
   :alt: Package Version
   :target: https://pypi.org/project/emcd-appcore/

.. image:: https://img.shields.io/pypi/status/emcd-appcore
   :alt: PyPI - Status
   :target: https://pypi.org/project/emcd-appcore/

.. image:: https://github.com/emcd/python-appcore/actions/workflows/tester.yaml/badge.svg?branch=master&event=push
   :alt: Tests Status
   :target: https://github.com/emcd/python-appcore/actions/workflows/tester.yaml

.. image:: https://emcd.github.io/python-appcore/coverage.svg
   :alt: Code Coverage Percentage
   :target: https://github.com/emcd/python-appcore/actions/workflows/tester.yaml

.. image:: https://img.shields.io/github/license/emcd/python-appcore
   :alt: Project License
   :target: https://github.com/emcd/python-appcore/blob/master/LICENSE.txt

.. image:: https://img.shields.io/pypi/pyversions/emcd-appcore
   :alt: Python Versions
   :target: https://pypi.org/project/emcd-appcore/


🏗️ A Python library package which provides **application foundation
components** - streamlined async initialization, configuration management,
platform directories, logging setup, and environment handling for Python
applications.


Key Features ⭐
===============================================================================

* 🚀 **Async Application Initialization**: Single ``prepare()`` function that
  sets up your entire application foundation with sensible defaults.
* 📁 **Platform Directory Management**: Automatic discovery and creation of
  platform-specific directories for configuration, data, and cache.
* ⚙️ **TOML Configuration System**: Hierarchical configuration loading with
  includes, template variables, and overrides. Can bring your own configuration
  system too.
* 🎯 **Distribution Detection**: Automatic detection of development vs
  production deployment modes with package introspection.
* 📝 **Logging Configuration**: Logging setup with plain and rich modes and
  environment variable overrides.
* 🔄 **Resource Management**: Integration with ``AsyncExitStack`` for proper
  cleanup of async resources.
* 🏷️ **Safety**: Full type annotations with immutable data structures for
  thread safety.


Installation 📦
===============================================================================

Method: Install Python Package
-------------------------------------------------------------------------------

Install via `uv <https://github.com/astral-sh/uv/blob/main/README.md>`_ ``pip``
command:

::

    uv pip install emcd-appcore

Or, install via ``pip``:

::

    pip install emcd-appcore

**Optional Dependencies** ⚙️

For CLI applications, install the ``cli`` extra which includes Tyro and Rich:

::

    pip install emcd-appcore[cli]

For enhanced console output without CLI framework:

::

    pip install emcd-appcore[rich]


Examples 💡
===============================================================================


Quick Start 🚀
-------------------------------------------------------------------------------

The simplest way to initialize your application:

>>> import asyncio
>>> import contextlib
>>> import appcore
>>> async def main( ):
...     async with contextlib.AsyncExitStack( ) as exits:
...         auxdata = await appcore.prepare( exits )
...         print( f"App: {auxdata.application.name}" )
...         return auxdata.configuration
>>> # asyncio.run( main( ) )  # Returns configuration dictionary


Platform Directories 📁
-------------------------------------------------------------------------------

Access platform-specific directories for your application:

>>> async def display_directories( ):
...     async with contextlib.AsyncExitStack( ) as exits:
...         application = appcore.ApplicationInformation(
...             name = 'my-app', publisher = 'MyCompany' )
...         auxdata = await appcore.prepare( exits, application = application )
...         dirs = auxdata.directories
...         print( f"Config: {dirs.user_config_path}" )
...         print( f"Data: {dirs.user_data_path}" )
...         print( f"Cache: {dirs.user_cache_path}" )
>>> # asyncio.run( display_directories( ) )


Building CLI Applications 🔧
-------------------------------------------------------------------------------

Build command-line applications using the ``appcore.cli`` module:

>>> import asyncio
>>> from appcore import cli, state
>>> class HelloCommand( cli.Command ):
...     async def execute( self, auxdata: state.Globals ) -> None:
...         print( f"Hello from {auxdata.application.name}!" )
>>> class MyApplication( cli.Application ):
...     async def execute( self, auxdata: state.Globals ) -> None:
...         command = HelloCommand( )
...         await command( auxdata )
>>> # asyncio.run( MyApplication( )( ) )

The ``appcore`` CLI tool demonstrates these capabilities in action - inspect configuration, environment variables, and platform directories:

::

    $ python -m appcore configuration --display.presentation json
    $ python -m appcore environment
    $ python -m appcore directories --display.target-file dirs.txt

For a comprehensive implementation example, see ``sources/appcore/introspection.py`` which shows advanced patterns including subcommands, display options, and presentation formats.


Dependencies & Architecture 🏛️
===============================================================================

Appcore is built on a foundation of proven, lightweight dependencies:

* **Configuration**: Uses standard library ``tomli`` for TOML parsing with
  `accretive <https://pypi.org/project/accretive/>`_ data structures that can
  grow but never shrink.
* **Platform Integration**: Leverages ``platformdirs`` for cross-platform
  directory discovery and ``aiofiles`` for async file operations.
* **Logging Enhancement**: Optional integration with `Rich
  <https://github.com/Textualize/rich>`_ for enhanced console output with
  graceful fallbacks.
* **Distribution Management**: Uses ``importlib-metadata`` and
  ``importlib-resources`` for package introspection and resource handling.

The architecture emphasizes:

* **Immutability**: All configuration and state objects are immutable after
  creation, preventing accidental modifications.
* **Async-First**: Built from the ground up for async/await patterns with
  proper resource management.
* **Dependency Injection**: Configurable components that can be replaced or
  extended without modifying core functionality.
* **Type Safety**: Comprehensive type annotations for excellent IDE support
  and static analysis.


Contribution 🤝
===============================================================================

Contribution to this project is welcome! However, it must follow the `code of
conduct
<https://emcd.github.io/python-project-common/stable/sphinx-html/common/conduct.html>`_
for the project.

Please file bug reports and feature requests in the `issue tracker
<https://github.com/emcd/python-appcore/issues>`_ or submit `pull
requests <https://github.com/emcd/python-appcore/pulls>`_ to
improve the source code or documentation.

For development guidance and standards, please see the `development guide
<https://emcd.github.io/python-appcore/stable/sphinx-html/contribution.html#development>`_.


Additional Indicia
===============================================================================

.. image:: https://img.shields.io/github/last-commit/emcd/python-appcore
   :alt: GitHub last commit
   :target: https://github.com/emcd/python-appcore

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json
   :alt: Copier
   :target: https://github.com/copier-org/copier

.. image:: https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg
   :alt: Hatch
   :target: https://github.com/pypa/hatch

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
   :alt: pre-commit
   :target: https://github.com/pre-commit/pre-commit

.. image:: https://microsoft.github.io/pyright/img/pyright_badge.svg
   :alt: Pyright
   :target: https://microsoft.github.io/pyright

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :alt: Ruff
   :target: https://github.com/astral-sh/ruff

.. image:: https://img.shields.io/pypi/implementation/emcd-appcore
   :alt: PyPI - Implementation
   :target: https://pypi.org/project/emcd-appcore/

.. image:: https://img.shields.io/pypi/wheel/emcd-appcore
   :alt: PyPI - Wheel
   :target: https://pypi.org/project/emcd-appcore/


Other Projects by This Author 🌟
===============================================================================

* `python-absence <https://github.com/emcd/python-absence>`_ (`absence <https://pypi.org/project/absence/>`_ on PyPI)

  🕳️ A Python library package which provides a **sentinel for absent values** - a falsey, immutable singleton that represents the absence of a value in contexts where ``None`` or ``False`` may be valid values.

* `python-accretive <https://github.com/emcd/python-accretive>`_ (`accretive <https://pypi.org/project/accretive/>`_ on PyPI)

  🌌 A Python library package which provides **accretive data structures** - collections which can grow but never shrink.

* `python-classcore <https://github.com/emcd/python-classcore>`_ (`classcore <https://pypi.org/project/classcore/>`_ on PyPI)

  🏭 A Python library package which provides **foundational class factories and decorators** for providing classes with attributes immutability and concealment and other custom behaviors.

* `python-dynadoc <https://github.com/emcd/python-dynadoc>`_ (`dynadoc <https://pypi.org/project/dynadoc/>`_ on PyPI)

  📝 A Python library package which bridges the gap between **rich annotations** and **automatic documentation generation** with configurable renderers and support for reusable fragments.

* `python-falsifier <https://github.com/emcd/python-falsifier>`_ (`falsifier <https://pypi.org/project/falsifier/>`_ on PyPI)

  🎭 A very simple Python library package which provides a **base class for falsey objects** - objects that evaluate to ``False`` in boolean contexts.

* `python-frigid <https://github.com/emcd/python-frigid>`_ (`frigid <https://pypi.org/project/frigid/>`_ on PyPI)

  🔒 A Python library package which provides **immutable data structures** - collections which cannot be modified after creation.

* `python-icecream-truck <https://github.com/emcd/python-icecream-truck>`_ (`icecream-truck <https://pypi.org/project/icecream-truck/>`_ on PyPI)

  🍦 **Flavorful Debugging** - A Python library which enhances the powerful and well-known ``icecream`` package with flavored traces, configuration hierarchies, customized outputs, ready-made recipes, and more.

* `python-mimeogram <https://github.com/emcd/python-mimeogram>`_ (`mimeogram <https://pypi.org/project/mimeogram/>`_ on PyPI)

  📨 A command-line tool for **exchanging collections of files with Large Language Models** - bundle multiple files into a single clipboard-ready document while preserving directory structure and metadata... good for code reviews, project sharing, and LLM interactions.
