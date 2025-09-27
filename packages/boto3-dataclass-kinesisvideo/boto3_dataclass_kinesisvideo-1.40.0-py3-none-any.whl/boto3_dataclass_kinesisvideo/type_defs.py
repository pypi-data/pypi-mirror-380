# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kinesisvideo import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class SingleMasterConfiguration:
    boto3_raw_data: "type_defs.SingleMasterConfigurationTypeDef" = dataclasses.field()

    MessageTtlSeconds = field("MessageTtlSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SingleMasterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SingleMasterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelNameCondition:
    boto3_raw_data: "type_defs.ChannelNameConditionTypeDef" = dataclasses.field()

    ComparisonOperator = field("ComparisonOperator")
    ComparisonValue = field("ComparisonValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChannelNameConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelNameConditionTypeDef"]
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
class CreateStreamInput:
    boto3_raw_data: "type_defs.CreateStreamInputTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    DeviceName = field("DeviceName")
    MediaType = field("MediaType")
    KmsKeyId = field("KmsKeyId")
    DataRetentionInHours = field("DataRetentionInHours")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateStreamInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEdgeConfigurationInput:
    boto3_raw_data: "type_defs.DeleteEdgeConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEdgeConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEdgeConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSignalingChannelInput:
    boto3_raw_data: "type_defs.DeleteSignalingChannelInputTypeDef" = dataclasses.field()

    ChannelARN = field("ChannelARN")
    CurrentVersion = field("CurrentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSignalingChannelInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSignalingChannelInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStreamInput:
    boto3_raw_data: "type_defs.DeleteStreamInputTypeDef" = dataclasses.field()

    StreamARN = field("StreamARN")
    CurrentVersion = field("CurrentVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteStreamInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocalSizeConfig:
    boto3_raw_data: "type_defs.LocalSizeConfigTypeDef" = dataclasses.field()

    MaxLocalMediaSizeInMB = field("MaxLocalMediaSizeInMB")
    StrategyOnFullSize = field("StrategyOnFullSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocalSizeConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocalSizeConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEdgeConfigurationInput:
    boto3_raw_data: "type_defs.DescribeEdgeConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEdgeConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEdgeConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageGenerationConfigurationInput:
    boto3_raw_data: "type_defs.DescribeImageGenerationConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeImageGenerationConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageGenerationConfigurationInputTypeDef"]
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
class DescribeMappedResourceConfigurationInput:
    boto3_raw_data: "type_defs.DescribeMappedResourceConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMappedResourceConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMappedResourceConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MappedResourceConfigurationListItem:
    boto3_raw_data: "type_defs.MappedResourceConfigurationListItemTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    ARN = field("ARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MappedResourceConfigurationListItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MappedResourceConfigurationListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMediaStorageConfigurationInput:
    boto3_raw_data: "type_defs.DescribeMediaStorageConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    ChannelName = field("ChannelName")
    ChannelARN = field("ChannelARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMediaStorageConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMediaStorageConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaStorageConfiguration:
    boto3_raw_data: "type_defs.MediaStorageConfigurationTypeDef" = dataclasses.field()

    Status = field("Status")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaStorageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaStorageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotificationConfigurationInput:
    boto3_raw_data: "type_defs.DescribeNotificationConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNotificationConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNotificationConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSignalingChannelInput:
    boto3_raw_data: "type_defs.DescribeSignalingChannelInputTypeDef" = (
        dataclasses.field()
    )

    ChannelName = field("ChannelName")
    ChannelARN = field("ChannelARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSignalingChannelInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSignalingChannelInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamInput:
    boto3_raw_data: "type_defs.DescribeStreamInputTypeDef" = dataclasses.field()

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamInfo:
    boto3_raw_data: "type_defs.StreamInfoTypeDef" = dataclasses.field()

    DeviceName = field("DeviceName")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    MediaType = field("MediaType")
    KmsKeyId = field("KmsKeyId")
    Version = field("Version")
    Status = field("Status")
    CreationTime = field("CreationTime")
    DataRetentionInHours = field("DataRetentionInHours")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LastRecorderStatus:
    boto3_raw_data: "type_defs.LastRecorderStatusTypeDef" = dataclasses.field()

    JobStatusDetails = field("JobStatusDetails")
    LastCollectedTime = field("LastCollectedTime")
    LastUpdatedTime = field("LastUpdatedTime")
    RecorderStatus = field("RecorderStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LastRecorderStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LastRecorderStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LastUploaderStatus:
    boto3_raw_data: "type_defs.LastUploaderStatusTypeDef" = dataclasses.field()

    JobStatusDetails = field("JobStatusDetails")
    LastCollectedTime = field("LastCollectedTime")
    LastUpdatedTime = field("LastUpdatedTime")
    UploaderStatus = field("UploaderStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LastUploaderStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LastUploaderStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataEndpointInput:
    boto3_raw_data: "type_defs.GetDataEndpointInputTypeDef" = dataclasses.field()

    APIName = field("APIName")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataEndpointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SingleMasterChannelEndpointConfiguration:
    boto3_raw_data: "type_defs.SingleMasterChannelEndpointConfigurationTypeDef" = (
        dataclasses.field()
    )

    Protocols = field("Protocols")
    Role = field("Role")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SingleMasterChannelEndpointConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SingleMasterChannelEndpointConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceEndpointListItem:
    boto3_raw_data: "type_defs.ResourceEndpointListItemTypeDef" = dataclasses.field()

    Protocol = field("Protocol")
    ResourceEndpoint = field("ResourceEndpoint")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceEndpointListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceEndpointListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageGenerationDestinationConfig:
    boto3_raw_data: "type_defs.ImageGenerationDestinationConfigTypeDef" = (
        dataclasses.field()
    )

    Uri = field("Uri")
    DestinationRegion = field("DestinationRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImageGenerationDestinationConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageGenerationDestinationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEdgeAgentConfigurationsInput:
    boto3_raw_data: "type_defs.ListEdgeAgentConfigurationsInputTypeDef" = (
        dataclasses.field()
    )

    HubDeviceArn = field("HubDeviceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEdgeAgentConfigurationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEdgeAgentConfigurationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamNameCondition:
    boto3_raw_data: "type_defs.StreamNameConditionTypeDef" = dataclasses.field()

    ComparisonOperator = field("ComparisonOperator")
    ComparisonValue = field("ComparisonValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamNameConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamNameConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForStreamInput:
    boto3_raw_data: "type_defs.ListTagsForStreamInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    StreamARN = field("StreamARN")
    StreamName = field("StreamName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForStreamInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaSourceConfig:
    boto3_raw_data: "type_defs.MediaSourceConfigTypeDef" = dataclasses.field()

    MediaUriSecretArn = field("MediaUriSecretArn")
    MediaUriType = field("MediaUriType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaSourceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationDestinationConfig:
    boto3_raw_data: "type_defs.NotificationDestinationConfigTypeDef" = (
        dataclasses.field()
    )

    Uri = field("Uri")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NotificationDestinationConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationDestinationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleConfig:
    boto3_raw_data: "type_defs.ScheduleConfigTypeDef" = dataclasses.field()

    ScheduleExpression = field("ScheduleExpression")
    DurationInSeconds = field("DurationInSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagStreamInput:
    boto3_raw_data: "type_defs.TagStreamInputTypeDef" = dataclasses.field()

    Tags = field("Tags")
    StreamARN = field("StreamARN")
    StreamName = field("StreamName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagStreamInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagStreamInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
    TagKeyList = field("TagKeyList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagStreamInput:
    boto3_raw_data: "type_defs.UntagStreamInputTypeDef" = dataclasses.field()

    TagKeyList = field("TagKeyList")
    StreamARN = field("StreamARN")
    StreamName = field("StreamName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UntagStreamInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataRetentionInput:
    boto3_raw_data: "type_defs.UpdateDataRetentionInputTypeDef" = dataclasses.field()

    CurrentVersion = field("CurrentVersion")
    Operation = field("Operation")
    DataRetentionChangeInHours = field("DataRetentionChangeInHours")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataRetentionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataRetentionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStreamInput:
    boto3_raw_data: "type_defs.UpdateStreamInputTypeDef" = dataclasses.field()

    CurrentVersion = field("CurrentVersion")
    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    DeviceName = field("DeviceName")
    MediaType = field("MediaType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateStreamInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStreamInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelInfo:
    boto3_raw_data: "type_defs.ChannelInfoTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")
    ChannelARN = field("ChannelARN")
    ChannelType = field("ChannelType")
    ChannelStatus = field("ChannelStatus")
    CreationTime = field("CreationTime")

    @cached_property
    def SingleMasterConfiguration(self):  # pragma: no cover
        return SingleMasterConfiguration.make_one(
            self.boto3_raw_data["SingleMasterConfiguration"]
        )

    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSignalingChannelInput:
    boto3_raw_data: "type_defs.UpdateSignalingChannelInputTypeDef" = dataclasses.field()

    ChannelARN = field("ChannelARN")
    CurrentVersion = field("CurrentVersion")

    @cached_property
    def SingleMasterConfiguration(self):  # pragma: no cover
        return SingleMasterConfiguration.make_one(
            self.boto3_raw_data["SingleMasterConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSignalingChannelInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSignalingChannelInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalingChannelsInput:
    boto3_raw_data: "type_defs.ListSignalingChannelsInputTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def ChannelNameCondition(self):  # pragma: no cover
        return ChannelNameCondition.make_one(
            self.boto3_raw_data["ChannelNameCondition"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSignalingChannelsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalingChannelsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSignalingChannelInput:
    boto3_raw_data: "type_defs.CreateSignalingChannelInputTypeDef" = dataclasses.field()

    ChannelName = field("ChannelName")
    ChannelType = field("ChannelType")

    @cached_property
    def SingleMasterConfiguration(self):  # pragma: no cover
        return SingleMasterConfiguration.make_one(
            self.boto3_raw_data["SingleMasterConfiguration"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSignalingChannelInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSignalingChannelInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSignalingChannelOutput:
    boto3_raw_data: "type_defs.CreateSignalingChannelOutputTypeDef" = (
        dataclasses.field()
    )

    ChannelARN = field("ChannelARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSignalingChannelOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSignalingChannelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStreamOutput:
    boto3_raw_data: "type_defs.CreateStreamOutputTypeDef" = dataclasses.field()

    StreamARN = field("StreamARN")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataEndpointOutput:
    boto3_raw_data: "type_defs.GetDataEndpointOutputTypeDef" = dataclasses.field()

    DataEndpoint = field("DataEndpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataEndpointOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForStreamOutput:
    boto3_raw_data: "type_defs.ListTagsForStreamOutputTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletionConfig:
    boto3_raw_data: "type_defs.DeletionConfigTypeDef" = dataclasses.field()

    EdgeRetentionInHours = field("EdgeRetentionInHours")

    @cached_property
    def LocalSizeConfig(self):  # pragma: no cover
        return LocalSizeConfig.make_one(self.boto3_raw_data["LocalSizeConfig"])

    DeleteAfterUpload = field("DeleteAfterUpload")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeletionConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeletionConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMappedResourceConfigurationInputPaginate:
    boto3_raw_data: (
        "type_defs.DescribeMappedResourceConfigurationInputPaginateTypeDef"
    ) = dataclasses.field()

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMappedResourceConfigurationInputPaginateTypeDef"
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
                "type_defs.DescribeMappedResourceConfigurationInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEdgeAgentConfigurationsInputPaginate:
    boto3_raw_data: "type_defs.ListEdgeAgentConfigurationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    HubDeviceArn = field("HubDeviceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEdgeAgentConfigurationsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEdgeAgentConfigurationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalingChannelsInputPaginate:
    boto3_raw_data: "type_defs.ListSignalingChannelsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChannelNameCondition(self):  # pragma: no cover
        return ChannelNameCondition.make_one(
            self.boto3_raw_data["ChannelNameCondition"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSignalingChannelsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalingChannelsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMappedResourceConfigurationOutput:
    boto3_raw_data: "type_defs.DescribeMappedResourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MappedResourceConfigurationList(self):  # pragma: no cover
        return MappedResourceConfigurationListItem.make_many(
            self.boto3_raw_data["MappedResourceConfigurationList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMappedResourceConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMappedResourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMediaStorageConfigurationOutput:
    boto3_raw_data: "type_defs.DescribeMediaStorageConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MediaStorageConfiguration(self):  # pragma: no cover
        return MediaStorageConfiguration.make_one(
            self.boto3_raw_data["MediaStorageConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMediaStorageConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMediaStorageConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMediaStorageConfigurationInput:
    boto3_raw_data: "type_defs.UpdateMediaStorageConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    ChannelARN = field("ChannelARN")

    @cached_property
    def MediaStorageConfiguration(self):  # pragma: no cover
        return MediaStorageConfiguration.make_one(
            self.boto3_raw_data["MediaStorageConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMediaStorageConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMediaStorageConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStreamOutput:
    boto3_raw_data: "type_defs.DescribeStreamOutputTypeDef" = dataclasses.field()

    @cached_property
    def StreamInfo(self):  # pragma: no cover
        return StreamInfo.make_one(self.boto3_raw_data["StreamInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStreamOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStreamOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsOutput:
    boto3_raw_data: "type_defs.ListStreamsOutputTypeDef" = dataclasses.field()

    @cached_property
    def StreamInfoList(self):  # pragma: no cover
        return StreamInfo.make_many(self.boto3_raw_data["StreamInfoList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStreamsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EdgeAgentStatus:
    boto3_raw_data: "type_defs.EdgeAgentStatusTypeDef" = dataclasses.field()

    @cached_property
    def LastRecorderStatus(self):  # pragma: no cover
        return LastRecorderStatus.make_one(self.boto3_raw_data["LastRecorderStatus"])

    @cached_property
    def LastUploaderStatus(self):  # pragma: no cover
        return LastUploaderStatus.make_one(self.boto3_raw_data["LastUploaderStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdgeAgentStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EdgeAgentStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSignalingChannelEndpointInput:
    boto3_raw_data: "type_defs.GetSignalingChannelEndpointInputTypeDef" = (
        dataclasses.field()
    )

    ChannelARN = field("ChannelARN")

    @cached_property
    def SingleMasterChannelEndpointConfiguration(self):  # pragma: no cover
        return SingleMasterChannelEndpointConfiguration.make_one(
            self.boto3_raw_data["SingleMasterChannelEndpointConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSignalingChannelEndpointInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSignalingChannelEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSignalingChannelEndpointOutput:
    boto3_raw_data: "type_defs.GetSignalingChannelEndpointOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceEndpointList(self):  # pragma: no cover
        return ResourceEndpointListItem.make_many(
            self.boto3_raw_data["ResourceEndpointList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSignalingChannelEndpointOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSignalingChannelEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageGenerationConfigurationOutput:
    boto3_raw_data: "type_defs.ImageGenerationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    ImageSelectorType = field("ImageSelectorType")

    @cached_property
    def DestinationConfig(self):  # pragma: no cover
        return ImageGenerationDestinationConfig.make_one(
            self.boto3_raw_data["DestinationConfig"]
        )

    SamplingInterval = field("SamplingInterval")
    Format = field("Format")
    FormatConfig = field("FormatConfig")
    WidthPixels = field("WidthPixels")
    HeightPixels = field("HeightPixels")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImageGenerationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageGenerationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageGenerationConfiguration:
    boto3_raw_data: "type_defs.ImageGenerationConfigurationTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    ImageSelectorType = field("ImageSelectorType")

    @cached_property
    def DestinationConfig(self):  # pragma: no cover
        return ImageGenerationDestinationConfig.make_one(
            self.boto3_raw_data["DestinationConfig"]
        )

    SamplingInterval = field("SamplingInterval")
    Format = field("Format")
    FormatConfig = field("FormatConfig")
    WidthPixels = field("WidthPixels")
    HeightPixels = field("HeightPixels")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageGenerationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageGenerationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsInputPaginate:
    boto3_raw_data: "type_defs.ListStreamsInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def StreamNameCondition(self):  # pragma: no cover
        return StreamNameCondition.make_one(self.boto3_raw_data["StreamNameCondition"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStreamsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStreamsInput:
    boto3_raw_data: "type_defs.ListStreamsInputTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def StreamNameCondition(self):  # pragma: no cover
        return StreamNameCondition.make_one(self.boto3_raw_data["StreamNameCondition"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStreamsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStreamsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfiguration:
    boto3_raw_data: "type_defs.NotificationConfigurationTypeDef" = dataclasses.field()

    Status = field("Status")

    @cached_property
    def DestinationConfig(self):  # pragma: no cover
        return NotificationDestinationConfig.make_one(
            self.boto3_raw_data["DestinationConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecorderConfig:
    boto3_raw_data: "type_defs.RecorderConfigTypeDef" = dataclasses.field()

    @cached_property
    def MediaSourceConfig(self):  # pragma: no cover
        return MediaSourceConfig.make_one(self.boto3_raw_data["MediaSourceConfig"])

    @cached_property
    def ScheduleConfig(self):  # pragma: no cover
        return ScheduleConfig.make_one(self.boto3_raw_data["ScheduleConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecorderConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecorderConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploaderConfig:
    boto3_raw_data: "type_defs.UploaderConfigTypeDef" = dataclasses.field()

    @cached_property
    def ScheduleConfig(self):  # pragma: no cover
        return ScheduleConfig.make_one(self.boto3_raw_data["ScheduleConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UploaderConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UploaderConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSignalingChannelOutput:
    boto3_raw_data: "type_defs.DescribeSignalingChannelOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChannelInfo(self):  # pragma: no cover
        return ChannelInfo.make_one(self.boto3_raw_data["ChannelInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSignalingChannelOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSignalingChannelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSignalingChannelsOutput:
    boto3_raw_data: "type_defs.ListSignalingChannelsOutputTypeDef" = dataclasses.field()

    @cached_property
    def ChannelInfoList(self):  # pragma: no cover
        return ChannelInfo.make_many(self.boto3_raw_data["ChannelInfoList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSignalingChannelsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSignalingChannelsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageGenerationConfigurationOutput:
    boto3_raw_data: "type_defs.DescribeImageGenerationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ImageGenerationConfiguration(self):  # pragma: no cover
        return ImageGenerationConfigurationOutput.make_one(
            self.boto3_raw_data["ImageGenerationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeImageGenerationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageGenerationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNotificationConfigurationOutput:
    boto3_raw_data: "type_defs.DescribeNotificationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NotificationConfiguration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(
            self.boto3_raw_data["NotificationConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNotificationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNotificationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNotificationConfigurationInput:
    boto3_raw_data: "type_defs.UpdateNotificationConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @cached_property
    def NotificationConfiguration(self):  # pragma: no cover
        return NotificationConfiguration.make_one(
            self.boto3_raw_data["NotificationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateNotificationConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNotificationConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EdgeConfig:
    boto3_raw_data: "type_defs.EdgeConfigTypeDef" = dataclasses.field()

    HubDeviceArn = field("HubDeviceArn")

    @cached_property
    def RecorderConfig(self):  # pragma: no cover
        return RecorderConfig.make_one(self.boto3_raw_data["RecorderConfig"])

    @cached_property
    def UploaderConfig(self):  # pragma: no cover
        return UploaderConfig.make_one(self.boto3_raw_data["UploaderConfig"])

    @cached_property
    def DeletionConfig(self):  # pragma: no cover
        return DeletionConfig.make_one(self.boto3_raw_data["DeletionConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdgeConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EdgeConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateImageGenerationConfigurationInput:
    boto3_raw_data: "type_defs.UpdateImageGenerationConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    ImageGenerationConfiguration = field("ImageGenerationConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateImageGenerationConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateImageGenerationConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEdgeConfigurationOutput:
    boto3_raw_data: "type_defs.DescribeEdgeConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")
    SyncStatus = field("SyncStatus")
    FailedStatusDetails = field("FailedStatusDetails")

    @cached_property
    def EdgeConfig(self):  # pragma: no cover
        return EdgeConfig.make_one(self.boto3_raw_data["EdgeConfig"])

    @cached_property
    def EdgeAgentStatus(self):  # pragma: no cover
        return EdgeAgentStatus.make_one(self.boto3_raw_data["EdgeAgentStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEdgeConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEdgeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEdgeAgentConfigurationsEdgeConfig:
    boto3_raw_data: "type_defs.ListEdgeAgentConfigurationsEdgeConfigTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")
    SyncStatus = field("SyncStatus")
    FailedStatusDetails = field("FailedStatusDetails")

    @cached_property
    def EdgeConfig(self):  # pragma: no cover
        return EdgeConfig.make_one(self.boto3_raw_data["EdgeConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEdgeAgentConfigurationsEdgeConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEdgeAgentConfigurationsEdgeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEdgeConfigurationUpdateInput:
    boto3_raw_data: "type_defs.StartEdgeConfigurationUpdateInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EdgeConfig(self):  # pragma: no cover
        return EdgeConfig.make_one(self.boto3_raw_data["EdgeConfig"])

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartEdgeConfigurationUpdateInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEdgeConfigurationUpdateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEdgeConfigurationUpdateOutput:
    boto3_raw_data: "type_defs.StartEdgeConfigurationUpdateOutputTypeDef" = (
        dataclasses.field()
    )

    StreamName = field("StreamName")
    StreamARN = field("StreamARN")
    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")
    SyncStatus = field("SyncStatus")
    FailedStatusDetails = field("FailedStatusDetails")

    @cached_property
    def EdgeConfig(self):  # pragma: no cover
        return EdgeConfig.make_one(self.boto3_raw_data["EdgeConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartEdgeConfigurationUpdateOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEdgeConfigurationUpdateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEdgeAgentConfigurationsOutput:
    boto3_raw_data: "type_defs.ListEdgeAgentConfigurationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EdgeConfigs(self):  # pragma: no cover
        return ListEdgeAgentConfigurationsEdgeConfig.make_many(
            self.boto3_raw_data["EdgeConfigs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEdgeAgentConfigurationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEdgeAgentConfigurationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
