# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workspaces_web import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssociateBrowserSettingsRequest:
    boto3_raw_data: "type_defs.AssociateBrowserSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    browserSettingsArn = field("browserSettingsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateBrowserSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateBrowserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateDataProtectionSettingsRequest:
    boto3_raw_data: "type_defs.AssociateDataProtectionSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    dataProtectionSettingsArn = field("dataProtectionSettingsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateDataProtectionSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateDataProtectionSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateIpAccessSettingsRequest:
    boto3_raw_data: "type_defs.AssociateIpAccessSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    ipAccessSettingsArn = field("ipAccessSettingsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateIpAccessSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateIpAccessSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateNetworkSettingsRequest:
    boto3_raw_data: "type_defs.AssociateNetworkSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    networkSettingsArn = field("networkSettingsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateNetworkSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateNetworkSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSessionLoggerRequest:
    boto3_raw_data: "type_defs.AssociateSessionLoggerRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    sessionLoggerArn = field("sessionLoggerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateSessionLoggerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSessionLoggerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateTrustStoreRequest:
    boto3_raw_data: "type_defs.AssociateTrustStoreRequestTypeDef" = dataclasses.field()

    portalArn = field("portalArn")
    trustStoreArn = field("trustStoreArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateTrustStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateTrustStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateUserAccessLoggingSettingsRequest:
    boto3_raw_data: "type_defs.AssociateUserAccessLoggingSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    userAccessLoggingSettingsArn = field("userAccessLoggingSettingsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateUserAccessLoggingSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateUserAccessLoggingSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateUserSettingsRequest:
    boto3_raw_data: "type_defs.AssociateUserSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    userSettingsArn = field("userSettingsArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateUserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateUserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrowserSettingsSummary:
    boto3_raw_data: "type_defs.BrowserSettingsSummaryTypeDef" = dataclasses.field()

    browserSettingsArn = field("browserSettingsArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BrowserSettingsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrowserSettingsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrowserSettings:
    boto3_raw_data: "type_defs.BrowserSettingsTypeDef" = dataclasses.field()

    browserSettingsArn = field("browserSettingsArn")
    associatedPortalArns = field("associatedPortalArns")
    browserPolicy = field("browserPolicy")
    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BrowserSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BrowserSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateSummary:
    boto3_raw_data: "type_defs.CertificateSummaryTypeDef" = dataclasses.field()

    thumbprint = field("thumbprint")
    subject = field("subject")
    issuer = field("issuer")
    notValidBefore = field("notValidBefore")
    notValidAfter = field("notValidAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CertificateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Certificate:
    boto3_raw_data: "type_defs.CertificateTypeDef" = dataclasses.field()

    thumbprint = field("thumbprint")
    subject = field("subject")
    issuer = field("issuer")
    notValidBefore = field("notValidBefore")
    notValidAfter = field("notValidAfter")
    body = field("body")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CertificateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CookieSpecification:
    boto3_raw_data: "type_defs.CookieSpecificationTypeDef" = dataclasses.field()

    domain = field("domain")
    name = field("name")
    path = field("path")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CookieSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CookieSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpRule:
    boto3_raw_data: "type_defs.IpRuleTypeDef" = dataclasses.field()

    ipRange = field("ipRange")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomPattern:
    boto3_raw_data: "type_defs.CustomPatternTypeDef" = dataclasses.field()

    patternName = field("patternName")
    patternRegex = field("patternRegex")
    patternDescription = field("patternDescription")
    keywordRegex = field("keywordRegex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomPatternTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomPatternTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProtectionSettingsSummary:
    boto3_raw_data: "type_defs.DataProtectionSettingsSummaryTypeDef" = (
        dataclasses.field()
    )

    dataProtectionSettingsArn = field("dataProtectionSettingsArn")
    displayName = field("displayName")
    description = field("description")
    creationDate = field("creationDate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataProtectionSettingsSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProtectionSettingsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBrowserSettingsRequest:
    boto3_raw_data: "type_defs.DeleteBrowserSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    browserSettingsArn = field("browserSettingsArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBrowserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBrowserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataProtectionSettingsRequest:
    boto3_raw_data: "type_defs.DeleteDataProtectionSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    dataProtectionSettingsArn = field("dataProtectionSettingsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDataProtectionSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataProtectionSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdentityProviderRequest:
    boto3_raw_data: "type_defs.DeleteIdentityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    identityProviderArn = field("identityProviderArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteIdentityProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdentityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIpAccessSettingsRequest:
    boto3_raw_data: "type_defs.DeleteIpAccessSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    ipAccessSettingsArn = field("ipAccessSettingsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteIpAccessSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIpAccessSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNetworkSettingsRequest:
    boto3_raw_data: "type_defs.DeleteNetworkSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    networkSettingsArn = field("networkSettingsArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNetworkSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNetworkSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePortalRequest:
    boto3_raw_data: "type_defs.DeletePortalRequestTypeDef" = dataclasses.field()

    portalArn = field("portalArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePortalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePortalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSessionLoggerRequest:
    boto3_raw_data: "type_defs.DeleteSessionLoggerRequestTypeDef" = dataclasses.field()

    sessionLoggerArn = field("sessionLoggerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSessionLoggerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSessionLoggerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrustStoreRequest:
    boto3_raw_data: "type_defs.DeleteTrustStoreRequestTypeDef" = dataclasses.field()

    trustStoreArn = field("trustStoreArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTrustStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrustStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserAccessLoggingSettingsRequest:
    boto3_raw_data: "type_defs.DeleteUserAccessLoggingSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    userAccessLoggingSettingsArn = field("userAccessLoggingSettingsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteUserAccessLoggingSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserAccessLoggingSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserSettingsRequest:
    boto3_raw_data: "type_defs.DeleteUserSettingsRequestTypeDef" = dataclasses.field()

    userSettingsArn = field("userSettingsArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateBrowserSettingsRequest:
    boto3_raw_data: "type_defs.DisassociateBrowserSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateBrowserSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateBrowserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateDataProtectionSettingsRequest:
    boto3_raw_data: "type_defs.DisassociateDataProtectionSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateDataProtectionSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateDataProtectionSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateIpAccessSettingsRequest:
    boto3_raw_data: "type_defs.DisassociateIpAccessSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateIpAccessSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateIpAccessSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateNetworkSettingsRequest:
    boto3_raw_data: "type_defs.DisassociateNetworkSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateNetworkSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateNetworkSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateSessionLoggerRequest:
    boto3_raw_data: "type_defs.DisassociateSessionLoggerRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateSessionLoggerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateSessionLoggerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateTrustStoreRequest:
    boto3_raw_data: "type_defs.DisassociateTrustStoreRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateTrustStoreRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateTrustStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateUserAccessLoggingSettingsRequest:
    boto3_raw_data: "type_defs.DisassociateUserAccessLoggingSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateUserAccessLoggingSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateUserAccessLoggingSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateUserSettingsRequest:
    boto3_raw_data: "type_defs.DisassociateUserSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateUserSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateUserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventFilterOutput:
    boto3_raw_data: "type_defs.EventFilterOutputTypeDef" = dataclasses.field()

    all = field("all")
    include = field("include")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventFilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventFilter:
    boto3_raw_data: "type_defs.EventFilterTypeDef" = dataclasses.field()

    all = field("all")
    include = field("include")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpireSessionRequest:
    boto3_raw_data: "type_defs.ExpireSessionRequestTypeDef" = dataclasses.field()

    portalId = field("portalId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpireSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpireSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBrowserSettingsRequest:
    boto3_raw_data: "type_defs.GetBrowserSettingsRequestTypeDef" = dataclasses.field()

    browserSettingsArn = field("browserSettingsArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBrowserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBrowserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataProtectionSettingsRequest:
    boto3_raw_data: "type_defs.GetDataProtectionSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    dataProtectionSettingsArn = field("dataProtectionSettingsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataProtectionSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataProtectionSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityProviderRequest:
    boto3_raw_data: "type_defs.GetIdentityProviderRequestTypeDef" = dataclasses.field()

    identityProviderArn = field("identityProviderArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdentityProviderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityProvider:
    boto3_raw_data: "type_defs.IdentityProviderTypeDef" = dataclasses.field()

    identityProviderArn = field("identityProviderArn")
    identityProviderName = field("identityProviderName")
    identityProviderType = field("identityProviderType")
    identityProviderDetails = field("identityProviderDetails")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdentityProviderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIpAccessSettingsRequest:
    boto3_raw_data: "type_defs.GetIpAccessSettingsRequestTypeDef" = dataclasses.field()

    ipAccessSettingsArn = field("ipAccessSettingsArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIpAccessSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIpAccessSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkSettingsRequest:
    boto3_raw_data: "type_defs.GetNetworkSettingsRequestTypeDef" = dataclasses.field()

    networkSettingsArn = field("networkSettingsArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNetworkSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkSettings:
    boto3_raw_data: "type_defs.NetworkSettingsTypeDef" = dataclasses.field()

    networkSettingsArn = field("networkSettingsArn")
    associatedPortalArns = field("associatedPortalArns")
    vpcId = field("vpcId")
    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPortalRequest:
    boto3_raw_data: "type_defs.GetPortalRequestTypeDef" = dataclasses.field()

    portalArn = field("portalArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPortalRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPortalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Portal:
    boto3_raw_data: "type_defs.PortalTypeDef" = dataclasses.field()

    portalArn = field("portalArn")
    rendererType = field("rendererType")
    browserType = field("browserType")
    portalStatus = field("portalStatus")
    portalEndpoint = field("portalEndpoint")
    displayName = field("displayName")
    creationDate = field("creationDate")
    browserSettingsArn = field("browserSettingsArn")
    dataProtectionSettingsArn = field("dataProtectionSettingsArn")
    userSettingsArn = field("userSettingsArn")
    networkSettingsArn = field("networkSettingsArn")
    sessionLoggerArn = field("sessionLoggerArn")
    trustStoreArn = field("trustStoreArn")
    statusReason = field("statusReason")
    userAccessLoggingSettingsArn = field("userAccessLoggingSettingsArn")
    authenticationType = field("authenticationType")
    ipAccessSettingsArn = field("ipAccessSettingsArn")
    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")
    instanceType = field("instanceType")
    maxConcurrentSessions = field("maxConcurrentSessions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPortalServiceProviderMetadataRequest:
    boto3_raw_data: "type_defs.GetPortalServiceProviderMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPortalServiceProviderMetadataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPortalServiceProviderMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionLoggerRequest:
    boto3_raw_data: "type_defs.GetSessionLoggerRequestTypeDef" = dataclasses.field()

    sessionLoggerArn = field("sessionLoggerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionLoggerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionLoggerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionRequest:
    boto3_raw_data: "type_defs.GetSessionRequestTypeDef" = dataclasses.field()

    portalId = field("portalId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSessionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Session:
    boto3_raw_data: "type_defs.SessionTypeDef" = dataclasses.field()

    portalArn = field("portalArn")
    sessionId = field("sessionId")
    username = field("username")
    clientIpAddresses = field("clientIpAddresses")
    status = field("status")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrustStoreCertificateRequest:
    boto3_raw_data: "type_defs.GetTrustStoreCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    trustStoreArn = field("trustStoreArn")
    thumbprint = field("thumbprint")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTrustStoreCertificateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrustStoreCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrustStoreRequest:
    boto3_raw_data: "type_defs.GetTrustStoreRequestTypeDef" = dataclasses.field()

    trustStoreArn = field("trustStoreArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrustStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrustStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustStore:
    boto3_raw_data: "type_defs.TrustStoreTypeDef" = dataclasses.field()

    trustStoreArn = field("trustStoreArn")
    associatedPortalArns = field("associatedPortalArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrustStoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrustStoreTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserAccessLoggingSettingsRequest:
    boto3_raw_data: "type_defs.GetUserAccessLoggingSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    userAccessLoggingSettingsArn = field("userAccessLoggingSettingsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetUserAccessLoggingSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserAccessLoggingSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserAccessLoggingSettings:
    boto3_raw_data: "type_defs.UserAccessLoggingSettingsTypeDef" = dataclasses.field()

    userAccessLoggingSettingsArn = field("userAccessLoggingSettingsArn")
    associatedPortalArns = field("associatedPortalArns")
    kinesisStreamArn = field("kinesisStreamArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserAccessLoggingSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserAccessLoggingSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserSettingsRequest:
    boto3_raw_data: "type_defs.GetUserSettingsRequestTypeDef" = dataclasses.field()

    userSettingsArn = field("userSettingsArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityProviderSummary:
    boto3_raw_data: "type_defs.IdentityProviderSummaryTypeDef" = dataclasses.field()

    identityProviderArn = field("identityProviderArn")
    identityProviderName = field("identityProviderName")
    identityProviderType = field("identityProviderType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityProviderSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityProviderSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedactionPlaceHolder:
    boto3_raw_data: "type_defs.RedactionPlaceHolderTypeDef" = dataclasses.field()

    redactionPlaceHolderType = field("redactionPlaceHolderType")
    redactionPlaceHolderText = field("redactionPlaceHolderText")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedactionPlaceHolderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedactionPlaceHolderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpAccessSettingsSummary:
    boto3_raw_data: "type_defs.IpAccessSettingsSummaryTypeDef" = dataclasses.field()

    ipAccessSettingsArn = field("ipAccessSettingsArn")
    displayName = field("displayName")
    description = field("description")
    creationDate = field("creationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IpAccessSettingsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IpAccessSettingsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBrowserSettingsRequest:
    boto3_raw_data: "type_defs.ListBrowserSettingsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBrowserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBrowserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataProtectionSettingsRequest:
    boto3_raw_data: "type_defs.ListDataProtectionSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataProtectionSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataProtectionSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityProvidersRequest:
    boto3_raw_data: "type_defs.ListIdentityProvidersRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdentityProvidersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityProvidersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIpAccessSettingsRequest:
    boto3_raw_data: "type_defs.ListIpAccessSettingsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIpAccessSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIpAccessSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNetworkSettingsRequest:
    boto3_raw_data: "type_defs.ListNetworkSettingsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNetworkSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNetworkSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkSettingsSummary:
    boto3_raw_data: "type_defs.NetworkSettingsSummaryTypeDef" = dataclasses.field()

    networkSettingsArn = field("networkSettingsArn")
    vpcId = field("vpcId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkSettingsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkSettingsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortalsRequest:
    boto3_raw_data: "type_defs.ListPortalsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPortalsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortalsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortalSummary:
    boto3_raw_data: "type_defs.PortalSummaryTypeDef" = dataclasses.field()

    portalArn = field("portalArn")
    rendererType = field("rendererType")
    browserType = field("browserType")
    portalStatus = field("portalStatus")
    portalEndpoint = field("portalEndpoint")
    displayName = field("displayName")
    creationDate = field("creationDate")
    browserSettingsArn = field("browserSettingsArn")
    dataProtectionSettingsArn = field("dataProtectionSettingsArn")
    userSettingsArn = field("userSettingsArn")
    networkSettingsArn = field("networkSettingsArn")
    sessionLoggerArn = field("sessionLoggerArn")
    trustStoreArn = field("trustStoreArn")
    userAccessLoggingSettingsArn = field("userAccessLoggingSettingsArn")
    authenticationType = field("authenticationType")
    ipAccessSettingsArn = field("ipAccessSettingsArn")
    instanceType = field("instanceType")
    maxConcurrentSessions = field("maxConcurrentSessions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortalSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortalSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionLoggersRequest:
    boto3_raw_data: "type_defs.ListSessionLoggersRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionLoggersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionLoggersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsRequest:
    boto3_raw_data: "type_defs.ListSessionsRequestTypeDef" = dataclasses.field()

    portalId = field("portalId")
    username = field("username")
    sessionId = field("sessionId")
    sortBy = field("sortBy")
    status = field("status")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionSummary:
    boto3_raw_data: "type_defs.SessionSummaryTypeDef" = dataclasses.field()

    portalArn = field("portalArn")
    sessionId = field("sessionId")
    username = field("username")
    status = field("status")
    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrustStoreCertificatesRequest:
    boto3_raw_data: "type_defs.ListTrustStoreCertificatesRequestTypeDef" = (
        dataclasses.field()
    )

    trustStoreArn = field("trustStoreArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrustStoreCertificatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrustStoreCertificatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrustStoresRequest:
    boto3_raw_data: "type_defs.ListTrustStoresRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrustStoresRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrustStoresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustStoreSummary:
    boto3_raw_data: "type_defs.TrustStoreSummaryTypeDef" = dataclasses.field()

    trustStoreArn = field("trustStoreArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrustStoreSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustStoreSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserAccessLoggingSettingsRequest:
    boto3_raw_data: "type_defs.ListUserAccessLoggingSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUserAccessLoggingSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserAccessLoggingSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserAccessLoggingSettingsSummary:
    boto3_raw_data: "type_defs.UserAccessLoggingSettingsSummaryTypeDef" = (
        dataclasses.field()
    )

    userAccessLoggingSettingsArn = field("userAccessLoggingSettingsArn")
    kinesisStreamArn = field("kinesisStreamArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UserAccessLoggingSettingsSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserAccessLoggingSettingsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserSettingsRequest:
    boto3_raw_data: "type_defs.ListUserSettingsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3LogConfiguration:
    boto3_raw_data: "type_defs.S3LogConfigurationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    logFileFormat = field("logFileFormat")
    folderStructure = field("folderStructure")
    keyPrefix = field("keyPrefix")
    bucketOwner = field("bucketOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3LogConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3LogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolbarConfigurationOutput:
    boto3_raw_data: "type_defs.ToolbarConfigurationOutputTypeDef" = dataclasses.field()

    toolbarType = field("toolbarType")
    visualMode = field("visualMode")
    hiddenToolbarItems = field("hiddenToolbarItems")
    maxDisplayResolution = field("maxDisplayResolution")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToolbarConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolbarConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ToolbarConfiguration:
    boto3_raw_data: "type_defs.ToolbarConfigurationTypeDef" = dataclasses.field()

    toolbarType = field("toolbarType")
    visualMode = field("visualMode")
    hiddenToolbarItems = field("hiddenToolbarItems")
    maxDisplayResolution = field("maxDisplayResolution")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ToolbarConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ToolbarConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBrowserSettingsRequest:
    boto3_raw_data: "type_defs.UpdateBrowserSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    browserSettingsArn = field("browserSettingsArn")
    browserPolicy = field("browserPolicy")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBrowserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrowserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdentityProviderRequest:
    boto3_raw_data: "type_defs.UpdateIdentityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    identityProviderArn = field("identityProviderArn")
    identityProviderName = field("identityProviderName")
    identityProviderType = field("identityProviderType")
    identityProviderDetails = field("identityProviderDetails")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateIdentityProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdentityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNetworkSettingsRequest:
    boto3_raw_data: "type_defs.UpdateNetworkSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    networkSettingsArn = field("networkSettingsArn")
    vpcId = field("vpcId")
    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNetworkSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNetworkSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePortalRequest:
    boto3_raw_data: "type_defs.UpdatePortalRequestTypeDef" = dataclasses.field()

    portalArn = field("portalArn")
    displayName = field("displayName")
    authenticationType = field("authenticationType")
    instanceType = field("instanceType")
    maxConcurrentSessions = field("maxConcurrentSessions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePortalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePortalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserAccessLoggingSettingsRequest:
    boto3_raw_data: "type_defs.UpdateUserAccessLoggingSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    userAccessLoggingSettingsArn = field("userAccessLoggingSettingsArn")
    kinesisStreamArn = field("kinesisStreamArn")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateUserAccessLoggingSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserAccessLoggingSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateBrowserSettingsResponse:
    boto3_raw_data: "type_defs.AssociateBrowserSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    browserSettingsArn = field("browserSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateBrowserSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateBrowserSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateDataProtectionSettingsResponse:
    boto3_raw_data: "type_defs.AssociateDataProtectionSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    dataProtectionSettingsArn = field("dataProtectionSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateDataProtectionSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateDataProtectionSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateIpAccessSettingsResponse:
    boto3_raw_data: "type_defs.AssociateIpAccessSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    ipAccessSettingsArn = field("ipAccessSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateIpAccessSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateIpAccessSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateNetworkSettingsResponse:
    boto3_raw_data: "type_defs.AssociateNetworkSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    networkSettingsArn = field("networkSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateNetworkSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateNetworkSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateSessionLoggerResponse:
    boto3_raw_data: "type_defs.AssociateSessionLoggerResponseTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    sessionLoggerArn = field("sessionLoggerArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateSessionLoggerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateSessionLoggerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateTrustStoreResponse:
    boto3_raw_data: "type_defs.AssociateTrustStoreResponseTypeDef" = dataclasses.field()

    portalArn = field("portalArn")
    trustStoreArn = field("trustStoreArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateTrustStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateTrustStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateUserAccessLoggingSettingsResponse:
    boto3_raw_data: "type_defs.AssociateUserAccessLoggingSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    userAccessLoggingSettingsArn = field("userAccessLoggingSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateUserAccessLoggingSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateUserAccessLoggingSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateUserSettingsResponse:
    boto3_raw_data: "type_defs.AssociateUserSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    userSettingsArn = field("userSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateUserSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateUserSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBrowserSettingsResponse:
    boto3_raw_data: "type_defs.CreateBrowserSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    browserSettingsArn = field("browserSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBrowserSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBrowserSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataProtectionSettingsResponse:
    boto3_raw_data: "type_defs.CreateDataProtectionSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    dataProtectionSettingsArn = field("dataProtectionSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataProtectionSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataProtectionSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdentityProviderResponse:
    boto3_raw_data: "type_defs.CreateIdentityProviderResponseTypeDef" = (
        dataclasses.field()
    )

    identityProviderArn = field("identityProviderArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateIdentityProviderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdentityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIpAccessSettingsResponse:
    boto3_raw_data: "type_defs.CreateIpAccessSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    ipAccessSettingsArn = field("ipAccessSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateIpAccessSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIpAccessSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNetworkSettingsResponse:
    boto3_raw_data: "type_defs.CreateNetworkSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    networkSettingsArn = field("networkSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateNetworkSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNetworkSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePortalResponse:
    boto3_raw_data: "type_defs.CreatePortalResponseTypeDef" = dataclasses.field()

    portalArn = field("portalArn")
    portalEndpoint = field("portalEndpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePortalResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePortalResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSessionLoggerResponse:
    boto3_raw_data: "type_defs.CreateSessionLoggerResponseTypeDef" = dataclasses.field()

    sessionLoggerArn = field("sessionLoggerArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSessionLoggerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSessionLoggerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrustStoreResponse:
    boto3_raw_data: "type_defs.CreateTrustStoreResponseTypeDef" = dataclasses.field()

    trustStoreArn = field("trustStoreArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrustStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrustStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserAccessLoggingSettingsResponse:
    boto3_raw_data: "type_defs.CreateUserAccessLoggingSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    userAccessLoggingSettingsArn = field("userAccessLoggingSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateUserAccessLoggingSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserAccessLoggingSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserSettingsResponse:
    boto3_raw_data: "type_defs.CreateUserSettingsResponseTypeDef" = dataclasses.field()

    userSettingsArn = field("userSettingsArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPortalServiceProviderMetadataResponse:
    boto3_raw_data: "type_defs.GetPortalServiceProviderMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    serviceProviderSamlMetadata = field("serviceProviderSamlMetadata")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPortalServiceProviderMetadataResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPortalServiceProviderMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrustStoreResponse:
    boto3_raw_data: "type_defs.UpdateTrustStoreResponseTypeDef" = dataclasses.field()

    trustStoreArn = field("trustStoreArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTrustStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrustStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrustStoreRequest:
    boto3_raw_data: "type_defs.UpdateTrustStoreRequestTypeDef" = dataclasses.field()

    trustStoreArn = field("trustStoreArn")
    certificatesToAdd = field("certificatesToAdd")
    certificatesToDelete = field("certificatesToDelete")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTrustStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrustStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBrowserSettingsResponse:
    boto3_raw_data: "type_defs.ListBrowserSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def browserSettings(self):  # pragma: no cover
        return BrowserSettingsSummary.make_many(self.boto3_raw_data["browserSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBrowserSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBrowserSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBrowserSettingsResponse:
    boto3_raw_data: "type_defs.GetBrowserSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def browserSettings(self):  # pragma: no cover
        return BrowserSettings.make_one(self.boto3_raw_data["browserSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBrowserSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBrowserSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBrowserSettingsResponse:
    boto3_raw_data: "type_defs.UpdateBrowserSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def browserSettings(self):  # pragma: no cover
        return BrowserSettings.make_one(self.boto3_raw_data["browserSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateBrowserSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrowserSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrustStoreCertificatesResponse:
    boto3_raw_data: "type_defs.ListTrustStoreCertificatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def certificateList(self):  # pragma: no cover
        return CertificateSummary.make_many(self.boto3_raw_data["certificateList"])

    trustStoreArn = field("trustStoreArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrustStoreCertificatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrustStoreCertificatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrustStoreCertificateResponse:
    boto3_raw_data: "type_defs.GetTrustStoreCertificateResponseTypeDef" = (
        dataclasses.field()
    )

    trustStoreArn = field("trustStoreArn")

    @cached_property
    def certificate(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["certificate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTrustStoreCertificateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrustStoreCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CookieSynchronizationConfigurationOutput:
    boto3_raw_data: "type_defs.CookieSynchronizationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def allowlist(self):  # pragma: no cover
        return CookieSpecification.make_many(self.boto3_raw_data["allowlist"])

    @cached_property
    def blocklist(self):  # pragma: no cover
        return CookieSpecification.make_many(self.boto3_raw_data["blocklist"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CookieSynchronizationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CookieSynchronizationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CookieSynchronizationConfiguration:
    boto3_raw_data: "type_defs.CookieSynchronizationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def allowlist(self):  # pragma: no cover
        return CookieSpecification.make_many(self.boto3_raw_data["allowlist"])

    @cached_property
    def blocklist(self):  # pragma: no cover
        return CookieSpecification.make_many(self.boto3_raw_data["blocklist"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CookieSynchronizationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CookieSynchronizationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBrowserSettingsRequest:
    boto3_raw_data: "type_defs.CreateBrowserSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    browserPolicy = field("browserPolicy")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBrowserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBrowserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdentityProviderRequest:
    boto3_raw_data: "type_defs.CreateIdentityProviderRequestTypeDef" = (
        dataclasses.field()
    )

    portalArn = field("portalArn")
    identityProviderName = field("identityProviderName")
    identityProviderType = field("identityProviderType")
    identityProviderDetails = field("identityProviderDetails")
    clientToken = field("clientToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateIdentityProviderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdentityProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNetworkSettingsRequest:
    boto3_raw_data: "type_defs.CreateNetworkSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    vpcId = field("vpcId")
    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNetworkSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNetworkSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePortalRequest:
    boto3_raw_data: "type_defs.CreatePortalRequestTypeDef" = dataclasses.field()

    displayName = field("displayName")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")
    clientToken = field("clientToken")
    authenticationType = field("authenticationType")
    instanceType = field("instanceType")
    maxConcurrentSessions = field("maxConcurrentSessions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePortalRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePortalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrustStoreRequest:
    boto3_raw_data: "type_defs.CreateTrustStoreRequestTypeDef" = dataclasses.field()

    certificateList = field("certificateList")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrustStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrustStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserAccessLoggingSettingsRequest:
    boto3_raw_data: "type_defs.CreateUserAccessLoggingSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    kinesisStreamArn = field("kinesisStreamArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateUserAccessLoggingSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserAccessLoggingSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIpAccessSettingsRequest:
    boto3_raw_data: "type_defs.CreateIpAccessSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ipRules(self):  # pragma: no cover
        return IpRule.make_many(self.boto3_raw_data["ipRules"])

    displayName = field("displayName")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateIpAccessSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIpAccessSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpAccessSettings:
    boto3_raw_data: "type_defs.IpAccessSettingsTypeDef" = dataclasses.field()

    ipAccessSettingsArn = field("ipAccessSettingsArn")
    associatedPortalArns = field("associatedPortalArns")

    @cached_property
    def ipRules(self):  # pragma: no cover
        return IpRule.make_many(self.boto3_raw_data["ipRules"])

    displayName = field("displayName")
    description = field("description")
    creationDate = field("creationDate")
    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpAccessSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IpAccessSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIpAccessSettingsRequest:
    boto3_raw_data: "type_defs.UpdateIpAccessSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    ipAccessSettingsArn = field("ipAccessSettingsArn")
    displayName = field("displayName")
    description = field("description")

    @cached_property
    def ipRules(self):  # pragma: no cover
        return IpRule.make_many(self.boto3_raw_data["ipRules"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateIpAccessSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIpAccessSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataProtectionSettingsResponse:
    boto3_raw_data: "type_defs.ListDataProtectionSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataProtectionSettings(self):  # pragma: no cover
        return DataProtectionSettingsSummary.make_many(
            self.boto3_raw_data["dataProtectionSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataProtectionSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataProtectionSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityProviderResponse:
    boto3_raw_data: "type_defs.GetIdentityProviderResponseTypeDef" = dataclasses.field()

    @cached_property
    def identityProvider(self):  # pragma: no cover
        return IdentityProvider.make_one(self.boto3_raw_data["identityProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdentityProviderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdentityProviderResponse:
    boto3_raw_data: "type_defs.UpdateIdentityProviderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def identityProvider(self):  # pragma: no cover
        return IdentityProvider.make_one(self.boto3_raw_data["identityProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateIdentityProviderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdentityProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkSettingsResponse:
    boto3_raw_data: "type_defs.GetNetworkSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def networkSettings(self):  # pragma: no cover
        return NetworkSettings.make_one(self.boto3_raw_data["networkSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNetworkSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNetworkSettingsResponse:
    boto3_raw_data: "type_defs.UpdateNetworkSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def networkSettings(self):  # pragma: no cover
        return NetworkSettings.make_one(self.boto3_raw_data["networkSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateNetworkSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNetworkSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPortalResponse:
    boto3_raw_data: "type_defs.GetPortalResponseTypeDef" = dataclasses.field()

    @cached_property
    def portal(self):  # pragma: no cover
        return Portal.make_one(self.boto3_raw_data["portal"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPortalResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPortalResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePortalResponse:
    boto3_raw_data: "type_defs.UpdatePortalResponseTypeDef" = dataclasses.field()

    @cached_property
    def portal(self):  # pragma: no cover
        return Portal.make_one(self.boto3_raw_data["portal"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePortalResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePortalResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionResponse:
    boto3_raw_data: "type_defs.GetSessionResponseTypeDef" = dataclasses.field()

    @cached_property
    def session(self):  # pragma: no cover
        return Session.make_one(self.boto3_raw_data["session"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrustStoreResponse:
    boto3_raw_data: "type_defs.GetTrustStoreResponseTypeDef" = dataclasses.field()

    @cached_property
    def trustStore(self):  # pragma: no cover
        return TrustStore.make_one(self.boto3_raw_data["trustStore"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrustStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrustStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserAccessLoggingSettingsResponse:
    boto3_raw_data: "type_defs.GetUserAccessLoggingSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def userAccessLoggingSettings(self):  # pragma: no cover
        return UserAccessLoggingSettings.make_one(
            self.boto3_raw_data["userAccessLoggingSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetUserAccessLoggingSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserAccessLoggingSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserAccessLoggingSettingsResponse:
    boto3_raw_data: "type_defs.UpdateUserAccessLoggingSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def userAccessLoggingSettings(self):  # pragma: no cover
        return UserAccessLoggingSettings.make_one(
            self.boto3_raw_data["userAccessLoggingSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateUserAccessLoggingSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserAccessLoggingSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityProvidersResponse:
    boto3_raw_data: "type_defs.ListIdentityProvidersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def identityProviders(self):  # pragma: no cover
        return IdentityProviderSummary.make_many(
            self.boto3_raw_data["identityProviders"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIdentityProvidersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineRedactionPatternOutput:
    boto3_raw_data: "type_defs.InlineRedactionPatternOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def redactionPlaceHolder(self):  # pragma: no cover
        return RedactionPlaceHolder.make_one(
            self.boto3_raw_data["redactionPlaceHolder"]
        )

    builtInPatternId = field("builtInPatternId")

    @cached_property
    def customPattern(self):  # pragma: no cover
        return CustomPattern.make_one(self.boto3_raw_data["customPattern"])

    enforcedUrls = field("enforcedUrls")
    exemptUrls = field("exemptUrls")
    confidenceLevel = field("confidenceLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InlineRedactionPatternOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineRedactionPatternOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineRedactionPattern:
    boto3_raw_data: "type_defs.InlineRedactionPatternTypeDef" = dataclasses.field()

    @cached_property
    def redactionPlaceHolder(self):  # pragma: no cover
        return RedactionPlaceHolder.make_one(
            self.boto3_raw_data["redactionPlaceHolder"]
        )

    builtInPatternId = field("builtInPatternId")

    @cached_property
    def customPattern(self):  # pragma: no cover
        return CustomPattern.make_one(self.boto3_raw_data["customPattern"])

    enforcedUrls = field("enforcedUrls")
    exemptUrls = field("exemptUrls")
    confidenceLevel = field("confidenceLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InlineRedactionPatternTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineRedactionPatternTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIpAccessSettingsResponse:
    boto3_raw_data: "type_defs.ListIpAccessSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ipAccessSettings(self):  # pragma: no cover
        return IpAccessSettingsSummary.make_many(
            self.boto3_raw_data["ipAccessSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIpAccessSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIpAccessSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataProtectionSettingsRequestPaginate:
    boto3_raw_data: "type_defs.ListDataProtectionSettingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataProtectionSettingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataProtectionSettingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionLoggersRequestPaginate:
    boto3_raw_data: "type_defs.ListSessionLoggersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSessionLoggersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionLoggersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSessionsRequestPaginateTypeDef" = dataclasses.field()

    portalId = field("portalId")
    username = field("username")
    sessionId = field("sessionId")
    sortBy = field("sortBy")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNetworkSettingsResponse:
    boto3_raw_data: "type_defs.ListNetworkSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def networkSettings(self):  # pragma: no cover
        return NetworkSettingsSummary.make_many(self.boto3_raw_data["networkSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNetworkSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNetworkSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPortalsResponse:
    boto3_raw_data: "type_defs.ListPortalsResponseTypeDef" = dataclasses.field()

    @cached_property
    def portals(self):  # pragma: no cover
        return PortalSummary.make_many(self.boto3_raw_data["portals"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPortalsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPortalsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionsResponse:
    boto3_raw_data: "type_defs.ListSessionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def sessions(self):  # pragma: no cover
        return SessionSummary.make_many(self.boto3_raw_data["sessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrustStoresResponse:
    boto3_raw_data: "type_defs.ListTrustStoresResponseTypeDef" = dataclasses.field()

    @cached_property
    def trustStores(self):  # pragma: no cover
        return TrustStoreSummary.make_many(self.boto3_raw_data["trustStores"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrustStoresResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrustStoresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserAccessLoggingSettingsResponse:
    boto3_raw_data: "type_defs.ListUserAccessLoggingSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def userAccessLoggingSettings(self):  # pragma: no cover
        return UserAccessLoggingSettingsSummary.make_many(
            self.boto3_raw_data["userAccessLoggingSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUserAccessLoggingSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserAccessLoggingSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogConfiguration:
    boto3_raw_data: "type_defs.LogConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return S3LogConfiguration.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSettingsSummary:
    boto3_raw_data: "type_defs.UserSettingsSummaryTypeDef" = dataclasses.field()

    userSettingsArn = field("userSettingsArn")
    copyAllowed = field("copyAllowed")
    pasteAllowed = field("pasteAllowed")
    downloadAllowed = field("downloadAllowed")
    uploadAllowed = field("uploadAllowed")
    printAllowed = field("printAllowed")
    disconnectTimeoutInMinutes = field("disconnectTimeoutInMinutes")
    idleDisconnectTimeoutInMinutes = field("idleDisconnectTimeoutInMinutes")

    @cached_property
    def cookieSynchronizationConfiguration(self):  # pragma: no cover
        return CookieSynchronizationConfigurationOutput.make_one(
            self.boto3_raw_data["cookieSynchronizationConfiguration"]
        )

    deepLinkAllowed = field("deepLinkAllowed")

    @cached_property
    def toolbarConfiguration(self):  # pragma: no cover
        return ToolbarConfigurationOutput.make_one(
            self.boto3_raw_data["toolbarConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserSettingsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserSettingsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSettings:
    boto3_raw_data: "type_defs.UserSettingsTypeDef" = dataclasses.field()

    userSettingsArn = field("userSettingsArn")
    associatedPortalArns = field("associatedPortalArns")
    copyAllowed = field("copyAllowed")
    pasteAllowed = field("pasteAllowed")
    downloadAllowed = field("downloadAllowed")
    uploadAllowed = field("uploadAllowed")
    printAllowed = field("printAllowed")
    disconnectTimeoutInMinutes = field("disconnectTimeoutInMinutes")
    idleDisconnectTimeoutInMinutes = field("idleDisconnectTimeoutInMinutes")

    @cached_property
    def cookieSynchronizationConfiguration(self):  # pragma: no cover
        return CookieSynchronizationConfigurationOutput.make_one(
            self.boto3_raw_data["cookieSynchronizationConfiguration"]
        )

    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")
    deepLinkAllowed = field("deepLinkAllowed")

    @cached_property
    def toolbarConfiguration(self):  # pragma: no cover
        return ToolbarConfigurationOutput.make_one(
            self.boto3_raw_data["toolbarConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIpAccessSettingsResponse:
    boto3_raw_data: "type_defs.GetIpAccessSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ipAccessSettings(self):  # pragma: no cover
        return IpAccessSettings.make_one(self.boto3_raw_data["ipAccessSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIpAccessSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIpAccessSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIpAccessSettingsResponse:
    boto3_raw_data: "type_defs.UpdateIpAccessSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ipAccessSettings(self):  # pragma: no cover
        return IpAccessSettings.make_one(self.boto3_raw_data["ipAccessSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateIpAccessSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIpAccessSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineRedactionConfigurationOutput:
    boto3_raw_data: "type_defs.InlineRedactionConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def inlineRedactionPatterns(self):  # pragma: no cover
        return InlineRedactionPatternOutput.make_many(
            self.boto3_raw_data["inlineRedactionPatterns"]
        )

    globalEnforcedUrls = field("globalEnforcedUrls")
    globalExemptUrls = field("globalExemptUrls")
    globalConfidenceLevel = field("globalConfidenceLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InlineRedactionConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineRedactionConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InlineRedactionConfiguration:
    boto3_raw_data: "type_defs.InlineRedactionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def inlineRedactionPatterns(self):  # pragma: no cover
        return InlineRedactionPattern.make_many(
            self.boto3_raw_data["inlineRedactionPatterns"]
        )

    globalEnforcedUrls = field("globalEnforcedUrls")
    globalExemptUrls = field("globalExemptUrls")
    globalConfidenceLevel = field("globalConfidenceLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InlineRedactionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InlineRedactionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSessionLoggerRequest:
    boto3_raw_data: "type_defs.CreateSessionLoggerRequestTypeDef" = dataclasses.field()

    eventFilter = field("eventFilter")

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["logConfiguration"])

    displayName = field("displayName")
    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSessionLoggerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSessionLoggerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionLoggerSummary:
    boto3_raw_data: "type_defs.SessionLoggerSummaryTypeDef" = dataclasses.field()

    sessionLoggerArn = field("sessionLoggerArn")

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["logConfiguration"])

    displayName = field("displayName")
    creationDate = field("creationDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionLoggerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionLoggerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionLogger:
    boto3_raw_data: "type_defs.SessionLoggerTypeDef" = dataclasses.field()

    sessionLoggerArn = field("sessionLoggerArn")

    @cached_property
    def eventFilter(self):  # pragma: no cover
        return EventFilterOutput.make_one(self.boto3_raw_data["eventFilter"])

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["logConfiguration"])

    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")
    associatedPortalArns = field("associatedPortalArns")
    displayName = field("displayName")
    creationDate = field("creationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionLoggerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionLoggerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSessionLoggerRequest:
    boto3_raw_data: "type_defs.UpdateSessionLoggerRequestTypeDef" = dataclasses.field()

    sessionLoggerArn = field("sessionLoggerArn")
    eventFilter = field("eventFilter")

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return LogConfiguration.make_one(self.boto3_raw_data["logConfiguration"])

    displayName = field("displayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSessionLoggerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSessionLoggerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUserSettingsResponse:
    boto3_raw_data: "type_defs.ListUserSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def userSettings(self):  # pragma: no cover
        return UserSettingsSummary.make_many(self.boto3_raw_data["userSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUserSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUserSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserSettingsResponse:
    boto3_raw_data: "type_defs.GetUserSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def userSettings(self):  # pragma: no cover
        return UserSettings.make_one(self.boto3_raw_data["userSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserSettingsResponse:
    boto3_raw_data: "type_defs.UpdateUserSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def userSettings(self):  # pragma: no cover
        return UserSettings.make_one(self.boto3_raw_data["userSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserSettingsRequest:
    boto3_raw_data: "type_defs.CreateUserSettingsRequestTypeDef" = dataclasses.field()

    copyAllowed = field("copyAllowed")
    pasteAllowed = field("pasteAllowed")
    downloadAllowed = field("downloadAllowed")
    uploadAllowed = field("uploadAllowed")
    printAllowed = field("printAllowed")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    disconnectTimeoutInMinutes = field("disconnectTimeoutInMinutes")
    idleDisconnectTimeoutInMinutes = field("idleDisconnectTimeoutInMinutes")
    clientToken = field("clientToken")
    cookieSynchronizationConfiguration = field("cookieSynchronizationConfiguration")
    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")
    deepLinkAllowed = field("deepLinkAllowed")
    toolbarConfiguration = field("toolbarConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserSettingsRequest:
    boto3_raw_data: "type_defs.UpdateUserSettingsRequestTypeDef" = dataclasses.field()

    userSettingsArn = field("userSettingsArn")
    copyAllowed = field("copyAllowed")
    pasteAllowed = field("pasteAllowed")
    downloadAllowed = field("downloadAllowed")
    uploadAllowed = field("uploadAllowed")
    printAllowed = field("printAllowed")
    disconnectTimeoutInMinutes = field("disconnectTimeoutInMinutes")
    idleDisconnectTimeoutInMinutes = field("idleDisconnectTimeoutInMinutes")
    clientToken = field("clientToken")
    cookieSynchronizationConfiguration = field("cookieSynchronizationConfiguration")
    deepLinkAllowed = field("deepLinkAllowed")
    toolbarConfiguration = field("toolbarConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProtectionSettings:
    boto3_raw_data: "type_defs.DataProtectionSettingsTypeDef" = dataclasses.field()

    dataProtectionSettingsArn = field("dataProtectionSettingsArn")

    @cached_property
    def inlineRedactionConfiguration(self):  # pragma: no cover
        return InlineRedactionConfigurationOutput.make_one(
            self.boto3_raw_data["inlineRedactionConfiguration"]
        )

    associatedPortalArns = field("associatedPortalArns")
    displayName = field("displayName")
    description = field("description")
    creationDate = field("creationDate")
    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProtectionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProtectionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionLoggersResponse:
    boto3_raw_data: "type_defs.ListSessionLoggersResponseTypeDef" = dataclasses.field()

    @cached_property
    def sessionLoggers(self):  # pragma: no cover
        return SessionLoggerSummary.make_many(self.boto3_raw_data["sessionLoggers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionLoggersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionLoggersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionLoggerResponse:
    boto3_raw_data: "type_defs.GetSessionLoggerResponseTypeDef" = dataclasses.field()

    @cached_property
    def sessionLogger(self):  # pragma: no cover
        return SessionLogger.make_one(self.boto3_raw_data["sessionLogger"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionLoggerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionLoggerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSessionLoggerResponse:
    boto3_raw_data: "type_defs.UpdateSessionLoggerResponseTypeDef" = dataclasses.field()

    @cached_property
    def sessionLogger(self):  # pragma: no cover
        return SessionLogger.make_one(self.boto3_raw_data["sessionLogger"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSessionLoggerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSessionLoggerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataProtectionSettingsResponse:
    boto3_raw_data: "type_defs.GetDataProtectionSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataProtectionSettings(self):  # pragma: no cover
        return DataProtectionSettings.make_one(
            self.boto3_raw_data["dataProtectionSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDataProtectionSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataProtectionSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataProtectionSettingsResponse:
    boto3_raw_data: "type_defs.UpdateDataProtectionSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataProtectionSettings(self):  # pragma: no cover
        return DataProtectionSettings.make_one(
            self.boto3_raw_data["dataProtectionSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDataProtectionSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataProtectionSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataProtectionSettingsRequest:
    boto3_raw_data: "type_defs.CreateDataProtectionSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    displayName = field("displayName")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    customerManagedKey = field("customerManagedKey")
    additionalEncryptionContext = field("additionalEncryptionContext")
    inlineRedactionConfiguration = field("inlineRedactionConfiguration")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDataProtectionSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataProtectionSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataProtectionSettingsRequest:
    boto3_raw_data: "type_defs.UpdateDataProtectionSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    dataProtectionSettingsArn = field("dataProtectionSettingsArn")
    inlineRedactionConfiguration = field("inlineRedactionConfiguration")
    displayName = field("displayName")
    description = field("description")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDataProtectionSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataProtectionSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
