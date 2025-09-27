from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.o_auth_2_token import OAuth2Token
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/callback",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[OAuth2Token]:
    if response.status_code == 200:
        response_200 = OAuth2Token.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[OAuth2Token]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OAuth2Token]:
    """Callback

     Exchange the authorization code for tokens using the full redirect URL.

    For PKCE, the verifier is auto-fetched from cache via `state` (or falls back to the verifier
    included in the /login response if the caller passes it back).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth2Token]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OAuth2Token]:
    """Callback

     Exchange the authorization code for tokens using the full redirect URL.

    For PKCE, the verifier is auto-fetched from cache via `state` (or falls back to the verifier
    included in the /login response if the caller passes it back).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OAuth2Token
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OAuth2Token]:
    """Callback

     Exchange the authorization code for tokens using the full redirect URL.

    For PKCE, the verifier is auto-fetched from cache via `state` (or falls back to the verifier
    included in the /login response if the caller passes it back).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth2Token]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OAuth2Token]:
    """Callback

     Exchange the authorization code for tokens using the full redirect URL.

    For PKCE, the verifier is auto-fetched from cache via `state` (or falls back to the verifier
    included in the /login response if the caller passes it back).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OAuth2Token
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
