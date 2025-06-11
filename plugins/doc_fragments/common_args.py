#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Contributors to the Ansible project
# Apache-2.0 license (see LICENSE or https://www.apache.org/licenses/LICENSE-2.0)

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'self'}

class ModuleDocFragment(object):
  # Standard documentation
  DOCUMENTATION = r'''
  ---
  options:
    iim_path:
      description:
        - Absolute path to an existing installation of IBM Installation Manager.
      required: false
      default: /opt/IBM/InstallationManager
      type: path
      version_added: "0.1.0"
    product_id:
      type: list
      elements: str
      description:
          - May be product family, or a specific product ID instance (including FixPack details).
  seealso:
    - name: Product offerings
      description: WebSphere Application Server product offerings for supported operating systems
      link: https://www.ibm.com/docs/en/was/9.0.5?topic=installation-product-offerings-supported-operating-systems
  '''
