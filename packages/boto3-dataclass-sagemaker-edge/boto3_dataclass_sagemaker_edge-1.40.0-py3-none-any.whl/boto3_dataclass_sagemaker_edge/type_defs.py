# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sagemaker_edge import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Checksum:
    boto3_raw_data: "type_defs.ChecksumTypeDef" = dataclasses.field()

    Type = field("Type")
    Sum = field("Sum")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChecksumTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChecksumTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentModel:
    boto3_raw_data: "type_defs.DeploymentModelTypeDef" = dataclasses.field()

    ModelHandle = field("ModelHandle")
    ModelName = field("ModelName")
    ModelVersion = field("ModelVersion")
    DesiredState = field("DesiredState")
    State = field("State")
    Status = field("Status")
    StatusReason = field("StatusReason")
    RollbackFailureReason = field("RollbackFailureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentModelTypeDef"]],
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
class GetDeploymentsRequest:
    boto3_raw_data: "type_defs.GetDeploymentsRequestTypeDef" = dataclasses.field()

    DeviceName = field("DeviceName")
    DeviceFleetName = field("DeviceFleetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeviceRegistrationRequest:
    boto3_raw_data: "type_defs.GetDeviceRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    DeviceName = field("DeviceName")
    DeviceFleetName = field("DeviceFleetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeviceRegistrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeviceRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Definition:
    boto3_raw_data: "type_defs.DefinitionTypeDef" = dataclasses.field()

    ModelHandle = field("ModelHandle")
    S3Url = field("S3Url")

    @cached_property
    def Checksum(self):  # pragma: no cover
        return Checksum.make_one(self.boto3_raw_data["Checksum"])

    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DefinitionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentResult:
    boto3_raw_data: "type_defs.DeploymentResultTypeDef" = dataclasses.field()

    DeploymentName = field("DeploymentName")
    DeploymentStatus = field("DeploymentStatus")
    DeploymentStatusMessage = field("DeploymentStatusMessage")
    DeploymentStartTime = field("DeploymentStartTime")
    DeploymentEndTime = field("DeploymentEndTime")

    @cached_property
    def DeploymentModels(self):  # pragma: no cover
        return DeploymentModel.make_many(self.boto3_raw_data["DeploymentModels"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EdgeMetric:
    boto3_raw_data: "type_defs.EdgeMetricTypeDef" = dataclasses.field()

    Dimension = field("Dimension")
    MetricName = field("MetricName")
    Value = field("Value")
    Timestamp = field("Timestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdgeMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EdgeMetricTypeDef"]]
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
class GetDeviceRegistrationResult:
    boto3_raw_data: "type_defs.GetDeviceRegistrationResultTypeDef" = dataclasses.field()

    DeviceRegistration = field("DeviceRegistration")
    CacheTTL = field("CacheTTL")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeviceRegistrationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeviceRegistrationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EdgeDeployment:
    boto3_raw_data: "type_defs.EdgeDeploymentTypeDef" = dataclasses.field()

    DeploymentName = field("DeploymentName")
    Type = field("Type")
    FailureHandlingPolicy = field("FailureHandlingPolicy")

    @cached_property
    def Definitions(self):  # pragma: no cover
        return Definition.make_many(self.boto3_raw_data["Definitions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdgeDeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EdgeDeploymentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Model:
    boto3_raw_data: "type_defs.ModelTypeDef" = dataclasses.field()

    ModelName = field("ModelName")
    ModelVersion = field("ModelVersion")
    LatestSampleTime = field("LatestSampleTime")
    LatestInference = field("LatestInference")

    @cached_property
    def ModelMetrics(self):  # pragma: no cover
        return EdgeMetric.make_many(self.boto3_raw_data["ModelMetrics"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentsResult:
    boto3_raw_data: "type_defs.GetDeploymentsResultTypeDef" = dataclasses.field()

    @cached_property
    def Deployments(self):  # pragma: no cover
        return EdgeDeployment.make_many(self.boto3_raw_data["Deployments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendHeartbeatRequest:
    boto3_raw_data: "type_defs.SendHeartbeatRequestTypeDef" = dataclasses.field()

    AgentVersion = field("AgentVersion")
    DeviceName = field("DeviceName")
    DeviceFleetName = field("DeviceFleetName")

    @cached_property
    def AgentMetrics(self):  # pragma: no cover
        return EdgeMetric.make_many(self.boto3_raw_data["AgentMetrics"])

    @cached_property
    def Models(self):  # pragma: no cover
        return Model.make_many(self.boto3_raw_data["Models"])

    @cached_property
    def DeploymentResult(self):  # pragma: no cover
        return DeploymentResult.make_one(self.boto3_raw_data["DeploymentResult"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendHeartbeatRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendHeartbeatRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
