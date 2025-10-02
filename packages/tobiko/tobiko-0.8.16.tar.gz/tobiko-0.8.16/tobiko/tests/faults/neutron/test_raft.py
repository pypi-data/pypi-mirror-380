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

import testtools

from tobiko.openstack import neutron
from tobiko.openstack import tests
from tobiko.tripleo import overcloud
from tobiko.tripleo import undercloud


@neutron.skip_unless_is_ovn()
@undercloud.skip_if_missing_undercloud
@overcloud.skip_unless_ovn_using_raft
class TestRAFTDisruption(testtools.TestCase):

    def test_raft_status(self):
        tests.test_raft_cluster()
        tests.test_raft_clients_connected()

    def test_ovsdb_transation(self):
        tests.test_ovsdb_transactions()
