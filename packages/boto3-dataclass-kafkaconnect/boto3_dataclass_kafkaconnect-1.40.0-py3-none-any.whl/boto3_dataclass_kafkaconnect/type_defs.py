# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kafkaconnect import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class VpcDescription:
    boto3_raw_data: "type_defs.VpcDescriptionTypeDef" = dataclasses.field()

    securityGroups = field("securityGroups")
    subnets = field("subnets")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcDescriptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Vpc:
    boto3_raw_data: "type_defs.VpcTypeDef" = dataclasses.field()

    subnets = field("subnets")
    securityGroups = field("securityGroups")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScaleInPolicyDescription:
    boto3_raw_data: "type_defs.ScaleInPolicyDescriptionTypeDef" = dataclasses.field()

    cpuUtilizationPercentage = field("cpuUtilizationPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScaleInPolicyDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScaleInPolicyDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScaleOutPolicyDescription:
    boto3_raw_data: "type_defs.ScaleOutPolicyDescriptionTypeDef" = dataclasses.field()

    cpuUtilizationPercentage = field("cpuUtilizationPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScaleOutPolicyDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScaleOutPolicyDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScaleInPolicy:
    boto3_raw_data: "type_defs.ScaleInPolicyTypeDef" = dataclasses.field()

    cpuUtilizationPercentage = field("cpuUtilizationPercentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScaleInPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScaleInPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScaleOutPolicy:
    boto3_raw_data: "type_defs.ScaleOutPolicyTypeDef" = dataclasses.field()

    cpuUtilizationPercentage = field("cpuUtilizationPercentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScaleOutPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScaleOutPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScaleInPolicyUpdate:
    boto3_raw_data: "type_defs.ScaleInPolicyUpdateTypeDef" = dataclasses.field()

    cpuUtilizationPercentage = field("cpuUtilizationPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScaleInPolicyUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScaleInPolicyUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScaleOutPolicyUpdate:
    boto3_raw_data: "type_defs.ScaleOutPolicyUpdateTypeDef" = dataclasses.field()

    cpuUtilizationPercentage = field("cpuUtilizationPercentage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScaleOutPolicyUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScaleOutPolicyUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedCapacityDescription:
    boto3_raw_data: "type_defs.ProvisionedCapacityDescriptionTypeDef" = (
        dataclasses.field()
    )

    mcuCount = field("mcuCount")
    workerCount = field("workerCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisionedCapacityDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedCapacityDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedCapacity:
    boto3_raw_data: "type_defs.ProvisionedCapacityTypeDef" = dataclasses.field()

    mcuCount = field("mcuCount")
    workerCount = field("workerCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedCapacityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedCapacityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedCapacityUpdate:
    boto3_raw_data: "type_defs.ProvisionedCapacityUpdateTypeDef" = dataclasses.field()

    mcuCount = field("mcuCount")
    workerCount = field("workerCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedCapacityUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedCapacityUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsLogDeliveryDescription:
    boto3_raw_data: "type_defs.CloudWatchLogsLogDeliveryDescriptionTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")
    logGroup = field("logGroup")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudWatchLogsLogDeliveryDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsLogDeliveryDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogsLogDelivery:
    boto3_raw_data: "type_defs.CloudWatchLogsLogDeliveryTypeDef" = dataclasses.field()

    enabled = field("enabled")
    logGroup = field("logGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogsLogDeliveryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogsLogDeliveryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorOperationStep:
    boto3_raw_data: "type_defs.ConnectorOperationStepTypeDef" = dataclasses.field()

    stepType = field("stepType")
    stepState = field("stepState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorOperationStepTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorOperationStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorOperationSummary:
    boto3_raw_data: "type_defs.ConnectorOperationSummaryTypeDef" = dataclasses.field()

    connectorOperationArn = field("connectorOperationArn")
    connectorOperationType = field("connectorOperationType")
    connectorOperationState = field("connectorOperationState")
    creationTime = field("creationTime")
    endTime = field("endTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorOperationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorOperationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaClusterClientAuthenticationDescription:
    boto3_raw_data: "type_defs.KafkaClusterClientAuthenticationDescriptionTypeDef" = (
        dataclasses.field()
    )

    authenticationType = field("authenticationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KafkaClusterClientAuthenticationDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaClusterClientAuthenticationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaClusterEncryptionInTransitDescription:
    boto3_raw_data: "type_defs.KafkaClusterEncryptionInTransitDescriptionTypeDef" = (
        dataclasses.field()
    )

    encryptionType = field("encryptionType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KafkaClusterEncryptionInTransitDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaClusterEncryptionInTransitDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerConfigurationDescription:
    boto3_raw_data: "type_defs.WorkerConfigurationDescriptionTypeDef" = (
        dataclasses.field()
    )

    revision = field("revision")
    workerConfigurationArn = field("workerConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WorkerConfigurationDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerConfigurationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaClusterClientAuthentication:
    boto3_raw_data: "type_defs.KafkaClusterClientAuthenticationTypeDef" = (
        dataclasses.field()
    )

    authenticationType = field("authenticationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KafkaClusterClientAuthenticationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaClusterClientAuthenticationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaClusterEncryptionInTransit:
    boto3_raw_data: "type_defs.KafkaClusterEncryptionInTransitTypeDef" = (
        dataclasses.field()
    )

    encryptionType = field("encryptionType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KafkaClusterEncryptionInTransitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KafkaClusterEncryptionInTransitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerConfiguration:
    boto3_raw_data: "type_defs.WorkerConfigurationTypeDef" = dataclasses.field()

    revision = field("revision")
    workerConfigurationArn = field("workerConfigurationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerConfigurationTypeDef"]
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
class CreateWorkerConfigurationRequest:
    boto3_raw_data: "type_defs.CreateWorkerConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    propertiesFileContent = field("propertiesFileContent")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorkerConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkerConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerConfigurationRevisionSummary:
    boto3_raw_data: "type_defs.WorkerConfigurationRevisionSummaryTypeDef" = (
        dataclasses.field()
    )

    creationTime = field("creationTime")
    description = field("description")
    revision = field("revision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkerConfigurationRevisionSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerConfigurationRevisionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomPluginDescription:
    boto3_raw_data: "type_defs.CustomPluginDescriptionTypeDef" = dataclasses.field()

    customPluginArn = field("customPluginArn")
    revision = field("revision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomPluginDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomPluginDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomPluginFileDescription:
    boto3_raw_data: "type_defs.CustomPluginFileDescriptionTypeDef" = dataclasses.field()

    fileMd5 = field("fileMd5")
    fileSize = field("fileSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomPluginFileDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomPluginFileDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3LocationDescription:
    boto3_raw_data: "type_defs.S3LocationDescriptionTypeDef" = dataclasses.field()

    bucketArn = field("bucketArn")
    fileKey = field("fileKey")
    objectVersion = field("objectVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3LocationDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3LocationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    bucketArn = field("bucketArn")
    fileKey = field("fileKey")
    objectVersion = field("objectVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomPlugin:
    boto3_raw_data: "type_defs.CustomPluginTypeDef" = dataclasses.field()

    customPluginArn = field("customPluginArn")
    revision = field("revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomPluginTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomPluginTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectorRequest:
    boto3_raw_data: "type_defs.DeleteConnectorRequestTypeDef" = dataclasses.field()

    connectorArn = field("connectorArn")
    currentVersion = field("currentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomPluginRequest:
    boto3_raw_data: "type_defs.DeleteCustomPluginRequestTypeDef" = dataclasses.field()

    customPluginArn = field("customPluginArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCustomPluginRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomPluginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkerConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteWorkerConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    workerConfigurationArn = field("workerConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteWorkerConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkerConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorOperationRequest:
    boto3_raw_data: "type_defs.DescribeConnectorOperationRequestTypeDef" = (
        dataclasses.field()
    )

    connectorOperationArn = field("connectorOperationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConnectorOperationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorOperationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateDescription:
    boto3_raw_data: "type_defs.StateDescriptionTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StateDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorRequest:
    boto3_raw_data: "type_defs.DescribeConnectorRequestTypeDef" = dataclasses.field()

    connectorArn = field("connectorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomPluginRequest:
    boto3_raw_data: "type_defs.DescribeCustomPluginRequestTypeDef" = dataclasses.field()

    customPluginArn = field("customPluginArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCustomPluginRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomPluginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkerConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeWorkerConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    workerConfigurationArn = field("workerConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkerConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkerConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerConfigurationRevisionDescription:
    boto3_raw_data: "type_defs.WorkerConfigurationRevisionDescriptionTypeDef" = (
        dataclasses.field()
    )

    creationTime = field("creationTime")
    description = field("description")
    propertiesFileContent = field("propertiesFileContent")
    revision = field("revision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkerConfigurationRevisionDescriptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerConfigurationRevisionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirehoseLogDeliveryDescription:
    boto3_raw_data: "type_defs.FirehoseLogDeliveryDescriptionTypeDef" = (
        dataclasses.field()
    )

    deliveryStream = field("deliveryStream")
    enabled = field("enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FirehoseLogDeliveryDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirehoseLogDeliveryDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FirehoseLogDelivery:
    boto3_raw_data: "type_defs.FirehoseLogDeliveryTypeDef" = dataclasses.field()

    enabled = field("enabled")
    deliveryStream = field("deliveryStream")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FirehoseLogDeliveryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FirehoseLogDeliveryTypeDef"]
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
class ListConnectorOperationsRequest:
    boto3_raw_data: "type_defs.ListConnectorOperationsRequestTypeDef" = (
        dataclasses.field()
    )

    connectorArn = field("connectorArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConnectorOperationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorOperationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorsRequest:
    boto3_raw_data: "type_defs.ListConnectorsRequestTypeDef" = dataclasses.field()

    connectorNamePrefix = field("connectorNamePrefix")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomPluginsRequest:
    boto3_raw_data: "type_defs.ListCustomPluginsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    namePrefix = field("namePrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCustomPluginsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomPluginsRequestTypeDef"]
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
class ListWorkerConfigurationsRequest:
    boto3_raw_data: "type_defs.ListWorkerConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    namePrefix = field("namePrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkerConfigurationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkerConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3LogDeliveryDescription:
    boto3_raw_data: "type_defs.S3LogDeliveryDescriptionTypeDef" = dataclasses.field()

    bucket = field("bucket")
    enabled = field("enabled")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3LogDeliveryDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3LogDeliveryDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3LogDelivery:
    boto3_raw_data: "type_defs.S3LogDeliveryTypeDef" = dataclasses.field()

    enabled = field("enabled")
    bucket = field("bucket")
    prefix = field("prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LogDeliveryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LogDeliveryTypeDef"]],
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
class ApacheKafkaClusterDescription:
    boto3_raw_data: "type_defs.ApacheKafkaClusterDescriptionTypeDef" = (
        dataclasses.field()
    )

    bootstrapServers = field("bootstrapServers")

    @cached_property
    def vpc(self):  # pragma: no cover
        return VpcDescription.make_one(self.boto3_raw_data["vpc"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApacheKafkaClusterDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApacheKafkaClusterDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApacheKafkaCluster:
    boto3_raw_data: "type_defs.ApacheKafkaClusterTypeDef" = dataclasses.field()

    bootstrapServers = field("bootstrapServers")

    @cached_property
    def vpc(self):  # pragma: no cover
        return Vpc.make_one(self.boto3_raw_data["vpc"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApacheKafkaClusterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApacheKafkaClusterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingDescription:
    boto3_raw_data: "type_defs.AutoScalingDescriptionTypeDef" = dataclasses.field()

    maxWorkerCount = field("maxWorkerCount")
    mcuCount = field("mcuCount")
    minWorkerCount = field("minWorkerCount")

    @cached_property
    def scaleInPolicy(self):  # pragma: no cover
        return ScaleInPolicyDescription.make_one(self.boto3_raw_data["scaleInPolicy"])

    @cached_property
    def scaleOutPolicy(self):  # pragma: no cover
        return ScaleOutPolicyDescription.make_one(self.boto3_raw_data["scaleOutPolicy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoScalingDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScaling:
    boto3_raw_data: "type_defs.AutoScalingTypeDef" = dataclasses.field()

    maxWorkerCount = field("maxWorkerCount")
    mcuCount = field("mcuCount")
    minWorkerCount = field("minWorkerCount")

    @cached_property
    def scaleInPolicy(self):  # pragma: no cover
        return ScaleInPolicy.make_one(self.boto3_raw_data["scaleInPolicy"])

    @cached_property
    def scaleOutPolicy(self):  # pragma: no cover
        return ScaleOutPolicy.make_one(self.boto3_raw_data["scaleOutPolicy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoScalingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoScalingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingUpdate:
    boto3_raw_data: "type_defs.AutoScalingUpdateTypeDef" = dataclasses.field()

    maxWorkerCount = field("maxWorkerCount")
    mcuCount = field("mcuCount")
    minWorkerCount = field("minWorkerCount")

    @cached_property
    def scaleInPolicy(self):  # pragma: no cover
        return ScaleInPolicyUpdate.make_one(self.boto3_raw_data["scaleInPolicy"])

    @cached_property
    def scaleOutPolicy(self):  # pragma: no cover
        return ScaleOutPolicyUpdate.make_one(self.boto3_raw_data["scaleOutPolicy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoScalingUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorResponse:
    boto3_raw_data: "type_defs.CreateConnectorResponseTypeDef" = dataclasses.field()

    connectorArn = field("connectorArn")
    connectorName = field("connectorName")
    connectorState = field("connectorState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomPluginResponse:
    boto3_raw_data: "type_defs.CreateCustomPluginResponseTypeDef" = dataclasses.field()

    customPluginArn = field("customPluginArn")
    customPluginState = field("customPluginState")
    name = field("name")
    revision = field("revision")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomPluginResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomPluginResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectorResponse:
    boto3_raw_data: "type_defs.DeleteConnectorResponseTypeDef" = dataclasses.field()

    connectorArn = field("connectorArn")
    connectorState = field("connectorState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomPluginResponse:
    boto3_raw_data: "type_defs.DeleteCustomPluginResponseTypeDef" = dataclasses.field()

    customPluginArn = field("customPluginArn")
    customPluginState = field("customPluginState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCustomPluginResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomPluginResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkerConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteWorkerConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    workerConfigurationArn = field("workerConfigurationArn")
    workerConfigurationState = field("workerConfigurationState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteWorkerConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkerConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorOperationsResponse:
    boto3_raw_data: "type_defs.ListConnectorOperationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def connectorOperations(self):  # pragma: no cover
        return ConnectorOperationSummary.make_many(
            self.boto3_raw_data["connectorOperations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConnectorOperationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorOperationsResponseTypeDef"]
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
class UpdateConnectorResponse:
    boto3_raw_data: "type_defs.UpdateConnectorResponseTypeDef" = dataclasses.field()

    connectorArn = field("connectorArn")
    connectorState = field("connectorState")
    connectorOperationArn = field("connectorOperationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkerConfigurationResponse:
    boto3_raw_data: "type_defs.CreateWorkerConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    creationTime = field("creationTime")

    @cached_property
    def latestRevision(self):  # pragma: no cover
        return WorkerConfigurationRevisionSummary.make_one(
            self.boto3_raw_data["latestRevision"]
        )

    name = field("name")
    workerConfigurationArn = field("workerConfigurationArn")
    workerConfigurationState = field("workerConfigurationState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateWorkerConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkerConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerConfigurationSummary:
    boto3_raw_data: "type_defs.WorkerConfigurationSummaryTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    description = field("description")

    @cached_property
    def latestRevision(self):  # pragma: no cover
        return WorkerConfigurationRevisionSummary.make_one(
            self.boto3_raw_data["latestRevision"]
        )

    name = field("name")
    workerConfigurationArn = field("workerConfigurationArn")
    workerConfigurationState = field("workerConfigurationState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerConfigurationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PluginDescription:
    boto3_raw_data: "type_defs.PluginDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def customPlugin(self):  # pragma: no cover
        return CustomPluginDescription.make_one(self.boto3_raw_data["customPlugin"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PluginDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PluginDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomPluginLocationDescription:
    boto3_raw_data: "type_defs.CustomPluginLocationDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3LocationDescription.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomPluginLocationDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomPluginLocationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomPluginLocation:
    boto3_raw_data: "type_defs.CustomPluginLocationTypeDef" = dataclasses.field()

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["s3Location"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomPluginLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomPluginLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Plugin:
    boto3_raw_data: "type_defs.PluginTypeDef" = dataclasses.field()

    @cached_property
    def customPlugin(self):  # pragma: no cover
        return CustomPlugin.make_one(self.boto3_raw_data["customPlugin"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PluginTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PluginTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkerConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeWorkerConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    creationTime = field("creationTime")
    description = field("description")

    @cached_property
    def latestRevision(self):  # pragma: no cover
        return WorkerConfigurationRevisionDescription.make_one(
            self.boto3_raw_data["latestRevision"]
        )

    name = field("name")
    workerConfigurationArn = field("workerConfigurationArn")
    workerConfigurationState = field("workerConfigurationState")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkerConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkerConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorOperationsRequestPaginate:
    boto3_raw_data: "type_defs.ListConnectorOperationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    connectorArn = field("connectorArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConnectorOperationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorOperationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorsRequestPaginate:
    boto3_raw_data: "type_defs.ListConnectorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    connectorNamePrefix = field("connectorNamePrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConnectorsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomPluginsRequestPaginate:
    boto3_raw_data: "type_defs.ListCustomPluginsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    namePrefix = field("namePrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCustomPluginsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomPluginsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkerConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkerConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    namePrefix = field("namePrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkerConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkerConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerLogDeliveryDescription:
    boto3_raw_data: "type_defs.WorkerLogDeliveryDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def cloudWatchLogs(self):  # pragma: no cover
        return CloudWatchLogsLogDeliveryDescription.make_one(
            self.boto3_raw_data["cloudWatchLogs"]
        )

    @cached_property
    def firehose(self):  # pragma: no cover
        return FirehoseLogDeliveryDescription.make_one(self.boto3_raw_data["firehose"])

    @cached_property
    def s3(self):  # pragma: no cover
        return S3LogDeliveryDescription.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerLogDeliveryDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerLogDeliveryDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerLogDelivery:
    boto3_raw_data: "type_defs.WorkerLogDeliveryTypeDef" = dataclasses.field()

    @cached_property
    def cloudWatchLogs(self):  # pragma: no cover
        return CloudWatchLogsLogDelivery.make_one(self.boto3_raw_data["cloudWatchLogs"])

    @cached_property
    def firehose(self):  # pragma: no cover
        return FirehoseLogDelivery.make_one(self.boto3_raw_data["firehose"])

    @cached_property
    def s3(self):  # pragma: no cover
        return S3LogDelivery.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkerLogDeliveryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerLogDeliveryTypeDef"]
        ],
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
    def apacheKafkaCluster(self):  # pragma: no cover
        return ApacheKafkaClusterDescription.make_one(
            self.boto3_raw_data["apacheKafkaCluster"]
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
class KafkaCluster:
    boto3_raw_data: "type_defs.KafkaClusterTypeDef" = dataclasses.field()

    @cached_property
    def apacheKafkaCluster(self):  # pragma: no cover
        return ApacheKafkaCluster.make_one(self.boto3_raw_data["apacheKafkaCluster"])

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
class CapacityDescription:
    boto3_raw_data: "type_defs.CapacityDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def autoScaling(self):  # pragma: no cover
        return AutoScalingDescription.make_one(self.boto3_raw_data["autoScaling"])

    @cached_property
    def provisionedCapacity(self):  # pragma: no cover
        return ProvisionedCapacityDescription.make_one(
            self.boto3_raw_data["provisionedCapacity"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Capacity:
    boto3_raw_data: "type_defs.CapacityTypeDef" = dataclasses.field()

    @cached_property
    def autoScaling(self):  # pragma: no cover
        return AutoScaling.make_one(self.boto3_raw_data["autoScaling"])

    @cached_property
    def provisionedCapacity(self):  # pragma: no cover
        return ProvisionedCapacity.make_one(self.boto3_raw_data["provisionedCapacity"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapacityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CapacityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityUpdate:
    boto3_raw_data: "type_defs.CapacityUpdateTypeDef" = dataclasses.field()

    @cached_property
    def autoScaling(self):  # pragma: no cover
        return AutoScalingUpdate.make_one(self.boto3_raw_data["autoScaling"])

    @cached_property
    def provisionedCapacity(self):  # pragma: no cover
        return ProvisionedCapacityUpdate.make_one(
            self.boto3_raw_data["provisionedCapacity"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapacityUpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CapacityUpdateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkerConfigurationsResponse:
    boto3_raw_data: "type_defs.ListWorkerConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def workerConfigurations(self):  # pragma: no cover
        return WorkerConfigurationSummary.make_many(
            self.boto3_raw_data["workerConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkerConfigurationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkerConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomPluginRevisionSummary:
    boto3_raw_data: "type_defs.CustomPluginRevisionSummaryTypeDef" = dataclasses.field()

    contentType = field("contentType")
    creationTime = field("creationTime")
    description = field("description")

    @cached_property
    def fileDescription(self):  # pragma: no cover
        return CustomPluginFileDescription.make_one(
            self.boto3_raw_data["fileDescription"]
        )

    @cached_property
    def location(self):  # pragma: no cover
        return CustomPluginLocationDescription.make_one(self.boto3_raw_data["location"])

    revision = field("revision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomPluginRevisionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomPluginRevisionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomPluginRequest:
    boto3_raw_data: "type_defs.CreateCustomPluginRequestTypeDef" = dataclasses.field()

    contentType = field("contentType")

    @cached_property
    def location(self):  # pragma: no cover
        return CustomPluginLocation.make_one(self.boto3_raw_data["location"])

    name = field("name")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomPluginRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomPluginRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogDeliveryDescription:
    boto3_raw_data: "type_defs.LogDeliveryDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def workerLogDelivery(self):  # pragma: no cover
        return WorkerLogDeliveryDescription.make_one(
            self.boto3_raw_data["workerLogDelivery"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LogDeliveryDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LogDeliveryDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogDelivery:
    boto3_raw_data: "type_defs.LogDeliveryTypeDef" = dataclasses.field()

    @cached_property
    def workerLogDelivery(self):  # pragma: no cover
        return WorkerLogDelivery.make_one(self.boto3_raw_data["workerLogDelivery"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogDeliveryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogDeliveryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerSetting:
    boto3_raw_data: "type_defs.WorkerSettingTypeDef" = dataclasses.field()

    @cached_property
    def capacity(self):  # pragma: no cover
        return CapacityDescription.make_one(self.boto3_raw_data["capacity"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkerSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkerSettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectorRequest:
    boto3_raw_data: "type_defs.UpdateConnectorRequestTypeDef" = dataclasses.field()

    connectorArn = field("connectorArn")
    currentVersion = field("currentVersion")

    @cached_property
    def capacity(self):  # pragma: no cover
        return CapacityUpdate.make_one(self.boto3_raw_data["capacity"])

    connectorConfiguration = field("connectorConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomPluginSummary:
    boto3_raw_data: "type_defs.CustomPluginSummaryTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    customPluginArn = field("customPluginArn")
    customPluginState = field("customPluginState")
    description = field("description")

    @cached_property
    def latestRevision(self):  # pragma: no cover
        return CustomPluginRevisionSummary.make_one(
            self.boto3_raw_data["latestRevision"]
        )

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomPluginSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomPluginSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomPluginResponse:
    boto3_raw_data: "type_defs.DescribeCustomPluginResponseTypeDef" = (
        dataclasses.field()
    )

    creationTime = field("creationTime")
    customPluginArn = field("customPluginArn")
    customPluginState = field("customPluginState")
    description = field("description")

    @cached_property
    def latestRevision(self):  # pragma: no cover
        return CustomPluginRevisionSummary.make_one(
            self.boto3_raw_data["latestRevision"]
        )

    name = field("name")

    @cached_property
    def stateDescription(self):  # pragma: no cover
        return StateDescription.make_one(self.boto3_raw_data["stateDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCustomPluginResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomPluginResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorSummary:
    boto3_raw_data: "type_defs.ConnectorSummaryTypeDef" = dataclasses.field()

    @cached_property
    def capacity(self):  # pragma: no cover
        return CapacityDescription.make_one(self.boto3_raw_data["capacity"])

    connectorArn = field("connectorArn")
    connectorDescription = field("connectorDescription")
    connectorName = field("connectorName")
    connectorState = field("connectorState")
    creationTime = field("creationTime")
    currentVersion = field("currentVersion")

    @cached_property
    def kafkaCluster(self):  # pragma: no cover
        return KafkaClusterDescription.make_one(self.boto3_raw_data["kafkaCluster"])

    @cached_property
    def kafkaClusterClientAuthentication(self):  # pragma: no cover
        return KafkaClusterClientAuthenticationDescription.make_one(
            self.boto3_raw_data["kafkaClusterClientAuthentication"]
        )

    @cached_property
    def kafkaClusterEncryptionInTransit(self):  # pragma: no cover
        return KafkaClusterEncryptionInTransitDescription.make_one(
            self.boto3_raw_data["kafkaClusterEncryptionInTransit"]
        )

    kafkaConnectVersion = field("kafkaConnectVersion")

    @cached_property
    def logDelivery(self):  # pragma: no cover
        return LogDeliveryDescription.make_one(self.boto3_raw_data["logDelivery"])

    @cached_property
    def plugins(self):  # pragma: no cover
        return PluginDescription.make_many(self.boto3_raw_data["plugins"])

    serviceExecutionRoleArn = field("serviceExecutionRoleArn")

    @cached_property
    def workerConfiguration(self):  # pragma: no cover
        return WorkerConfigurationDescription.make_one(
            self.boto3_raw_data["workerConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectorSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorResponse:
    boto3_raw_data: "type_defs.DescribeConnectorResponseTypeDef" = dataclasses.field()

    @cached_property
    def capacity(self):  # pragma: no cover
        return CapacityDescription.make_one(self.boto3_raw_data["capacity"])

    connectorArn = field("connectorArn")
    connectorConfiguration = field("connectorConfiguration")
    connectorDescription = field("connectorDescription")
    connectorName = field("connectorName")
    connectorState = field("connectorState")
    creationTime = field("creationTime")
    currentVersion = field("currentVersion")

    @cached_property
    def kafkaCluster(self):  # pragma: no cover
        return KafkaClusterDescription.make_one(self.boto3_raw_data["kafkaCluster"])

    @cached_property
    def kafkaClusterClientAuthentication(self):  # pragma: no cover
        return KafkaClusterClientAuthenticationDescription.make_one(
            self.boto3_raw_data["kafkaClusterClientAuthentication"]
        )

    @cached_property
    def kafkaClusterEncryptionInTransit(self):  # pragma: no cover
        return KafkaClusterEncryptionInTransitDescription.make_one(
            self.boto3_raw_data["kafkaClusterEncryptionInTransit"]
        )

    kafkaConnectVersion = field("kafkaConnectVersion")

    @cached_property
    def logDelivery(self):  # pragma: no cover
        return LogDeliveryDescription.make_one(self.boto3_raw_data["logDelivery"])

    @cached_property
    def plugins(self):  # pragma: no cover
        return PluginDescription.make_many(self.boto3_raw_data["plugins"])

    serviceExecutionRoleArn = field("serviceExecutionRoleArn")

    @cached_property
    def workerConfiguration(self):  # pragma: no cover
        return WorkerConfigurationDescription.make_one(
            self.boto3_raw_data["workerConfiguration"]
        )

    @cached_property
    def stateDescription(self):  # pragma: no cover
        return StateDescription.make_one(self.boto3_raw_data["stateDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorRequest:
    boto3_raw_data: "type_defs.CreateConnectorRequestTypeDef" = dataclasses.field()

    @cached_property
    def capacity(self):  # pragma: no cover
        return Capacity.make_one(self.boto3_raw_data["capacity"])

    connectorConfiguration = field("connectorConfiguration")
    connectorName = field("connectorName")

    @cached_property
    def kafkaCluster(self):  # pragma: no cover
        return KafkaCluster.make_one(self.boto3_raw_data["kafkaCluster"])

    @cached_property
    def kafkaClusterClientAuthentication(self):  # pragma: no cover
        return KafkaClusterClientAuthentication.make_one(
            self.boto3_raw_data["kafkaClusterClientAuthentication"]
        )

    @cached_property
    def kafkaClusterEncryptionInTransit(self):  # pragma: no cover
        return KafkaClusterEncryptionInTransit.make_one(
            self.boto3_raw_data["kafkaClusterEncryptionInTransit"]
        )

    kafkaConnectVersion = field("kafkaConnectVersion")

    @cached_property
    def plugins(self):  # pragma: no cover
        return Plugin.make_many(self.boto3_raw_data["plugins"])

    serviceExecutionRoleArn = field("serviceExecutionRoleArn")
    connectorDescription = field("connectorDescription")

    @cached_property
    def logDelivery(self):  # pragma: no cover
        return LogDelivery.make_one(self.boto3_raw_data["logDelivery"])

    @cached_property
    def workerConfiguration(self):  # pragma: no cover
        return WorkerConfiguration.make_one(self.boto3_raw_data["workerConfiguration"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorOperationResponse:
    boto3_raw_data: "type_defs.DescribeConnectorOperationResponseTypeDef" = (
        dataclasses.field()
    )

    connectorArn = field("connectorArn")
    connectorOperationArn = field("connectorOperationArn")
    connectorOperationState = field("connectorOperationState")
    connectorOperationType = field("connectorOperationType")

    @cached_property
    def operationSteps(self):  # pragma: no cover
        return ConnectorOperationStep.make_many(self.boto3_raw_data["operationSteps"])

    @cached_property
    def originWorkerSetting(self):  # pragma: no cover
        return WorkerSetting.make_one(self.boto3_raw_data["originWorkerSetting"])

    originConnectorConfiguration = field("originConnectorConfiguration")

    @cached_property
    def targetWorkerSetting(self):  # pragma: no cover
        return WorkerSetting.make_one(self.boto3_raw_data["targetWorkerSetting"])

    targetConnectorConfiguration = field("targetConnectorConfiguration")

    @cached_property
    def errorInfo(self):  # pragma: no cover
        return StateDescription.make_one(self.boto3_raw_data["errorInfo"])

    creationTime = field("creationTime")
    endTime = field("endTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConnectorOperationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorOperationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomPluginsResponse:
    boto3_raw_data: "type_defs.ListCustomPluginsResponseTypeDef" = dataclasses.field()

    @cached_property
    def customPlugins(self):  # pragma: no cover
        return CustomPluginSummary.make_many(self.boto3_raw_data["customPlugins"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCustomPluginsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomPluginsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorsResponse:
    boto3_raw_data: "type_defs.ListConnectorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def connectors(self):  # pragma: no cover
        return ConnectorSummary.make_many(self.boto3_raw_data["connectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
