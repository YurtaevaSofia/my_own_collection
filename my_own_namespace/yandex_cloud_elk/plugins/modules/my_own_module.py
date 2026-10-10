#!/usr/bin/python

# Copyright: (c) 2026, Sofia Yurtaeva <yurtaeva.sofia@yandex.ru>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file with the given content

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description:
    - Creates a text file on the remote host at C(path) with C(content).
    - If the file already exists with the same content, nothing is changed.

options:
    path:
        description: Absolute path to the file on the remote host.
        required: true
        type: path
    content:
        description: Text content to write into the file.
        required: false
        type: str
        default: ''

author:
    - Sofia Yurtaeva (@YurtaevaSofia)
'''

EXAMPLES = r'''
- name: Create file with content
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/hello.txt
    content: hello world

- name: Create empty file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/empty.txt
'''

RETURN = r'''
path:
    description: Path to the file.
    type: str
    returned: always
    sample: '/tmp/hello.txt'
content:
    description: Content of the file.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: Human readable result of the module.
    type: str
    returned: always
    sample: 'File created'
'''

import os

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_bytes, to_native


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='path', required=True),
        content=dict(type='str', required=False, default=''),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    b_path = to_bytes(path, errors='surrogate_or_strict')
    b_content = to_bytes(content, errors='surrogate_or_strict')

    result = dict(
        changed=False,
        path=path,
        content=content,
        message=''
    )

    # compare current state of the file with the desired one
    if os.path.isdir(b_path):
        module.fail_json(msg='Path %s is a directory' % path, **result)

    if os.path.exists(b_path):
        with open(b_path, 'rb') as f:
            if f.read() == b_content:
                result['message'] = 'File already exists with the same content'
                module.exit_json(**result)
        result['message'] = 'File content updated'
    else:
        result['message'] = 'File created'

    result['changed'] = True

    # in check mode only report that the file would be changed
    if module.check_mode:
        module.exit_json(**result)

    try:
        with open(b_path, 'wb') as f:
            f.write(b_content)
    except (IOError, OSError) as e:
        module.fail_json(msg='Failed to write file %s: %s' % (path, to_native(e)), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
