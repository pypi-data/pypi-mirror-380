# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotfleetwise import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActuatorOutput:
    boto3_raw_data: "type_defs.ActuatorOutputTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    dataType = field("dataType")
    description = field("description")
    unit = field("unit")
    allowedValues = field("allowedValues")
    min = field("min")
    max = field("max")
    assignedValue = field("assignedValue")
    deprecationMessage = field("deprecationMessage")
    comment = field("comment")
    structFullyQualifiedName = field("structFullyQualifiedName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActuatorOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActuatorOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Actuator:
    boto3_raw_data: "type_defs.ActuatorTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    dataType = field("dataType")
    description = field("description")
    unit = field("unit")
    allowedValues = field("allowedValues")
    min = field("min")
    max = field("max")
    assignedValue = field("assignedValue")
    deprecationMessage = field("deprecationMessage")
    comment = field("comment")
    structFullyQualifiedName = field("structFullyQualifiedName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActuatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActuatorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateVehicleFleetRequest:
    boto3_raw_data: "type_defs.AssociateVehicleFleetRequestTypeDef" = (
        dataclasses.field()
    )

    vehicleName = field("vehicleName")
    fleetId = field("fleetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateVehicleFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateVehicleFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeOutput:
    boto3_raw_data: "type_defs.AttributeOutputTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    dataType = field("dataType")
    description = field("description")
    unit = field("unit")
    allowedValues = field("allowedValues")
    min = field("min")
    max = field("max")
    assignedValue = field("assignedValue")
    defaultValue = field("defaultValue")
    deprecationMessage = field("deprecationMessage")
    comment = field("comment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Attribute:
    boto3_raw_data: "type_defs.AttributeTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    dataType = field("dataType")
    description = field("description")
    unit = field("unit")
    allowedValues = field("allowedValues")
    min = field("min")
    max = field("max")
    assignedValue = field("assignedValue")
    defaultValue = field("defaultValue")
    deprecationMessage = field("deprecationMessage")
    comment = field("comment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVehicleError:
    boto3_raw_data: "type_defs.CreateVehicleErrorTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVehicleErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVehicleErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVehicleResponseItem:
    boto3_raw_data: "type_defs.CreateVehicleResponseItemTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    arn = field("arn")
    thingArn = field("thingArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVehicleResponseItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVehicleResponseItemTypeDef"]
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
class UpdateVehicleError:
    boto3_raw_data: "type_defs.UpdateVehicleErrorTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVehicleErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVehicleErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVehicleResponseItem:
    boto3_raw_data: "type_defs.UpdateVehicleResponseItemTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVehicleResponseItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVehicleResponseItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Branch:
    boto3_raw_data: "type_defs.BranchTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    description = field("description")
    deprecationMessage = field("deprecationMessage")
    comment = field("comment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BranchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BranchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignSummary:
    boto3_raw_data: "type_defs.CampaignSummaryTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")
    arn = field("arn")
    name = field("name")
    description = field("description")
    signalCatalogArn = field("signalCatalogArn")
    targetArn = field("targetArn")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CampaignSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanInterface:
    boto3_raw_data: "type_defs.CanInterfaceTypeDef" = dataclasses.field()

    name = field("name")
    protocolName = field("protocolName")
    protocolVersion = field("protocolVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CanInterfaceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanSignal:
    boto3_raw_data: "type_defs.CanSignalTypeDef" = dataclasses.field()

    messageId = field("messageId")
    isBigEndian = field("isBigEndian")
    isSigned = field("isSigned")
    startBit = field("startBit")
    offset = field("offset")
    factor = field("factor")
    length = field("length")
    name = field("name")
    signalValueType = field("signalValueType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanSignalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CanSignalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogDeliveryOptions:
    boto3_raw_data: "type_defs.CloudWatchLogDeliveryOptionsTypeDef" = (
        dataclasses.field()
    )

    logType = field("logType")
    logGroupName = field("logGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchLogDeliveryOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogDeliveryOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionBasedCollectionScheme:
    boto3_raw_data: "type_defs.ConditionBasedCollectionSchemeTypeDef" = (
        dataclasses.field()
    )

    expression = field("expression")
    minimumTriggerIntervalMs = field("minimumTriggerIntervalMs")
    triggerMode = field("triggerMode")
    conditionLanguageVersion = field("conditionLanguageVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConditionBasedCollectionSchemeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionBasedCollectionSchemeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeBasedCollectionScheme:
    boto3_raw_data: "type_defs.TimeBasedCollectionSchemeTypeDef" = dataclasses.field()

    periodMs = field("periodMs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeBasedCollectionSchemeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeBasedCollectionSchemeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionBasedSignalFetchConfig:
    boto3_raw_data: "type_defs.ConditionBasedSignalFetchConfigTypeDef" = (
        dataclasses.field()
    )

    conditionExpression = field("conditionExpression")
    triggerMode = field("triggerMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConditionBasedSignalFetchConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionBasedSignalFetchConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalInformation:
    boto3_raw_data: "type_defs.SignalInformationTypeDef" = dataclasses.field()

    name = field("name")
    maxSampleCount = field("maxSampleCount")
    minimumSamplingIntervalMs = field("minimumSamplingIntervalMs")
    dataPartitionId = field("dataPartitionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignalInformationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignalInformationTypeDef"]
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
class CustomDecodingInterface:
    boto3_raw_data: "type_defs.CustomDecodingInterfaceTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomDecodingInterfaceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDecodingInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomDecodingSignal:
    boto3_raw_data: "type_defs.CustomDecodingSignalTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomDecodingSignalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomDecodingSignalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomProperty:
    boto3_raw_data: "type_defs.CustomPropertyTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    dataType = field("dataType")
    dataEncoding = field("dataEncoding")
    description = field("description")
    deprecationMessage = field("deprecationMessage")
    comment = field("comment")
    structFullyQualifiedName = field("structFullyQualifiedName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomPropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomPropertyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomStruct:
    boto3_raw_data: "type_defs.CustomStructTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    description = field("description")
    deprecationMessage = field("deprecationMessage")
    comment = field("comment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomStructTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomStructTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MqttTopicConfig:
    boto3_raw_data: "type_defs.MqttTopicConfigTypeDef" = dataclasses.field()

    mqttTopicArn = field("mqttTopicArn")
    executionRoleArn = field("executionRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MqttTopicConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MqttTopicConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Config:
    boto3_raw_data: "type_defs.S3ConfigTypeDef" = dataclasses.field()

    bucketArn = field("bucketArn")
    dataFormat = field("dataFormat")
    storageCompressionFormat = field("storageCompressionFormat")
    prefix = field("prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestreamConfig:
    boto3_raw_data: "type_defs.TimestreamConfigTypeDef" = dataclasses.field()

    timestreamTableArn = field("timestreamTableArn")
    executionRoleArn = field("executionRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimestreamConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestreamConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageMaximumSize:
    boto3_raw_data: "type_defs.StorageMaximumSizeTypeDef" = dataclasses.field()

    unit = field("unit")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageMaximumSizeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageMaximumSizeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageMinimumTimeToLive:
    boto3_raw_data: "type_defs.StorageMinimumTimeToLiveTypeDef" = dataclasses.field()

    unit = field("unit")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageMinimumTimeToLiveTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageMinimumTimeToLiveTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataPartitionUploadOptions:
    boto3_raw_data: "type_defs.DataPartitionUploadOptionsTypeDef" = dataclasses.field()

    expression = field("expression")
    conditionLanguageVersion = field("conditionLanguageVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataPartitionUploadOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataPartitionUploadOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecoderManifestSummary:
    boto3_raw_data: "type_defs.DecoderManifestSummaryTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")
    name = field("name")
    arn = field("arn")
    modelManifestArn = field("modelManifestArn")
    description = field("description")
    status = field("status")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DecoderManifestSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecoderManifestSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCampaignRequest:
    boto3_raw_data: "type_defs.DeleteCampaignRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDecoderManifestRequest:
    boto3_raw_data: "type_defs.DeleteDecoderManifestRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDecoderManifestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDecoderManifestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetRequest:
    boto3_raw_data: "type_defs.DeleteFleetRequestTypeDef" = dataclasses.field()

    fleetId = field("fleetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteModelManifestRequest:
    boto3_raw_data: "type_defs.DeleteModelManifestRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteModelManifestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteModelManifestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSignalCatalogRequest:
    boto3_raw_data: "type_defs.DeleteSignalCatalogRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSignalCatalogRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSignalCatalogRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStateTemplateRequest:
    boto3_raw_data: "type_defs.DeleteStateTemplateRequestTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStateTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVehicleRequest:
    boto3_raw_data: "type_defs.DeleteVehicleRequestTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVehicleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVehicleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateVehicleFleetRequest:
    boto3_raw_data: "type_defs.DisassociateVehicleFleetRequestTypeDef" = (
        dataclasses.field()
    )

    vehicleName = field("vehicleName")
    fleetId = field("fleetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateVehicleFleetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateVehicleFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetSummary:
    boto3_raw_data: "type_defs.FleetSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    signalCatalogArn = field("signalCatalogArn")
    creationTime = field("creationTime")
    description = field("description")
    lastModificationTime = field("lastModificationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FleetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FleetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormattedVss:
    boto3_raw_data: "type_defs.FormattedVssTypeDef" = dataclasses.field()

    vssJson = field("vssJson")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormattedVssTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormattedVssTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignRequest:
    boto3_raw_data: "type_defs.GetCampaignRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDecoderManifestRequest:
    boto3_raw_data: "type_defs.GetDecoderManifestRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDecoderManifestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDecoderManifestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFleetRequest:
    boto3_raw_data: "type_defs.GetFleetRequestTypeDef" = dataclasses.field()

    fleetId = field("fleetId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFleetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFleetRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelManifestRequest:
    boto3_raw_data: "type_defs.GetModelManifestRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelManifestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelManifestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamRegistrationResponse:
    boto3_raw_data: "type_defs.IamRegistrationResponseTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    registrationStatus = field("registrationStatus")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamRegistrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamRegistrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestreamRegistrationResponse:
    boto3_raw_data: "type_defs.TimestreamRegistrationResponseTypeDef" = (
        dataclasses.field()
    )

    timestreamDatabaseName = field("timestreamDatabaseName")
    timestreamTableName = field("timestreamTableName")
    registrationStatus = field("registrationStatus")
    timestreamDatabaseArn = field("timestreamDatabaseArn")
    timestreamTableArn = field("timestreamTableArn")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TimestreamRegistrationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestreamRegistrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSignalCatalogRequest:
    boto3_raw_data: "type_defs.GetSignalCatalogRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSignalCatalogRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSignalCatalogRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeCounts:
    boto3_raw_data: "type_defs.NodeCountsTypeDef" = dataclasses.field()

    totalNodes = field("totalNodes")
    totalBranches = field("totalBranches")
    totalSensors = field("totalSensors")
    totalAttributes = field("totalAttributes")
    totalActuators = field("totalActuators")
    totalStructs = field("totalStructs")
    totalProperties = field("totalProperties")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeCountsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeCountsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStateTemplateRequest:
    boto3_raw_data: "type_defs.GetStateTemplateRequestTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStateTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVehicleRequest:
    boto3_raw_data: "type_defs.GetVehicleRequestTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetVehicleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVehicleRequestTypeDef"]
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
class GetVehicleStatusRequest:
    boto3_raw_data: "type_defs.GetVehicleStatusRequestTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVehicleStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVehicleStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VehicleStatus:
    boto3_raw_data: "type_defs.VehicleStatusTypeDef" = dataclasses.field()

    campaignName = field("campaignName")
    vehicleName = field("vehicleName")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VehicleStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VehicleStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamResources:
    boto3_raw_data: "type_defs.IamResourcesTypeDef" = dataclasses.field()

    roleArn = field("roleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IamResourcesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IamResourcesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCampaignsRequest:
    boto3_raw_data: "type_defs.ListCampaignsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    status = field("status")
    listResponseScope = field("listResponseScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCampaignsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCampaignsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDecoderManifestNetworkInterfacesRequest:
    boto3_raw_data: "type_defs.ListDecoderManifestNetworkInterfacesRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDecoderManifestNetworkInterfacesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDecoderManifestNetworkInterfacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDecoderManifestSignalsRequest:
    boto3_raw_data: "type_defs.ListDecoderManifestSignalsRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDecoderManifestSignalsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDecoderManifestSignalsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDecoderManifestsRequest:
    boto3_raw_data: "type_defs.ListDecoderManifestsRequestTypeDef" = dataclasses.field()

    modelManifestArn = field("modelManifestArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    listResponseScope = field("listResponseScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDecoderManifestsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDecoderManifestsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsForVehicleRequest:
    boto3_raw_data: "type_defs.ListFleetsForVehicleRequestTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetsForVehicleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsForVehicleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsRequest:
    boto3_raw_data: "type_defs.ListFleetsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    listResponseScope = field("listResponseScope")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFleetsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelManifestNodesRequest:
    boto3_raw_data: "type_defs.ListModelManifestNodesRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListModelManifestNodesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelManifestNodesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelManifestsRequest:
    boto3_raw_data: "type_defs.ListModelManifestsRequestTypeDef" = dataclasses.field()

    signalCatalogArn = field("signalCatalogArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    listResponseScope = field("listResponseScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListModelManifestsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelManifestsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelManifestSummary:
    boto3_raw_data: "type_defs.ModelManifestSummaryTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")
    name = field("name")
    arn = field("arn")
    signalCatalogArn = field("signalCatalogArn")
    description = field("description")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelManifestSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelManifestSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalCatalogNodesRequest:
    boto3_raw_data: "type_defs.ListSignalCatalogNodesRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    signalNodeType = field("signalNodeType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSignalCatalogNodesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalCatalogNodesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalCatalogsRequest:
    boto3_raw_data: "type_defs.ListSignalCatalogsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSignalCatalogsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalCatalogsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalCatalogSummary:
    boto3_raw_data: "type_defs.SignalCatalogSummaryTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignalCatalogSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignalCatalogSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStateTemplatesRequest:
    boto3_raw_data: "type_defs.ListStateTemplatesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    listResponseScope = field("listResponseScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStateTemplatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStateTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateTemplateSummary:
    boto3_raw_data: "type_defs.StateTemplateSummaryTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    signalCatalogArn = field("signalCatalogArn")
    description = field("description")
    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StateTemplateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateTemplateSummaryTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class ListVehiclesInFleetRequest:
    boto3_raw_data: "type_defs.ListVehiclesInFleetRequestTypeDef" = dataclasses.field()

    fleetId = field("fleetId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVehiclesInFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVehiclesInFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVehiclesRequest:
    boto3_raw_data: "type_defs.ListVehiclesRequestTypeDef" = dataclasses.field()

    modelManifestArn = field("modelManifestArn")
    attributeNames = field("attributeNames")
    attributeValues = field("attributeValues")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    listResponseScope = field("listResponseScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVehiclesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVehiclesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VehicleSummary:
    boto3_raw_data: "type_defs.VehicleSummaryTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    arn = field("arn")
    modelManifestArn = field("modelManifestArn")
    decoderManifestArn = field("decoderManifestArn")
    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")
    attributes = field("attributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VehicleSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VehicleSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObdInterface:
    boto3_raw_data: "type_defs.ObdInterfaceTypeDef" = dataclasses.field()

    name = field("name")
    requestMessageId = field("requestMessageId")
    obdStandard = field("obdStandard")
    pidRequestIntervalSeconds = field("pidRequestIntervalSeconds")
    dtcRequestIntervalSeconds = field("dtcRequestIntervalSeconds")
    useExtendedIds = field("useExtendedIds")
    hasTransmissionEcu = field("hasTransmissionEcu")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObdInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObdInterfaceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VehicleMiddleware:
    boto3_raw_data: "type_defs.VehicleMiddlewareTypeDef" = dataclasses.field()

    name = field("name")
    protocolName = field("protocolName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VehicleMiddlewareTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VehicleMiddlewareTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SensorOutput:
    boto3_raw_data: "type_defs.SensorOutputTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    dataType = field("dataType")
    description = field("description")
    unit = field("unit")
    allowedValues = field("allowedValues")
    min = field("min")
    max = field("max")
    deprecationMessage = field("deprecationMessage")
    comment = field("comment")
    structFullyQualifiedName = field("structFullyQualifiedName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SensorOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SensorOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObdSignal:
    boto3_raw_data: "type_defs.ObdSignalTypeDef" = dataclasses.field()

    pidResponseLength = field("pidResponseLength")
    serviceMode = field("serviceMode")
    pid = field("pid")
    scaling = field("scaling")
    offset = field("offset")
    startByte = field("startByte")
    byteLength = field("byteLength")
    bitRightShift = field("bitRightShift")
    bitMaskLength = field("bitMaskLength")
    isSigned = field("isSigned")
    signalValueType = field("signalValueType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObdSignalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObdSignalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimePeriod:
    boto3_raw_data: "type_defs.TimePeriodTypeDef" = dataclasses.field()

    unit = field("unit")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimePeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimePeriodTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ROS2PrimitiveMessageDefinition:
    boto3_raw_data: "type_defs.ROS2PrimitiveMessageDefinitionTypeDef" = (
        dataclasses.field()
    )

    primitiveType = field("primitiveType")
    offset = field("offset")
    scaling = field("scaling")
    upperBound = field("upperBound")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ROS2PrimitiveMessageDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ROS2PrimitiveMessageDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEncryptionConfigurationRequest:
    boto3_raw_data: "type_defs.PutEncryptionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    encryptionType = field("encryptionType")
    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutEncryptionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEncryptionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestreamResources:
    boto3_raw_data: "type_defs.TimestreamResourcesTypeDef" = dataclasses.field()

    timestreamDatabaseName = field("timestreamDatabaseName")
    timestreamTableName = field("timestreamTableName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestreamResourcesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestreamResourcesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Sensor:
    boto3_raw_data: "type_defs.SensorTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    dataType = field("dataType")
    description = field("description")
    unit = field("unit")
    allowedValues = field("allowedValues")
    min = field("min")
    max = field("max")
    deprecationMessage = field("deprecationMessage")
    comment = field("comment")
    structFullyQualifiedName = field("structFullyQualifiedName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SensorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SensorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeBasedSignalFetchConfig:
    boto3_raw_data: "type_defs.TimeBasedSignalFetchConfigTypeDef" = dataclasses.field()

    executionFrequencyMs = field("executionFrequencyMs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeBasedSignalFetchConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeBasedSignalFetchConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StructuredMessageFieldNameAndDataTypePairOutput:
    boto3_raw_data: (
        "type_defs.StructuredMessageFieldNameAndDataTypePairOutputTypeDef"
    ) = dataclasses.field()

    fieldName = field("fieldName")
    dataType = field("dataType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StructuredMessageFieldNameAndDataTypePairOutputTypeDef"
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
                "type_defs.StructuredMessageFieldNameAndDataTypePairOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StructuredMessageFieldNameAndDataTypePairPaginator:
    boto3_raw_data: (
        "type_defs.StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef"
    ) = dataclasses.field()

    fieldName = field("fieldName")
    dataType = field("dataType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef"
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
                "type_defs.StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StructuredMessageFieldNameAndDataTypePair:
    boto3_raw_data: "type_defs.StructuredMessageFieldNameAndDataTypePairTypeDef" = (
        dataclasses.field()
    )

    fieldName = field("fieldName")
    dataType = field("dataType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StructuredMessageFieldNameAndDataTypePairTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StructuredMessageFieldNameAndDataTypePairTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StructuredMessageListDefinitionOutput:
    boto3_raw_data: "type_defs.StructuredMessageListDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    memberType = field("memberType")
    listType = field("listType")
    capacity = field("capacity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StructuredMessageListDefinitionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StructuredMessageListDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StructuredMessageListDefinitionPaginator:
    boto3_raw_data: "type_defs.StructuredMessageListDefinitionPaginatorTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    memberType = field("memberType")
    listType = field("listType")
    capacity = field("capacity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StructuredMessageListDefinitionPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StructuredMessageListDefinitionPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StructuredMessageListDefinition:
    boto3_raw_data: "type_defs.StructuredMessageListDefinitionTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    memberType = field("memberType")
    listType = field("listType")
    capacity = field("capacity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StructuredMessageListDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StructuredMessageListDefinitionTypeDef"]
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

    ResourceARN = field("ResourceARN")
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
class UpdateCampaignRequest:
    boto3_raw_data: "type_defs.UpdateCampaignRequestTypeDef" = dataclasses.field()

    name = field("name")
    action = field("action")
    description = field("description")
    dataExtraDimensions = field("dataExtraDimensions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetRequest:
    boto3_raw_data: "type_defs.UpdateFleetRequestTypeDef" = dataclasses.field()

    fleetId = field("fleetId")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateModelManifestRequest:
    boto3_raw_data: "type_defs.UpdateModelManifestRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    nodesToAdd = field("nodesToAdd")
    nodesToRemove = field("nodesToRemove")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateModelManifestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateModelManifestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStateTemplateRequest:
    boto3_raw_data: "type_defs.UpdateStateTemplateRequestTypeDef" = dataclasses.field()

    identifier = field("identifier")
    description = field("description")
    stateTemplatePropertiesToAdd = field("stateTemplatePropertiesToAdd")
    stateTemplatePropertiesToRemove = field("stateTemplatePropertiesToRemove")
    dataExtraDimensions = field("dataExtraDimensions")
    metadataExtraDimensions = field("metadataExtraDimensions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStateTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateVehicleResponse:
    boto3_raw_data: "type_defs.BatchCreateVehicleResponseTypeDef" = dataclasses.field()

    @cached_property
    def vehicles(self):  # pragma: no cover
        return CreateVehicleResponseItem.make_many(self.boto3_raw_data["vehicles"])

    @cached_property
    def errors(self):  # pragma: no cover
        return CreateVehicleError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchCreateVehicleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateVehicleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCampaignResponse:
    boto3_raw_data: "type_defs.CreateCampaignResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDecoderManifestResponse:
    boto3_raw_data: "type_defs.CreateDecoderManifestResponseTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDecoderManifestResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDecoderManifestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetResponse:
    boto3_raw_data: "type_defs.CreateFleetResponseTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFleetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelManifestResponse:
    boto3_raw_data: "type_defs.CreateModelManifestResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelManifestResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelManifestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSignalCatalogResponse:
    boto3_raw_data: "type_defs.CreateSignalCatalogResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSignalCatalogResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSignalCatalogResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStateTemplateResponse:
    boto3_raw_data: "type_defs.CreateStateTemplateResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStateTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStateTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVehicleResponse:
    boto3_raw_data: "type_defs.CreateVehicleResponseTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    arn = field("arn")
    thingArn = field("thingArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVehicleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVehicleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCampaignResponse:
    boto3_raw_data: "type_defs.DeleteCampaignResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDecoderManifestResponse:
    boto3_raw_data: "type_defs.DeleteDecoderManifestResponseTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDecoderManifestResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDecoderManifestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetResponse:
    boto3_raw_data: "type_defs.DeleteFleetResponseTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFleetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteModelManifestResponse:
    boto3_raw_data: "type_defs.DeleteModelManifestResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteModelManifestResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteModelManifestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSignalCatalogResponse:
    boto3_raw_data: "type_defs.DeleteSignalCatalogResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSignalCatalogResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSignalCatalogResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStateTemplateResponse:
    boto3_raw_data: "type_defs.DeleteStateTemplateResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStateTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStateTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVehicleResponse:
    boto3_raw_data: "type_defs.DeleteVehicleResponseTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVehicleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVehicleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDecoderManifestResponse:
    boto3_raw_data: "type_defs.GetDecoderManifestResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    description = field("description")
    modelManifestArn = field("modelManifestArn")
    status = field("status")
    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")
    message = field("message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDecoderManifestResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDecoderManifestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEncryptionConfigurationResponse:
    boto3_raw_data: "type_defs.GetEncryptionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    kmsKeyId = field("kmsKeyId")
    encryptionStatus = field("encryptionStatus")
    encryptionType = field("encryptionType")
    errorMessage = field("errorMessage")
    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEncryptionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEncryptionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFleetResponse:
    boto3_raw_data: "type_defs.GetFleetResponseTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    description = field("description")
    signalCatalogArn = field("signalCatalogArn")
    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFleetResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFleetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelManifestResponse:
    boto3_raw_data: "type_defs.GetModelManifestResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    description = field("description")
    signalCatalogArn = field("signalCatalogArn")
    status = field("status")
    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelManifestResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelManifestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStateTemplateResponse:
    boto3_raw_data: "type_defs.GetStateTemplateResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    description = field("description")
    signalCatalogArn = field("signalCatalogArn")
    stateTemplateProperties = field("stateTemplateProperties")
    dataExtraDimensions = field("dataExtraDimensions")
    metadataExtraDimensions = field("metadataExtraDimensions")
    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")
    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStateTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStateTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportDecoderManifestResponse:
    boto3_raw_data: "type_defs.ImportDecoderManifestResponseTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImportDecoderManifestResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDecoderManifestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportSignalCatalogResponse:
    boto3_raw_data: "type_defs.ImportSignalCatalogResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportSignalCatalogResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportSignalCatalogResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsForVehicleResponse:
    boto3_raw_data: "type_defs.ListFleetsForVehicleResponseTypeDef" = (
        dataclasses.field()
    )

    fleets = field("fleets")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetsForVehicleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsForVehicleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVehiclesInFleetResponse:
    boto3_raw_data: "type_defs.ListVehiclesInFleetResponseTypeDef" = dataclasses.field()

    vehicles = field("vehicles")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVehiclesInFleetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVehiclesInFleetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEncryptionConfigurationResponse:
    boto3_raw_data: "type_defs.PutEncryptionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    kmsKeyId = field("kmsKeyId")
    encryptionStatus = field("encryptionStatus")
    encryptionType = field("encryptionType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutEncryptionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEncryptionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignResponse:
    boto3_raw_data: "type_defs.UpdateCampaignResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDecoderManifestResponse:
    boto3_raw_data: "type_defs.UpdateDecoderManifestResponseTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDecoderManifestResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDecoderManifestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFleetResponse:
    boto3_raw_data: "type_defs.UpdateFleetResponseTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFleetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFleetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateModelManifestResponse:
    boto3_raw_data: "type_defs.UpdateModelManifestResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateModelManifestResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateModelManifestResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSignalCatalogResponse:
    boto3_raw_data: "type_defs.UpdateSignalCatalogResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSignalCatalogResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSignalCatalogResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStateTemplateResponse:
    boto3_raw_data: "type_defs.UpdateStateTemplateResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStateTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStateTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVehicleResponse:
    boto3_raw_data: "type_defs.UpdateVehicleResponseTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVehicleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVehicleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateVehicleResponse:
    boto3_raw_data: "type_defs.BatchUpdateVehicleResponseTypeDef" = dataclasses.field()

    @cached_property
    def vehicles(self):  # pragma: no cover
        return UpdateVehicleResponseItem.make_many(self.boto3_raw_data["vehicles"])

    @cached_property
    def errors(self):  # pragma: no cover
        return UpdateVehicleError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateVehicleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateVehicleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CanDbcDefinition:
    boto3_raw_data: "type_defs.CanDbcDefinitionTypeDef" = dataclasses.field()

    networkInterface = field("networkInterface")
    canDbcFiles = field("canDbcFiles")
    signalsMap = field("signalsMap")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CanDbcDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CanDbcDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCampaignsResponse:
    boto3_raw_data: "type_defs.ListCampaignsResponseTypeDef" = dataclasses.field()

    @cached_property
    def campaignSummaries(self):  # pragma: no cover
        return CampaignSummary.make_many(self.boto3_raw_data["campaignSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCampaignsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCampaignsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLoggingOptionsResponse:
    boto3_raw_data: "type_defs.GetLoggingOptionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def cloudWatchLogDelivery(self):  # pragma: no cover
        return CloudWatchLogDeliveryOptions.make_one(
            self.boto3_raw_data["cloudWatchLogDelivery"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLoggingOptionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLoggingOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLoggingOptionsRequest:
    boto3_raw_data: "type_defs.PutLoggingOptionsRequestTypeDef" = dataclasses.field()

    @cached_property
    def cloudWatchLogDelivery(self):  # pragma: no cover
        return CloudWatchLogDeliveryOptions.make_one(
            self.boto3_raw_data["cloudWatchLogDelivery"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutLoggingOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLoggingOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollectionScheme:
    boto3_raw_data: "type_defs.CollectionSchemeTypeDef" = dataclasses.field()

    @cached_property
    def timeBasedCollectionScheme(self):  # pragma: no cover
        return TimeBasedCollectionScheme.make_one(
            self.boto3_raw_data["timeBasedCollectionScheme"]
        )

    @cached_property
    def conditionBasedCollectionScheme(self):  # pragma: no cover
        return ConditionBasedCollectionScheme.make_one(
            self.boto3_raw_data["conditionBasedCollectionScheme"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CollectionSchemeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollectionSchemeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetRequest:
    boto3_raw_data: "type_defs.CreateFleetRequestTypeDef" = dataclasses.field()

    fleetId = field("fleetId")
    signalCatalogArn = field("signalCatalogArn")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFleetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelManifestRequest:
    boto3_raw_data: "type_defs.CreateModelManifestRequestTypeDef" = dataclasses.field()

    name = field("name")
    nodes = field("nodes")
    signalCatalogArn = field("signalCatalogArn")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelManifestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelManifestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStateTemplateRequest:
    boto3_raw_data: "type_defs.CreateStateTemplateRequestTypeDef" = dataclasses.field()

    name = field("name")
    signalCatalogArn = field("signalCatalogArn")
    stateTemplateProperties = field("stateTemplateProperties")
    description = field("description")
    dataExtraDimensions = field("dataExtraDimensions")
    metadataExtraDimensions = field("metadataExtraDimensions")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStateTemplateRequestTypeDef"]
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
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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

    ResourceARN = field("ResourceARN")

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
class DataDestinationConfig:
    boto3_raw_data: "type_defs.DataDestinationConfigTypeDef" = dataclasses.field()

    @cached_property
    def s3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["s3Config"])

    @cached_property
    def timestreamConfig(self):  # pragma: no cover
        return TimestreamConfig.make_one(self.boto3_raw_data["timestreamConfig"])

    @cached_property
    def mqttTopicConfig(self):  # pragma: no cover
        return MqttTopicConfig.make_one(self.boto3_raw_data["mqttTopicConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataDestinationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataDestinationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataPartitionStorageOptions:
    boto3_raw_data: "type_defs.DataPartitionStorageOptionsTypeDef" = dataclasses.field()

    @cached_property
    def maximumSize(self):  # pragma: no cover
        return StorageMaximumSize.make_one(self.boto3_raw_data["maximumSize"])

    storageLocation = field("storageLocation")

    @cached_property
    def minimumTimeToLive(self):  # pragma: no cover
        return StorageMinimumTimeToLive.make_one(
            self.boto3_raw_data["minimumTimeToLive"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataPartitionStorageOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataPartitionStorageOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDecoderManifestsResponse:
    boto3_raw_data: "type_defs.ListDecoderManifestsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def summaries(self):  # pragma: no cover
        return DecoderManifestSummary.make_many(self.boto3_raw_data["summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDecoderManifestsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDecoderManifestsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsResponse:
    boto3_raw_data: "type_defs.ListFleetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def fleetSummaries(self):  # pragma: no cover
        return FleetSummary.make_many(self.boto3_raw_data["fleetSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportSignalCatalogRequest:
    boto3_raw_data: "type_defs.ImportSignalCatalogRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def vss(self):  # pragma: no cover
        return FormattedVss.make_one(self.boto3_raw_data["vss"])

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportSignalCatalogRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportSignalCatalogRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRegisterAccountStatusResponse:
    boto3_raw_data: "type_defs.GetRegisterAccountStatusResponseTypeDef" = (
        dataclasses.field()
    )

    customerAccountId = field("customerAccountId")
    accountStatus = field("accountStatus")

    @cached_property
    def timestreamRegistrationResponse(self):  # pragma: no cover
        return TimestreamRegistrationResponse.make_one(
            self.boto3_raw_data["timestreamRegistrationResponse"]
        )

    @cached_property
    def iamRegistrationResponse(self):  # pragma: no cover
        return IamRegistrationResponse.make_one(
            self.boto3_raw_data["iamRegistrationResponse"]
        )

    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRegisterAccountStatusResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRegisterAccountStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSignalCatalogResponse:
    boto3_raw_data: "type_defs.GetSignalCatalogResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    description = field("description")

    @cached_property
    def nodeCounts(self):  # pragma: no cover
        return NodeCounts.make_one(self.boto3_raw_data["nodeCounts"])

    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSignalCatalogResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSignalCatalogResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVehicleStatusRequestPaginate:
    boto3_raw_data: "type_defs.GetVehicleStatusRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    vehicleName = field("vehicleName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetVehicleStatusRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVehicleStatusRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCampaignsRequestPaginate:
    boto3_raw_data: "type_defs.ListCampaignsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    listResponseScope = field("listResponseScope")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCampaignsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCampaignsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDecoderManifestNetworkInterfacesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListDecoderManifestNetworkInterfacesRequestPaginateTypeDef"
    ) = dataclasses.field()

    name = field("name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDecoderManifestNetworkInterfacesRequestPaginateTypeDef"
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
                "type_defs.ListDecoderManifestNetworkInterfacesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDecoderManifestSignalsRequestPaginate:
    boto3_raw_data: "type_defs.ListDecoderManifestSignalsRequestPaginateTypeDef" = (
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
            "type_defs.ListDecoderManifestSignalsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDecoderManifestSignalsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDecoderManifestsRequestPaginate:
    boto3_raw_data: "type_defs.ListDecoderManifestsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    modelManifestArn = field("modelManifestArn")
    listResponseScope = field("listResponseScope")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDecoderManifestsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDecoderManifestsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsForVehicleRequestPaginate:
    boto3_raw_data: "type_defs.ListFleetsForVehicleRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    vehicleName = field("vehicleName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFleetsForVehicleRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsForVehicleRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFleetsRequestPaginate:
    boto3_raw_data: "type_defs.ListFleetsRequestPaginateTypeDef" = dataclasses.field()

    listResponseScope = field("listResponseScope")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFleetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFleetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelManifestNodesRequestPaginate:
    boto3_raw_data: "type_defs.ListModelManifestNodesRequestPaginateTypeDef" = (
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
            "type_defs.ListModelManifestNodesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelManifestNodesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelManifestsRequestPaginate:
    boto3_raw_data: "type_defs.ListModelManifestsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    signalCatalogArn = field("signalCatalogArn")
    listResponseScope = field("listResponseScope")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListModelManifestsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelManifestsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalCatalogNodesRequestPaginate:
    boto3_raw_data: "type_defs.ListSignalCatalogNodesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    signalNodeType = field("signalNodeType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSignalCatalogNodesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalCatalogNodesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalCatalogsRequestPaginate:
    boto3_raw_data: "type_defs.ListSignalCatalogsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSignalCatalogsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalCatalogsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStateTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListStateTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    listResponseScope = field("listResponseScope")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStateTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStateTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVehiclesInFleetRequestPaginate:
    boto3_raw_data: "type_defs.ListVehiclesInFleetRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    fleetId = field("fleetId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVehiclesInFleetRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVehiclesInFleetRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVehiclesRequestPaginate:
    boto3_raw_data: "type_defs.ListVehiclesRequestPaginateTypeDef" = dataclasses.field()

    modelManifestArn = field("modelManifestArn")
    attributeNames = field("attributeNames")
    attributeValues = field("attributeValues")
    listResponseScope = field("listResponseScope")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVehiclesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVehiclesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVehicleStatusResponse:
    boto3_raw_data: "type_defs.GetVehicleStatusResponseTypeDef" = dataclasses.field()

    @cached_property
    def campaigns(self):  # pragma: no cover
        return VehicleStatus.make_many(self.boto3_raw_data["campaigns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVehicleStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVehicleStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelManifestsResponse:
    boto3_raw_data: "type_defs.ListModelManifestsResponseTypeDef" = dataclasses.field()

    @cached_property
    def summaries(self):  # pragma: no cover
        return ModelManifestSummary.make_many(self.boto3_raw_data["summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListModelManifestsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelManifestsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalCatalogsResponse:
    boto3_raw_data: "type_defs.ListSignalCatalogsResponseTypeDef" = dataclasses.field()

    @cached_property
    def summaries(self):  # pragma: no cover
        return SignalCatalogSummary.make_many(self.boto3_raw_data["summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSignalCatalogsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalCatalogsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStateTemplatesResponse:
    boto3_raw_data: "type_defs.ListStateTemplatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def summaries(self):  # pragma: no cover
        return StateTemplateSummary.make_many(self.boto3_raw_data["summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStateTemplatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStateTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVehiclesResponse:
    boto3_raw_data: "type_defs.ListVehiclesResponseTypeDef" = dataclasses.field()

    @cached_property
    def vehicleSummaries(self):  # pragma: no cover
        return VehicleSummary.make_many(self.boto3_raw_data["vehicleSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVehiclesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVehiclesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkInterface:
    boto3_raw_data: "type_defs.NetworkInterfaceTypeDef" = dataclasses.field()

    interfaceId = field("interfaceId")
    type = field("type")

    @cached_property
    def canInterface(self):  # pragma: no cover
        return CanInterface.make_one(self.boto3_raw_data["canInterface"])

    @cached_property
    def obdInterface(self):  # pragma: no cover
        return ObdInterface.make_one(self.boto3_raw_data["obdInterface"])

    @cached_property
    def vehicleMiddleware(self):  # pragma: no cover
        return VehicleMiddleware.make_one(self.boto3_raw_data["vehicleMiddleware"])

    @cached_property
    def customDecodingInterface(self):  # pragma: no cover
        return CustomDecodingInterface.make_one(
            self.boto3_raw_data["customDecodingInterface"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeOutput:
    boto3_raw_data: "type_defs.NodeOutputTypeDef" = dataclasses.field()

    @cached_property
    def branch(self):  # pragma: no cover
        return Branch.make_one(self.boto3_raw_data["branch"])

    @cached_property
    def sensor(self):  # pragma: no cover
        return SensorOutput.make_one(self.boto3_raw_data["sensor"])

    @cached_property
    def actuator(self):  # pragma: no cover
        return ActuatorOutput.make_one(self.boto3_raw_data["actuator"])

    @cached_property
    def attribute(self):  # pragma: no cover
        return AttributeOutput.make_one(self.boto3_raw_data["attribute"])

    @cached_property
    def struct(self):  # pragma: no cover
        return CustomStruct.make_one(self.boto3_raw_data["struct"])

    @cached_property
    def property(self):  # pragma: no cover
        return CustomProperty.make_one(self.boto3_raw_data["property"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PeriodicStateTemplateUpdateStrategy:
    boto3_raw_data: "type_defs.PeriodicStateTemplateUpdateStrategyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def stateTemplateUpdateRate(self):  # pragma: no cover
        return TimePeriod.make_one(self.boto3_raw_data["stateTemplateUpdateRate"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PeriodicStateTemplateUpdateStrategyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PeriodicStateTemplateUpdateStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrimitiveMessageDefinition:
    boto3_raw_data: "type_defs.PrimitiveMessageDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def ros2PrimitiveMessageDefinition(self):  # pragma: no cover
        return ROS2PrimitiveMessageDefinition.make_one(
            self.boto3_raw_data["ros2PrimitiveMessageDefinition"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrimitiveMessageDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrimitiveMessageDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterAccountRequest:
    boto3_raw_data: "type_defs.RegisterAccountRequestTypeDef" = dataclasses.field()

    @cached_property
    def timestreamResources(self):  # pragma: no cover
        return TimestreamResources.make_one(self.boto3_raw_data["timestreamResources"])

    @cached_property
    def iamResources(self):  # pragma: no cover
        return IamResources.make_one(self.boto3_raw_data["iamResources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterAccountResponse:
    boto3_raw_data: "type_defs.RegisterAccountResponseTypeDef" = dataclasses.field()

    registerAccountStatus = field("registerAccountStatus")

    @cached_property
    def timestreamResources(self):  # pragma: no cover
        return TimestreamResources.make_one(self.boto3_raw_data["timestreamResources"])

    @cached_property
    def iamResources(self):  # pragma: no cover
        return IamResources.make_one(self.boto3_raw_data["iamResources"])

    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterAccountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalFetchConfig:
    boto3_raw_data: "type_defs.SignalFetchConfigTypeDef" = dataclasses.field()

    @cached_property
    def timeBased(self):  # pragma: no cover
        return TimeBasedSignalFetchConfig.make_one(self.boto3_raw_data["timeBased"])

    @cached_property
    def conditionBased(self):  # pragma: no cover
        return ConditionBasedSignalFetchConfig.make_one(
            self.boto3_raw_data["conditionBased"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignalFetchConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignalFetchConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkFileDefinition:
    boto3_raw_data: "type_defs.NetworkFileDefinitionTypeDef" = dataclasses.field()

    @cached_property
    def canDbc(self):  # pragma: no cover
        return CanDbcDefinition.make_one(self.boto3_raw_data["canDbc"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkFileDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkFileDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataPartition:
    boto3_raw_data: "type_defs.DataPartitionTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def storageOptions(self):  # pragma: no cover
        return DataPartitionStorageOptions.make_one(
            self.boto3_raw_data["storageOptions"]
        )

    @cached_property
    def uploadOptions(self):  # pragma: no cover
        return DataPartitionUploadOptions.make_one(self.boto3_raw_data["uploadOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataPartitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataPartitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDecoderManifestNetworkInterfacesResponse:
    boto3_raw_data: "type_defs.ListDecoderManifestNetworkInterfacesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDecoderManifestNetworkInterfacesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDecoderManifestNetworkInterfacesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelManifestNodesResponse:
    boto3_raw_data: "type_defs.ListModelManifestNodesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def nodes(self):  # pragma: no cover
        return NodeOutput.make_many(self.boto3_raw_data["nodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListModelManifestNodesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelManifestNodesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalCatalogNodesResponse:
    boto3_raw_data: "type_defs.ListSignalCatalogNodesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def nodes(self):  # pragma: no cover
        return NodeOutput.make_many(self.boto3_raw_data["nodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSignalCatalogNodesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalCatalogNodesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateTemplateUpdateStrategyOutput:
    boto3_raw_data: "type_defs.StateTemplateUpdateStrategyOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def periodic(self):  # pragma: no cover
        return PeriodicStateTemplateUpdateStrategy.make_one(
            self.boto3_raw_data["periodic"]
        )

    onChange = field("onChange")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StateTemplateUpdateStrategyOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateTemplateUpdateStrategyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateTemplateUpdateStrategy:
    boto3_raw_data: "type_defs.StateTemplateUpdateStrategyTypeDef" = dataclasses.field()

    @cached_property
    def periodic(self):  # pragma: no cover
        return PeriodicStateTemplateUpdateStrategy.make_one(
            self.boto3_raw_data["periodic"]
        )

    onChange = field("onChange")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StateTemplateUpdateStrategyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateTemplateUpdateStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StructuredMessageOutput:
    boto3_raw_data: "type_defs.StructuredMessageOutputTypeDef" = dataclasses.field()

    @cached_property
    def primitiveMessageDefinition(self):  # pragma: no cover
        return PrimitiveMessageDefinition.make_one(
            self.boto3_raw_data["primitiveMessageDefinition"]
        )

    @cached_property
    def structuredMessageListDefinition(self):  # pragma: no cover
        return StructuredMessageListDefinitionOutput.make_one(
            self.boto3_raw_data["structuredMessageListDefinition"]
        )

    @cached_property
    def structuredMessageDefinition(self):  # pragma: no cover
        return StructuredMessageFieldNameAndDataTypePairOutput.make_many(
            self.boto3_raw_data["structuredMessageDefinition"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StructuredMessageOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StructuredMessageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StructuredMessagePaginator:
    boto3_raw_data: "type_defs.StructuredMessagePaginatorTypeDef" = dataclasses.field()

    @cached_property
    def primitiveMessageDefinition(self):  # pragma: no cover
        return PrimitiveMessageDefinition.make_one(
            self.boto3_raw_data["primitiveMessageDefinition"]
        )

    @cached_property
    def structuredMessageListDefinition(self):  # pragma: no cover
        return StructuredMessageListDefinitionPaginator.make_one(
            self.boto3_raw_data["structuredMessageListDefinition"]
        )

    @cached_property
    def structuredMessageDefinition(self):  # pragma: no cover
        return StructuredMessageFieldNameAndDataTypePairPaginator.make_many(
            self.boto3_raw_data["structuredMessageDefinition"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StructuredMessagePaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StructuredMessagePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Node:
    boto3_raw_data: "type_defs.NodeTypeDef" = dataclasses.field()

    @cached_property
    def branch(self):  # pragma: no cover
        return Branch.make_one(self.boto3_raw_data["branch"])

    sensor = field("sensor")
    actuator = field("actuator")
    attribute = field("attribute")

    @cached_property
    def struct(self):  # pragma: no cover
        return CustomStruct.make_one(self.boto3_raw_data["struct"])

    @cached_property
    def property(self):  # pragma: no cover
        return CustomProperty.make_one(self.boto3_raw_data["property"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalFetchInformationOutput:
    boto3_raw_data: "type_defs.SignalFetchInformationOutputTypeDef" = (
        dataclasses.field()
    )

    fullyQualifiedName = field("fullyQualifiedName")

    @cached_property
    def signalFetchConfig(self):  # pragma: no cover
        return SignalFetchConfig.make_one(self.boto3_raw_data["signalFetchConfig"])

    actions = field("actions")
    conditionLanguageVersion = field("conditionLanguageVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignalFetchInformationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignalFetchInformationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalFetchInformation:
    boto3_raw_data: "type_defs.SignalFetchInformationTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")

    @cached_property
    def signalFetchConfig(self):  # pragma: no cover
        return SignalFetchConfig.make_one(self.boto3_raw_data["signalFetchConfig"])

    actions = field("actions")
    conditionLanguageVersion = field("conditionLanguageVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignalFetchInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignalFetchInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StructuredMessage:
    boto3_raw_data: "type_defs.StructuredMessageTypeDef" = dataclasses.field()

    @cached_property
    def primitiveMessageDefinition(self):  # pragma: no cover
        return PrimitiveMessageDefinition.make_one(
            self.boto3_raw_data["primitiveMessageDefinition"]
        )

    structuredMessageListDefinition = field("structuredMessageListDefinition")
    structuredMessageDefinition = field("structuredMessageDefinition")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StructuredMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StructuredMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportDecoderManifestRequest:
    boto3_raw_data: "type_defs.ImportDecoderManifestRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def networkFileDefinitions(self):  # pragma: no cover
        return NetworkFileDefinition.make_many(
            self.boto3_raw_data["networkFileDefinitions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportDecoderManifestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportDecoderManifestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateTemplateAssociationOutput:
    boto3_raw_data: "type_defs.StateTemplateAssociationOutputTypeDef" = (
        dataclasses.field()
    )

    identifier = field("identifier")

    @cached_property
    def stateTemplateUpdateStrategy(self):  # pragma: no cover
        return StateTemplateUpdateStrategyOutput.make_one(
            self.boto3_raw_data["stateTemplateUpdateStrategy"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StateTemplateAssociationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateTemplateAssociationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageSignalOutput:
    boto3_raw_data: "type_defs.MessageSignalOutputTypeDef" = dataclasses.field()

    topicName = field("topicName")

    @cached_property
    def structuredMessage(self):  # pragma: no cover
        return StructuredMessageOutput.make_one(
            self.boto3_raw_data["structuredMessage"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageSignalOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageSignalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageSignalPaginator:
    boto3_raw_data: "type_defs.MessageSignalPaginatorTypeDef" = dataclasses.field()

    topicName = field("topicName")

    @cached_property
    def structuredMessage(self):  # pragma: no cover
        return StructuredMessagePaginator.make_one(
            self.boto3_raw_data["structuredMessage"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageSignalPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageSignalPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCampaignResponse:
    boto3_raw_data: "type_defs.GetCampaignResponseTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    description = field("description")
    signalCatalogArn = field("signalCatalogArn")
    targetArn = field("targetArn")
    status = field("status")
    startTime = field("startTime")
    expiryTime = field("expiryTime")
    postTriggerCollectionDuration = field("postTriggerCollectionDuration")
    diagnosticsMode = field("diagnosticsMode")
    spoolingMode = field("spoolingMode")
    compression = field("compression")
    priority = field("priority")

    @cached_property
    def signalsToCollect(self):  # pragma: no cover
        return SignalInformation.make_many(self.boto3_raw_data["signalsToCollect"])

    @cached_property
    def collectionScheme(self):  # pragma: no cover
        return CollectionScheme.make_one(self.boto3_raw_data["collectionScheme"])

    dataExtraDimensions = field("dataExtraDimensions")
    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")

    @cached_property
    def dataDestinationConfigs(self):  # pragma: no cover
        return DataDestinationConfig.make_many(
            self.boto3_raw_data["dataDestinationConfigs"]
        )

    @cached_property
    def dataPartitions(self):  # pragma: no cover
        return DataPartition.make_many(self.boto3_raw_data["dataPartitions"])

    @cached_property
    def signalsToFetch(self):  # pragma: no cover
        return SignalFetchInformationOutput.make_many(
            self.boto3_raw_data["signalsToFetch"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVehicleResponse:
    boto3_raw_data: "type_defs.GetVehicleResponseTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    arn = field("arn")
    modelManifestArn = field("modelManifestArn")
    decoderManifestArn = field("decoderManifestArn")
    attributes = field("attributes")

    @cached_property
    def stateTemplates(self):  # pragma: no cover
        return StateTemplateAssociationOutput.make_many(
            self.boto3_raw_data["stateTemplates"]
        )

    creationTime = field("creationTime")
    lastModificationTime = field("lastModificationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVehicleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVehicleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StateTemplateAssociation:
    boto3_raw_data: "type_defs.StateTemplateAssociationTypeDef" = dataclasses.field()

    identifier = field("identifier")
    stateTemplateUpdateStrategy = field("stateTemplateUpdateStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StateTemplateAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StateTemplateAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalDecoderOutput:
    boto3_raw_data: "type_defs.SignalDecoderOutputTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    type = field("type")
    interfaceId = field("interfaceId")

    @cached_property
    def canSignal(self):  # pragma: no cover
        return CanSignal.make_one(self.boto3_raw_data["canSignal"])

    @cached_property
    def obdSignal(self):  # pragma: no cover
        return ObdSignal.make_one(self.boto3_raw_data["obdSignal"])

    @cached_property
    def messageSignal(self):  # pragma: no cover
        return MessageSignalOutput.make_one(self.boto3_raw_data["messageSignal"])

    @cached_property
    def customDecodingSignal(self):  # pragma: no cover
        return CustomDecodingSignal.make_one(
            self.boto3_raw_data["customDecodingSignal"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignalDecoderOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignalDecoderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalDecoderPaginator:
    boto3_raw_data: "type_defs.SignalDecoderPaginatorTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    type = field("type")
    interfaceId = field("interfaceId")

    @cached_property
    def canSignal(self):  # pragma: no cover
        return CanSignal.make_one(self.boto3_raw_data["canSignal"])

    @cached_property
    def obdSignal(self):  # pragma: no cover
        return ObdSignal.make_one(self.boto3_raw_data["obdSignal"])

    @cached_property
    def messageSignal(self):  # pragma: no cover
        return MessageSignalPaginator.make_one(self.boto3_raw_data["messageSignal"])

    @cached_property
    def customDecodingSignal(self):  # pragma: no cover
        return CustomDecodingSignal.make_one(
            self.boto3_raw_data["customDecodingSignal"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignalDecoderPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignalDecoderPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSignalCatalogRequest:
    boto3_raw_data: "type_defs.CreateSignalCatalogRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    nodes = field("nodes")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSignalCatalogRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSignalCatalogRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSignalCatalogRequest:
    boto3_raw_data: "type_defs.UpdateSignalCatalogRequestTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    nodesToAdd = field("nodesToAdd")
    nodesToUpdate = field("nodesToUpdate")
    nodesToRemove = field("nodesToRemove")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSignalCatalogRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSignalCatalogRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCampaignRequest:
    boto3_raw_data: "type_defs.CreateCampaignRequestTypeDef" = dataclasses.field()

    name = field("name")
    signalCatalogArn = field("signalCatalogArn")
    targetArn = field("targetArn")

    @cached_property
    def collectionScheme(self):  # pragma: no cover
        return CollectionScheme.make_one(self.boto3_raw_data["collectionScheme"])

    description = field("description")
    startTime = field("startTime")
    expiryTime = field("expiryTime")
    postTriggerCollectionDuration = field("postTriggerCollectionDuration")
    diagnosticsMode = field("diagnosticsMode")
    spoolingMode = field("spoolingMode")
    compression = field("compression")
    priority = field("priority")

    @cached_property
    def signalsToCollect(self):  # pragma: no cover
        return SignalInformation.make_many(self.boto3_raw_data["signalsToCollect"])

    dataExtraDimensions = field("dataExtraDimensions")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def dataDestinationConfigs(self):  # pragma: no cover
        return DataDestinationConfig.make_many(
            self.boto3_raw_data["dataDestinationConfigs"]
        )

    @cached_property
    def dataPartitions(self):  # pragma: no cover
        return DataPartition.make_many(self.boto3_raw_data["dataPartitions"])

    signalsToFetch = field("signalsToFetch")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageSignal:
    boto3_raw_data: "type_defs.MessageSignalTypeDef" = dataclasses.field()

    topicName = field("topicName")
    structuredMessage = field("structuredMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageSignalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageSignalTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDecoderManifestSignalsResponse:
    boto3_raw_data: "type_defs.ListDecoderManifestSignalsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def signalDecoders(self):  # pragma: no cover
        return SignalDecoderOutput.make_many(self.boto3_raw_data["signalDecoders"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDecoderManifestSignalsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDecoderManifestSignalsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDecoderManifestSignalsResponsePaginator:
    boto3_raw_data: "type_defs.ListDecoderManifestSignalsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def signalDecoders(self):  # pragma: no cover
        return SignalDecoderPaginator.make_many(self.boto3_raw_data["signalDecoders"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDecoderManifestSignalsResponsePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDecoderManifestSignalsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVehicleRequestItem:
    boto3_raw_data: "type_defs.CreateVehicleRequestItemTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    modelManifestArn = field("modelManifestArn")
    decoderManifestArn = field("decoderManifestArn")
    attributes = field("attributes")
    associationBehavior = field("associationBehavior")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    stateTemplates = field("stateTemplates")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVehicleRequestItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVehicleRequestItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVehicleRequest:
    boto3_raw_data: "type_defs.CreateVehicleRequestTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    modelManifestArn = field("modelManifestArn")
    decoderManifestArn = field("decoderManifestArn")
    attributes = field("attributes")
    associationBehavior = field("associationBehavior")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    stateTemplates = field("stateTemplates")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVehicleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVehicleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVehicleRequestItem:
    boto3_raw_data: "type_defs.UpdateVehicleRequestItemTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    modelManifestArn = field("modelManifestArn")
    decoderManifestArn = field("decoderManifestArn")
    attributes = field("attributes")
    attributeUpdateMode = field("attributeUpdateMode")
    stateTemplatesToAdd = field("stateTemplatesToAdd")
    stateTemplatesToRemove = field("stateTemplatesToRemove")

    @cached_property
    def stateTemplatesToUpdate(self):  # pragma: no cover
        return StateTemplateAssociation.make_many(
            self.boto3_raw_data["stateTemplatesToUpdate"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVehicleRequestItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVehicleRequestItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVehicleRequest:
    boto3_raw_data: "type_defs.UpdateVehicleRequestTypeDef" = dataclasses.field()

    vehicleName = field("vehicleName")
    modelManifestArn = field("modelManifestArn")
    decoderManifestArn = field("decoderManifestArn")
    attributes = field("attributes")
    attributeUpdateMode = field("attributeUpdateMode")
    stateTemplatesToAdd = field("stateTemplatesToAdd")
    stateTemplatesToRemove = field("stateTemplatesToRemove")
    stateTemplatesToUpdate = field("stateTemplatesToUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVehicleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVehicleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalDecoder:
    boto3_raw_data: "type_defs.SignalDecoderTypeDef" = dataclasses.field()

    fullyQualifiedName = field("fullyQualifiedName")
    type = field("type")
    interfaceId = field("interfaceId")

    @cached_property
    def canSignal(self):  # pragma: no cover
        return CanSignal.make_one(self.boto3_raw_data["canSignal"])

    @cached_property
    def obdSignal(self):  # pragma: no cover
        return ObdSignal.make_one(self.boto3_raw_data["obdSignal"])

    messageSignal = field("messageSignal")

    @cached_property
    def customDecodingSignal(self):  # pragma: no cover
        return CustomDecodingSignal.make_one(
            self.boto3_raw_data["customDecodingSignal"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignalDecoderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SignalDecoderTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateVehicleRequest:
    boto3_raw_data: "type_defs.BatchCreateVehicleRequestTypeDef" = dataclasses.field()

    @cached_property
    def vehicles(self):  # pragma: no cover
        return CreateVehicleRequestItem.make_many(self.boto3_raw_data["vehicles"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchCreateVehicleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateVehicleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateVehicleRequest:
    boto3_raw_data: "type_defs.BatchUpdateVehicleRequestTypeDef" = dataclasses.field()

    @cached_property
    def vehicles(self):  # pragma: no cover
        return UpdateVehicleRequestItem.make_many(self.boto3_raw_data["vehicles"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateVehicleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateVehicleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDecoderManifestRequest:
    boto3_raw_data: "type_defs.CreateDecoderManifestRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    modelManifestArn = field("modelManifestArn")
    description = field("description")
    signalDecoders = field("signalDecoders")

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    defaultForUnmappedSignals = field("defaultForUnmappedSignals")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDecoderManifestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDecoderManifestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDecoderManifestRequest:
    boto3_raw_data: "type_defs.UpdateDecoderManifestRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")
    signalDecodersToAdd = field("signalDecodersToAdd")
    signalDecodersToUpdate = field("signalDecodersToUpdate")
    signalDecodersToRemove = field("signalDecodersToRemove")

    @cached_property
    def networkInterfacesToAdd(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfacesToAdd"])

    @cached_property
    def networkInterfacesToUpdate(self):  # pragma: no cover
        return NetworkInterface.make_many(
            self.boto3_raw_data["networkInterfacesToUpdate"]
        )

    networkInterfacesToRemove = field("networkInterfacesToRemove")
    status = field("status")
    defaultForUnmappedSignals = field("defaultForUnmappedSignals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDecoderManifestRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDecoderManifestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
