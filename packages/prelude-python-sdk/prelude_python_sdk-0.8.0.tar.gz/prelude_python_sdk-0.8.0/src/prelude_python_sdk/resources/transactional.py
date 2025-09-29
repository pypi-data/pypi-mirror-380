# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import transactional_send_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.transactional_send_response import TransactionalSendResponse

__all__ = ["TransactionalResource", "AsyncTransactionalResource"]


class TransactionalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TransactionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return TransactionalResourceWithStreamingResponse(self)

    def send(
        self,
        *,
        template_id: str,
        to: str,
        callback_url: str | Omit = omit,
        correlation_id: str | Omit = omit,
        expires_at: str | Omit = omit,
        from_: str | Omit = omit,
        locale: str | Omit = omit,
        variables: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionalSendResponse:
        """
        Send a transactional message to your user.

        Args:
          template_id: The template identifier.

          to: The recipient's phone number.

          callback_url: The callback URL.

          correlation_id: A user-defined identifier to correlate this transactional message with. It is
              returned in the response and any webhook events that refer to this
              transactionalmessage.

          expires_at: The message expiration date.

          from_: The Sender ID.

          locale: A BCP-47 formatted locale string with the language the text message will be sent
              to. If there's no locale set, the language will be determined by the country
              code of the phone number. If the language specified doesn't exist, the default
              set on the template will be used.

          variables: The variables to be replaced in the template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/transactional",
            body=maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "callback_url": callback_url,
                    "correlation_id": correlation_id,
                    "expires_at": expires_at,
                    "from_": from_,
                    "locale": locale,
                    "variables": variables,
                },
                transactional_send_params.TransactionalSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionalSendResponse,
        )


class AsyncTransactionalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncTransactionalResourceWithStreamingResponse(self)

    async def send(
        self,
        *,
        template_id: str,
        to: str,
        callback_url: str | Omit = omit,
        correlation_id: str | Omit = omit,
        expires_at: str | Omit = omit,
        from_: str | Omit = omit,
        locale: str | Omit = omit,
        variables: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionalSendResponse:
        """
        Send a transactional message to your user.

        Args:
          template_id: The template identifier.

          to: The recipient's phone number.

          callback_url: The callback URL.

          correlation_id: A user-defined identifier to correlate this transactional message with. It is
              returned in the response and any webhook events that refer to this
              transactionalmessage.

          expires_at: The message expiration date.

          from_: The Sender ID.

          locale: A BCP-47 formatted locale string with the language the text message will be sent
              to. If there's no locale set, the language will be determined by the country
              code of the phone number. If the language specified doesn't exist, the default
              set on the template will be used.

          variables: The variables to be replaced in the template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/transactional",
            body=await async_maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "callback_url": callback_url,
                    "correlation_id": correlation_id,
                    "expires_at": expires_at,
                    "from_": from_,
                    "locale": locale,
                    "variables": variables,
                },
                transactional_send_params.TransactionalSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionalSendResponse,
        )


class TransactionalResourceWithRawResponse:
    def __init__(self, transactional: TransactionalResource) -> None:
        self._transactional = transactional

        self.send = to_raw_response_wrapper(
            transactional.send,
        )


class AsyncTransactionalResourceWithRawResponse:
    def __init__(self, transactional: AsyncTransactionalResource) -> None:
        self._transactional = transactional

        self.send = async_to_raw_response_wrapper(
            transactional.send,
        )


class TransactionalResourceWithStreamingResponse:
    def __init__(self, transactional: TransactionalResource) -> None:
        self._transactional = transactional

        self.send = to_streamed_response_wrapper(
            transactional.send,
        )


class AsyncTransactionalResourceWithStreamingResponse:
    def __init__(self, transactional: AsyncTransactionalResource) -> None:
        self._transactional = transactional

        self.send = async_to_streamed_response_wrapper(
            transactional.send,
        )
