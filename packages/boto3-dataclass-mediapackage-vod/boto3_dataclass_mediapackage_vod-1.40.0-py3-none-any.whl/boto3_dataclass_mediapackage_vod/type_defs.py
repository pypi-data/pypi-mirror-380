# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediapackage_vod import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssetShallow:
    boto3_raw_data: "type_defs.AssetShallowTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")
    Id = field("Id")
    PackagingGroupId = field("PackagingGroupId")
    ResourceId = field("ResourceId")
    SourceArn = field("SourceArn")
    SourceRoleArn = field("SourceRoleArn")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetShallowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetShallowTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


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
class CreateAssetRequest:
    boto3_raw_data: "type_defs.CreateAssetRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    PackagingGroupId = field("PackagingGroupId")
    SourceArn = field("SourceArn")
    SourceRoleArn = field("SourceRoleArn")
    ResourceId = field("ResourceId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EgressEndpoint:
    boto3_raw_data: "type_defs.EgressEndpointTypeDef" = dataclasses.field()

    PackagingConfigurationId = field("PackagingConfigurationId")
    Status = field("Status")
    Url = field("Url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EgressEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EgressEndpointTypeDef"]],
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
class DeleteAssetRequest:
    boto3_raw_data: "type_defs.DeleteAssetRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackagingConfigurationRequest:
    boto3_raw_data: "type_defs.DeletePackagingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePackagingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackagingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePackagingGroupRequest:
    boto3_raw_data: "type_defs.DeletePackagingGroupRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePackagingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePackagingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetRequest:
    boto3_raw_data: "type_defs.DescribeAssetRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAssetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackagingConfigurationRequest:
    boto3_raw_data: "type_defs.DescribePackagingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePackagingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackagingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackagingGroupRequest:
    boto3_raw_data: "type_defs.DescribePackagingGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePackagingGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackagingGroupRequestTypeDef"]
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
class ListAssetsRequest:
    boto3_raw_data: "type_defs.ListAssetsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    PackagingGroupId = field("PackagingGroupId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAssetsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagingConfigurationsRequest:
    boto3_raw_data: "type_defs.ListPackagingConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    PackagingGroupId = field("PackagingGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPackagingConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagingConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagingGroupsRequest:
    boto3_raw_data: "type_defs.ListPackagingGroupsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackagingGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagingGroupsRequestTypeDef"]
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
class UpdatePackagingGroupRequest:
    boto3_raw_data: "type_defs.UpdatePackagingGroupRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePackagingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackagingGroupRequestTypeDef"]
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
class CreatePackagingGroupRequest:
    boto3_raw_data: "type_defs.CreatePackagingGroupRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackagingGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackagingGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackagingGroup:
    boto3_raw_data: "type_defs.PackagingGroupTypeDef" = dataclasses.field()

    ApproximateAssetCount = field("ApproximateAssetCount")
    Arn = field("Arn")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    CreatedAt = field("CreatedAt")
    DomainName = field("DomainName")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    Id = field("Id")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PackagingGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PackagingGroupTypeDef"]],
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

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    CreatedAt = field("CreatedAt")
    DomainName = field("DomainName")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    Id = field("Id")
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
class CreatePackagingGroupResponse:
    boto3_raw_data: "type_defs.CreatePackagingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    CreatedAt = field("CreatedAt")
    DomainName = field("DomainName")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    Id = field("Id")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePackagingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackagingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackagingGroupResponse:
    boto3_raw_data: "type_defs.DescribePackagingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    ApproximateAssetCount = field("ApproximateAssetCount")
    Arn = field("Arn")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    CreatedAt = field("CreatedAt")
    DomainName = field("DomainName")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    Id = field("Id")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePackagingGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackagingGroupResponseTypeDef"]
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
class ListAssetsResponse:
    boto3_raw_data: "type_defs.ListAssetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Assets(self):  # pragma: no cover
        return AssetShallow.make_many(self.boto3_raw_data["Assets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetsResponseTypeDef"]
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
class UpdatePackagingGroupResponse:
    boto3_raw_data: "type_defs.UpdatePackagingGroupResponseTypeDef" = (
        dataclasses.field()
    )

    ApproximateAssetCount = field("ApproximateAssetCount")
    Arn = field("Arn")

    @cached_property
    def Authorization(self):  # pragma: no cover
        return Authorization.make_one(self.boto3_raw_data["Authorization"])

    CreatedAt = field("CreatedAt")
    DomainName = field("DomainName")

    @cached_property
    def EgressAccessLogs(self):  # pragma: no cover
        return EgressAccessLogs.make_one(self.boto3_raw_data["EgressAccessLogs"])

    Id = field("Id")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePackagingGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePackagingGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetResponse:
    boto3_raw_data: "type_defs.CreateAssetResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def EgressEndpoints(self):  # pragma: no cover
        return EgressEndpoint.make_many(self.boto3_raw_data["EgressEndpoints"])

    Id = field("Id")
    PackagingGroupId = field("PackagingGroupId")
    ResourceId = field("ResourceId")
    SourceArn = field("SourceArn")
    SourceRoleArn = field("SourceRoleArn")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAssetResponse:
    boto3_raw_data: "type_defs.DescribeAssetResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedAt = field("CreatedAt")

    @cached_property
    def EgressEndpoints(self):  # pragma: no cover
        return EgressEndpoint.make_many(self.boto3_raw_data["EgressEndpoints"])

    Id = field("Id")
    PackagingGroupId = field("PackagingGroupId")
    ResourceId = field("ResourceId")
    SourceArn = field("SourceArn")
    SourceRoleArn = field("SourceRoleArn")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAssetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAssetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashManifest:
    boto3_raw_data: "type_defs.DashManifestTypeDef" = dataclasses.field()

    ManifestLayout = field("ManifestLayout")
    ManifestName = field("ManifestName")
    MinBufferTimeSeconds = field("MinBufferTimeSeconds")
    Profile = field("Profile")
    ScteMarkersSource = field("ScteMarkersSource")

    @cached_property
    def StreamSelection(self):  # pragma: no cover
        return StreamSelection.make_one(self.boto3_raw_data["StreamSelection"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashManifestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DashManifestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsManifest:
    boto3_raw_data: "type_defs.HlsManifestTypeDef" = dataclasses.field()

    AdMarkers = field("AdMarkers")
    IncludeIframeOnlyStream = field("IncludeIframeOnlyStream")
    ManifestName = field("ManifestName")
    ProgramDateTimeIntervalSeconds = field("ProgramDateTimeIntervalSeconds")
    RepeatExtXKey = field("RepeatExtXKey")

    @cached_property
    def StreamSelection(self):  # pragma: no cover
        return StreamSelection.make_one(self.boto3_raw_data["StreamSelection"])

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
class MssManifest:
    boto3_raw_data: "type_defs.MssManifestTypeDef" = dataclasses.field()

    ManifestName = field("ManifestName")

    @cached_property
    def StreamSelection(self):  # pragma: no cover
        return StreamSelection.make_one(self.boto3_raw_data["StreamSelection"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MssManifestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MssManifestTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpekeKeyProviderOutput:
    boto3_raw_data: "type_defs.SpekeKeyProviderOutputTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    SystemIds = field("SystemIds")
    Url = field("Url")

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

    RoleArn = field("RoleArn")
    SystemIds = field("SystemIds")
    Url = field("Url")

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
class ListAssetsRequestPaginate:
    boto3_raw_data: "type_defs.ListAssetsRequestPaginateTypeDef" = dataclasses.field()

    PackagingGroupId = field("PackagingGroupId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagingConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListPackagingConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PackagingGroupId = field("PackagingGroupId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPackagingConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagingConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagingGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListPackagingGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPackagingGroupsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagingGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagingGroupsResponse:
    boto3_raw_data: "type_defs.ListPackagingGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def PackagingGroups(self):  # pragma: no cover
        return PackagingGroup.make_many(self.boto3_raw_data["PackagingGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPackagingGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagingGroupsResponseTypeDef"]
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
class CmafEncryption:
    boto3_raw_data: "type_defs.CmafEncryptionTypeDef" = dataclasses.field()

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProvider.make_one(self.boto3_raw_data["SpekeKeyProvider"])

    ConstantInitializationVector = field("ConstantInitializationVector")

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
class DashEncryption:
    boto3_raw_data: "type_defs.DashEncryptionTypeDef" = dataclasses.field()

    @cached_property
    def SpekeKeyProvider(self):  # pragma: no cover
        return SpekeKeyProvider.make_one(self.boto3_raw_data["SpekeKeyProvider"])

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
class CmafPackageOutput:
    boto3_raw_data: "type_defs.CmafPackageOutputTypeDef" = dataclasses.field()

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return HlsManifest.make_many(self.boto3_raw_data["HlsManifests"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return CmafEncryptionOutput.make_one(self.boto3_raw_data["Encryption"])

    IncludeEncoderConfigurationInSegments = field(
        "IncludeEncoderConfigurationInSegments"
    )
    SegmentDurationSeconds = field("SegmentDurationSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CmafPackageOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CmafPackageOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashPackageOutput:
    boto3_raw_data: "type_defs.DashPackageOutputTypeDef" = dataclasses.field()

    @cached_property
    def DashManifests(self):  # pragma: no cover
        return DashManifest.make_many(self.boto3_raw_data["DashManifests"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return DashEncryptionOutput.make_one(self.boto3_raw_data["Encryption"])

    IncludeEncoderConfigurationInSegments = field(
        "IncludeEncoderConfigurationInSegments"
    )
    IncludeIframeOnlyStream = field("IncludeIframeOnlyStream")
    PeriodTriggers = field("PeriodTriggers")
    SegmentDurationSeconds = field("SegmentDurationSeconds")
    SegmentTemplateFormat = field("SegmentTemplateFormat")

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

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return HlsManifest.make_many(self.boto3_raw_data["HlsManifests"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return HlsEncryptionOutput.make_one(self.boto3_raw_data["Encryption"])

    IncludeDvbSubtitles = field("IncludeDvbSubtitles")
    SegmentDurationSeconds = field("SegmentDurationSeconds")
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
    def MssManifests(self):  # pragma: no cover
        return MssManifest.make_many(self.boto3_raw_data["MssManifests"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return MssEncryptionOutput.make_one(self.boto3_raw_data["Encryption"])

    SegmentDurationSeconds = field("SegmentDurationSeconds")

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
class CmafPackage:
    boto3_raw_data: "type_defs.CmafPackageTypeDef" = dataclasses.field()

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return HlsManifest.make_many(self.boto3_raw_data["HlsManifests"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return CmafEncryption.make_one(self.boto3_raw_data["Encryption"])

    IncludeEncoderConfigurationInSegments = field(
        "IncludeEncoderConfigurationInSegments"
    )
    SegmentDurationSeconds = field("SegmentDurationSeconds")

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
class DashPackage:
    boto3_raw_data: "type_defs.DashPackageTypeDef" = dataclasses.field()

    @cached_property
    def DashManifests(self):  # pragma: no cover
        return DashManifest.make_many(self.boto3_raw_data["DashManifests"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return DashEncryption.make_one(self.boto3_raw_data["Encryption"])

    IncludeEncoderConfigurationInSegments = field(
        "IncludeEncoderConfigurationInSegments"
    )
    IncludeIframeOnlyStream = field("IncludeIframeOnlyStream")
    PeriodTriggers = field("PeriodTriggers")
    SegmentDurationSeconds = field("SegmentDurationSeconds")
    SegmentTemplateFormat = field("SegmentTemplateFormat")

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

    @cached_property
    def HlsManifests(self):  # pragma: no cover
        return HlsManifest.make_many(self.boto3_raw_data["HlsManifests"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return HlsEncryption.make_one(self.boto3_raw_data["Encryption"])

    IncludeDvbSubtitles = field("IncludeDvbSubtitles")
    SegmentDurationSeconds = field("SegmentDurationSeconds")
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
    def MssManifests(self):  # pragma: no cover
        return MssManifest.make_many(self.boto3_raw_data["MssManifests"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return MssEncryption.make_one(self.boto3_raw_data["Encryption"])

    SegmentDurationSeconds = field("SegmentDurationSeconds")

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
class CreatePackagingConfigurationResponse:
    boto3_raw_data: "type_defs.CreatePackagingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def CmafPackage(self):  # pragma: no cover
        return CmafPackageOutput.make_one(self.boto3_raw_data["CmafPackage"])

    CreatedAt = field("CreatedAt")

    @cached_property
    def DashPackage(self):  # pragma: no cover
        return DashPackageOutput.make_one(self.boto3_raw_data["DashPackage"])

    @cached_property
    def HlsPackage(self):  # pragma: no cover
        return HlsPackageOutput.make_one(self.boto3_raw_data["HlsPackage"])

    Id = field("Id")

    @cached_property
    def MssPackage(self):  # pragma: no cover
        return MssPackageOutput.make_one(self.boto3_raw_data["MssPackage"])

    PackagingGroupId = field("PackagingGroupId")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePackagingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackagingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePackagingConfigurationResponse:
    boto3_raw_data: "type_defs.DescribePackagingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def CmafPackage(self):  # pragma: no cover
        return CmafPackageOutput.make_one(self.boto3_raw_data["CmafPackage"])

    CreatedAt = field("CreatedAt")

    @cached_property
    def DashPackage(self):  # pragma: no cover
        return DashPackageOutput.make_one(self.boto3_raw_data["DashPackage"])

    @cached_property
    def HlsPackage(self):  # pragma: no cover
        return HlsPackageOutput.make_one(self.boto3_raw_data["HlsPackage"])

    Id = field("Id")

    @cached_property
    def MssPackage(self):  # pragma: no cover
        return MssPackageOutput.make_one(self.boto3_raw_data["MssPackage"])

    PackagingGroupId = field("PackagingGroupId")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePackagingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePackagingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PackagingConfiguration:
    boto3_raw_data: "type_defs.PackagingConfigurationTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def CmafPackage(self):  # pragma: no cover
        return CmafPackageOutput.make_one(self.boto3_raw_data["CmafPackage"])

    CreatedAt = field("CreatedAt")

    @cached_property
    def DashPackage(self):  # pragma: no cover
        return DashPackageOutput.make_one(self.boto3_raw_data["DashPackage"])

    @cached_property
    def HlsPackage(self):  # pragma: no cover
        return HlsPackageOutput.make_one(self.boto3_raw_data["HlsPackage"])

    Id = field("Id")

    @cached_property
    def MssPackage(self):  # pragma: no cover
        return MssPackageOutput.make_one(self.boto3_raw_data["MssPackage"])

    PackagingGroupId = field("PackagingGroupId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PackagingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PackagingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPackagingConfigurationsResponse:
    boto3_raw_data: "type_defs.ListPackagingConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PackagingConfigurations(self):  # pragma: no cover
        return PackagingConfiguration.make_many(
            self.boto3_raw_data["PackagingConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPackagingConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPackagingConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePackagingConfigurationRequest:
    boto3_raw_data: "type_defs.CreatePackagingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    PackagingGroupId = field("PackagingGroupId")
    CmafPackage = field("CmafPackage")
    DashPackage = field("DashPackage")
    HlsPackage = field("HlsPackage")
    MssPackage = field("MssPackage")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePackagingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePackagingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
