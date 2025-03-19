# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import extract_detail_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ExtractDetailsResource", "AsyncExtractDetailsResource"]


class ExtractDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtractDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/metavoiceio/postcall-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ExtractDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/metavoiceio/postcall-python-sdk#with_streaming_response
        """
        return ExtractDetailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        background_info: str,
        call_transcript: str,
        fields_config: Iterable[extract_detail_create_params.FieldsConfig],
        recording_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Given a recording URL, a transcript, some background information, and a list of
        field configurations, this endpoint will:

        return a dictionary of extracted details according to the provided
        `fields_config`.

        Args:
          background_info: Additional context that helps guide what should be extracted from the transcript
              (e.g. information about the business).

          call_transcript: A string representing transcript of the call.

          fields_config: List of field configuration objects specifying what to extract from the
              transcript.

          recording_url: URL to the audio file of the call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extract_details",
            body=maybe_transform(
                {
                    "background_info": background_info,
                    "call_transcript": call_transcript,
                    "fields_config": fields_config,
                    "recording_url": recording_url,
                },
                extract_detail_create_params.ExtractDetailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncExtractDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtractDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/metavoiceio/postcall-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/metavoiceio/postcall-python-sdk#with_streaming_response
        """
        return AsyncExtractDetailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        background_info: str,
        call_transcript: str,
        fields_config: Iterable[extract_detail_create_params.FieldsConfig],
        recording_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Given a recording URL, a transcript, some background information, and a list of
        field configurations, this endpoint will:

        return a dictionary of extracted details according to the provided
        `fields_config`.

        Args:
          background_info: Additional context that helps guide what should be extracted from the transcript
              (e.g. information about the business).

          call_transcript: A string representing transcript of the call.

          fields_config: List of field configuration objects specifying what to extract from the
              transcript.

          recording_url: URL to the audio file of the call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extract_details",
            body=await async_maybe_transform(
                {
                    "background_info": background_info,
                    "call_transcript": call_transcript,
                    "fields_config": fields_config,
                    "recording_url": recording_url,
                },
                extract_detail_create_params.ExtractDetailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ExtractDetailsResourceWithRawResponse:
    def __init__(self, extract_details: ExtractDetailsResource) -> None:
        self._extract_details = extract_details

        self.create = to_raw_response_wrapper(
            extract_details.create,
        )


class AsyncExtractDetailsResourceWithRawResponse:
    def __init__(self, extract_details: AsyncExtractDetailsResource) -> None:
        self._extract_details = extract_details

        self.create = async_to_raw_response_wrapper(
            extract_details.create,
        )


class ExtractDetailsResourceWithStreamingResponse:
    def __init__(self, extract_details: ExtractDetailsResource) -> None:
        self._extract_details = extract_details

        self.create = to_streamed_response_wrapper(
            extract_details.create,
        )


class AsyncExtractDetailsResourceWithStreamingResponse:
    def __init__(self, extract_details: AsyncExtractDetailsResource) -> None:
        self._extract_details = extract_details

        self.create = async_to_streamed_response_wrapper(
            extract_details.create,
        )
