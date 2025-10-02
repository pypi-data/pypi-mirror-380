# Copyright 2022 Red Hat, Inc.
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

import time
import uuid


class WaitTimeout(Exception):
    """Default exception coming from wait_until_true() function."""


def create_row(**kwargs):
    row = type('FakeRow', (object,), kwargs)
    if not hasattr(row, 'uuid'):
        row.uuid = uuid.uuid4()
    return row


class FakeLinuxRoute(dict):
    def get_attr(self, key, default=None):
        for k, v in self.get('attrs', []):
            if k == key:
                return v
        return default


def create_linux_routes(route_info) -> 'list[FakeLinuxRoute]':
    return [FakeLinuxRoute(r) for r in route_info]


def wait_until_true(predicate, timeout=60, sleep=1, exception=None):
    """Wait until callable predicate is evaluated as True

    Imported from ``neutron.common.utils``.

    :param predicate: Callable deciding whether waiting should continue.
    Best practice is to instantiate predicate with functools.partial()
    :param timeout: Timeout in seconds how long should function wait.
    :param sleep: Polling interval for results in seconds.
    :param exception: Exception instance to raise on timeout. If None is passed
                      (default) then WaitTimeout exception is raised.
    """
    start_time = time.time()

    while not predicate():
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            raise exception if exception else WaitTimeout(
                _("Timed out after %d seconds") % timeout
            )
        time.sleep(sleep)
