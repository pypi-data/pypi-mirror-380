"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import Unset


T = TypeVar("T", bound="AadharOtpVerificationRequestRequest")


@attr.s(auto_attribs=True)
class AadharOtpVerificationRequestRequest:
    """
    Attributes:
        signature (str):
        otp (str):
    """

    signature: str
    otp: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        signature = self.signature
        otp = self.otp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signature": signature,
                "otp": otp,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        signature = (
            self.signature
            if isinstance(self.signature, Unset)
            else (None, str(self.signature).encode(), "text/plain")
        )
        otp = (
            self.otp
            if isinstance(self.otp, Unset)
            else (None, str(self.otp).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value).encode(), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        field_dict.update(
            {
                "signature": signature,
                "otp": otp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        signature = d.pop("signature")

        otp = d.pop("otp")

        aadhar_otp_verification_request_request = cls(
            signature=signature,
            otp=otp,
        )

        aadhar_otp_verification_request_request.additional_properties = d
        return aadhar_otp_verification_request_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
