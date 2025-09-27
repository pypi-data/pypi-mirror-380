# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_inspector2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class SeverityCounts:
    boto3_raw_data: "type_defs.SeverityCountsTypeDef" = dataclasses.field()

    all = field("all")
    medium = field("medium")
    high = field("high")
    critical = field("critical")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SeverityCountsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SeverityCountsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountAggregation:
    boto3_raw_data: "type_defs.AccountAggregationTypeDef" = dataclasses.field()

    findingType = field("findingType")
    resourceType = field("resourceType")
    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class State:
    boto3_raw_data: "type_defs.StateTypeDef" = dataclasses.field()

    status = field("status")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceStatus:
    boto3_raw_data: "type_defs.ResourceStatusTypeDef" = dataclasses.field()

    ec2 = field("ec2")
    ecr = field("ecr")
    lambda_ = field("lambda")
    lambdaCode = field("lambdaCode")
    codeRepository = field("codeRepository")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingTypeAggregation:
    boto3_raw_data: "type_defs.FindingTypeAggregationTypeDef" = dataclasses.field()

    findingType = field("findingType")
    resourceType = field("resourceType")
    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FindingTypeAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingTypeAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StringFilter:
    boto3_raw_data: "type_defs.StringFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StringFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StringFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSecurityResource:
    boto3_raw_data: "type_defs.CodeSecurityResourceTypeDef" = dataclasses.field()

    projectId = field("projectId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeSecurityResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSecurityResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateMemberRequest:
    boto3_raw_data: "type_defs.AssociateMemberRequestTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateMemberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMemberRequestTypeDef"]
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
class AtigData:
    boto3_raw_data: "type_defs.AtigDataTypeDef" = dataclasses.field()

    firstSeen = field("firstSeen")
    lastSeen = field("lastSeen")
    targets = field("targets")
    ttps = field("ttps")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AtigDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AtigDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoEnable:
    boto3_raw_data: "type_defs.AutoEnableTypeDef" = dataclasses.field()

    ec2 = field("ec2")
    ecr = field("ecr")
    lambda_ = field("lambda")
    lambdaCode = field("lambdaCode")
    codeRepository = field("codeRepository")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoEnableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoEnableTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsEc2InstanceDetails:
    boto3_raw_data: "type_defs.AwsEc2InstanceDetailsTypeDef" = dataclasses.field()

    type = field("type")
    imageId = field("imageId")
    ipV4Addresses = field("ipV4Addresses")
    ipV6Addresses = field("ipV6Addresses")
    keyName = field("keyName")
    iamInstanceProfileArn = field("iamInstanceProfileArn")
    vpcId = field("vpcId")
    subnetId = field("subnetId")
    launchedAt = field("launchedAt")
    platform = field("platform")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsEc2InstanceDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsEc2InstanceDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NumberFilter:
    boto3_raw_data: "type_defs.NumberFilterTypeDef" = dataclasses.field()

    upperInclusive = field("upperInclusive")
    lowerInclusive = field("lowerInclusive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NumberFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NumberFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsEcrContainerImageDetails:
    boto3_raw_data: "type_defs.AwsEcrContainerImageDetailsTypeDef" = dataclasses.field()

    repositoryName = field("repositoryName")
    imageHash = field("imageHash")
    registry = field("registry")
    imageTags = field("imageTags")
    pushedAt = field("pushedAt")
    author = field("author")
    architecture = field("architecture")
    platform = field("platform")
    lastInUseAt = field("lastInUseAt")
    inUseCount = field("inUseCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsEcrContainerImageDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsEcrContainerImageDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsEcsMetadataDetails:
    boto3_raw_data: "type_defs.AwsEcsMetadataDetailsTypeDef" = dataclasses.field()

    detailsGroup = field("detailsGroup")
    taskDefinitionArn = field("taskDefinitionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsEcsMetadataDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsEcsMetadataDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsEksWorkloadInfo:
    boto3_raw_data: "type_defs.AwsEksWorkloadInfoTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsEksWorkloadInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsEksWorkloadInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaVpcConfig:
    boto3_raw_data: "type_defs.LambdaVpcConfigTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")
    vpcId = field("vpcId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaVpcConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaVpcConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAccountStatusRequest:
    boto3_raw_data: "type_defs.BatchGetAccountStatusRequestTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetAccountStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAccountStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCodeSnippetRequest:
    boto3_raw_data: "type_defs.BatchGetCodeSnippetRequestTypeDef" = dataclasses.field()

    findingArns = field("findingArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetCodeSnippetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCodeSnippetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSnippetError:
    boto3_raw_data: "type_defs.CodeSnippetErrorTypeDef" = dataclasses.field()

    findingArn = field("findingArn")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeSnippetErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSnippetErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetFindingDetailsRequest:
    boto3_raw_data: "type_defs.BatchGetFindingDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    findingArns = field("findingArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetFindingDetailsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFindingDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingDetailsError:
    boto3_raw_data: "type_defs.FindingDetailsErrorTypeDef" = dataclasses.field()

    findingArn = field("findingArn")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FindingDetailsErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingDetailsErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetFreeTrialInfoRequest:
    boto3_raw_data: "type_defs.BatchGetFreeTrialInfoRequestTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetFreeTrialInfoRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFreeTrialInfoRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FreeTrialInfoError:
    boto3_raw_data: "type_defs.FreeTrialInfoErrorTypeDef" = dataclasses.field()

    accountId = field("accountId")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FreeTrialInfoErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FreeTrialInfoErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetMemberEc2DeepInspectionStatusRequest:
    boto3_raw_data: "type_defs.BatchGetMemberEc2DeepInspectionStatusRequestTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetMemberEc2DeepInspectionStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetMemberEc2DeepInspectionStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedMemberAccountEc2DeepInspectionStatusState:
    boto3_raw_data: (
        "type_defs.FailedMemberAccountEc2DeepInspectionStatusStateTypeDef"
    ) = dataclasses.field()

    accountId = field("accountId")
    ec2ScanStatus = field("ec2ScanStatus")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FailedMemberAccountEc2DeepInspectionStatusStateTypeDef"
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
                "type_defs.FailedMemberAccountEc2DeepInspectionStatusStateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberAccountEc2DeepInspectionStatusState:
    boto3_raw_data: "type_defs.MemberAccountEc2DeepInspectionStatusStateTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    status = field("status")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MemberAccountEc2DeepInspectionStatusStateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberAccountEc2DeepInspectionStatusStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberAccountEc2DeepInspectionStatus:
    boto3_raw_data: "type_defs.MemberAccountEc2DeepInspectionStatusTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    activateDeepInspection = field("activateDeepInspection")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MemberAccountEc2DeepInspectionStatusTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberAccountEc2DeepInspectionStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelFindingsReportRequest:
    boto3_raw_data: "type_defs.CancelFindingsReportRequestTypeDef" = dataclasses.field()

    reportId = field("reportId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelFindingsReportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelFindingsReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelSbomExportRequest:
    boto3_raw_data: "type_defs.CancelSbomExportRequestTypeDef" = dataclasses.field()

    reportId = field("reportId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelSbomExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSbomExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatusCounts:
    boto3_raw_data: "type_defs.StatusCountsTypeDef" = dataclasses.field()

    failed = field("failed")
    skipped = field("skipped")
    passed = field("passed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatusCountsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatusCountsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisFindingStatusFilter:
    boto3_raw_data: "type_defs.CisFindingStatusFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CisFindingStatusFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisFindingStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisNumberFilter:
    boto3_raw_data: "type_defs.CisNumberFilterTypeDef" = dataclasses.field()

    upperInclusive = field("upperInclusive")
    lowerInclusive = field("lowerInclusive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CisNumberFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CisNumberFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisResultStatusFilter:
    boto3_raw_data: "type_defs.CisResultStatusFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CisResultStatusFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisResultStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisTargets:
    boto3_raw_data: "type_defs.CisTargetsTypeDef" = dataclasses.field()

    accountIds = field("accountIds")
    targetResourceTags = field("targetResourceTags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CisTargetsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CisTargetsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisSecurityLevelFilter:
    boto3_raw_data: "type_defs.CisSecurityLevelFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CisSecurityLevelFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisSecurityLevelFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisStringFilter:
    boto3_raw_data: "type_defs.CisStringFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CisStringFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CisStringFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisScanResultDetails:
    boto3_raw_data: "type_defs.CisScanResultDetailsTypeDef" = dataclasses.field()

    scanArn = field("scanArn")
    accountId = field("accountId")
    targetResourceId = field("targetResourceId")
    platform = field("platform")
    status = field("status")
    statusReason = field("statusReason")
    checkId = field("checkId")
    title = field("title")
    checkDescription = field("checkDescription")
    remediation = field("remediation")
    level = field("level")
    findingArn = field("findingArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CisScanResultDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisScanResultDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisTargetStatusFilter:
    boto3_raw_data: "type_defs.CisTargetStatusFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CisTargetStatusFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisTargetStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisTargetStatusReasonFilter:
    boto3_raw_data: "type_defs.CisTargetStatusReasonFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CisTargetStatusReasonFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisTargetStatusReasonFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagFilter:
    boto3_raw_data: "type_defs.TagFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisScanStatusFilter:
    boto3_raw_data: "type_defs.CisScanStatusFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CisScanStatusFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisScanStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisaData:
    boto3_raw_data: "type_defs.CisaDataTypeDef" = dataclasses.field()

    dateAdded = field("dateAdded")
    dateDue = field("dateDue")
    action = field("action")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CisaDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CisaDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterForImageFilterCriteria:
    boto3_raw_data: "type_defs.ClusterForImageFilterCriteriaTypeDef" = (
        dataclasses.field()
    )

    resourceId = field("resourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ClusterForImageFilterCriteriaTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterForImageFilterCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeFilePath:
    boto3_raw_data: "type_defs.CodeFilePathTypeDef" = dataclasses.field()

    fileName = field("fileName")
    filePath = field("filePath")
    startLine = field("startLine")
    endLine = field("endLine")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeFilePathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodeFilePathTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeLine:
    boto3_raw_data: "type_defs.CodeLineTypeDef" = dataclasses.field()

    content = field("content")
    lineNumber = field("lineNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeLineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodeLineTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeRepositoryDetails:
    boto3_raw_data: "type_defs.CodeRepositoryDetailsTypeDef" = dataclasses.field()

    projectName = field("projectName")
    integrationArn = field("integrationArn")
    providerType = field("providerType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeRepositoryDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeRepositoryDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanStatus:
    boto3_raw_data: "type_defs.ScanStatusTypeDef" = dataclasses.field()

    statusCode = field("statusCode")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScanStatusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSecurityIntegrationSummary:
    boto3_raw_data: "type_defs.CodeSecurityIntegrationSummaryTypeDef" = (
        dataclasses.field()
    )

    integrationArn = field("integrationArn")
    name = field("name")
    type = field("type")
    status = field("status")
    statusReason = field("statusReason")
    createdOn = field("createdOn")
    lastUpdateOn = field("lastUpdateOn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CodeSecurityIntegrationSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSecurityIntegrationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousIntegrationScanConfigurationOutput:
    boto3_raw_data: "type_defs.ContinuousIntegrationScanConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    supportedEvents = field("supportedEvents")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContinuousIntegrationScanConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousIntegrationScanConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PeriodicScanConfiguration:
    boto3_raw_data: "type_defs.PeriodicScanConfigurationTypeDef" = dataclasses.field()

    frequency = field("frequency")
    frequencyExpression = field("frequencyExpression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PeriodicScanConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PeriodicScanConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScopeSettings:
    boto3_raw_data: "type_defs.ScopeSettingsTypeDef" = dataclasses.field()

    projectSelectionScope = field("projectSelectionScope")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousIntegrationScanConfiguration:
    boto3_raw_data: "type_defs.ContinuousIntegrationScanConfigurationTypeDef" = (
        dataclasses.field()
    )

    supportedEvents = field("supportedEvents")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContinuousIntegrationScanConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousIntegrationScanConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestedFix:
    boto3_raw_data: "type_defs.SuggestedFixTypeDef" = dataclasses.field()

    description = field("description")
    code = field("code")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestedFixTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggestedFixTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputePlatform:
    boto3_raw_data: "type_defs.ComputePlatformTypeDef" = dataclasses.field()

    vendor = field("vendor")
    product = field("product")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputePlatformTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComputePlatformTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Counts:
    boto3_raw_data: "type_defs.CountsTypeDef" = dataclasses.field()

    count = field("count")
    groupKey = field("groupKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CountsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CountsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageMapFilter:
    boto3_raw_data: "type_defs.CoverageMapFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoverageMapFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageMapFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageNumberFilter:
    boto3_raw_data: "type_defs.CoverageNumberFilterTypeDef" = dataclasses.field()

    upperInclusive = field("upperInclusive")
    lowerInclusive = field("lowerInclusive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageNumberFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageNumberFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageStringFilter:
    boto3_raw_data: "type_defs.CoverageStringFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageStringFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageStringFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCisTargets:
    boto3_raw_data: "type_defs.CreateCisTargetsTypeDef" = dataclasses.field()

    accountIds = field("accountIds")
    targetResourceTags = field("targetResourceTags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateCisTargetsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCisTargetsTypeDef"]
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

    bucketName = field("bucketName")
    kmsKeyArn = field("kmsKeyArn")
    keyPrefix = field("keyPrefix")

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
class CreateGitLabSelfManagedIntegrationDetail:
    boto3_raw_data: "type_defs.CreateGitLabSelfManagedIntegrationDetailTypeDef" = (
        dataclasses.field()
    )

    instanceUrl = field("instanceUrl")
    accessToken = field("accessToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateGitLabSelfManagedIntegrationDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGitLabSelfManagedIntegrationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cvss2:
    boto3_raw_data: "type_defs.Cvss2TypeDef" = dataclasses.field()

    baseScore = field("baseScore")
    scoringVector = field("scoringVector")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Cvss2TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Cvss2TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cvss3:
    boto3_raw_data: "type_defs.Cvss3TypeDef" = dataclasses.field()

    baseScore = field("baseScore")
    scoringVector = field("scoringVector")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Cvss3TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Cvss3TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cvss4:
    boto3_raw_data: "type_defs.Cvss4TypeDef" = dataclasses.field()

    baseScore = field("baseScore")
    scoringVector = field("scoringVector")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Cvss4TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Cvss4TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CvssScoreAdjustment:
    boto3_raw_data: "type_defs.CvssScoreAdjustmentTypeDef" = dataclasses.field()

    metric = field("metric")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CvssScoreAdjustmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CvssScoreAdjustmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CvssScore:
    boto3_raw_data: "type_defs.CvssScoreTypeDef" = dataclasses.field()

    baseScore = field("baseScore")
    scoringVector = field("scoringVector")
    version = field("version")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CvssScoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CvssScoreTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Time:
    boto3_raw_data: "type_defs.TimeTypeDef" = dataclasses.field()

    timeOfDay = field("timeOfDay")
    timezone = field("timezone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateFilterOutput:
    boto3_raw_data: "type_defs.DateFilterOutputTypeDef" = dataclasses.field()

    startInclusive = field("startInclusive")
    endInclusive = field("endInclusive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateFilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DateFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DelegatedAdminAccount:
    boto3_raw_data: "type_defs.DelegatedAdminAccountTypeDef" = dataclasses.field()

    accountId = field("accountId")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DelegatedAdminAccountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DelegatedAdminAccountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DelegatedAdmin:
    boto3_raw_data: "type_defs.DelegatedAdminTypeDef" = dataclasses.field()

    accountId = field("accountId")
    relationshipStatus = field("relationshipStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DelegatedAdminTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DelegatedAdminTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCisScanConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteCisScanConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCisScanConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCisScanConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCodeSecurityIntegrationRequest:
    boto3_raw_data: "type_defs.DeleteCodeSecurityIntegrationRequestTypeDef" = (
        dataclasses.field()
    )

    integrationArn = field("integrationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCodeSecurityIntegrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCodeSecurityIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCodeSecurityScanConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteCodeSecurityScanConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCodeSecurityScanConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCodeSecurityScanConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFilterRequest:
    boto3_raw_data: "type_defs.DeleteFilterRequestTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableDelegatedAdminAccountRequest:
    boto3_raw_data: "type_defs.DisableDelegatedAdminAccountRequestTypeDef" = (
        dataclasses.field()
    )

    delegatedAdminAccountId = field("delegatedAdminAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisableDelegatedAdminAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableDelegatedAdminAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableRequest:
    boto3_raw_data: "type_defs.DisableRequestTypeDef" = dataclasses.field()

    accountIds = field("accountIds")
    resourceTypes = field("resourceTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DisableRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DisableRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMemberRequest:
    boto3_raw_data: "type_defs.DisassociateMemberRequestTypeDef" = dataclasses.field()

    accountId = field("accountId")

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
class Ec2ScanModeState:
    boto3_raw_data: "type_defs.Ec2ScanModeStateTypeDef" = dataclasses.field()

    scanMode = field("scanMode")
    scanModeStatus = field("scanModeStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ec2ScanModeStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2ScanModeStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2Configuration:
    boto3_raw_data: "type_defs.Ec2ConfigurationTypeDef" = dataclasses.field()

    scanMode = field("scanMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ec2ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2ConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapFilter:
    boto3_raw_data: "type_defs.MapFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MapFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MapFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2Metadata:
    boto3_raw_data: "type_defs.Ec2MetadataTypeDef" = dataclasses.field()

    tags = field("tags")
    amiId = field("amiId")
    platform = field("platform")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ec2MetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.Ec2MetadataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcrRescanDurationState:
    boto3_raw_data: "type_defs.EcrRescanDurationStateTypeDef" = dataclasses.field()

    rescanDuration = field("rescanDuration")
    status = field("status")
    updatedAt = field("updatedAt")
    pullDateRescanDuration = field("pullDateRescanDuration")
    pullDateRescanMode = field("pullDateRescanMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcrRescanDurationStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcrRescanDurationStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcrConfiguration:
    boto3_raw_data: "type_defs.EcrConfigurationTypeDef" = dataclasses.field()

    rescanDuration = field("rescanDuration")
    pullDateRescanDuration = field("pullDateRescanDuration")
    pullDateRescanMode = field("pullDateRescanMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EcrConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcrConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcrContainerImageMetadata:
    boto3_raw_data: "type_defs.EcrContainerImageMetadataTypeDef" = dataclasses.field()

    tags = field("tags")
    imagePulledAt = field("imagePulledAt")
    lastInUseAt = field("lastInUseAt")
    inUseCount = field("inUseCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcrContainerImageMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcrContainerImageMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcrRepositoryMetadata:
    boto3_raw_data: "type_defs.EcrRepositoryMetadataTypeDef" = dataclasses.field()

    name = field("name")
    scanFrequency = field("scanFrequency")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcrRepositoryMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcrRepositoryMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableDelegatedAdminAccountRequest:
    boto3_raw_data: "type_defs.EnableDelegatedAdminAccountRequestTypeDef" = (
        dataclasses.field()
    )

    delegatedAdminAccountId = field("delegatedAdminAccountId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableDelegatedAdminAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableDelegatedAdminAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableRequest:
    boto3_raw_data: "type_defs.EnableRequestTypeDef" = dataclasses.field()

    resourceTypes = field("resourceTypes")
    accountIds = field("accountIds")
    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnableRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnableRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EpssDetails:
    boto3_raw_data: "type_defs.EpssDetailsTypeDef" = dataclasses.field()

    score = field("score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EpssDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EpssDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Epss:
    boto3_raw_data: "type_defs.EpssTypeDef" = dataclasses.field()

    score = field("score")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EpssTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EpssTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Evidence:
    boto3_raw_data: "type_defs.EvidenceTypeDef" = dataclasses.field()

    evidenceRule = field("evidenceRule")
    evidenceDetail = field("evidenceDetail")
    severity = field("severity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvidenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvidenceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExploitObserved:
    boto3_raw_data: "type_defs.ExploitObservedTypeDef" = dataclasses.field()

    lastSeen = field("lastSeen")
    firstSeen = field("firstSeen")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExploitObservedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExploitObservedTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExploitabilityDetails:
    boto3_raw_data: "type_defs.ExploitabilityDetailsTypeDef" = dataclasses.field()

    lastKnownExploitAt = field("lastKnownExploitAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExploitabilityDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExploitabilityDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortRangeFilter:
    boto3_raw_data: "type_defs.PortRangeFilterTypeDef" = dataclasses.field()

    beginInclusive = field("beginInclusive")
    endInclusive = field("endInclusive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortRangeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortRangeFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FreeTrialInfo:
    boto3_raw_data: "type_defs.FreeTrialInfoTypeDef" = dataclasses.field()

    type = field("type")
    start = field("start")
    end = field("end")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FreeTrialInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FreeTrialInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCisScanReportRequest:
    boto3_raw_data: "type_defs.GetCisScanReportRequestTypeDef" = dataclasses.field()

    scanArn = field("scanArn")
    targetAccounts = field("targetAccounts")
    reportFormat = field("reportFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCisScanReportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCisScanReportRequestTypeDef"]
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
class GetCodeSecurityIntegrationRequest:
    boto3_raw_data: "type_defs.GetCodeSecurityIntegrationRequestTypeDef" = (
        dataclasses.field()
    )

    integrationArn = field("integrationArn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCodeSecurityIntegrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeSecurityIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodeSecurityScanConfigurationRequest:
    boto3_raw_data: "type_defs.GetCodeSecurityScanConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCodeSecurityScanConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeSecurityScanConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEncryptionKeyRequest:
    boto3_raw_data: "type_defs.GetEncryptionKeyRequestTypeDef" = dataclasses.field()

    scanType = field("scanType")
    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEncryptionKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEncryptionKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsReportStatusRequest:
    boto3_raw_data: "type_defs.GetFindingsReportStatusRequestTypeDef" = (
        dataclasses.field()
    )

    reportId = field("reportId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFindingsReportStatusRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsReportStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMemberRequest:
    boto3_raw_data: "type_defs.GetMemberRequestTypeDef" = dataclasses.field()

    accountId = field("accountId")

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
class Member:
    boto3_raw_data: "type_defs.MemberTypeDef" = dataclasses.field()

    accountId = field("accountId")
    relationshipStatus = field("relationshipStatus")
    delegatedAdminAccountId = field("delegatedAdminAccountId")
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
class GetSbomExportRequest:
    boto3_raw_data: "type_defs.GetSbomExportRequestTypeDef" = dataclasses.field()

    reportId = field("reportId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSbomExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSbomExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionMetadata:
    boto3_raw_data: "type_defs.LambdaFunctionMetadataTypeDef" = dataclasses.field()

    functionTags = field("functionTags")
    layers = field("layers")
    functionName = field("functionName")
    runtime = field("runtime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaFunctionMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountPermissionsRequest:
    boto3_raw_data: "type_defs.ListAccountPermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    service = field("service")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountPermissionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountPermissionsRequestTypeDef"]
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

    service = field("service")
    operation = field("operation")

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
class ListCodeSecurityIntegrationsRequest:
    boto3_raw_data: "type_defs.ListCodeSecurityIntegrationsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCodeSecurityIntegrationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeSecurityIntegrationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeSecurityScanConfigurationAssociationsRequest:
    boto3_raw_data: (
        "type_defs.ListCodeSecurityScanConfigurationAssociationsRequestTypeDef"
    ) = dataclasses.field()

    scanConfigurationArn = field("scanConfigurationArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCodeSecurityScanConfigurationAssociationsRequestTypeDef"
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
                "type_defs.ListCodeSecurityScanConfigurationAssociationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeSecurityScanConfigurationsRequest:
    boto3_raw_data: "type_defs.ListCodeSecurityScanConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCodeSecurityScanConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeSecurityScanConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDelegatedAdminAccountsRequest:
    boto3_raw_data: "type_defs.ListDelegatedAdminAccountsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDelegatedAdminAccountsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDelegatedAdminAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFiltersRequest:
    boto3_raw_data: "type_defs.ListFiltersRequestTypeDef" = dataclasses.field()

    arns = field("arns")
    action = field("action")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFiltersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFiltersRequestTypeDef"]
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

    field = field("field")
    sortOrder = field("sortOrder")

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
class ListMembersRequest:
    boto3_raw_data: "type_defs.ListMembersRequestTypeDef" = dataclasses.field()

    onlyAssociated = field("onlyAssociated")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

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
class ListUsageTotalsRequest:
    boto3_raw_data: "type_defs.ListUsageTotalsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    accountIds = field("accountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsageTotalsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsageTotalsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Step:
    boto3_raw_data: "type_defs.StepTypeDef" = dataclasses.field()

    componentId = field("componentId")
    componentType = field("componentType")
    componentArn = field("componentArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortRange:
    boto3_raw_data: "type_defs.PortRangeTypeDef" = dataclasses.field()

    begin = field("begin")
    end = field("end")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VulnerablePackage:
    boto3_raw_data: "type_defs.VulnerablePackageTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")
    sourceLayerHash = field("sourceLayerHash")
    epoch = field("epoch")
    release = field("release")
    arch = field("arch")
    packageManager = field("packageManager")
    filePath = field("filePath")
    fixedInVersion = field("fixedInVersion")
    remediation = field("remediation")
    sourceLambdaLayerArn = field("sourceLambdaLayerArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VulnerablePackageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VulnerablePackageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectContinuousIntegrationScanConfiguration:
    boto3_raw_data: "type_defs.ProjectContinuousIntegrationScanConfigurationTypeDef" = (
        dataclasses.field()
    )

    supportedEvent = field("supportedEvent")
    ruleSetCategories = field("ruleSetCategories")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProjectContinuousIntegrationScanConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectContinuousIntegrationScanConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectPeriodicScanConfiguration:
    boto3_raw_data: "type_defs.ProjectPeriodicScanConfigurationTypeDef" = (
        dataclasses.field()
    )

    frequencyExpression = field("frequencyExpression")
    ruleSetCategories = field("ruleSetCategories")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProjectPeriodicScanConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectPeriodicScanConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recommendation:
    boto3_raw_data: "type_defs.RecommendationTypeDef" = dataclasses.field()

    text = field("text")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommendationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecommendationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetEncryptionKeyRequest:
    boto3_raw_data: "type_defs.ResetEncryptionKeyRequestTypeDef" = dataclasses.field()

    scanType = field("scanType")
    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetEncryptionKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetEncryptionKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceMapFilter:
    boto3_raw_data: "type_defs.ResourceMapFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceMapFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceMapFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceStringFilter:
    boto3_raw_data: "type_defs.ResourceStringFilterTypeDef" = dataclasses.field()

    comparison = field("comparison")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceStringFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceStringFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchVulnerabilitiesFilterCriteria:
    boto3_raw_data: "type_defs.SearchVulnerabilitiesFilterCriteriaTypeDef" = (
        dataclasses.field()
    )

    vulnerabilityIds = field("vulnerabilityIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchVulnerabilitiesFilterCriteriaTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchVulnerabilitiesFilterCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendCisSessionHealthRequest:
    boto3_raw_data: "type_defs.SendCisSessionHealthRequestTypeDef" = dataclasses.field()

    scanJobId = field("scanJobId")
    sessionToken = field("sessionToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendCisSessionHealthRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendCisSessionHealthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCisSessionMessage:
    boto3_raw_data: "type_defs.StartCisSessionMessageTypeDef" = dataclasses.field()

    sessionToken = field("sessionToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCisSessionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCisSessionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopCisMessageProgress:
    boto3_raw_data: "type_defs.StopCisMessageProgressTypeDef" = dataclasses.field()

    totalChecks = field("totalChecks")
    successfulChecks = field("successfulChecks")
    failedChecks = field("failedChecks")
    notEvaluatedChecks = field("notEvaluatedChecks")
    unknownChecks = field("unknownChecks")
    notApplicableChecks = field("notApplicableChecks")
    informationalChecks = field("informationalChecks")
    errorChecks = field("errorChecks")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopCisMessageProgressTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopCisMessageProgressTypeDef"]
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
class UpdateCisTargets:
    boto3_raw_data: "type_defs.UpdateCisTargetsTypeDef" = dataclasses.field()

    accountIds = field("accountIds")
    targetResourceTags = field("targetResourceTags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateCisTargetsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCisTargetsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEc2DeepInspectionConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateEc2DeepInspectionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    activateDeepInspection = field("activateDeepInspection")
    packagePaths = field("packagePaths")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEc2DeepInspectionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEc2DeepInspectionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEncryptionKeyRequest:
    boto3_raw_data: "type_defs.UpdateEncryptionKeyRequestTypeDef" = dataclasses.field()

    kmsKeyId = field("kmsKeyId")
    scanType = field("scanType")
    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEncryptionKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEncryptionKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGitHubIntegrationDetail:
    boto3_raw_data: "type_defs.UpdateGitHubIntegrationDetailTypeDef" = (
        dataclasses.field()
    )

    code = field("code")
    installationId = field("installationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGitHubIntegrationDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGitHubIntegrationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGitLabSelfManagedIntegrationDetail:
    boto3_raw_data: "type_defs.UpdateGitLabSelfManagedIntegrationDetailTypeDef" = (
        dataclasses.field()
    )

    authCode = field("authCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateGitLabSelfManagedIntegrationDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGitLabSelfManagedIntegrationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOrgEc2DeepInspectionConfigurationRequest:
    boto3_raw_data: (
        "type_defs.UpdateOrgEc2DeepInspectionConfigurationRequestTypeDef"
    ) = dataclasses.field()

    orgPackagePaths = field("orgPackagePaths")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOrgEc2DeepInspectionConfigurationRequestTypeDef"
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
                "type_defs.UpdateOrgEc2DeepInspectionConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Usage:
    boto3_raw_data: "type_defs.UsageTypeDef" = dataclasses.field()

    type = field("type")
    total = field("total")
    estimatedMonthlyCost = field("estimatedMonthlyCost")
    currency = field("currency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountAggregationResponse:
    boto3_raw_data: "type_defs.AccountAggregationResponseTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    exploitAvailableCount = field("exploitAvailableCount")
    fixAvailableCount = field("fixAvailableCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountAggregationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmiAggregationResponse:
    boto3_raw_data: "type_defs.AmiAggregationResponseTypeDef" = dataclasses.field()

    ami = field("ami")
    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    affectedInstances = field("affectedInstances")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AmiAggregationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmiAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsEcrContainerAggregationResponse:
    boto3_raw_data: "type_defs.AwsEcrContainerAggregationResponseTypeDef" = (
        dataclasses.field()
    )

    resourceId = field("resourceId")
    imageSha = field("imageSha")
    repository = field("repository")
    architecture = field("architecture")
    imageTags = field("imageTags")
    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    lastInUseAt = field("lastInUseAt")
    inUseCount = field("inUseCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AwsEcrContainerAggregationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsEcrContainerAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeRepositoryAggregationResponse:
    boto3_raw_data: "type_defs.CodeRepositoryAggregationResponseTypeDef" = (
        dataclasses.field()
    )

    projectNames = field("projectNames")
    providerType = field("providerType")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    exploitAvailableActiveFindingsCount = field("exploitAvailableActiveFindingsCount")
    fixAvailableActiveFindingsCount = field("fixAvailableActiveFindingsCount")
    accountId = field("accountId")
    resourceId = field("resourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CodeRepositoryAggregationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeRepositoryAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2InstanceAggregationResponse:
    boto3_raw_data: "type_defs.Ec2InstanceAggregationResponseTypeDef" = (
        dataclasses.field()
    )

    instanceId = field("instanceId")
    ami = field("ami")
    operatingSystem = field("operatingSystem")
    instanceTags = field("instanceTags")
    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    networkFindings = field("networkFindings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.Ec2InstanceAggregationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2InstanceAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingTypeAggregationResponse:
    boto3_raw_data: "type_defs.FindingTypeAggregationResponseTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    exploitAvailableCount = field("exploitAvailableCount")
    fixAvailableCount = field("fixAvailableCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FindingTypeAggregationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FindingTypeAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageLayerAggregationResponse:
    boto3_raw_data: "type_defs.ImageLayerAggregationResponseTypeDef" = (
        dataclasses.field()
    )

    repository = field("repository")
    resourceId = field("resourceId")
    layerHash = field("layerHash")
    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImageLayerAggregationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageLayerAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionAggregationResponse:
    boto3_raw_data: "type_defs.LambdaFunctionAggregationResponseTypeDef" = (
        dataclasses.field()
    )

    resourceId = field("resourceId")
    functionName = field("functionName")
    runtime = field("runtime")
    lambdaTags = field("lambdaTags")
    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    lastModifiedAt = field("lastModifiedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionAggregationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaLayerAggregationResponse:
    boto3_raw_data: "type_defs.LambdaLayerAggregationResponseTypeDef" = (
        dataclasses.field()
    )

    functionName = field("functionName")
    resourceId = field("resourceId")
    layerArn = field("layerArn")
    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LambdaLayerAggregationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaLayerAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageAggregationResponse:
    boto3_raw_data: "type_defs.PackageAggregationResponseTypeDef" = dataclasses.field()

    packageName = field("packageName")
    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageAggregationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryAggregationResponse:
    boto3_raw_data: "type_defs.RepositoryAggregationResponseTypeDef" = (
        dataclasses.field()
    )

    repository = field("repository")
    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    affectedImages = field("affectedImages")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RepositoryAggregationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TitleAggregationResponse:
    boto3_raw_data: "type_defs.TitleAggregationResponseTypeDef" = dataclasses.field()

    title = field("title")
    vulnerabilityId = field("vulnerabilityId")
    accountId = field("accountId")

    @cached_property
    def severityCounts(self):  # pragma: no cover
        return SeverityCounts.make_one(self.boto3_raw_data["severityCounts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TitleAggregationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TitleAggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceState:
    boto3_raw_data: "type_defs.ResourceStateTypeDef" = dataclasses.field()

    @cached_property
    def ec2(self):  # pragma: no cover
        return State.make_one(self.boto3_raw_data["ec2"])

    @cached_property
    def ecr(self):  # pragma: no cover
        return State.make_one(self.boto3_raw_data["ecr"])

    @cached_property
    def lambda_(self):  # pragma: no cover
        return State.make_one(self.boto3_raw_data["lambda"])

    @cached_property
    def lambdaCode(self):  # pragma: no cover
        return State.make_one(self.boto3_raw_data["lambdaCode"])

    @cached_property
    def codeRepository(self):  # pragma: no cover
        return State.make_one(self.boto3_raw_data["codeRepository"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Account:
    boto3_raw_data: "type_defs.AccountTypeDef" = dataclasses.field()

    accountId = field("accountId")
    status = field("status")

    @cached_property
    def resourceStatus(self):  # pragma: no cover
        return ResourceStatus.make_one(self.boto3_raw_data["resourceStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedAccount:
    boto3_raw_data: "type_defs.FailedAccountTypeDef" = dataclasses.field()

    accountId = field("accountId")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")
    status = field("status")

    @cached_property
    def resourceStatus(self):  # pragma: no cover
        return ResourceStatus.make_one(self.boto3_raw_data["resourceStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailedAccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailedAccountTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmiAggregation:
    boto3_raw_data: "type_defs.AmiAggregationTypeDef" = dataclasses.field()

    @cached_property
    def amis(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["amis"])

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AmiAggregationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AmiAggregationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeRepositoryAggregation:
    boto3_raw_data: "type_defs.CodeRepositoryAggregationTypeDef" = dataclasses.field()

    @cached_property
    def projectNames(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["projectNames"])

    @cached_property
    def providerTypes(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["providerTypes"])

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @cached_property
    def resourceIds(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["resourceIds"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeRepositoryAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeRepositoryAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageLayerAggregation:
    boto3_raw_data: "type_defs.ImageLayerAggregationTypeDef" = dataclasses.field()

    @cached_property
    def repositories(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["repositories"])

    @cached_property
    def resourceIds(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["resourceIds"])

    @cached_property
    def layerHashes(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["layerHashes"])

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageLayerAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageLayerAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaLayerAggregation:
    boto3_raw_data: "type_defs.LambdaLayerAggregationTypeDef" = dataclasses.field()

    @cached_property
    def functionNames(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["functionNames"])

    @cached_property
    def resourceIds(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["resourceIds"])

    @cached_property
    def layerArns(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["layerArns"])

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaLayerAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaLayerAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageAggregation:
    boto3_raw_data: "type_defs.PackageAggregationTypeDef" = dataclasses.field()

    @cached_property
    def packageNames(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["packageNames"])

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RepositoryAggregation:
    boto3_raw_data: "type_defs.RepositoryAggregationTypeDef" = dataclasses.field()

    @cached_property
    def repositories(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["repositories"])

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RepositoryAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RepositoryAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TitleAggregation:
    boto3_raw_data: "type_defs.TitleAggregationTypeDef" = dataclasses.field()

    @cached_property
    def titles(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["titles"])

    @cached_property
    def vulnerabilityIds(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["vulnerabilityIds"])

    resourceType = field("resourceType")
    sortOrder = field("sortOrder")
    sortBy = field("sortBy")
    findingType = field("findingType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TitleAggregationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TitleAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateConfigurationRequest:
    boto3_raw_data: "type_defs.AssociateConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")

    @cached_property
    def resource(self):  # pragma: no cover
        return CodeSecurityResource.make_one(self.boto3_raw_data["resource"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSecurityScanConfigurationAssociationSummary:
    boto3_raw_data: (
        "type_defs.CodeSecurityScanConfigurationAssociationSummaryTypeDef"
    ) = dataclasses.field()

    @cached_property
    def resource(self):  # pragma: no cover
        return CodeSecurityResource.make_one(self.boto3_raw_data["resource"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CodeSecurityScanConfigurationAssociationSummaryTypeDef"
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
                "type_defs.CodeSecurityScanConfigurationAssociationSummaryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateConfigurationRequest:
    boto3_raw_data: "type_defs.DisassociateConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")

    @cached_property
    def resource(self):  # pragma: no cover
        return CodeSecurityResource.make_one(self.boto3_raw_data["resource"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedAssociationResult:
    boto3_raw_data: "type_defs.FailedAssociationResultTypeDef" = dataclasses.field()

    scanConfigurationArn = field("scanConfigurationArn")

    @cached_property
    def resource(self):  # pragma: no cover
        return CodeSecurityResource.make_one(self.boto3_raw_data["resource"])

    statusCode = field("statusCode")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailedAssociationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodeSecurityScanRequest:
    boto3_raw_data: "type_defs.GetCodeSecurityScanRequestTypeDef" = dataclasses.field()

    @cached_property
    def resource(self):  # pragma: no cover
        return CodeSecurityResource.make_one(self.boto3_raw_data["resource"])

    scanId = field("scanId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCodeSecurityScanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeSecurityScanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCodeSecurityScanRequest:
    boto3_raw_data: "type_defs.StartCodeSecurityScanRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resource(self):  # pragma: no cover
        return CodeSecurityResource.make_one(self.boto3_raw_data["resource"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCodeSecurityScanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCodeSecurityScanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuccessfulAssociationResult:
    boto3_raw_data: "type_defs.SuccessfulAssociationResultTypeDef" = dataclasses.field()

    scanConfigurationArn = field("scanConfigurationArn")

    @cached_property
    def resource(self):  # pragma: no cover
        return CodeSecurityResource.make_one(self.boto3_raw_data["resource"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuccessfulAssociationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuccessfulAssociationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateMemberResponse:
    boto3_raw_data: "type_defs.AssociateMemberResponseTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateMemberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMemberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelFindingsReportResponse:
    boto3_raw_data: "type_defs.CancelFindingsReportResponseTypeDef" = (
        dataclasses.field()
    )

    reportId = field("reportId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelFindingsReportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelFindingsReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelSbomExportResponse:
    boto3_raw_data: "type_defs.CancelSbomExportResponseTypeDef" = dataclasses.field()

    reportId = field("reportId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelSbomExportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSbomExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCisScanConfigurationResponse:
    boto3_raw_data: "type_defs.CreateCisScanConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCisScanConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCisScanConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCodeSecurityIntegrationResponse:
    boto3_raw_data: "type_defs.CreateCodeSecurityIntegrationResponseTypeDef" = (
        dataclasses.field()
    )

    integrationArn = field("integrationArn")
    status = field("status")
    authorizationUrl = field("authorizationUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCodeSecurityIntegrationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCodeSecurityIntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCodeSecurityScanConfigurationResponse:
    boto3_raw_data: "type_defs.CreateCodeSecurityScanConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCodeSecurityScanConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCodeSecurityScanConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFilterResponse:
    boto3_raw_data: "type_defs.CreateFilterResponseTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFindingsReportResponse:
    boto3_raw_data: "type_defs.CreateFindingsReportResponseTypeDef" = (
        dataclasses.field()
    )

    reportId = field("reportId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFindingsReportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFindingsReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSbomExportResponse:
    boto3_raw_data: "type_defs.CreateSbomExportResponseTypeDef" = dataclasses.field()

    reportId = field("reportId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSbomExportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSbomExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCisScanConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteCisScanConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCisScanConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCisScanConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCodeSecurityIntegrationResponse:
    boto3_raw_data: "type_defs.DeleteCodeSecurityIntegrationResponseTypeDef" = (
        dataclasses.field()
    )

    integrationArn = field("integrationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCodeSecurityIntegrationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCodeSecurityIntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCodeSecurityScanConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteCodeSecurityScanConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCodeSecurityScanConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCodeSecurityScanConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFilterResponse:
    boto3_raw_data: "type_defs.DeleteFilterResponseTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableDelegatedAdminAccountResponse:
    boto3_raw_data: "type_defs.DisableDelegatedAdminAccountResponseTypeDef" = (
        dataclasses.field()
    )

    delegatedAdminAccountId = field("delegatedAdminAccountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisableDelegatedAdminAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableDelegatedAdminAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMemberResponse:
    boto3_raw_data: "type_defs.DisassociateMemberResponseTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateMemberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMemberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableDelegatedAdminAccountResponse:
    boto3_raw_data: "type_defs.EnableDelegatedAdminAccountResponseTypeDef" = (
        dataclasses.field()
    )

    delegatedAdminAccountId = field("delegatedAdminAccountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableDelegatedAdminAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableDelegatedAdminAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCisScanReportResponse:
    boto3_raw_data: "type_defs.GetCisScanReportResponseTypeDef" = dataclasses.field()

    url = field("url")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCisScanReportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCisScanReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodeSecurityIntegrationResponse:
    boto3_raw_data: "type_defs.GetCodeSecurityIntegrationResponseTypeDef" = (
        dataclasses.field()
    )

    integrationArn = field("integrationArn")
    name = field("name")
    type = field("type")
    status = field("status")
    statusReason = field("statusReason")
    createdOn = field("createdOn")
    lastUpdateOn = field("lastUpdateOn")
    tags = field("tags")
    authorizationUrl = field("authorizationUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCodeSecurityIntegrationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeSecurityIntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodeSecurityScanResponse:
    boto3_raw_data: "type_defs.GetCodeSecurityScanResponseTypeDef" = dataclasses.field()

    scanId = field("scanId")

    @cached_property
    def resource(self):  # pragma: no cover
        return CodeSecurityResource.make_one(self.boto3_raw_data["resource"])

    accountId = field("accountId")
    status = field("status")
    statusReason = field("statusReason")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    lastCommitId = field("lastCommitId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCodeSecurityScanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeSecurityScanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEc2DeepInspectionConfigurationResponse:
    boto3_raw_data: "type_defs.GetEc2DeepInspectionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    packagePaths = field("packagePaths")
    orgPackagePaths = field("orgPackagePaths")
    status = field("status")
    errorMessage = field("errorMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEc2DeepInspectionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEc2DeepInspectionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEncryptionKeyResponse:
    boto3_raw_data: "type_defs.GetEncryptionKeyResponseTypeDef" = dataclasses.field()

    kmsKeyId = field("kmsKeyId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEncryptionKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEncryptionKeyResponseTypeDef"]
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
class StartCodeSecurityScanResponse:
    boto3_raw_data: "type_defs.StartCodeSecurityScanResponseTypeDef" = (
        dataclasses.field()
    )

    scanId = field("scanId")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartCodeSecurityScanResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCodeSecurityScanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCisScanConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateCisScanConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCisScanConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCisScanConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCodeSecurityIntegrationResponse:
    boto3_raw_data: "type_defs.UpdateCodeSecurityIntegrationResponseTypeDef" = (
        dataclasses.field()
    )

    integrationArn = field("integrationArn")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCodeSecurityIntegrationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCodeSecurityIntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCodeSecurityScanConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateCodeSecurityScanConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCodeSecurityScanConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCodeSecurityScanConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEc2DeepInspectionConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateEc2DeepInspectionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    packagePaths = field("packagePaths")
    orgPackagePaths = field("orgPackagePaths")
    status = field("status")
    errorMessage = field("errorMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEc2DeepInspectionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEc2DeepInspectionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFilterResponse:
    boto3_raw_data: "type_defs.UpdateFilterResponseTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFilterResponseTypeDef"]
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

    @cached_property
    def autoEnable(self):  # pragma: no cover
        return AutoEnable.make_one(self.boto3_raw_data["autoEnable"])

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
class UpdateOrganizationConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateOrganizationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def autoEnable(self):  # pragma: no cover
        return AutoEnable.make_one(self.boto3_raw_data["autoEnable"])

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
class UpdateOrganizationConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateOrganizationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def autoEnable(self):  # pragma: no cover
        return AutoEnable.make_one(self.boto3_raw_data["autoEnable"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOrganizationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOrganizationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageFilter:
    boto3_raw_data: "type_defs.PackageFilterTypeDef" = dataclasses.field()

    @cached_property
    def name(self):  # pragma: no cover
        return StringFilter.make_one(self.boto3_raw_data["name"])

    @cached_property
    def version(self):  # pragma: no cover
        return StringFilter.make_one(self.boto3_raw_data["version"])

    @cached_property
    def epoch(self):  # pragma: no cover
        return NumberFilter.make_one(self.boto3_raw_data["epoch"])

    @cached_property
    def release(self):  # pragma: no cover
        return StringFilter.make_one(self.boto3_raw_data["release"])

    @cached_property
    def architecture(self):  # pragma: no cover
        return StringFilter.make_one(self.boto3_raw_data["architecture"])

    @cached_property
    def sourceLayerHash(self):  # pragma: no cover
        return StringFilter.make_one(self.boto3_raw_data["sourceLayerHash"])

    @cached_property
    def sourceLambdaLayerArn(self):  # pragma: no cover
        return StringFilter.make_one(self.boto3_raw_data["sourceLambdaLayerArn"])

    @cached_property
    def filePath(self):  # pragma: no cover
        return StringFilter.make_one(self.boto3_raw_data["filePath"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PackageFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PackageFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsEksMetadataDetails:
    boto3_raw_data: "type_defs.AwsEksMetadataDetailsTypeDef" = dataclasses.field()

    namespace = field("namespace")

    @cached_property
    def workloadInfoList(self):  # pragma: no cover
        return AwsEksWorkloadInfo.make_many(self.boto3_raw_data["workloadInfoList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsEksMetadataDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsEksMetadataDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsLambdaFunctionDetails:
    boto3_raw_data: "type_defs.AwsLambdaFunctionDetailsTypeDef" = dataclasses.field()

    functionName = field("functionName")
    runtime = field("runtime")
    codeSha256 = field("codeSha256")
    version = field("version")
    executionRoleArn = field("executionRoleArn")
    layers = field("layers")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return LambdaVpcConfig.make_one(self.boto3_raw_data["vpcConfig"])

    packageType = field("packageType")
    architectures = field("architectures")
    lastModifiedAt = field("lastModifiedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsLambdaFunctionDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsLambdaFunctionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetMemberEc2DeepInspectionStatusResponse:
    boto3_raw_data: "type_defs.BatchGetMemberEc2DeepInspectionStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accountIds(self):  # pragma: no cover
        return MemberAccountEc2DeepInspectionStatusState.make_many(
            self.boto3_raw_data["accountIds"]
        )

    @cached_property
    def failedAccountIds(self):  # pragma: no cover
        return FailedMemberAccountEc2DeepInspectionStatusState.make_many(
            self.boto3_raw_data["failedAccountIds"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetMemberEc2DeepInspectionStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetMemberEc2DeepInspectionStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateMemberEc2DeepInspectionStatusResponse:
    boto3_raw_data: (
        "type_defs.BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def accountIds(self):  # pragma: no cover
        return MemberAccountEc2DeepInspectionStatusState.make_many(
            self.boto3_raw_data["accountIds"]
        )

    @cached_property
    def failedAccountIds(self):  # pragma: no cover
        return FailedMemberAccountEc2DeepInspectionStatusState.make_many(
            self.boto3_raw_data["failedAccountIds"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef"
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
                "type_defs.BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateMemberEc2DeepInspectionStatusRequest:
    boto3_raw_data: (
        "type_defs.BatchUpdateMemberEc2DeepInspectionStatusRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def accountIds(self):  # pragma: no cover
        return MemberAccountEc2DeepInspectionStatus.make_many(
            self.boto3_raw_data["accountIds"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateMemberEc2DeepInspectionStatusRequestTypeDef"
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
                "type_defs.BatchUpdateMemberEc2DeepInspectionStatusRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisSessionMessage:
    boto3_raw_data: "type_defs.CisSessionMessageTypeDef" = dataclasses.field()

    ruleId = field("ruleId")
    status = field("status")
    cisRuleDetails = field("cisRuleDetails")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CisSessionMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisSessionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisCheckAggregation:
    boto3_raw_data: "type_defs.CisCheckAggregationTypeDef" = dataclasses.field()

    scanArn = field("scanArn")
    checkId = field("checkId")
    title = field("title")
    checkDescription = field("checkDescription")
    level = field("level")
    accountId = field("accountId")

    @cached_property
    def statusCounts(self):  # pragma: no cover
        return StatusCounts.make_one(self.boto3_raw_data["statusCounts"])

    platform = field("platform")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CisCheckAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisCheckAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisTargetResourceAggregation:
    boto3_raw_data: "type_defs.CisTargetResourceAggregationTypeDef" = (
        dataclasses.field()
    )

    scanArn = field("scanArn")
    targetResourceId = field("targetResourceId")
    accountId = field("accountId")
    targetResourceTags = field("targetResourceTags")

    @cached_property
    def statusCounts(self):  # pragma: no cover
        return StatusCounts.make_one(self.boto3_raw_data["statusCounts"])

    platform = field("platform")
    targetStatus = field("targetStatus")
    targetStatusReason = field("targetStatusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CisTargetResourceAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisTargetResourceAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisDateFilter:
    boto3_raw_data: "type_defs.CisDateFilterTypeDef" = dataclasses.field()

    earliestScanStartTime = field("earliestScanStartTime")
    latestScanStartTime = field("latestScanStartTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CisDateFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CisDateFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageDateFilter:
    boto3_raw_data: "type_defs.CoverageDateFilterTypeDef" = dataclasses.field()

    startInclusive = field("startInclusive")
    endInclusive = field("endInclusive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageDateFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateFilter:
    boto3_raw_data: "type_defs.DateFilterTypeDef" = dataclasses.field()

    startInclusive = field("startInclusive")
    endInclusive = field("endInclusive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisScan:
    boto3_raw_data: "type_defs.CisScanTypeDef" = dataclasses.field()

    scanArn = field("scanArn")
    scanConfigurationArn = field("scanConfigurationArn")
    status = field("status")
    scanName = field("scanName")
    scanDate = field("scanDate")
    failedChecks = field("failedChecks")
    totalChecks = field("totalChecks")

    @cached_property
    def targets(self):  # pragma: no cover
        return CisTargets.make_one(self.boto3_raw_data["targets"])

    scheduledBy = field("scheduledBy")
    securityLevel = field("securityLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CisScanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CisScanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisScanResultDetailsFilterCriteria:
    boto3_raw_data: "type_defs.CisScanResultDetailsFilterCriteriaTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def findingStatusFilters(self):  # pragma: no cover
        return CisFindingStatusFilter.make_many(
            self.boto3_raw_data["findingStatusFilters"]
        )

    @cached_property
    def checkIdFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["checkIdFilters"])

    @cached_property
    def titleFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["titleFilters"])

    @cached_property
    def securityLevelFilters(self):  # pragma: no cover
        return CisSecurityLevelFilter.make_many(
            self.boto3_raw_data["securityLevelFilters"]
        )

    @cached_property
    def findingArnFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["findingArnFilters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CisScanResultDetailsFilterCriteriaTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisScanResultDetailsFilterCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisScanResultsAggregatedByChecksFilterCriteria:
    boto3_raw_data: (
        "type_defs.CisScanResultsAggregatedByChecksFilterCriteriaTypeDef"
    ) = dataclasses.field()

    @cached_property
    def accountIdFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["accountIdFilters"])

    @cached_property
    def checkIdFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["checkIdFilters"])

    @cached_property
    def titleFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["titleFilters"])

    @cached_property
    def platformFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["platformFilters"])

    @cached_property
    def failedResourcesFilters(self):  # pragma: no cover
        return CisNumberFilter.make_many(self.boto3_raw_data["failedResourcesFilters"])

    @cached_property
    def securityLevelFilters(self):  # pragma: no cover
        return CisSecurityLevelFilter.make_many(
            self.boto3_raw_data["securityLevelFilters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CisScanResultsAggregatedByChecksFilterCriteriaTypeDef"
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
                "type_defs.CisScanResultsAggregatedByChecksFilterCriteriaTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCisScanResultDetailsResponse:
    boto3_raw_data: "type_defs.GetCisScanResultDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def scanResultDetails(self):  # pragma: no cover
        return CisScanResultDetails.make_many(self.boto3_raw_data["scanResultDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCisScanResultDetailsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCisScanResultDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisScanResultsAggregatedByTargetResourceFilterCriteria:
    boto3_raw_data: (
        "type_defs.CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef"
    ) = dataclasses.field()

    @cached_property
    def accountIdFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["accountIdFilters"])

    @cached_property
    def statusFilters(self):  # pragma: no cover
        return CisResultStatusFilter.make_many(self.boto3_raw_data["statusFilters"])

    @cached_property
    def checkIdFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["checkIdFilters"])

    @cached_property
    def targetResourceIdFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["targetResourceIdFilters"])

    @cached_property
    def targetResourceTagFilters(self):  # pragma: no cover
        return TagFilter.make_many(self.boto3_raw_data["targetResourceTagFilters"])

    @cached_property
    def platformFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["platformFilters"])

    @cached_property
    def targetStatusFilters(self):  # pragma: no cover
        return CisTargetStatusFilter.make_many(
            self.boto3_raw_data["targetStatusFilters"]
        )

    @cached_property
    def targetStatusReasonFilters(self):  # pragma: no cover
        return CisTargetStatusReasonFilter.make_many(
            self.boto3_raw_data["targetStatusReasonFilters"]
        )

    @cached_property
    def failedChecksFilters(self):  # pragma: no cover
        return CisNumberFilter.make_many(self.boto3_raw_data["failedChecksFilters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef"
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
                "type_defs.CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScanConfigurationsFilterCriteria:
    boto3_raw_data: "type_defs.ListCisScanConfigurationsFilterCriteriaTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def scanNameFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["scanNameFilters"])

    @cached_property
    def targetResourceTagFilters(self):  # pragma: no cover
        return TagFilter.make_many(self.boto3_raw_data["targetResourceTagFilters"])

    @cached_property
    def scanConfigurationArnFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(
            self.boto3_raw_data["scanConfigurationArnFilters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCisScanConfigurationsFilterCriteriaTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCisScanConfigurationsFilterCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClustersForImageRequest:
    boto3_raw_data: "type_defs.GetClustersForImageRequestTypeDef" = dataclasses.field()

    @cached_property
    def filter(self):  # pragma: no cover
        return ClusterForImageFilterCriteria.make_one(self.boto3_raw_data["filter"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetClustersForImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClustersForImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeVulnerabilityDetails:
    boto3_raw_data: "type_defs.CodeVulnerabilityDetailsTypeDef" = dataclasses.field()

    @cached_property
    def filePath(self):  # pragma: no cover
        return CodeFilePath.make_one(self.boto3_raw_data["filePath"])

    detectorId = field("detectorId")
    detectorName = field("detectorName")
    cwes = field("cwes")
    detectorTags = field("detectorTags")
    referenceUrls = field("referenceUrls")
    ruleId = field("ruleId")
    sourceLambdaLayerArn = field("sourceLambdaLayerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeVulnerabilityDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeVulnerabilityDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeRepositoryOnDemandScan:
    boto3_raw_data: "type_defs.CodeRepositoryOnDemandScanTypeDef" = dataclasses.field()

    lastScannedCommitId = field("lastScannedCommitId")
    lastScanAt = field("lastScanAt")

    @cached_property
    def scanStatus(self):  # pragma: no cover
        return ScanStatus.make_one(self.boto3_raw_data["scanStatus"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeRepositoryOnDemandScanTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeRepositoryOnDemandScanTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeSecurityIntegrationsResponse:
    boto3_raw_data: "type_defs.ListCodeSecurityIntegrationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def integrations(self):  # pragma: no cover
        return CodeSecurityIntegrationSummary.make_many(
            self.boto3_raw_data["integrations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCodeSecurityIntegrationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeSecurityIntegrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSecurityScanConfigurationOutput:
    boto3_raw_data: "type_defs.CodeSecurityScanConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    ruleSetCategories = field("ruleSetCategories")

    @cached_property
    def periodicScanConfiguration(self):  # pragma: no cover
        return PeriodicScanConfiguration.make_one(
            self.boto3_raw_data["periodicScanConfiguration"]
        )

    @cached_property
    def continuousIntegrationScanConfiguration(self):  # pragma: no cover
        return ContinuousIntegrationScanConfigurationOutput.make_one(
            self.boto3_raw_data["continuousIntegrationScanConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CodeSecurityScanConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSecurityScanConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSecurityScanConfigurationSummary:
    boto3_raw_data: "type_defs.CodeSecurityScanConfigurationSummaryTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")
    name = field("name")
    ownerAccountId = field("ownerAccountId")
    ruleSetCategories = field("ruleSetCategories")
    periodicScanFrequency = field("periodicScanFrequency")
    frequencyExpression = field("frequencyExpression")
    continuousIntegrationScanSupportedEvents = field(
        "continuousIntegrationScanSupportedEvents"
    )

    @cached_property
    def scopeSettings(self):  # pragma: no cover
        return ScopeSettings.make_one(self.boto3_raw_data["scopeSettings"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CodeSecurityScanConfigurationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSecurityScanConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSecurityScanConfiguration:
    boto3_raw_data: "type_defs.CodeSecurityScanConfigurationTypeDef" = (
        dataclasses.field()
    )

    ruleSetCategories = field("ruleSetCategories")

    @cached_property
    def periodicScanConfiguration(self):  # pragma: no cover
        return PeriodicScanConfiguration.make_one(
            self.boto3_raw_data["periodicScanConfiguration"]
        )

    @cached_property
    def continuousIntegrationScanConfiguration(self):  # pragma: no cover
        return ContinuousIntegrationScanConfiguration.make_one(
            self.boto3_raw_data["continuousIntegrationScanConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CodeSecurityScanConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSecurityScanConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeSnippetResult:
    boto3_raw_data: "type_defs.CodeSnippetResultTypeDef" = dataclasses.field()

    findingArn = field("findingArn")
    startLine = field("startLine")
    endLine = field("endLine")

    @cached_property
    def codeSnippet(self):  # pragma: no cover
        return CodeLine.make_many(self.boto3_raw_data["codeSnippet"])

    @cached_property
    def suggestedFixes(self):  # pragma: no cover
        return SuggestedFix.make_many(self.boto3_raw_data["suggestedFixes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodeSnippetResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeSnippetResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoverageStatisticsResponse:
    boto3_raw_data: "type_defs.ListCoverageStatisticsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def countsByGroup(self):  # pragma: no cover
        return Counts.make_many(self.boto3_raw_data["countsByGroup"])

    totalCounts = field("totalCounts")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCoverageStatisticsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoverageStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntegrationDetail:
    boto3_raw_data: "type_defs.CreateIntegrationDetailTypeDef" = dataclasses.field()

    @cached_property
    def gitlabSelfManaged(self):  # pragma: no cover
        return CreateGitLabSelfManagedIntegrationDetail.make_one(
            self.boto3_raw_data["gitlabSelfManaged"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIntegrationDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntegrationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CvssScoreDetails:
    boto3_raw_data: "type_defs.CvssScoreDetailsTypeDef" = dataclasses.field()

    scoreSource = field("scoreSource")
    version = field("version")
    score = field("score")
    scoringVector = field("scoringVector")
    cvssSource = field("cvssSource")

    @cached_property
    def adjustments(self):  # pragma: no cover
        return CvssScoreAdjustment.make_many(self.boto3_raw_data["adjustments"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CvssScoreDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CvssScoreDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DailySchedule:
    boto3_raw_data: "type_defs.DailyScheduleTypeDef" = dataclasses.field()

    @cached_property
    def startTime(self):  # pragma: no cover
        return Time.make_one(self.boto3_raw_data["startTime"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DailyScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DailyScheduleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonthlySchedule:
    boto3_raw_data: "type_defs.MonthlyScheduleTypeDef" = dataclasses.field()

    @cached_property
    def startTime(self):  # pragma: no cover
        return Time.make_one(self.boto3_raw_data["startTime"])

    day = field("day")

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
class WeeklyScheduleOutput:
    boto3_raw_data: "type_defs.WeeklyScheduleOutputTypeDef" = dataclasses.field()

    @cached_property
    def startTime(self):  # pragma: no cover
        return Time.make_one(self.boto3_raw_data["startTime"])

    days = field("days")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WeeklyScheduleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WeeklyScheduleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WeeklySchedule:
    boto3_raw_data: "type_defs.WeeklyScheduleTypeDef" = dataclasses.field()

    @cached_property
    def startTime(self):  # pragma: no cover
        return Time.make_one(self.boto3_raw_data["startTime"])

    days = field("days")

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
class ListDelegatedAdminAccountsResponse:
    boto3_raw_data: "type_defs.ListDelegatedAdminAccountsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def delegatedAdminAccounts(self):  # pragma: no cover
        return DelegatedAdminAccount.make_many(
            self.boto3_raw_data["delegatedAdminAccounts"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDelegatedAdminAccountsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDelegatedAdminAccountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDelegatedAdminAccountResponse:
    boto3_raw_data: "type_defs.GetDelegatedAdminAccountResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def delegatedAdmin(self):  # pragma: no cover
        return DelegatedAdmin.make_one(self.boto3_raw_data["delegatedAdmin"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDelegatedAdminAccountResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDelegatedAdminAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2ConfigurationState:
    boto3_raw_data: "type_defs.Ec2ConfigurationStateTypeDef" = dataclasses.field()

    @cached_property
    def scanModeState(self):  # pragma: no cover
        return Ec2ScanModeState.make_one(self.boto3_raw_data["scanModeState"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Ec2ConfigurationStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2ConfigurationStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ec2InstanceAggregation:
    boto3_raw_data: "type_defs.Ec2InstanceAggregationTypeDef" = dataclasses.field()

    @cached_property
    def amis(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["amis"])

    @cached_property
    def operatingSystems(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["operatingSystems"])

    @cached_property
    def instanceIds(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["instanceIds"])

    @cached_property
    def instanceTags(self):  # pragma: no cover
        return MapFilter.make_many(self.boto3_raw_data["instanceTags"])

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Ec2InstanceAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ec2InstanceAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionAggregation:
    boto3_raw_data: "type_defs.LambdaFunctionAggregationTypeDef" = dataclasses.field()

    @cached_property
    def resourceIds(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["resourceIds"])

    @cached_property
    def functionNames(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["functionNames"])

    @cached_property
    def runtimes(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["runtimes"])

    @cached_property
    def functionTags(self):  # pragma: no cover
        return MapFilter.make_many(self.boto3_raw_data["functionTags"])

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaFunctionAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcrConfigurationState:
    boto3_raw_data: "type_defs.EcrConfigurationStateTypeDef" = dataclasses.field()

    @cached_property
    def rescanDurationState(self):  # pragma: no cover
        return EcrRescanDurationState.make_one(
            self.boto3_raw_data["rescanDurationState"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcrConfigurationStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcrConfigurationStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateConfigurationRequestTypeDef" = dataclasses.field()

    @cached_property
    def ecrConfiguration(self):  # pragma: no cover
        return EcrConfiguration.make_one(self.boto3_raw_data["ecrConfiguration"])

    @cached_property
    def ec2Configuration(self):  # pragma: no cover
        return Ec2Configuration.make_one(self.boto3_raw_data["ec2Configuration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FindingDetail:
    boto3_raw_data: "type_defs.FindingDetailTypeDef" = dataclasses.field()

    findingArn = field("findingArn")

    @cached_property
    def cisaData(self):  # pragma: no cover
        return CisaData.make_one(self.boto3_raw_data["cisaData"])

    riskScore = field("riskScore")

    @cached_property
    def evidences(self):  # pragma: no cover
        return Evidence.make_many(self.boto3_raw_data["evidences"])

    ttps = field("ttps")
    tools = field("tools")

    @cached_property
    def exploitObserved(self):  # pragma: no cover
        return ExploitObserved.make_one(self.boto3_raw_data["exploitObserved"])

    referenceUrls = field("referenceUrls")
    cwes = field("cwes")
    epssScore = field("epssScore")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FindingDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FindingDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Vulnerability:
    boto3_raw_data: "type_defs.VulnerabilityTypeDef" = dataclasses.field()

    id = field("id")
    cwes = field("cwes")

    @cached_property
    def cisaData(self):  # pragma: no cover
        return CisaData.make_one(self.boto3_raw_data["cisaData"])

    source = field("source")
    description = field("description")

    @cached_property
    def atigData(self):  # pragma: no cover
        return AtigData.make_one(self.boto3_raw_data["atigData"])

    vendorSeverity = field("vendorSeverity")

    @cached_property
    def cvss4(self):  # pragma: no cover
        return Cvss4.make_one(self.boto3_raw_data["cvss4"])

    @cached_property
    def cvss3(self):  # pragma: no cover
        return Cvss3.make_one(self.boto3_raw_data["cvss3"])

    relatedVulnerabilities = field("relatedVulnerabilities")

    @cached_property
    def cvss2(self):  # pragma: no cover
        return Cvss2.make_one(self.boto3_raw_data["cvss2"])

    vendorCreatedAt = field("vendorCreatedAt")
    vendorUpdatedAt = field("vendorUpdatedAt")
    sourceUrl = field("sourceUrl")
    referenceUrls = field("referenceUrls")

    @cached_property
    def exploitObserved(self):  # pragma: no cover
        return ExploitObserved.make_one(self.boto3_raw_data["exploitObserved"])

    detectionPlatforms = field("detectionPlatforms")

    @cached_property
    def epss(self):  # pragma: no cover
        return Epss.make_one(self.boto3_raw_data["epss"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VulnerabilityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VulnerabilityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FreeTrialAccountInfo:
    boto3_raw_data: "type_defs.FreeTrialAccountInfoTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @cached_property
    def freeTrialInfo(self):  # pragma: no cover
        return FreeTrialInfo.make_many(self.boto3_raw_data["freeTrialInfo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FreeTrialAccountInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FreeTrialAccountInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClustersForImageRequestPaginate:
    boto3_raw_data: "type_defs.GetClustersForImageRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filter(self):  # pragma: no cover
        return ClusterForImageFilterCriteria.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetClustersForImageRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClustersForImageRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountPermissionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAccountPermissionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    service = field("service")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountPermissionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountPermissionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDelegatedAdminAccountsRequestPaginate:
    boto3_raw_data: "type_defs.ListDelegatedAdminAccountsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDelegatedAdminAccountsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDelegatedAdminAccountsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFiltersRequestPaginate:
    boto3_raw_data: "type_defs.ListFiltersRequestPaginateTypeDef" = dataclasses.field()

    arns = field("arns")
    action = field("action")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFiltersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFiltersRequestPaginateTypeDef"]
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
class ListUsageTotalsRequestPaginate:
    boto3_raw_data: "type_defs.ListUsageTotalsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    accountIds = field("accountIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListUsageTotalsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsageTotalsRequestPaginateTypeDef"]
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

    @cached_property
    def member(self):  # pragma: no cover
        return Member.make_one(self.boto3_raw_data["member"])

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
class ListAccountPermissionsResponse:
    boto3_raw_data: "type_defs.ListAccountPermissionsResponseTypeDef" = (
        dataclasses.field()
    )

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
        boto3_raw_data: T.Optional["type_defs.ListAccountPermissionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountPermissionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkPath:
    boto3_raw_data: "type_defs.NetworkPathTypeDef" = dataclasses.field()

    @cached_property
    def steps(self):  # pragma: no cover
        return Step.make_many(self.boto3_raw_data["steps"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkPathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NetworkPathTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackageVulnerabilityDetails:
    boto3_raw_data: "type_defs.PackageVulnerabilityDetailsTypeDef" = dataclasses.field()

    vulnerabilityId = field("vulnerabilityId")
    source = field("source")

    @cached_property
    def vulnerablePackages(self):  # pragma: no cover
        return VulnerablePackage.make_many(self.boto3_raw_data["vulnerablePackages"])

    @cached_property
    def cvss(self):  # pragma: no cover
        return CvssScore.make_many(self.boto3_raw_data["cvss"])

    relatedVulnerabilities = field("relatedVulnerabilities")
    sourceUrl = field("sourceUrl")
    vendorSeverity = field("vendorSeverity")
    vendorCreatedAt = field("vendorCreatedAt")
    vendorUpdatedAt = field("vendorUpdatedAt")
    referenceUrls = field("referenceUrls")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackageVulnerabilityDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackageVulnerabilityDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectCodeSecurityScanConfiguration:
    boto3_raw_data: "type_defs.ProjectCodeSecurityScanConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def periodicScanConfigurations(self):  # pragma: no cover
        return ProjectPeriodicScanConfiguration.make_many(
            self.boto3_raw_data["periodicScanConfigurations"]
        )

    @cached_property
    def continuousIntegrationScanConfigurations(self):  # pragma: no cover
        return ProjectContinuousIntegrationScanConfiguration.make_many(
            self.boto3_raw_data["continuousIntegrationScanConfigurations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProjectCodeSecurityScanConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectCodeSecurityScanConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Remediation:
    boto3_raw_data: "type_defs.RemediationTypeDef" = dataclasses.field()

    @cached_property
    def recommendation(self):  # pragma: no cover
        return Recommendation.make_one(self.boto3_raw_data["recommendation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemediationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RemediationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceFilterCriteriaOutput:
    boto3_raw_data: "type_defs.ResourceFilterCriteriaOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accountId(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["accountId"])

    @cached_property
    def resourceId(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["resourceId"])

    @cached_property
    def resourceType(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["resourceType"])

    @cached_property
    def ecrRepositoryName(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["ecrRepositoryName"])

    @cached_property
    def lambdaFunctionName(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["lambdaFunctionName"])

    @cached_property
    def ecrImageTags(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["ecrImageTags"])

    @cached_property
    def ec2InstanceTags(self):  # pragma: no cover
        return ResourceMapFilter.make_many(self.boto3_raw_data["ec2InstanceTags"])

    @cached_property
    def lambdaFunctionTags(self):  # pragma: no cover
        return ResourceMapFilter.make_many(self.boto3_raw_data["lambdaFunctionTags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceFilterCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceFilterCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceFilterCriteria:
    boto3_raw_data: "type_defs.ResourceFilterCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def accountId(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["accountId"])

    @cached_property
    def resourceId(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["resourceId"])

    @cached_property
    def resourceType(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["resourceType"])

    @cached_property
    def ecrRepositoryName(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["ecrRepositoryName"])

    @cached_property
    def lambdaFunctionName(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["lambdaFunctionName"])

    @cached_property
    def ecrImageTags(self):  # pragma: no cover
        return ResourceStringFilter.make_many(self.boto3_raw_data["ecrImageTags"])

    @cached_property
    def ec2InstanceTags(self):  # pragma: no cover
        return ResourceMapFilter.make_many(self.boto3_raw_data["ec2InstanceTags"])

    @cached_property
    def lambdaFunctionTags(self):  # pragma: no cover
        return ResourceMapFilter.make_many(self.boto3_raw_data["lambdaFunctionTags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceFilterCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceFilterCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchVulnerabilitiesRequestPaginate:
    boto3_raw_data: "type_defs.SearchVulnerabilitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return SearchVulnerabilitiesFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchVulnerabilitiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchVulnerabilitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchVulnerabilitiesRequest:
    boto3_raw_data: "type_defs.SearchVulnerabilitiesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return SearchVulnerabilitiesFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchVulnerabilitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchVulnerabilitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCisSessionRequest:
    boto3_raw_data: "type_defs.StartCisSessionRequestTypeDef" = dataclasses.field()

    scanJobId = field("scanJobId")

    @cached_property
    def message(self):  # pragma: no cover
        return StartCisSessionMessage.make_one(self.boto3_raw_data["message"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCisSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCisSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopCisSessionMessage:
    boto3_raw_data: "type_defs.StopCisSessionMessageTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def progress(self):  # pragma: no cover
        return StopCisMessageProgress.make_one(self.boto3_raw_data["progress"])

    reason = field("reason")

    @cached_property
    def computePlatform(self):  # pragma: no cover
        return ComputePlatform.make_one(self.boto3_raw_data["computePlatform"])

    benchmarkVersion = field("benchmarkVersion")
    benchmarkProfile = field("benchmarkProfile")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopCisSessionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopCisSessionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIntegrationDetails:
    boto3_raw_data: "type_defs.UpdateIntegrationDetailsTypeDef" = dataclasses.field()

    @cached_property
    def gitlabSelfManaged(self):  # pragma: no cover
        return UpdateGitLabSelfManagedIntegrationDetail.make_one(
            self.boto3_raw_data["gitlabSelfManaged"]
        )

    @cached_property
    def github(self):  # pragma: no cover
        return UpdateGitHubIntegrationDetail.make_one(self.boto3_raw_data["github"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIntegrationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIntegrationDetailsTypeDef"]
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

    accountId = field("accountId")

    @cached_property
    def usage(self):  # pragma: no cover
        return Usage.make_many(self.boto3_raw_data["usage"])

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
class AggregationResponse:
    boto3_raw_data: "type_defs.AggregationResponseTypeDef" = dataclasses.field()

    @cached_property
    def accountAggregation(self):  # pragma: no cover
        return AccountAggregationResponse.make_one(
            self.boto3_raw_data["accountAggregation"]
        )

    @cached_property
    def amiAggregation(self):  # pragma: no cover
        return AmiAggregationResponse.make_one(self.boto3_raw_data["amiAggregation"])

    @cached_property
    def awsEcrContainerAggregation(self):  # pragma: no cover
        return AwsEcrContainerAggregationResponse.make_one(
            self.boto3_raw_data["awsEcrContainerAggregation"]
        )

    @cached_property
    def ec2InstanceAggregation(self):  # pragma: no cover
        return Ec2InstanceAggregationResponse.make_one(
            self.boto3_raw_data["ec2InstanceAggregation"]
        )

    @cached_property
    def findingTypeAggregation(self):  # pragma: no cover
        return FindingTypeAggregationResponse.make_one(
            self.boto3_raw_data["findingTypeAggregation"]
        )

    @cached_property
    def imageLayerAggregation(self):  # pragma: no cover
        return ImageLayerAggregationResponse.make_one(
            self.boto3_raw_data["imageLayerAggregation"]
        )

    @cached_property
    def packageAggregation(self):  # pragma: no cover
        return PackageAggregationResponse.make_one(
            self.boto3_raw_data["packageAggregation"]
        )

    @cached_property
    def repositoryAggregation(self):  # pragma: no cover
        return RepositoryAggregationResponse.make_one(
            self.boto3_raw_data["repositoryAggregation"]
        )

    @cached_property
    def titleAggregation(self):  # pragma: no cover
        return TitleAggregationResponse.make_one(
            self.boto3_raw_data["titleAggregation"]
        )

    @cached_property
    def lambdaLayerAggregation(self):  # pragma: no cover
        return LambdaLayerAggregationResponse.make_one(
            self.boto3_raw_data["lambdaLayerAggregation"]
        )

    @cached_property
    def lambdaFunctionAggregation(self):  # pragma: no cover
        return LambdaFunctionAggregationResponse.make_one(
            self.boto3_raw_data["lambdaFunctionAggregation"]
        )

    @cached_property
    def codeRepositoryAggregation(self):  # pragma: no cover
        return CodeRepositoryAggregationResponse.make_one(
            self.boto3_raw_data["codeRepositoryAggregation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountState:
    boto3_raw_data: "type_defs.AccountStateTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @cached_property
    def state(self):  # pragma: no cover
        return State.make_one(self.boto3_raw_data["state"])

    @cached_property
    def resourceState(self):  # pragma: no cover
        return ResourceState.make_one(self.boto3_raw_data["resourceState"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableResponse:
    boto3_raw_data: "type_defs.DisableResponseTypeDef" = dataclasses.field()

    @cached_property
    def accounts(self):  # pragma: no cover
        return Account.make_many(self.boto3_raw_data["accounts"])

    @cached_property
    def failedAccounts(self):  # pragma: no cover
        return FailedAccount.make_many(self.boto3_raw_data["failedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DisableResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DisableResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableResponse:
    boto3_raw_data: "type_defs.EnableResponseTypeDef" = dataclasses.field()

    @cached_property
    def accounts(self):  # pragma: no cover
        return Account.make_many(self.boto3_raw_data["accounts"])

    @cached_property
    def failedAccounts(self):  # pragma: no cover
        return FailedAccount.make_many(self.boto3_raw_data["failedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnableResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnableResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateCodeSecurityScanConfigurationRequest:
    boto3_raw_data: (
        "type_defs.BatchAssociateCodeSecurityScanConfigurationRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def associateConfigurationRequests(self):  # pragma: no cover
        return AssociateConfigurationRequest.make_many(
            self.boto3_raw_data["associateConfigurationRequests"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateCodeSecurityScanConfigurationRequestTypeDef"
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
                "type_defs.BatchAssociateCodeSecurityScanConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeSecurityScanConfigurationAssociationsResponse:
    boto3_raw_data: (
        "type_defs.ListCodeSecurityScanConfigurationAssociationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def associations(self):  # pragma: no cover
        return CodeSecurityScanConfigurationAssociationSummary.make_many(
            self.boto3_raw_data["associations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCodeSecurityScanConfigurationAssociationsResponseTypeDef"
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
                "type_defs.ListCodeSecurityScanConfigurationAssociationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateCodeSecurityScanConfigurationRequest:
    boto3_raw_data: (
        "type_defs.BatchDisassociateCodeSecurityScanConfigurationRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def disassociateConfigurationRequests(self):  # pragma: no cover
        return DisassociateConfigurationRequest.make_many(
            self.boto3_raw_data["disassociateConfigurationRequests"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateCodeSecurityScanConfigurationRequestTypeDef"
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
                "type_defs.BatchDisassociateCodeSecurityScanConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateCodeSecurityScanConfigurationResponse:
    boto3_raw_data: (
        "type_defs.BatchAssociateCodeSecurityScanConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def failedAssociations(self):  # pragma: no cover
        return FailedAssociationResult.make_many(
            self.boto3_raw_data["failedAssociations"]
        )

    @cached_property
    def successfulAssociations(self):  # pragma: no cover
        return SuccessfulAssociationResult.make_many(
            self.boto3_raw_data["successfulAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateCodeSecurityScanConfigurationResponseTypeDef"
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
                "type_defs.BatchAssociateCodeSecurityScanConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateCodeSecurityScanConfigurationResponse:
    boto3_raw_data: (
        "type_defs.BatchDisassociateCodeSecurityScanConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def failedAssociations(self):  # pragma: no cover
        return FailedAssociationResult.make_many(
            self.boto3_raw_data["failedAssociations"]
        )

    @cached_property
    def successfulAssociations(self):  # pragma: no cover
        return SuccessfulAssociationResult.make_many(
            self.boto3_raw_data["successfulAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateCodeSecurityScanConfigurationResponseTypeDef"
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
                "type_defs.BatchDisassociateCodeSecurityScanConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCriteriaOutput:
    boto3_raw_data: "type_defs.FilterCriteriaOutputTypeDef" = dataclasses.field()

    @cached_property
    def findingArn(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["findingArn"])

    @cached_property
    def awsAccountId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["awsAccountId"])

    @cached_property
    def findingType(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["findingType"])

    @cached_property
    def severity(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["severity"])

    @cached_property
    def firstObservedAt(self):  # pragma: no cover
        return DateFilterOutput.make_many(self.boto3_raw_data["firstObservedAt"])

    @cached_property
    def lastObservedAt(self):  # pragma: no cover
        return DateFilterOutput.make_many(self.boto3_raw_data["lastObservedAt"])

    @cached_property
    def updatedAt(self):  # pragma: no cover
        return DateFilterOutput.make_many(self.boto3_raw_data["updatedAt"])

    @cached_property
    def findingStatus(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["findingStatus"])

    @cached_property
    def title(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["title"])

    @cached_property
    def inspectorScore(self):  # pragma: no cover
        return NumberFilter.make_many(self.boto3_raw_data["inspectorScore"])

    @cached_property
    def resourceType(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["resourceType"])

    @cached_property
    def resourceId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["resourceId"])

    @cached_property
    def resourceTags(self):  # pragma: no cover
        return MapFilter.make_many(self.boto3_raw_data["resourceTags"])

    @cached_property
    def ec2InstanceImageId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ec2InstanceImageId"])

    @cached_property
    def ec2InstanceVpcId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ec2InstanceVpcId"])

    @cached_property
    def ec2InstanceSubnetId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ec2InstanceSubnetId"])

    @cached_property
    def ecrImagePushedAt(self):  # pragma: no cover
        return DateFilterOutput.make_many(self.boto3_raw_data["ecrImagePushedAt"])

    @cached_property
    def ecrImageArchitecture(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ecrImageArchitecture"])

    @cached_property
    def ecrImageRegistry(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ecrImageRegistry"])

    @cached_property
    def ecrImageRepositoryName(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ecrImageRepositoryName"])

    @cached_property
    def ecrImageTags(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ecrImageTags"])

    @cached_property
    def ecrImageHash(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ecrImageHash"])

    @cached_property
    def ecrImageLastInUseAt(self):  # pragma: no cover
        return DateFilterOutput.make_many(self.boto3_raw_data["ecrImageLastInUseAt"])

    @cached_property
    def ecrImageInUseCount(self):  # pragma: no cover
        return NumberFilter.make_many(self.boto3_raw_data["ecrImageInUseCount"])

    @cached_property
    def portRange(self):  # pragma: no cover
        return PortRangeFilter.make_many(self.boto3_raw_data["portRange"])

    @cached_property
    def networkProtocol(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["networkProtocol"])

    @cached_property
    def componentId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["componentId"])

    @cached_property
    def componentType(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["componentType"])

    @cached_property
    def vulnerabilityId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["vulnerabilityId"])

    @cached_property
    def vulnerabilitySource(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["vulnerabilitySource"])

    @cached_property
    def vendorSeverity(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["vendorSeverity"])

    @cached_property
    def vulnerablePackages(self):  # pragma: no cover
        return PackageFilter.make_many(self.boto3_raw_data["vulnerablePackages"])

    @cached_property
    def relatedVulnerabilities(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["relatedVulnerabilities"])

    @cached_property
    def fixAvailable(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["fixAvailable"])

    @cached_property
    def lambdaFunctionName(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["lambdaFunctionName"])

    @cached_property
    def lambdaFunctionLayers(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["lambdaFunctionLayers"])

    @cached_property
    def lambdaFunctionRuntime(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["lambdaFunctionRuntime"])

    @cached_property
    def lambdaFunctionLastModifiedAt(self):  # pragma: no cover
        return DateFilterOutput.make_many(
            self.boto3_raw_data["lambdaFunctionLastModifiedAt"]
        )

    @cached_property
    def lambdaFunctionExecutionRoleArn(self):  # pragma: no cover
        return StringFilter.make_many(
            self.boto3_raw_data["lambdaFunctionExecutionRoleArn"]
        )

    @cached_property
    def exploitAvailable(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["exploitAvailable"])

    @cached_property
    def codeVulnerabilityDetectorName(self):  # pragma: no cover
        return StringFilter.make_many(
            self.boto3_raw_data["codeVulnerabilityDetectorName"]
        )

    @cached_property
    def codeVulnerabilityDetectorTags(self):  # pragma: no cover
        return StringFilter.make_many(
            self.boto3_raw_data["codeVulnerabilityDetectorTags"]
        )

    @cached_property
    def codeVulnerabilityFilePath(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["codeVulnerabilityFilePath"])

    @cached_property
    def epssScore(self):  # pragma: no cover
        return NumberFilter.make_many(self.boto3_raw_data["epssScore"])

    @cached_property
    def codeRepositoryProjectName(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["codeRepositoryProjectName"])

    @cached_property
    def codeRepositoryProviderType(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["codeRepositoryProviderType"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterCriteriaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterCriteriaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterMetadata:
    boto3_raw_data: "type_defs.ClusterMetadataTypeDef" = dataclasses.field()

    @cached_property
    def awsEcsMetadataDetails(self):  # pragma: no cover
        return AwsEcsMetadataDetails.make_one(
            self.boto3_raw_data["awsEcsMetadataDetails"]
        )

    @cached_property
    def awsEksMetadataDetails(self):  # pragma: no cover
        return AwsEksMetadataDetails.make_one(
            self.boto3_raw_data["awsEksMetadataDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDetails:
    boto3_raw_data: "type_defs.ResourceDetailsTypeDef" = dataclasses.field()

    @cached_property
    def awsEc2Instance(self):  # pragma: no cover
        return AwsEc2InstanceDetails.make_one(self.boto3_raw_data["awsEc2Instance"])

    @cached_property
    def awsEcrContainerImage(self):  # pragma: no cover
        return AwsEcrContainerImageDetails.make_one(
            self.boto3_raw_data["awsEcrContainerImage"]
        )

    @cached_property
    def awsLambdaFunction(self):  # pragma: no cover
        return AwsLambdaFunctionDetails.make_one(
            self.boto3_raw_data["awsLambdaFunction"]
        )

    @cached_property
    def codeRepository(self):  # pragma: no cover
        return CodeRepositoryDetails.make_one(self.boto3_raw_data["codeRepository"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendCisSessionTelemetryRequest:
    boto3_raw_data: "type_defs.SendCisSessionTelemetryRequestTypeDef" = (
        dataclasses.field()
    )

    scanJobId = field("scanJobId")
    sessionToken = field("sessionToken")

    @cached_property
    def messages(self):  # pragma: no cover
        return CisSessionMessage.make_many(self.boto3_raw_data["messages"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendCisSessionTelemetryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendCisSessionTelemetryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScanResultsAggregatedByChecksResponse:
    boto3_raw_data: "type_defs.ListCisScanResultsAggregatedByChecksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def checkAggregations(self):  # pragma: no cover
        return CisCheckAggregation.make_many(self.boto3_raw_data["checkAggregations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCisScanResultsAggregatedByChecksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCisScanResultsAggregatedByChecksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScanResultsAggregatedByTargetResourceResponse:
    boto3_raw_data: (
        "type_defs.ListCisScanResultsAggregatedByTargetResourceResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def targetResourceAggregations(self):  # pragma: no cover
        return CisTargetResourceAggregation.make_many(
            self.boto3_raw_data["targetResourceAggregations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCisScanResultsAggregatedByTargetResourceResponseTypeDef"
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
                "type_defs.ListCisScanResultsAggregatedByTargetResourceResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScansFilterCriteria:
    boto3_raw_data: "type_defs.ListCisScansFilterCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def scanNameFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["scanNameFilters"])

    @cached_property
    def targetResourceTagFilters(self):  # pragma: no cover
        return TagFilter.make_many(self.boto3_raw_data["targetResourceTagFilters"])

    @cached_property
    def targetResourceIdFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["targetResourceIdFilters"])

    @cached_property
    def scanStatusFilters(self):  # pragma: no cover
        return CisScanStatusFilter.make_many(self.boto3_raw_data["scanStatusFilters"])

    @cached_property
    def scanAtFilters(self):  # pragma: no cover
        return CisDateFilter.make_many(self.boto3_raw_data["scanAtFilters"])

    @cached_property
    def scanConfigurationArnFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(
            self.boto3_raw_data["scanConfigurationArnFilters"]
        )

    @cached_property
    def scanArnFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["scanArnFilters"])

    @cached_property
    def scheduledByFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["scheduledByFilters"])

    @cached_property
    def failedChecksFilters(self):  # pragma: no cover
        return CisNumberFilter.make_many(self.boto3_raw_data["failedChecksFilters"])

    @cached_property
    def targetAccountIdFilters(self):  # pragma: no cover
        return CisStringFilter.make_many(self.boto3_raw_data["targetAccountIdFilters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCisScansFilterCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCisScansFilterCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageFilterCriteria:
    boto3_raw_data: "type_defs.CoverageFilterCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def scanStatusCode(self):  # pragma: no cover
        return CoverageStringFilter.make_many(self.boto3_raw_data["scanStatusCode"])

    @cached_property
    def scanStatusReason(self):  # pragma: no cover
        return CoverageStringFilter.make_many(self.boto3_raw_data["scanStatusReason"])

    @cached_property
    def accountId(self):  # pragma: no cover
        return CoverageStringFilter.make_many(self.boto3_raw_data["accountId"])

    @cached_property
    def resourceId(self):  # pragma: no cover
        return CoverageStringFilter.make_many(self.boto3_raw_data["resourceId"])

    @cached_property
    def resourceType(self):  # pragma: no cover
        return CoverageStringFilter.make_many(self.boto3_raw_data["resourceType"])

    @cached_property
    def scanType(self):  # pragma: no cover
        return CoverageStringFilter.make_many(self.boto3_raw_data["scanType"])

    @cached_property
    def ecrRepositoryName(self):  # pragma: no cover
        return CoverageStringFilter.make_many(self.boto3_raw_data["ecrRepositoryName"])

    @cached_property
    def ecrImageTags(self):  # pragma: no cover
        return CoverageStringFilter.make_many(self.boto3_raw_data["ecrImageTags"])

    @cached_property
    def ec2InstanceTags(self):  # pragma: no cover
        return CoverageMapFilter.make_many(self.boto3_raw_data["ec2InstanceTags"])

    @cached_property
    def lambdaFunctionName(self):  # pragma: no cover
        return CoverageStringFilter.make_many(self.boto3_raw_data["lambdaFunctionName"])

    @cached_property
    def lambdaFunctionTags(self):  # pragma: no cover
        return CoverageMapFilter.make_many(self.boto3_raw_data["lambdaFunctionTags"])

    @cached_property
    def lambdaFunctionRuntime(self):  # pragma: no cover
        return CoverageStringFilter.make_many(
            self.boto3_raw_data["lambdaFunctionRuntime"]
        )

    @cached_property
    def lastScannedAt(self):  # pragma: no cover
        return CoverageDateFilter.make_many(self.boto3_raw_data["lastScannedAt"])

    @cached_property
    def scanMode(self):  # pragma: no cover
        return CoverageStringFilter.make_many(self.boto3_raw_data["scanMode"])

    @cached_property
    def imagePulledAt(self):  # pragma: no cover
        return CoverageDateFilter.make_many(self.boto3_raw_data["imagePulledAt"])

    @cached_property
    def ecrImageLastInUseAt(self):  # pragma: no cover
        return CoverageDateFilter.make_many(self.boto3_raw_data["ecrImageLastInUseAt"])

    @cached_property
    def ecrImageInUseCount(self):  # pragma: no cover
        return CoverageNumberFilter.make_many(self.boto3_raw_data["ecrImageInUseCount"])

    @cached_property
    def codeRepositoryProjectName(self):  # pragma: no cover
        return CoverageStringFilter.make_many(
            self.boto3_raw_data["codeRepositoryProjectName"]
        )

    @cached_property
    def codeRepositoryProviderType(self):  # pragma: no cover
        return CoverageStringFilter.make_many(
            self.boto3_raw_data["codeRepositoryProviderType"]
        )

    @cached_property
    def codeRepositoryProviderTypeVisibility(self):  # pragma: no cover
        return CoverageStringFilter.make_many(
            self.boto3_raw_data["codeRepositoryProviderTypeVisibility"]
        )

    @cached_property
    def lastScannedCommitId(self):  # pragma: no cover
        return CoverageStringFilter.make_many(
            self.boto3_raw_data["lastScannedCommitId"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CoverageFilterCriteriaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CoverageFilterCriteriaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCriteria:
    boto3_raw_data: "type_defs.FilterCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def findingArn(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["findingArn"])

    @cached_property
    def awsAccountId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["awsAccountId"])

    @cached_property
    def findingType(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["findingType"])

    @cached_property
    def severity(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["severity"])

    @cached_property
    def firstObservedAt(self):  # pragma: no cover
        return DateFilter.make_many(self.boto3_raw_data["firstObservedAt"])

    @cached_property
    def lastObservedAt(self):  # pragma: no cover
        return DateFilter.make_many(self.boto3_raw_data["lastObservedAt"])

    @cached_property
    def updatedAt(self):  # pragma: no cover
        return DateFilter.make_many(self.boto3_raw_data["updatedAt"])

    @cached_property
    def findingStatus(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["findingStatus"])

    @cached_property
    def title(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["title"])

    @cached_property
    def inspectorScore(self):  # pragma: no cover
        return NumberFilter.make_many(self.boto3_raw_data["inspectorScore"])

    @cached_property
    def resourceType(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["resourceType"])

    @cached_property
    def resourceId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["resourceId"])

    @cached_property
    def resourceTags(self):  # pragma: no cover
        return MapFilter.make_many(self.boto3_raw_data["resourceTags"])

    @cached_property
    def ec2InstanceImageId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ec2InstanceImageId"])

    @cached_property
    def ec2InstanceVpcId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ec2InstanceVpcId"])

    @cached_property
    def ec2InstanceSubnetId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ec2InstanceSubnetId"])

    @cached_property
    def ecrImagePushedAt(self):  # pragma: no cover
        return DateFilter.make_many(self.boto3_raw_data["ecrImagePushedAt"])

    @cached_property
    def ecrImageArchitecture(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ecrImageArchitecture"])

    @cached_property
    def ecrImageRegistry(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ecrImageRegistry"])

    @cached_property
    def ecrImageRepositoryName(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ecrImageRepositoryName"])

    @cached_property
    def ecrImageTags(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ecrImageTags"])

    @cached_property
    def ecrImageHash(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["ecrImageHash"])

    @cached_property
    def ecrImageLastInUseAt(self):  # pragma: no cover
        return DateFilter.make_many(self.boto3_raw_data["ecrImageLastInUseAt"])

    @cached_property
    def ecrImageInUseCount(self):  # pragma: no cover
        return NumberFilter.make_many(self.boto3_raw_data["ecrImageInUseCount"])

    @cached_property
    def portRange(self):  # pragma: no cover
        return PortRangeFilter.make_many(self.boto3_raw_data["portRange"])

    @cached_property
    def networkProtocol(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["networkProtocol"])

    @cached_property
    def componentId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["componentId"])

    @cached_property
    def componentType(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["componentType"])

    @cached_property
    def vulnerabilityId(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["vulnerabilityId"])

    @cached_property
    def vulnerabilitySource(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["vulnerabilitySource"])

    @cached_property
    def vendorSeverity(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["vendorSeverity"])

    @cached_property
    def vulnerablePackages(self):  # pragma: no cover
        return PackageFilter.make_many(self.boto3_raw_data["vulnerablePackages"])

    @cached_property
    def relatedVulnerabilities(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["relatedVulnerabilities"])

    @cached_property
    def fixAvailable(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["fixAvailable"])

    @cached_property
    def lambdaFunctionName(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["lambdaFunctionName"])

    @cached_property
    def lambdaFunctionLayers(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["lambdaFunctionLayers"])

    @cached_property
    def lambdaFunctionRuntime(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["lambdaFunctionRuntime"])

    @cached_property
    def lambdaFunctionLastModifiedAt(self):  # pragma: no cover
        return DateFilter.make_many(self.boto3_raw_data["lambdaFunctionLastModifiedAt"])

    @cached_property
    def lambdaFunctionExecutionRoleArn(self):  # pragma: no cover
        return StringFilter.make_many(
            self.boto3_raw_data["lambdaFunctionExecutionRoleArn"]
        )

    @cached_property
    def exploitAvailable(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["exploitAvailable"])

    @cached_property
    def codeVulnerabilityDetectorName(self):  # pragma: no cover
        return StringFilter.make_many(
            self.boto3_raw_data["codeVulnerabilityDetectorName"]
        )

    @cached_property
    def codeVulnerabilityDetectorTags(self):  # pragma: no cover
        return StringFilter.make_many(
            self.boto3_raw_data["codeVulnerabilityDetectorTags"]
        )

    @cached_property
    def codeVulnerabilityFilePath(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["codeVulnerabilityFilePath"])

    @cached_property
    def epssScore(self):  # pragma: no cover
        return NumberFilter.make_many(self.boto3_raw_data["epssScore"])

    @cached_property
    def codeRepositoryProjectName(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["codeRepositoryProjectName"])

    @cached_property
    def codeRepositoryProviderType(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["codeRepositoryProviderType"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScansResponse:
    boto3_raw_data: "type_defs.ListCisScansResponseTypeDef" = dataclasses.field()

    @cached_property
    def scans(self):  # pragma: no cover
        return CisScan.make_many(self.boto3_raw_data["scans"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCisScansResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCisScansResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCisScanResultDetailsRequestPaginate:
    boto3_raw_data: "type_defs.GetCisScanResultDetailsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    scanArn = field("scanArn")
    targetResourceId = field("targetResourceId")
    accountId = field("accountId")

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return CisScanResultDetailsFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCisScanResultDetailsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCisScanResultDetailsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCisScanResultDetailsRequest:
    boto3_raw_data: "type_defs.GetCisScanResultDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    scanArn = field("scanArn")
    targetResourceId = field("targetResourceId")
    accountId = field("accountId")

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return CisScanResultDetailsFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCisScanResultDetailsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCisScanResultDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScanResultsAggregatedByChecksRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListCisScanResultsAggregatedByChecksRequestPaginateTypeDef"
    ) = dataclasses.field()

    scanArn = field("scanArn")

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return CisScanResultsAggregatedByChecksFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCisScanResultsAggregatedByChecksRequestPaginateTypeDef"
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
                "type_defs.ListCisScanResultsAggregatedByChecksRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScanResultsAggregatedByChecksRequest:
    boto3_raw_data: "type_defs.ListCisScanResultsAggregatedByChecksRequestTypeDef" = (
        dataclasses.field()
    )

    scanArn = field("scanArn")

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return CisScanResultsAggregatedByChecksFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCisScanResultsAggregatedByChecksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCisScanResultsAggregatedByChecksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScanResultsAggregatedByTargetResourceRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListCisScanResultsAggregatedByTargetResourceRequestPaginateTypeDef"
    ) = dataclasses.field()

    scanArn = field("scanArn")

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return CisScanResultsAggregatedByTargetResourceFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCisScanResultsAggregatedByTargetResourceRequestPaginateTypeDef"
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
                "type_defs.ListCisScanResultsAggregatedByTargetResourceRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScanResultsAggregatedByTargetResourceRequest:
    boto3_raw_data: (
        "type_defs.ListCisScanResultsAggregatedByTargetResourceRequestTypeDef"
    ) = dataclasses.field()

    scanArn = field("scanArn")

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return CisScanResultsAggregatedByTargetResourceFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCisScanResultsAggregatedByTargetResourceRequestTypeDef"
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
                "type_defs.ListCisScanResultsAggregatedByTargetResourceRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScanConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListCisScanConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return ListCisScanConfigurationsFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCisScanConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCisScanConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScanConfigurationsRequest:
    boto3_raw_data: "type_defs.ListCisScanConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return ListCisScanConfigurationsFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCisScanConfigurationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCisScanConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodeSecurityScanConfigurationResponse:
    boto3_raw_data: "type_defs.GetCodeSecurityScanConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")
    name = field("name")

    @cached_property
    def configuration(self):  # pragma: no cover
        return CodeSecurityScanConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    level = field("level")

    @cached_property
    def scopeSettings(self):  # pragma: no cover
        return ScopeSettings.make_one(self.boto3_raw_data["scopeSettings"])

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCodeSecurityScanConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodeSecurityScanConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodeSecurityScanConfigurationsResponse:
    boto3_raw_data: "type_defs.ListCodeSecurityScanConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configurations(self):  # pragma: no cover
        return CodeSecurityScanConfigurationSummary.make_many(
            self.boto3_raw_data["configurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCodeSecurityScanConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodeSecurityScanConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCodeSnippetResponse:
    boto3_raw_data: "type_defs.BatchGetCodeSnippetResponseTypeDef" = dataclasses.field()

    @cached_property
    def codeSnippetResults(self):  # pragma: no cover
        return CodeSnippetResult.make_many(self.boto3_raw_data["codeSnippetResults"])

    @cached_property
    def errors(self):  # pragma: no cover
        return CodeSnippetError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetCodeSnippetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCodeSnippetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCodeSecurityIntegrationRequest:
    boto3_raw_data: "type_defs.CreateCodeSecurityIntegrationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    type = field("type")

    @cached_property
    def details(self):  # pragma: no cover
        return CreateIntegrationDetail.make_one(self.boto3_raw_data["details"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCodeSecurityIntegrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCodeSecurityIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InspectorScoreDetails:
    boto3_raw_data: "type_defs.InspectorScoreDetailsTypeDef" = dataclasses.field()

    @cached_property
    def adjustedCvss(self):  # pragma: no cover
        return CvssScoreDetails.make_one(self.boto3_raw_data["adjustedCvss"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InspectorScoreDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InspectorScoreDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleOutput:
    boto3_raw_data: "type_defs.ScheduleOutputTypeDef" = dataclasses.field()

    oneTime = field("oneTime")

    @cached_property
    def daily(self):  # pragma: no cover
        return DailySchedule.make_one(self.boto3_raw_data["daily"])

    @cached_property
    def weekly(self):  # pragma: no cover
        return WeeklyScheduleOutput.make_one(self.boto3_raw_data["weekly"])

    @cached_property
    def monthly(self):  # pragma: no cover
        return MonthlySchedule.make_one(self.boto3_raw_data["monthly"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Schedule:
    boto3_raw_data: "type_defs.ScheduleTypeDef" = dataclasses.field()

    oneTime = field("oneTime")

    @cached_property
    def daily(self):  # pragma: no cover
        return DailySchedule.make_one(self.boto3_raw_data["daily"])

    @cached_property
    def weekly(self):  # pragma: no cover
        return WeeklySchedule.make_one(self.boto3_raw_data["weekly"])

    @cached_property
    def monthly(self):  # pragma: no cover
        return MonthlySchedule.make_one(self.boto3_raw_data["monthly"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfigurationResponse:
    boto3_raw_data: "type_defs.GetConfigurationResponseTypeDef" = dataclasses.field()

    @cached_property
    def ecrConfiguration(self):  # pragma: no cover
        return EcrConfigurationState.make_one(self.boto3_raw_data["ecrConfiguration"])

    @cached_property
    def ec2Configuration(self):  # pragma: no cover
        return Ec2ConfigurationState.make_one(self.boto3_raw_data["ec2Configuration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConfigurationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetFindingDetailsResponse:
    boto3_raw_data: "type_defs.BatchGetFindingDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def findingDetails(self):  # pragma: no cover
        return FindingDetail.make_many(self.boto3_raw_data["findingDetails"])

    @cached_property
    def errors(self):  # pragma: no cover
        return FindingDetailsError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetFindingDetailsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFindingDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchVulnerabilitiesResponse:
    boto3_raw_data: "type_defs.SearchVulnerabilitiesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vulnerabilities(self):  # pragma: no cover
        return Vulnerability.make_many(self.boto3_raw_data["vulnerabilities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchVulnerabilitiesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchVulnerabilitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetFreeTrialInfoResponse:
    boto3_raw_data: "type_defs.BatchGetFreeTrialInfoResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accounts(self):  # pragma: no cover
        return FreeTrialAccountInfo.make_many(self.boto3_raw_data["accounts"])

    @cached_property
    def failedAccounts(self):  # pragma: no cover
        return FreeTrialInfoError.make_many(self.boto3_raw_data["failedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetFreeTrialInfoResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFreeTrialInfoResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkReachabilityDetails:
    boto3_raw_data: "type_defs.NetworkReachabilityDetailsTypeDef" = dataclasses.field()

    @cached_property
    def openPortRange(self):  # pragma: no cover
        return PortRange.make_one(self.boto3_raw_data["openPortRange"])

    protocol = field("protocol")

    @cached_property
    def networkPath(self):  # pragma: no cover
        return NetworkPath.make_one(self.boto3_raw_data["networkPath"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkReachabilityDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkReachabilityDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeRepositoryMetadata:
    boto3_raw_data: "type_defs.CodeRepositoryMetadataTypeDef" = dataclasses.field()

    projectName = field("projectName")
    providerType = field("providerType")
    providerTypeVisibility = field("providerTypeVisibility")
    integrationArn = field("integrationArn")
    lastScannedCommitId = field("lastScannedCommitId")

    @cached_property
    def scanConfiguration(self):  # pragma: no cover
        return ProjectCodeSecurityScanConfiguration.make_one(
            self.boto3_raw_data["scanConfiguration"]
        )

    @cached_property
    def onDemandScan(self):  # pragma: no cover
        return CodeRepositoryOnDemandScan.make_one(self.boto3_raw_data["onDemandScan"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeRepositoryMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeRepositoryMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSbomExportResponse:
    boto3_raw_data: "type_defs.GetSbomExportResponseTypeDef" = dataclasses.field()

    reportId = field("reportId")
    format = field("format")
    status = field("status")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["s3Destination"])

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return ResourceFilterCriteriaOutput.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSbomExportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSbomExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopCisSessionRequest:
    boto3_raw_data: "type_defs.StopCisSessionRequestTypeDef" = dataclasses.field()

    scanJobId = field("scanJobId")
    sessionToken = field("sessionToken")

    @cached_property
    def message(self):  # pragma: no cover
        return StopCisSessionMessage.make_one(self.boto3_raw_data["message"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopCisSessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopCisSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCodeSecurityIntegrationRequest:
    boto3_raw_data: "type_defs.UpdateCodeSecurityIntegrationRequestTypeDef" = (
        dataclasses.field()
    )

    integrationArn = field("integrationArn")

    @cached_property
    def details(self):  # pragma: no cover
        return UpdateIntegrationDetails.make_one(self.boto3_raw_data["details"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCodeSecurityIntegrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCodeSecurityIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsageTotalsResponse:
    boto3_raw_data: "type_defs.ListUsageTotalsResponseTypeDef" = dataclasses.field()

    @cached_property
    def totals(self):  # pragma: no cover
        return UsageTotal.make_many(self.boto3_raw_data["totals"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsageTotalsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsageTotalsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingAggregationsResponse:
    boto3_raw_data: "type_defs.ListFindingAggregationsResponseTypeDef" = (
        dataclasses.field()
    )

    aggregationType = field("aggregationType")

    @cached_property
    def responses(self):  # pragma: no cover
        return AggregationResponse.make_many(self.boto3_raw_data["responses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFindingAggregationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingAggregationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAccountStatusResponse:
    boto3_raw_data: "type_defs.BatchGetAccountStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accounts(self):  # pragma: no cover
        return AccountState.make_many(self.boto3_raw_data["accounts"])

    @cached_property
    def failedAccounts(self):  # pragma: no cover
        return FailedAccount.make_many(self.boto3_raw_data["failedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetAccountStatusResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAccountStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    arn = field("arn")
    ownerId = field("ownerId")
    name = field("name")

    @cached_property
    def criteria(self):  # pragma: no cover
        return FilterCriteriaOutput.make_one(self.boto3_raw_data["criteria"])

    action = field("action")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")
    reason = field("reason")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFindingsReportStatusResponse:
    boto3_raw_data: "type_defs.GetFindingsReportStatusResponseTypeDef" = (
        dataclasses.field()
    )

    reportId = field("reportId")
    status = field("status")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @cached_property
    def destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["destination"])

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return FilterCriteriaOutput.make_one(self.boto3_raw_data["filterCriteria"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetFindingsReportStatusResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFindingsReportStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterDetails:
    boto3_raw_data: "type_defs.ClusterDetailsTypeDef" = dataclasses.field()

    lastInUse = field("lastInUse")

    @cached_property
    def clusterMetadata(self):  # pragma: no cover
        return ClusterMetadata.make_one(self.boto3_raw_data["clusterMetadata"])

    runningUnitCount = field("runningUnitCount")
    stoppedUnitCount = field("stoppedUnitCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    type = field("type")
    id = field("id")
    partition = field("partition")
    region = field("region")
    tags = field("tags")

    @cached_property
    def details(self):  # pragma: no cover
        return ResourceDetails.make_one(self.boto3_raw_data["details"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScansRequestPaginate:
    boto3_raw_data: "type_defs.ListCisScansRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return ListCisScansFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    detailLevel = field("detailLevel")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCisScansRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCisScansRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScansRequest:
    boto3_raw_data: "type_defs.ListCisScansRequestTypeDef" = dataclasses.field()

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return ListCisScansFilterCriteria.make_one(
            self.boto3_raw_data["filterCriteria"]
        )

    detailLevel = field("detailLevel")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCisScansRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCisScansRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoverageRequestPaginate:
    boto3_raw_data: "type_defs.ListCoverageRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return CoverageFilterCriteria.make_one(self.boto3_raw_data["filterCriteria"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoverageRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoverageRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoverageRequest:
    boto3_raw_data: "type_defs.ListCoverageRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return CoverageFilterCriteria.make_one(self.boto3_raw_data["filterCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoverageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoverageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoverageStatisticsRequestPaginate:
    boto3_raw_data: "type_defs.ListCoverageStatisticsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return CoverageFilterCriteria.make_one(self.boto3_raw_data["filterCriteria"])

    groupBy = field("groupBy")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCoverageStatisticsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoverageStatisticsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoverageStatisticsRequest:
    boto3_raw_data: "type_defs.ListCoverageStatisticsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filterCriteria(self):  # pragma: no cover
        return CoverageFilterCriteria.make_one(self.boto3_raw_data["filterCriteria"])

    groupBy = field("groupBy")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCoverageStatisticsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoverageStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsEcrContainerAggregation:
    boto3_raw_data: "type_defs.AwsEcrContainerAggregationTypeDef" = dataclasses.field()

    @cached_property
    def resourceIds(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["resourceIds"])

    @cached_property
    def imageShas(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["imageShas"])

    @cached_property
    def repositories(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["repositories"])

    @cached_property
    def architectures(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["architectures"])

    @cached_property
    def imageTags(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["imageTags"])

    sortOrder = field("sortOrder")
    sortBy = field("sortBy")
    lastInUseAt = field("lastInUseAt")

    @cached_property
    def inUseCount(self):  # pragma: no cover
        return NumberFilter.make_many(self.boto3_raw_data["inUseCount"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsEcrContainerAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsEcrContainerAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCodeSecurityScanConfigurationRequest:
    boto3_raw_data: "type_defs.CreateCodeSecurityScanConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    level = field("level")
    configuration = field("configuration")

    @cached_property
    def scopeSettings(self):  # pragma: no cover
        return ScopeSettings.make_one(self.boto3_raw_data["scopeSettings"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCodeSecurityScanConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCodeSecurityScanConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCodeSecurityScanConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateCodeSecurityScanConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")
    configuration = field("configuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCodeSecurityScanConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCodeSecurityScanConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CisScanConfiguration:
    boto3_raw_data: "type_defs.CisScanConfigurationTypeDef" = dataclasses.field()

    scanConfigurationArn = field("scanConfigurationArn")
    ownerId = field("ownerId")
    scanName = field("scanName")
    securityLevel = field("securityLevel")

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleOutput.make_one(self.boto3_raw_data["schedule"])

    @cached_property
    def targets(self):  # pragma: no cover
        return CisTargets.make_one(self.boto3_raw_data["targets"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CisScanConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CisScanConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceScanMetadata:
    boto3_raw_data: "type_defs.ResourceScanMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ecrRepository(self):  # pragma: no cover
        return EcrRepositoryMetadata.make_one(self.boto3_raw_data["ecrRepository"])

    @cached_property
    def ecrImage(self):  # pragma: no cover
        return EcrContainerImageMetadata.make_one(self.boto3_raw_data["ecrImage"])

    @cached_property
    def ec2(self):  # pragma: no cover
        return Ec2Metadata.make_one(self.boto3_raw_data["ec2"])

    @cached_property
    def lambdaFunction(self):  # pragma: no cover
        return LambdaFunctionMetadata.make_one(self.boto3_raw_data["lambdaFunction"])

    @cached_property
    def codeRepository(self):  # pragma: no cover
        return CodeRepositoryMetadata.make_one(self.boto3_raw_data["codeRepository"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceScanMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceScanMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSbomExportRequest:
    boto3_raw_data: "type_defs.CreateSbomExportRequestTypeDef" = dataclasses.field()

    reportFormat = field("reportFormat")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["s3Destination"])

    resourceFilterCriteria = field("resourceFilterCriteria")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSbomExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSbomExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFiltersResponse:
    boto3_raw_data: "type_defs.ListFiltersResponseTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFiltersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFiltersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterInformation:
    boto3_raw_data: "type_defs.ClusterInformationTypeDef" = dataclasses.field()

    clusterArn = field("clusterArn")

    @cached_property
    def clusterDetails(self):  # pragma: no cover
        return ClusterDetails.make_many(self.boto3_raw_data["clusterDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterInformationTypeDef"]
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

    findingArn = field("findingArn")
    awsAccountId = field("awsAccountId")
    type = field("type")
    description = field("description")

    @cached_property
    def remediation(self):  # pragma: no cover
        return Remediation.make_one(self.boto3_raw_data["remediation"])

    severity = field("severity")
    firstObservedAt = field("firstObservedAt")
    lastObservedAt = field("lastObservedAt")
    status = field("status")

    @cached_property
    def resources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["resources"])

    title = field("title")
    updatedAt = field("updatedAt")
    inspectorScore = field("inspectorScore")

    @cached_property
    def inspectorScoreDetails(self):  # pragma: no cover
        return InspectorScoreDetails.make_one(
            self.boto3_raw_data["inspectorScoreDetails"]
        )

    @cached_property
    def networkReachabilityDetails(self):  # pragma: no cover
        return NetworkReachabilityDetails.make_one(
            self.boto3_raw_data["networkReachabilityDetails"]
        )

    @cached_property
    def packageVulnerabilityDetails(self):  # pragma: no cover
        return PackageVulnerabilityDetails.make_one(
            self.boto3_raw_data["packageVulnerabilityDetails"]
        )

    fixAvailable = field("fixAvailable")
    exploitAvailable = field("exploitAvailable")

    @cached_property
    def exploitabilityDetails(self):  # pragma: no cover
        return ExploitabilityDetails.make_one(
            self.boto3_raw_data["exploitabilityDetails"]
        )

    @cached_property
    def codeVulnerabilityDetails(self):  # pragma: no cover
        return CodeVulnerabilityDetails.make_one(
            self.boto3_raw_data["codeVulnerabilityDetails"]
        )

    @cached_property
    def epss(self):  # pragma: no cover
        return EpssDetails.make_one(self.boto3_raw_data["epss"])

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
class AggregationRequest:
    boto3_raw_data: "type_defs.AggregationRequestTypeDef" = dataclasses.field()

    @cached_property
    def accountAggregation(self):  # pragma: no cover
        return AccountAggregation.make_one(self.boto3_raw_data["accountAggregation"])

    @cached_property
    def amiAggregation(self):  # pragma: no cover
        return AmiAggregation.make_one(self.boto3_raw_data["amiAggregation"])

    @cached_property
    def awsEcrContainerAggregation(self):  # pragma: no cover
        return AwsEcrContainerAggregation.make_one(
            self.boto3_raw_data["awsEcrContainerAggregation"]
        )

    @cached_property
    def ec2InstanceAggregation(self):  # pragma: no cover
        return Ec2InstanceAggregation.make_one(
            self.boto3_raw_data["ec2InstanceAggregation"]
        )

    @cached_property
    def findingTypeAggregation(self):  # pragma: no cover
        return FindingTypeAggregation.make_one(
            self.boto3_raw_data["findingTypeAggregation"]
        )

    @cached_property
    def imageLayerAggregation(self):  # pragma: no cover
        return ImageLayerAggregation.make_one(
            self.boto3_raw_data["imageLayerAggregation"]
        )

    @cached_property
    def packageAggregation(self):  # pragma: no cover
        return PackageAggregation.make_one(self.boto3_raw_data["packageAggregation"])

    @cached_property
    def repositoryAggregation(self):  # pragma: no cover
        return RepositoryAggregation.make_one(
            self.boto3_raw_data["repositoryAggregation"]
        )

    @cached_property
    def titleAggregation(self):  # pragma: no cover
        return TitleAggregation.make_one(self.boto3_raw_data["titleAggregation"])

    @cached_property
    def lambdaLayerAggregation(self):  # pragma: no cover
        return LambdaLayerAggregation.make_one(
            self.boto3_raw_data["lambdaLayerAggregation"]
        )

    @cached_property
    def lambdaFunctionAggregation(self):  # pragma: no cover
        return LambdaFunctionAggregation.make_one(
            self.boto3_raw_data["lambdaFunctionAggregation"]
        )

    @cached_property
    def codeRepositoryAggregation(self):  # pragma: no cover
        return CodeRepositoryAggregation.make_one(
            self.boto3_raw_data["codeRepositoryAggregation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFilterRequest:
    boto3_raw_data: "type_defs.CreateFilterRequestTypeDef" = dataclasses.field()

    action = field("action")
    filterCriteria = field("filterCriteria")
    name = field("name")
    description = field("description")
    tags = field("tags")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFindingsReportRequest:
    boto3_raw_data: "type_defs.CreateFindingsReportRequestTypeDef" = dataclasses.field()

    reportFormat = field("reportFormat")

    @cached_property
    def s3Destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["s3Destination"])

    filterCriteria = field("filterCriteria")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFindingsReportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFindingsReportRequestTypeDef"]
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

    filterCriteria = field("filterCriteria")

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

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    filterCriteria = field("filterCriteria")

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
class UpdateFilterRequest:
    boto3_raw_data: "type_defs.UpdateFilterRequestTypeDef" = dataclasses.field()

    filterArn = field("filterArn")
    action = field("action")
    description = field("description")
    filterCriteria = field("filterCriteria")
    name = field("name")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCisScanConfigurationsResponse:
    boto3_raw_data: "type_defs.ListCisScanConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def scanConfigurations(self):  # pragma: no cover
        return CisScanConfiguration.make_many(self.boto3_raw_data["scanConfigurations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCisScanConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCisScanConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCisScanConfigurationRequest:
    boto3_raw_data: "type_defs.CreateCisScanConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    scanName = field("scanName")
    securityLevel = field("securityLevel")
    schedule = field("schedule")

    @cached_property
    def targets(self):  # pragma: no cover
        return CreateCisTargets.make_one(self.boto3_raw_data["targets"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCisScanConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCisScanConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCisScanConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateCisScanConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    scanConfigurationArn = field("scanConfigurationArn")
    scanName = field("scanName")
    securityLevel = field("securityLevel")
    schedule = field("schedule")

    @cached_property
    def targets(self):  # pragma: no cover
        return UpdateCisTargets.make_one(self.boto3_raw_data["targets"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCisScanConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCisScanConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoveredResource:
    boto3_raw_data: "type_defs.CoveredResourceTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resourceId = field("resourceId")
    accountId = field("accountId")
    scanType = field("scanType")

    @cached_property
    def scanStatus(self):  # pragma: no cover
        return ScanStatus.make_one(self.boto3_raw_data["scanStatus"])

    @cached_property
    def resourceMetadata(self):  # pragma: no cover
        return ResourceScanMetadata.make_one(self.boto3_raw_data["resourceMetadata"])

    lastScannedAt = field("lastScannedAt")
    scanMode = field("scanMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoveredResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoveredResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClustersForImageResponse:
    boto3_raw_data: "type_defs.GetClustersForImageResponseTypeDef" = dataclasses.field()

    @cached_property
    def cluster(self):  # pragma: no cover
        return ClusterInformation.make_many(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetClustersForImageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClustersForImageResponseTypeDef"]
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

    @cached_property
    def findings(self):  # pragma: no cover
        return Finding.make_many(self.boto3_raw_data["findings"])

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
class ListFindingAggregationsRequestPaginate:
    boto3_raw_data: "type_defs.ListFindingAggregationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    aggregationType = field("aggregationType")

    @cached_property
    def accountIds(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["accountIds"])

    @cached_property
    def aggregationRequest(self):  # pragma: no cover
        return AggregationRequest.make_one(self.boto3_raw_data["aggregationRequest"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFindingAggregationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingAggregationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFindingAggregationsRequest:
    boto3_raw_data: "type_defs.ListFindingAggregationsRequestTypeDef" = (
        dataclasses.field()
    )

    aggregationType = field("aggregationType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @cached_property
    def accountIds(self):  # pragma: no cover
        return StringFilter.make_many(self.boto3_raw_data["accountIds"])

    @cached_property
    def aggregationRequest(self):  # pragma: no cover
        return AggregationRequest.make_one(self.boto3_raw_data["aggregationRequest"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFindingAggregationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFindingAggregationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCoverageResponse:
    boto3_raw_data: "type_defs.ListCoverageResponseTypeDef" = dataclasses.field()

    @cached_property
    def coveredResources(self):  # pragma: no cover
        return CoveredResource.make_many(self.boto3_raw_data["coveredResources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCoverageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCoverageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
