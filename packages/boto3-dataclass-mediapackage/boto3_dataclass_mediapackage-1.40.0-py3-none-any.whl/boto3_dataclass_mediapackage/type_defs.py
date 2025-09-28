# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediapackage import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Authorization:
    boto3_raw_data: "type_defs.AuthorizationTypeDef" = dataclasses.field()

    CdnIdentifierSecret = field("CdnIdentifierSecret")
    SecretsRoleArn = field("SecretsRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthorizationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthorizationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EgressAccessLogs:
    boto3_raw_data: "type_defs.EgressAccessLogsTypeDef" = dataclasses.field()

    LogGroupName = field("LogGroupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EgressAccessLogsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EgressAccessLogsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngressAccessLogs:
    boto3_raw_data: "type_defs.IngressAccessLogsTypeDef" = dataclasses.field()

    LogGroupName = field("LogGroupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IngressAccessLogsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IngressAccessLogsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsManifestCreateOrUpdateParameters:
    boto3_raw_data: "type_defs.HlsManifestCreateOrUpdateParametersTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    AdMarkers = field("AdMarkers")
    AdTriggers = field("AdTriggers")
    AdsOnDeliveryRestrictions = field("AdsOnDeliveryRestrictions")
    IncludeIframeOnlyStream = field("IncludeIframeOnlyStream")
    ManifestName = field("ManifestName")
    PlaylistType = field("PlaylistType")
    PlaylistWindowSeconds = field("PlaylistWindowSeconds")
    ProgramDateTimeIntervalSeconds = field("ProgramDateTimeIntervalSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HlsManifestCreateOrUpdateParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsManifestCreateOrUpdateParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamSelection:
    boto3_raw_data: "type_defs.StreamSelectionTypeDef" = dataclasses.field()

    MaxVideoBitsPerSecond = field("MaxVideoBitsPerSecond")
    MinVideoBitsPerSecond = field("MinVideoBitsPerSecond")
    StreamOrder = field("StreamOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreamSelectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StreamSelectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsManifest:
    boto3_raw_data: "type_defs.HlsManifestTypeDef" = dataclasses.field()

    Id = field("Id")
    AdMarkers = field("AdMarkers")
    IncludeIframeOnlyStream = field("IncludeIframeOnlyStream")
    ManifestName = field("ManifestName")
    PlaylistType = field("PlaylistType")
    PlaylistWindowSeconds = field("PlaylistWindowSeconds")
    ProgramDateTimeIntervalSeconds = field("ProgramDateTimeIntervalSeconds")
    Url = field("Url")
    AdTriggers = field("AdTriggers")
    AdsOnDeliveryRestrictions = field("AdsOnDeliveryRestrictions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsManifestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HlsManifestTypeDef"]]
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
class CreateChannelRequest:
    boto3_raw_data: "type_defs.CreateChannelRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Destination:
    boto3_raw_data: "type_defs.S3DestinationTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    ManifestKey = field("ManifestKey")
    RoleArn = field("RoleArn")

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
class DeleteChannelRequest:
    boto3_raw_data: "type_defs.DeleteChannelRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOriginEndpointRequest:
    boto3_raw_data: "type_defs.DeleteOriginEndpointRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOriginEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOriginEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelRequest:
    boto3_raw_data: "type_defs.DescribeChannelRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHarvestJobRequest:
    boto3_raw_data: "type_defs.DescribeHarvestJobRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeHarvestJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHarvestJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOriginEndpointRequest:
    boto3_raw_data: "type_defs.DescribeOriginEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeOriginEndpointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOriginEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionContractConfiguration:
    boto3_raw_data: "type_defs.EncryptionContractConfigurationTypeDef" = (
        dataclasses.field()
    )

    PresetSpeke20Audio = field("PresetSpeke20Audio")
    PresetSpeke20Video = field("PresetSpeke20Video")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EncryptionContractConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionContractConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestEndpoint:
    boto3_raw_data: "type_defs.IngestEndpointTypeDef" = dataclasses.field()

    Id = field("Id")
    Password = field("Password")
    Url = field("Url")
    Username = field("Username")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IngestEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IngestEndpointTypeDef"]],
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
class ListChannelsRequest:
    boto3_raw_data: "type_defs.ListChannelsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHarvestJobsRequest:
    boto3_raw_data: "type_defs.ListHarvestJobsRequestTypeDef" = dataclasses.field()

    IncludeChannelId = field("IncludeChannelId")
    IncludeStatus = field("IncludeStatus")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHarvestJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHarvestJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOriginEndpointsRequest:
    boto3_raw_data: "type_defs.ListOriginEndpointsRequestTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOriginEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOriginEndpointsRequestTypeDef"]
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
class RotateChannelCredentialsRequest:
    boto3_raw_data: "type_defs.RotateChannelCredentialsRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RotateChannelCredentialsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RotateChannelCredentialsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RotateIngestEndpointCredentialsRequest:
    boto3_raw_data: "type_defs.RotateIngestEndpointCredentialsRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    IngestEndpointId = field("IngestEndpointId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RotateIngestEndpointCredentialsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RotateIngestEndpointCredentialsRequestTypeDef"]
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
class UpdateChannelRequest:
    boto3_raw_data: "type_defs.UpdateChannelRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigureLogsRequest:
    boto3_raw_data: "type_defs.ConfigureLogsRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    @cached_property
    def IngressAccessLogs(self):  # pragma: no cover
        return IngressAccessLogs.make_one(self.boto3_raw_data["IngressAccessLogs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigureLogsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigureLogsRequestTypeDef"]
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
class CreateHarvestJobRequest:
    boto3_raw_data: "type_defs.CreateHarvestJobRequestTypeDef" = dataclasses.field()

    EndTime = field("EndTime")
    Id = field("Id")
    OriginEndpointId = field("OriginEndpointId")

    @cached_property
    def S3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["S3Destination"])

    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHarvestJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHarvestJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHarvestJobResponse:
    boto3_raw_data: "type_defs.CreateHarvestJobResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelId = field("ChannelId")
    CreatedAt = field("CreatedAt")
    EndTime = field("EndTime")
    Id = field("Id")
    OriginEndpointId = field("OriginEndpointId")

    @cached_property
    def S3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["S3Destination"])

    StartTime = field("StartTime")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHarvestJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHarvestJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeHarvestJobResponse:
    boto3_raw_data: "type_defs.DescribeHarvestJobResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelId = field("ChannelId")
    CreatedAt = field("CreatedAt")
    EndTime = field("EndTime")
    Id = field("Id")
    OriginEndpointId = field("OriginEndpointId")

    @cached_property
    def S3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["S3Destination"])

    StartTime = field("StartTime")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeHarvestJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeHarvestJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HarvestJob:
    boto3_raw_data: "type_defs.HarvestJobTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ChannelId = field("ChannelId")
    CreatedAt = field("CreatedAt")
    EndTime = field("EndTime")
    Id = field("Id")
    OriginEndpointId = field("OriginEndpointId")

    @cached_property
    def S3Destination(self):  # pragma: no cover
        return S3Destination.make_one(self.boto3_raw_data["S3Destination"])

    StartTime = field("StartTime")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HarvestJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HarvestJobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpekeKeyProviderOutput:
    boto3_raw_data: "type_defs.SpekeKeyProviderOutputTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    RoleArn = field("RoleArn")
    SystemIds = field("SystemIds")
    Url = field("Url")
    CertificateArn = field("CertificateArn")

    @cached_property
    def EncryptionContractConfiguration(self):  # pragma: no cover
        return EncryptionContractConfiguration.make_one(
            self.boto3_raw_data["EncryptionContractConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpekeKeyProviderOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpekeKeyProviderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpekeKeyProvider:
    boto3_raw_data: "type_defs.SpekeKeyProviderTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    RoleArn = field("RoleArn")
    SystemIds = field("SystemIds")
    Url = field("Url")
    CertificateArn = field("CertificateArn")

    @cached_property
    def EncryptionContractConfiguration(self):  # pragma: no cover
        return EncryptionContractConfiguration.make_one(
            self.boto3_raw_data["EncryptionContractConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpekeKeyProviderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpekeKeyProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsIngest:
    boto3_raw_data: "type_defs.HlsIngestTypeDef" = dataclasses.field()

    @cached_property
    def IngestEndpoints(self):  # pragma: no cover
        return IngestEndpoint.make_many(self.boto3_raw_data["IngestEndpoints"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsIngestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HlsIngestTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsRequestPaginate:
    boto3_raw_data: "type_defs.ListChannelsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHarvestJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListHarvestJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    IncludeChannelId = field("IncludeChannelId")
    IncludeStatus = field("IncludeStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListHarvestJobsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHarvestJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOriginEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.ListOriginEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ChannelId = field("ChannelId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOriginEndpointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOriginEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHarvestJobsResponse:
    boto3_raw_data: "type_defs.ListHarvestJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def HarvestJobs(self):  # pragma: no cover
        return HarvestJob.make_many(self.boto3_raw_data["HarvestJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHarvestJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHarvestJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafEncryptionOutput:
    boto3_raw_data: "type_defs.CmafEncryptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProviderOutput.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    ConstantInitializationVector = field("ConstantInitializationVector")
    EncryptionMethod = field("EncryptionMethod")
    KeyRotationIntervalSeconds = field("KeyRotationIntervalSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CmafEncryptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafEncryptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashEncryptionOutput:
    boto3_raw_data: "type_defs.DashEncryptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProviderOutput.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    KeyRotationIntervalSeconds = field("KeyRotationIntervalSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DashEncryptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashEncryptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsEncryptionOutput:
    boto3_raw_data: "type_defs.HlsEncryptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProviderOutput.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    ConstantInitializationVector = field("ConstantInitializationVector")
    EncryptionMethod = field("EncryptionMethod")
    KeyRotationIntervalSeconds = field("KeyRotationIntervalSeconds")
    RepeatExtXKey = field("RepeatExtXKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsEncryptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsEncryptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MssEncryptionOutput:
    boto3_raw_data: "type_defs.MssEncryptionOutputTypeDef" = dataclasses.field()

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProviderOutput.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MssEncryptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MssEncryptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashEncryption:
    boto3_raw_data: "type_defs.DashEncryptionTypeDef" = dataclasses.field()

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProvider.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    KeyRotationIntervalSeconds = field("KeyRotationIntervalSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashEncryptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DashEncryptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsEncryption:
    boto3_raw_data: "type_defs.HlsEncryptionTypeDef" = dataclasses.field()

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProvider.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    ConstantInitializationVector = field("ConstantInitializationVector")
    EncryptionMethod = field("EncryptionMethod")
    KeyRotationIntervalSeconds = field("KeyRotationIntervalSeconds")
    RepeatExtXKey = field("RepeatExtXKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsEncryptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HlsEncryptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MssEncryption:
    boto3_raw_data: "type_defs.MssEncryptionTypeDef" = dataclasses.field()

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProvider.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MssEncryptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MssEncryptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Channel:
    boto3_raw_data: "type_defs.ChannelTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    @cached_property
    def HlsIngest(self):  # pragma: no cover
        return HlsIngest.make_one(self.boto3_raw_data["HlsIngest"])

    Id = field("Id")

    @cached_property
    def IngressAccessLogs(self):  # pragma: no cover
        return IngressAccessLogs.make_one(self.boto3_raw_data["IngressAccessLogs"])

    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigureLogsResponse:
    boto3_raw_data: "type_defs.ConfigureLogsResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    @cached_property
    def HlsIngest(self):  # pragma: no cover
        return HlsIngest.make_one(self.boto3_raw_data["HlsIngest"])

    Id = field("Id")

    @cached_property
    def IngressAccessLogs(self):  # pragma: no cover
        return IngressAccessLogs.make_one(self.boto3_raw_data["IngressAccessLogs"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigureLogsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigureLogsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelResponse:
    boto3_raw_data: "type_defs.CreateChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    @cached_property
    def HlsIngest(self):  # pragma: no cover
        return HlsIngest.make_one(self.boto3_raw_data["HlsIngest"])

    Id = field("Id")

    @cached_property
    def IngressAccessLogs(self):  # pragma: no cover
        return IngressAccessLogs.make_one(self.boto3_raw_data["IngressAccessLogs"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChannelResponse:
    boto3_raw_data: "type_defs.DescribeChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    @cached_property
    def HlsIngest(self):  # pragma: no cover
        return HlsIngest.make_one(self.boto3_raw_data["HlsIngest"])

    Id = field("Id")

    @cached_property
    def IngressAccessLogs(self):  # pragma: no cover
        return IngressAccessLogs.make_one(self.boto3_raw_data["IngressAccessLogs"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RotateChannelCredentialsResponse:
    boto3_raw_data: "type_defs.RotateChannelCredentialsResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    @cached_property
    def HlsIngest(self):  # pragma: no cover
        return HlsIngest.make_one(self.boto3_raw_data["HlsIngest"])

    Id = field("Id")

    @cached_property
    def IngressAccessLogs(self):  # pragma: no cover
        return IngressAccessLogs.make_one(self.boto3_raw_data["IngressAccessLogs"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RotateChannelCredentialsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RotateChannelCredentialsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RotateIngestEndpointCredentialsResponse:
    boto3_raw_data: "type_defs.RotateIngestEndpointCredentialsResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    @cached_property
    def HlsIngest(self):  # pragma: no cover
        return HlsIngest.make_one(self.boto3_raw_data["HlsIngest"])

    Id = field("Id")

    @cached_property
    def IngressAccessLogs(self):  # pragma: no cover
        return IngressAccessLogs.make_one(self.boto3_raw_data["IngressAccessLogs"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RotateIngestEndpointCredentialsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RotateIngestEndpointCredentialsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelResponse:
    boto3_raw_data: "type_defs.UpdateChannelResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Description = field("Description")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    @cached_property
    def HlsIngest(self):  # pragma: no cover
        return HlsIngest.make_one(self.boto3_raw_data["HlsIngest"])

    Id = field("Id")

    @cached_property
    def IngressAccessLogs(self):  # pragma: no cover
        return IngressAccessLogs.make_one(self.boto3_raw_data["IngressAccessLogs"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafPackage:
    boto3_raw_data: "type_defs.CmafPackageTypeDef" = dataclasses.field()

    @cached_property
    def Encryption(self):  # pragma: no cover
        return CmafEncryptionOutput.make_one(self.boto3_raw_data["Encryption"])

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return HlsManifest.make_many(self.boto3_raw_data["HlsManifests"])

    SegmentDurationSeconds = field("SegmentDurationSeconds")
    SegmentPrefix = field("SegmentPrefix")

    @cached_property
    def StreamSelection(self):  # pragma: no cover
        return StreamSelection.make_one(self.boto3_raw_data["StreamSelection"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CmafPackageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CmafPackageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashPackageOutput:
    boto3_raw_data: "type_defs.DashPackageOutputTypeDef" = dataclasses.field()

    AdTriggers = field("AdTriggers")
    AdsOnDeliveryRestrictions = field("AdsOnDeliveryRestrictions")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return DashEncryptionOutput.make_one(self.boto3_raw_data["Encryption"])

    IncludeIframeOnlyStream = field("IncludeIframeOnlyStream")
    ManifestLayout = field("ManifestLayout")
    ManifestWindowSeconds = field("ManifestWindowSeconds")
    MinBufferTimeSeconds = field("MinBufferTimeSeconds")
    MinUpdatePeriodSeconds = field("MinUpdatePeriodSeconds")
    PeriodTriggers = field("PeriodTriggers")
    Profile = field("Profile")
    SegmentDurationSeconds = field("SegmentDurationSeconds")
    SegmentTemplateFormat = field("SegmentTemplateFormat")

    @cached_property
    def StreamSelection(self):  # pragma: no cover
        return StreamSelection.make_one(self.boto3_raw_data["StreamSelection"])

    SuggestedPresentationDelaySeconds = field("SuggestedPresentationDelaySeconds")
    UtcTiming = field("UtcTiming")
    UtcTimingUri = field("UtcTimingUri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashPackageOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DashPackageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsPackageOutput:
    boto3_raw_data: "type_defs.HlsPackageOutputTypeDef" = dataclasses.field()

    AdMarkers = field("AdMarkers")
    AdTriggers = field("AdTriggers")
    AdsOnDeliveryRestrictions = field("AdsOnDeliveryRestrictions")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return HlsEncryptionOutput.make_one(self.boto3_raw_data["Encryption"])

    IncludeDvbSubtitles = field("IncludeDvbSubtitles")
    IncludeIframeOnlyStream = field("IncludeIframeOnlyStream")
    PlaylistType = field("PlaylistType")
    PlaylistWindowSeconds = field("PlaylistWindowSeconds")
    ProgramDateTimeIntervalSeconds = field("ProgramDateTimeIntervalSeconds")
    SegmentDurationSeconds = field("SegmentDurationSeconds")

    @cached_property
    def StreamSelection(self):  # pragma: no cover
        return StreamSelection.make_one(self.boto3_raw_data["StreamSelection"])

    UseAudioRenditionGroup = field("UseAudioRenditionGroup")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsPackageOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsPackageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MssPackageOutput:
    boto3_raw_data: "type_defs.MssPackageOutputTypeDef" = dataclasses.field()

    @cached_property
    def Encryption(self):  # pragma: no cover
        return MssEncryptionOutput.make_one(self.boto3_raw_data["Encryption"])

    ManifestWindowSeconds = field("ManifestWindowSeconds")
    SegmentDurationSeconds = field("SegmentDurationSeconds")

    @cached_property
    def StreamSelection(self):  # pragma: no cover
        return StreamSelection.make_one(self.boto3_raw_data["StreamSelection"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MssPackageOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MssPackageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashPackage:
    boto3_raw_data: "type_defs.DashPackageTypeDef" = dataclasses.field()

    AdTriggers = field("AdTriggers")
    AdsOnDeliveryRestrictions = field("AdsOnDeliveryRestrictions")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return DashEncryption.make_one(self.boto3_raw_data["Encryption"])

    IncludeIframeOnlyStream = field("IncludeIframeOnlyStream")
    ManifestLayout = field("ManifestLayout")
    ManifestWindowSeconds = field("ManifestWindowSeconds")
    MinBufferTimeSeconds = field("MinBufferTimeSeconds")
    MinUpdatePeriodSeconds = field("MinUpdatePeriodSeconds")
    PeriodTriggers = field("PeriodTriggers")
    Profile = field("Profile")
    SegmentDurationSeconds = field("SegmentDurationSeconds")
    SegmentTemplateFormat = field("SegmentTemplateFormat")

    @cached_property
    def StreamSelection(self):  # pragma: no cover
        return StreamSelection.make_one(self.boto3_raw_data["StreamSelection"])

    SuggestedPresentationDelaySeconds = field("SuggestedPresentationDelaySeconds")
    UtcTiming = field("UtcTiming")
    UtcTimingUri = field("UtcTimingUri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashPackageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DashPackageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsPackage:
    boto3_raw_data: "type_defs.HlsPackageTypeDef" = dataclasses.field()

    AdMarkers = field("AdMarkers")
    AdTriggers = field("AdTriggers")
    AdsOnDeliveryRestrictions = field("AdsOnDeliveryRestrictions")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return HlsEncryption.make_one(self.boto3_raw_data["Encryption"])

    IncludeDvbSubtitles = field("IncludeDvbSubtitles")
    IncludeIframeOnlyStream = field("IncludeIframeOnlyStream")
    PlaylistType = field("PlaylistType")
    PlaylistWindowSeconds = field("PlaylistWindowSeconds")
    ProgramDateTimeIntervalSeconds = field("ProgramDateTimeIntervalSeconds")
    SegmentDurationSeconds = field("SegmentDurationSeconds")

    @cached_property
    def StreamSelection(self):  # pragma: no cover
        return StreamSelection.make_one(self.boto3_raw_data["StreamSelection"])

    UseAudioRenditionGroup = field("UseAudioRenditionGroup")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HlsPackageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HlsPackageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MssPackage:
    boto3_raw_data: "type_defs.MssPackageTypeDef" = dataclasses.field()

    @cached_property
    def Encryption(self):  # pragma: no cover
        return MssEncryption.make_one(self.boto3_raw_data["Encryption"])

    ManifestWindowSeconds = field("ManifestWindowSeconds")
    SegmentDurationSeconds = field("SegmentDurationSeconds")

    @cached_property
    def StreamSelection(self):  # pragma: no cover
        return StreamSelection.make_one(self.boto3_raw_data["StreamSelection"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MssPackageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MssPackageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafEncryption:
    boto3_raw_data: "type_defs.CmafEncryptionTypeDef" = dataclasses.field()

    SpekeKeyProvider = field("SpekeKeyProvider")
    ConstantInitializationVector = field("ConstantInitializationVector")
    EncryptionMethod = field("EncryptionMethod")
    KeyRotationIntervalSeconds = field("KeyRotationIntervalSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CmafEncryptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CmafEncryptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsResponse:
    boto3_raw_data: "type_defs.ListChannelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Channels(self):  # pragma: no cover
        return Channel.make_many(self.boto3_raw_data["Channels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOriginEndpointResponse:
    boto3_raw_data: "type_defs.CreateOriginEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    ChannelId = field("ChannelId")

    @cached_property
    def CmafPackage(self):  # pragma: no cover
        return CmafPackage.make_one(self.boto3_raw_data["CmafPackage"])

    CreatedAt = field("CreatedAt")

    @cached_property
    def DashPackage(self):  # pragma: no cover
        return DashPackageOutput.make_one(self.boto3_raw_data["DashPackage"])

    Description = field("Description")

    @cached_property
    def HlsPackage(self):  # pragma: no cover
        return HlsPackageOutput.make_one(self.boto3_raw_data["HlsPackage"])

    Id = field("Id")
    ManifestName = field("ManifestName")

    @cached_property
    def MssPackage(self):  # pragma: no cover
        return MssPackageOutput.make_one(self.boto3_raw_data["MssPackage"])

    Origination = field("Origination")
    StartoverWindowSeconds = field("StartoverWindowSeconds")
    Tags = field("Tags")
    TimeDelaySeconds = field("TimeDelaySeconds")
    Url = field("Url")
    Whitelist = field("Whitelist")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOriginEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOriginEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOriginEndpointResponse:
    boto3_raw_data: "type_defs.DescribeOriginEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    ChannelId = field("ChannelId")

    @cached_property
    def CmafPackage(self):  # pragma: no cover
        return CmafPackage.make_one(self.boto3_raw_data["CmafPackage"])

    CreatedAt = field("CreatedAt")

    @cached_property
    def DashPackage(self):  # pragma: no cover
        return DashPackageOutput.make_one(self.boto3_raw_data["DashPackage"])

    Description = field("Description")

    @cached_property
    def HlsPackage(self):  # pragma: no cover
        return HlsPackageOutput.make_one(self.boto3_raw_data["HlsPackage"])

    Id = field("Id")
    ManifestName = field("ManifestName")

    @cached_property
    def MssPackage(self):  # pragma: no cover
        return MssPackageOutput.make_one(self.boto3_raw_data["MssPackage"])

    Origination = field("Origination")
    StartoverWindowSeconds = field("StartoverWindowSeconds")
    Tags = field("Tags")
    TimeDelaySeconds = field("TimeDelaySeconds")
    Url = field("Url")
    Whitelist = field("Whitelist")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeOriginEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOriginEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginEndpoint:
    boto3_raw_data: "type_defs.OriginEndpointTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    ChannelId = field("ChannelId")

    @cached_property
    def CmafPackage(self):  # pragma: no cover
        return CmafPackage.make_one(self.boto3_raw_data["CmafPackage"])

    CreatedAt = field("CreatedAt")

    @cached_property
    def DashPackage(self):  # pragma: no cover
        return DashPackageOutput.make_one(self.boto3_raw_data["DashPackage"])

    Description = field("Description")

    @cached_property
    def HlsPackage(self):  # pragma: no cover
        return HlsPackageOutput.make_one(self.boto3_raw_data["HlsPackage"])

    Id = field("Id")
    ManifestName = field("ManifestName")

    @cached_property
    def MssPackage(self):  # pragma: no cover
        return MssPackageOutput.make_one(self.boto3_raw_data["MssPackage"])

    Origination = field("Origination")
    StartoverWindowSeconds = field("StartoverWindowSeconds")
    Tags = field("Tags")
    TimeDelaySeconds = field("TimeDelaySeconds")
    Url = field("Url")
    Whitelist = field("Whitelist")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OriginEndpointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOriginEndpointResponse:
    boto3_raw_data: "type_defs.UpdateOriginEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    ChannelId = field("ChannelId")

    @cached_property
    def CmafPackage(self):  # pragma: no cover
        return CmafPackage.make_one(self.boto3_raw_data["CmafPackage"])

    CreatedAt = field("CreatedAt")

    @cached_property
    def DashPackage(self):  # pragma: no cover
        return DashPackageOutput.make_one(self.boto3_raw_data["DashPackage"])

    Description = field("Description")

    @cached_property
    def HlsPackage(self):  # pragma: no cover
        return HlsPackageOutput.make_one(self.boto3_raw_data["HlsPackage"])

    Id = field("Id")
    ManifestName = field("ManifestName")

    @cached_property
    def MssPackage(self):  # pragma: no cover
        return MssPackageOutput.make_one(self.boto3_raw_data["MssPackage"])

    Origination = field("Origination")
    StartoverWindowSeconds = field("StartoverWindowSeconds")
    Tags = field("Tags")
    TimeDelaySeconds = field("TimeDelaySeconds")
    Url = field("Url")
    Whitelist = field("Whitelist")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOriginEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOriginEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOriginEndpointsResponse:
    boto3_raw_data: "type_defs.ListOriginEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def OriginEndpoints(self):  # pragma: no cover
        return OriginEndpoint.make_many(self.boto3_raw_data["OriginEndpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOriginEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOriginEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CmafPackageCreateOrUpdateParameters:
    boto3_raw_data: "type_defs.CmafPackageCreateOrUpdateParametersTypeDef" = (
        dataclasses.field()
    )

    Encryption = field("Encryption")

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return HlsManifestCreateOrUpdateParameters.make_many(
            self.boto3_raw_data["HlsManifests"]
        )

    SegmentDurationSeconds = field("SegmentDurationSeconds")
    SegmentPrefix = field("SegmentPrefix")

    @cached_property
    def StreamSelection(self):  # pragma: no cover
        return StreamSelection.make_one(self.boto3_raw_data["StreamSelection"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CmafPackageCreateOrUpdateParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafPackageCreateOrUpdateParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOriginEndpointRequest:
    boto3_raw_data: "type_defs.CreateOriginEndpointRequestTypeDef" = dataclasses.field()

    ChannelId = field("ChannelId")
    Id = field("Id")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    @cached_property
    def CmafPackage(self):  # pragma: no cover
        return CmafPackageCreateOrUpdateParameters.make_one(
            self.boto3_raw_data["CmafPackage"]
        )

    DashPackage = field("DashPackage")
    Description = field("Description")
    HlsPackage = field("HlsPackage")
    ManifestName = field("ManifestName")
    MssPackage = field("MssPackage")
    Origination = field("Origination")
    StartoverWindowSeconds = field("StartoverWindowSeconds")
    Tags = field("Tags")
    TimeDelaySeconds = field("TimeDelaySeconds")
    Whitelist = field("Whitelist")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOriginEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOriginEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOriginEndpointRequest:
    boto3_raw_data: "type_defs.UpdateOriginEndpointRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    @cached_property
    def CmafPackage(self):  # pragma: no cover
        return CmafPackageCreateOrUpdateParameters.make_one(
            self.boto3_raw_data["CmafPackage"]
        )

    DashPackage = field("DashPackage")
    Description = field("Description")
    HlsPackage = field("HlsPackage")
    ManifestName = field("ManifestName")
    MssPackage = field("MssPackage")
    Origination = field("Origination")
    StartoverWindowSeconds = field("StartoverWindowSeconds")
    TimeDelaySeconds = field("TimeDelaySeconds")
    Whitelist = field("Whitelist")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateOriginEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOriginEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
