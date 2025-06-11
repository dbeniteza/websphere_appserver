.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.16.3

.. Anchors

.. _ansible_collections.dbeniteza.websphere_appserver.iim_info_module:

.. Anchors: short name for ansible.builtin

.. Title

dbeniteza.websphere_appserver.iim_info module -- List packages installed by IBM Installation Manager
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `dbeniteza.websphere_appserver collection <https://galaxy.ansible.com/ui/repo/published/dbeniteza/websphere_appserver/>`_ (version 1.0.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install dbeniteza.websphere\_appserver`.

    To use it in a playbook, specify: :code:`dbeniteza.websphere_appserver.iim_info`.

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

- See what packages are installed by IBM Installation Manager.


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

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_info_module__parameter-iim_path:

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
        <div class="ansibleOptionAnchor" id="parameter-product_id"></div>

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_info_module__parameter-product_id:

      .. rst-class:: ansible-option-title

      **product_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-product_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      May be product family, or a specific product ID instance (including FixPack details)


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
    - name: Check packages
      iim_info:
        iim_path: /opt/IBM/InstallationManager
        product_id: com.ibm.websphere.liberty.ND
      register: iim_info

    - name: List packages intalled by IIM
      ansible.builtin.debug:
        msg: "Packages installed {{ iim_info.packages }}"
      when: iim_info.base_installed



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

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_info_module__return-base_installed:

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

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_info_module__return-exact_installed:

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

      .. _ansible_collections.dbeniteza.websphere_appserver.iim_info_module__return-packages:

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
