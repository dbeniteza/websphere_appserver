#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Contributors to the Ansible project

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'self'}

DOCUMENTATION = r'''
---
module: iim_package
short_description: Install/Update packages using IBM Installation Manager
description:
  - Install or update packages using IBM Installation Manager (must be installed using the "iim" role).
version_added: 0.1.0
author: Daniel Benitez (@dbeniteza)
options:
  iim_path:
    description:
      - Absolute path to an existing installation of IBM Installation Manager.
    required: false
    default: /opt/IBM/InstallationManager
    type: path
    version_added: "0.1.0"
  product_id:
    description:
      - Product ID to be installed/updated/deleted.
      - May be product family, or a specific product ID instance (including FixPack details).
    required: true
    type: list
    elements: str
  path:
    description:
      - Absolute path where the package should be installed.
    required: false
    type: path
  preferences:
    description:
      - A dictionary to be passed to the installer as preferences flag.
    required: false
    type: dict
  properties:
    description:
      - A dictionary to be passed to the installer as properties flag.
    required: false
    type: dict
  repos:
    description:
      - List of repositories to include when installing the package(s) specified by C(product_id).
    required: false
    type: list
    elements: str
  shared_resources:
    description:
      - Absolute path to an existing location of the shared resources directory for IIM.
    required: false
    default: /opt/IBM/IMShared
    type: path
  state: 
    description:
      - Desired state of the package denoted by C(product_id).
    required: false
    default: present
    choices:
      - absent
      - present
    type: str
'''

EXAMPLES = r'''
---
- name: Install WebSphere Liberty
  dbeniteza.websphere_appserver.iim_package:
    iim_path: /opt/IBM/InstallationManager
    product_id: com.ibm.websphere.liberty.ND
    path: /opt/IBM/WebSphere/Liberty
    repo: /tmp/was-repo
    state: present
'''

RETURN = r'''
---
packages:
  description: List of installed packages.
  returned: always
  type: list
  elements: str
  version_added: "0.1.0"
base_installed:
  description: Indicator if the product is installed.
  returned: always
  type: str
  version_added: "0.1.0"
exact_installed:
  description: Indicator if the exact version of the product is installed.
  returned: when supported
  type: str
  version_added: "0.1.0"
'''

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import logging.config
import os
import re
import sys

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dbeniteza.websphere_appserver.plugins.module_utils.iim import IIMAgent

logger = logging.getLogger(sys.argv[0])


def main():
    module = AnsibleModule(
        argument_spec=dict(
            iim_path=dict(default='/opt/IBM/InstallationManager', type='path'),
            shared_resources=dict(default='/opt/IBM/IMShared', type='path'),
            repos=dict(type='list', aliases=['repo'], elements='str'),
            product_id=dict(type='list', elements='str', required=True),
            path=dict(type='path'),
            preferences=dict(type='dict'),
            properties=dict(type='dict'),
            state=dict(default='present', choices=['absent', 'present'])
        ),
        supports_check_mode=False
    )

    iim = IIMAgent(module)

    # Process all arguments
    state = module.params['state']
    product_id = module.params['product_id']
    result = dict(changed=False)

    if state == 'absent':
        if iim.have_base_version(product_id[0]):
            result = iim.uninstall_package(product_id)
            module.exit_json(**result)
        else:
            module.exit_json(**result)

    if state == 'present' and (not iim.have_base_version(product_id[0]) or not iim.have_exact_version(product_id[0])):
        result = iim.install_package(product_id)
        module.exit_json(**result)

    module.fail_json('Should have exited cleanly by now ...', **result)


if __name__ == '__main__':
    main()
