# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
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
# NOTE(sean-k-mooney): watcher does not split up the tests that need eventlet
# and those that do not currently so we need to monkey patch all the tests.
# as an example the watcher.test.cmd module is importing watcher.cmd,
# that has the side effect of monkey patching the test executor
# after many modules are already imported.
from watcher import eventlet
eventlet.patch()

# NOTE(dviroel): oslo service backend needs to be initialize
# as soon as possible, before importing oslo service. If eventlet
# patching is enabled, it should be patched before calling this
# function
from watcher.common import oslo_service_helper as helper  # noqa E402
helper.init_oslo_service_backend()

from watcher import objects  # noqa E402

# NOTE(comstud): Make sure we have all of the objects loaded. We do this
# at module import time, because we may be using mock decorators in our
# tests that run at import time.
objects.register_all()
