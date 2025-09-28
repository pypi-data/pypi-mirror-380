# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_rolesanywhere import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class MappingRule:
    boto3_raw_data: "type_defs.MappingRuleTypeDef" = dataclasses.field()

    specifier = field("specifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MappingRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MappingRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

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
class NotificationSetting:
    boto3_raw_data: "type_defs.NotificationSettingTypeDef" = dataclasses.field()

    enabled = field("enabled")
    event = field("event")
    channel = field("channel")
    threshold = field("threshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CredentialSummary:
    boto3_raw_data: "type_defs.CredentialSummaryTypeDef" = dataclasses.field()

    enabled = field("enabled")
    failed = field("failed")
    issuer = field("issuer")
    seenAt = field("seenAt")
    serialNumber = field("serialNumber")
    x509CertificateData = field("x509CertificateData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CredentialSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CredentialSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrlDetail:
    boto3_raw_data: "type_defs.CrlDetailTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    crlArn = field("crlArn")
    crlData = field("crlData")
    crlId = field("crlId")
    enabled = field("enabled")
    name = field("name")
    trustAnchorArn = field("trustAnchorArn")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CrlDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CrlDetailTypeDef"]]
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
class DeleteAttributeMappingRequest:
    boto3_raw_data: "type_defs.DeleteAttributeMappingRequestTypeDef" = (
        dataclasses.field()
    )

    certificateField = field("certificateField")
    profileId = field("profileId")
    specifiers = field("specifiers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAttributeMappingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAttributeMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceProperty:
    boto3_raw_data: "type_defs.InstancePropertyTypeDef" = dataclasses.field()

    failed = field("failed")
    properties = field("properties")
    seenAt = field("seenAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstancePropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstancePropertyTypeDef"]
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
class ListRequestRequestExtraExtra:
    boto3_raw_data: "type_defs.ListRequestRequestExtraExtraTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    pageSize = field("pageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRequestRequestExtraExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRequestRequestExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestRequestExtra:
    boto3_raw_data: "type_defs.ListRequestRequestExtraTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    pageSize = field("pageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRequestRequestExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRequestRequestExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestRequest:
    boto3_raw_data: "type_defs.ListRequestRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    pageSize = field("pageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRequestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRequestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequest:
    boto3_raw_data: "type_defs.ListRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    pageSize = field("pageSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListRequestTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubjectSummary:
    boto3_raw_data: "type_defs.SubjectSummaryTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    enabled = field("enabled")
    lastSeenAt = field("lastSeenAt")
    subjectArn = field("subjectArn")
    subjectId = field("subjectId")
    updatedAt = field("updatedAt")
    x509Subject = field("x509Subject")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubjectSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubjectSummaryTypeDef"]],
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
class NotificationSettingDetail:
    boto3_raw_data: "type_defs.NotificationSettingDetailTypeDef" = dataclasses.field()

    enabled = field("enabled")
    event = field("event")
    channel = field("channel")
    configuredBy = field("configuredBy")
    threshold = field("threshold")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationSettingDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationSettingDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationSettingKey:
    boto3_raw_data: "type_defs.NotificationSettingKeyTypeDef" = dataclasses.field()

    event = field("event")
    channel = field("channel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationSettingKeyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationSettingKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarCrlRequestRequestExtraExtra:
    boto3_raw_data: "type_defs.ScalarCrlRequestRequestExtraExtraTypeDef" = (
        dataclasses.field()
    )

    crlId = field("crlId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScalarCrlRequestRequestExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarCrlRequestRequestExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarCrlRequestRequestExtra:
    boto3_raw_data: "type_defs.ScalarCrlRequestRequestExtraTypeDef" = (
        dataclasses.field()
    )

    crlId = field("crlId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalarCrlRequestRequestExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarCrlRequestRequestExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarCrlRequestRequest:
    boto3_raw_data: "type_defs.ScalarCrlRequestRequestTypeDef" = dataclasses.field()

    crlId = field("crlId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalarCrlRequestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarCrlRequestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarCrlRequest:
    boto3_raw_data: "type_defs.ScalarCrlRequestTypeDef" = dataclasses.field()

    crlId = field("crlId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalarCrlRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarCrlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarProfileRequestRequestExtraExtra:
    boto3_raw_data: "type_defs.ScalarProfileRequestRequestExtraExtraTypeDef" = (
        dataclasses.field()
    )

    profileId = field("profileId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScalarProfileRequestRequestExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarProfileRequestRequestExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarProfileRequestRequestExtra:
    boto3_raw_data: "type_defs.ScalarProfileRequestRequestExtraTypeDef" = (
        dataclasses.field()
    )

    profileId = field("profileId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ScalarProfileRequestRequestExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarProfileRequestRequestExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarProfileRequestRequest:
    boto3_raw_data: "type_defs.ScalarProfileRequestRequestTypeDef" = dataclasses.field()

    profileId = field("profileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalarProfileRequestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarProfileRequestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarProfileRequest:
    boto3_raw_data: "type_defs.ScalarProfileRequestTypeDef" = dataclasses.field()

    profileId = field("profileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalarProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarSubjectRequest:
    boto3_raw_data: "type_defs.ScalarSubjectRequestTypeDef" = dataclasses.field()

    subjectId = field("subjectId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalarSubjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarSubjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarTrustAnchorRequestRequestExtraExtra:
    boto3_raw_data: "type_defs.ScalarTrustAnchorRequestRequestExtraExtraTypeDef" = (
        dataclasses.field()
    )

    trustAnchorId = field("trustAnchorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScalarTrustAnchorRequestRequestExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarTrustAnchorRequestRequestExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarTrustAnchorRequestRequestExtra:
    boto3_raw_data: "type_defs.ScalarTrustAnchorRequestRequestExtraTypeDef" = (
        dataclasses.field()
    )

    trustAnchorId = field("trustAnchorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScalarTrustAnchorRequestRequestExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarTrustAnchorRequestRequestExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarTrustAnchorRequestRequest:
    boto3_raw_data: "type_defs.ScalarTrustAnchorRequestRequestTypeDef" = (
        dataclasses.field()
    )

    trustAnchorId = field("trustAnchorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ScalarTrustAnchorRequestRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarTrustAnchorRequestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalarTrustAnchorRequest:
    boto3_raw_data: "type_defs.ScalarTrustAnchorRequestTypeDef" = dataclasses.field()

    trustAnchorId = field("trustAnchorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalarTrustAnchorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalarTrustAnchorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceData:
    boto3_raw_data: "type_defs.SourceDataTypeDef" = dataclasses.field()

    acmPcaArn = field("acmPcaArn")
    x509CertificateData = field("x509CertificateData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceDataTypeDef"]]
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
class UpdateProfileRequest:
    boto3_raw_data: "type_defs.UpdateProfileRequestTypeDef" = dataclasses.field()

    profileId = field("profileId")
    acceptRoleSessionName = field("acceptRoleSessionName")
    durationSeconds = field("durationSeconds")
    managedPolicyArns = field("managedPolicyArns")
    name = field("name")
    roleArns = field("roleArns")
    sessionPolicy = field("sessionPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeMapping:
    boto3_raw_data: "type_defs.AttributeMappingTypeDef" = dataclasses.field()

    certificateField = field("certificateField")

    @cached_property
    def mappingRules(self):  # pragma: no cover
        return MappingRule.make_many(self.boto3_raw_data["mappingRules"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeMappingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAttributeMappingRequest:
    boto3_raw_data: "type_defs.PutAttributeMappingRequestTypeDef" = dataclasses.field()

    certificateField = field("certificateField")

    @cached_property
    def mappingRules(self):  # pragma: no cover
        return MappingRule.make_many(self.boto3_raw_data["mappingRules"])

    profileId = field("profileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAttributeMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAttributeMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCrlRequest:
    boto3_raw_data: "type_defs.UpdateCrlRequestTypeDef" = dataclasses.field()

    crlId = field("crlId")
    crlData = field("crlData")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateCrlRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCrlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfileRequest:
    boto3_raw_data: "type_defs.CreateProfileRequestTypeDef" = dataclasses.field()

    name = field("name")
    roleArns = field("roleArns")
    acceptRoleSessionName = field("acceptRoleSessionName")
    durationSeconds = field("durationSeconds")
    enabled = field("enabled")
    managedPolicyArns = field("managedPolicyArns")
    requireInstanceProperties = field("requireInstanceProperties")
    sessionPolicy = field("sessionPolicy")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportCrlRequest:
    boto3_raw_data: "type_defs.ImportCrlRequestTypeDef" = dataclasses.field()

    crlData = field("crlData")
    name = field("name")
    trustAnchorArn = field("trustAnchorArn")
    enabled = field("enabled")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportCrlRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportCrlRequestTypeDef"]
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
class PutNotificationSettingsRequest:
    boto3_raw_data: "type_defs.PutNotificationSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def notificationSettings(self):  # pragma: no cover
        return NotificationSetting.make_many(
            self.boto3_raw_data["notificationSettings"]
        )

    trustAnchorId = field("trustAnchorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutNotificationSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutNotificationSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrlDetailResponse:
    boto3_raw_data: "type_defs.CrlDetailResponseTypeDef" = dataclasses.field()

    @cached_property
    def crl(self):  # pragma: no cover
        return CrlDetail.make_one(self.boto3_raw_data["crl"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CrlDetailResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrlDetailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCrlsResponse:
    boto3_raw_data: "type_defs.ListCrlsResponseTypeDef" = dataclasses.field()

    @cached_property
    def crls(self):  # pragma: no cover
        return CrlDetail.make_many(self.boto3_raw_data["crls"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListCrlsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCrlsResponseTypeDef"]
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
class SubjectDetail:
    boto3_raw_data: "type_defs.SubjectDetailTypeDef" = dataclasses.field()

    createdAt = field("createdAt")

    @cached_property
    def credentials(self):  # pragma: no cover
        return CredentialSummary.make_many(self.boto3_raw_data["credentials"])

    enabled = field("enabled")

    @cached_property
    def instanceProperties(self):  # pragma: no cover
        return InstanceProperty.make_many(self.boto3_raw_data["instanceProperties"])

    lastSeenAt = field("lastSeenAt")
    subjectArn = field("subjectArn")
    subjectId = field("subjectId")
    updatedAt = field("updatedAt")
    x509Subject = field("x509Subject")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubjectDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubjectDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestPaginateExtraExtraExtra:
    boto3_raw_data: "type_defs.ListRequestPaginateExtraExtraExtraTypeDef" = (
        dataclasses.field()
    )

    pageSize = field("pageSize")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRequestPaginateExtraExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRequestPaginateExtraExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestPaginateExtraExtra:
    boto3_raw_data: "type_defs.ListRequestPaginateExtraExtraTypeDef" = (
        dataclasses.field()
    )

    pageSize = field("pageSize")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRequestPaginateExtraExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRequestPaginateExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestPaginateExtra:
    boto3_raw_data: "type_defs.ListRequestPaginateExtraTypeDef" = dataclasses.field()

    pageSize = field("pageSize")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRequestPaginateExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRequestPaginateExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRequestPaginate:
    boto3_raw_data: "type_defs.ListRequestPaginateTypeDef" = dataclasses.field()

    pageSize = field("pageSize")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubjectsResponse:
    boto3_raw_data: "type_defs.ListSubjectsResponseTypeDef" = dataclasses.field()

    @cached_property
    def subjects(self):  # pragma: no cover
        return SubjectSummary.make_many(self.boto3_raw_data["subjects"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubjectsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubjectsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetNotificationSettingsRequest:
    boto3_raw_data: "type_defs.ResetNotificationSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def notificationSettingKeys(self):  # pragma: no cover
        return NotificationSettingKey.make_many(
            self.boto3_raw_data["notificationSettingKeys"]
        )

    trustAnchorId = field("trustAnchorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResetNotificationSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetNotificationSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Source:
    boto3_raw_data: "type_defs.SourceTypeDef" = dataclasses.field()

    @cached_property
    def sourceData(self):  # pragma: no cover
        return SourceData.make_one(self.boto3_raw_data["sourceData"])

    sourceType = field("sourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileDetail:
    boto3_raw_data: "type_defs.ProfileDetailTypeDef" = dataclasses.field()

    acceptRoleSessionName = field("acceptRoleSessionName")

    @cached_property
    def attributeMappings(self):  # pragma: no cover
        return AttributeMapping.make_many(self.boto3_raw_data["attributeMappings"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    durationSeconds = field("durationSeconds")
    enabled = field("enabled")
    managedPolicyArns = field("managedPolicyArns")
    name = field("name")
    profileArn = field("profileArn")
    profileId = field("profileId")
    requireInstanceProperties = field("requireInstanceProperties")
    roleArns = field("roleArns")
    sessionPolicy = field("sessionPolicy")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfileDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProfileDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubjectDetailResponse:
    boto3_raw_data: "type_defs.SubjectDetailResponseTypeDef" = dataclasses.field()

    @cached_property
    def subject(self):  # pragma: no cover
        return SubjectDetail.make_one(self.boto3_raw_data["subject"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubjectDetailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubjectDetailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrustAnchorRequest:
    boto3_raw_data: "type_defs.CreateTrustAnchorRequestTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    enabled = field("enabled")

    @cached_property
    def notificationSettings(self):  # pragma: no cover
        return NotificationSetting.make_many(
            self.boto3_raw_data["notificationSettings"]
        )

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrustAnchorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrustAnchorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustAnchorDetail:
    boto3_raw_data: "type_defs.TrustAnchorDetailTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    enabled = field("enabled")
    name = field("name")

    @cached_property
    def notificationSettings(self):  # pragma: no cover
        return NotificationSettingDetail.make_many(
            self.boto3_raw_data["notificationSettings"]
        )

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    trustAnchorArn = field("trustAnchorArn")
    trustAnchorId = field("trustAnchorId")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrustAnchorDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustAnchorDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrustAnchorRequest:
    boto3_raw_data: "type_defs.UpdateTrustAnchorRequestTypeDef" = dataclasses.field()

    trustAnchorId = field("trustAnchorId")
    name = field("name")

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTrustAnchorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrustAnchorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAttributeMappingResponse:
    boto3_raw_data: "type_defs.DeleteAttributeMappingResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def profile(self):  # pragma: no cover
        return ProfileDetail.make_one(self.boto3_raw_data["profile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAttributeMappingResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAttributeMappingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilesResponse:
    boto3_raw_data: "type_defs.ListProfilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def profiles(self):  # pragma: no cover
        return ProfileDetail.make_many(self.boto3_raw_data["profiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileDetailResponse:
    boto3_raw_data: "type_defs.ProfileDetailResponseTypeDef" = dataclasses.field()

    @cached_property
    def profile(self):  # pragma: no cover
        return ProfileDetail.make_one(self.boto3_raw_data["profile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileDetailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileDetailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAttributeMappingResponse:
    boto3_raw_data: "type_defs.PutAttributeMappingResponseTypeDef" = dataclasses.field()

    @cached_property
    def profile(self):  # pragma: no cover
        return ProfileDetail.make_one(self.boto3_raw_data["profile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAttributeMappingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAttributeMappingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrustAnchorsResponse:
    boto3_raw_data: "type_defs.ListTrustAnchorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def trustAnchors(self):  # pragma: no cover
        return TrustAnchorDetail.make_many(self.boto3_raw_data["trustAnchors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrustAnchorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrustAnchorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutNotificationSettingsResponse:
    boto3_raw_data: "type_defs.PutNotificationSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trustAnchor(self):  # pragma: no cover
        return TrustAnchorDetail.make_one(self.boto3_raw_data["trustAnchor"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutNotificationSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutNotificationSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetNotificationSettingsResponse:
    boto3_raw_data: "type_defs.ResetNotificationSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def trustAnchor(self):  # pragma: no cover
        return TrustAnchorDetail.make_one(self.boto3_raw_data["trustAnchor"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResetNotificationSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetNotificationSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustAnchorDetailResponse:
    boto3_raw_data: "type_defs.TrustAnchorDetailResponseTypeDef" = dataclasses.field()

    @cached_property
    def trustAnchor(self):  # pragma: no cover
        return TrustAnchorDetail.make_one(self.boto3_raw_data["trustAnchor"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrustAnchorDetailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustAnchorDetailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
