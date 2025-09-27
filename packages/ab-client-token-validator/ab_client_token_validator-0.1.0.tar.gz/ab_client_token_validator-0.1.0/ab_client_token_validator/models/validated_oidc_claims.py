from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidatedOIDCClaims")


@_attrs_define
class ValidatedOIDCClaims:
    """
    Attributes:
        iss (str):
        sub (str):
        aud (Union[list[str], str]):
        exp (int):
        iat (int):
        auth_time (int):
        acr (str):
        email (Union[None, Unset, str]):
        email_verified (Union[None, Unset, bool]):
        name (Union[None, Unset, str]):
        given_name (Union[None, Unset, str]):
        preferred_username (Union[None, Unset, str]):
        nickname (Union[None, Unset, str]):
        groups (Union[None, Unset, list[str]]):
    """

    iss: str
    sub: str
    aud: Union[list[str], str]
    exp: int
    iat: int
    auth_time: int
    acr: str
    email: Union[None, Unset, str] = UNSET
    email_verified: Union[None, Unset, bool] = UNSET
    name: Union[None, Unset, str] = UNSET
    given_name: Union[None, Unset, str] = UNSET
    preferred_username: Union[None, Unset, str] = UNSET
    nickname: Union[None, Unset, str] = UNSET
    groups: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iss = self.iss

        sub = self.sub

        aud: Union[list[str], str]
        if isinstance(self.aud, list):
            aud = self.aud

        else:
            aud = self.aud

        exp = self.exp

        iat = self.iat

        auth_time = self.auth_time

        acr = self.acr

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        email_verified: Union[None, Unset, bool]
        if isinstance(self.email_verified, Unset):
            email_verified = UNSET
        else:
            email_verified = self.email_verified

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        given_name: Union[None, Unset, str]
        if isinstance(self.given_name, Unset):
            given_name = UNSET
        else:
            given_name = self.given_name

        preferred_username: Union[None, Unset, str]
        if isinstance(self.preferred_username, Unset):
            preferred_username = UNSET
        else:
            preferred_username = self.preferred_username

        nickname: Union[None, Unset, str]
        if isinstance(self.nickname, Unset):
            nickname = UNSET
        else:
            nickname = self.nickname

        groups: Union[None, Unset, list[str]]
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = self.groups

        else:
            groups = self.groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iss": iss,
                "sub": sub,
                "aud": aud,
                "exp": exp,
                "iat": iat,
                "auth_time": auth_time,
                "acr": acr,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified
        if name is not UNSET:
            field_dict["name"] = name
        if given_name is not UNSET:
            field_dict["given_name"] = given_name
        if preferred_username is not UNSET:
            field_dict["preferred_username"] = preferred_username
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        iss = d.pop("iss")

        sub = d.pop("sub")

        def _parse_aud(data: object) -> Union[list[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aud_type_1 = cast(list[str], data)

                return aud_type_1
            except:  # noqa: E722
                pass
            return cast(Union[list[str], str], data)

        aud = _parse_aud(d.pop("aud"))

        exp = d.pop("exp")

        iat = d.pop("iat")

        auth_time = d.pop("auth_time")

        acr = d.pop("acr")

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_email_verified(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        email_verified = _parse_email_verified(d.pop("email_verified", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_given_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        given_name = _parse_given_name(d.pop("given_name", UNSET))

        def _parse_preferred_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preferred_username = _parse_preferred_username(d.pop("preferred_username", UNSET))

        def _parse_nickname(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nickname = _parse_nickname(d.pop("nickname", UNSET))

        def _parse_groups(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = cast(list[str], data)

                return groups_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        groups = _parse_groups(d.pop("groups", UNSET))

        validated_oidc_claims = cls(
            iss=iss,
            sub=sub,
            aud=aud,
            exp=exp,
            iat=iat,
            auth_time=auth_time,
            acr=acr,
            email=email,
            email_verified=email_verified,
            name=name,
            given_name=given_name,
            preferred_username=preferred_username,
            nickname=nickname,
            groups=groups,
        )

        validated_oidc_claims.additional_properties = d
        return validated_oidc_claims

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
