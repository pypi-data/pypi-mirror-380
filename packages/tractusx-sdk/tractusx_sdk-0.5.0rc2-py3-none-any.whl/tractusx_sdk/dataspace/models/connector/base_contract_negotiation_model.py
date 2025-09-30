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

from abc import ABC
from typing import Optional, Union
from pydantic import Field

from .base_policy_model import BasePolicyModel
from ..model import BaseModel


class BaseContractNegotiationModel(BaseModel, ABC):
    """
    Base model class for representing a connector's contract negotiation.
    """

    counter_party_address: str
    offer_id: str
    offer_policy: dict
    asset_id: str
    provider_id: str
    context: Optional[Union[dict, list, str]] = Field(default={
        "@vocab": "https://w3id.org/edc/v0.0.1/ns/"
    })
    callback_addresses: Optional[list[dict]] = Field(default_factory=list)
    protocol: Optional[str] = Field(default="dataspace-protocol-http")

    class _Builder(BaseModel._Builder):
        def context(self, context: dict):
            self._data["context"] = context
            return self

        def counter_party_address(self, counter_party_address: str):
            self._data["counter_party_address"] = counter_party_address
            return self

        def offer_id(self, offer_id: str):
            self._data["offer_id"] = offer_id
            return self

        def asset_id(self, asset_id: str):
            self._data["asset_id"] = asset_id
            return self

        def provider_id(self, provider_id: str):
            self._data["provider_id"] = provider_id
            return self

        def offer_policy_from_policy_model(self, policy_model: BasePolicyModel):
            # Remove unnecessary fields from a policy model's policy data
            policy_data = policy_model.to_data()["policy"]
            policy_data.pop("@id", None)
            policy_data.pop("@type", None)

            return self.offer_policy(policy_data)

        def offer_policy(self, offer_policy: dict):
            self._data["offer_policy"] = offer_policy
            return self

        def callback_addresses(self, callback_addresses: list[dict]):
            self._data["callback_addresses"] = callback_addresses
            return self

        def protocol(self, protocol: str):
            self._data["protocol"] = protocol
            return self
