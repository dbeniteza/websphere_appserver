# Ansible Collection - dbeniteza.websphere_appserver

Collection Name: `dbeniteza.websphere_appserver`
A collection of Middleware modules and roles required for installing and configuring WebSphere Application Server.

* Entries in `galaxy.yml` should point to correct locations
* Molecule config and plays should point to correct collection
    - molecule/default/converge.yml

## Installation

Install this collection locally:

```shell
ansible-galaxy collection install dbeniteza.websphere_appserver
```

## Overview

Collections are a distribution format for Ansible content. You can use collections to package and distribute playbooks, roles, modules, and plugins.
You can publish and use collections through `Ansible Galaxy <https://galaxy.ansible.com/ibm>`.

Assumption for having collection as a repo, is it enable reuse of content as well, such repo can be easily used separately by just adding `ansible.cfg`.

## Collection structure

Collections follow a simple data structure. None of the directories are required unless you have specific content that belongs in one of them. A collection does require a ``galaxy.yml`` file at the root level of the collection. This file contains all of the metadata that Galaxy
and other tools need in order to package, build and publish the collection::

    collection/
    ├── docs/
    ├── galaxy.yml
    ├── plugins/
    │   ├── modules/
    │   │   └── module1.py
    │   ├── inventory/
    │   └── .../
    ├── README.md
    ├── roles/
    │   ├── role1/
    │   ├── role2/
    │   └── .../
    ├── playbooks/
    │   ├── files/
    │   ├── vars/
    │   ├── templates/
    │   └── tasks/
    └── tests/

## Related Information

- [Developing collections](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html)
- [Installation Manager and Packaging Utility download documents](https://www.ibm.com/support/pages/installation-manager-and-packaging-utility-download-documents)
- [System Requirements for IBM Installation Manager and Packaging Utility](https://www.ibm.com/support/pages/system-requirements-ibm-installation-manager-and-packaging-utility)
- [Commands to install Installation Manager](https://www.ibm.com/docs/en/installation-manager/current?topic=group-commands-install-installation-manager)
- [Installation Manager command-line arguments for silent mode](https://www.ibm.com/docs/en/installation-manager/current?topic=mode-installation-manager-command-line-arguments-silent)
- [Response files](https://www.ibm.com/docs/en/installation-manager/current?topic=mode-response-files)
- [Response file variables](https://www.ibm.com/docs/en/installation-manager/current?topic=files-response-file-variables)
- [Sample response file: Installing Installation Manager and packages](https://www.ibm.com/docs/en/installation-manager/current?topic=files-sample-response-file-installing-installation-manager-packages)
- [Searching for updates in silent mode](https://www.ibm.com/docs/en/installation-manager/current?topic=keys-searching-updates-in-silent-mode)
- [IBM Installation Manager Repositories](https://www.ibm.com/docs/en/installation-manager/current?topic=files-repositories)

