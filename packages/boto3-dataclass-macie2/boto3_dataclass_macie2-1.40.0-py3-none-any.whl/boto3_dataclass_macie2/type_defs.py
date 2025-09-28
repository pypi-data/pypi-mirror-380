# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_macie2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptInvitationRequest:
    boto3_raw_data: "type_defs.AcceptInvitationRequestTypeDef" = dataclasses.field()

    invitationId = field("invitationId")
    administratorAccountId = field("administratorAccountId")
    masterAccount = field("masterAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptInvitationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControlList:
    boto3_raw_data: "type_defs.AccessControlListTypeDef" = dataclasses.field()

    allowsPublicReadAccess = field("allowsPublicReadAccess")
    allowsPublicWriteAccess = field("allowsPublicWriteAccess")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessControlListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountDetail:
    boto3_raw_data: "type_defs.AccountDetailTypeDef" = dataclasses.field()

    accountId = field("accountId")
    email = field("email")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockPublicAccess:
    boto3_raw_data: "type_defs.BlockPublicAccessTypeDef" = dataclasses.field()

    blockPublicAcls = field("blockPublicAcls")
    blockPublicPolicy = field("blockPublicPolicy")
    ignorePublicAcls = field("ignorePublicAcls")
    restrictPublicBuckets = field("restrictPublicBuckets")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlockPublicAccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BlockPublicAccessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdminAccount:
    boto3_raw_data: "type_defs.AdminAccountTypeDef" = dataclasses.field()

    accountId = field("accountId")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdminAccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdminAccountTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3WordsList:
    boto3_raw_data: "type_defs.S3WordsListTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    objectKey = field("objectKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3WordsListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3WordsListTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowListStatus:
    boto3_raw_data: "type_defs.AllowListStatusTypeDef" = dataclasses.field()

    code = field("code")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AllowListStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AllowListStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowListSummary:
    boto3_raw_data: "type_defs.AllowListSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    description = field("description")
    id = field("id")
    name = field("name")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AllowListSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowListSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiCallDetails:
    boto3_raw_data: "type_defs.ApiCallDetailsTypeDef" = dataclasses.field()

    api = field("api")
    apiServiceName = field("apiServiceName")
    firstSeen = field("firstSeen")
    lastSeen = field("lastSeen")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiCallDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiCallDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedDiscoveryAccount:
    boto3_raw_data: "type_defs.AutomatedDiscoveryAccountTypeDef" = dataclasses.field()

    accountId = field("accountId")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomatedDiscoveryAccountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedDiscoveryAccountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedDiscoveryAccountUpdateError:
    boto3_raw_data: "type_defs.AutomatedDiscoveryAccountUpdateErrorTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedDiscoveryAccountUpdateErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedDiscoveryAccountUpdateErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedDiscoveryAccountUpdate:
    boto3_raw_data: "type_defs.AutomatedDiscoveryAccountUpdateTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedDiscoveryAccountUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedDiscoveryAccountUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsAccount:
    boto3_raw_data: "type_defs.AwsAccountTypeDef" = dataclasses.field()

    accountId = field("accountId")
    principalId = field("principalId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsAccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AwsAccountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsService:
    boto3_raw_data: "type_defs.AwsServiceTypeDef" = dataclasses.field()

    invokedBy = field("invokedBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AwsServiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCustomDataIdentifierSummary:
    boto3_raw_data: "type_defs.BatchGetCustomDataIdentifierSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    deleted = field("deleted")
    description = field("description")
    id = field("id")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetCustomDataIdentifierSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCustomDataIdentifierSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCustomDataIdentifiersRequest:
    boto3_raw_data: "type_defs.BatchGetCustomDataIdentifiersRequestTypeDef" = (
        dataclasses.field()
    )

    ids = field("ids")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetCustomDataIdentifiersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCustomDataIdentifiersRequestTypeDef"]
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
class BucketCountByEffectivePermission:
    boto3_raw_data: "type_defs.BucketCountByEffectivePermissionTypeDef" = (
        dataclasses.field()
    )

    publiclyAccessible = field("publiclyAccessible")
    publiclyReadable = field("publiclyReadable")
    publiclyWritable = field("publiclyWritable")
    unknown = field("unknown")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BucketCountByEffectivePermissionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketCountByEffectivePermissionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketCountByEncryptionType:
    boto3_raw_data: "type_defs.BucketCountByEncryptionTypeTypeDef" = dataclasses.field()

    kmsManaged = field("kmsManaged")
    s3Managed = field("s3Managed")
    unencrypted = field("unencrypted")
    unknown = field("unknown")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketCountByEncryptionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketCountByEncryptionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketCountBySharedAccessType:
    boto3_raw_data: "type_defs.BucketCountBySharedAccessTypeTypeDef" = (
        dataclasses.field()
    )

    external = field("external")
    internal = field("internal")
    notShared = field("notShared")
    unknown = field("unknown")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BucketCountBySharedAccessTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketCountBySharedAccessTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketCountPolicyAllowsUnencryptedObjectUploads:
    boto3_raw_data: (
        "type_defs.BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef"
    ) = dataclasses.field()

    allowsUnencryptedObjectUploads = field("allowsUnencryptedObjectUploads")
    deniesUnencryptedObjectUploads = field("deniesUnencryptedObjectUploads")
    unknown = field("unknown")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketCriteriaAdditionalProperties:
    boto3_raw_data: "type_defs.BucketCriteriaAdditionalPropertiesTypeDef" = (
        dataclasses.field()
    )

    eq = field("eq")
    gt = field("gt")
    gte = field("gte")
    lt = field("lt")
    lte = field("lte")
    neq = field("neq")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BucketCriteriaAdditionalPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketCriteriaAdditionalPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketPolicy:
    boto3_raw_data: "type_defs.BucketPolicyTypeDef" = dataclasses.field()

    allowsPublicReadAccess = field("allowsPublicReadAccess")
    allowsPublicWriteAccess = field("allowsPublicWriteAccess")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketServerSideEncryption:
    boto3_raw_data: "type_defs.BucketServerSideEncryptionTypeDef" = dataclasses.field()

    kmsMasterKeyId = field("kmsMasterKeyId")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketServerSideEncryptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketServerSideEncryptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDetails:
    boto3_raw_data: "type_defs.JobDetailsTypeDef" = dataclasses.field()

    isDefinedInJob = field("isDefinedInJob")
    isMonitoredByJob = field("isMonitoredByJob")
    lastJobId = field("lastJobId")
    lastJobRunTime = field("lastJobRunTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyValuePair:
    boto3_raw_data: "type_defs.KeyValuePairTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyValuePairTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyValuePairTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectCountByEncryptionType:
    boto3_raw_data: "type_defs.ObjectCountByEncryptionTypeTypeDef" = dataclasses.field()

    customerManaged = field("customerManaged")
    kmsManaged = field("kmsManaged")
    s3Managed = field("s3Managed")
    unencrypted = field("unencrypted")
    unknown = field("unknown")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectCountByEncryptionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectCountByEncryptionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLevelStatistics:
    boto3_raw_data: "type_defs.ObjectLevelStatisticsTypeDef" = dataclasses.field()

    fileType = field("fileType")
    storageClass = field("storageClass")
    total = field("total")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectLevelStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLevelStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationDetails:
    boto3_raw_data: "type_defs.ReplicationDetailsTypeDef" = dataclasses.field()

    replicated = field("replicated")
    replicatedExternally = field("replicatedExternally")
    replicationAccounts = field("replicationAccounts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketSortCriteria:
    boto3_raw_data: "type_defs.BucketSortCriteriaTypeDef" = dataclasses.field()

    attributeName = field("attributeName")
    orderBy = field("orderBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketSortCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketSortCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SensitivityAggregations:
    boto3_raw_data: "type_defs.SensitivityAggregationsTypeDef" = dataclasses.field()

    classifiableSizeInBytes = field("classifiableSizeInBytes")
    publiclyAccessibleCount = field("publiclyAccessibleCount")
    totalCount = field("totalCount")
    totalSizeInBytes = field("totalSizeInBytes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SensitivityAggregationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SensitivityAggregationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cell:
    boto3_raw_data: "type_defs.CellTypeDef" = dataclasses.field()

    cellReference = field("cellReference")
    column = field("column")
    columnName = field("columnName")
    row = field("row")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CellTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CellTypeDef"]]
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
    kmsKeyArn = field("kmsKeyArn")
    keyPrefix = field("keyPrefix")

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
class ClassificationResultStatus:
    boto3_raw_data: "type_defs.ClassificationResultStatusTypeDef" = dataclasses.field()

    code = field("code")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClassificationResultStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClassificationResultStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClassificationScopeSummary:
    boto3_raw_data: "type_defs.ClassificationScopeSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClassificationScopeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClassificationScopeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SeverityLevel:
    boto3_raw_data: "type_defs.SeverityLevelTypeDef" = dataclasses.field()

    occurrencesThreshold = field("occurrencesThreshold")
    severity = field("severity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SeverityLevelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SeverityLevelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInvitationsRequest:
    boto3_raw_data: "type_defs.CreateInvitationsRequestTypeDef" = dataclasses.field()

    accountIds = field("accountIds")
    disableEmailNotification = field("disableEmailNotification")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInvitationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInvitationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnprocessedAccount:
    boto3_raw_data: "type_defs.UnprocessedAccountTypeDef" = dataclasses.field()

    accountId = field("accountId")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedAccountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedAccountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSampleFindingsRequest:
    boto3_raw_data: "type_defs.CreateSampleFindingsRequestTypeDef" = dataclasses.field()

    findingTypes = field("findingTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSampleFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSampleFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimpleCriterionForJobOutput:
    boto3_raw_data: "type_defs.SimpleCriterionForJobOutputTypeDef" = dataclasses.field()

    comparator = field("comparator")
    key = field("key")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimpleCriterionForJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimpleCriterionForJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimpleCriterionForJob:
    boto3_raw_data: "type_defs.SimpleCriterionForJobTypeDef" = dataclasses.field()

    comparator = field("comparator")
    key = field("key")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimpleCriterionForJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimpleCriterionForJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CriterionAdditionalPropertiesOutput:
    boto3_raw_data: "type_defs.CriterionAdditionalPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    eq = field("eq")
    eqExactMatch = field("eqExactMatch")
    gt = field("gt")
    gte = field("gte")
    lt = field("lt")
    lte = field("lte")
    neq = field("neq")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CriterionAdditionalPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CriterionAdditionalPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CriterionAdditionalProperties:
    boto3_raw_data: "type_defs.CriterionAdditionalPropertiesTypeDef" = (
        dataclasses.field()
    )

    eq = field("eq")
    eqExactMatch = field("eqExactMatch")
    gt = field("gt")
    gte = field("gte")
    lt = field("lt")
    lte = field("lte")
    neq = field("neq")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CriterionAdditionalPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CriterionAdditionalPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDataIdentifierSummary:
    boto3_raw_data: "type_defs.CustomDataIdentifierSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    description = field("description")
    id = field("id")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomDataIdentifierSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDataIdentifierSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeclineInvitationsRequest:
    boto3_raw_data: "type_defs.DeclineInvitationsRequestTypeDef" = dataclasses.field()

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeclineInvitationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeclineInvitationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAllowListRequest:
    boto3_raw_data: "type_defs.DeleteAllowListRequestTypeDef" = dataclasses.field()

    id = field("id")
    ignoreJobChecks = field("ignoreJobChecks")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAllowListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAllowListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomDataIdentifierRequest:
    boto3_raw_data: "type_defs.DeleteCustomDataIdentifierRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCustomDataIdentifierRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomDataIdentifierRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFindingsFilterRequest:
    boto3_raw_data: "type_defs.DeleteFindingsFilterRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFindingsFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFindingsFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInvitationsRequest:
    boto3_raw_data: "type_defs.DeleteInvitationsRequestTypeDef" = dataclasses.field()

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInvitationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInvitationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMemberRequest:
    boto3_raw_data: "type_defs.DeleteMemberRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMemberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMemberRequestTypeDef"]
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
class DescribeClassificationJobRequest:
    boto3_raw_data: "type_defs.DescribeClassificationJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClassificationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClassificationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LastRunErrorStatus:
    boto3_raw_data: "type_defs.LastRunErrorStatusTypeDef" = dataclasses.field()

    code = field("code")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LastRunErrorStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LastRunErrorStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Statistics:
    boto3_raw_data: "type_defs.StatisticsTypeDef" = dataclasses.field()

    approximateNumberOfObjectsToProcess = field("approximateNumberOfObjectsToProcess")
    numberOfRuns = field("numberOfRuns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatisticsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPausedDetails:
    boto3_raw_data: "type_defs.UserPausedDetailsTypeDef" = dataclasses.field()

    jobExpiresAt = field("jobExpiresAt")
    jobImminentExpirationHealthEventArn = field("jobImminentExpirationHealthEventArn")
    jobPausedAt = field("jobPausedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserPausedDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPausedDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectedDataDetails:
    boto3_raw_data: "type_defs.DetectedDataDetailsTypeDef" = dataclasses.field()

    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectedDataDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectedDataDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Detection:
    boto3_raw_data: "type_defs.DetectionTypeDef" = dataclasses.field()

    arn = field("arn")
    count = field("count")
    id = field("id")
    name = field("name")
    suppressed = field("suppressed")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DetectionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableOrganizationAdminAccountRequest:
    boto3_raw_data: "type_defs.DisableOrganizationAdminAccountRequestTypeDef" = (
        dataclasses.field()
    )

    adminAccountId = field("adminAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisableOrganizationAdminAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableOrganizationAdminAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMemberRequest:
    boto3_raw_data: "type_defs.DisassociateMemberRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateMemberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMemberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainDetails:
    boto3_raw_data: "type_defs.DomainDetailsTypeDef" = dataclasses.field()

    domainName = field("domainName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableMacieRequest:
    boto3_raw_data: "type_defs.EnableMacieRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    findingPublishingFrequency = field("findingPublishingFrequency")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableMacieRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableMacieRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableOrganizationAdminAccountRequest:
    boto3_raw_data: "type_defs.EnableOrganizationAdminAccountRequestTypeDef" = (
        dataclasses.field()
    )

    adminAccountId = field("adminAccountId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableOrganizationAdminAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableOrganizationAdminAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingStatisticsSortCriteria:
    boto3_raw_data: "type_defs.FindingStatisticsSortCriteriaTypeDef" = (
        dataclasses.field()
    )

    attributeName = field("attributeName")
    orderBy = field("orderBy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FindingStatisticsSortCriteriaTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingStatisticsSortCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Severity:
    boto3_raw_data: "type_defs.SeverityTypeDef" = dataclasses.field()

    description = field("description")
    score = field("score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SeverityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SeverityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingsFilterListItem:
    boto3_raw_data: "type_defs.FindingsFilterListItemTypeDef" = dataclasses.field()

    action = field("action")
    arn = field("arn")
    id = field("id")
    name = field("name")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FindingsFilterListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingsFilterListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Invitation:
    boto3_raw_data: "type_defs.InvitationTypeDef" = dataclasses.field()

    accountId = field("accountId")
    invitationId = field("invitationId")
    invitedAt = field("invitedAt")
    relationshipStatus = field("relationshipStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InvitationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InvitationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAllowListRequest:
    boto3_raw_data: "type_defs.GetAllowListRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAllowListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAllowListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketStatisticsRequest:
    boto3_raw_data: "type_defs.GetBucketStatisticsRequestTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketStatisticsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClassificationScopeRequest:
    boto3_raw_data: "type_defs.GetClassificationScopeRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetClassificationScopeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClassificationScopeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomDataIdentifierRequest:
    boto3_raw_data: "type_defs.GetCustomDataIdentifierRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCustomDataIdentifierRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomDataIdentifierRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupCount:
    boto3_raw_data: "type_defs.GroupCountTypeDef" = dataclasses.field()

    count = field("count")
    groupKey = field("groupKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupCountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupCountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsFilterRequest:
    boto3_raw_data: "type_defs.GetFindingsFilterRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingsFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityHubConfiguration:
    boto3_raw_data: "type_defs.SecurityHubConfigurationTypeDef" = dataclasses.field()

    publishClassificationFindings = field("publishClassificationFindings")
    publishPolicyFindings = field("publishPolicyFindings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityHubConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityHubConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SortCriteria:
    boto3_raw_data: "type_defs.SortCriteriaTypeDef" = dataclasses.field()

    attributeName = field("attributeName")
    orderBy = field("orderBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemberRequest:
    boto3_raw_data: "type_defs.GetMemberRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMemberRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMemberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceProfileRequest:
    boto3_raw_data: "type_defs.GetResourceProfileRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceStatistics:
    boto3_raw_data: "type_defs.ResourceStatisticsTypeDef" = dataclasses.field()

    totalBytesClassified = field("totalBytesClassified")
    totalDetections = field("totalDetections")
    totalDetectionsSuppressed = field("totalDetectionsSuppressed")
    totalItemsClassified = field("totalItemsClassified")
    totalItemsSensitive = field("totalItemsSensitive")
    totalItemsSkipped = field("totalItemsSkipped")
    totalItemsSkippedInvalidEncryption = field("totalItemsSkippedInvalidEncryption")
    totalItemsSkippedInvalidKms = field("totalItemsSkippedInvalidKms")
    totalItemsSkippedPermissionDenied = field("totalItemsSkippedPermissionDenied")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalConfiguration:
    boto3_raw_data: "type_defs.RetrievalConfigurationTypeDef" = dataclasses.field()

    retrievalMode = field("retrievalMode")
    externalId = field("externalId")
    roleName = field("roleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrievalConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevealConfiguration:
    boto3_raw_data: "type_defs.RevealConfigurationTypeDef" = dataclasses.field()

    status = field("status")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevealConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevealConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSensitiveDataOccurrencesAvailabilityRequest:
    boto3_raw_data: (
        "type_defs.GetSensitiveDataOccurrencesAvailabilityRequestTypeDef"
    ) = dataclasses.field()

    findingId = field("findingId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSensitiveDataOccurrencesAvailabilityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetSensitiveDataOccurrencesAvailabilityRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSensitiveDataOccurrencesRequest:
    boto3_raw_data: "type_defs.GetSensitiveDataOccurrencesRequestTypeDef" = (
        dataclasses.field()
    )

    findingId = field("findingId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSensitiveDataOccurrencesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSensitiveDataOccurrencesRequestTypeDef"]
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
class GetSensitivityInspectionTemplateRequest:
    boto3_raw_data: "type_defs.GetSensitivityInspectionTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSensitivityInspectionTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSensitivityInspectionTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SensitivityInspectionTemplateExcludesOutput:
    boto3_raw_data: "type_defs.SensitivityInspectionTemplateExcludesOutputTypeDef" = (
        dataclasses.field()
    )

    managedDataIdentifierIds = field("managedDataIdentifierIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SensitivityInspectionTemplateExcludesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SensitivityInspectionTemplateExcludesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SensitivityInspectionTemplateIncludesOutput:
    boto3_raw_data: "type_defs.SensitivityInspectionTemplateIncludesOutputTypeDef" = (
        dataclasses.field()
    )

    allowListIds = field("allowListIds")
    customDataIdentifierIds = field("customDataIdentifierIds")
    managedDataIdentifierIds = field("managedDataIdentifierIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SensitivityInspectionTemplateIncludesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SensitivityInspectionTemplateIncludesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageStatisticsFilter:
    boto3_raw_data: "type_defs.UsageStatisticsFilterTypeDef" = dataclasses.field()

    comparator = field("comparator")
    key = field("key")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageStatisticsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageStatisticsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageStatisticsSortBy:
    boto3_raw_data: "type_defs.UsageStatisticsSortByTypeDef" = dataclasses.field()

    key = field("key")
    orderBy = field("orderBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageStatisticsSortByTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageStatisticsSortByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageTotalsRequest:
    boto3_raw_data: "type_defs.GetUsageTotalsRequestTypeDef" = dataclasses.field()

    timeRange = field("timeRange")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsageTotalsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageTotalsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageTotal:
    boto3_raw_data: "type_defs.UsageTotalTypeDef" = dataclasses.field()

    currency = field("currency")
    estimatedCost = field("estimatedCost")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageTotalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageTotalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamUser:
    boto3_raw_data: "type_defs.IamUserTypeDef" = dataclasses.field()

    accountId = field("accountId")
    arn = field("arn")
    principalId = field("principalId")
    userName = field("userName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IamUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IamUserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpCity:
    boto3_raw_data: "type_defs.IpCityTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpCityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpCityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpCountry:
    boto3_raw_data: "type_defs.IpCountryTypeDef" = dataclasses.field()

    code = field("code")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpCountryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpCountryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpGeoLocation:
    boto3_raw_data: "type_defs.IpGeoLocationTypeDef" = dataclasses.field()

    lat = field("lat")
    lon = field("lon")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpGeoLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpGeoLocationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpOwner:
    boto3_raw_data: "type_defs.IpOwnerTypeDef" = dataclasses.field()

    asn = field("asn")
    asnOrg = field("asnOrg")
    isp = field("isp")
    org = field("org")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpOwnerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpOwnerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonthlySchedule:
    boto3_raw_data: "type_defs.MonthlyScheduleTypeDef" = dataclasses.field()

    dayOfMonth = field("dayOfMonth")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonthlyScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonthlyScheduleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WeeklySchedule:
    boto3_raw_data: "type_defs.WeeklyScheduleTypeDef" = dataclasses.field()

    dayOfWeek = field("dayOfWeek")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WeeklyScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WeeklyScheduleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimpleScopeTermOutput:
    boto3_raw_data: "type_defs.SimpleScopeTermOutputTypeDef" = dataclasses.field()

    comparator = field("comparator")
    key = field("key")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SimpleScopeTermOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SimpleScopeTermOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SimpleScopeTerm:
    boto3_raw_data: "type_defs.SimpleScopeTermTypeDef" = dataclasses.field()

    comparator = field("comparator")
    key = field("key")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SimpleScopeTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SimpleScopeTermTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketDefinitionForJobOutput:
    boto3_raw_data: "type_defs.S3BucketDefinitionForJobOutputTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    buckets = field("buckets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3BucketDefinitionForJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketDefinitionForJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAllowListsRequest:
    boto3_raw_data: "type_defs.ListAllowListsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAllowListsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAllowListsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedDiscoveryAccountsRequest:
    boto3_raw_data: "type_defs.ListAutomatedDiscoveryAccountsRequestTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedDiscoveryAccountsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutomatedDiscoveryAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsSortCriteria:
    boto3_raw_data: "type_defs.ListJobsSortCriteriaTypeDef" = dataclasses.field()

    attributeName = field("attributeName")
    orderBy = field("orderBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsSortCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsSortCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClassificationScopesRequest:
    boto3_raw_data: "type_defs.ListClassificationScopesRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListClassificationScopesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClassificationScopesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomDataIdentifiersRequest:
    boto3_raw_data: "type_defs.ListCustomDataIdentifiersRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCustomDataIdentifiersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomDataIdentifiersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsFiltersRequest:
    boto3_raw_data: "type_defs.ListFindingsFiltersRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsFiltersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsFiltersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvitationsRequest:
    boto3_raw_data: "type_defs.ListInvitationsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvitationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvitationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsFilterTerm:
    boto3_raw_data: "type_defs.ListJobsFilterTermTypeDef" = dataclasses.field()

    comparator = field("comparator")
    key = field("key")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsFilterTermTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsFilterTermTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedDataIdentifiersRequest:
    boto3_raw_data: "type_defs.ListManagedDataIdentifiersRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedDataIdentifiersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedDataIdentifiersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedDataIdentifierSummary:
    boto3_raw_data: "type_defs.ManagedDataIdentifierSummaryTypeDef" = (
        dataclasses.field()
    )

    category = field("category")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedDataIdentifierSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedDataIdentifierSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersRequest:
    boto3_raw_data: "type_defs.ListMembersRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    onlyAssociated = field("onlyAssociated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Member:
    boto3_raw_data: "type_defs.MemberTypeDef" = dataclasses.field()

    accountId = field("accountId")
    administratorAccountId = field("administratorAccountId")
    arn = field("arn")
    email = field("email")
    invitedAt = field("invitedAt")
    masterAccountId = field("masterAccountId")
    relationshipStatus = field("relationshipStatus")
    tags = field("tags")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationAdminAccountsRequest:
    boto3_raw_data: "type_defs.ListOrganizationAdminAccountsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationAdminAccountsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationAdminAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceProfileArtifactsRequest:
    boto3_raw_data: "type_defs.ListResourceProfileArtifactsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceProfileArtifactsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceProfileArtifactsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceProfileArtifact:
    boto3_raw_data: "type_defs.ResourceProfileArtifactTypeDef" = dataclasses.field()

    arn = field("arn")
    classificationResultStatus = field("classificationResultStatus")
    sensitive = field("sensitive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceProfileArtifactTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceProfileArtifactTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceProfileDetectionsRequest:
    boto3_raw_data: "type_defs.ListResourceProfileDetectionsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceProfileDetectionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceProfileDetectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSensitivityInspectionTemplatesRequest:
    boto3_raw_data: "type_defs.ListSensitivityInspectionTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSensitivityInspectionTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSensitivityInspectionTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SensitivityInspectionTemplatesEntry:
    boto3_raw_data: "type_defs.SensitivityInspectionTemplatesEntryTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SensitivityInspectionTemplatesEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SensitivityInspectionTemplatesEntryTypeDef"]
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
class Range:
    boto3_raw_data: "type_defs.RangeTypeDef" = dataclasses.field()

    end = field("end")
    start = field("start")
    startColumn = field("startColumn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Record:
    boto3_raw_data: "type_defs.RecordTypeDef" = dataclasses.field()

    jsonPath = field("jsonPath")
    recordIndex = field("recordIndex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketDefinitionForJob:
    boto3_raw_data: "type_defs.S3BucketDefinitionForJobTypeDef" = dataclasses.field()

    accountId = field("accountId")
    buckets = field("buckets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BucketDefinitionForJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketDefinitionForJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketOwner:
    boto3_raw_data: "type_defs.S3BucketOwnerTypeDef" = dataclasses.field()

    displayName = field("displayName")
    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3BucketOwnerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3BucketOwnerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSideEncryption:
    boto3_raw_data: "type_defs.ServerSideEncryptionTypeDef" = dataclasses.field()

    encryptionType = field("encryptionType")
    kmsMasterKeyId = field("kmsMasterKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerSideEncryptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerSideEncryptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ClassificationScopeExclusion:
    boto3_raw_data: "type_defs.S3ClassificationScopeExclusionTypeDef" = (
        dataclasses.field()
    )

    bucketNames = field("bucketNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3ClassificationScopeExclusionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ClassificationScopeExclusionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ClassificationScopeExclusionUpdate:
    boto3_raw_data: "type_defs.S3ClassificationScopeExclusionUpdateTypeDef" = (
        dataclasses.field()
    )

    bucketNames = field("bucketNames")
    operation = field("operation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3ClassificationScopeExclusionUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ClassificationScopeExclusionUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesSimpleCriterion:
    boto3_raw_data: "type_defs.SearchResourcesSimpleCriterionTypeDef" = (
        dataclasses.field()
    )

    comparator = field("comparator")
    key = field("key")
    values = field("values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchResourcesSimpleCriterionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesSimpleCriterionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesSortCriteria:
    boto3_raw_data: "type_defs.SearchResourcesSortCriteriaTypeDef" = dataclasses.field()

    attributeName = field("attributeName")
    orderBy = field("orderBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchResourcesSortCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesSortCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesTagCriterionPair:
    boto3_raw_data: "type_defs.SearchResourcesTagCriterionPairTypeDef" = (
        dataclasses.field()
    )

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchResourcesTagCriterionPairTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesTagCriterionPairTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SensitivityInspectionTemplateExcludes:
    boto3_raw_data: "type_defs.SensitivityInspectionTemplateExcludesTypeDef" = (
        dataclasses.field()
    )

    managedDataIdentifierIds = field("managedDataIdentifierIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SensitivityInspectionTemplateExcludesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SensitivityInspectionTemplateExcludesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SensitivityInspectionTemplateIncludes:
    boto3_raw_data: "type_defs.SensitivityInspectionTemplateIncludesTypeDef" = (
        dataclasses.field()
    )

    allowListIds = field("allowListIds")
    customDataIdentifierIds = field("customDataIdentifierIds")
    managedDataIdentifierIds = field("managedDataIdentifierIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SensitivityInspectionTemplateIncludesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SensitivityInspectionTemplateIncludesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceLimit:
    boto3_raw_data: "type_defs.ServiceLimitTypeDef" = dataclasses.field()

    isServiceLimited = field("isServiceLimited")
    unit = field("unit")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceLimitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionContextAttributes:
    boto3_raw_data: "type_defs.SessionContextAttributesTypeDef" = dataclasses.field()

    creationDate = field("creationDate")
    mfaAuthenticated = field("mfaAuthenticated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionContextAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionContextAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionIssuer:
    boto3_raw_data: "type_defs.SessionIssuerTypeDef" = dataclasses.field()

    accountId = field("accountId")
    arn = field("arn")
    principalId = field("principalId")
    type = field("type")
    userName = field("userName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionIssuerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionIssuerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuppressDataIdentifier:
    boto3_raw_data: "type_defs.SuppressDataIdentifierTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuppressDataIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuppressDataIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagCriterionPairForJob:
    boto3_raw_data: "type_defs.TagCriterionPairForJobTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagCriterionPairForJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagCriterionPairForJobTypeDef"]
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
class TagValuePair:
    boto3_raw_data: "type_defs.TagValuePairTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagValuePairTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagValuePairTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestCustomDataIdentifierRequest:
    boto3_raw_data: "type_defs.TestCustomDataIdentifierRequestTypeDef" = (
        dataclasses.field()
    )

    regex = field("regex")
    sampleText = field("sampleText")
    ignoreWords = field("ignoreWords")
    keywords = field("keywords")
    maximumMatchDistance = field("maximumMatchDistance")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TestCustomDataIdentifierRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestCustomDataIdentifierRequestTypeDef"]
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
class UpdateAutomatedDiscoveryConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateAutomatedDiscoveryConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    autoEnableOrganizationMembers = field("autoEnableOrganizationMembers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAutomatedDiscoveryConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAutomatedDiscoveryConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClassificationJobRequest:
    boto3_raw_data: "type_defs.UpdateClassificationJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobId = field("jobId")
    jobStatus = field("jobStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateClassificationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClassificationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMacieSessionRequest:
    boto3_raw_data: "type_defs.UpdateMacieSessionRequestTypeDef" = dataclasses.field()

    findingPublishingFrequency = field("findingPublishingFrequency")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMacieSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMacieSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMemberSessionRequest:
    boto3_raw_data: "type_defs.UpdateMemberSessionRequestTypeDef" = dataclasses.field()

    id = field("id")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMemberSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMemberSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOrganizationConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateOrganizationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    autoEnable = field("autoEnable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOrganizationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOrganizationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceProfileRequest:
    boto3_raw_data: "type_defs.UpdateResourceProfileRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    sensitivityScoreOverride = field("sensitivityScoreOverride")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResourceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRetrievalConfiguration:
    boto3_raw_data: "type_defs.UpdateRetrievalConfigurationTypeDef" = (
        dataclasses.field()
    )

    retrievalMode = field("retrievalMode")
    roleName = field("roleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRetrievalConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRetrievalConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserIdentityRoot:
    boto3_raw_data: "type_defs.UserIdentityRootTypeDef" = dataclasses.field()

    accountId = field("accountId")
    arn = field("arn")
    principalId = field("principalId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserIdentityRootTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserIdentityRootTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMemberRequest:
    boto3_raw_data: "type_defs.CreateMemberRequestTypeDef" = dataclasses.field()

    @cached_property
    def account(self):  # pragma: no cover
        return AccountDetail.make_one(self.boto3_raw_data["account"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMemberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMemberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountLevelPermissions:
    boto3_raw_data: "type_defs.AccountLevelPermissionsTypeDef" = dataclasses.field()

    @cached_property
    def blockPublicAccess(self):  # pragma: no cover
        return BlockPublicAccess.make_one(self.boto3_raw_data["blockPublicAccess"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountLevelPermissionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountLevelPermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowListCriteria:
    boto3_raw_data: "type_defs.AllowListCriteriaTypeDef" = dataclasses.field()

    regex = field("regex")

    @cached_property
    def s3WordsList(self):  # pragma: no cover
        return S3WordsList.make_one(self.boto3_raw_data["s3WordsList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AllowListCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowListCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingAction:
    boto3_raw_data: "type_defs.FindingActionTypeDef" = dataclasses.field()

    actionType = field("actionType")

    @cached_property
    def apiCallDetails(self):  # pragma: no cover
        return ApiCallDetails.make_one(self.boto3_raw_data["apiCallDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateAutomatedDiscoveryAccountsRequest:
    boto3_raw_data: "type_defs.BatchUpdateAutomatedDiscoveryAccountsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accounts(self):  # pragma: no cover
        return AutomatedDiscoveryAccountUpdate.make_many(
            self.boto3_raw_data["accounts"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateAutomatedDiscoveryAccountsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateAutomatedDiscoveryAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCustomDataIdentifiersResponse:
    boto3_raw_data: "type_defs.BatchGetCustomDataIdentifiersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def customDataIdentifiers(self):  # pragma: no cover
        return BatchGetCustomDataIdentifierSummary.make_many(
            self.boto3_raw_data["customDataIdentifiers"]
        )

    notFoundIdentifierIds = field("notFoundIdentifierIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetCustomDataIdentifiersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCustomDataIdentifiersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateAutomatedDiscoveryAccountsResponse:
    boto3_raw_data: "type_defs.BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return AutomatedDiscoveryAccountUpdateError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAllowListResponse:
    boto3_raw_data: "type_defs.CreateAllowListResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAllowListResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAllowListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClassificationJobResponse:
    boto3_raw_data: "type_defs.CreateClassificationJobResponseTypeDef" = (
        dataclasses.field()
    )

    jobArn = field("jobArn")
    jobId = field("jobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateClassificationJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClassificationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomDataIdentifierResponse:
    boto3_raw_data: "type_defs.CreateCustomDataIdentifierResponseTypeDef" = (
        dataclasses.field()
    )

    customDataIdentifierId = field("customDataIdentifierId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomDataIdentifierResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomDataIdentifierResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFindingsFilterResponse:
    boto3_raw_data: "type_defs.CreateFindingsFilterResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFindingsFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFindingsFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMemberResponse:
    boto3_raw_data: "type_defs.CreateMemberResponseTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMemberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMemberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeOrganizationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    autoEnable = field("autoEnable")
    maxAccountLimitReached = field("maxAccountLimitReached")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedDiscoveryConfigurationResponse:
    boto3_raw_data: "type_defs.GetAutomatedDiscoveryConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    autoEnableOrganizationMembers = field("autoEnableOrganizationMembers")
    classificationScopeId = field("classificationScopeId")
    disabledAt = field("disabledAt")
    firstEnabledAt = field("firstEnabledAt")
    lastUpdatedAt = field("lastUpdatedAt")
    sensitivityInspectionTemplateId = field("sensitivityInspectionTemplateId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedDiscoveryConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutomatedDiscoveryConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvitationsCountResponse:
    boto3_raw_data: "type_defs.GetInvitationsCountResponseTypeDef" = dataclasses.field()

    invitationsCount = field("invitationsCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInvitationsCountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvitationsCountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMacieSessionResponse:
    boto3_raw_data: "type_defs.GetMacieSessionResponseTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    findingPublishingFrequency = field("findingPublishingFrequency")
    serviceRole = field("serviceRole")
    status = field("status")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMacieSessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMacieSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemberResponse:
    boto3_raw_data: "type_defs.GetMemberResponseTypeDef" = dataclasses.field()

    accountId = field("accountId")
    administratorAccountId = field("administratorAccountId")
    arn = field("arn")
    email = field("email")
    invitedAt = field("invitedAt")
    masterAccountId = field("masterAccountId")
    relationshipStatus = field("relationshipStatus")
    tags = field("tags")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMemberResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMemberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSensitiveDataOccurrencesAvailabilityResponse:
    boto3_raw_data: (
        "type_defs.GetSensitiveDataOccurrencesAvailabilityResponseTypeDef"
    ) = dataclasses.field()

    code = field("code")
    reasons = field("reasons")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSensitiveDataOccurrencesAvailabilityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetSensitiveDataOccurrencesAvailabilityResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAllowListsResponse:
    boto3_raw_data: "type_defs.ListAllowListsResponseTypeDef" = dataclasses.field()

    @cached_property
    def allowLists(self):  # pragma: no cover
        return AllowListSummary.make_many(self.boto3_raw_data["allowLists"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAllowListsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAllowListsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedDiscoveryAccountsResponse:
    boto3_raw_data: "type_defs.ListAutomatedDiscoveryAccountsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return AutomatedDiscoveryAccount.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedDiscoveryAccountsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutomatedDiscoveryAccountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsResponse:
    boto3_raw_data: "type_defs.ListFindingsResponseTypeDef" = dataclasses.field()

    findingIds = field("findingIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationAdminAccountsResponse:
    boto3_raw_data: "type_defs.ListOrganizationAdminAccountsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def adminAccounts(self):  # pragma: no cover
        return AdminAccount.make_many(self.boto3_raw_data["adminAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationAdminAccountsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationAdminAccountsResponseTypeDef"]
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
class TestCustomDataIdentifierResponse:
    boto3_raw_data: "type_defs.TestCustomDataIdentifierResponseTypeDef" = (
        dataclasses.field()
    )

    matchCount = field("matchCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TestCustomDataIdentifierResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestCustomDataIdentifierResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAllowListResponse:
    boto3_raw_data: "type_defs.UpdateAllowListResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAllowListResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAllowListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFindingsFilterResponse:
    boto3_raw_data: "type_defs.UpdateFindingsFilterResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFindingsFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFindingsFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketLevelPermissions:
    boto3_raw_data: "type_defs.BucketLevelPermissionsTypeDef" = dataclasses.field()

    @cached_property
    def accessControlList(self):  # pragma: no cover
        return AccessControlList.make_one(self.boto3_raw_data["accessControlList"])

    @cached_property
    def blockPublicAccess(self):  # pragma: no cover
        return BlockPublicAccess.make_one(self.boto3_raw_data["blockPublicAccess"])

    @cached_property
    def bucketPolicy(self):  # pragma: no cover
        return BucketPolicy.make_one(self.boto3_raw_data["bucketPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketLevelPermissionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketLevelPermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchingBucket:
    boto3_raw_data: "type_defs.MatchingBucketTypeDef" = dataclasses.field()

    accountId = field("accountId")
    automatedDiscoveryMonitoringStatus = field("automatedDiscoveryMonitoringStatus")
    bucketName = field("bucketName")
    classifiableObjectCount = field("classifiableObjectCount")
    classifiableSizeInBytes = field("classifiableSizeInBytes")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @cached_property
    def jobDetails(self):  # pragma: no cover
        return JobDetails.make_one(self.boto3_raw_data["jobDetails"])

    lastAutomatedDiscoveryTime = field("lastAutomatedDiscoveryTime")
    objectCount = field("objectCount")

    @cached_property
    def objectCountByEncryptionType(self):  # pragma: no cover
        return ObjectCountByEncryptionType.make_one(
            self.boto3_raw_data["objectCountByEncryptionType"]
        )

    sensitivityScore = field("sensitivityScore")
    sizeInBytes = field("sizeInBytes")
    sizeInBytesCompressed = field("sizeInBytesCompressed")

    @cached_property
    def unclassifiableObjectCount(self):  # pragma: no cover
        return ObjectLevelStatistics.make_one(
            self.boto3_raw_data["unclassifiableObjectCount"]
        )

    @cached_property
    def unclassifiableObjectSizeInBytes(self):  # pragma: no cover
        return ObjectLevelStatistics.make_one(
            self.boto3_raw_data["unclassifiableObjectSizeInBytes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchingBucketTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchingBucketTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBucketsRequest:
    boto3_raw_data: "type_defs.DescribeBucketsRequestTypeDef" = dataclasses.field()

    criteria = field("criteria")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def sortCriteria(self):  # pragma: no cover
        return BucketSortCriteria.make_one(self.boto3_raw_data["sortCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBucketsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBucketsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketStatisticsBySensitivity:
    boto3_raw_data: "type_defs.BucketStatisticsBySensitivityTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def classificationError(self):  # pragma: no cover
        return SensitivityAggregations.make_one(
            self.boto3_raw_data["classificationError"]
        )

    @cached_property
    def notClassified(self):  # pragma: no cover
        return SensitivityAggregations.make_one(self.boto3_raw_data["notClassified"])

    @cached_property
    def notSensitive(self):  # pragma: no cover
        return SensitivityAggregations.make_one(self.boto3_raw_data["notSensitive"])

    @cached_property
    def sensitive(self):  # pragma: no cover
        return SensitivityAggregations.make_one(self.boto3_raw_data["sensitive"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BucketStatisticsBySensitivityTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketStatisticsBySensitivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClassificationExportConfiguration:
    boto3_raw_data: "type_defs.ClassificationExportConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["s3Destination"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ClassificationExportConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClassificationExportConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClassificationScopesResponse:
    boto3_raw_data: "type_defs.ListClassificationScopesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def classificationScopes(self):  # pragma: no cover
        return ClassificationScopeSummary.make_many(
            self.boto3_raw_data["classificationScopes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListClassificationScopesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClassificationScopesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomDataIdentifierRequest:
    boto3_raw_data: "type_defs.CreateCustomDataIdentifierRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    regex = field("regex")
    clientToken = field("clientToken")
    description = field("description")
    ignoreWords = field("ignoreWords")
    keywords = field("keywords")
    maximumMatchDistance = field("maximumMatchDistance")

    @cached_property
    def severityLevels(self):  # pragma: no cover
        return SeverityLevel.make_many(self.boto3_raw_data["severityLevels"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomDataIdentifierRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomDataIdentifierRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomDataIdentifierResponse:
    boto3_raw_data: "type_defs.GetCustomDataIdentifierResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createdAt = field("createdAt")
    deleted = field("deleted")
    description = field("description")
    id = field("id")
    ignoreWords = field("ignoreWords")
    keywords = field("keywords")
    maximumMatchDistance = field("maximumMatchDistance")
    name = field("name")
    regex = field("regex")

    @cached_property
    def severityLevels(self):  # pragma: no cover
        return SeverityLevel.make_many(self.boto3_raw_data["severityLevels"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCustomDataIdentifierResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomDataIdentifierResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInvitationsResponse:
    boto3_raw_data: "type_defs.CreateInvitationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def unprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["unprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInvitationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInvitationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeclineInvitationsResponse:
    boto3_raw_data: "type_defs.DeclineInvitationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def unprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["unprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeclineInvitationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeclineInvitationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInvitationsResponse:
    boto3_raw_data: "type_defs.DeleteInvitationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def unprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["unprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInvitationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInvitationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingCriteriaOutput:
    boto3_raw_data: "type_defs.FindingCriteriaOutputTypeDef" = dataclasses.field()

    criterion = field("criterion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FindingCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingCriteria:
    boto3_raw_data: "type_defs.FindingCriteriaTypeDef" = dataclasses.field()

    criterion = field("criterion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomDataIdentifiersResponse:
    boto3_raw_data: "type_defs.ListCustomDataIdentifiersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return CustomDataIdentifierSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomDataIdentifiersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomDataIdentifiersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBucketsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeBucketsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    criteria = field("criteria")

    @cached_property
    def sortCriteria(self):  # pragma: no cover
        return BucketSortCriteria.make_one(self.boto3_raw_data["sortCriteria"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBucketsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBucketsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAllowListsRequestPaginate:
    boto3_raw_data: "type_defs.ListAllowListsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAllowListsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAllowListsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedDiscoveryAccountsRequestPaginate:
    boto3_raw_data: "type_defs.ListAutomatedDiscoveryAccountsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedDiscoveryAccountsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutomatedDiscoveryAccountsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClassificationScopesRequestPaginate:
    boto3_raw_data: "type_defs.ListClassificationScopesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListClassificationScopesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClassificationScopesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomDataIdentifiersRequestPaginate:
    boto3_raw_data: "type_defs.ListCustomDataIdentifiersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomDataIdentifiersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomDataIdentifiersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsFiltersRequestPaginate:
    boto3_raw_data: "type_defs.ListFindingsFiltersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFindingsFiltersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsFiltersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvitationsRequestPaginate:
    boto3_raw_data: "type_defs.ListInvitationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInvitationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvitationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedDataIdentifiersRequestPaginate:
    boto3_raw_data: "type_defs.ListManagedDataIdentifiersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedDataIdentifiersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedDataIdentifiersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersRequestPaginate:
    boto3_raw_data: "type_defs.ListMembersRequestPaginateTypeDef" = dataclasses.field()

    onlyAssociated = field("onlyAssociated")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationAdminAccountsRequestPaginate:
    boto3_raw_data: "type_defs.ListOrganizationAdminAccountsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationAdminAccountsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationAdminAccountsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceProfileArtifactsRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceProfileArtifactsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceProfileArtifactsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceProfileArtifactsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceProfileDetectionsRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceProfileDetectionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceProfileDetectionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceProfileDetectionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSensitivityInspectionTemplatesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListSensitivityInspectionTemplatesRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSensitivityInspectionTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListSensitivityInspectionTemplatesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSensitiveDataOccurrencesResponse:
    boto3_raw_data: "type_defs.GetSensitiveDataOccurrencesResponseTypeDef" = (
        dataclasses.field()
    )

    error = field("error")
    sensitiveDataOccurrences = field("sensitiveDataOccurrences")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSensitiveDataOccurrencesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSensitiveDataOccurrencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceProfileDetectionsResponse:
    boto3_raw_data: "type_defs.ListResourceProfileDetectionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def detections(self):  # pragma: no cover
        return Detection.make_many(self.boto3_raw_data["detections"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceProfileDetectionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceProfileDetectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsFiltersResponse:
    boto3_raw_data: "type_defs.ListFindingsFiltersResponseTypeDef" = dataclasses.field()

    @cached_property
    def findingsFilterListItems(self):  # pragma: no cover
        return FindingsFilterListItem.make_many(
            self.boto3_raw_data["findingsFilterListItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsFiltersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsFiltersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAdministratorAccountResponse:
    boto3_raw_data: "type_defs.GetAdministratorAccountResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def administrator(self):  # pragma: no cover
        return Invitation.make_one(self.boto3_raw_data["administrator"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAdministratorAccountResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdministratorAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMasterAccountResponse:
    boto3_raw_data: "type_defs.GetMasterAccountResponseTypeDef" = dataclasses.field()

    @cached_property
    def master(self):  # pragma: no cover
        return Invitation.make_one(self.boto3_raw_data["master"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMasterAccountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMasterAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvitationsResponse:
    boto3_raw_data: "type_defs.ListInvitationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def invitations(self):  # pragma: no cover
        return Invitation.make_many(self.boto3_raw_data["invitations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvitationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvitationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingStatisticsResponse:
    boto3_raw_data: "type_defs.GetFindingStatisticsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def countsByGroup(self):  # pragma: no cover
        return GroupCount.make_many(self.boto3_raw_data["countsByGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingStatisticsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsPublicationConfigurationResponse:
    boto3_raw_data: "type_defs.GetFindingsPublicationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityHubConfiguration(self):  # pragma: no cover
        return SecurityHubConfiguration.make_one(
            self.boto3_raw_data["securityHubConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFindingsPublicationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsPublicationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutFindingsPublicationConfigurationRequest:
    boto3_raw_data: "type_defs.PutFindingsPublicationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    clientToken = field("clientToken")

    @cached_property
    def securityHubConfiguration(self):  # pragma: no cover
        return SecurityHubConfiguration.make_one(
            self.boto3_raw_data["securityHubConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutFindingsPublicationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutFindingsPublicationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsRequest:
    boto3_raw_data: "type_defs.GetFindingsRequestTypeDef" = dataclasses.field()

    findingIds = field("findingIds")

    @cached_property
    def sortCriteria(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["sortCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceProfileResponse:
    boto3_raw_data: "type_defs.GetResourceProfileResponseTypeDef" = dataclasses.field()

    profileUpdatedAt = field("profileUpdatedAt")
    sensitivityScore = field("sensitivityScore")
    sensitivityScoreOverridden = field("sensitivityScoreOverridden")

    @cached_property
    def statistics(self):  # pragma: no cover
        return ResourceStatistics.make_one(self.boto3_raw_data["statistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRevealConfigurationResponse:
    boto3_raw_data: "type_defs.GetRevealConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return RevealConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def retrievalConfiguration(self):  # pragma: no cover
        return RetrievalConfiguration.make_one(
            self.boto3_raw_data["retrievalConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRevealConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRevealConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRevealConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateRevealConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return RevealConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def retrievalConfiguration(self):  # pragma: no cover
        return RetrievalConfiguration.make_one(
            self.boto3_raw_data["retrievalConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateRevealConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRevealConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSensitiveDataOccurrencesRequestWait:
    boto3_raw_data: "type_defs.GetSensitiveDataOccurrencesRequestWaitTypeDef" = (
        dataclasses.field()
    )

    findingId = field("findingId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSensitiveDataOccurrencesRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSensitiveDataOccurrencesRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSensitivityInspectionTemplateResponse:
    boto3_raw_data: "type_defs.GetSensitivityInspectionTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    description = field("description")

    @cached_property
    def excludes(self):  # pragma: no cover
        return SensitivityInspectionTemplateExcludesOutput.make_one(
            self.boto3_raw_data["excludes"]
        )

    @cached_property
    def includes(self):  # pragma: no cover
        return SensitivityInspectionTemplateIncludesOutput.make_one(
            self.boto3_raw_data["includes"]
        )

    name = field("name")
    sensitivityInspectionTemplateId = field("sensitivityInspectionTemplateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSensitivityInspectionTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSensitivityInspectionTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageStatisticsRequestPaginate:
    boto3_raw_data: "type_defs.GetUsageStatisticsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterBy(self):  # pragma: no cover
        return UsageStatisticsFilter.make_many(self.boto3_raw_data["filterBy"])

    @cached_property
    def sortBy(self):  # pragma: no cover
        return UsageStatisticsSortBy.make_one(self.boto3_raw_data["sortBy"])

    timeRange = field("timeRange")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetUsageStatisticsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageStatisticsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageStatisticsRequest:
    boto3_raw_data: "type_defs.GetUsageStatisticsRequestTypeDef" = dataclasses.field()

    @cached_property
    def filterBy(self):  # pragma: no cover
        return UsageStatisticsFilter.make_many(self.boto3_raw_data["filterBy"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return UsageStatisticsSortBy.make_one(self.boto3_raw_data["sortBy"])

    timeRange = field("timeRange")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsageStatisticsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageTotalsResponse:
    boto3_raw_data: "type_defs.GetUsageTotalsResponseTypeDef" = dataclasses.field()

    timeRange = field("timeRange")

    @cached_property
    def usageTotals(self):  # pragma: no cover
        return UsageTotal.make_many(self.boto3_raw_data["usageTotals"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsageTotalsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageTotalsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpAddressDetails:
    boto3_raw_data: "type_defs.IpAddressDetailsTypeDef" = dataclasses.field()

    ipAddressV4 = field("ipAddressV4")

    @cached_property
    def ipCity(self):  # pragma: no cover
        return IpCity.make_one(self.boto3_raw_data["ipCity"])

    @cached_property
    def ipCountry(self):  # pragma: no cover
        return IpCountry.make_one(self.boto3_raw_data["ipCountry"])

    @cached_property
    def ipGeoLocation(self):  # pragma: no cover
        return IpGeoLocation.make_one(self.boto3_raw_data["ipGeoLocation"])

    @cached_property
    def ipOwner(self):  # pragma: no cover
        return IpOwner.make_one(self.boto3_raw_data["ipOwner"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpAddressDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IpAddressDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobScheduleFrequencyOutput:
    boto3_raw_data: "type_defs.JobScheduleFrequencyOutputTypeDef" = dataclasses.field()

    dailySchedule = field("dailySchedule")

    @cached_property
    def monthlySchedule(self):  # pragma: no cover
        return MonthlySchedule.make_one(self.boto3_raw_data["monthlySchedule"])

    @cached_property
    def weeklySchedule(self):  # pragma: no cover
        return WeeklySchedule.make_one(self.boto3_raw_data["weeklySchedule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobScheduleFrequencyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobScheduleFrequencyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobScheduleFrequency:
    boto3_raw_data: "type_defs.JobScheduleFrequencyTypeDef" = dataclasses.field()

    dailySchedule = field("dailySchedule")

    @cached_property
    def monthlySchedule(self):  # pragma: no cover
        return MonthlySchedule.make_one(self.boto3_raw_data["monthlySchedule"])

    @cached_property
    def weeklySchedule(self):  # pragma: no cover
        return WeeklySchedule.make_one(self.boto3_raw_data["weeklySchedule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobScheduleFrequencyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobScheduleFrequencyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsFilterCriteria:
    boto3_raw_data: "type_defs.ListJobsFilterCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def excludes(self):  # pragma: no cover
        return ListJobsFilterTerm.make_many(self.boto3_raw_data["excludes"])

    @cached_property
    def includes(self):  # pragma: no cover
        return ListJobsFilterTerm.make_many(self.boto3_raw_data["includes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsFilterCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsFilterCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedDataIdentifiersResponse:
    boto3_raw_data: "type_defs.ListManagedDataIdentifiersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return ManagedDataIdentifierSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedDataIdentifiersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedDataIdentifiersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersResponse:
    boto3_raw_data: "type_defs.ListMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def members(self):  # pragma: no cover
        return Member.make_many(self.boto3_raw_data["members"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceProfileArtifactsResponse:
    boto3_raw_data: "type_defs.ListResourceProfileArtifactsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def artifacts(self):  # pragma: no cover
        return ResourceProfileArtifact.make_many(self.boto3_raw_data["artifacts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceProfileArtifactsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceProfileArtifactsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSensitivityInspectionTemplatesResponse:
    boto3_raw_data: "type_defs.ListSensitivityInspectionTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sensitivityInspectionTemplates(self):  # pragma: no cover
        return SensitivityInspectionTemplatesEntry.make_many(
            self.boto3_raw_data["sensitivityInspectionTemplates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSensitivityInspectionTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSensitivityInspectionTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Page:
    boto3_raw_data: "type_defs.PageTypeDef" = dataclasses.field()

    @cached_property
    def lineRange(self):  # pragma: no cover
        return Range.make_one(self.boto3_raw_data["lineRange"])

    @cached_property
    def offsetRange(self):  # pragma: no cover
        return Range.make_one(self.boto3_raw_data["offsetRange"])

    pageNumber = field("pageNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Object:
    boto3_raw_data: "type_defs.S3ObjectTypeDef" = dataclasses.field()

    bucketArn = field("bucketArn")
    eTag = field("eTag")
    extension = field("extension")
    key = field("key")
    lastModified = field("lastModified")
    path = field("path")
    publicAccess = field("publicAccess")

    @cached_property
    def serverSideEncryption(self):  # pragma: no cover
        return ServerSideEncryption.make_one(
            self.boto3_raw_data["serverSideEncryption"]
        )

    size = field("size")
    storageClass = field("storageClass")

    @cached_property
    def tags(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["tags"])

    versionId = field("versionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ClassificationScope:
    boto3_raw_data: "type_defs.S3ClassificationScopeTypeDef" = dataclasses.field()

    @cached_property
    def excludes(self):  # pragma: no cover
        return S3ClassificationScopeExclusion.make_one(self.boto3_raw_data["excludes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ClassificationScopeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ClassificationScopeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ClassificationScopeUpdate:
    boto3_raw_data: "type_defs.S3ClassificationScopeUpdateTypeDef" = dataclasses.field()

    @cached_property
    def excludes(self):  # pragma: no cover
        return S3ClassificationScopeExclusionUpdate.make_one(
            self.boto3_raw_data["excludes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ClassificationScopeUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ClassificationScopeUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesTagCriterion:
    boto3_raw_data: "type_defs.SearchResourcesTagCriterionTypeDef" = dataclasses.field()

    comparator = field("comparator")

    @cached_property
    def tagValues(self):  # pragma: no cover
        return SearchResourcesTagCriterionPair.make_many(
            self.boto3_raw_data["tagValues"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchResourcesTagCriterionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesTagCriterionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageByAccount:
    boto3_raw_data: "type_defs.UsageByAccountTypeDef" = dataclasses.field()

    currency = field("currency")
    estimatedCost = field("estimatedCost")

    @cached_property
    def serviceLimit(self):  # pragma: no cover
        return ServiceLimit.make_one(self.boto3_raw_data["serviceLimit"])

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageByAccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageByAccountTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionContext:
    boto3_raw_data: "type_defs.SessionContextTypeDef" = dataclasses.field()

    @cached_property
    def attributes(self):  # pragma: no cover
        return SessionContextAttributes.make_one(self.boto3_raw_data["attributes"])

    @cached_property
    def sessionIssuer(self):  # pragma: no cover
        return SessionIssuer.make_one(self.boto3_raw_data["sessionIssuer"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceProfileDetectionsRequest:
    boto3_raw_data: "type_defs.UpdateResourceProfileDetectionsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")

    @cached_property
    def suppressDataIdentifiers(self):  # pragma: no cover
        return SuppressDataIdentifier.make_many(
            self.boto3_raw_data["suppressDataIdentifiers"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateResourceProfileDetectionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceProfileDetectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagCriterionForJobOutput:
    boto3_raw_data: "type_defs.TagCriterionForJobOutputTypeDef" = dataclasses.field()

    comparator = field("comparator")

    @cached_property
    def tagValues(self):  # pragma: no cover
        return TagCriterionPairForJob.make_many(self.boto3_raw_data["tagValues"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagCriterionForJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagCriterionForJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagCriterionForJob:
    boto3_raw_data: "type_defs.TagCriterionForJobTypeDef" = dataclasses.field()

    comparator = field("comparator")

    @cached_property
    def tagValues(self):  # pragma: no cover
        return TagCriterionPairForJob.make_many(self.boto3_raw_data["tagValues"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagCriterionForJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagCriterionForJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagScopeTermOutput:
    boto3_raw_data: "type_defs.TagScopeTermOutputTypeDef" = dataclasses.field()

    comparator = field("comparator")
    key = field("key")

    @cached_property
    def tagValues(self):  # pragma: no cover
        return TagValuePair.make_many(self.boto3_raw_data["tagValues"])

    target = field("target")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagScopeTermOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagScopeTermOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagScopeTerm:
    boto3_raw_data: "type_defs.TagScopeTermTypeDef" = dataclasses.field()

    comparator = field("comparator")
    key = field("key")

    @cached_property
    def tagValues(self):  # pragma: no cover
        return TagValuePair.make_many(self.boto3_raw_data["tagValues"])

    target = field("target")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagScopeTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagScopeTermTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRevealConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateRevealConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return RevealConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def retrievalConfiguration(self):  # pragma: no cover
        return UpdateRetrievalConfiguration.make_one(
            self.boto3_raw_data["retrievalConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateRevealConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRevealConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAllowListRequest:
    boto3_raw_data: "type_defs.CreateAllowListRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")

    @cached_property
    def criteria(self):  # pragma: no cover
        return AllowListCriteria.make_one(self.boto3_raw_data["criteria"])

    name = field("name")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAllowListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAllowListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAllowListResponse:
    boto3_raw_data: "type_defs.GetAllowListResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")

    @cached_property
    def criteria(self):  # pragma: no cover
        return AllowListCriteria.make_one(self.boto3_raw_data["criteria"])

    description = field("description")
    id = field("id")
    name = field("name")

    @cached_property
    def status(self):  # pragma: no cover
        return AllowListStatus.make_one(self.boto3_raw_data["status"])

    tags = field("tags")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAllowListResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAllowListResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAllowListRequest:
    boto3_raw_data: "type_defs.UpdateAllowListRequestTypeDef" = dataclasses.field()

    @cached_property
    def criteria(self):  # pragma: no cover
        return AllowListCriteria.make_one(self.boto3_raw_data["criteria"])

    id = field("id")
    name = field("name")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAllowListRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAllowListRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketPermissionConfiguration:
    boto3_raw_data: "type_defs.BucketPermissionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accountLevelPermissions(self):  # pragma: no cover
        return AccountLevelPermissions.make_one(
            self.boto3_raw_data["accountLevelPermissions"]
        )

    @cached_property
    def bucketLevelPermissions(self):  # pragma: no cover
        return BucketLevelPermissions.make_one(
            self.boto3_raw_data["bucketLevelPermissions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BucketPermissionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketPermissionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchingResource:
    boto3_raw_data: "type_defs.MatchingResourceTypeDef" = dataclasses.field()

    @cached_property
    def matchingBucket(self):  # pragma: no cover
        return MatchingBucket.make_one(self.boto3_raw_data["matchingBucket"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchingResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchingResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketStatisticsResponse:
    boto3_raw_data: "type_defs.GetBucketStatisticsResponseTypeDef" = dataclasses.field()

    bucketCount = field("bucketCount")

    @cached_property
    def bucketCountByEffectivePermission(self):  # pragma: no cover
        return BucketCountByEffectivePermission.make_one(
            self.boto3_raw_data["bucketCountByEffectivePermission"]
        )

    @cached_property
    def bucketCountByEncryptionType(self):  # pragma: no cover
        return BucketCountByEncryptionType.make_one(
            self.boto3_raw_data["bucketCountByEncryptionType"]
        )

    @cached_property
    def bucketCountByObjectEncryptionRequirement(self):  # pragma: no cover
        return BucketCountPolicyAllowsUnencryptedObjectUploads.make_one(
            self.boto3_raw_data["bucketCountByObjectEncryptionRequirement"]
        )

    @cached_property
    def bucketCountBySharedAccessType(self):  # pragma: no cover
        return BucketCountBySharedAccessType.make_one(
            self.boto3_raw_data["bucketCountBySharedAccessType"]
        )

    @cached_property
    def bucketStatisticsBySensitivity(self):  # pragma: no cover
        return BucketStatisticsBySensitivity.make_one(
            self.boto3_raw_data["bucketStatisticsBySensitivity"]
        )

    classifiableObjectCount = field("classifiableObjectCount")
    classifiableSizeInBytes = field("classifiableSizeInBytes")
    lastUpdated = field("lastUpdated")
    objectCount = field("objectCount")
    sizeInBytes = field("sizeInBytes")
    sizeInBytesCompressed = field("sizeInBytesCompressed")

    @cached_property
    def unclassifiableObjectCount(self):  # pragma: no cover
        return ObjectLevelStatistics.make_one(
            self.boto3_raw_data["unclassifiableObjectCount"]
        )

    @cached_property
    def unclassifiableObjectSizeInBytes(self):  # pragma: no cover
        return ObjectLevelStatistics.make_one(
            self.boto3_raw_data["unclassifiableObjectSizeInBytes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketStatisticsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClassificationExportConfigurationResponse:
    boto3_raw_data: "type_defs.GetClassificationExportConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return ClassificationExportConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetClassificationExportConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClassificationExportConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutClassificationExportConfigurationRequest:
    boto3_raw_data: "type_defs.PutClassificationExportConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return ClassificationExportConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutClassificationExportConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutClassificationExportConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutClassificationExportConfigurationResponse:
    boto3_raw_data: "type_defs.PutClassificationExportConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuration(self):  # pragma: no cover
        return ClassificationExportConfiguration.make_one(
            self.boto3_raw_data["configuration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutClassificationExportConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutClassificationExportConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsFilterResponse:
    boto3_raw_data: "type_defs.GetFindingsFilterResponseTypeDef" = dataclasses.field()

    action = field("action")
    arn = field("arn")
    description = field("description")

    @cached_property
    def findingCriteria(self):  # pragma: no cover
        return FindingCriteriaOutput.make_one(self.boto3_raw_data["findingCriteria"])

    id = field("id")
    name = field("name")
    position = field("position")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingsFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClassificationJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListClassificationJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return ListJobsFilterCriteria.make_one(self.boto3_raw_data["filterCriteria"])

    @cached_property
    def sortCriteria(self):  # pragma: no cover
        return ListJobsSortCriteria.make_one(self.boto3_raw_data["sortCriteria"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListClassificationJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClassificationJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClassificationJobsRequest:
    boto3_raw_data: "type_defs.ListClassificationJobsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return ListJobsFilterCriteria.make_one(self.boto3_raw_data["filterCriteria"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def sortCriteria(self):  # pragma: no cover
        return ListJobsSortCriteria.make_one(self.boto3_raw_data["sortCriteria"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListClassificationJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClassificationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Occurrences:
    boto3_raw_data: "type_defs.OccurrencesTypeDef" = dataclasses.field()

    @cached_property
    def cells(self):  # pragma: no cover
        return Cell.make_many(self.boto3_raw_data["cells"])

    @cached_property
    def lineRanges(self):  # pragma: no cover
        return Range.make_many(self.boto3_raw_data["lineRanges"])

    @cached_property
    def offsetRanges(self):  # pragma: no cover
        return Range.make_many(self.boto3_raw_data["offsetRanges"])

    @cached_property
    def pages(self):  # pragma: no cover
        return Page.make_many(self.boto3_raw_data["pages"])

    @cached_property
    def records(self):  # pragma: no cover
        return Record.make_many(self.boto3_raw_data["records"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OccurrencesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OccurrencesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClassificationScopeResponse:
    boto3_raw_data: "type_defs.GetClassificationScopeResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")

    @cached_property
    def s3(self):  # pragma: no cover
        return S3ClassificationScope.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetClassificationScopeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClassificationScopeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClassificationScopeRequest:
    boto3_raw_data: "type_defs.UpdateClassificationScopeRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def s3(self):  # pragma: no cover
        return S3ClassificationScopeUpdate.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateClassificationScopeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClassificationScopeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesCriteria:
    boto3_raw_data: "type_defs.SearchResourcesCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def simpleCriterion(self):  # pragma: no cover
        return SearchResourcesSimpleCriterion.make_one(
            self.boto3_raw_data["simpleCriterion"]
        )

    @cached_property
    def tagCriterion(self):  # pragma: no cover
        return SearchResourcesTagCriterion.make_one(self.boto3_raw_data["tagCriterion"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchResourcesCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSensitivityInspectionTemplateRequest:
    boto3_raw_data: "type_defs.UpdateSensitivityInspectionTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    description = field("description")
    excludes = field("excludes")
    includes = field("includes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSensitivityInspectionTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSensitivityInspectionTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageRecord:
    boto3_raw_data: "type_defs.UsageRecordTypeDef" = dataclasses.field()

    accountId = field("accountId")
    automatedDiscoveryFreeTrialStartDate = field("automatedDiscoveryFreeTrialStartDate")
    freeTrialStartDate = field("freeTrialStartDate")

    @cached_property
    def usage(self):  # pragma: no cover
        return UsageByAccount.make_many(self.boto3_raw_data["usage"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageRecordTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumedRole:
    boto3_raw_data: "type_defs.AssumedRoleTypeDef" = dataclasses.field()

    accessKeyId = field("accessKeyId")
    accountId = field("accountId")
    arn = field("arn")
    principalId = field("principalId")

    @cached_property
    def sessionContext(self):  # pragma: no cover
        return SessionContext.make_one(self.boto3_raw_data["sessionContext"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssumedRoleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssumedRoleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FederatedUser:
    boto3_raw_data: "type_defs.FederatedUserTypeDef" = dataclasses.field()

    accessKeyId = field("accessKeyId")
    accountId = field("accountId")
    arn = field("arn")
    principalId = field("principalId")

    @cached_property
    def sessionContext(self):  # pragma: no cover
        return SessionContext.make_one(self.boto3_raw_data["sessionContext"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FederatedUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FederatedUserTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CriteriaForJobOutput:
    boto3_raw_data: "type_defs.CriteriaForJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def simpleCriterion(self):  # pragma: no cover
        return SimpleCriterionForJobOutput.make_one(
            self.boto3_raw_data["simpleCriterion"]
        )

    @cached_property
    def tagCriterion(self):  # pragma: no cover
        return TagCriterionForJobOutput.make_one(self.boto3_raw_data["tagCriterion"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CriteriaForJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CriteriaForJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CriteriaForJob:
    boto3_raw_data: "type_defs.CriteriaForJobTypeDef" = dataclasses.field()

    @cached_property
    def simpleCriterion(self):  # pragma: no cover
        return SimpleCriterionForJob.make_one(self.boto3_raw_data["simpleCriterion"])

    @cached_property
    def tagCriterion(self):  # pragma: no cover
        return TagCriterionForJob.make_one(self.boto3_raw_data["tagCriterion"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CriteriaForJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CriteriaForJobTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobScopeTermOutput:
    boto3_raw_data: "type_defs.JobScopeTermOutputTypeDef" = dataclasses.field()

    @cached_property
    def simpleScopeTerm(self):  # pragma: no cover
        return SimpleScopeTermOutput.make_one(self.boto3_raw_data["simpleScopeTerm"])

    @cached_property
    def tagScopeTerm(self):  # pragma: no cover
        return TagScopeTermOutput.make_one(self.boto3_raw_data["tagScopeTerm"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobScopeTermOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobScopeTermOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobScopeTerm:
    boto3_raw_data: "type_defs.JobScopeTermTypeDef" = dataclasses.field()

    @cached_property
    def simpleScopeTerm(self):  # pragma: no cover
        return SimpleScopeTerm.make_one(self.boto3_raw_data["simpleScopeTerm"])

    @cached_property
    def tagScopeTerm(self):  # pragma: no cover
        return TagScopeTerm.make_one(self.boto3_raw_data["tagScopeTerm"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobScopeTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobScopeTermTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketPublicAccess:
    boto3_raw_data: "type_defs.BucketPublicAccessTypeDef" = dataclasses.field()

    effectivePermission = field("effectivePermission")

    @cached_property
    def permissionConfiguration(self):  # pragma: no cover
        return BucketPermissionConfiguration.make_one(
            self.boto3_raw_data["permissionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BucketPublicAccessTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BucketPublicAccessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesResponse:
    boto3_raw_data: "type_defs.SearchResourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def matchingResources(self):  # pragma: no cover
        return MatchingResource.make_many(self.boto3_raw_data["matchingResources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchResourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFindingsFilterRequest:
    boto3_raw_data: "type_defs.CreateFindingsFilterRequestTypeDef" = dataclasses.field()

    action = field("action")
    findingCriteria = field("findingCriteria")
    name = field("name")
    clientToken = field("clientToken")
    description = field("description")
    position = field("position")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFindingsFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFindingsFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingStatisticsRequest:
    boto3_raw_data: "type_defs.GetFindingStatisticsRequestTypeDef" = dataclasses.field()

    groupBy = field("groupBy")
    findingCriteria = field("findingCriteria")
    size = field("size")

    @cached_property
    def sortCriteria(self):  # pragma: no cover
        return FindingStatisticsSortCriteria.make_one(
            self.boto3_raw_data["sortCriteria"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingStatisticsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsRequestPaginate:
    boto3_raw_data: "type_defs.ListFindingsRequestPaginateTypeDef" = dataclasses.field()

    findingCriteria = field("findingCriteria")

    @cached_property
    def sortCriteria(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["sortCriteria"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingsRequest:
    boto3_raw_data: "type_defs.ListFindingsRequestTypeDef" = dataclasses.field()

    findingCriteria = field("findingCriteria")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def sortCriteria(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["sortCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFindingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFindingsFilterRequest:
    boto3_raw_data: "type_defs.UpdateFindingsFilterRequestTypeDef" = dataclasses.field()

    id = field("id")
    action = field("action")
    clientToken = field("clientToken")
    description = field("description")
    findingCriteria = field("findingCriteria")
    name = field("name")
    position = field("position")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFindingsFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFindingsFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDetection:
    boto3_raw_data: "type_defs.CustomDetectionTypeDef" = dataclasses.field()

    arn = field("arn")
    count = field("count")
    name = field("name")

    @cached_property
    def occurrences(self):  # pragma: no cover
        return Occurrences.make_one(self.boto3_raw_data["occurrences"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomDetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomDetectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultDetection:
    boto3_raw_data: "type_defs.DefaultDetectionTypeDef" = dataclasses.field()

    count = field("count")

    @cached_property
    def occurrences(self):  # pragma: no cover
        return Occurrences.make_one(self.boto3_raw_data["occurrences"])

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DefaultDetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultDetectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesCriteriaBlock:
    boto3_raw_data: "type_defs.SearchResourcesCriteriaBlockTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def and_(self):  # pragma: no cover
        return SearchResourcesCriteria.make_many(self.boto3_raw_data["and"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchResourcesCriteriaBlockTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesCriteriaBlockTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUsageStatisticsResponse:
    boto3_raw_data: "type_defs.GetUsageStatisticsResponseTypeDef" = dataclasses.field()

    @cached_property
    def records(self):  # pragma: no cover
        return UsageRecord.make_many(self.boto3_raw_data["records"])

    timeRange = field("timeRange")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUsageStatisticsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUsageStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserIdentity:
    boto3_raw_data: "type_defs.UserIdentityTypeDef" = dataclasses.field()

    @cached_property
    def assumedRole(self):  # pragma: no cover
        return AssumedRole.make_one(self.boto3_raw_data["assumedRole"])

    @cached_property
    def awsAccount(self):  # pragma: no cover
        return AwsAccount.make_one(self.boto3_raw_data["awsAccount"])

    @cached_property
    def awsService(self):  # pragma: no cover
        return AwsService.make_one(self.boto3_raw_data["awsService"])

    @cached_property
    def federatedUser(self):  # pragma: no cover
        return FederatedUser.make_one(self.boto3_raw_data["federatedUser"])

    @cached_property
    def iamUser(self):  # pragma: no cover
        return IamUser.make_one(self.boto3_raw_data["iamUser"])

    @cached_property
    def root(self):  # pragma: no cover
        return UserIdentityRoot.make_one(self.boto3_raw_data["root"])

    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserIdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserIdentityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CriteriaBlockForJobOutput:
    boto3_raw_data: "type_defs.CriteriaBlockForJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def and_(self):  # pragma: no cover
        return CriteriaForJobOutput.make_many(self.boto3_raw_data["and"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CriteriaBlockForJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CriteriaBlockForJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CriteriaBlockForJob:
    boto3_raw_data: "type_defs.CriteriaBlockForJobTypeDef" = dataclasses.field()

    @cached_property
    def and_(self):  # pragma: no cover
        return CriteriaForJob.make_many(self.boto3_raw_data["and"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CriteriaBlockForJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CriteriaBlockForJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobScopingBlockOutput:
    boto3_raw_data: "type_defs.JobScopingBlockOutputTypeDef" = dataclasses.field()

    @cached_property
    def and_(self):  # pragma: no cover
        return JobScopeTermOutput.make_many(self.boto3_raw_data["and"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobScopingBlockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobScopingBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobScopingBlock:
    boto3_raw_data: "type_defs.JobScopingBlockTypeDef" = dataclasses.field()

    @cached_property
    def and_(self):  # pragma: no cover
        return JobScopeTerm.make_many(self.boto3_raw_data["and"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobScopingBlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobScopingBlockTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketMetadata:
    boto3_raw_data: "type_defs.BucketMetadataTypeDef" = dataclasses.field()

    accountId = field("accountId")
    allowsUnencryptedObjectUploads = field("allowsUnencryptedObjectUploads")
    automatedDiscoveryMonitoringStatus = field("automatedDiscoveryMonitoringStatus")
    bucketArn = field("bucketArn")
    bucketCreatedAt = field("bucketCreatedAt")
    bucketName = field("bucketName")
    classifiableObjectCount = field("classifiableObjectCount")
    classifiableSizeInBytes = field("classifiableSizeInBytes")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @cached_property
    def jobDetails(self):  # pragma: no cover
        return JobDetails.make_one(self.boto3_raw_data["jobDetails"])

    lastAutomatedDiscoveryTime = field("lastAutomatedDiscoveryTime")
    lastUpdated = field("lastUpdated")
    objectCount = field("objectCount")

    @cached_property
    def objectCountByEncryptionType(self):  # pragma: no cover
        return ObjectCountByEncryptionType.make_one(
            self.boto3_raw_data["objectCountByEncryptionType"]
        )

    @cached_property
    def publicAccess(self):  # pragma: no cover
        return BucketPublicAccess.make_one(self.boto3_raw_data["publicAccess"])

    region = field("region")

    @cached_property
    def replicationDetails(self):  # pragma: no cover
        return ReplicationDetails.make_one(self.boto3_raw_data["replicationDetails"])

    sensitivityScore = field("sensitivityScore")

    @cached_property
    def serverSideEncryption(self):  # pragma: no cover
        return BucketServerSideEncryption.make_one(
            self.boto3_raw_data["serverSideEncryption"]
        )

    sharedAccess = field("sharedAccess")
    sizeInBytes = field("sizeInBytes")
    sizeInBytesCompressed = field("sizeInBytesCompressed")

    @cached_property
    def tags(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def unclassifiableObjectCount(self):  # pragma: no cover
        return ObjectLevelStatistics.make_one(
            self.boto3_raw_data["unclassifiableObjectCount"]
        )

    @cached_property
    def unclassifiableObjectSizeInBytes(self):  # pragma: no cover
        return ObjectLevelStatistics.make_one(
            self.boto3_raw_data["unclassifiableObjectSizeInBytes"]
        )

    versioning = field("versioning")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Bucket:
    boto3_raw_data: "type_defs.S3BucketTypeDef" = dataclasses.field()

    allowsUnencryptedObjectUploads = field("allowsUnencryptedObjectUploads")
    arn = field("arn")
    createdAt = field("createdAt")

    @cached_property
    def defaultServerSideEncryption(self):  # pragma: no cover
        return ServerSideEncryption.make_one(
            self.boto3_raw_data["defaultServerSideEncryption"]
        )

    name = field("name")

    @cached_property
    def owner(self):  # pragma: no cover
        return S3BucketOwner.make_one(self.boto3_raw_data["owner"])

    @cached_property
    def publicAccess(self):  # pragma: no cover
        return BucketPublicAccess.make_one(self.boto3_raw_data["publicAccess"])

    @cached_property
    def tags(self):  # pragma: no cover
        return KeyValuePair.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3BucketTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3BucketTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDataIdentifiers:
    boto3_raw_data: "type_defs.CustomDataIdentifiersTypeDef" = dataclasses.field()

    @cached_property
    def detections(self):  # pragma: no cover
        return CustomDetection.make_many(self.boto3_raw_data["detections"])

    totalCount = field("totalCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomDataIdentifiersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDataIdentifiersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SensitiveDataItem:
    boto3_raw_data: "type_defs.SensitiveDataItemTypeDef" = dataclasses.field()

    category = field("category")

    @cached_property
    def detections(self):  # pragma: no cover
        return DefaultDetection.make_many(self.boto3_raw_data["detections"])

    totalCount = field("totalCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SensitiveDataItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SensitiveDataItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesBucketCriteria:
    boto3_raw_data: "type_defs.SearchResourcesBucketCriteriaTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def excludes(self):  # pragma: no cover
        return SearchResourcesCriteriaBlock.make_one(self.boto3_raw_data["excludes"])

    @cached_property
    def includes(self):  # pragma: no cover
        return SearchResourcesCriteriaBlock.make_one(self.boto3_raw_data["includes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchResourcesBucketCriteriaTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesBucketCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingActor:
    boto3_raw_data: "type_defs.FindingActorTypeDef" = dataclasses.field()

    @cached_property
    def domainDetails(self):  # pragma: no cover
        return DomainDetails.make_one(self.boto3_raw_data["domainDetails"])

    @cached_property
    def ipAddressDetails(self):  # pragma: no cover
        return IpAddressDetails.make_one(self.boto3_raw_data["ipAddressDetails"])

    @cached_property
    def userIdentity(self):  # pragma: no cover
        return UserIdentity.make_one(self.boto3_raw_data["userIdentity"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingActorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingActorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketCriteriaForJobOutput:
    boto3_raw_data: "type_defs.S3BucketCriteriaForJobOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def excludes(self):  # pragma: no cover
        return CriteriaBlockForJobOutput.make_one(self.boto3_raw_data["excludes"])

    @cached_property
    def includes(self):  # pragma: no cover
        return CriteriaBlockForJobOutput.make_one(self.boto3_raw_data["includes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BucketCriteriaForJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketCriteriaForJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketCriteriaForJob:
    boto3_raw_data: "type_defs.S3BucketCriteriaForJobTypeDef" = dataclasses.field()

    @cached_property
    def excludes(self):  # pragma: no cover
        return CriteriaBlockForJob.make_one(self.boto3_raw_data["excludes"])

    @cached_property
    def includes(self):  # pragma: no cover
        return CriteriaBlockForJob.make_one(self.boto3_raw_data["includes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BucketCriteriaForJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketCriteriaForJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScopingOutput:
    boto3_raw_data: "type_defs.ScopingOutputTypeDef" = dataclasses.field()

    @cached_property
    def excludes(self):  # pragma: no cover
        return JobScopingBlockOutput.make_one(self.boto3_raw_data["excludes"])

    @cached_property
    def includes(self):  # pragma: no cover
        return JobScopingBlockOutput.make_one(self.boto3_raw_data["includes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopingOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopingOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scoping:
    boto3_raw_data: "type_defs.ScopingTypeDef" = dataclasses.field()

    @cached_property
    def excludes(self):  # pragma: no cover
        return JobScopingBlock.make_one(self.boto3_raw_data["excludes"])

    @cached_property
    def includes(self):  # pragma: no cover
        return JobScopingBlock.make_one(self.boto3_raw_data["includes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBucketsResponse:
    boto3_raw_data: "type_defs.DescribeBucketsResponseTypeDef" = dataclasses.field()

    @cached_property
    def buckets(self):  # pragma: no cover
        return BucketMetadata.make_many(self.boto3_raw_data["buckets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBucketsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBucketsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourcesAffected:
    boto3_raw_data: "type_defs.ResourcesAffectedTypeDef" = dataclasses.field()

    @cached_property
    def s3Bucket(self):  # pragma: no cover
        return S3Bucket.make_one(self.boto3_raw_data["s3Bucket"])

    @cached_property
    def s3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["s3Object"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourcesAffectedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourcesAffectedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClassificationResult:
    boto3_raw_data: "type_defs.ClassificationResultTypeDef" = dataclasses.field()

    additionalOccurrences = field("additionalOccurrences")

    @cached_property
    def customDataIdentifiers(self):  # pragma: no cover
        return CustomDataIdentifiers.make_one(
            self.boto3_raw_data["customDataIdentifiers"]
        )

    mimeType = field("mimeType")

    @cached_property
    def sensitiveData(self):  # pragma: no cover
        return SensitiveDataItem.make_many(self.boto3_raw_data["sensitiveData"])

    sizeClassified = field("sizeClassified")

    @cached_property
    def status(self):  # pragma: no cover
        return ClassificationResultStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClassificationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClassificationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesRequestPaginate:
    boto3_raw_data: "type_defs.SearchResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def bucketCriteria(self):  # pragma: no cover
        return SearchResourcesBucketCriteria.make_one(
            self.boto3_raw_data["bucketCriteria"]
        )

    @cached_property
    def sortCriteria(self):  # pragma: no cover
        return SearchResourcesSortCriteria.make_one(self.boto3_raw_data["sortCriteria"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchResourcesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResourcesRequest:
    boto3_raw_data: "type_defs.SearchResourcesRequestTypeDef" = dataclasses.field()

    @cached_property
    def bucketCriteria(self):  # pragma: no cover
        return SearchResourcesBucketCriteria.make_one(
            self.boto3_raw_data["bucketCriteria"]
        )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def sortCriteria(self):  # pragma: no cover
        return SearchResourcesSortCriteria.make_one(self.boto3_raw_data["sortCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyDetails:
    boto3_raw_data: "type_defs.PolicyDetailsTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return FindingAction.make_one(self.boto3_raw_data["action"])

    @cached_property
    def actor(self):  # pragma: no cover
        return FindingActor.make_one(self.boto3_raw_data["actor"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSummary:
    boto3_raw_data: "type_defs.JobSummaryTypeDef" = dataclasses.field()

    @cached_property
    def bucketCriteria(self):  # pragma: no cover
        return S3BucketCriteriaForJobOutput.make_one(
            self.boto3_raw_data["bucketCriteria"]
        )

    @cached_property
    def bucketDefinitions(self):  # pragma: no cover
        return S3BucketDefinitionForJobOutput.make_many(
            self.boto3_raw_data["bucketDefinitions"]
        )

    createdAt = field("createdAt")
    jobId = field("jobId")
    jobStatus = field("jobStatus")
    jobType = field("jobType")

    @cached_property
    def lastRunErrorStatus(self):  # pragma: no cover
        return LastRunErrorStatus.make_one(self.boto3_raw_data["lastRunErrorStatus"])

    name = field("name")

    @cached_property
    def userPausedDetails(self):  # pragma: no cover
        return UserPausedDetails.make_one(self.boto3_raw_data["userPausedDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3JobDefinitionOutput:
    boto3_raw_data: "type_defs.S3JobDefinitionOutputTypeDef" = dataclasses.field()

    @cached_property
    def bucketCriteria(self):  # pragma: no cover
        return S3BucketCriteriaForJobOutput.make_one(
            self.boto3_raw_data["bucketCriteria"]
        )

    @cached_property
    def bucketDefinitions(self):  # pragma: no cover
        return S3BucketDefinitionForJobOutput.make_many(
            self.boto3_raw_data["bucketDefinitions"]
        )

    @cached_property
    def scoping(self):  # pragma: no cover
        return ScopingOutput.make_one(self.boto3_raw_data["scoping"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3JobDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3JobDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3JobDefinition:
    boto3_raw_data: "type_defs.S3JobDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def bucketCriteria(self):  # pragma: no cover
        return S3BucketCriteriaForJob.make_one(self.boto3_raw_data["bucketCriteria"])

    @cached_property
    def bucketDefinitions(self):  # pragma: no cover
        return S3BucketDefinitionForJob.make_many(
            self.boto3_raw_data["bucketDefinitions"]
        )

    @cached_property
    def scoping(self):  # pragma: no cover
        return Scoping.make_one(self.boto3_raw_data["scoping"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3JobDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3JobDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClassificationDetails:
    boto3_raw_data: "type_defs.ClassificationDetailsTypeDef" = dataclasses.field()

    detailedResultsLocation = field("detailedResultsLocation")
    jobArn = field("jobArn")
    jobId = field("jobId")
    originType = field("originType")

    @cached_property
    def result(self):  # pragma: no cover
        return ClassificationResult.make_one(self.boto3_raw_data["result"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClassificationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClassificationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClassificationJobsResponse:
    boto3_raw_data: "type_defs.ListClassificationJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return JobSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListClassificationJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClassificationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClassificationJobResponse:
    boto3_raw_data: "type_defs.DescribeClassificationJobResponseTypeDef" = (
        dataclasses.field()
    )

    allowListIds = field("allowListIds")
    clientToken = field("clientToken")
    createdAt = field("createdAt")
    customDataIdentifierIds = field("customDataIdentifierIds")
    description = field("description")
    initialRun = field("initialRun")
    jobArn = field("jobArn")
    jobId = field("jobId")
    jobStatus = field("jobStatus")
    jobType = field("jobType")

    @cached_property
    def lastRunErrorStatus(self):  # pragma: no cover
        return LastRunErrorStatus.make_one(self.boto3_raw_data["lastRunErrorStatus"])

    lastRunTime = field("lastRunTime")
    managedDataIdentifierIds = field("managedDataIdentifierIds")
    managedDataIdentifierSelector = field("managedDataIdentifierSelector")
    name = field("name")

    @cached_property
    def s3JobDefinition(self):  # pragma: no cover
        return S3JobDefinitionOutput.make_one(self.boto3_raw_data["s3JobDefinition"])

    samplingPercentage = field("samplingPercentage")

    @cached_property
    def scheduleFrequency(self):  # pragma: no cover
        return JobScheduleFrequencyOutput.make_one(
            self.boto3_raw_data["scheduleFrequency"]
        )

    @cached_property
    def statistics(self):  # pragma: no cover
        return Statistics.make_one(self.boto3_raw_data["statistics"])

    tags = field("tags")

    @cached_property
    def userPausedDetails(self):  # pragma: no cover
        return UserPausedDetails.make_one(self.boto3_raw_data["userPausedDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClassificationJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClassificationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Finding:
    boto3_raw_data: "type_defs.FindingTypeDef" = dataclasses.field()

    accountId = field("accountId")
    archived = field("archived")
    category = field("category")

    @cached_property
    def classificationDetails(self):  # pragma: no cover
        return ClassificationDetails.make_one(
            self.boto3_raw_data["classificationDetails"]
        )

    count = field("count")
    createdAt = field("createdAt")
    description = field("description")
    id = field("id")
    partition = field("partition")

    @cached_property
    def policyDetails(self):  # pragma: no cover
        return PolicyDetails.make_one(self.boto3_raw_data["policyDetails"])

    region = field("region")

    @cached_property
    def resourcesAffected(self):  # pragma: no cover
        return ResourcesAffected.make_one(self.boto3_raw_data["resourcesAffected"])

    sample = field("sample")
    schemaVersion = field("schemaVersion")

    @cached_property
    def severity(self):  # pragma: no cover
        return Severity.make_one(self.boto3_raw_data["severity"])

    title = field("title")
    type = field("type")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClassificationJobRequest:
    boto3_raw_data: "type_defs.CreateClassificationJobRequestTypeDef" = (
        dataclasses.field()
    )

    clientToken = field("clientToken")
    jobType = field("jobType")
    name = field("name")
    s3JobDefinition = field("s3JobDefinition")
    allowListIds = field("allowListIds")
    customDataIdentifierIds = field("customDataIdentifierIds")
    description = field("description")
    initialRun = field("initialRun")
    managedDataIdentifierIds = field("managedDataIdentifierIds")
    managedDataIdentifierSelector = field("managedDataIdentifierSelector")
    samplingPercentage = field("samplingPercentage")
    scheduleFrequency = field("scheduleFrequency")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateClassificationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClassificationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsResponse:
    boto3_raw_data: "type_defs.GetFindingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def findings(self):  # pragma: no cover
        return Finding.make_many(self.boto3_raw_data["findings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFindingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
