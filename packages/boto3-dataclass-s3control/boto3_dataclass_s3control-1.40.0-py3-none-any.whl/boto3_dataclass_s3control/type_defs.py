# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_s3control import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AbortIncompleteMultipartUpload:
    boto3_raw_data: "type_defs.AbortIncompleteMultipartUploadTypeDef" = (
        dataclasses.field()
    )

    DaysAfterInitiation = field("DaysAfterInitiation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AbortIncompleteMultipartUploadTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbortIncompleteMultipartUploadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControlTranslation:
    boto3_raw_data: "type_defs.AccessControlTranslationTypeDef" = dataclasses.field()

    Owner = field("Owner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessControlTranslationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlTranslationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessGrantsLocationConfiguration:
    boto3_raw_data: "type_defs.AccessGrantsLocationConfigurationTypeDef" = (
        dataclasses.field()
    )

    S3SubPrefix = field("S3SubPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AccessGrantsLocationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessGrantsLocationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfiguration:
    boto3_raw_data: "type_defs.VpcConfigurationTypeDef" = dataclasses.field()

    VpcId = field("VpcId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityMetrics:
    boto3_raw_data: "type_defs.ActivityMetricsTypeDef" = dataclasses.field()

    IsEnabled = field("IsEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityMetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivityMetricsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedCostOptimizationMetrics:
    boto3_raw_data: "type_defs.AdvancedCostOptimizationMetricsTypeDef" = (
        dataclasses.field()
    )

    IsEnabled = field("IsEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdvancedCostOptimizationMetricsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedCostOptimizationMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedDataProtectionMetrics:
    boto3_raw_data: "type_defs.AdvancedDataProtectionMetricsTypeDef" = (
        dataclasses.field()
    )

    IsEnabled = field("IsEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdvancedDataProtectionMetricsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedDataProtectionMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetailedStatusCodesMetrics:
    boto3_raw_data: "type_defs.DetailedStatusCodesMetricsTypeDef" = dataclasses.field()

    IsEnabled = field("IsEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetailedStatusCodesMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetailedStatusCodesMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAccessGrantsIdentityCenterRequest:
    boto3_raw_data: "type_defs.AssociateAccessGrantsIdentityCenterRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    IdentityCenterArn = field("IdentityCenterArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAccessGrantsIdentityCenterRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAccessGrantsIdentityCenterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AsyncErrorDetails:
    boto3_raw_data: "type_defs.AsyncErrorDetailsTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")
    Resource = field("Resource")
    RequestId = field("RequestId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AsyncErrorDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AsyncErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMultiRegionAccessPointInput:
    boto3_raw_data: "type_defs.DeleteMultiRegionAccessPointInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMultiRegionAccessPointInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMultiRegionAccessPointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMultiRegionAccessPointPolicyInput:
    boto3_raw_data: "type_defs.PutMultiRegionAccessPointPolicyInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutMultiRegionAccessPointPolicyInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMultiRegionAccessPointPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsLambdaTransformation:
    boto3_raw_data: "type_defs.AwsLambdaTransformationTypeDef" = dataclasses.field()

    FunctionArn = field("FunctionArn")
    FunctionPayload = field("FunctionPayload")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsLambdaTransformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsLambdaTransformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchMetrics:
    boto3_raw_data: "type_defs.CloudWatchMetricsTypeDef" = dataclasses.field()

    IsEnabled = field("IsEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CloudWatchMetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Grantee:
    boto3_raw_data: "type_defs.GranteeTypeDef" = dataclasses.field()

    GranteeType = field("GranteeType")
    GranteeIdentifier = field("GranteeIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GranteeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GranteeTypeDef"]]
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
class ObjectLambdaAccessPointAlias:
    boto3_raw_data: "type_defs.ObjectLambdaAccessPointAliasTypeDef" = (
        dataclasses.field()
    )

    Value = field("Value")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectLambdaAccessPointAliasTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLambdaAccessPointAliasTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicAccessBlockConfiguration:
    boto3_raw_data: "type_defs.PublicAccessBlockConfigurationTypeDef" = (
        dataclasses.field()
    )

    BlockPublicAcls = field("BlockPublicAcls")
    IgnorePublicAcls = field("IgnorePublicAcls")
    BlockPublicPolicy = field("BlockPublicPolicy")
    RestrictPublicBuckets = field("RestrictPublicBuckets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PublicAccessBlockConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublicAccessBlockConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketConfiguration:
    boto3_raw_data: "type_defs.CreateBucketConfigurationTypeDef" = dataclasses.field()

    LocationConstraint = field("LocationConstraint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBucketConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobReport:
    boto3_raw_data: "type_defs.JobReportTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Bucket = field("Bucket")
    Format = field("Format")
    Prefix = field("Prefix")
    ReportScope = field("ReportScope")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobReportTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Tag:
    boto3_raw_data: "type_defs.S3TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Region:
    boto3_raw_data: "type_defs.RegionTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    BucketAccountId = field("BucketAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Credentials:
    boto3_raw_data: "type_defs.CredentialsTypeDef" = dataclasses.field()

    AccessKeyId = field("AccessKeyId")
    SecretAccessKey = field("SecretAccessKey")
    SessionToken = field("SessionToken")
    Expiration = field("Expiration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CredentialsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DSSEKMSFilter:
    boto3_raw_data: "type_defs.DSSEKMSFilterTypeDef" = dataclasses.field()

    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DSSEKMSFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DSSEKMSFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessGrantRequest:
    boto3_raw_data: "type_defs.DeleteAccessGrantRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    AccessGrantId = field("AccessGrantId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccessGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessGrantsInstanceRequest:
    boto3_raw_data: "type_defs.DeleteAccessGrantsInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAccessGrantsInstanceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessGrantsInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessGrantsInstanceResourcePolicyRequest:
    boto3_raw_data: (
        "type_defs.DeleteAccessGrantsInstanceResourcePolicyRequestTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAccessGrantsInstanceResourcePolicyRequestTypeDef"
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
                "type_defs.DeleteAccessGrantsInstanceResourcePolicyRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessGrantsLocationRequest:
    boto3_raw_data: "type_defs.DeleteAccessGrantsLocationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    AccessGrantsLocationId = field("AccessGrantsLocationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAccessGrantsLocationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessGrantsLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessPointForObjectLambdaRequest:
    boto3_raw_data: "type_defs.DeleteAccessPointForObjectLambdaRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAccessPointForObjectLambdaRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessPointForObjectLambdaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessPointPolicyForObjectLambdaRequest:
    boto3_raw_data: "type_defs.DeleteAccessPointPolicyForObjectLambdaRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAccessPointPolicyForObjectLambdaRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessPointPolicyForObjectLambdaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessPointPolicyRequest:
    boto3_raw_data: "type_defs.DeleteAccessPointPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAccessPointPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessPointPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessPointRequest:
    boto3_raw_data: "type_defs.DeleteAccessPointRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccessPointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessPointScopeRequest:
    boto3_raw_data: "type_defs.DeleteAccessPointScopeRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAccessPointScopeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessPointScopeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketLifecycleConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteBucketLifecycleConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteBucketLifecycleConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketLifecycleConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketPolicyRequest:
    boto3_raw_data: "type_defs.DeleteBucketPolicyRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketReplicationRequest:
    boto3_raw_data: "type_defs.DeleteBucketReplicationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteBucketReplicationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketRequest:
    boto3_raw_data: "type_defs.DeleteBucketRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBucketTaggingRequest:
    boto3_raw_data: "type_defs.DeleteBucketTaggingRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBucketTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBucketTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobTaggingRequest:
    boto3_raw_data: "type_defs.DeleteJobTaggingRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteJobTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMarkerReplication:
    boto3_raw_data: "type_defs.DeleteMarkerReplicationTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMarkerReplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMarkerReplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePublicAccessBlockRequest:
    boto3_raw_data: "type_defs.DeletePublicAccessBlockRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePublicAccessBlockRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePublicAccessBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStorageLensConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteStorageLensConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigId = field("ConfigId")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteStorageLensConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStorageLensConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStorageLensConfigurationTaggingRequest:
    boto3_raw_data: "type_defs.DeleteStorageLensConfigurationTaggingRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigId = field("ConfigId")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteStorageLensConfigurationTaggingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStorageLensConfigurationTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStorageLensGroupRequest:
    boto3_raw_data: "type_defs.DeleteStorageLensGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteStorageLensGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStorageLensGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobRequest:
    boto3_raw_data: "type_defs.DescribeJobRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiRegionAccessPointOperationRequest:
    boto3_raw_data: (
        "type_defs.DescribeMultiRegionAccessPointOperationRequestTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")
    RequestTokenARN = field("RequestTokenARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMultiRegionAccessPointOperationRequestTypeDef"
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
                "type_defs.DescribeMultiRegionAccessPointOperationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    ReplicaKmsKeyID = field("ReplicaKmsKeyID")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DissociateAccessGrantsIdentityCenterRequest:
    boto3_raw_data: "type_defs.DissociateAccessGrantsIdentityCenterRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DissociateAccessGrantsIdentityCenterRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DissociateAccessGrantsIdentityCenterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EstablishedMultiRegionAccessPointPolicy:
    boto3_raw_data: "type_defs.EstablishedMultiRegionAccessPointPolicyTypeDef" = (
        dataclasses.field()
    )

    Policy = field("Policy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EstablishedMultiRegionAccessPointPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EstablishedMultiRegionAccessPointPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExcludeOutput:
    boto3_raw_data: "type_defs.ExcludeOutputTypeDef" = dataclasses.field()

    Buckets = field("Buckets")
    Regions = field("Regions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExcludeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExcludeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Exclude:
    boto3_raw_data: "type_defs.ExcludeTypeDef" = dataclasses.field()

    Buckets = field("Buckets")
    Regions = field("Regions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExcludeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExcludeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExistingObjectReplication:
    boto3_raw_data: "type_defs.ExistingObjectReplicationTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExistingObjectReplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExistingObjectReplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSEKMSEncryption:
    boto3_raw_data: "type_defs.SSEKMSEncryptionTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSEKMSEncryptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SSEKMSEncryptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessGrantRequest:
    boto3_raw_data: "type_defs.GetAccessGrantRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    AccessGrantId = field("AccessGrantId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessGrantsInstanceForPrefixRequest:
    boto3_raw_data: "type_defs.GetAccessGrantsInstanceForPrefixRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    S3Prefix = field("S3Prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessGrantsInstanceForPrefixRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessGrantsInstanceForPrefixRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessGrantsInstanceRequest:
    boto3_raw_data: "type_defs.GetAccessGrantsInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccessGrantsInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessGrantsInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessGrantsInstanceResourcePolicyRequest:
    boto3_raw_data: "type_defs.GetAccessGrantsInstanceResourcePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessGrantsInstanceResourcePolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessGrantsInstanceResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessGrantsLocationRequest:
    boto3_raw_data: "type_defs.GetAccessGrantsLocationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    AccessGrantsLocationId = field("AccessGrantsLocationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccessGrantsLocationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessGrantsLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointConfigurationForObjectLambdaRequest:
    boto3_raw_data: (
        "type_defs.GetAccessPointConfigurationForObjectLambdaRequestTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessPointConfigurationForObjectLambdaRequestTypeDef"
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
                "type_defs.GetAccessPointConfigurationForObjectLambdaRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointForObjectLambdaRequest:
    boto3_raw_data: "type_defs.GetAccessPointForObjectLambdaRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessPointForObjectLambdaRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointForObjectLambdaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointPolicyForObjectLambdaRequest:
    boto3_raw_data: "type_defs.GetAccessPointPolicyForObjectLambdaRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessPointPolicyForObjectLambdaRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointPolicyForObjectLambdaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointPolicyRequest:
    boto3_raw_data: "type_defs.GetAccessPointPolicyRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessPointPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointPolicyStatusForObjectLambdaRequest:
    boto3_raw_data: (
        "type_defs.GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef"
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
                "type_defs.GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyStatus:
    boto3_raw_data: "type_defs.PolicyStatusTypeDef" = dataclasses.field()

    IsPublic = field("IsPublic")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointPolicyStatusRequest:
    boto3_raw_data: "type_defs.GetAccessPointPolicyStatusRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessPointPolicyStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointPolicyStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointRequest:
    boto3_raw_data: "type_defs.GetAccessPointRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessPointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointScopeRequest:
    boto3_raw_data: "type_defs.GetAccessPointScopeRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessPointScopeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointScopeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScopeOutput:
    boto3_raw_data: "type_defs.ScopeOutputTypeDef" = dataclasses.field()

    Prefixes = field("Prefixes")
    Permissions = field("Permissions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketLifecycleConfigurationRequest:
    boto3_raw_data: "type_defs.GetBucketLifecycleConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketLifecycleConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketLifecycleConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketPolicyRequest:
    boto3_raw_data: "type_defs.GetBucketPolicyRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketReplicationRequest:
    boto3_raw_data: "type_defs.GetBucketReplicationRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketRequest:
    boto3_raw_data: "type_defs.GetBucketRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBucketRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketTaggingRequest:
    boto3_raw_data: "type_defs.GetBucketTaggingRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketVersioningRequest:
    boto3_raw_data: "type_defs.GetBucketVersioningRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketVersioningRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketVersioningRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataAccessRequest:
    boto3_raw_data: "type_defs.GetDataAccessRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Target = field("Target")
    Permission = field("Permission")
    DurationSeconds = field("DurationSeconds")
    Privilege = field("Privilege")
    TargetType = field("TargetType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataAccessRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobTaggingRequest:
    boto3_raw_data: "type_defs.GetJobTaggingRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJobTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMultiRegionAccessPointPolicyRequest:
    boto3_raw_data: "type_defs.GetMultiRegionAccessPointPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMultiRegionAccessPointPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMultiRegionAccessPointPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMultiRegionAccessPointPolicyStatusRequest:
    boto3_raw_data: "type_defs.GetMultiRegionAccessPointPolicyStatusRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMultiRegionAccessPointPolicyStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMultiRegionAccessPointPolicyStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMultiRegionAccessPointRequest:
    boto3_raw_data: "type_defs.GetMultiRegionAccessPointRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMultiRegionAccessPointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMultiRegionAccessPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMultiRegionAccessPointRoutesRequest:
    boto3_raw_data: "type_defs.GetMultiRegionAccessPointRoutesRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Mrap = field("Mrap")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMultiRegionAccessPointRoutesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMultiRegionAccessPointRoutesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiRegionAccessPointRoute:
    boto3_raw_data: "type_defs.MultiRegionAccessPointRouteTypeDef" = dataclasses.field()

    TrafficDialPercentage = field("TrafficDialPercentage")
    Bucket = field("Bucket")
    Region = field("Region")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiRegionAccessPointRouteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiRegionAccessPointRouteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicAccessBlockRequest:
    boto3_raw_data: "type_defs.GetPublicAccessBlockRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicAccessBlockRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicAccessBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageLensConfigurationRequest:
    boto3_raw_data: "type_defs.GetStorageLensConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigId = field("ConfigId")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetStorageLensConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageLensConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageLensConfigurationTaggingRequest:
    boto3_raw_data: "type_defs.GetStorageLensConfigurationTaggingRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigId = field("ConfigId")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetStorageLensConfigurationTaggingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageLensConfigurationTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensTag:
    boto3_raw_data: "type_defs.StorageLensTagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorageLensTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StorageLensTagTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageLensGroupRequest:
    boto3_raw_data: "type_defs.GetStorageLensGroupRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStorageLensGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageLensGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncludeOutput:
    boto3_raw_data: "type_defs.IncludeOutputTypeDef" = dataclasses.field()

    Buckets = field("Buckets")
    Regions = field("Regions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IncludeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IncludeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Include:
    boto3_raw_data: "type_defs.IncludeTypeDef" = dataclasses.field()

    Buckets = field("Buckets")
    Regions = field("Regions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IncludeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IncludeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobFailure:
    boto3_raw_data: "type_defs.JobFailureTypeDef" = dataclasses.field()

    FailureCode = field("FailureCode")
    FailureReason = field("FailureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobFailureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobFailureTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyNameConstraintOutput:
    boto3_raw_data: "type_defs.KeyNameConstraintOutputTypeDef" = dataclasses.field()

    MatchAnyPrefix = field("MatchAnyPrefix")
    MatchAnySuffix = field("MatchAnySuffix")
    MatchAnySubstring = field("MatchAnySubstring")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KeyNameConstraintOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyNameConstraintOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyNameConstraint:
    boto3_raw_data: "type_defs.KeyNameConstraintTypeDef" = dataclasses.field()

    MatchAnyPrefix = field("MatchAnyPrefix")
    MatchAnySuffix = field("MatchAnySuffix")
    MatchAnySubstring = field("MatchAnySubstring")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyNameConstraintTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KeyNameConstraintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobManifestLocation:
    boto3_raw_data: "type_defs.JobManifestLocationTypeDef" = dataclasses.field()

    ObjectArn = field("ObjectArn")
    ETag = field("ETag")
    ObjectVersionId = field("ObjectVersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobManifestLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobManifestLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobManifestSpecOutput:
    boto3_raw_data: "type_defs.JobManifestSpecOutputTypeDef" = dataclasses.field()

    Format = field("Format")
    Fields = field("Fields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobManifestSpecOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobManifestSpecOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobManifestSpec:
    boto3_raw_data: "type_defs.JobManifestSpecTypeDef" = dataclasses.field()

    Format = field("Format")
    Fields = field("Fields")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobManifestSpecTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobManifestSpecTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaInvokeOperationOutput:
    boto3_raw_data: "type_defs.LambdaInvokeOperationOutputTypeDef" = dataclasses.field()

    FunctionArn = field("FunctionArn")
    InvocationSchemaVersion = field("InvocationSchemaVersion")
    UserArguments = field("UserArguments")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaInvokeOperationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaInvokeOperationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ComputeObjectChecksumOperation:
    boto3_raw_data: "type_defs.S3ComputeObjectChecksumOperationTypeDef" = (
        dataclasses.field()
    )

    ChecksumAlgorithm = field("ChecksumAlgorithm")
    ChecksumType = field("ChecksumType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3ComputeObjectChecksumOperationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ComputeObjectChecksumOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3InitiateRestoreObjectOperation:
    boto3_raw_data: "type_defs.S3InitiateRestoreObjectOperationTypeDef" = (
        dataclasses.field()
    )

    ExpirationInDays = field("ExpirationInDays")
    GlacierJobTier = field("GlacierJobTier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3InitiateRestoreObjectOperationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3InitiateRestoreObjectOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaInvokeOperation:
    boto3_raw_data: "type_defs.LambdaInvokeOperationTypeDef" = dataclasses.field()

    FunctionArn = field("FunctionArn")
    InvocationSchemaVersion = field("InvocationSchemaVersion")
    UserArguments = field("UserArguments")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaInvokeOperationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaInvokeOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobTimers:
    boto3_raw_data: "type_defs.JobTimersTypeDef" = dataclasses.field()

    ElapsedTimeInActiveSeconds = field("ElapsedTimeInActiveSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTimersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTimersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleExpirationOutput:
    boto3_raw_data: "type_defs.LifecycleExpirationOutputTypeDef" = dataclasses.field()

    Date = field("Date")
    Days = field("Days")
    ExpiredObjectDeleteMarker = field("ExpiredObjectDeleteMarker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleExpirationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleExpirationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoncurrentVersionExpiration:
    boto3_raw_data: "type_defs.NoncurrentVersionExpirationTypeDef" = dataclasses.field()

    NoncurrentDays = field("NoncurrentDays")
    NewerNoncurrentVersions = field("NewerNoncurrentVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NoncurrentVersionExpirationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NoncurrentVersionExpirationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NoncurrentVersionTransition:
    boto3_raw_data: "type_defs.NoncurrentVersionTransitionTypeDef" = dataclasses.field()

    NoncurrentDays = field("NoncurrentDays")
    StorageClass = field("StorageClass")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NoncurrentVersionTransitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NoncurrentVersionTransitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransitionOutput:
    boto3_raw_data: "type_defs.TransitionOutputTypeDef" = dataclasses.field()

    Date = field("Date")
    Days = field("Days")
    StorageClass = field("StorageClass")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransitionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessGrantsInstanceEntry:
    boto3_raw_data: "type_defs.ListAccessGrantsInstanceEntryTypeDef" = (
        dataclasses.field()
    )

    AccessGrantsInstanceId = field("AccessGrantsInstanceId")
    AccessGrantsInstanceArn = field("AccessGrantsInstanceArn")
    CreatedAt = field("CreatedAt")
    IdentityCenterArn = field("IdentityCenterArn")
    IdentityCenterInstanceArn = field("IdentityCenterInstanceArn")
    IdentityCenterApplicationArn = field("IdentityCenterApplicationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccessGrantsInstanceEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessGrantsInstanceEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessGrantsInstancesRequest:
    boto3_raw_data: "type_defs.ListAccessGrantsInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccessGrantsInstancesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessGrantsInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessGrantsLocationsEntry:
    boto3_raw_data: "type_defs.ListAccessGrantsLocationsEntryTypeDef" = (
        dataclasses.field()
    )

    CreatedAt = field("CreatedAt")
    AccessGrantsLocationId = field("AccessGrantsLocationId")
    AccessGrantsLocationArn = field("AccessGrantsLocationArn")
    LocationScope = field("LocationScope")
    IAMRoleArn = field("IAMRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccessGrantsLocationsEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessGrantsLocationsEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessGrantsLocationsRequest:
    boto3_raw_data: "type_defs.ListAccessGrantsLocationsRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    LocationScope = field("LocationScope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccessGrantsLocationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessGrantsLocationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessGrantsRequest:
    boto3_raw_data: "type_defs.ListAccessGrantsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    GranteeType = field("GranteeType")
    GranteeIdentifier = field("GranteeIdentifier")
    Permission = field("Permission")
    GrantScope = field("GrantScope")
    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessGrantsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessGrantsRequestTypeDef"]
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
class ListAccessPointsForDirectoryBucketsRequest:
    boto3_raw_data: "type_defs.ListAccessPointsForDirectoryBucketsRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    DirectoryBucket = field("DirectoryBucket")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessPointsForDirectoryBucketsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPointsForDirectoryBucketsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPointsForObjectLambdaRequest:
    boto3_raw_data: "type_defs.ListAccessPointsForObjectLambdaRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessPointsForObjectLambdaRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPointsForObjectLambdaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPointsRequest:
    boto3_raw_data: "type_defs.ListAccessPointsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    DataSourceId = field("DataSourceId")
    DataSourceType = field("DataSourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessPointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCallerAccessGrantsEntry:
    boto3_raw_data: "type_defs.ListCallerAccessGrantsEntryTypeDef" = dataclasses.field()

    Permission = field("Permission")
    GrantScope = field("GrantScope")
    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCallerAccessGrantsEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCallerAccessGrantsEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCallerAccessGrantsRequest:
    boto3_raw_data: "type_defs.ListCallerAccessGrantsRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    GrantScope = field("GrantScope")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    AllowedByApplication = field("AllowedByApplication")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCallerAccessGrantsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCallerAccessGrantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsRequest:
    boto3_raw_data: "type_defs.ListJobsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    JobStatuses = field("JobStatuses")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultiRegionAccessPointsRequest:
    boto3_raw_data: "type_defs.ListMultiRegionAccessPointsRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMultiRegionAccessPointsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultiRegionAccessPointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRegionalBucketsRequest:
    boto3_raw_data: "type_defs.ListRegionalBucketsRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    OutpostId = field("OutpostId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRegionalBucketsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRegionalBucketsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegionalBucket:
    boto3_raw_data: "type_defs.RegionalBucketTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    PublicAccessBlockEnabled = field("PublicAccessBlockEnabled")
    CreationDate = field("CreationDate")
    BucketArn = field("BucketArn")
    OutpostId = field("OutpostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionalBucketTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegionalBucketTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageLensConfigurationEntry:
    boto3_raw_data: "type_defs.ListStorageLensConfigurationEntryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    StorageLensArn = field("StorageLensArn")
    HomeRegion = field("HomeRegion")
    IsEnabled = field("IsEnabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStorageLensConfigurationEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageLensConfigurationEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageLensConfigurationsRequest:
    boto3_raw_data: "type_defs.ListStorageLensConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStorageLensConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageLensConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageLensGroupEntry:
    boto3_raw_data: "type_defs.ListStorageLensGroupEntryTypeDef" = dataclasses.field()

    Name = field("Name")
    StorageLensGroupArn = field("StorageLensGroupArn")
    HomeRegion = field("HomeRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStorageLensGroupEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageLensGroupEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageLensGroupsRequest:
    boto3_raw_data: "type_defs.ListStorageLensGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStorageLensGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageLensGroupsRequestTypeDef"]
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

    AccountId = field("AccountId")
    ResourceArn = field("ResourceArn")

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
class MatchObjectAge:
    boto3_raw_data: "type_defs.MatchObjectAgeTypeDef" = dataclasses.field()

    DaysGreaterThan = field("DaysGreaterThan")
    DaysLessThan = field("DaysLessThan")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchObjectAgeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchObjectAgeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchObjectSize:
    boto3_raw_data: "type_defs.MatchObjectSizeTypeDef" = dataclasses.field()

    BytesGreaterThan = field("BytesGreaterThan")
    BytesLessThan = field("BytesLessThan")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchObjectSizeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchObjectSizeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTimeValue:
    boto3_raw_data: "type_defs.ReplicationTimeValueTypeDef" = dataclasses.field()

    Minutes = field("Minutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationTimeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationTimeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProposedMultiRegionAccessPointPolicy:
    boto3_raw_data: "type_defs.ProposedMultiRegionAccessPointPolicyTypeDef" = (
        dataclasses.field()
    )

    Policy = field("Policy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProposedMultiRegionAccessPointPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProposedMultiRegionAccessPointPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiRegionAccessPointRegionalResponse:
    boto3_raw_data: "type_defs.MultiRegionAccessPointRegionalResponseTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    RequestStatus = field("RequestStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultiRegionAccessPointRegionalResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiRegionAccessPointRegionalResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegionReport:
    boto3_raw_data: "type_defs.RegionReportTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Region = field("Region")
    BucketAccountId = field("BucketAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegionReportTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSEKMSFilter:
    boto3_raw_data: "type_defs.SSEKMSFilterTypeDef" = dataclasses.field()

    KmsKeyArn = field("KmsKeyArn")
    BucketKeyEnabled = field("BucketKeyEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSEKMSFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SSEKMSFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectionCriteria:
    boto3_raw_data: "type_defs.SelectionCriteriaTypeDef" = dataclasses.field()

    Delimiter = field("Delimiter")
    MaxDepth = field("MaxDepth")
    MinStorageBytesPercentage = field("MinStorageBytesPercentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SelectionCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectionCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccessGrantsInstanceResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutAccessGrantsInstanceResourcePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Policy = field("Policy")
    Organization = field("Organization")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAccessGrantsInstanceResourcePolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccessGrantsInstanceResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccessPointPolicyForObjectLambdaRequest:
    boto3_raw_data: "type_defs.PutAccessPointPolicyForObjectLambdaRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAccessPointPolicyForObjectLambdaRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccessPointPolicyForObjectLambdaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccessPointPolicyRequest:
    boto3_raw_data: "type_defs.PutAccessPointPolicyRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccessPointPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccessPointPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketPolicyRequest:
    boto3_raw_data: "type_defs.PutBucketPolicyRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")
    Policy = field("Policy")
    ConfirmRemoveSelfBucketAccess = field("ConfirmRemoveSelfBucketAccess")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VersioningConfiguration:
    boto3_raw_data: "type_defs.VersioningConfigurationTypeDef" = dataclasses.field()

    MFADelete = field("MFADelete")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VersioningConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VersioningConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicaModifications:
    boto3_raw_data: "type_defs.ReplicaModificationsTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicaModificationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicaModificationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ObjectOwner:
    boto3_raw_data: "type_defs.S3ObjectOwnerTypeDef" = dataclasses.field()

    ID = field("ID")
    DisplayName = field("DisplayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectOwnerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectOwnerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ObjectMetadataOutput:
    boto3_raw_data: "type_defs.S3ObjectMetadataOutputTypeDef" = dataclasses.field()

    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    UserMetadata = field("UserMetadata")
    ContentLength = field("ContentLength")
    ContentMD5 = field("ContentMD5")
    ContentType = field("ContentType")
    HttpExpiresDate = field("HttpExpiresDate")
    RequesterCharged = field("RequesterCharged")
    SSEAlgorithm = field("SSEAlgorithm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ObjectMetadataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ObjectMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Grantee:
    boto3_raw_data: "type_defs.S3GranteeTypeDef" = dataclasses.field()

    TypeIdentifier = field("TypeIdentifier")
    Identifier = field("Identifier")
    DisplayName = field("DisplayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3GranteeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3GranteeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ObjectLockLegalHold:
    boto3_raw_data: "type_defs.S3ObjectLockLegalHoldTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ObjectLockLegalHoldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ObjectLockLegalHoldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3RetentionOutput:
    boto3_raw_data: "type_defs.S3RetentionOutputTypeDef" = dataclasses.field()

    RetainUntilDate = field("RetainUntilDate")
    Mode = field("Mode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3RetentionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3RetentionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSEKMS:
    boto3_raw_data: "type_defs.SSEKMSTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSEKMSTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SSEKMSTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scope:
    boto3_raw_data: "type_defs.ScopeTypeDef" = dataclasses.field()

    Prefixes = field("Prefixes")
    Permissions = field("Permissions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SseKmsEncryptedObjects:
    boto3_raw_data: "type_defs.SseKmsEncryptedObjectsTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SseKmsEncryptedObjectsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SseKmsEncryptedObjectsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensAwsOrg:
    boto3_raw_data: "type_defs.StorageLensAwsOrgTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorageLensAwsOrgTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensAwsOrgTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroupLevelSelectionCriteriaOutput:
    boto3_raw_data: "type_defs.StorageLensGroupLevelSelectionCriteriaOutputTypeDef" = (
        dataclasses.field()
    )

    Include = field("Include")
    Exclude = field("Exclude")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StorageLensGroupLevelSelectionCriteriaOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupLevelSelectionCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroupLevelSelectionCriteria:
    boto3_raw_data: "type_defs.StorageLensGroupLevelSelectionCriteriaTypeDef" = (
        dataclasses.field()
    )

    Include = field("Include")
    Exclude = field("Exclude")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StorageLensGroupLevelSelectionCriteriaTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupLevelSelectionCriteriaTypeDef"]
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

    AccountId = field("AccountId")
    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

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
class UpdateAccessGrantsLocationRequest:
    boto3_raw_data: "type_defs.UpdateAccessGrantsLocationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    AccessGrantsLocationId = field("AccessGrantsLocationId")
    IAMRoleArn = field("IAMRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAccessGrantsLocationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessGrantsLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobPriorityRequest:
    boto3_raw_data: "type_defs.UpdateJobPriorityRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    JobId = field("JobId")
    Priority = field("Priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJobPriorityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobPriorityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobStatusRequest:
    boto3_raw_data: "type_defs.UpdateJobStatusRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    JobId = field("JobId")
    RequestedJobStatus = field("RequestedJobStatus")
    StatusUpdateReason = field("StatusUpdateReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJobStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPoint:
    boto3_raw_data: "type_defs.AccessPointTypeDef" = dataclasses.field()

    Name = field("Name")
    NetworkOrigin = field("NetworkOrigin")
    Bucket = field("Bucket")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["VpcConfiguration"])

    AccessPointArn = field("AccessPointArn")
    Alias = field("Alias")
    BucketAccountId = field("BucketAccountId")
    DataSourceId = field("DataSourceId")
    DataSourceType = field("DataSourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessPointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMultiRegionAccessPointRequest:
    boto3_raw_data: "type_defs.DeleteMultiRegionAccessPointRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    ClientToken = field("ClientToken")

    @cached_property
    def Details(self):  # pragma: no cover
        return DeleteMultiRegionAccessPointInput.make_one(
            self.boto3_raw_data["Details"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMultiRegionAccessPointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMultiRegionAccessPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMultiRegionAccessPointPolicyRequest:
    boto3_raw_data: "type_defs.PutMultiRegionAccessPointPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    ClientToken = field("ClientToken")

    @cached_property
    def Details(self):  # pragma: no cover
        return PutMultiRegionAccessPointPolicyInput.make_one(
            self.boto3_raw_data["Details"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutMultiRegionAccessPointPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMultiRegionAccessPointPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLambdaContentTransformation:
    boto3_raw_data: "type_defs.ObjectLambdaContentTransformationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AwsLambda(self):  # pragma: no cover
        return AwsLambdaTransformation.make_one(self.boto3_raw_data["AwsLambda"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ObjectLambdaContentTransformationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLambdaContentTransformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessGrantEntry:
    boto3_raw_data: "type_defs.ListAccessGrantEntryTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    AccessGrantId = field("AccessGrantId")
    AccessGrantArn = field("AccessGrantArn")

    @cached_property
    def Grantee(self):  # pragma: no cover
        return Grantee.make_one(self.boto3_raw_data["Grantee"])

    Permission = field("Permission")
    AccessGrantsLocationId = field("AccessGrantsLocationId")

    @cached_property
    def AccessGrantsLocationConfiguration(self):  # pragma: no cover
        return AccessGrantsLocationConfiguration.make_one(
            self.boto3_raw_data["AccessGrantsLocationConfiguration"]
        )

    GrantScope = field("GrantScope")
    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessGrantEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessGrantEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessGrantRequest:
    boto3_raw_data: "type_defs.CreateAccessGrantRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    AccessGrantsLocationId = field("AccessGrantsLocationId")

    @cached_property
    def Grantee(self):  # pragma: no cover
        return Grantee.make_one(self.boto3_raw_data["Grantee"])

    Permission = field("Permission")

    @cached_property
    def AccessGrantsLocationConfiguration(self):  # pragma: no cover
        return AccessGrantsLocationConfiguration.make_one(
            self.boto3_raw_data["AccessGrantsLocationConfiguration"]
        )

    ApplicationArn = field("ApplicationArn")
    S3PrefixType = field("S3PrefixType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessGrantsInstanceRequest:
    boto3_raw_data: "type_defs.CreateAccessGrantsInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    IdentityCenterArn = field("IdentityCenterArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAccessGrantsInstanceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessGrantsInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessGrantsLocationRequest:
    boto3_raw_data: "type_defs.CreateAccessGrantsLocationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    LocationScope = field("LocationScope")
    IAMRoleArn = field("IAMRoleArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAccessGrantsLocationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessGrantsLocationRequestTypeDef"]
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

    AccountId = field("AccountId")
    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateAccessGrantResult:
    boto3_raw_data: "type_defs.CreateAccessGrantResultTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    AccessGrantId = field("AccessGrantId")
    AccessGrantArn = field("AccessGrantArn")

    @cached_property
    def Grantee(self):  # pragma: no cover
        return Grantee.make_one(self.boto3_raw_data["Grantee"])

    AccessGrantsLocationId = field("AccessGrantsLocationId")

    @cached_property
    def AccessGrantsLocationConfiguration(self):  # pragma: no cover
        return AccessGrantsLocationConfiguration.make_one(
            self.boto3_raw_data["AccessGrantsLocationConfiguration"]
        )

    Permission = field("Permission")
    ApplicationArn = field("ApplicationArn")
    GrantScope = field("GrantScope")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessGrantResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessGrantResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessGrantsInstanceResult:
    boto3_raw_data: "type_defs.CreateAccessGrantsInstanceResultTypeDef" = (
        dataclasses.field()
    )

    CreatedAt = field("CreatedAt")
    AccessGrantsInstanceId = field("AccessGrantsInstanceId")
    AccessGrantsInstanceArn = field("AccessGrantsInstanceArn")
    IdentityCenterArn = field("IdentityCenterArn")
    IdentityCenterInstanceArn = field("IdentityCenterInstanceArn")
    IdentityCenterApplicationArn = field("IdentityCenterApplicationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAccessGrantsInstanceResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessGrantsInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessGrantsLocationResult:
    boto3_raw_data: "type_defs.CreateAccessGrantsLocationResultTypeDef" = (
        dataclasses.field()
    )

    CreatedAt = field("CreatedAt")
    AccessGrantsLocationId = field("AccessGrantsLocationId")
    AccessGrantsLocationArn = field("AccessGrantsLocationArn")
    LocationScope = field("LocationScope")
    IAMRoleArn = field("IAMRoleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAccessGrantsLocationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessGrantsLocationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPointResult:
    boto3_raw_data: "type_defs.CreateAccessPointResultTypeDef" = dataclasses.field()

    AccessPointArn = field("AccessPointArn")
    Alias = field("Alias")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessPointResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPointResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketResult:
    boto3_raw_data: "type_defs.CreateBucketResultTypeDef" = dataclasses.field()

    Location = field("Location")
    BucketArn = field("BucketArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBucketResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobResult:
    boto3_raw_data: "type_defs.CreateJobResultTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateJobResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultiRegionAccessPointResult:
    boto3_raw_data: "type_defs.CreateMultiRegionAccessPointResultTypeDef" = (
        dataclasses.field()
    )

    RequestTokenARN = field("RequestTokenARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMultiRegionAccessPointResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiRegionAccessPointResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMultiRegionAccessPointResult:
    boto3_raw_data: "type_defs.DeleteMultiRegionAccessPointResultTypeDef" = (
        dataclasses.field()
    )

    RequestTokenARN = field("RequestTokenARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMultiRegionAccessPointResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMultiRegionAccessPointResultTypeDef"]
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
class GetAccessGrantResult:
    boto3_raw_data: "type_defs.GetAccessGrantResultTypeDef" = dataclasses.field()

    CreatedAt = field("CreatedAt")
    AccessGrantId = field("AccessGrantId")
    AccessGrantArn = field("AccessGrantArn")

    @cached_property
    def Grantee(self):  # pragma: no cover
        return Grantee.make_one(self.boto3_raw_data["Grantee"])

    Permission = field("Permission")
    AccessGrantsLocationId = field("AccessGrantsLocationId")

    @cached_property
    def AccessGrantsLocationConfiguration(self):  # pragma: no cover
        return AccessGrantsLocationConfiguration.make_one(
            self.boto3_raw_data["AccessGrantsLocationConfiguration"]
        )

    GrantScope = field("GrantScope")
    ApplicationArn = field("ApplicationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessGrantResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessGrantResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessGrantsInstanceForPrefixResult:
    boto3_raw_data: "type_defs.GetAccessGrantsInstanceForPrefixResultTypeDef" = (
        dataclasses.field()
    )

    AccessGrantsInstanceArn = field("AccessGrantsInstanceArn")
    AccessGrantsInstanceId = field("AccessGrantsInstanceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessGrantsInstanceForPrefixResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessGrantsInstanceForPrefixResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessGrantsInstanceResourcePolicyResult:
    boto3_raw_data: "type_defs.GetAccessGrantsInstanceResourcePolicyResultTypeDef" = (
        dataclasses.field()
    )

    Policy = field("Policy")
    Organization = field("Organization")
    CreatedAt = field("CreatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessGrantsInstanceResourcePolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessGrantsInstanceResourcePolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessGrantsInstanceResult:
    boto3_raw_data: "type_defs.GetAccessGrantsInstanceResultTypeDef" = (
        dataclasses.field()
    )

    AccessGrantsInstanceArn = field("AccessGrantsInstanceArn")
    AccessGrantsInstanceId = field("AccessGrantsInstanceId")
    IdentityCenterArn = field("IdentityCenterArn")
    IdentityCenterInstanceArn = field("IdentityCenterInstanceArn")
    IdentityCenterApplicationArn = field("IdentityCenterApplicationArn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccessGrantsInstanceResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessGrantsInstanceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessGrantsLocationResult:
    boto3_raw_data: "type_defs.GetAccessGrantsLocationResultTypeDef" = (
        dataclasses.field()
    )

    CreatedAt = field("CreatedAt")
    AccessGrantsLocationId = field("AccessGrantsLocationId")
    AccessGrantsLocationArn = field("AccessGrantsLocationArn")
    LocationScope = field("LocationScope")
    IAMRoleArn = field("IAMRoleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccessGrantsLocationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessGrantsLocationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointPolicyForObjectLambdaResult:
    boto3_raw_data: "type_defs.GetAccessPointPolicyForObjectLambdaResultTypeDef" = (
        dataclasses.field()
    )

    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessPointPolicyForObjectLambdaResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointPolicyForObjectLambdaResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointPolicyResult:
    boto3_raw_data: "type_defs.GetAccessPointPolicyResultTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessPointPolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketPolicyResult:
    boto3_raw_data: "type_defs.GetBucketPolicyResultTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketPolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketResult:
    boto3_raw_data: "type_defs.GetBucketResultTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    PublicAccessBlockEnabled = field("PublicAccessBlockEnabled")
    CreationDate = field("CreationDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBucketResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetBucketResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketVersioningResult:
    boto3_raw_data: "type_defs.GetBucketVersioningResultTypeDef" = dataclasses.field()

    Status = field("Status")
    MFADelete = field("MFADelete")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketVersioningResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketVersioningResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResult:
    boto3_raw_data: "type_defs.ListTagsForResourceResultTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccessGrantsInstanceResourcePolicyResult:
    boto3_raw_data: "type_defs.PutAccessGrantsInstanceResourcePolicyResultTypeDef" = (
        dataclasses.field()
    )

    Policy = field("Policy")
    Organization = field("Organization")
    CreatedAt = field("CreatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAccessGrantsInstanceResourcePolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccessGrantsInstanceResourcePolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMultiRegionAccessPointPolicyResult:
    boto3_raw_data: "type_defs.PutMultiRegionAccessPointPolicyResultTypeDef" = (
        dataclasses.field()
    )

    RequestTokenARN = field("RequestTokenARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutMultiRegionAccessPointPolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMultiRegionAccessPointPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessGrantsLocationResult:
    boto3_raw_data: "type_defs.UpdateAccessGrantsLocationResultTypeDef" = (
        dataclasses.field()
    )

    CreatedAt = field("CreatedAt")
    AccessGrantsLocationId = field("AccessGrantsLocationId")
    AccessGrantsLocationArn = field("AccessGrantsLocationArn")
    LocationScope = field("LocationScope")
    IAMRoleArn = field("IAMRoleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAccessGrantsLocationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessGrantsLocationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobPriorityResult:
    boto3_raw_data: "type_defs.UpdateJobPriorityResultTypeDef" = dataclasses.field()

    JobId = field("JobId")
    Priority = field("Priority")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJobPriorityResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobPriorityResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateJobStatusResult:
    boto3_raw_data: "type_defs.UpdateJobStatusResultTypeDef" = dataclasses.field()

    JobId = field("JobId")
    Status = field("Status")
    StatusUpdateReason = field("StatusUpdateReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateJobStatusResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateJobStatusResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPointForObjectLambdaResult:
    boto3_raw_data: "type_defs.CreateAccessPointForObjectLambdaResultTypeDef" = (
        dataclasses.field()
    )

    ObjectLambdaAccessPointArn = field("ObjectLambdaAccessPointArn")

    @cached_property
    def Alias(self):  # pragma: no cover
        return ObjectLambdaAccessPointAlias.make_one(self.boto3_raw_data["Alias"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAccessPointForObjectLambdaResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPointForObjectLambdaResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLambdaAccessPoint:
    boto3_raw_data: "type_defs.ObjectLambdaAccessPointTypeDef" = dataclasses.field()

    Name = field("Name")
    ObjectLambdaAccessPointArn = field("ObjectLambdaAccessPointArn")

    @cached_property
    def Alias(self):  # pragma: no cover
        return ObjectLambdaAccessPointAlias.make_one(self.boto3_raw_data["Alias"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectLambdaAccessPointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLambdaAccessPointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointForObjectLambdaResult:
    boto3_raw_data: "type_defs.GetAccessPointForObjectLambdaResultTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def PublicAccessBlockConfiguration(self):  # pragma: no cover
        return PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["PublicAccessBlockConfiguration"]
        )

    CreationDate = field("CreationDate")

    @cached_property
    def Alias(self):  # pragma: no cover
        return ObjectLambdaAccessPointAlias.make_one(self.boto3_raw_data["Alias"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessPointForObjectLambdaResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointForObjectLambdaResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointResult:
    boto3_raw_data: "type_defs.GetAccessPointResultTypeDef" = dataclasses.field()

    Name = field("Name")
    Bucket = field("Bucket")
    NetworkOrigin = field("NetworkOrigin")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["VpcConfiguration"])

    @cached_property
    def PublicAccessBlockConfiguration(self):  # pragma: no cover
        return PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["PublicAccessBlockConfiguration"]
        )

    CreationDate = field("CreationDate")
    Alias = field("Alias")
    AccessPointArn = field("AccessPointArn")
    Endpoints = field("Endpoints")
    BucketAccountId = field("BucketAccountId")
    DataSourceId = field("DataSourceId")
    DataSourceType = field("DataSourceType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessPointResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicAccessBlockOutput:
    boto3_raw_data: "type_defs.GetPublicAccessBlockOutputTypeDef" = dataclasses.field()

    @cached_property
    def PublicAccessBlockConfiguration(self):  # pragma: no cover
        return PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["PublicAccessBlockConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicAccessBlockOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicAccessBlockOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPublicAccessBlockRequest:
    boto3_raw_data: "type_defs.PutPublicAccessBlockRequestTypeDef" = dataclasses.field()

    @cached_property
    def PublicAccessBlockConfiguration(self):  # pragma: no cover
        return PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["PublicAccessBlockConfiguration"]
        )

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutPublicAccessBlockRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPublicAccessBlockRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBucketRequest:
    boto3_raw_data: "type_defs.CreateBucketRequestTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ACL = field("ACL")

    @cached_property
    def CreateBucketConfiguration(self):  # pragma: no cover
        return CreateBucketConfiguration.make_one(
            self.boto3_raw_data["CreateBucketConfiguration"]
        )

    GrantFullControl = field("GrantFullControl")
    GrantRead = field("GrantRead")
    GrantReadACP = field("GrantReadACP")
    GrantWrite = field("GrantWrite")
    GrantWriteACP = field("GrantWriteACP")
    ObjectLockEnabledForBucket = field("ObjectLockEnabledForBucket")
    OutpostId = field("OutpostId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBucketRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBucketRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketTaggingResult:
    boto3_raw_data: "type_defs.GetBucketTaggingResultTypeDef" = dataclasses.field()

    @cached_property
    def TagSet(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["TagSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketTaggingResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketTaggingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobTaggingResult:
    boto3_raw_data: "type_defs.GetJobTaggingResultTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetJobTaggingResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetJobTaggingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRuleAndOperatorOutput:
    boto3_raw_data: "type_defs.LifecycleRuleAndOperatorOutputTypeDef" = (
        dataclasses.field()
    )

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["Tags"])

    ObjectSizeGreaterThan = field("ObjectSizeGreaterThan")
    ObjectSizeLessThan = field("ObjectSizeLessThan")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LifecycleRuleAndOperatorOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleRuleAndOperatorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRuleAndOperator:
    boto3_raw_data: "type_defs.LifecycleRuleAndOperatorTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["Tags"])

    ObjectSizeGreaterThan = field("ObjectSizeGreaterThan")
    ObjectSizeLessThan = field("ObjectSizeLessThan")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleRuleAndOperatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleRuleAndOperatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutJobTaggingRequest:
    boto3_raw_data: "type_defs.PutJobTaggingRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    JobId = field("JobId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutJobTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutJobTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRuleAndOperatorOutput:
    boto3_raw_data: "type_defs.ReplicationRuleAndOperatorOutputTypeDef" = (
        dataclasses.field()
    )

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReplicationRuleAndOperatorOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRuleAndOperatorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRuleAndOperator:
    boto3_raw_data: "type_defs.ReplicationRuleAndOperatorTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tags(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleAndOperatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRuleAndOperatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SetObjectTaggingOperationOutput:
    boto3_raw_data: "type_defs.S3SetObjectTaggingOperationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TagSet(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["TagSet"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3SetObjectTaggingOperationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3SetObjectTaggingOperationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SetObjectTaggingOperation:
    boto3_raw_data: "type_defs.S3SetObjectTaggingOperationTypeDef" = dataclasses.field()

    @cached_property
    def TagSet(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["TagSet"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3SetObjectTaggingOperationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3SetObjectTaggingOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tagging:
    boto3_raw_data: "type_defs.TaggingTypeDef" = dataclasses.field()

    @cached_property
    def TagSet(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["TagSet"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaggingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaggingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultiRegionAccessPointInputOutput:
    boto3_raw_data: "type_defs.CreateMultiRegionAccessPointInputOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def Regions(self):  # pragma: no cover
        return Region.make_many(self.boto3_raw_data["Regions"])

    @cached_property
    def PublicAccessBlock(self):  # pragma: no cover
        return PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["PublicAccessBlock"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMultiRegionAccessPointInputOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiRegionAccessPointInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultiRegionAccessPointInput:
    boto3_raw_data: "type_defs.CreateMultiRegionAccessPointInputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def Regions(self):  # pragma: no cover
        return Region.make_many(self.boto3_raw_data["Regions"])

    @cached_property
    def PublicAccessBlock(self):  # pragma: no cover
        return PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["PublicAccessBlock"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMultiRegionAccessPointInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiRegionAccessPointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataAccessResult:
    boto3_raw_data: "type_defs.GetDataAccessResultTypeDef" = dataclasses.field()

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["Credentials"])

    MatchedGrantTarget = field("MatchedGrantTarget")

    @cached_property
    def Grantee(self):  # pragma: no cover
        return Grantee.make_one(self.boto3_raw_data["Grantee"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataAccessResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataAccessResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneratedManifestEncryptionOutput:
    boto3_raw_data: "type_defs.GeneratedManifestEncryptionOutputTypeDef" = (
        dataclasses.field()
    )

    SSES3 = field("SSES3")

    @cached_property
    def SSEKMS(self):  # pragma: no cover
        return SSEKMSEncryption.make_one(self.boto3_raw_data["SSEKMS"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GeneratedManifestEncryptionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeneratedManifestEncryptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneratedManifestEncryption:
    boto3_raw_data: "type_defs.GeneratedManifestEncryptionTypeDef" = dataclasses.field()

    SSES3 = field("SSES3")

    @cached_property
    def SSEKMS(self):  # pragma: no cover
        return SSEKMSEncryption.make_one(self.boto3_raw_data["SSEKMS"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeneratedManifestEncryptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeneratedManifestEncryptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointPolicyStatusForObjectLambdaResult:
    boto3_raw_data: (
        "type_defs.GetAccessPointPolicyStatusForObjectLambdaResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PolicyStatus(self):  # pragma: no cover
        return PolicyStatus.make_one(self.boto3_raw_data["PolicyStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessPointPolicyStatusForObjectLambdaResultTypeDef"
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
                "type_defs.GetAccessPointPolicyStatusForObjectLambdaResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointPolicyStatusResult:
    boto3_raw_data: "type_defs.GetAccessPointPolicyStatusResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PolicyStatus(self):  # pragma: no cover
        return PolicyStatus.make_one(self.boto3_raw_data["PolicyStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccessPointPolicyStatusResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointPolicyStatusResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMultiRegionAccessPointPolicyStatusResult:
    boto3_raw_data: "type_defs.GetMultiRegionAccessPointPolicyStatusResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Established(self):  # pragma: no cover
        return PolicyStatus.make_one(self.boto3_raw_data["Established"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMultiRegionAccessPointPolicyStatusResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMultiRegionAccessPointPolicyStatusResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointScopeResult:
    boto3_raw_data: "type_defs.GetAccessPointScopeResultTypeDef" = dataclasses.field()

    @cached_property
    def Scope(self):  # pragma: no cover
        return ScopeOutput.make_one(self.boto3_raw_data["Scope"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessPointScopeResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPointScopeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMultiRegionAccessPointRoutesResult:
    boto3_raw_data: "type_defs.GetMultiRegionAccessPointRoutesResultTypeDef" = (
        dataclasses.field()
    )

    Mrap = field("Mrap")

    @cached_property
    def Routes(self):  # pragma: no cover
        return MultiRegionAccessPointRoute.make_many(self.boto3_raw_data["Routes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMultiRegionAccessPointRoutesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMultiRegionAccessPointRoutesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubmitMultiRegionAccessPointRoutesRequest:
    boto3_raw_data: "type_defs.SubmitMultiRegionAccessPointRoutesRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Mrap = field("Mrap")

    @cached_property
    def RouteUpdates(self):  # pragma: no cover
        return MultiRegionAccessPointRoute.make_many(
            self.boto3_raw_data["RouteUpdates"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SubmitMultiRegionAccessPointRoutesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubmitMultiRegionAccessPointRoutesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageLensConfigurationTaggingResult:
    boto3_raw_data: "type_defs.GetStorageLensConfigurationTaggingResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Tags(self):  # pragma: no cover
        return StorageLensTag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetStorageLensConfigurationTaggingResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageLensConfigurationTaggingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutStorageLensConfigurationTaggingRequest:
    boto3_raw_data: "type_defs.PutStorageLensConfigurationTaggingRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigId = field("ConfigId")
    AccountId = field("AccountId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return StorageLensTag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutStorageLensConfigurationTaggingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutStorageLensConfigurationTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleExpiration:
    boto3_raw_data: "type_defs.LifecycleExpirationTypeDef" = dataclasses.field()

    Date = field("Date")
    Days = field("Days")
    ExpiredObjectDeleteMarker = field("ExpiredObjectDeleteMarker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleExpirationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleExpirationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ObjectMetadata:
    boto3_raw_data: "type_defs.S3ObjectMetadataTypeDef" = dataclasses.field()

    CacheControl = field("CacheControl")
    ContentDisposition = field("ContentDisposition")
    ContentEncoding = field("ContentEncoding")
    ContentLanguage = field("ContentLanguage")
    UserMetadata = field("UserMetadata")
    ContentLength = field("ContentLength")
    ContentMD5 = field("ContentMD5")
    ContentType = field("ContentType")
    HttpExpiresDate = field("HttpExpiresDate")
    RequesterCharged = field("RequesterCharged")
    SSEAlgorithm = field("SSEAlgorithm")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ObjectMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Retention:
    boto3_raw_data: "type_defs.S3RetentionTypeDef" = dataclasses.field()

    RetainUntilDate = field("RetainUntilDate")
    Mode = field("Mode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3RetentionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3RetentionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Transition:
    boto3_raw_data: "type_defs.TransitionTypeDef" = dataclasses.field()

    Date = field("Date")
    Days = field("Days")
    StorageClass = field("StorageClass")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TransitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TransitionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3GeneratedManifestDescriptor:
    boto3_raw_data: "type_defs.S3GeneratedManifestDescriptorTypeDef" = (
        dataclasses.field()
    )

    Format = field("Format")

    @cached_property
    def Location(self):  # pragma: no cover
        return JobManifestLocation.make_one(self.boto3_raw_data["Location"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3GeneratedManifestDescriptorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3GeneratedManifestDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobManifestOutput:
    boto3_raw_data: "type_defs.JobManifestOutputTypeDef" = dataclasses.field()

    @cached_property
    def Spec(self):  # pragma: no cover
        return JobManifestSpecOutput.make_one(self.boto3_raw_data["Spec"])

    @cached_property
    def Location(self):  # pragma: no cover
        return JobManifestLocation.make_one(self.boto3_raw_data["Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobManifestOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobManifestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobManifest:
    boto3_raw_data: "type_defs.JobManifestTypeDef" = dataclasses.field()

    @cached_property
    def Spec(self):  # pragma: no cover
        return JobManifestSpec.make_one(self.boto3_raw_data["Spec"])

    @cached_property
    def Location(self):  # pragma: no cover
        return JobManifestLocation.make_one(self.boto3_raw_data["Location"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobManifestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobManifestTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobProgressSummary:
    boto3_raw_data: "type_defs.JobProgressSummaryTypeDef" = dataclasses.field()

    TotalNumberOfTasks = field("TotalNumberOfTasks")
    NumberOfTasksSucceeded = field("NumberOfTasksSucceeded")
    NumberOfTasksFailed = field("NumberOfTasksFailed")

    @cached_property
    def Timers(self):  # pragma: no cover
        return JobTimers.make_one(self.boto3_raw_data["Timers"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobProgressSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobProgressSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessGrantsInstancesResult:
    boto3_raw_data: "type_defs.ListAccessGrantsInstancesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessGrantsInstancesList(self):  # pragma: no cover
        return ListAccessGrantsInstanceEntry.make_many(
            self.boto3_raw_data["AccessGrantsInstancesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccessGrantsInstancesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessGrantsInstancesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessGrantsLocationsResult:
    boto3_raw_data: "type_defs.ListAccessGrantsLocationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessGrantsLocationsList(self):  # pragma: no cover
        return ListAccessGrantsLocationsEntry.make_many(
            self.boto3_raw_data["AccessGrantsLocationsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccessGrantsLocationsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessGrantsLocationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPointsForDirectoryBucketsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAccessPointsForDirectoryBucketsRequestPaginateTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")
    DirectoryBucket = field("DirectoryBucket")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessPointsForDirectoryBucketsRequestPaginateTypeDef"
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
                "type_defs.ListAccessPointsForDirectoryBucketsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPointsForObjectLambdaRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAccessPointsForObjectLambdaRequestPaginateTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessPointsForObjectLambdaRequestPaginateTypeDef"
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
                "type_defs.ListAccessPointsForObjectLambdaRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCallerAccessGrantsRequestPaginate:
    boto3_raw_data: "type_defs.ListCallerAccessGrantsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    GrantScope = field("GrantScope")
    AllowedByApplication = field("AllowedByApplication")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCallerAccessGrantsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCallerAccessGrantsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCallerAccessGrantsResult:
    boto3_raw_data: "type_defs.ListCallerAccessGrantsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CallerAccessGrantsList(self):  # pragma: no cover
        return ListCallerAccessGrantsEntry.make_many(
            self.boto3_raw_data["CallerAccessGrantsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCallerAccessGrantsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCallerAccessGrantsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRegionalBucketsResult:
    boto3_raw_data: "type_defs.ListRegionalBucketsResultTypeDef" = dataclasses.field()

    @cached_property
    def RegionalBucketList(self):  # pragma: no cover
        return RegionalBucket.make_many(self.boto3_raw_data["RegionalBucketList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRegionalBucketsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRegionalBucketsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageLensConfigurationsResult:
    boto3_raw_data: "type_defs.ListStorageLensConfigurationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StorageLensConfigurationList(self):  # pragma: no cover
        return ListStorageLensConfigurationEntry.make_many(
            self.boto3_raw_data["StorageLensConfigurationList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStorageLensConfigurationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageLensConfigurationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStorageLensGroupsResult:
    boto3_raw_data: "type_defs.ListStorageLensGroupsResultTypeDef" = dataclasses.field()

    @cached_property
    def StorageLensGroupList(self):  # pragma: no cover
        return ListStorageLensGroupEntry.make_many(
            self.boto3_raw_data["StorageLensGroupList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStorageLensGroupsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStorageLensGroupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroupAndOperatorOutput:
    boto3_raw_data: "type_defs.StorageLensGroupAndOperatorOutputTypeDef" = (
        dataclasses.field()
    )

    MatchAnyPrefix = field("MatchAnyPrefix")
    MatchAnySuffix = field("MatchAnySuffix")

    @cached_property
    def MatchAnyTag(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["MatchAnyTag"])

    @cached_property
    def MatchObjectAge(self):  # pragma: no cover
        return MatchObjectAge.make_one(self.boto3_raw_data["MatchObjectAge"])

    @cached_property
    def MatchObjectSize(self):  # pragma: no cover
        return MatchObjectSize.make_one(self.boto3_raw_data["MatchObjectSize"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StorageLensGroupAndOperatorOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupAndOperatorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroupAndOperator:
    boto3_raw_data: "type_defs.StorageLensGroupAndOperatorTypeDef" = dataclasses.field()

    MatchAnyPrefix = field("MatchAnyPrefix")
    MatchAnySuffix = field("MatchAnySuffix")

    @cached_property
    def MatchAnyTag(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["MatchAnyTag"])

    @cached_property
    def MatchObjectAge(self):  # pragma: no cover
        return MatchObjectAge.make_one(self.boto3_raw_data["MatchObjectAge"])

    @cached_property
    def MatchObjectSize(self):  # pragma: no cover
        return MatchObjectSize.make_one(self.boto3_raw_data["MatchObjectSize"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageLensGroupAndOperatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupAndOperatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroupOrOperatorOutput:
    boto3_raw_data: "type_defs.StorageLensGroupOrOperatorOutputTypeDef" = (
        dataclasses.field()
    )

    MatchAnyPrefix = field("MatchAnyPrefix")
    MatchAnySuffix = field("MatchAnySuffix")

    @cached_property
    def MatchAnyTag(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["MatchAnyTag"])

    @cached_property
    def MatchObjectAge(self):  # pragma: no cover
        return MatchObjectAge.make_one(self.boto3_raw_data["MatchObjectAge"])

    @cached_property
    def MatchObjectSize(self):  # pragma: no cover
        return MatchObjectSize.make_one(self.boto3_raw_data["MatchObjectSize"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StorageLensGroupOrOperatorOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupOrOperatorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroupOrOperator:
    boto3_raw_data: "type_defs.StorageLensGroupOrOperatorTypeDef" = dataclasses.field()

    MatchAnyPrefix = field("MatchAnyPrefix")
    MatchAnySuffix = field("MatchAnySuffix")

    @cached_property
    def MatchAnyTag(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["MatchAnyTag"])

    @cached_property
    def MatchObjectAge(self):  # pragma: no cover
        return MatchObjectAge.make_one(self.boto3_raw_data["MatchObjectAge"])

    @cached_property
    def MatchObjectSize(self):  # pragma: no cover
        return MatchObjectSize.make_one(self.boto3_raw_data["MatchObjectSize"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageLensGroupOrOperatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupOrOperatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Metrics:
    boto3_raw_data: "type_defs.MetricsTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def EventThreshold(self):  # pragma: no cover
        return ReplicationTimeValue.make_one(self.boto3_raw_data["EventThreshold"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTime:
    boto3_raw_data: "type_defs.ReplicationTimeTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def Time(self):  # pragma: no cover
        return ReplicationTimeValue.make_one(self.boto3_raw_data["Time"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicationTimeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiRegionAccessPointPolicyDocument:
    boto3_raw_data: "type_defs.MultiRegionAccessPointPolicyDocumentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Established(self):  # pragma: no cover
        return EstablishedMultiRegionAccessPointPolicy.make_one(
            self.boto3_raw_data["Established"]
        )

    @cached_property
    def Proposed(self):  # pragma: no cover
        return ProposedMultiRegionAccessPointPolicy.make_one(
            self.boto3_raw_data["Proposed"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultiRegionAccessPointPolicyDocumentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiRegionAccessPointPolicyDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiRegionAccessPointsAsyncResponse:
    boto3_raw_data: "type_defs.MultiRegionAccessPointsAsyncResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Regions(self):  # pragma: no cover
        return MultiRegionAccessPointRegionalResponse.make_many(
            self.boto3_raw_data["Regions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MultiRegionAccessPointsAsyncResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiRegionAccessPointsAsyncResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiRegionAccessPointReport:
    boto3_raw_data: "type_defs.MultiRegionAccessPointReportTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Alias = field("Alias")
    CreatedAt = field("CreatedAt")

    @cached_property
    def PublicAccessBlock(self):  # pragma: no cover
        return PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["PublicAccessBlock"]
        )

    Status = field("Status")

    @cached_property
    def Regions(self):  # pragma: no cover
        return RegionReport.make_many(self.boto3_raw_data["Regions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiRegionAccessPointReportTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiRegionAccessPointReportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectEncryptionFilterOutput:
    boto3_raw_data: "type_defs.ObjectEncryptionFilterOutputTypeDef" = (
        dataclasses.field()
    )

    SSES3 = field("SSES3")

    @cached_property
    def SSEKMS(self):  # pragma: no cover
        return SSEKMSFilter.make_one(self.boto3_raw_data["SSEKMS"])

    @cached_property
    def DSSEKMS(self):  # pragma: no cover
        return DSSEKMSFilter.make_one(self.boto3_raw_data["DSSEKMS"])

    SSEC = field("SSEC")
    NOTSSE = field("NOTSSE")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectEncryptionFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectEncryptionFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectEncryptionFilter:
    boto3_raw_data: "type_defs.ObjectEncryptionFilterTypeDef" = dataclasses.field()

    SSES3 = field("SSES3")

    @cached_property
    def SSEKMS(self):  # pragma: no cover
        return SSEKMSFilter.make_one(self.boto3_raw_data["SSEKMS"])

    @cached_property
    def DSSEKMS(self):  # pragma: no cover
        return DSSEKMSFilter.make_one(self.boto3_raw_data["DSSEKMS"])

    SSEC = field("SSEC")
    NOTSSE = field("NOTSSE")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectEncryptionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectEncryptionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrefixLevelStorageMetrics:
    boto3_raw_data: "type_defs.PrefixLevelStorageMetricsTypeDef" = dataclasses.field()

    IsEnabled = field("IsEnabled")

    @cached_property
    def SelectionCriteria(self):  # pragma: no cover
        return SelectionCriteria.make_one(self.boto3_raw_data["SelectionCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrefixLevelStorageMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrefixLevelStorageMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketVersioningRequest:
    boto3_raw_data: "type_defs.PutBucketVersioningRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @cached_property
    def VersioningConfiguration(self):  # pragma: no cover
        return VersioningConfiguration.make_one(
            self.boto3_raw_data["VersioningConfiguration"]
        )

    MFA = field("MFA")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketVersioningRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketVersioningRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Grant:
    boto3_raw_data: "type_defs.S3GrantTypeDef" = dataclasses.field()

    @cached_property
    def Grantee(self):  # pragma: no cover
        return S3Grantee.make_one(self.boto3_raw_data["Grantee"])

    Permission = field("Permission")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3GrantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3GrantTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SetObjectLegalHoldOperation:
    boto3_raw_data: "type_defs.S3SetObjectLegalHoldOperationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LegalHold(self):  # pragma: no cover
        return S3ObjectLockLegalHold.make_one(self.boto3_raw_data["LegalHold"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3SetObjectLegalHoldOperationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3SetObjectLegalHoldOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SetObjectRetentionOperationOutput:
    boto3_raw_data: "type_defs.S3SetObjectRetentionOperationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Retention(self):  # pragma: no cover
        return S3RetentionOutput.make_one(self.boto3_raw_data["Retention"])

    BypassGovernanceRetention = field("BypassGovernanceRetention")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.S3SetObjectRetentionOperationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3SetObjectRetentionOperationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensDataExportEncryptionOutput:
    boto3_raw_data: "type_defs.StorageLensDataExportEncryptionOutputTypeDef" = (
        dataclasses.field()
    )

    SSES3 = field("SSES3")

    @cached_property
    def SSEKMS(self):  # pragma: no cover
        return SSEKMS.make_one(self.boto3_raw_data["SSEKMS"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StorageLensDataExportEncryptionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensDataExportEncryptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensDataExportEncryption:
    boto3_raw_data: "type_defs.StorageLensDataExportEncryptionTypeDef" = (
        dataclasses.field()
    )

    SSES3 = field("SSES3")

    @cached_property
    def SSEKMS(self):  # pragma: no cover
        return SSEKMS.make_one(self.boto3_raw_data["SSEKMS"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StorageLensDataExportEncryptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensDataExportEncryptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceSelectionCriteria:
    boto3_raw_data: "type_defs.SourceSelectionCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def SseKmsEncryptedObjects(self):  # pragma: no cover
        return SseKmsEncryptedObjects.make_one(
            self.boto3_raw_data["SseKmsEncryptedObjects"]
        )

    @cached_property
    def ReplicaModifications(self):  # pragma: no cover
        return ReplicaModifications.make_one(
            self.boto3_raw_data["ReplicaModifications"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceSelectionCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceSelectionCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroupLevelOutput:
    boto3_raw_data: "type_defs.StorageLensGroupLevelOutputTypeDef" = dataclasses.field()

    @cached_property
    def SelectionCriteria(self):  # pragma: no cover
        return StorageLensGroupLevelSelectionCriteriaOutput.make_one(
            self.boto3_raw_data["SelectionCriteria"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageLensGroupLevelOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupLevelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroupLevel:
    boto3_raw_data: "type_defs.StorageLensGroupLevelTypeDef" = dataclasses.field()

    @cached_property
    def SelectionCriteria(self):  # pragma: no cover
        return StorageLensGroupLevelSelectionCriteria.make_one(
            self.boto3_raw_data["SelectionCriteria"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageLensGroupLevelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupLevelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPointsForDirectoryBucketsResult:
    boto3_raw_data: "type_defs.ListAccessPointsForDirectoryBucketsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessPointList(self):  # pragma: no cover
        return AccessPoint.make_many(self.boto3_raw_data["AccessPointList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessPointsForDirectoryBucketsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPointsForDirectoryBucketsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPointsResult:
    boto3_raw_data: "type_defs.ListAccessPointsResultTypeDef" = dataclasses.field()

    @cached_property
    def AccessPointList(self):  # pragma: no cover
        return AccessPoint.make_many(self.boto3_raw_data["AccessPointList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessPointsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPointsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLambdaTransformationConfigurationOutput:
    boto3_raw_data: "type_defs.ObjectLambdaTransformationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Actions = field("Actions")

    @cached_property
    def ContentTransformation(self):  # pragma: no cover
        return ObjectLambdaContentTransformation.make_one(
            self.boto3_raw_data["ContentTransformation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ObjectLambdaTransformationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLambdaTransformationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLambdaTransformationConfiguration:
    boto3_raw_data: "type_defs.ObjectLambdaTransformationConfigurationTypeDef" = (
        dataclasses.field()
    )

    Actions = field("Actions")

    @cached_property
    def ContentTransformation(self):  # pragma: no cover
        return ObjectLambdaContentTransformation.make_one(
            self.boto3_raw_data["ContentTransformation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ObjectLambdaTransformationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLambdaTransformationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessGrantsResult:
    boto3_raw_data: "type_defs.ListAccessGrantsResultTypeDef" = dataclasses.field()

    @cached_property
    def AccessGrantsList(self):  # pragma: no cover
        return ListAccessGrantEntry.make_many(self.boto3_raw_data["AccessGrantsList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessGrantsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessGrantsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPointsForObjectLambdaResult:
    boto3_raw_data: "type_defs.ListAccessPointsForObjectLambdaResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ObjectLambdaAccessPointList(self):  # pragma: no cover
        return ObjectLambdaAccessPoint.make_many(
            self.boto3_raw_data["ObjectLambdaAccessPointList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessPointsForObjectLambdaResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPointsForObjectLambdaResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRuleFilterOutput:
    boto3_raw_data: "type_defs.LifecycleRuleFilterOutputTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return S3Tag.make_one(self.boto3_raw_data["Tag"])

    @cached_property
    def And(self):  # pragma: no cover
        return LifecycleRuleAndOperatorOutput.make_one(self.boto3_raw_data["And"])

    ObjectSizeGreaterThan = field("ObjectSizeGreaterThan")
    ObjectSizeLessThan = field("ObjectSizeLessThan")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleRuleFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleRuleFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRuleFilterOutput:
    boto3_raw_data: "type_defs.ReplicationRuleFilterOutputTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return S3Tag.make_one(self.boto3_raw_data["Tag"])

    @cached_property
    def And(self):  # pragma: no cover
        return ReplicationRuleAndOperatorOutput.make_one(self.boto3_raw_data["And"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRuleFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRuleFilter:
    boto3_raw_data: "type_defs.ReplicationRuleFilterTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return S3Tag.make_one(self.boto3_raw_data["Tag"])

    @cached_property
    def And(self):  # pragma: no cover
        return ReplicationRuleAndOperator.make_one(self.boto3_raw_data["And"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRuleFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketTaggingRequest:
    boto3_raw_data: "type_defs.PutBucketTaggingRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @cached_property
    def Tagging(self):  # pragma: no cover
        return Tagging.make_one(self.boto3_raw_data["Tagging"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketTaggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketTaggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AsyncRequestParameters:
    boto3_raw_data: "type_defs.AsyncRequestParametersTypeDef" = dataclasses.field()

    @cached_property
    def CreateMultiRegionAccessPointRequest(self):  # pragma: no cover
        return CreateMultiRegionAccessPointInputOutput.make_one(
            self.boto3_raw_data["CreateMultiRegionAccessPointRequest"]
        )

    @cached_property
    def DeleteMultiRegionAccessPointRequest(self):  # pragma: no cover
        return DeleteMultiRegionAccessPointInput.make_one(
            self.boto3_raw_data["DeleteMultiRegionAccessPointRequest"]
        )

    @cached_property
    def PutMultiRegionAccessPointPolicyRequest(self):  # pragma: no cover
        return PutMultiRegionAccessPointPolicyInput.make_one(
            self.boto3_raw_data["PutMultiRegionAccessPointPolicyRequest"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AsyncRequestParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AsyncRequestParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ManifestOutputLocationOutput:
    boto3_raw_data: "type_defs.S3ManifestOutputLocationOutputTypeDef" = (
        dataclasses.field()
    )

    Bucket = field("Bucket")
    ManifestFormat = field("ManifestFormat")
    ExpectedManifestBucketOwner = field("ExpectedManifestBucketOwner")
    ManifestPrefix = field("ManifestPrefix")

    @cached_property
    def ManifestEncryption(self):  # pragma: no cover
        return GeneratedManifestEncryptionOutput.make_one(
            self.boto3_raw_data["ManifestEncryption"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3ManifestOutputLocationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ManifestOutputLocationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ManifestOutputLocation:
    boto3_raw_data: "type_defs.S3ManifestOutputLocationTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    ManifestFormat = field("ManifestFormat")
    ExpectedManifestBucketOwner = field("ExpectedManifestBucketOwner")
    ManifestPrefix = field("ManifestPrefix")

    @cached_property
    def ManifestEncryption(self):  # pragma: no cover
        return GeneratedManifestEncryption.make_one(
            self.boto3_raw_data["ManifestEncryption"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ManifestOutputLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ManifestOutputLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SetObjectRetentionOperation:
    boto3_raw_data: "type_defs.S3SetObjectRetentionOperationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Retention(self):  # pragma: no cover
        return S3Retention.make_one(self.boto3_raw_data["Retention"])

    BypassGovernanceRetention = field("BypassGovernanceRetention")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3SetObjectRetentionOperationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3SetObjectRetentionOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobListDescriptor:
    boto3_raw_data: "type_defs.JobListDescriptorTypeDef" = dataclasses.field()

    JobId = field("JobId")
    Description = field("Description")
    Operation = field("Operation")
    Priority = field("Priority")
    Status = field("Status")
    CreationTime = field("CreationTime")
    TerminationDate = field("TerminationDate")

    @cached_property
    def ProgressSummary(self):  # pragma: no cover
        return JobProgressSummary.make_one(self.boto3_raw_data["ProgressSummary"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobListDescriptorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobListDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroupFilterOutput:
    boto3_raw_data: "type_defs.StorageLensGroupFilterOutputTypeDef" = (
        dataclasses.field()
    )

    MatchAnyPrefix = field("MatchAnyPrefix")
    MatchAnySuffix = field("MatchAnySuffix")

    @cached_property
    def MatchAnyTag(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["MatchAnyTag"])

    @cached_property
    def MatchObjectAge(self):  # pragma: no cover
        return MatchObjectAge.make_one(self.boto3_raw_data["MatchObjectAge"])

    @cached_property
    def MatchObjectSize(self):  # pragma: no cover
        return MatchObjectSize.make_one(self.boto3_raw_data["MatchObjectSize"])

    @cached_property
    def And(self):  # pragma: no cover
        return StorageLensGroupAndOperatorOutput.make_one(self.boto3_raw_data["And"])

    @cached_property
    def Or(self):  # pragma: no cover
        return StorageLensGroupOrOperatorOutput.make_one(self.boto3_raw_data["Or"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageLensGroupFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroupFilter:
    boto3_raw_data: "type_defs.StorageLensGroupFilterTypeDef" = dataclasses.field()

    MatchAnyPrefix = field("MatchAnyPrefix")
    MatchAnySuffix = field("MatchAnySuffix")

    @cached_property
    def MatchAnyTag(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["MatchAnyTag"])

    @cached_property
    def MatchObjectAge(self):  # pragma: no cover
        return MatchObjectAge.make_one(self.boto3_raw_data["MatchObjectAge"])

    @cached_property
    def MatchObjectSize(self):  # pragma: no cover
        return MatchObjectSize.make_one(self.boto3_raw_data["MatchObjectSize"])

    @cached_property
    def And(self):  # pragma: no cover
        return StorageLensGroupAndOperator.make_one(self.boto3_raw_data["And"])

    @cached_property
    def Or(self):  # pragma: no cover
        return StorageLensGroupOrOperator.make_one(self.boto3_raw_data["Or"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageLensGroupFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupFilterTypeDef"]
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

    Bucket = field("Bucket")
    Account = field("Account")

    @cached_property
    def ReplicationTime(self):  # pragma: no cover
        return ReplicationTime.make_one(self.boto3_raw_data["ReplicationTime"])

    @cached_property
    def AccessControlTranslation(self):  # pragma: no cover
        return AccessControlTranslation.make_one(
            self.boto3_raw_data["AccessControlTranslation"]
        )

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def Metrics(self):  # pragma: no cover
        return Metrics.make_one(self.boto3_raw_data["Metrics"])

    StorageClass = field("StorageClass")

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
class GetMultiRegionAccessPointPolicyResult:
    boto3_raw_data: "type_defs.GetMultiRegionAccessPointPolicyResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Policy(self):  # pragma: no cover
        return MultiRegionAccessPointPolicyDocument.make_one(
            self.boto3_raw_data["Policy"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMultiRegionAccessPointPolicyResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMultiRegionAccessPointPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AsyncResponseDetails:
    boto3_raw_data: "type_defs.AsyncResponseDetailsTypeDef" = dataclasses.field()

    @cached_property
    def MultiRegionAccessPointDetails(self):  # pragma: no cover
        return MultiRegionAccessPointsAsyncResponse.make_one(
            self.boto3_raw_data["MultiRegionAccessPointDetails"]
        )

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return AsyncErrorDetails.make_one(self.boto3_raw_data["ErrorDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AsyncResponseDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AsyncResponseDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMultiRegionAccessPointResult:
    boto3_raw_data: "type_defs.GetMultiRegionAccessPointResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessPoint(self):  # pragma: no cover
        return MultiRegionAccessPointReport.make_one(self.boto3_raw_data["AccessPoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMultiRegionAccessPointResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMultiRegionAccessPointResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMultiRegionAccessPointsResult:
    boto3_raw_data: "type_defs.ListMultiRegionAccessPointsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessPoints(self):  # pragma: no cover
        return MultiRegionAccessPointReport.make_many(
            self.boto3_raw_data["AccessPoints"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMultiRegionAccessPointsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMultiRegionAccessPointsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobManifestGeneratorFilterOutput:
    boto3_raw_data: "type_defs.JobManifestGeneratorFilterOutputTypeDef" = (
        dataclasses.field()
    )

    EligibleForReplication = field("EligibleForReplication")
    CreatedAfter = field("CreatedAfter")
    CreatedBefore = field("CreatedBefore")
    ObjectReplicationStatuses = field("ObjectReplicationStatuses")

    @cached_property
    def KeyNameConstraint(self):  # pragma: no cover
        return KeyNameConstraintOutput.make_one(
            self.boto3_raw_data["KeyNameConstraint"]
        )

    ObjectSizeGreaterThanBytes = field("ObjectSizeGreaterThanBytes")
    ObjectSizeLessThanBytes = field("ObjectSizeLessThanBytes")
    MatchAnyStorageClass = field("MatchAnyStorageClass")

    @cached_property
    def MatchAnyObjectEncryption(self):  # pragma: no cover
        return ObjectEncryptionFilterOutput.make_many(
            self.boto3_raw_data["MatchAnyObjectEncryption"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.JobManifestGeneratorFilterOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobManifestGeneratorFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobManifestGeneratorFilter:
    boto3_raw_data: "type_defs.JobManifestGeneratorFilterTypeDef" = dataclasses.field()

    EligibleForReplication = field("EligibleForReplication")
    CreatedAfter = field("CreatedAfter")
    CreatedBefore = field("CreatedBefore")
    ObjectReplicationStatuses = field("ObjectReplicationStatuses")

    @cached_property
    def KeyNameConstraint(self):  # pragma: no cover
        return KeyNameConstraint.make_one(self.boto3_raw_data["KeyNameConstraint"])

    ObjectSizeGreaterThanBytes = field("ObjectSizeGreaterThanBytes")
    ObjectSizeLessThanBytes = field("ObjectSizeLessThanBytes")
    MatchAnyStorageClass = field("MatchAnyStorageClass")

    @cached_property
    def MatchAnyObjectEncryption(self):  # pragma: no cover
        return ObjectEncryptionFilter.make_many(
            self.boto3_raw_data["MatchAnyObjectEncryption"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobManifestGeneratorFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobManifestGeneratorFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrefixLevel:
    boto3_raw_data: "type_defs.PrefixLevelTypeDef" = dataclasses.field()

    @cached_property
    def StorageMetrics(self):  # pragma: no cover
        return PrefixLevelStorageMetrics.make_one(self.boto3_raw_data["StorageMetrics"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrefixLevelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrefixLevelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessControlListOutput:
    boto3_raw_data: "type_defs.S3AccessControlListOutputTypeDef" = dataclasses.field()

    @cached_property
    def Owner(self):  # pragma: no cover
        return S3ObjectOwner.make_one(self.boto3_raw_data["Owner"])

    @cached_property
    def Grants(self):  # pragma: no cover
        return S3Grant.make_many(self.boto3_raw_data["Grants"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3AccessControlListOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3AccessControlListOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessControlList:
    boto3_raw_data: "type_defs.S3AccessControlListTypeDef" = dataclasses.field()

    @cached_property
    def Owner(self):  # pragma: no cover
        return S3ObjectOwner.make_one(self.boto3_raw_data["Owner"])

    @cached_property
    def Grants(self):  # pragma: no cover
        return S3Grant.make_many(self.boto3_raw_data["Grants"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3AccessControlListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3AccessControlListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3CopyObjectOperationOutput:
    boto3_raw_data: "type_defs.S3CopyObjectOperationOutputTypeDef" = dataclasses.field()

    TargetResource = field("TargetResource")
    CannedAccessControlList = field("CannedAccessControlList")

    @cached_property
    def AccessControlGrants(self):  # pragma: no cover
        return S3Grant.make_many(self.boto3_raw_data["AccessControlGrants"])

    MetadataDirective = field("MetadataDirective")
    ModifiedSinceConstraint = field("ModifiedSinceConstraint")

    @cached_property
    def NewObjectMetadata(self):  # pragma: no cover
        return S3ObjectMetadataOutput.make_one(self.boto3_raw_data["NewObjectMetadata"])

    @cached_property
    def NewObjectTagging(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["NewObjectTagging"])

    RedirectLocation = field("RedirectLocation")
    RequesterPays = field("RequesterPays")
    StorageClass = field("StorageClass")
    UnModifiedSinceConstraint = field("UnModifiedSinceConstraint")
    SSEAwsKmsKeyId = field("SSEAwsKmsKeyId")
    TargetKeyPrefix = field("TargetKeyPrefix")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    BucketKeyEnabled = field("BucketKeyEnabled")
    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3CopyObjectOperationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3CopyObjectOperationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3CopyObjectOperation:
    boto3_raw_data: "type_defs.S3CopyObjectOperationTypeDef" = dataclasses.field()

    TargetResource = field("TargetResource")
    CannedAccessControlList = field("CannedAccessControlList")

    @cached_property
    def AccessControlGrants(self):  # pragma: no cover
        return S3Grant.make_many(self.boto3_raw_data["AccessControlGrants"])

    MetadataDirective = field("MetadataDirective")
    ModifiedSinceConstraint = field("ModifiedSinceConstraint")

    @cached_property
    def NewObjectMetadata(self):  # pragma: no cover
        return S3ObjectMetadata.make_one(self.boto3_raw_data["NewObjectMetadata"])

    @cached_property
    def NewObjectTagging(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["NewObjectTagging"])

    RedirectLocation = field("RedirectLocation")
    RequesterPays = field("RequesterPays")
    StorageClass = field("StorageClass")
    UnModifiedSinceConstraint = field("UnModifiedSinceConstraint")
    SSEAwsKmsKeyId = field("SSEAwsKmsKeyId")
    TargetKeyPrefix = field("TargetKeyPrefix")
    ObjectLockLegalHoldStatus = field("ObjectLockLegalHoldStatus")
    ObjectLockMode = field("ObjectLockMode")
    ObjectLockRetainUntilDate = field("ObjectLockRetainUntilDate")
    BucketKeyEnabled = field("BucketKeyEnabled")
    ChecksumAlgorithm = field("ChecksumAlgorithm")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3CopyObjectOperationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3CopyObjectOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketDestinationOutput:
    boto3_raw_data: "type_defs.S3BucketDestinationOutputTypeDef" = dataclasses.field()

    Format = field("Format")
    OutputSchemaVersion = field("OutputSchemaVersion")
    AccountId = field("AccountId")
    Arn = field("Arn")
    Prefix = field("Prefix")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return StorageLensDataExportEncryptionOutput.make_one(
            self.boto3_raw_data["Encryption"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BucketDestinationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketDestinationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketDestination:
    boto3_raw_data: "type_defs.S3BucketDestinationTypeDef" = dataclasses.field()

    Format = field("Format")
    OutputSchemaVersion = field("OutputSchemaVersion")
    AccountId = field("AccountId")
    Arn = field("Arn")
    Prefix = field("Prefix")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return StorageLensDataExportEncryption.make_one(
            self.boto3_raw_data["Encryption"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BucketDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPointRequest:
    boto3_raw_data: "type_defs.CreateAccessPointRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")
    Bucket = field("Bucket")

    @cached_property
    def VpcConfiguration(self):  # pragma: no cover
        return VpcConfiguration.make_one(self.boto3_raw_data["VpcConfiguration"])

    @cached_property
    def PublicAccessBlockConfiguration(self):  # pragma: no cover
        return PublicAccessBlockConfiguration.make_one(
            self.boto3_raw_data["PublicAccessBlockConfiguration"]
        )

    BucketAccountId = field("BucketAccountId")
    Scope = field("Scope")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessPointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccessPointScopeRequest:
    boto3_raw_data: "type_defs.PutAccessPointScopeRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")
    Scope = field("Scope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccessPointScopeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccessPointScopeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLambdaConfigurationOutput:
    boto3_raw_data: "type_defs.ObjectLambdaConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    SupportingAccessPoint = field("SupportingAccessPoint")

    @cached_property
    def TransformationConfigurations(self):  # pragma: no cover
        return ObjectLambdaTransformationConfigurationOutput.make_many(
            self.boto3_raw_data["TransformationConfigurations"]
        )

    CloudWatchMetricsEnabled = field("CloudWatchMetricsEnabled")
    AllowedFeatures = field("AllowedFeatures")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ObjectLambdaConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLambdaConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectLambdaConfiguration:
    boto3_raw_data: "type_defs.ObjectLambdaConfigurationTypeDef" = dataclasses.field()

    SupportingAccessPoint = field("SupportingAccessPoint")

    @cached_property
    def TransformationConfigurations(self):  # pragma: no cover
        return ObjectLambdaTransformationConfiguration.make_many(
            self.boto3_raw_data["TransformationConfigurations"]
        )

    CloudWatchMetricsEnabled = field("CloudWatchMetricsEnabled")
    AllowedFeatures = field("AllowedFeatures")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectLambdaConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectLambdaConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRuleOutput:
    boto3_raw_data: "type_defs.LifecycleRuleOutputTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def Expiration(self):  # pragma: no cover
        return LifecycleExpirationOutput.make_one(self.boto3_raw_data["Expiration"])

    ID = field("ID")

    @cached_property
    def Filter(self):  # pragma: no cover
        return LifecycleRuleFilterOutput.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def Transitions(self):  # pragma: no cover
        return TransitionOutput.make_many(self.boto3_raw_data["Transitions"])

    @cached_property
    def NoncurrentVersionTransitions(self):  # pragma: no cover
        return NoncurrentVersionTransition.make_many(
            self.boto3_raw_data["NoncurrentVersionTransitions"]
        )

    @cached_property
    def NoncurrentVersionExpiration(self):  # pragma: no cover
        return NoncurrentVersionExpiration.make_one(
            self.boto3_raw_data["NoncurrentVersionExpiration"]
        )

    @cached_property
    def AbortIncompleteMultipartUpload(self):  # pragma: no cover
        return AbortIncompleteMultipartUpload.make_one(
            self.boto3_raw_data["AbortIncompleteMultipartUpload"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRuleFilter:
    boto3_raw_data: "type_defs.LifecycleRuleFilterTypeDef" = dataclasses.field()

    Prefix = field("Prefix")

    @cached_property
    def Tag(self):  # pragma: no cover
        return S3Tag.make_one(self.boto3_raw_data["Tag"])

    And = field("And")
    ObjectSizeGreaterThan = field("ObjectSizeGreaterThan")
    ObjectSizeLessThan = field("ObjectSizeLessThan")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleRuleFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleRuleFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMultiRegionAccessPointRequest:
    boto3_raw_data: "type_defs.CreateMultiRegionAccessPointRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    ClientToken = field("ClientToken")
    Details = field("Details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMultiRegionAccessPointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMultiRegionAccessPointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsResult:
    boto3_raw_data: "type_defs.ListJobsResultTypeDef" = dataclasses.field()

    @cached_property
    def Jobs(self):  # pragma: no cover
        return JobListDescriptor.make_many(self.boto3_raw_data["Jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobsResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListJobsResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroupOutput:
    boto3_raw_data: "type_defs.StorageLensGroupOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Filter(self):  # pragma: no cover
        return StorageLensGroupFilterOutput.make_one(self.boto3_raw_data["Filter"])

    StorageLensGroupArn = field("StorageLensGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageLensGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensGroup:
    boto3_raw_data: "type_defs.StorageLensGroupTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def Filter(self):  # pragma: no cover
        return StorageLensGroupFilter.make_one(self.boto3_raw_data["Filter"])

    StorageLensGroupArn = field("StorageLensGroupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorageLensGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRuleOutput:
    boto3_raw_data: "type_defs.ReplicationRuleOutputTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    Bucket = field("Bucket")
    ID = field("ID")
    Priority = field("Priority")
    Prefix = field("Prefix")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ReplicationRuleFilterOutput.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def SourceSelectionCriteria(self):  # pragma: no cover
        return SourceSelectionCriteria.make_one(
            self.boto3_raw_data["SourceSelectionCriteria"]
        )

    @cached_property
    def ExistingObjectReplication(self):  # pragma: no cover
        return ExistingObjectReplication.make_one(
            self.boto3_raw_data["ExistingObjectReplication"]
        )

    @cached_property
    def DeleteMarkerReplication(self):  # pragma: no cover
        return DeleteMarkerReplication.make_one(
            self.boto3_raw_data["DeleteMarkerReplication"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationRule:
    boto3_raw_data: "type_defs.ReplicationRuleTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["Destination"])

    Bucket = field("Bucket")
    ID = field("ID")
    Priority = field("Priority")
    Prefix = field("Prefix")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ReplicationRuleFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def SourceSelectionCriteria(self):  # pragma: no cover
        return SourceSelectionCriteria.make_one(
            self.boto3_raw_data["SourceSelectionCriteria"]
        )

    @cached_property
    def ExistingObjectReplication(self):  # pragma: no cover
        return ExistingObjectReplication.make_one(
            self.boto3_raw_data["ExistingObjectReplication"]
        )

    @cached_property
    def DeleteMarkerReplication(self):  # pragma: no cover
        return DeleteMarkerReplication.make_one(
            self.boto3_raw_data["DeleteMarkerReplication"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicationRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AsyncOperation:
    boto3_raw_data: "type_defs.AsyncOperationTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")
    Operation = field("Operation")
    RequestTokenARN = field("RequestTokenARN")

    @cached_property
    def RequestParameters(self):  # pragma: no cover
        return AsyncRequestParameters.make_one(self.boto3_raw_data["RequestParameters"])

    RequestStatus = field("RequestStatus")

    @cached_property
    def ResponseDetails(self):  # pragma: no cover
        return AsyncResponseDetails.make_one(self.boto3_raw_data["ResponseDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AsyncOperationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AsyncOperationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3JobManifestGeneratorOutput:
    boto3_raw_data: "type_defs.S3JobManifestGeneratorOutputTypeDef" = (
        dataclasses.field()
    )

    SourceBucket = field("SourceBucket")
    EnableManifestOutput = field("EnableManifestOutput")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @cached_property
    def ManifestOutputLocation(self):  # pragma: no cover
        return S3ManifestOutputLocationOutput.make_one(
            self.boto3_raw_data["ManifestOutputLocation"]
        )

    @cached_property
    def Filter(self):  # pragma: no cover
        return JobManifestGeneratorFilterOutput.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3JobManifestGeneratorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3JobManifestGeneratorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3JobManifestGenerator:
    boto3_raw_data: "type_defs.S3JobManifestGeneratorTypeDef" = dataclasses.field()

    SourceBucket = field("SourceBucket")
    EnableManifestOutput = field("EnableManifestOutput")
    ExpectedBucketOwner = field("ExpectedBucketOwner")

    @cached_property
    def ManifestOutputLocation(self):  # pragma: no cover
        return S3ManifestOutputLocation.make_one(
            self.boto3_raw_data["ManifestOutputLocation"]
        )

    @cached_property
    def Filter(self):  # pragma: no cover
        return JobManifestGeneratorFilter.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3JobManifestGeneratorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3JobManifestGeneratorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BucketLevel:
    boto3_raw_data: "type_defs.BucketLevelTypeDef" = dataclasses.field()

    @cached_property
    def ActivityMetrics(self):  # pragma: no cover
        return ActivityMetrics.make_one(self.boto3_raw_data["ActivityMetrics"])

    @cached_property
    def PrefixLevel(self):  # pragma: no cover
        return PrefixLevel.make_one(self.boto3_raw_data["PrefixLevel"])

    @cached_property
    def AdvancedCostOptimizationMetrics(self):  # pragma: no cover
        return AdvancedCostOptimizationMetrics.make_one(
            self.boto3_raw_data["AdvancedCostOptimizationMetrics"]
        )

    @cached_property
    def AdvancedDataProtectionMetrics(self):  # pragma: no cover
        return AdvancedDataProtectionMetrics.make_one(
            self.boto3_raw_data["AdvancedDataProtectionMetrics"]
        )

    @cached_property
    def DetailedStatusCodesMetrics(self):  # pragma: no cover
        return DetailedStatusCodesMetrics.make_one(
            self.boto3_raw_data["DetailedStatusCodesMetrics"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BucketLevelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BucketLevelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessControlPolicyOutput:
    boto3_raw_data: "type_defs.S3AccessControlPolicyOutputTypeDef" = dataclasses.field()

    @cached_property
    def AccessControlList(self):  # pragma: no cover
        return S3AccessControlListOutput.make_one(
            self.boto3_raw_data["AccessControlList"]
        )

    CannedAccessControlList = field("CannedAccessControlList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3AccessControlPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3AccessControlPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3AccessControlPolicy:
    boto3_raw_data: "type_defs.S3AccessControlPolicyTypeDef" = dataclasses.field()

    @cached_property
    def AccessControlList(self):  # pragma: no cover
        return S3AccessControlList.make_one(self.boto3_raw_data["AccessControlList"])

    CannedAccessControlList = field("CannedAccessControlList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3AccessControlPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3AccessControlPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensDataExportOutput:
    boto3_raw_data: "type_defs.StorageLensDataExportOutputTypeDef" = dataclasses.field()

    @cached_property
    def S3BucketDestination(self):  # pragma: no cover
        return S3BucketDestinationOutput.make_one(
            self.boto3_raw_data["S3BucketDestination"]
        )

    @cached_property
    def CloudWatchMetrics(self):  # pragma: no cover
        return CloudWatchMetrics.make_one(self.boto3_raw_data["CloudWatchMetrics"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageLensDataExportOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensDataExportOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensDataExport:
    boto3_raw_data: "type_defs.StorageLensDataExportTypeDef" = dataclasses.field()

    @cached_property
    def S3BucketDestination(self):  # pragma: no cover
        return S3BucketDestination.make_one(self.boto3_raw_data["S3BucketDestination"])

    @cached_property
    def CloudWatchMetrics(self):  # pragma: no cover
        return CloudWatchMetrics.make_one(self.boto3_raw_data["CloudWatchMetrics"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageLensDataExportTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensDataExportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPointConfigurationForObjectLambdaResult:
    boto3_raw_data: (
        "type_defs.GetAccessPointConfigurationForObjectLambdaResultTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Configuration(self):  # pragma: no cover
        return ObjectLambdaConfigurationOutput.make_one(
            self.boto3_raw_data["Configuration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAccessPointConfigurationForObjectLambdaResultTypeDef"
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
                "type_defs.GetAccessPointConfigurationForObjectLambdaResultTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketLifecycleConfigurationResult:
    boto3_raw_data: "type_defs.GetBucketLifecycleConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Rules(self):  # pragma: no cover
        return LifecycleRuleOutput.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetBucketLifecycleConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketLifecycleConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageLensGroupResult:
    boto3_raw_data: "type_defs.GetStorageLensGroupResultTypeDef" = dataclasses.field()

    @cached_property
    def StorageLensGroup(self):  # pragma: no cover
        return StorageLensGroupOutput.make_one(self.boto3_raw_data["StorageLensGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStorageLensGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageLensGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfigurationOutput:
    boto3_raw_data: "type_defs.ReplicationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Role = field("Role")

    @cached_property
    def Rules(self):  # pragma: no cover
        return ReplicationRuleOutput.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReplicationConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfiguration:
    boto3_raw_data: "type_defs.ReplicationConfigurationTypeDef" = dataclasses.field()

    Role = field("Role")

    @cached_property
    def Rules(self):  # pragma: no cover
        return ReplicationRule.make_many(self.boto3_raw_data["Rules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMultiRegionAccessPointOperationResult:
    boto3_raw_data: "type_defs.DescribeMultiRegionAccessPointOperationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AsyncOperation(self):  # pragma: no cover
        return AsyncOperation.make_one(self.boto3_raw_data["AsyncOperation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMultiRegionAccessPointOperationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMultiRegionAccessPointOperationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobManifestGeneratorOutput:
    boto3_raw_data: "type_defs.JobManifestGeneratorOutputTypeDef" = dataclasses.field()

    @cached_property
    def S3JobManifestGenerator(self):  # pragma: no cover
        return S3JobManifestGeneratorOutput.make_one(
            self.boto3_raw_data["S3JobManifestGenerator"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobManifestGeneratorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobManifestGeneratorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobManifestGenerator:
    boto3_raw_data: "type_defs.JobManifestGeneratorTypeDef" = dataclasses.field()

    @cached_property
    def S3JobManifestGenerator(self):  # pragma: no cover
        return S3JobManifestGenerator.make_one(
            self.boto3_raw_data["S3JobManifestGenerator"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobManifestGeneratorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobManifestGeneratorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountLevelOutput:
    boto3_raw_data: "type_defs.AccountLevelOutputTypeDef" = dataclasses.field()

    @cached_property
    def BucketLevel(self):  # pragma: no cover
        return BucketLevel.make_one(self.boto3_raw_data["BucketLevel"])

    @cached_property
    def ActivityMetrics(self):  # pragma: no cover
        return ActivityMetrics.make_one(self.boto3_raw_data["ActivityMetrics"])

    @cached_property
    def AdvancedCostOptimizationMetrics(self):  # pragma: no cover
        return AdvancedCostOptimizationMetrics.make_one(
            self.boto3_raw_data["AdvancedCostOptimizationMetrics"]
        )

    @cached_property
    def AdvancedDataProtectionMetrics(self):  # pragma: no cover
        return AdvancedDataProtectionMetrics.make_one(
            self.boto3_raw_data["AdvancedDataProtectionMetrics"]
        )

    @cached_property
    def DetailedStatusCodesMetrics(self):  # pragma: no cover
        return DetailedStatusCodesMetrics.make_one(
            self.boto3_raw_data["DetailedStatusCodesMetrics"]
        )

    @cached_property
    def StorageLensGroupLevel(self):  # pragma: no cover
        return StorageLensGroupLevelOutput.make_one(
            self.boto3_raw_data["StorageLensGroupLevel"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountLevelOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountLevelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountLevel:
    boto3_raw_data: "type_defs.AccountLevelTypeDef" = dataclasses.field()

    @cached_property
    def BucketLevel(self):  # pragma: no cover
        return BucketLevel.make_one(self.boto3_raw_data["BucketLevel"])

    @cached_property
    def ActivityMetrics(self):  # pragma: no cover
        return ActivityMetrics.make_one(self.boto3_raw_data["ActivityMetrics"])

    @cached_property
    def AdvancedCostOptimizationMetrics(self):  # pragma: no cover
        return AdvancedCostOptimizationMetrics.make_one(
            self.boto3_raw_data["AdvancedCostOptimizationMetrics"]
        )

    @cached_property
    def AdvancedDataProtectionMetrics(self):  # pragma: no cover
        return AdvancedDataProtectionMetrics.make_one(
            self.boto3_raw_data["AdvancedDataProtectionMetrics"]
        )

    @cached_property
    def DetailedStatusCodesMetrics(self):  # pragma: no cover
        return DetailedStatusCodesMetrics.make_one(
            self.boto3_raw_data["DetailedStatusCodesMetrics"]
        )

    @cached_property
    def StorageLensGroupLevel(self):  # pragma: no cover
        return StorageLensGroupLevel.make_one(
            self.boto3_raw_data["StorageLensGroupLevel"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountLevelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountLevelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SetObjectAclOperationOutput:
    boto3_raw_data: "type_defs.S3SetObjectAclOperationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessControlPolicy(self):  # pragma: no cover
        return S3AccessControlPolicyOutput.make_one(
            self.boto3_raw_data["AccessControlPolicy"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3SetObjectAclOperationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3SetObjectAclOperationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SetObjectAclOperation:
    boto3_raw_data: "type_defs.S3SetObjectAclOperationTypeDef" = dataclasses.field()

    @cached_property
    def AccessControlPolicy(self):  # pragma: no cover
        return S3AccessControlPolicy.make_one(
            self.boto3_raw_data["AccessControlPolicy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3SetObjectAclOperationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3SetObjectAclOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPointForObjectLambdaRequest:
    boto3_raw_data: "type_defs.CreateAccessPointForObjectLambdaRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Name = field("Name")
    Configuration = field("Configuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAccessPointForObjectLambdaRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPointForObjectLambdaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccessPointConfigurationForObjectLambdaRequest:
    boto3_raw_data: (
        "type_defs.PutAccessPointConfigurationForObjectLambdaRequestTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")
    Name = field("Name")
    Configuration = field("Configuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAccessPointConfigurationForObjectLambdaRequestTypeDef"
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
                "type_defs.PutAccessPointConfigurationForObjectLambdaRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleRule:
    boto3_raw_data: "type_defs.LifecycleRuleTypeDef" = dataclasses.field()

    Status = field("Status")
    Expiration = field("Expiration")
    ID = field("ID")
    Filter = field("Filter")
    Transitions = field("Transitions")

    @cached_property
    def NoncurrentVersionTransitions(self):  # pragma: no cover
        return NoncurrentVersionTransition.make_many(
            self.boto3_raw_data["NoncurrentVersionTransitions"]
        )

    @cached_property
    def NoncurrentVersionExpiration(self):  # pragma: no cover
        return NoncurrentVersionExpiration.make_one(
            self.boto3_raw_data["NoncurrentVersionExpiration"]
        )

    @cached_property
    def AbortIncompleteMultipartUpload(self):  # pragma: no cover
        return AbortIncompleteMultipartUpload.make_one(
            self.boto3_raw_data["AbortIncompleteMultipartUpload"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifecycleRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifecycleRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStorageLensGroupRequest:
    boto3_raw_data: "type_defs.CreateStorageLensGroupRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    StorageLensGroup = field("StorageLensGroup")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateStorageLensGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStorageLensGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStorageLensGroupRequest:
    boto3_raw_data: "type_defs.UpdateStorageLensGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    AccountId = field("AccountId")
    StorageLensGroup = field("StorageLensGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateStorageLensGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStorageLensGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBucketReplicationResult:
    boto3_raw_data: "type_defs.GetBucketReplicationResultTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationConfiguration(self):  # pragma: no cover
        return ReplicationConfigurationOutput.make_one(
            self.boto3_raw_data["ReplicationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBucketReplicationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBucketReplicationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensConfigurationOutput:
    boto3_raw_data: "type_defs.StorageLensConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def AccountLevel(self):  # pragma: no cover
        return AccountLevelOutput.make_one(self.boto3_raw_data["AccountLevel"])

    IsEnabled = field("IsEnabled")

    @cached_property
    def Include(self):  # pragma: no cover
        return IncludeOutput.make_one(self.boto3_raw_data["Include"])

    @cached_property
    def Exclude(self):  # pragma: no cover
        return ExcludeOutput.make_one(self.boto3_raw_data["Exclude"])

    @cached_property
    def DataExport(self):  # pragma: no cover
        return StorageLensDataExportOutput.make_one(self.boto3_raw_data["DataExport"])

    @cached_property
    def AwsOrg(self):  # pragma: no cover
        return StorageLensAwsOrg.make_one(self.boto3_raw_data["AwsOrg"])

    StorageLensArn = field("StorageLensArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StorageLensConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageLensConfiguration:
    boto3_raw_data: "type_defs.StorageLensConfigurationTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def AccountLevel(self):  # pragma: no cover
        return AccountLevel.make_one(self.boto3_raw_data["AccountLevel"])

    IsEnabled = field("IsEnabled")

    @cached_property
    def Include(self):  # pragma: no cover
        return Include.make_one(self.boto3_raw_data["Include"])

    @cached_property
    def Exclude(self):  # pragma: no cover
        return Exclude.make_one(self.boto3_raw_data["Exclude"])

    @cached_property
    def DataExport(self):  # pragma: no cover
        return StorageLensDataExport.make_one(self.boto3_raw_data["DataExport"])

    @cached_property
    def AwsOrg(self):  # pragma: no cover
        return StorageLensAwsOrg.make_one(self.boto3_raw_data["AwsOrg"])

    StorageLensArn = field("StorageLensArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageLensConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageLensConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobOperationOutput:
    boto3_raw_data: "type_defs.JobOperationOutputTypeDef" = dataclasses.field()

    @cached_property
    def LambdaInvoke(self):  # pragma: no cover
        return LambdaInvokeOperationOutput.make_one(self.boto3_raw_data["LambdaInvoke"])

    @cached_property
    def S3PutObjectCopy(self):  # pragma: no cover
        return S3CopyObjectOperationOutput.make_one(
            self.boto3_raw_data["S3PutObjectCopy"]
        )

    @cached_property
    def S3PutObjectAcl(self):  # pragma: no cover
        return S3SetObjectAclOperationOutput.make_one(
            self.boto3_raw_data["S3PutObjectAcl"]
        )

    @cached_property
    def S3PutObjectTagging(self):  # pragma: no cover
        return S3SetObjectTaggingOperationOutput.make_one(
            self.boto3_raw_data["S3PutObjectTagging"]
        )

    S3DeleteObjectTagging = field("S3DeleteObjectTagging")

    @cached_property
    def S3InitiateRestoreObject(self):  # pragma: no cover
        return S3InitiateRestoreObjectOperation.make_one(
            self.boto3_raw_data["S3InitiateRestoreObject"]
        )

    @cached_property
    def S3PutObjectLegalHold(self):  # pragma: no cover
        return S3SetObjectLegalHoldOperation.make_one(
            self.boto3_raw_data["S3PutObjectLegalHold"]
        )

    @cached_property
    def S3PutObjectRetention(self):  # pragma: no cover
        return S3SetObjectRetentionOperationOutput.make_one(
            self.boto3_raw_data["S3PutObjectRetention"]
        )

    S3ReplicateObject = field("S3ReplicateObject")

    @cached_property
    def S3ComputeObjectChecksum(self):  # pragma: no cover
        return S3ComputeObjectChecksumOperation.make_one(
            self.boto3_raw_data["S3ComputeObjectChecksum"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobOperationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobOperationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobOperation:
    boto3_raw_data: "type_defs.JobOperationTypeDef" = dataclasses.field()

    @cached_property
    def LambdaInvoke(self):  # pragma: no cover
        return LambdaInvokeOperation.make_one(self.boto3_raw_data["LambdaInvoke"])

    @cached_property
    def S3PutObjectCopy(self):  # pragma: no cover
        return S3CopyObjectOperation.make_one(self.boto3_raw_data["S3PutObjectCopy"])

    @cached_property
    def S3PutObjectAcl(self):  # pragma: no cover
        return S3SetObjectAclOperation.make_one(self.boto3_raw_data["S3PutObjectAcl"])

    @cached_property
    def S3PutObjectTagging(self):  # pragma: no cover
        return S3SetObjectTaggingOperation.make_one(
            self.boto3_raw_data["S3PutObjectTagging"]
        )

    S3DeleteObjectTagging = field("S3DeleteObjectTagging")

    @cached_property
    def S3InitiateRestoreObject(self):  # pragma: no cover
        return S3InitiateRestoreObjectOperation.make_one(
            self.boto3_raw_data["S3InitiateRestoreObject"]
        )

    @cached_property
    def S3PutObjectLegalHold(self):  # pragma: no cover
        return S3SetObjectLegalHoldOperation.make_one(
            self.boto3_raw_data["S3PutObjectLegalHold"]
        )

    @cached_property
    def S3PutObjectRetention(self):  # pragma: no cover
        return S3SetObjectRetentionOperation.make_one(
            self.boto3_raw_data["S3PutObjectRetention"]
        )

    S3ReplicateObject = field("S3ReplicateObject")

    @cached_property
    def S3ComputeObjectChecksum(self):  # pragma: no cover
        return S3ComputeObjectChecksumOperation.make_one(
            self.boto3_raw_data["S3ComputeObjectChecksum"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobOperationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobOperationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketReplicationRequest:
    boto3_raw_data: "type_defs.PutBucketReplicationRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Bucket = field("Bucket")
    ReplicationConfiguration = field("ReplicationConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutBucketReplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketReplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStorageLensConfigurationResult:
    boto3_raw_data: "type_defs.GetStorageLensConfigurationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StorageLensConfiguration(self):  # pragma: no cover
        return StorageLensConfigurationOutput.make_one(
            self.boto3_raw_data["StorageLensConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetStorageLensConfigurationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStorageLensConfigurationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDescriptor:
    boto3_raw_data: "type_defs.JobDescriptorTypeDef" = dataclasses.field()

    JobId = field("JobId")
    ConfirmationRequired = field("ConfirmationRequired")
    Description = field("Description")
    JobArn = field("JobArn")
    Status = field("Status")

    @cached_property
    def Manifest(self):  # pragma: no cover
        return JobManifestOutput.make_one(self.boto3_raw_data["Manifest"])

    @cached_property
    def Operation(self):  # pragma: no cover
        return JobOperationOutput.make_one(self.boto3_raw_data["Operation"])

    Priority = field("Priority")

    @cached_property
    def ProgressSummary(self):  # pragma: no cover
        return JobProgressSummary.make_one(self.boto3_raw_data["ProgressSummary"])

    StatusUpdateReason = field("StatusUpdateReason")

    @cached_property
    def FailureReasons(self):  # pragma: no cover
        return JobFailure.make_many(self.boto3_raw_data["FailureReasons"])

    @cached_property
    def Report(self):  # pragma: no cover
        return JobReport.make_one(self.boto3_raw_data["Report"])

    CreationTime = field("CreationTime")
    TerminationDate = field("TerminationDate")
    RoleArn = field("RoleArn")
    SuspendedDate = field("SuspendedDate")
    SuspendedCause = field("SuspendedCause")

    @cached_property
    def ManifestGenerator(self):  # pragma: no cover
        return JobManifestGeneratorOutput.make_one(
            self.boto3_raw_data["ManifestGenerator"]
        )

    @cached_property
    def GeneratedManifestDescriptor(self):  # pragma: no cover
        return S3GeneratedManifestDescriptor.make_one(
            self.boto3_raw_data["GeneratedManifestDescriptor"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDescriptorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDescriptorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecycleConfiguration:
    boto3_raw_data: "type_defs.LifecycleConfigurationTypeDef" = dataclasses.field()

    Rules = field("Rules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecycleConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecycleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutStorageLensConfigurationRequest:
    boto3_raw_data: "type_defs.PutStorageLensConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigId = field("ConfigId")
    AccountId = field("AccountId")
    StorageLensConfiguration = field("StorageLensConfiguration")

    @cached_property
    def Tags(self):  # pragma: no cover
        return StorageLensTag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutStorageLensConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutStorageLensConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobResult:
    boto3_raw_data: "type_defs.DescribeJobResultTypeDef" = dataclasses.field()

    @cached_property
    def Job(self):  # pragma: no cover
        return JobDescriptor.make_one(self.boto3_raw_data["Job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribeJobResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobRequest:
    boto3_raw_data: "type_defs.CreateJobRequestTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Operation = field("Operation")

    @cached_property
    def Report(self):  # pragma: no cover
        return JobReport.make_one(self.boto3_raw_data["Report"])

    ClientRequestToken = field("ClientRequestToken")
    Priority = field("Priority")
    RoleArn = field("RoleArn")
    ConfirmationRequired = field("ConfirmationRequired")
    Manifest = field("Manifest")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return S3Tag.make_many(self.boto3_raw_data["Tags"])

    ManifestGenerator = field("ManifestGenerator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutBucketLifecycleConfigurationRequest:
    boto3_raw_data: "type_defs.PutBucketLifecycleConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Bucket = field("Bucket")

    @cached_property
    def LifecycleConfiguration(self):  # pragma: no cover
        return LifecycleConfiguration.make_one(
            self.boto3_raw_data["LifecycleConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutBucketLifecycleConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutBucketLifecycleConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
