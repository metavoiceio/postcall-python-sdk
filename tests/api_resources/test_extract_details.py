# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postcall import Postcall, AsyncPostcall
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtractDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Postcall) -> None:
        extract_detail = client.extract_details.create(
            background_info="background_info",
            call_transcript="call_transcript",
            fields_config=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
            recording_url="recording_url",
        )
        assert_matches_type(object, extract_detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Postcall) -> None:
        response = client.extract_details.with_raw_response.create(
            background_info="background_info",
            call_transcript="call_transcript",
            fields_config=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
            recording_url="recording_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract_detail = response.parse()
        assert_matches_type(object, extract_detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Postcall) -> None:
        with client.extract_details.with_streaming_response.create(
            background_info="background_info",
            call_transcript="call_transcript",
            fields_config=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
            recording_url="recording_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract_detail = response.parse()
            assert_matches_type(object, extract_detail, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtractDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncPostcall) -> None:
        extract_detail = await async_client.extract_details.create(
            background_info="background_info",
            call_transcript="call_transcript",
            fields_config=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
            recording_url="recording_url",
        )
        assert_matches_type(object, extract_detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostcall) -> None:
        response = await async_client.extract_details.with_raw_response.create(
            background_info="background_info",
            call_transcript="call_transcript",
            fields_config=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
            recording_url="recording_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract_detail = await response.parse()
        assert_matches_type(object, extract_detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostcall) -> None:
        async with async_client.extract_details.with_streaming_response.create(
            background_info="background_info",
            call_transcript="call_transcript",
            fields_config=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
            recording_url="recording_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract_detail = await response.parse()
            assert_matches_type(object, extract_detail, path=["response"])

        assert cast(Any, response.is_closed) is True
