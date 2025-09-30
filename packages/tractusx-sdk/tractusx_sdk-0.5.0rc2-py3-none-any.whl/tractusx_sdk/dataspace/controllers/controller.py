#################################################################################
# Eclipse Tractus-X - Software Development KIT
#
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the
# License for the specific language govern in permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0
#################################################################################

from ..adapters.adapter import Adapter


class Controller:
    adapter: Adapter
    endpoint_url: str

    def __init__(self, adapter: Adapter):
        self.adapter = adapter

    @classmethod
    def builder(cls):
        """
        This method is intended to return a builder for the controller inheriting this class.
        This means that such a controller should implement its own `_Builder` inner class.
        By default, the `Controller._Builder` class is used.

        :return: a builder for the controller inheriting this class
        """
        return cls._Builder(cls)

    class _Builder:
        """
        Default _Builder class for the Controller.
        """

        def __init__(self, cls):
            self.cls = cls
            self._data = {}

        def adapter(self, adapter: Adapter):
            self._data["adapter"] = adapter
            return self

        def data(self, data: dict):
            """
            This method is intended to set all the data of the controller inheriting this class.

            It can be used to set all the data of the controller in a single call, without the need to declare
            each builder method separately. This is useful for cases where a controller may deviate from its base
            controller implementation, and the base controller builder methods are not sufficient to set all the necessary data.
            """

            self._data.update(data)
            return self

        def build(self):
            """
            :return: an instance of the class inheriting the base controller
            """
            return self.cls(**self._data)
