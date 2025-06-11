.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.16.3

.. Anchors

.. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module:

.. Anchors: short name for ansible.builtin

.. Title

dbeniteza.websphere_appserver.iim_package module -- Install/Update packages using IBM Installation Manager
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `dbeniteza.websphere_appserver collection <https://galaxy.ansible.com/ui/repo/published/dbeniteza/websphere_appserver/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install dbeniteza.websphere\_appserver`.

    To use it in a playbook, specify: :code:`dbeniteza.websphere_appserver.iim_package`.

.. version_added

.. rst-class:: ansible-version-added

New in dbeniteza.websphere\_appserver 0.1.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Install or update packages using IBM Installation Manager (must be installed using the "iim" role)


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-iim_path"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__parameter-iim_path:

      .. rst-class:: ansible-option-title

      **iim_path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-iim_path" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`path`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Absolute path to an existing installation of IBM Installation Manager


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"/opt/IBM/InstallationManager"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-path"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__parameter-path:

      .. rst-class:: ansible-option-title

      **path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-path" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`path`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Absolute path where the package should be installed


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-preferences"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__parameter-preferences:

      .. rst-class:: ansible-option-title

      **preferences**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-preferences" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A dictionary to be passed to the installer as preferences flag


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-product_id"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__parameter-product_id:

      .. rst-class:: ansible-option-title

      **product_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-product_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Product ID to be installed/updated/deleted.

      May be product family, or a specific product ID instance (including FixPack details)


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-properties"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__parameter-properties:

      .. rst-class:: ansible-option-title

      **properties**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-properties" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A dictionary to be passed to the installer as properties flag


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-repos"></div>
        <div class="ansibleOptionAnchor" id="parameter-repo"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__parameter-repo:
      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__parameter-repos:

      .. rst-class:: ansible-option-title

      **repos**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-repos" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-aliases:`aliases: repo`

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of repositories to include when installing the package(s) specified by :literal:`product\_id`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-shared_resources"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__parameter-shared_resources:

      .. rst-class:: ansible-option-title

      **shared_resources**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-shared_resources" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`path`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Absolute path to an existing location of the shared resources directory for IIM


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"/opt/IBM/IMShared"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Desired state of the package denoted by :literal:`product\_id`


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    ---
    - name: Install WebSphere Liberty
      iim_package:
        product_id: com.ibm.websphere.liberty.ND
        path: /opt/IBM/WebSphere/Liberty
        repo: /tmp/wlp-repo



.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-base_installed"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__return-base_installed:

      .. rst-class:: ansible-option-title

      **base_installed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-base_installed" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicator if the product is installed.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-exact_installed"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__return-exact_installed:

      .. rst-class:: ansible-option-title

      **exact_installed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-exact_installed" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicator if the exact version of the product is installed.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when supported


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-packages"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_package_module__return-packages:

      .. rst-class:: ansible-option-title

      **packages**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-packages" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of installed packages.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Daniel Benitez Aguila (@dbeniteza)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/dbeniteza/websphere_appserver/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/dbeniteza/websphere_appserver"
    external: true


.. Parsing errors
