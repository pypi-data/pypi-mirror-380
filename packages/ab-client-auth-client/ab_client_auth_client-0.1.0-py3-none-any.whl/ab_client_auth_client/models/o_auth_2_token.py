from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2Token")


@_attrs_define
class OAuth2Token:
    """
    Attributes:
        access_token (str):
        expires_in (int):
        token_type (str):
        id_token (Union[None, Unset, str]):
        refresh_token (Union[None, Unset, str]):
        scope (Union[None, Unset, str]):
    """

    access_token: str
    expires_in: int
    token_type: str
    id_token: Union[None, Unset, str] = UNSET
    refresh_token: Union[None, Unset, str] = UNSET
    scope: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        expires_in = self.expires_in

        token_type = self.token_type

        id_token: Union[None, Unset, str]
        if isinstance(self.id_token, Unset):
            id_token = UNSET
        else:
            id_token = self.id_token

        refresh_token: Union[None, Unset, str]
        if isinstance(self.refresh_token, Unset):
            refresh_token = UNSET
        else:
            refresh_token = self.refresh_token

        scope: Union[None, Unset, str]
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
                "expires_in": expires_in,
                "token_type": token_type,
            }
        )
        if id_token is not UNSET:
            field_dict["id_token"] = id_token
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token")

        expires_in = d.pop("expires_in")

        token_type = d.pop("token_type")

        def _parse_id_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id_token = _parse_id_token(d.pop("id_token", UNSET))

        def _parse_refresh_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        refresh_token = _parse_refresh_token(d.pop("refresh_token", UNSET))

        def _parse_scope(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scope = _parse_scope(d.pop("scope", UNSET))

        o_auth_2_token = cls(
            access_token=access_token,
            expires_in=expires_in,
            token_type=token_type,
            id_token=id_token,
            refresh_token=refresh_token,
            scope=scope,
        )

        o_auth_2_token.additional_properties = d
        return o_auth_2_token

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
