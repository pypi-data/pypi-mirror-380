# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_signer import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddProfilePermissionRequest:
    boto3_raw_data: "type_defs.AddProfilePermissionRequestTypeDef" = dataclasses.field()

    profileName = field("profileName")
    action = field("action")
    principal = field("principal")
    statementId = field("statementId")
    profileVersion = field("profileVersion")
    revisionId = field("revisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddProfilePermissionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddProfilePermissionRequestTypeDef"]
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
class CancelSigningProfileRequest:
    boto3_raw_data: "type_defs.CancelSigningProfileRequestTypeDef" = dataclasses.field()

    profileName = field("profileName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelSigningProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSigningProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSigningJobRequest:
    boto3_raw_data: "type_defs.DescribeSigningJobRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSigningJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSigningJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigningJobRevocationRecord:
    boto3_raw_data: "type_defs.SigningJobRevocationRecordTypeDef" = dataclasses.field()

    reason = field("reason")
    revokedAt = field("revokedAt")
    revokedBy = field("revokedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SigningJobRevocationRecordTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SigningJobRevocationRecordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigningMaterial:
    boto3_raw_data: "type_defs.SigningMaterialTypeDef" = dataclasses.field()

    certificateArn = field("certificateArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SigningMaterialTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SigningMaterialTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Destination:
    boto3_raw_data: "type_defs.S3DestinationTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    prefix = field("prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3DestinationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionAlgorithmOptions:
    boto3_raw_data: "type_defs.EncryptionAlgorithmOptionsTypeDef" = dataclasses.field()

    allowedValues = field("allowedValues")
    defaultValue = field("defaultValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionAlgorithmOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionAlgorithmOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSigningPlatformRequest:
    boto3_raw_data: "type_defs.GetSigningPlatformRequestTypeDef" = dataclasses.field()

    platformId = field("platformId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSigningPlatformRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSigningPlatformRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigningImageFormat:
    boto3_raw_data: "type_defs.SigningImageFormatTypeDef" = dataclasses.field()

    supportedFormats = field("supportedFormats")
    defaultFormat = field("defaultFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SigningImageFormatTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SigningImageFormatTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSigningProfileRequest:
    boto3_raw_data: "type_defs.GetSigningProfileRequestTypeDef" = dataclasses.field()

    profileName = field("profileName")
    profileOwner = field("profileOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSigningProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSigningProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignatureValidityPeriod:
    boto3_raw_data: "type_defs.SignatureValidityPeriodTypeDef" = dataclasses.field()

    value = field("value")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignatureValidityPeriodTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignatureValidityPeriodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigningProfileRevocationRecord:
    boto3_raw_data: "type_defs.SigningProfileRevocationRecordTypeDef" = (
        dataclasses.field()
    )

    revocationEffectiveFrom = field("revocationEffectiveFrom")
    revokedAt = field("revokedAt")
    revokedBy = field("revokedBy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SigningProfileRevocationRecordTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SigningProfileRevocationRecordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HashAlgorithmOptions:
    boto3_raw_data: "type_defs.HashAlgorithmOptionsTypeDef" = dataclasses.field()

    allowedValues = field("allowedValues")
    defaultValue = field("defaultValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HashAlgorithmOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HashAlgorithmOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilePermissionsRequest:
    boto3_raw_data: "type_defs.ListProfilePermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    profileName = field("profileName")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProfilePermissionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Permission:
    boto3_raw_data: "type_defs.PermissionTypeDef" = dataclasses.field()

    action = field("action")
    principal = field("principal")
    statementId = field("statementId")
    profileVersion = field("profileVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PermissionTypeDef"]]
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
class ListSigningPlatformsRequest:
    boto3_raw_data: "type_defs.ListSigningPlatformsRequestTypeDef" = dataclasses.field()

    category = field("category")
    partner = field("partner")
    target = field("target")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSigningPlatformsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningPlatformsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSigningProfilesRequest:
    boto3_raw_data: "type_defs.ListSigningProfilesRequestTypeDef" = dataclasses.field()

    includeCanceled = field("includeCanceled")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    platformId = field("platformId")
    statuses = field("statuses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSigningProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningProfilesRequestTypeDef"]
        ],
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
class RemoveProfilePermissionRequest:
    boto3_raw_data: "type_defs.RemoveProfilePermissionRequestTypeDef" = (
        dataclasses.field()
    )

    profileName = field("profileName")
    revisionId = field("revisionId")
    statementId = field("statementId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveProfilePermissionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveProfilePermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeSignatureRequest:
    boto3_raw_data: "type_defs.RevokeSignatureRequestTypeDef" = dataclasses.field()

    jobId = field("jobId")
    reason = field("reason")
    jobOwner = field("jobOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeSignatureRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeSignatureRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SignedObject:
    boto3_raw_data: "type_defs.S3SignedObjectTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    key = field("key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3SignedObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3SignedObjectTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Source:
    boto3_raw_data: "type_defs.S3SourceTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    key = field("key")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3SourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3SourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigningConfigurationOverrides:
    boto3_raw_data: "type_defs.SigningConfigurationOverridesTypeDef" = (
        dataclasses.field()
    )

    encryptionAlgorithm = field("encryptionAlgorithm")
    hashAlgorithm = field("hashAlgorithm")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SigningConfigurationOverridesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SigningConfigurationOverridesTypeDef"]
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
    tags = field("tags")

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
class AddProfilePermissionResponse:
    boto3_raw_data: "type_defs.AddProfilePermissionResponseTypeDef" = (
        dataclasses.field()
    )

    revisionId = field("revisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddProfilePermissionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddProfilePermissionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRevocationStatusResponse:
    boto3_raw_data: "type_defs.GetRevocationStatusResponseTypeDef" = dataclasses.field()

    revokedEntities = field("revokedEntities")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRevocationStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRevocationStatusResponseTypeDef"]
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

    tags = field("tags")

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
class PutSigningProfileResponse:
    boto3_raw_data: "type_defs.PutSigningProfileResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    profileVersion = field("profileVersion")
    profileVersionArn = field("profileVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutSigningProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSigningProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveProfilePermissionResponse:
    boto3_raw_data: "type_defs.RemoveProfilePermissionResponseTypeDef" = (
        dataclasses.field()
    )

    revisionId = field("revisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveProfilePermissionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveProfilePermissionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignPayloadResponse:
    boto3_raw_data: "type_defs.SignPayloadResponseTypeDef" = dataclasses.field()

    jobId = field("jobId")
    jobOwner = field("jobOwner")
    metadata = field("metadata")
    signature = field("signature")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignPayloadResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignPayloadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSigningJobResponse:
    boto3_raw_data: "type_defs.StartSigningJobResponseTypeDef" = dataclasses.field()

    jobId = field("jobId")
    jobOwner = field("jobOwner")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSigningJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSigningJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignPayloadRequest:
    boto3_raw_data: "type_defs.SignPayloadRequestTypeDef" = dataclasses.field()

    profileName = field("profileName")
    payload = field("payload")
    payloadFormat = field("payloadFormat")
    profileOwner = field("profileOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignPayloadRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignPayloadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSigningJobRequestWait:
    boto3_raw_data: "type_defs.DescribeSigningJobRequestWaitTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSigningJobRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSigningJobRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Destination:
    boto3_raw_data: "type_defs.DestinationTypeDef" = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DestinationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRevocationStatusRequest:
    boto3_raw_data: "type_defs.GetRevocationStatusRequestTypeDef" = dataclasses.field()

    signatureTimestamp = field("signatureTimestamp")
    platformId = field("platformId")
    profileVersionArn = field("profileVersionArn")
    jobArn = field("jobArn")
    certificateHashes = field("certificateHashes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRevocationStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRevocationStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSigningJobsRequest:
    boto3_raw_data: "type_defs.ListSigningJobsRequestTypeDef" = dataclasses.field()

    status = field("status")
    platformId = field("platformId")
    requestedBy = field("requestedBy")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    isRevoked = field("isRevoked")
    signatureExpiresBefore = field("signatureExpiresBefore")
    signatureExpiresAfter = field("signatureExpiresAfter")
    jobInvoker = field("jobInvoker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSigningJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeSigningProfileRequest:
    boto3_raw_data: "type_defs.RevokeSigningProfileRequestTypeDef" = dataclasses.field()

    profileName = field("profileName")
    profileVersion = field("profileVersion")
    reason = field("reason")
    effectiveTime = field("effectiveTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeSigningProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeSigningProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigningProfile:
    boto3_raw_data: "type_defs.SigningProfileTypeDef" = dataclasses.field()

    profileName = field("profileName")
    profileVersion = field("profileVersion")
    profileVersionArn = field("profileVersionArn")

    @cached_property
    def signingMaterial(self):  # pragma: no cover
        return SigningMaterial.make_one(self.boto3_raw_data["signingMaterial"])

    @cached_property
    def signatureValidityPeriod(self):  # pragma: no cover
        return SignatureValidityPeriod.make_one(
            self.boto3_raw_data["signatureValidityPeriod"]
        )

    platformId = field("platformId")
    platformDisplayName = field("platformDisplayName")
    signingParameters = field("signingParameters")
    status = field("status")
    arn = field("arn")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SigningProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SigningProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigningConfiguration:
    boto3_raw_data: "type_defs.SigningConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def encryptionAlgorithmOptions(self):  # pragma: no cover
        return EncryptionAlgorithmOptions.make_one(
            self.boto3_raw_data["encryptionAlgorithmOptions"]
        )

    @cached_property
    def hashAlgorithmOptions(self):  # pragma: no cover
        return HashAlgorithmOptions.make_one(
            self.boto3_raw_data["hashAlgorithmOptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SigningConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SigningConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilePermissionsResponse:
    boto3_raw_data: "type_defs.ListProfilePermissionsResponseTypeDef" = (
        dataclasses.field()
    )

    revisionId = field("revisionId")
    policySizeBytes = field("policySizeBytes")

    @cached_property
    def permissions(self):  # pragma: no cover
        return Permission.make_many(self.boto3_raw_data["permissions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProfilePermissionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilePermissionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSigningJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListSigningJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    platformId = field("platformId")
    requestedBy = field("requestedBy")
    isRevoked = field("isRevoked")
    signatureExpiresBefore = field("signatureExpiresBefore")
    signatureExpiresAfter = field("signatureExpiresAfter")
    jobInvoker = field("jobInvoker")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSigningJobsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSigningPlatformsRequestPaginate:
    boto3_raw_data: "type_defs.ListSigningPlatformsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    category = field("category")
    partner = field("partner")
    target = field("target")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSigningPlatformsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningPlatformsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSigningProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListSigningProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    includeCanceled = field("includeCanceled")
    platformId = field("platformId")
    statuses = field("statuses")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSigningProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignedObject:
    boto3_raw_data: "type_defs.SignedObjectTypeDef" = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return S3SignedObject.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignedObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SignedObjectTypeDef"]],
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
    def s3(self):  # pragma: no cover
        return S3Source.make_one(self.boto3_raw_data["s3"])

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
class SigningPlatformOverrides:
    boto3_raw_data: "type_defs.SigningPlatformOverridesTypeDef" = dataclasses.field()

    @cached_property
    def signingConfiguration(self):  # pragma: no cover
        return SigningConfigurationOverrides.make_one(
            self.boto3_raw_data["signingConfiguration"]
        )

    signingImageFormat = field("signingImageFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SigningPlatformOverridesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SigningPlatformOverridesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSigningProfilesResponse:
    boto3_raw_data: "type_defs.ListSigningProfilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def profiles(self):  # pragma: no cover
        return SigningProfile.make_many(self.boto3_raw_data["profiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSigningProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSigningPlatformResponse:
    boto3_raw_data: "type_defs.GetSigningPlatformResponseTypeDef" = dataclasses.field()

    platformId = field("platformId")
    displayName = field("displayName")
    partner = field("partner")
    target = field("target")
    category = field("category")

    @cached_property
    def signingConfiguration(self):  # pragma: no cover
        return SigningConfiguration.make_one(
            self.boto3_raw_data["signingConfiguration"]
        )

    @cached_property
    def signingImageFormat(self):  # pragma: no cover
        return SigningImageFormat.make_one(self.boto3_raw_data["signingImageFormat"])

    maxSizeInMB = field("maxSizeInMB")
    revocationSupported = field("revocationSupported")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSigningPlatformResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSigningPlatformResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigningPlatform:
    boto3_raw_data: "type_defs.SigningPlatformTypeDef" = dataclasses.field()

    platformId = field("platformId")
    displayName = field("displayName")
    partner = field("partner")
    target = field("target")
    category = field("category")

    @cached_property
    def signingConfiguration(self):  # pragma: no cover
        return SigningConfiguration.make_one(
            self.boto3_raw_data["signingConfiguration"]
        )

    @cached_property
    def signingImageFormat(self):  # pragma: no cover
        return SigningImageFormat.make_one(self.boto3_raw_data["signingImageFormat"])

    maxSizeInMB = field("maxSizeInMB")
    revocationSupported = field("revocationSupported")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SigningPlatformTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SigningPlatformTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SigningJob:
    boto3_raw_data: "type_defs.SigningJobTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    @cached_property
    def signedObject(self):  # pragma: no cover
        return SignedObject.make_one(self.boto3_raw_data["signedObject"])

    @cached_property
    def signingMaterial(self):  # pragma: no cover
        return SigningMaterial.make_one(self.boto3_raw_data["signingMaterial"])

    createdAt = field("createdAt")
    status = field("status")
    isRevoked = field("isRevoked")
    profileName = field("profileName")
    profileVersion = field("profileVersion")
    platformId = field("platformId")
    platformDisplayName = field("platformDisplayName")
    signatureExpiresAt = field("signatureExpiresAt")
    jobOwner = field("jobOwner")
    jobInvoker = field("jobInvoker")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SigningJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SigningJobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSigningJobRequest:
    boto3_raw_data: "type_defs.StartSigningJobRequestTypeDef" = dataclasses.field()

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    @cached_property
    def destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["destination"])

    profileName = field("profileName")
    clientRequestToken = field("clientRequestToken")
    profileOwner = field("profileOwner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartSigningJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSigningJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSigningJobResponse:
    boto3_raw_data: "type_defs.DescribeSigningJobResponseTypeDef" = dataclasses.field()

    jobId = field("jobId")

    @cached_property
    def source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["source"])

    @cached_property
    def signingMaterial(self):  # pragma: no cover
        return SigningMaterial.make_one(self.boto3_raw_data["signingMaterial"])

    platformId = field("platformId")
    platformDisplayName = field("platformDisplayName")
    profileName = field("profileName")
    profileVersion = field("profileVersion")

    @cached_property
    def overrides(self):  # pragma: no cover
        return SigningPlatformOverrides.make_one(self.boto3_raw_data["overrides"])

    signingParameters = field("signingParameters")
    createdAt = field("createdAt")
    completedAt = field("completedAt")
    signatureExpiresAt = field("signatureExpiresAt")
    requestedBy = field("requestedBy")
    status = field("status")
    statusReason = field("statusReason")

    @cached_property
    def revocationRecord(self):  # pragma: no cover
        return SigningJobRevocationRecord.make_one(
            self.boto3_raw_data["revocationRecord"]
        )

    @cached_property
    def signedObject(self):  # pragma: no cover
        return SignedObject.make_one(self.boto3_raw_data["signedObject"])

    jobOwner = field("jobOwner")
    jobInvoker = field("jobInvoker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSigningJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSigningJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSigningProfileResponse:
    boto3_raw_data: "type_defs.GetSigningProfileResponseTypeDef" = dataclasses.field()

    profileName = field("profileName")
    profileVersion = field("profileVersion")
    profileVersionArn = field("profileVersionArn")

    @cached_property
    def revocationRecord(self):  # pragma: no cover
        return SigningProfileRevocationRecord.make_one(
            self.boto3_raw_data["revocationRecord"]
        )

    @cached_property
    def signingMaterial(self):  # pragma: no cover
        return SigningMaterial.make_one(self.boto3_raw_data["signingMaterial"])

    platformId = field("platformId")
    platformDisplayName = field("platformDisplayName")

    @cached_property
    def signatureValidityPeriod(self):  # pragma: no cover
        return SignatureValidityPeriod.make_one(
            self.boto3_raw_data["signatureValidityPeriod"]
        )

    @cached_property
    def overrides(self):  # pragma: no cover
        return SigningPlatformOverrides.make_one(self.boto3_raw_data["overrides"])

    signingParameters = field("signingParameters")
    status = field("status")
    statusReason = field("statusReason")
    arn = field("arn")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSigningProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSigningProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSigningProfileRequest:
    boto3_raw_data: "type_defs.PutSigningProfileRequestTypeDef" = dataclasses.field()

    profileName = field("profileName")
    platformId = field("platformId")

    @cached_property
    def signingMaterial(self):  # pragma: no cover
        return SigningMaterial.make_one(self.boto3_raw_data["signingMaterial"])

    @cached_property
    def signatureValidityPeriod(self):  # pragma: no cover
        return SignatureValidityPeriod.make_one(
            self.boto3_raw_data["signatureValidityPeriod"]
        )

    @cached_property
    def overrides(self):  # pragma: no cover
        return SigningPlatformOverrides.make_one(self.boto3_raw_data["overrides"])

    signingParameters = field("signingParameters")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutSigningProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSigningProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSigningPlatformsResponse:
    boto3_raw_data: "type_defs.ListSigningPlatformsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def platforms(self):  # pragma: no cover
        return SigningPlatform.make_many(self.boto3_raw_data["platforms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSigningPlatformsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningPlatformsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSigningJobsResponse:
    boto3_raw_data: "type_defs.ListSigningJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobs(self):  # pragma: no cover
        return SigningJob.make_many(self.boto3_raw_data["jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSigningJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSigningJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
