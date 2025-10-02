# Copyright (c) 2021 Red Hat, Inc.
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from __future__ import absolute_import

import tobiko
from tobiko.shell import ssh
from tobiko.shell.sh import _execute


def make_temp_dir(ssh_client: ssh.SSHClientType = None,
                  sudo: bool = None) \
        -> str:
    test_case = tobiko.get_test_case()
    dir_name: str = _execute.execute('mktemp -d',
                                     ssh_client=ssh_client,
                                     sudo=sudo).stdout.strip()
    test_case.addCleanup(_execute.execute,
                         f'rm -fR "{dir_name}"',
                         ssh_client=ssh_client,
                         sudo=sudo)
    return dir_name
