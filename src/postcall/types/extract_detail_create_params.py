# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExtractDetailCreateParams", "FieldsConfig"]


class ExtractDetailCreateParams(TypedDict, total=False):
    background_info: Required[str]
    """
    Additional context that helps guide what should be extracted from the transcript
    (e.g. information about the business).
    """

    fields_config: Required[Iterable[FieldsConfig]]
    """
    List of field configuration objects specifying what to extract from the
    transcript.
    """

    recording_url: Required[str]
    """URL to the audio file of the call."""

    retell_transcript: Required[str]
    """A string representing transcript of the call."""


class FieldsConfig(TypedDict, total=False):
    description: Required[str]
    """
    A human-readable description of what this field contains (e.g., 'The caller's
    email address').
    """

    name: Required[str]
    """
    The unique name of this field to be extracted (e.g., 'email', 'phone',
    'summary').
    """

    examples: Optional[List[str]]
    """Optional example values for this field to guide the extraction."""

    instructions_for_extraction: Optional[str]
    """
    Additional instructions or constraints about how to extract this field from the
    transcript.
    """

    required: bool
    """Indicates if this field is mandatory in the extracted results."""

    type: Literal["string", "boolean"]
    """The JSON data type for this field.

    Currently, only 'string' or 'boolean' are supported.
    """
