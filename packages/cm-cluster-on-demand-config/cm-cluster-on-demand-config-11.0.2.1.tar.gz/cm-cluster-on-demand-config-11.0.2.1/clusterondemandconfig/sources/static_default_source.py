# Copyright (c) 2004-2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .source import Source

if TYPE_CHECKING:
    from ..configuration import Configuration
    from ..parameter import Parameter


class StaticDefaultSource(Source):
    """Parameter value source that fills the configuration with the default value."""

    def __str__(self) -> str:  # pragma: no cover
        return "default"

    def is_enforcing(self) -> bool:
        return False

    def has_value_for_parameter(self, parameter: Parameter,
                                configuration: Configuration) -> bool:
        return configuration.get_source_of_parameter_value(parameter) is None \
            and not callable(parameter.default)

    def get_value_for_parameter(self, parameter: Parameter,
                                configuration: Configuration) -> Any:
        assert self.has_value_for_parameter(parameter, configuration)

        return parameter.default
