from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.o_auth_2_authorize_response import OAuth2AuthorizeResponse
from ...models.pkce_authorize_response import PKCEAuthorizeResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    scope: Union[Unset, str] = "openid email profile",
    response_type: Union[Unset, str] = "code",
    identity_provider: Union[None, Unset, str] = "Google",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["scope"] = scope

    params["response_type"] = response_type

    json_identity_provider: Union[None, Unset, str]
    if isinstance(identity_provider, Unset):
        json_identity_provider = UNSET
    else:
        json_identity_provider = identity_provider
    params["identity_provider"] = json_identity_provider

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/login",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Union["OAuth2AuthorizeResponse", "PKCEAuthorizeResponse"]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["OAuth2AuthorizeResponse", "PKCEAuthorizeResponse"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = OAuth2AuthorizeResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = PKCEAuthorizeResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, Union["OAuth2AuthorizeResponse", "PKCEAuthorizeResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    scope: Union[Unset, str] = "openid email profile",
    response_type: Union[Unset, str] = "code",
    identity_provider: Union[None, Unset, str] = "Google",
) -> Response[Union[HTTPValidationError, Union["OAuth2AuthorizeResponse", "PKCEAuthorizeResponse"]]]:
    """Get Login Url

     Build an OIDC authorize URL (Standard or PKCE) using the shared auth client.

    If PKCE, a fresh verifier/challenge is generated and (optionally) persisted to cache keyed by
    `state`.

    Args:
        scope (Union[Unset, str]):  Default: 'openid email profile'.
        response_type (Union[Unset, str]):  Default: 'code'.
        identity_provider (Union[None, Unset, str]):  Default: 'Google'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['OAuth2AuthorizeResponse', 'PKCEAuthorizeResponse']]]
    """

    kwargs = _get_kwargs(
        scope=scope,
        response_type=response_type,
        identity_provider=identity_provider,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    scope: Union[Unset, str] = "openid email profile",
    response_type: Union[Unset, str] = "code",
    identity_provider: Union[None, Unset, str] = "Google",
) -> Optional[Union[HTTPValidationError, Union["OAuth2AuthorizeResponse", "PKCEAuthorizeResponse"]]]:
    """Get Login Url

     Build an OIDC authorize URL (Standard or PKCE) using the shared auth client.

    If PKCE, a fresh verifier/challenge is generated and (optionally) persisted to cache keyed by
    `state`.

    Args:
        scope (Union[Unset, str]):  Default: 'openid email profile'.
        response_type (Union[Unset, str]):  Default: 'code'.
        identity_provider (Union[None, Unset, str]):  Default: 'Google'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['OAuth2AuthorizeResponse', 'PKCEAuthorizeResponse']]
    """

    return sync_detailed(
        client=client,
        scope=scope,
        response_type=response_type,
        identity_provider=identity_provider,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    scope: Union[Unset, str] = "openid email profile",
    response_type: Union[Unset, str] = "code",
    identity_provider: Union[None, Unset, str] = "Google",
) -> Response[Union[HTTPValidationError, Union["OAuth2AuthorizeResponse", "PKCEAuthorizeResponse"]]]:
    """Get Login Url

     Build an OIDC authorize URL (Standard or PKCE) using the shared auth client.

    If PKCE, a fresh verifier/challenge is generated and (optionally) persisted to cache keyed by
    `state`.

    Args:
        scope (Union[Unset, str]):  Default: 'openid email profile'.
        response_type (Union[Unset, str]):  Default: 'code'.
        identity_provider (Union[None, Unset, str]):  Default: 'Google'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['OAuth2AuthorizeResponse', 'PKCEAuthorizeResponse']]]
    """

    kwargs = _get_kwargs(
        scope=scope,
        response_type=response_type,
        identity_provider=identity_provider,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    scope: Union[Unset, str] = "openid email profile",
    response_type: Union[Unset, str] = "code",
    identity_provider: Union[None, Unset, str] = "Google",
) -> Optional[Union[HTTPValidationError, Union["OAuth2AuthorizeResponse", "PKCEAuthorizeResponse"]]]:
    """Get Login Url

     Build an OIDC authorize URL (Standard or PKCE) using the shared auth client.

    If PKCE, a fresh verifier/challenge is generated and (optionally) persisted to cache keyed by
    `state`.

    Args:
        scope (Union[Unset, str]):  Default: 'openid email profile'.
        response_type (Union[Unset, str]):  Default: 'code'.
        identity_provider (Union[None, Unset, str]):  Default: 'Google'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['OAuth2AuthorizeResponse', 'PKCEAuthorizeResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            scope=scope,
            response_type=response_type,
            identity_provider=identity_provider,
        )
    ).parsed
