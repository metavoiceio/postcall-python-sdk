# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExtractDetailCreateParams", "FieldsConfig"]


class ExtractDetailCreateParams(TypedDict, total=False):
    background_info: Required[str]

    fields_config: Required[Iterable[FieldsConfig]]

    recording_url: Required[str]

    retell_transcript: Required[str]


class FieldsConfig(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    examples: Optional[List[str]]

    instructions_for_extraction: Optional[str]

    required: bool

    type: Literal["string", "boolean"]
