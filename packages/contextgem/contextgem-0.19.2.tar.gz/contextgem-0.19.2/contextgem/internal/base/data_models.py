#
# ContextGem
#
# Copyright 2025 Shcherbak AI AS. All rights reserved. Developed by Sergii Shcherbak.
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
#

"""
Module defining base classes for data validation models.
"""

from __future__ import annotations

import warnings

from pydantic import ConfigDict, Field, StrictFloat, StrictInt, model_validator
from typing_extensions import Self

from contextgem.internal.base.serialization import _InstanceSerializer
from contextgem.internal.decorators import _disable_direct_initialization


@_disable_direct_initialization
class _LLMPricing(_InstanceSerializer):
    """
    Internal implementation of the LLMPricing class.
    """

    input_per_1m_tokens: StrictFloat = Field(
        ...,
        ge=0,
        description="Cost for processing 1 million input tokens.",
    )
    output_per_1m_tokens: StrictFloat = Field(
        ...,
        ge=0,
        description="Cost for generating 1 million output tokens.",
    )

    model_config = ConfigDict(
        extra="forbid", frozen=True
    )  # make immutable once created


# TODO: remove this class in v1.0.0.
@_disable_direct_initialization
class _RatingScale(_InstanceSerializer):
    """
    Internal implementation of the RatingScale class.
    """

    start: StrictInt = Field(
        ge=0, default=0, description="Minimum rating value (inclusive)."
    )
    end: StrictInt = Field(
        gt=0,
        default=10,
        description="Maximum rating value (inclusive). Must be greater than the start value.",
    )

    model_config = ConfigDict(
        extra="forbid", frozen=True
    )  # make immutable once created

    def __init__(self, **data):
        """
        Initialize RatingScale with deprecation warning.
        """
        warnings.warn(
            "RatingScale is deprecated and will be removed in v1.0.0. "
            "Use a tuple of (start, end) integers instead, e.g. (1, 5) "
            "instead of RatingScale(start=1, end=5).",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(**data)

    @model_validator(mode="after")
    def _validate_rating_scale_post(self) -> Self:
        """
        Validates that the end value is greater than the start value.

        :return: The validated model instance.
        :rtype: Self
        :raises ValueError: If the end value is not greater than the start value.
        """
        if self.end <= self.start:
            raise ValueError(
                f"Invalid rating scale: end value ({self.end}) must be greater than start value ({self.start})"
            )
        return self
