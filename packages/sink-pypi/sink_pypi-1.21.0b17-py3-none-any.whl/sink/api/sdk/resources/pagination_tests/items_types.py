# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPagePageNumber, AsyncPagePageNumber
from ..._base_client import AsyncPaginator, make_request_options
from ...types.pagination_tests import items_type_list_unknown_params

__all__ = ["ItemsTypesResource", "AsyncItemsTypesResource"]


class ItemsTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sink-python-public#accessing-raw-response-data-eg-headers
        """
        return ItemsTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sink-python-public#with_streaming_response
        """
        return ItemsTypesResourceWithStreamingResponse(self)

    def list_unknown(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPagePageNumber[object]:
        """
        Test case for paginated items of `unknown` types with page_number pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/items_types/unknown",
            page=SyncPagePageNumber[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    items_type_list_unknown_params.ItemsTypeListUnknownParams,
                ),
            ),
            model=object,
        )


class AsyncItemsTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sink-python-public#accessing-raw-response-data-eg-headers
        """
        return AsyncItemsTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sink-python-public#with_streaming_response
        """
        return AsyncItemsTypesResourceWithStreamingResponse(self)

    def list_unknown(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[object, AsyncPagePageNumber[object]]:
        """
        Test case for paginated items of `unknown` types with page_number pagination

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/paginated/items_types/unknown",
            page=AsyncPagePageNumber[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    items_type_list_unknown_params.ItemsTypeListUnknownParams,
                ),
            ),
            model=object,
        )


class ItemsTypesResourceWithRawResponse:
    def __init__(self, items_types: ItemsTypesResource) -> None:
        self._items_types = items_types

        self.list_unknown = _legacy_response.to_raw_response_wrapper(
            items_types.list_unknown,
        )


class AsyncItemsTypesResourceWithRawResponse:
    def __init__(self, items_types: AsyncItemsTypesResource) -> None:
        self._items_types = items_types

        self.list_unknown = _legacy_response.async_to_raw_response_wrapper(
            items_types.list_unknown,
        )


class ItemsTypesResourceWithStreamingResponse:
    def __init__(self, items_types: ItemsTypesResource) -> None:
        self._items_types = items_types

        self.list_unknown = to_streamed_response_wrapper(
            items_types.list_unknown,
        )


class AsyncItemsTypesResourceWithStreamingResponse:
    def __init__(self, items_types: AsyncItemsTypesResource) -> None:
        self._items_types = items_types

        self.list_unknown = async_to_streamed_response_wrapper(
            items_types.list_unknown,
        )
