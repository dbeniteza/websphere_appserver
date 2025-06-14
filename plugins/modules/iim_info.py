#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Contributors to the Ansible project
# Apache-2.0 license (see LICENSE or https://www.apache.org/licenses/LICENSE-2.0)

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'self'}

DOCUMENTATION = r'''
---
module: iim_info
short_description: List packages installed by IBM Installation Manager
description:
  - See what packages are installed by IBM Installation Manager.
  - If C(product_id) is provided, check if that specific package is installed.
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
      - May be product family, or a specific product ID instance (including FixPack details).
    required: true
    type: list
    elements: str
'''

EXAMPLES = r'''
---
- name: Check packages
  dbeniteza.websphere_appserver.iim_info:
    iim_path: /opt/IBM/InstallationManager
    product_id: com.ibm.websphere.liberty.ND
  register: iim_info

- name: List packages intalled by IIM
  ansible.builtin.debug:
    msg: "Packages installed {{ iim_info.packages }}"
  when: iim_info.base_installed
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
            product_id=dict(type='list', elements='str', required=True)
        ),
        supports_check_mode=False
    )

    iim = IIMAgent(module)

    product_id = module.params['product_id']

    result = dict(changed=False)
    result['packages'] = iim.list_installed_packages()

    if product_id is not None:
        result['base_installed'] = iim.have_base_version(product_id[0])
        result['exact_installed'] = iim.have_exact_version(product_id[0])

    module.exit_json(**result)


if __name__ == '__main__':
    main()
