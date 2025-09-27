# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kafka import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AmazonMskCluster:
    boto3_raw_data: "type_defs.AmazonMskClusterTypeDef" = dataclasses.field()

    MskClusterArn = field("MskClusterArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AmazonMskClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmazonMskClusterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateScramSecretRequest:
    boto3_raw_data: "type_defs.BatchAssociateScramSecretRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")
    SecretArnList = field("SecretArnList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchAssociateScramSecretRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateScramSecretRequestTypeDef"]
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
class UnprocessedScramSecret:
    boto3_raw_data: "type_defs.UnprocessedScramSecretTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")
    SecretArn = field("SecretArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedScramSecretTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedScramSecretTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateScramSecretRequest:
    boto3_raw_data: "type_defs.BatchDisassociateScramSecretRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")
    SecretArnList = field("SecretArnList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateScramSecretRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisassociateScramSecretRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrokerCountUpdateInfo:
    boto3_raw_data: "type_defs.BrokerCountUpdateInfoTypeDef" = dataclasses.field()

    CreatedBrokerIds = field("CreatedBrokerIds")
    DeletedBrokerIds = field("DeletedBrokerIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BrokerCountUpdateInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrokerCountUpdateInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedThroughput:
    boto3_raw_data: "type_defs.ProvisionedThroughputTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    VolumeThroughput = field("VolumeThroughput")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedThroughputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedThroughputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogs:
    boto3_raw_data: "type_defs.CloudWatchLogsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    LogGroup = field("LogGroup")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CloudWatchLogsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Firehose:
    boto3_raw_data: "type_defs.FirehoseTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    DeliveryStream = field("DeliveryStream")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FirehoseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FirehoseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3:
    boto3_raw_data: "type_defs.S3TypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Bucket = field("Bucket")
    Prefix = field("Prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrokerSoftwareInfo:
    boto3_raw_data: "type_defs.BrokerSoftwareInfoTypeDef" = dataclasses.field()

    ConfigurationArn = field("ConfigurationArn")
    ConfigurationRevision = field("ConfigurationRevision")
    KafkaVersion = field("KafkaVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BrokerSoftwareInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrokerSoftwareInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsOutput:
    boto3_raw_data: "type_defs.TlsOutputTypeDef" = dataclasses.field()

    CertificateAuthorityArnList = field("CertificateAuthorityArnList")
    Enabled = field("Enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TlsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TlsOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Unauthenticated:
    boto3_raw_data: "type_defs.UnauthenticatedTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UnauthenticatedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UnauthenticatedTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientVpcConnection:
    boto3_raw_data: "type_defs.ClientVpcConnectionTypeDef" = dataclasses.field()

    VpcConnectionArn = field("VpcConnectionArn")
    Authentication = field("Authentication")
    CreationTime = field("CreationTime")
    State = field("State")
    Owner = field("Owner")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientVpcConnectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientVpcConnectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateInfo:
    boto3_raw_data: "type_defs.StateInfoTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StateInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StateInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorInfo:
    boto3_raw_data: "type_defs.ErrorInfoTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorString = field("ErrorString")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterOperationStepInfo:
    boto3_raw_data: "type_defs.ClusterOperationStepInfoTypeDef" = dataclasses.field()

    StepStatus = field("StepStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterOperationStepInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterOperationStepInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterOperationV2Summary:
    boto3_raw_data: "type_defs.ClusterOperationV2SummaryTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterType = field("ClusterType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    OperationArn = field("OperationArn")
    OperationState = field("OperationState")
    OperationType = field("OperationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterOperationV2SummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterOperationV2SummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompatibleKafkaVersion:
    boto3_raw_data: "type_defs.CompatibleKafkaVersionTypeDef" = dataclasses.field()

    SourceVersion = field("SourceVersion")
    TargetVersions = field("TargetVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompatibleKafkaVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompatibleKafkaVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationInfo:
    boto3_raw_data: "type_defs.ConfigurationInfoTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Revision = field("Revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationRevision:
    boto3_raw_data: "type_defs.ConfigurationRevisionTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")
    Revision = field("Revision")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationRevisionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationRevisionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicAccess:
    boto3_raw_data: "type_defs.PublicAccessTypeDef" = dataclasses.field()

    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublicAccessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PublicAccessTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumerGroupReplicationOutput:
    boto3_raw_data: "type_defs.ConsumerGroupReplicationOutputTypeDef" = (
        dataclasses.field()
    )

    ConsumerGroupsToReplicate = field("ConsumerGroupsToReplicate")
    ConsumerGroupsToExclude = field("ConsumerGroupsToExclude")
    DetectAndCopyNewConsumerGroups = field("DetectAndCopyNewConsumerGroups")
    SynchroniseConsumerGroupOffsets = field("SynchroniseConsumerGroupOffsets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConsumerGroupReplicationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsumerGroupReplicationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumerGroupReplication:
    boto3_raw_data: "type_defs.ConsumerGroupReplicationTypeDef" = dataclasses.field()

    ConsumerGroupsToReplicate = field("ConsumerGroupsToReplicate")
    ConsumerGroupsToExclude = field("ConsumerGroupsToExclude")
    DetectAndCopyNewConsumerGroups = field("DetectAndCopyNewConsumerGroups")
    SynchroniseConsumerGroupOffsets = field("SynchroniseConsumerGroupOffsets")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsumerGroupReplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsumerGroupReplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsumerGroupReplicationUpdate:
    boto3_raw_data: "type_defs.ConsumerGroupReplicationUpdateTypeDef" = (
        dataclasses.field()
    )

    ConsumerGroupsToExclude = field("ConsumerGroupsToExclude")
    ConsumerGroupsToReplicate = field("ConsumerGroupsToReplicate")
    DetectAndCopyNewConsumerGroups = field("DetectAndCopyNewConsumerGroups")
    SynchroniseConsumerGroupOffsets = field("SynchroniseConsumerGroupOffsets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConsumerGroupReplicationUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsumerGroupReplicationUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControllerNodeInfo:
    boto3_raw_data: "type_defs.ControllerNodeInfoTypeDef" = dataclasses.field()

    Endpoints = field("Endpoints")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ControllerNodeInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControllerNodeInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcConnectionRequest:
    boto3_raw_data: "type_defs.CreateVpcConnectionRequestTypeDef" = dataclasses.field()

    TargetClusterArn = field("TargetClusterArn")
    Authentication = field("Authentication")
    VpcId = field("VpcId")
    ClientSubnets = field("ClientSubnets")
    SecurityGroups = field("SecurityGroups")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterPolicyRequest:
    boto3_raw_data: "type_defs.DeleteClusterPolicyRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterRequest:
    boto3_raw_data: "type_defs.DeleteClusterRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    CurrentVersion = field("CurrentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteConfigurationRequestTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicatorRequest:
    boto3_raw_data: "type_defs.DeleteReplicatorRequestTypeDef" = dataclasses.field()

    ReplicatorArn = field("ReplicatorArn")
    CurrentVersion = field("CurrentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReplicatorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcConnectionRequest:
    boto3_raw_data: "type_defs.DeleteVpcConnectionRequestTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterOperationRequest:
    boto3_raw_data: "type_defs.DescribeClusterOperationRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterOperationArn = field("ClusterOperationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClusterOperationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterOperationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterOperationV2Request:
    boto3_raw_data: "type_defs.DescribeClusterOperationV2RequestTypeDef" = (
        dataclasses.field()
    )

    ClusterOperationArn = field("ClusterOperationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterOperationV2RequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterOperationV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterRequest:
    boto3_raw_data: "type_defs.DescribeClusterRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterV2Request:
    boto3_raw_data: "type_defs.DescribeClusterV2RequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationRevisionRequest:
    boto3_raw_data: "type_defs.DescribeConfigurationRevisionRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Revision = field("Revision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationRevisionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationRevisionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicatorRequest:
    boto3_raw_data: "type_defs.DescribeReplicatorRequestTypeDef" = dataclasses.field()

    ReplicatorArn = field("ReplicatorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReplicatorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationStateInfo:
    boto3_raw_data: "type_defs.ReplicationStateInfoTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationStateInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationStateInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcConnectionRequest:
    boto3_raw_data: "type_defs.DescribeVpcConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeVpcConnectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionAtRest:
    boto3_raw_data: "type_defs.EncryptionAtRestTypeDef" = dataclasses.field()

    DataVolumeKMSKeyId = field("DataVolumeKMSKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionAtRestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionAtRestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionInTransit:
    boto3_raw_data: "type_defs.EncryptionInTransitTypeDef" = dataclasses.field()

    ClientBroker = field("ClientBroker")
    InCluster = field("InCluster")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionInTransitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionInTransitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBootstrapBrokersRequest:
    boto3_raw_data: "type_defs.GetBootstrapBrokersRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBootstrapBrokersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBootstrapBrokersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClusterPolicyRequest:
    boto3_raw_data: "type_defs.GetClusterPolicyRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetClusterPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClusterPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCompatibleKafkaVersionsRequest:
    boto3_raw_data: "type_defs.GetCompatibleKafkaVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCompatibleKafkaVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCompatibleKafkaVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Iam:
    boto3_raw_data: "type_defs.IamTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IamTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JmxExporterInfo:
    boto3_raw_data: "type_defs.JmxExporterInfoTypeDef" = dataclasses.field()

    EnabledInBroker = field("EnabledInBroker")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JmxExporterInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JmxExporterInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JmxExporter:
    boto3_raw_data: "type_defs.JmxExporterTypeDef" = dataclasses.field()

    EnabledInBroker = field("EnabledInBroker")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JmxExporterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JmxExporterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaClusterClientVpcConfigOutput:
    boto3_raw_data: "type_defs.KafkaClusterClientVpcConfigOutputTypeDef" = (
        dataclasses.field()
    )

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KafkaClusterClientVpcConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaClusterClientVpcConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaClusterClientVpcConfig:
    boto3_raw_data: "type_defs.KafkaClusterClientVpcConfigTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KafkaClusterClientVpcConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaClusterClientVpcConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaVersion:
    boto3_raw_data: "type_defs.KafkaVersionTypeDef" = dataclasses.field()

    Version = field("Version")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KafkaVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KafkaVersionTypeDef"]],
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
class ListClientVpcConnectionsRequest:
    boto3_raw_data: "type_defs.ListClientVpcConnectionsRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListClientVpcConnectionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClientVpcConnectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClusterOperationsRequest:
    boto3_raw_data: "type_defs.ListClusterOperationsRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClusterOperationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClusterOperationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClusterOperationsV2Request:
    boto3_raw_data: "type_defs.ListClusterOperationsV2RequestTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListClusterOperationsV2RequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClusterOperationsV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersRequest:
    boto3_raw_data: "type_defs.ListClustersRequestTypeDef" = dataclasses.field()

    ClusterNameFilter = field("ClusterNameFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersV2Request:
    boto3_raw_data: "type_defs.ListClustersV2RequestTypeDef" = dataclasses.field()

    ClusterNameFilter = field("ClusterNameFilter")
    ClusterTypeFilter = field("ClusterTypeFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationRevisionsRequest:
    boto3_raw_data: "type_defs.ListConfigurationRevisionsRequestTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfigurationRevisionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationRevisionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationsRequest:
    boto3_raw_data: "type_defs.ListConfigurationsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConfigurationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKafkaVersionsRequest:
    boto3_raw_data: "type_defs.ListKafkaVersionsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKafkaVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKafkaVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesRequest:
    boto3_raw_data: "type_defs.ListNodesRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListNodesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReplicatorsRequest:
    boto3_raw_data: "type_defs.ListReplicatorsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ReplicatorNameFilter = field("ReplicatorNameFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReplicatorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReplicatorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScramSecretsRequest:
    boto3_raw_data: "type_defs.ListScramSecretsRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScramSecretsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScramSecretsRequestTypeDef"]
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
class ListVpcConnectionsRequest:
    boto3_raw_data: "type_defs.ListVpcConnectionsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVpcConnectionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcConnectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConnection:
    boto3_raw_data: "type_defs.VpcConnectionTypeDef" = dataclasses.field()

    VpcConnectionArn = field("VpcConnectionArn")
    TargetClusterArn = field("TargetClusterArn")
    CreationTime = field("CreationTime")
    Authentication = field("Authentication")
    VpcId = field("VpcId")
    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConnectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeExporterInfo:
    boto3_raw_data: "type_defs.NodeExporterInfoTypeDef" = dataclasses.field()

    EnabledInBroker = field("EnabledInBroker")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeExporterInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeExporterInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeExporter:
    boto3_raw_data: "type_defs.NodeExporterTypeDef" = dataclasses.field()

    EnabledInBroker = field("EnabledInBroker")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeExporterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeExporterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZookeeperNodeInfo:
    boto3_raw_data: "type_defs.ZookeeperNodeInfoTypeDef" = dataclasses.field()

    AttachedENIId = field("AttachedENIId")
    ClientVpcIpAddress = field("ClientVpcIpAddress")
    Endpoints = field("Endpoints")
    ZookeeperId = field("ZookeeperId")
    ZookeeperVersion = field("ZookeeperVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ZookeeperNodeInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZookeeperNodeInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutClusterPolicyRequest:
    boto3_raw_data: "type_defs.PutClusterPolicyRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    Policy = field("Policy")
    CurrentVersion = field("CurrentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutClusterPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutClusterPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootBrokerRequest:
    boto3_raw_data: "type_defs.RebootBrokerRequestTypeDef" = dataclasses.field()

    BrokerIds = field("BrokerIds")
    ClusterArn = field("ClusterArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootBrokerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootBrokerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectClientVpcConnectionRequest:
    boto3_raw_data: "type_defs.RejectClientVpcConnectionRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")
    VpcConnectionArn = field("VpcConnectionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RejectClientVpcConnectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectClientVpcConnectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationInfoSummary:
    boto3_raw_data: "type_defs.ReplicationInfoSummaryTypeDef" = dataclasses.field()

    SourceKafkaClusterAlias = field("SourceKafkaClusterAlias")
    TargetKafkaClusterAlias = field("TargetKafkaClusterAlias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationInfoSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationInfoSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationStartingPosition:
    boto3_raw_data: "type_defs.ReplicationStartingPositionTypeDef" = dataclasses.field()

    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationStartingPositionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationStartingPositionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTopicNameConfiguration:
    boto3_raw_data: "type_defs.ReplicationTopicNameConfigurationTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicationTopicNameConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationTopicNameConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scram:
    boto3_raw_data: "type_defs.ScramTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScramTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScramTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigOutput:
    boto3_raw_data: "type_defs.VpcConfigOutputTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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
class Tls:
    boto3_raw_data: "type_defs.TlsTypeDef" = dataclasses.field()

    CertificateAuthorityArnList = field("CertificateAuthorityArnList")
    Enabled = field("Enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TlsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TlsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicReplicationUpdate:
    boto3_raw_data: "type_defs.TopicReplicationUpdateTypeDef" = dataclasses.field()

    CopyAccessControlListsForTopics = field("CopyAccessControlListsForTopics")
    CopyTopicConfigurations = field("CopyTopicConfigurations")
    DetectAndCopyNewTopics = field("DetectAndCopyNewTopics")
    TopicsToExclude = field("TopicsToExclude")
    TopicsToReplicate = field("TopicsToReplicate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TopicReplicationUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicReplicationUpdateTypeDef"]
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
class UpdateBrokerCountRequest:
    boto3_raw_data: "type_defs.UpdateBrokerCountRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    CurrentVersion = field("CurrentVersion")
    TargetNumberOfBrokerNodes = field("TargetNumberOfBrokerNodes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBrokerCountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrokerCountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBrokerTypeRequest:
    boto3_raw_data: "type_defs.UpdateBrokerTypeRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    CurrentVersion = field("CurrentVersion")
    TargetInstanceType = field("TargetInstanceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBrokerTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrokerTypeRequestTypeDef"]
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

    Type = field("Type")
    PrincipalId = field("PrincipalId")

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
class VpcConfig:
    boto3_raw_data: "type_defs.VpcConfigTypeDef" = dataclasses.field()

    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConnectivityTls:
    boto3_raw_data: "type_defs.VpcConnectivityTlsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConnectivityTlsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConnectivityTlsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConnectivityIam:
    boto3_raw_data: "type_defs.VpcConnectivityIamTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConnectivityIamTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConnectivityIamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConnectivityScram:
    boto3_raw_data: "type_defs.VpcConnectivityScramTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConnectivityScramTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConnectivityScramTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaClusterSummary:
    boto3_raw_data: "type_defs.KafkaClusterSummaryTypeDef" = dataclasses.field()

    @cached_property
    def AmazonMskCluster(self):  # pragma: no cover
        return AmazonMskCluster.make_one(self.boto3_raw_data["AmazonMskCluster"])

    KafkaClusterAlias = field("KafkaClusterAlias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KafkaClusterSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaClusterSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterResponse:
    boto3_raw_data: "type_defs.CreateClusterResponseTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterName = field("ClusterName")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterV2Response:
    boto3_raw_data: "type_defs.CreateClusterV2ResponseTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterName = field("ClusterName")
    State = field("State")
    ClusterType = field("ClusterType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterV2ResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicatorResponse:
    boto3_raw_data: "type_defs.CreateReplicatorResponseTypeDef" = dataclasses.field()

    ReplicatorArn = field("ReplicatorArn")
    ReplicatorName = field("ReplicatorName")
    ReplicatorState = field("ReplicatorState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReplicatorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicatorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcConnectionResponse:
    boto3_raw_data: "type_defs.CreateVpcConnectionResponseTypeDef" = dataclasses.field()

    VpcConnectionArn = field("VpcConnectionArn")
    State = field("State")
    Authentication = field("Authentication")
    VpcId = field("VpcId")
    ClientSubnets = field("ClientSubnets")
    SecurityGroups = field("SecurityGroups")
    CreationTime = field("CreationTime")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterResponse:
    boto3_raw_data: "type_defs.DeleteClusterResponseTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteConfigurationResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConfigurationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicatorResponse:
    boto3_raw_data: "type_defs.DeleteReplicatorResponseTypeDef" = dataclasses.field()

    ReplicatorArn = field("ReplicatorArn")
    ReplicatorState = field("ReplicatorState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReplicatorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicatorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcConnectionResponse:
    boto3_raw_data: "type_defs.DeleteVpcConnectionResponseTypeDef" = dataclasses.field()

    VpcConnectionArn = field("VpcConnectionArn")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationRevisionResponse:
    boto3_raw_data: "type_defs.DescribeConfigurationRevisionResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    Description = field("Description")
    Revision = field("Revision")
    ServerProperties = field("ServerProperties")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationRevisionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationRevisionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVpcConnectionResponse:
    boto3_raw_data: "type_defs.DescribeVpcConnectionResponseTypeDef" = (
        dataclasses.field()
    )

    VpcConnectionArn = field("VpcConnectionArn")
    TargetClusterArn = field("TargetClusterArn")
    State = field("State")
    Authentication = field("Authentication")
    VpcId = field("VpcId")
    Subnets = field("Subnets")
    SecurityGroups = field("SecurityGroups")
    CreationTime = field("CreationTime")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeVpcConnectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVpcConnectionResponseTypeDef"]
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
class GetBootstrapBrokersResponse:
    boto3_raw_data: "type_defs.GetBootstrapBrokersResponseTypeDef" = dataclasses.field()

    BootstrapBrokerString = field("BootstrapBrokerString")
    BootstrapBrokerStringTls = field("BootstrapBrokerStringTls")
    BootstrapBrokerStringSaslScram = field("BootstrapBrokerStringSaslScram")
    BootstrapBrokerStringSaslIam = field("BootstrapBrokerStringSaslIam")
    BootstrapBrokerStringPublicTls = field("BootstrapBrokerStringPublicTls")
    BootstrapBrokerStringPublicSaslScram = field("BootstrapBrokerStringPublicSaslScram")
    BootstrapBrokerStringPublicSaslIam = field("BootstrapBrokerStringPublicSaslIam")
    BootstrapBrokerStringVpcConnectivityTls = field(
        "BootstrapBrokerStringVpcConnectivityTls"
    )
    BootstrapBrokerStringVpcConnectivitySaslScram = field(
        "BootstrapBrokerStringVpcConnectivitySaslScram"
    )
    BootstrapBrokerStringVpcConnectivitySaslIam = field(
        "BootstrapBrokerStringVpcConnectivitySaslIam"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBootstrapBrokersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBootstrapBrokersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetClusterPolicyResponse:
    boto3_raw_data: "type_defs.GetClusterPolicyResponseTypeDef" = dataclasses.field()

    CurrentVersion = field("CurrentVersion")
    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetClusterPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetClusterPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScramSecretsResponse:
    boto3_raw_data: "type_defs.ListScramSecretsResponseTypeDef" = dataclasses.field()

    SecretArnList = field("SecretArnList")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScramSecretsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScramSecretsResponseTypeDef"]
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

    Tags = field("Tags")

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
class PutClusterPolicyResponse:
    boto3_raw_data: "type_defs.PutClusterPolicyResponseTypeDef" = dataclasses.field()

    CurrentVersion = field("CurrentVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutClusterPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutClusterPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootBrokerResponse:
    boto3_raw_data: "type_defs.RebootBrokerResponseTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterOperationArn = field("ClusterOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootBrokerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootBrokerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBrokerCountResponse:
    boto3_raw_data: "type_defs.UpdateBrokerCountResponseTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterOperationArn = field("ClusterOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBrokerCountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrokerCountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBrokerStorageResponse:
    boto3_raw_data: "type_defs.UpdateBrokerStorageResponseTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterOperationArn = field("ClusterOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBrokerStorageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrokerStorageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBrokerTypeResponse:
    boto3_raw_data: "type_defs.UpdateBrokerTypeResponseTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterOperationArn = field("ClusterOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBrokerTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrokerTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateClusterConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")
    ClusterOperationArn = field("ClusterOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateClusterConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterKafkaVersionResponse:
    boto3_raw_data: "type_defs.UpdateClusterKafkaVersionResponseTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")
    ClusterOperationArn = field("ClusterOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateClusterKafkaVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterKafkaVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectivityResponse:
    boto3_raw_data: "type_defs.UpdateConnectivityResponseTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterOperationArn = field("ClusterOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectivityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectivityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMonitoringResponse:
    boto3_raw_data: "type_defs.UpdateMonitoringResponseTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterOperationArn = field("ClusterOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMonitoringResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMonitoringResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReplicationInfoResponse:
    boto3_raw_data: "type_defs.UpdateReplicationInfoResponseTypeDef" = (
        dataclasses.field()
    )

    ReplicatorArn = field("ReplicatorArn")
    ReplicatorState = field("ReplicatorState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateReplicationInfoResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReplicationInfoResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSecurityResponse:
    boto3_raw_data: "type_defs.UpdateSecurityResponseTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterOperationArn = field("ClusterOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSecurityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSecurityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStorageResponse:
    boto3_raw_data: "type_defs.UpdateStorageResponseTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterOperationArn = field("ClusterOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStorageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStorageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateScramSecretResponse:
    boto3_raw_data: "type_defs.BatchAssociateScramSecretResponseTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")

    @cached_property
    def UnprocessedScramSecrets(self):  # pragma: no cover
        return UnprocessedScramSecret.make_many(
            self.boto3_raw_data["UnprocessedScramSecrets"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateScramSecretResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateScramSecretResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateScramSecretResponse:
    boto3_raw_data: "type_defs.BatchDisassociateScramSecretResponseTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")

    @cached_property
    def UnprocessedScramSecrets(self):  # pragma: no cover
        return UnprocessedScramSecret.make_many(
            self.boto3_raw_data["UnprocessedScramSecrets"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateScramSecretResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDisassociateScramSecretResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigurationRequest:
    boto3_raw_data: "type_defs.CreateConfigurationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    ServerProperties = field("ServerProperties")
    Description = field("Description")
    KafkaVersions = field("KafkaVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationRequestTypeDef"]
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

    Arn = field("Arn")
    ServerProperties = field("ServerProperties")
    Description = field("Description")

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
class BrokerEBSVolumeInfo:
    boto3_raw_data: "type_defs.BrokerEBSVolumeInfoTypeDef" = dataclasses.field()

    KafkaBrokerNodeId = field("KafkaBrokerNodeId")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    VolumeSizeGB = field("VolumeSizeGB")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BrokerEBSVolumeInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrokerEBSVolumeInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EBSStorageInfo:
    boto3_raw_data: "type_defs.EBSStorageInfoTypeDef" = dataclasses.field()

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    VolumeSize = field("VolumeSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EBSStorageInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EBSStorageInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStorageRequest:
    boto3_raw_data: "type_defs.UpdateStorageRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    CurrentVersion = field("CurrentVersion")

    @cached_property
    def ProvisionedThroughput(self):  # pragma: no cover
        return ProvisionedThroughput.make_one(
            self.boto3_raw_data["ProvisionedThroughput"]
        )

    StorageMode = field("StorageMode")
    VolumeSizeGB = field("VolumeSizeGB")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStorageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStorageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrokerLogs:
    boto3_raw_data: "type_defs.BrokerLogsTypeDef" = dataclasses.field()

    @cached_property
    def CloudWatchLogs(self):  # pragma: no cover
        return CloudWatchLogs.make_one(self.boto3_raw_data["CloudWatchLogs"])

    @cached_property
    def Firehose(self):  # pragma: no cover
        return Firehose.make_one(self.boto3_raw_data["Firehose"])

    @cached_property
    def S3(self):  # pragma: no cover
        return S3.make_one(self.boto3_raw_data["S3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BrokerLogsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BrokerLogsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrokerNodeInfo:
    boto3_raw_data: "type_defs.BrokerNodeInfoTypeDef" = dataclasses.field()

    AttachedENIId = field("AttachedENIId")
    BrokerId = field("BrokerId")
    ClientSubnet = field("ClientSubnet")
    ClientVpcIpAddress = field("ClientVpcIpAddress")

    @cached_property
    def CurrentBrokerSoftwareInfo(self):  # pragma: no cover
        return BrokerSoftwareInfo.make_one(
            self.boto3_raw_data["CurrentBrokerSoftwareInfo"]
        )

    Endpoints = field("Endpoints")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BrokerNodeInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BrokerNodeInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClientVpcConnectionsResponse:
    boto3_raw_data: "type_defs.ListClientVpcConnectionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClientVpcConnections(self):  # pragma: no cover
        return ClientVpcConnection.make_many(
            self.boto3_raw_data["ClientVpcConnections"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListClientVpcConnectionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClientVpcConnectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterOperationStep:
    boto3_raw_data: "type_defs.ClusterOperationStepTypeDef" = dataclasses.field()

    @cached_property
    def StepInfo(self):  # pragma: no cover
        return ClusterOperationStepInfo.make_one(self.boto3_raw_data["StepInfo"])

    StepName = field("StepName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterOperationStepTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterOperationStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClusterOperationsV2Response:
    boto3_raw_data: "type_defs.ListClusterOperationsV2ResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClusterOperationInfoList(self):  # pragma: no cover
        return ClusterOperationV2Summary.make_many(
            self.boto3_raw_data["ClusterOperationInfoList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListClusterOperationsV2ResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClusterOperationsV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCompatibleKafkaVersionsResponse:
    boto3_raw_data: "type_defs.GetCompatibleKafkaVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CompatibleKafkaVersions(self):  # pragma: no cover
        return CompatibleKafkaVersion.make_many(
            self.boto3_raw_data["CompatibleKafkaVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCompatibleKafkaVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCompatibleKafkaVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateClusterConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")

    @cached_property
    def ConfigurationInfo(self):  # pragma: no cover
        return ConfigurationInfo.make_one(self.boto3_raw_data["ConfigurationInfo"])

    CurrentVersion = field("CurrentVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateClusterConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterKafkaVersionRequest:
    boto3_raw_data: "type_defs.UpdateClusterKafkaVersionRequestTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")
    CurrentVersion = field("CurrentVersion")
    TargetKafkaVersion = field("TargetKafkaVersion")

    @cached_property
    def ConfigurationInfo(self):  # pragma: no cover
        return ConfigurationInfo.make_one(self.boto3_raw_data["ConfigurationInfo"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateClusterKafkaVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterKafkaVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Configuration:
    boto3_raw_data: "type_defs.ConfigurationTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    Description = field("Description")
    KafkaVersions = field("KafkaVersions")

    @cached_property
    def LatestRevision(self):  # pragma: no cover
        return ConfigurationRevision.make_one(self.boto3_raw_data["LatestRevision"])

    Name = field("Name")
    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigurationResponse:
    boto3_raw_data: "type_defs.CreateConfigurationResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreationTime = field("CreationTime")

    @cached_property
    def LatestRevision(self):  # pragma: no cover
        return ConfigurationRevision.make_one(self.boto3_raw_data["LatestRevision"])

    Name = field("Name")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConfigurationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    Description = field("Description")
    KafkaVersions = field("KafkaVersions")

    @cached_property
    def LatestRevision(self):  # pragma: no cover
        return ConfigurationRevision.make_one(self.boto3_raw_data["LatestRevision"])

    Name = field("Name")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationRevisionsResponse:
    boto3_raw_data: "type_defs.ListConfigurationRevisionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Revisions(self):  # pragma: no cover
        return ConfigurationRevision.make_many(self.boto3_raw_data["Revisions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfigurationRevisionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationRevisionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateConfigurationResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def LatestRevision(self):  # pragma: no cover
        return ConfigurationRevision.make_one(self.boto3_raw_data["LatestRevision"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConfigurationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionInfo:
    boto3_raw_data: "type_defs.EncryptionInfoTypeDef" = dataclasses.field()

    @cached_property
    def EncryptionAtRest(self):  # pragma: no cover
        return EncryptionAtRest.make_one(self.boto3_raw_data["EncryptionAtRest"])

    @cached_property
    def EncryptionInTransit(self):  # pragma: no cover
        return EncryptionInTransit.make_one(self.boto3_raw_data["EncryptionInTransit"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EncryptionInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessSasl:
    boto3_raw_data: "type_defs.ServerlessSaslTypeDef" = dataclasses.field()

    @cached_property
    def Iam(self):  # pragma: no cover
        return Iam.make_one(self.boto3_raw_data["Iam"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerlessSaslTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerlessSaslTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaClusterDescription:
    boto3_raw_data: "type_defs.KafkaClusterDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def AmazonMskCluster(self):  # pragma: no cover
        return AmazonMskCluster.make_one(self.boto3_raw_data["AmazonMskCluster"])

    KafkaClusterAlias = field("KafkaClusterAlias")

    @cached_property
    def VpcConfig(self):  # pragma: no cover
        return KafkaClusterClientVpcConfigOutput.make_one(
            self.boto3_raw_data["VpcConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KafkaClusterDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaClusterDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKafkaVersionsResponse:
    boto3_raw_data: "type_defs.ListKafkaVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def KafkaVersions(self):  # pragma: no cover
        return KafkaVersion.make_many(self.boto3_raw_data["KafkaVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKafkaVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKafkaVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClientVpcConnectionsRequestPaginate:
    boto3_raw_data: "type_defs.ListClientVpcConnectionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListClientVpcConnectionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClientVpcConnectionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClusterOperationsRequestPaginate:
    boto3_raw_data: "type_defs.ListClusterOperationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListClusterOperationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClusterOperationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClusterOperationsV2RequestPaginate:
    boto3_raw_data: "type_defs.ListClusterOperationsV2RequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListClusterOperationsV2RequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClusterOperationsV2RequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersRequestPaginate:
    boto3_raw_data: "type_defs.ListClustersRequestPaginateTypeDef" = dataclasses.field()

    ClusterNameFilter = field("ClusterNameFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersV2RequestPaginate:
    boto3_raw_data: "type_defs.ListClustersV2RequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterNameFilter = field("ClusterNameFilter")
    ClusterTypeFilter = field("ClusterTypeFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListClustersV2RequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersV2RequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationRevisionsRequestPaginate:
    boto3_raw_data: "type_defs.ListConfigurationRevisionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfigurationRevisionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationRevisionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKafkaVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListKafkaVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListKafkaVersionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKafkaVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesRequestPaginate:
    boto3_raw_data: "type_defs.ListNodesRequestPaginateTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNodesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReplicatorsRequestPaginate:
    boto3_raw_data: "type_defs.ListReplicatorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ReplicatorNameFilter = field("ReplicatorNameFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListReplicatorsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReplicatorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScramSecretsRequestPaginate:
    boto3_raw_data: "type_defs.ListScramSecretsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ClusterArn = field("ClusterArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListScramSecretsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScramSecretsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcConnectionsRequestPaginate:
    boto3_raw_data: "type_defs.ListVpcConnectionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVpcConnectionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcConnectionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcConnectionsResponse:
    boto3_raw_data: "type_defs.ListVpcConnectionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def VpcConnections(self):  # pragma: no cover
        return VpcConnection.make_many(self.boto3_raw_data["VpcConnections"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVpcConnectionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcConnectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrometheusInfo:
    boto3_raw_data: "type_defs.PrometheusInfoTypeDef" = dataclasses.field()

    @cached_property
    def JmxExporter(self):  # pragma: no cover
        return JmxExporterInfo.make_one(self.boto3_raw_data["JmxExporter"])

    @cached_property
    def NodeExporter(self):  # pragma: no cover
        return NodeExporterInfo.make_one(self.boto3_raw_data["NodeExporter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrometheusInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrometheusInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Prometheus:
    boto3_raw_data: "type_defs.PrometheusTypeDef" = dataclasses.field()

    @cached_property
    def JmxExporter(self):  # pragma: no cover
        return JmxExporter.make_one(self.boto3_raw_data["JmxExporter"])

    @cached_property
    def NodeExporter(self):  # pragma: no cover
        return NodeExporter.make_one(self.boto3_raw_data["NodeExporter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrometheusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrometheusTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicReplicationOutput:
    boto3_raw_data: "type_defs.TopicReplicationOutputTypeDef" = dataclasses.field()

    TopicsToReplicate = field("TopicsToReplicate")
    CopyAccessControlListsForTopics = field("CopyAccessControlListsForTopics")
    CopyTopicConfigurations = field("CopyTopicConfigurations")
    DetectAndCopyNewTopics = field("DetectAndCopyNewTopics")

    @cached_property
    def StartingPosition(self):  # pragma: no cover
        return ReplicationStartingPosition.make_one(
            self.boto3_raw_data["StartingPosition"]
        )

    @cached_property
    def TopicNameConfiguration(self):  # pragma: no cover
        return ReplicationTopicNameConfiguration.make_one(
            self.boto3_raw_data["TopicNameConfiguration"]
        )

    TopicsToExclude = field("TopicsToExclude")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TopicReplicationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicReplicationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TopicReplication:
    boto3_raw_data: "type_defs.TopicReplicationTypeDef" = dataclasses.field()

    TopicsToReplicate = field("TopicsToReplicate")
    CopyAccessControlListsForTopics = field("CopyAccessControlListsForTopics")
    CopyTopicConfigurations = field("CopyTopicConfigurations")
    DetectAndCopyNewTopics = field("DetectAndCopyNewTopics")

    @cached_property
    def StartingPosition(self):  # pragma: no cover
        return ReplicationStartingPosition.make_one(
            self.boto3_raw_data["StartingPosition"]
        )

    @cached_property
    def TopicNameConfiguration(self):  # pragma: no cover
        return ReplicationTopicNameConfiguration.make_one(
            self.boto3_raw_data["TopicNameConfiguration"]
        )

    TopicsToExclude = field("TopicsToExclude")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TopicReplicationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TopicReplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Sasl:
    boto3_raw_data: "type_defs.SaslTypeDef" = dataclasses.field()

    @cached_property
    def Scram(self):  # pragma: no cover
        return Scram.make_one(self.boto3_raw_data["Scram"])

    @cached_property
    def Iam(self):  # pragma: no cover
        return Iam.make_one(self.boto3_raw_data["Iam"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SaslTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SaslTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateReplicationInfoRequest:
    boto3_raw_data: "type_defs.UpdateReplicationInfoRequestTypeDef" = (
        dataclasses.field()
    )

    CurrentVersion = field("CurrentVersion")
    ReplicatorArn = field("ReplicatorArn")
    SourceKafkaClusterArn = field("SourceKafkaClusterArn")
    TargetKafkaClusterArn = field("TargetKafkaClusterArn")

    @cached_property
    def ConsumerGroupReplication(self):  # pragma: no cover
        return ConsumerGroupReplicationUpdate.make_one(
            self.boto3_raw_data["ConsumerGroupReplication"]
        )

    @cached_property
    def TopicReplication(self):  # pragma: no cover
        return TopicReplicationUpdate.make_one(self.boto3_raw_data["TopicReplication"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateReplicationInfoRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateReplicationInfoRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConnectionInfoServerless:
    boto3_raw_data: "type_defs.VpcConnectionInfoServerlessTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")
    Owner = field("Owner")

    @cached_property
    def UserIdentity(self):  # pragma: no cover
        return UserIdentity.make_one(self.boto3_raw_data["UserIdentity"])

    VpcConnectionArn = field("VpcConnectionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConnectionInfoServerlessTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConnectionInfoServerlessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConnectionInfo:
    boto3_raw_data: "type_defs.VpcConnectionInfoTypeDef" = dataclasses.field()

    VpcConnectionArn = field("VpcConnectionArn")
    Owner = field("Owner")

    @cached_property
    def UserIdentity(self):  # pragma: no cover
        return UserIdentity.make_one(self.boto3_raw_data["UserIdentity"])

    CreationTime = field("CreationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConnectionInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConnectionInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConnectivitySasl:
    boto3_raw_data: "type_defs.VpcConnectivitySaslTypeDef" = dataclasses.field()

    @cached_property
    def Scram(self):  # pragma: no cover
        return VpcConnectivityScram.make_one(self.boto3_raw_data["Scram"])

    @cached_property
    def Iam(self):  # pragma: no cover
        return VpcConnectivityIam.make_one(self.boto3_raw_data["Iam"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcConnectivitySaslTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConnectivitySaslTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicatorSummary:
    boto3_raw_data: "type_defs.ReplicatorSummaryTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")
    CurrentVersion = field("CurrentVersion")
    IsReplicatorReference = field("IsReplicatorReference")

    @cached_property
    def KafkaClustersSummary(self):  # pragma: no cover
        return KafkaClusterSummary.make_many(
            self.boto3_raw_data["KafkaClustersSummary"]
        )

    @cached_property
    def ReplicationInfoSummaryList(self):  # pragma: no cover
        return ReplicationInfoSummary.make_many(
            self.boto3_raw_data["ReplicationInfoSummaryList"]
        )

    ReplicatorArn = field("ReplicatorArn")
    ReplicatorName = field("ReplicatorName")
    ReplicatorResourceArn = field("ReplicatorResourceArn")
    ReplicatorState = field("ReplicatorState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicatorSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicatorSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBrokerStorageRequest:
    boto3_raw_data: "type_defs.UpdateBrokerStorageRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    CurrentVersion = field("CurrentVersion")

    @cached_property
    def TargetBrokerEBSVolumeInfo(self):  # pragma: no cover
        return BrokerEBSVolumeInfo.make_many(
            self.boto3_raw_data["TargetBrokerEBSVolumeInfo"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBrokerStorageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBrokerStorageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageInfo:
    boto3_raw_data: "type_defs.StorageInfoTypeDef" = dataclasses.field()

    @cached_property
    def EbsStorageInfo(self):  # pragma: no cover
        return EBSStorageInfo.make_one(self.boto3_raw_data["EbsStorageInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorageInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StorageInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingInfo:
    boto3_raw_data: "type_defs.LoggingInfoTypeDef" = dataclasses.field()

    @cached_property
    def BrokerLogs(self):  # pragma: no cover
        return BrokerLogs.make_one(self.boto3_raw_data["BrokerLogs"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeInfo:
    boto3_raw_data: "type_defs.NodeInfoTypeDef" = dataclasses.field()

    AddedToClusterTime = field("AddedToClusterTime")

    @cached_property
    def BrokerNodeInfo(self):  # pragma: no cover
        return BrokerNodeInfo.make_one(self.boto3_raw_data["BrokerNodeInfo"])

    @cached_property
    def ControllerNodeInfo(self):  # pragma: no cover
        return ControllerNodeInfo.make_one(self.boto3_raw_data["ControllerNodeInfo"])

    InstanceType = field("InstanceType")
    NodeARN = field("NodeARN")
    NodeType = field("NodeType")

    @cached_property
    def ZookeeperNodeInfo(self):  # pragma: no cover
        return ZookeeperNodeInfo.make_one(self.boto3_raw_data["ZookeeperNodeInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationsResponse:
    boto3_raw_data: "type_defs.ListConfigurationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Configurations(self):  # pragma: no cover
        return Configuration.make_many(self.boto3_raw_data["Configurations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConfigurationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessClientAuthentication:
    boto3_raw_data: "type_defs.ServerlessClientAuthenticationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sasl(self):  # pragma: no cover
        return ServerlessSasl.make_one(self.boto3_raw_data["Sasl"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ServerlessClientAuthenticationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerlessClientAuthenticationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaCluster:
    boto3_raw_data: "type_defs.KafkaClusterTypeDef" = dataclasses.field()

    @cached_property
    def AmazonMskCluster(self):  # pragma: no cover
        return AmazonMskCluster.make_one(self.boto3_raw_data["AmazonMskCluster"])

    VpcConfig = field("VpcConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KafkaClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KafkaClusterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenMonitoringInfo:
    boto3_raw_data: "type_defs.OpenMonitoringInfoTypeDef" = dataclasses.field()

    @cached_property
    def Prometheus(self):  # pragma: no cover
        return PrometheusInfo.make_one(self.boto3_raw_data["Prometheus"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenMonitoringInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenMonitoringInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenMonitoring:
    boto3_raw_data: "type_defs.OpenMonitoringTypeDef" = dataclasses.field()

    @cached_property
    def Prometheus(self):  # pragma: no cover
        return Prometheus.make_one(self.boto3_raw_data["Prometheus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpenMonitoringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpenMonitoringTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationInfoDescription:
    boto3_raw_data: "type_defs.ReplicationInfoDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def ConsumerGroupReplication(self):  # pragma: no cover
        return ConsumerGroupReplicationOutput.make_one(
            self.boto3_raw_data["ConsumerGroupReplication"]
        )

    SourceKafkaClusterAlias = field("SourceKafkaClusterAlias")
    TargetCompressionType = field("TargetCompressionType")
    TargetKafkaClusterAlias = field("TargetKafkaClusterAlias")

    @cached_property
    def TopicReplication(self):  # pragma: no cover
        return TopicReplicationOutput.make_one(self.boto3_raw_data["TopicReplication"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationInfoDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationInfoDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientAuthenticationOutput:
    boto3_raw_data: "type_defs.ClientAuthenticationOutputTypeDef" = dataclasses.field()

    @cached_property
    def Sasl(self):  # pragma: no cover
        return Sasl.make_one(self.boto3_raw_data["Sasl"])

    @cached_property
    def Tls(self):  # pragma: no cover
        return TlsOutput.make_one(self.boto3_raw_data["Tls"])

    @cached_property
    def Unauthenticated(self):  # pragma: no cover
        return Unauthenticated.make_one(self.boto3_raw_data["Unauthenticated"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientAuthenticationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientAuthenticationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientAuthentication:
    boto3_raw_data: "type_defs.ClientAuthenticationTypeDef" = dataclasses.field()

    @cached_property
    def Sasl(self):  # pragma: no cover
        return Sasl.make_one(self.boto3_raw_data["Sasl"])

    Tls = field("Tls")

    @cached_property
    def Unauthenticated(self):  # pragma: no cover
        return Unauthenticated.make_one(self.boto3_raw_data["Unauthenticated"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientAuthenticationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientAuthenticationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterOperationV2Serverless:
    boto3_raw_data: "type_defs.ClusterOperationV2ServerlessTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VpcConnectionInfo(self):  # pragma: no cover
        return VpcConnectionInfoServerless.make_one(
            self.boto3_raw_data["VpcConnectionInfo"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterOperationV2ServerlessTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterOperationV2ServerlessTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConnectivityClientAuthentication:
    boto3_raw_data: "type_defs.VpcConnectivityClientAuthenticationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sasl(self):  # pragma: no cover
        return VpcConnectivitySasl.make_one(self.boto3_raw_data["Sasl"])

    @cached_property
    def Tls(self):  # pragma: no cover
        return VpcConnectivityTls.make_one(self.boto3_raw_data["Tls"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VpcConnectivityClientAuthenticationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConnectivityClientAuthenticationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReplicatorsResponse:
    boto3_raw_data: "type_defs.ListReplicatorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Replicators(self):  # pragma: no cover
        return ReplicatorSummary.make_many(self.boto3_raw_data["Replicators"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListReplicatorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReplicatorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodesResponse:
    boto3_raw_data: "type_defs.ListNodesResponseTypeDef" = dataclasses.field()

    @cached_property
    def NodeInfoList(self):  # pragma: no cover
        return NodeInfo.make_many(self.boto3_raw_data["NodeInfoList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListNodesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerlessRequest:
    boto3_raw_data: "type_defs.ServerlessRequestTypeDef" = dataclasses.field()

    VpcConfigs = field("VpcConfigs")

    @cached_property
    def ClientAuthentication(self):  # pragma: no cover
        return ServerlessClientAuthentication.make_one(
            self.boto3_raw_data["ClientAuthentication"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerlessRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerlessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Serverless:
    boto3_raw_data: "type_defs.ServerlessTypeDef" = dataclasses.field()

    @cached_property
    def VpcConfigs(self):  # pragma: no cover
        return VpcConfigOutput.make_many(self.boto3_raw_data["VpcConfigs"])

    @cached_property
    def ClientAuthentication(self):  # pragma: no cover
        return ServerlessClientAuthentication.make_one(
            self.boto3_raw_data["ClientAuthentication"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServerlessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServerlessTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMonitoringRequest:
    boto3_raw_data: "type_defs.UpdateMonitoringRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    CurrentVersion = field("CurrentVersion")
    EnhancedMonitoring = field("EnhancedMonitoring")

    @cached_property
    def OpenMonitoring(self):  # pragma: no cover
        return OpenMonitoringInfo.make_one(self.boto3_raw_data["OpenMonitoring"])

    @cached_property
    def LoggingInfo(self):  # pragma: no cover
        return LoggingInfo.make_one(self.boto3_raw_data["LoggingInfo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMonitoringRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMonitoringRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicatorResponse:
    boto3_raw_data: "type_defs.DescribeReplicatorResponseTypeDef" = dataclasses.field()

    CreationTime = field("CreationTime")
    CurrentVersion = field("CurrentVersion")
    IsReplicatorReference = field("IsReplicatorReference")

    @cached_property
    def KafkaClusters(self):  # pragma: no cover
        return KafkaClusterDescription.make_many(self.boto3_raw_data["KafkaClusters"])

    @cached_property
    def ReplicationInfoList(self):  # pragma: no cover
        return ReplicationInfoDescription.make_many(
            self.boto3_raw_data["ReplicationInfoList"]
        )

    ReplicatorArn = field("ReplicatorArn")
    ReplicatorDescription = field("ReplicatorDescription")
    ReplicatorName = field("ReplicatorName")
    ReplicatorResourceArn = field("ReplicatorResourceArn")
    ReplicatorState = field("ReplicatorState")
    ServiceExecutionRoleArn = field("ServiceExecutionRoleArn")

    @cached_property
    def StateInfo(self):  # pragma: no cover
        return ReplicationStateInfo.make_one(self.boto3_raw_data["StateInfo"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReplicatorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicatorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationInfo:
    boto3_raw_data: "type_defs.ReplicationInfoTypeDef" = dataclasses.field()

    ConsumerGroupReplication = field("ConsumerGroupReplication")
    SourceKafkaClusterArn = field("SourceKafkaClusterArn")
    TargetCompressionType = field("TargetCompressionType")
    TargetKafkaClusterArn = field("TargetKafkaClusterArn")
    TopicReplication = field("TopicReplication")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicationInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConnectivity:
    boto3_raw_data: "type_defs.VpcConnectivityTypeDef" = dataclasses.field()

    @cached_property
    def ClientAuthentication(self):  # pragma: no cover
        return VpcConnectivityClientAuthentication.make_one(
            self.boto3_raw_data["ClientAuthentication"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConnectivityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConnectivityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicatorRequest:
    boto3_raw_data: "type_defs.CreateReplicatorRequestTypeDef" = dataclasses.field()

    @cached_property
    def KafkaClusters(self):  # pragma: no cover
        return KafkaCluster.make_many(self.boto3_raw_data["KafkaClusters"])

    @cached_property
    def ReplicationInfoList(self):  # pragma: no cover
        return ReplicationInfo.make_many(self.boto3_raw_data["ReplicationInfoList"])

    ReplicatorName = field("ReplicatorName")
    ServiceExecutionRoleArn = field("ServiceExecutionRoleArn")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReplicatorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSecurityRequest:
    boto3_raw_data: "type_defs.UpdateSecurityRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    CurrentVersion = field("CurrentVersion")
    ClientAuthentication = field("ClientAuthentication")

    @cached_property
    def EncryptionInfo(self):  # pragma: no cover
        return EncryptionInfo.make_one(self.boto3_raw_data["EncryptionInfo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSecurityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSecurityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectivityInfo:
    boto3_raw_data: "type_defs.ConnectivityInfoTypeDef" = dataclasses.field()

    @cached_property
    def PublicAccess(self):  # pragma: no cover
        return PublicAccess.make_one(self.boto3_raw_data["PublicAccess"])

    @cached_property
    def VpcConnectivity(self):  # pragma: no cover
        return VpcConnectivity.make_one(self.boto3_raw_data["VpcConnectivity"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectivityInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectivityInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrokerNodeGroupInfoOutput:
    boto3_raw_data: "type_defs.BrokerNodeGroupInfoOutputTypeDef" = dataclasses.field()

    ClientSubnets = field("ClientSubnets")
    InstanceType = field("InstanceType")
    BrokerAZDistribution = field("BrokerAZDistribution")
    SecurityGroups = field("SecurityGroups")

    @cached_property
    def StorageInfo(self):  # pragma: no cover
        return StorageInfo.make_one(self.boto3_raw_data["StorageInfo"])

    @cached_property
    def ConnectivityInfo(self):  # pragma: no cover
        return ConnectivityInfo.make_one(self.boto3_raw_data["ConnectivityInfo"])

    ZoneIds = field("ZoneIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BrokerNodeGroupInfoOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrokerNodeGroupInfoOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BrokerNodeGroupInfo:
    boto3_raw_data: "type_defs.BrokerNodeGroupInfoTypeDef" = dataclasses.field()

    ClientSubnets = field("ClientSubnets")
    InstanceType = field("InstanceType")
    BrokerAZDistribution = field("BrokerAZDistribution")
    SecurityGroups = field("SecurityGroups")

    @cached_property
    def StorageInfo(self):  # pragma: no cover
        return StorageInfo.make_one(self.boto3_raw_data["StorageInfo"])

    @cached_property
    def ConnectivityInfo(self):  # pragma: no cover
        return ConnectivityInfo.make_one(self.boto3_raw_data["ConnectivityInfo"])

    ZoneIds = field("ZoneIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BrokerNodeGroupInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BrokerNodeGroupInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MutableClusterInfo:
    boto3_raw_data: "type_defs.MutableClusterInfoTypeDef" = dataclasses.field()

    @cached_property
    def BrokerEBSVolumeInfo(self):  # pragma: no cover
        return BrokerEBSVolumeInfo.make_many(self.boto3_raw_data["BrokerEBSVolumeInfo"])

    @cached_property
    def ConfigurationInfo(self):  # pragma: no cover
        return ConfigurationInfo.make_one(self.boto3_raw_data["ConfigurationInfo"])

    NumberOfBrokerNodes = field("NumberOfBrokerNodes")
    EnhancedMonitoring = field("EnhancedMonitoring")

    @cached_property
    def OpenMonitoring(self):  # pragma: no cover
        return OpenMonitoring.make_one(self.boto3_raw_data["OpenMonitoring"])

    KafkaVersion = field("KafkaVersion")

    @cached_property
    def LoggingInfo(self):  # pragma: no cover
        return LoggingInfo.make_one(self.boto3_raw_data["LoggingInfo"])

    InstanceType = field("InstanceType")

    @cached_property
    def ClientAuthentication(self):  # pragma: no cover
        return ClientAuthenticationOutput.make_one(
            self.boto3_raw_data["ClientAuthentication"]
        )

    @cached_property
    def EncryptionInfo(self):  # pragma: no cover
        return EncryptionInfo.make_one(self.boto3_raw_data["EncryptionInfo"])

    @cached_property
    def ConnectivityInfo(self):  # pragma: no cover
        return ConnectivityInfo.make_one(self.boto3_raw_data["ConnectivityInfo"])

    StorageMode = field("StorageMode")

    @cached_property
    def BrokerCountUpdateInfo(self):  # pragma: no cover
        return BrokerCountUpdateInfo.make_one(
            self.boto3_raw_data["BrokerCountUpdateInfo"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MutableClusterInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MutableClusterInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectivityRequest:
    boto3_raw_data: "type_defs.UpdateConnectivityRequestTypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")

    @cached_property
    def ConnectivityInfo(self):  # pragma: no cover
        return ConnectivityInfo.make_one(self.boto3_raw_data["ConnectivityInfo"])

    CurrentVersion = field("CurrentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectivityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectivityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterInfo:
    boto3_raw_data: "type_defs.ClusterInfoTypeDef" = dataclasses.field()

    ActiveOperationArn = field("ActiveOperationArn")

    @cached_property
    def BrokerNodeGroupInfo(self):  # pragma: no cover
        return BrokerNodeGroupInfoOutput.make_one(
            self.boto3_raw_data["BrokerNodeGroupInfo"]
        )

    @cached_property
    def ClientAuthentication(self):  # pragma: no cover
        return ClientAuthenticationOutput.make_one(
            self.boto3_raw_data["ClientAuthentication"]
        )

    ClusterArn = field("ClusterArn")
    ClusterName = field("ClusterName")
    CreationTime = field("CreationTime")

    @cached_property
    def CurrentBrokerSoftwareInfo(self):  # pragma: no cover
        return BrokerSoftwareInfo.make_one(
            self.boto3_raw_data["CurrentBrokerSoftwareInfo"]
        )

    CurrentVersion = field("CurrentVersion")

    @cached_property
    def EncryptionInfo(self):  # pragma: no cover
        return EncryptionInfo.make_one(self.boto3_raw_data["EncryptionInfo"])

    EnhancedMonitoring = field("EnhancedMonitoring")

    @cached_property
    def OpenMonitoring(self):  # pragma: no cover
        return OpenMonitoring.make_one(self.boto3_raw_data["OpenMonitoring"])

    @cached_property
    def LoggingInfo(self):  # pragma: no cover
        return LoggingInfo.make_one(self.boto3_raw_data["LoggingInfo"])

    NumberOfBrokerNodes = field("NumberOfBrokerNodes")
    State = field("State")

    @cached_property
    def StateInfo(self):  # pragma: no cover
        return StateInfo.make_one(self.boto3_raw_data["StateInfo"])

    Tags = field("Tags")
    ZookeeperConnectString = field("ZookeeperConnectString")
    ZookeeperConnectStringTls = field("ZookeeperConnectStringTls")
    StorageMode = field("StorageMode")
    CustomerActionStatus = field("CustomerActionStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Provisioned:
    boto3_raw_data: "type_defs.ProvisionedTypeDef" = dataclasses.field()

    @cached_property
    def BrokerNodeGroupInfo(self):  # pragma: no cover
        return BrokerNodeGroupInfoOutput.make_one(
            self.boto3_raw_data["BrokerNodeGroupInfo"]
        )

    NumberOfBrokerNodes = field("NumberOfBrokerNodes")

    @cached_property
    def CurrentBrokerSoftwareInfo(self):  # pragma: no cover
        return BrokerSoftwareInfo.make_one(
            self.boto3_raw_data["CurrentBrokerSoftwareInfo"]
        )

    @cached_property
    def ClientAuthentication(self):  # pragma: no cover
        return ClientAuthenticationOutput.make_one(
            self.boto3_raw_data["ClientAuthentication"]
        )

    @cached_property
    def EncryptionInfo(self):  # pragma: no cover
        return EncryptionInfo.make_one(self.boto3_raw_data["EncryptionInfo"])

    EnhancedMonitoring = field("EnhancedMonitoring")

    @cached_property
    def OpenMonitoring(self):  # pragma: no cover
        return OpenMonitoringInfo.make_one(self.boto3_raw_data["OpenMonitoring"])

    @cached_property
    def LoggingInfo(self):  # pragma: no cover
        return LoggingInfo.make_one(self.boto3_raw_data["LoggingInfo"])

    ZookeeperConnectString = field("ZookeeperConnectString")
    ZookeeperConnectStringTls = field("ZookeeperConnectStringTls")
    StorageMode = field("StorageMode")
    CustomerActionStatus = field("CustomerActionStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProvisionedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProvisionedTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterOperationInfo:
    boto3_raw_data: "type_defs.ClusterOperationInfoTypeDef" = dataclasses.field()

    ClientRequestId = field("ClientRequestId")
    ClusterArn = field("ClusterArn")
    CreationTime = field("CreationTime")
    EndTime = field("EndTime")

    @cached_property
    def ErrorInfo(self):  # pragma: no cover
        return ErrorInfo.make_one(self.boto3_raw_data["ErrorInfo"])

    OperationArn = field("OperationArn")
    OperationState = field("OperationState")

    @cached_property
    def OperationSteps(self):  # pragma: no cover
        return ClusterOperationStep.make_many(self.boto3_raw_data["OperationSteps"])

    OperationType = field("OperationType")

    @cached_property
    def SourceClusterInfo(self):  # pragma: no cover
        return MutableClusterInfo.make_one(self.boto3_raw_data["SourceClusterInfo"])

    @cached_property
    def TargetClusterInfo(self):  # pragma: no cover
        return MutableClusterInfo.make_one(self.boto3_raw_data["TargetClusterInfo"])

    @cached_property
    def VpcConnectionInfo(self):  # pragma: no cover
        return VpcConnectionInfo.make_one(self.boto3_raw_data["VpcConnectionInfo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterOperationInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterOperationInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterOperationV2Provisioned:
    boto3_raw_data: "type_defs.ClusterOperationV2ProvisionedTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OperationSteps(self):  # pragma: no cover
        return ClusterOperationStep.make_many(self.boto3_raw_data["OperationSteps"])

    @cached_property
    def SourceClusterInfo(self):  # pragma: no cover
        return MutableClusterInfo.make_one(self.boto3_raw_data["SourceClusterInfo"])

    @cached_property
    def TargetClusterInfo(self):  # pragma: no cover
        return MutableClusterInfo.make_one(self.boto3_raw_data["TargetClusterInfo"])

    @cached_property
    def VpcConnectionInfo(self):  # pragma: no cover
        return VpcConnectionInfo.make_one(self.boto3_raw_data["VpcConnectionInfo"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ClusterOperationV2ProvisionedTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterOperationV2ProvisionedTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterResponse:
    boto3_raw_data: "type_defs.DescribeClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def ClusterInfo(self):  # pragma: no cover
        return ClusterInfo.make_one(self.boto3_raw_data["ClusterInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersResponse:
    boto3_raw_data: "type_defs.ListClustersResponseTypeDef" = dataclasses.field()

    @cached_property
    def ClusterInfoList(self):  # pragma: no cover
        return ClusterInfo.make_many(self.boto3_raw_data["ClusterInfoList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cluster:
    boto3_raw_data: "type_defs.ClusterTypeDef" = dataclasses.field()

    ActiveOperationArn = field("ActiveOperationArn")
    ClusterType = field("ClusterType")
    ClusterArn = field("ClusterArn")
    ClusterName = field("ClusterName")
    CreationTime = field("CreationTime")
    CurrentVersion = field("CurrentVersion")
    State = field("State")

    @cached_property
    def StateInfo(self):  # pragma: no cover
        return StateInfo.make_one(self.boto3_raw_data["StateInfo"])

    Tags = field("Tags")

    @cached_property
    def Provisioned(self):  # pragma: no cover
        return Provisioned.make_one(self.boto3_raw_data["Provisioned"])

    @cached_property
    def Serverless(self):  # pragma: no cover
        return Serverless.make_one(self.boto3_raw_data["Serverless"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterRequest:
    boto3_raw_data: "type_defs.CreateClusterRequestTypeDef" = dataclasses.field()

    BrokerNodeGroupInfo = field("BrokerNodeGroupInfo")
    ClusterName = field("ClusterName")
    KafkaVersion = field("KafkaVersion")
    NumberOfBrokerNodes = field("NumberOfBrokerNodes")
    ClientAuthentication = field("ClientAuthentication")

    @cached_property
    def ConfigurationInfo(self):  # pragma: no cover
        return ConfigurationInfo.make_one(self.boto3_raw_data["ConfigurationInfo"])

    @cached_property
    def EncryptionInfo(self):  # pragma: no cover
        return EncryptionInfo.make_one(self.boto3_raw_data["EncryptionInfo"])

    EnhancedMonitoring = field("EnhancedMonitoring")

    @cached_property
    def OpenMonitoring(self):  # pragma: no cover
        return OpenMonitoringInfo.make_one(self.boto3_raw_data["OpenMonitoring"])

    @cached_property
    def LoggingInfo(self):  # pragma: no cover
        return LoggingInfo.make_one(self.boto3_raw_data["LoggingInfo"])

    Tags = field("Tags")
    StorageMode = field("StorageMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedRequest:
    boto3_raw_data: "type_defs.ProvisionedRequestTypeDef" = dataclasses.field()

    BrokerNodeGroupInfo = field("BrokerNodeGroupInfo")
    KafkaVersion = field("KafkaVersion")
    NumberOfBrokerNodes = field("NumberOfBrokerNodes")
    ClientAuthentication = field("ClientAuthentication")

    @cached_property
    def ConfigurationInfo(self):  # pragma: no cover
        return ConfigurationInfo.make_one(self.boto3_raw_data["ConfigurationInfo"])

    @cached_property
    def EncryptionInfo(self):  # pragma: no cover
        return EncryptionInfo.make_one(self.boto3_raw_data["EncryptionInfo"])

    EnhancedMonitoring = field("EnhancedMonitoring")

    @cached_property
    def OpenMonitoring(self):  # pragma: no cover
        return OpenMonitoringInfo.make_one(self.boto3_raw_data["OpenMonitoring"])

    @cached_property
    def LoggingInfo(self):  # pragma: no cover
        return LoggingInfo.make_one(self.boto3_raw_data["LoggingInfo"])

    StorageMode = field("StorageMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterOperationResponse:
    boto3_raw_data: "type_defs.DescribeClusterOperationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClusterOperationInfo(self):  # pragma: no cover
        return ClusterOperationInfo.make_one(
            self.boto3_raw_data["ClusterOperationInfo"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClusterOperationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterOperationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClusterOperationsResponse:
    boto3_raw_data: "type_defs.ListClusterOperationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClusterOperationInfoList(self):  # pragma: no cover
        return ClusterOperationInfo.make_many(
            self.boto3_raw_data["ClusterOperationInfoList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListClusterOperationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClusterOperationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterOperationV2:
    boto3_raw_data: "type_defs.ClusterOperationV2TypeDef" = dataclasses.field()

    ClusterArn = field("ClusterArn")
    ClusterType = field("ClusterType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def ErrorInfo(self):  # pragma: no cover
        return ErrorInfo.make_one(self.boto3_raw_data["ErrorInfo"])

    OperationArn = field("OperationArn")
    OperationState = field("OperationState")
    OperationType = field("OperationType")

    @cached_property
    def Provisioned(self):  # pragma: no cover
        return ClusterOperationV2Provisioned.make_one(
            self.boto3_raw_data["Provisioned"]
        )

    @cached_property
    def Serverless(self):  # pragma: no cover
        return ClusterOperationV2Serverless.make_one(self.boto3_raw_data["Serverless"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterOperationV2TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterOperationV2TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterV2Response:
    boto3_raw_data: "type_defs.DescribeClusterV2ResponseTypeDef" = dataclasses.field()

    @cached_property
    def ClusterInfo(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["ClusterInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterV2ResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersV2Response:
    boto3_raw_data: "type_defs.ListClustersV2ResponseTypeDef" = dataclasses.field()

    @cached_property
    def ClusterInfoList(self):  # pragma: no cover
        return Cluster.make_many(self.boto3_raw_data["ClusterInfoList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersV2ResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterV2Request:
    boto3_raw_data: "type_defs.CreateClusterV2RequestTypeDef" = dataclasses.field()

    ClusterName = field("ClusterName")
    Tags = field("Tags")

    @cached_property
    def Provisioned(self):  # pragma: no cover
        return ProvisionedRequest.make_one(self.boto3_raw_data["Provisioned"])

    @cached_property
    def Serverless(self):  # pragma: no cover
        return ServerlessRequest.make_one(self.boto3_raw_data["Serverless"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterV2RequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterV2RequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterOperationV2Response:
    boto3_raw_data: "type_defs.DescribeClusterOperationV2ResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClusterOperationInfo(self):  # pragma: no cover
        return ClusterOperationV2.make_one(self.boto3_raw_data["ClusterOperationInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterOperationV2ResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterOperationV2ResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
