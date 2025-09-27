from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PKCEAuthorizeResponse")


@_attrs_define
class PKCEAuthorizeResponse:
    """
    Attributes:
        url (str):
        state (str):
        code_verifier (str):
        code_challenge (str):
        code_challenge_method (str):
    """

    url: str
    state: str
    code_verifier: str
    code_challenge: str
    code_challenge_method: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        state = self.state

        code_verifier = self.code_verifier

        code_challenge = self.code_challenge

        code_challenge_method = self.code_challenge_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "state": state,
                "code_verifier": code_verifier,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        state = d.pop("state")

        code_verifier = d.pop("code_verifier")

        code_challenge = d.pop("code_challenge")

        code_challenge_method = d.pop("code_challenge_method")

        pkce_authorize_response = cls(
            url=url,
            state=state,
            code_verifier=code_verifier,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
        )

        pkce_authorize_response.additional_properties = d
        return pkce_authorize_response

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
