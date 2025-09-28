# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediapackage_vod import type_defs as bs_td


class MEDIAPACKAGE_VODCaster:

    def configure_logs(
        self,
        res: "bs_td.ConfigureLogsResponseTypeDef",
    ) -> "dc_td.ConfigureLogsResponse":
        return dc_td.ConfigureLogsResponse.make_one(res)

    def create_asset(
        self,
        res: "bs_td.CreateAssetResponseTypeDef",
    ) -> "dc_td.CreateAssetResponse":
        return dc_td.CreateAssetResponse.make_one(res)

    def create_packaging_configuration(
        self,
        res: "bs_td.CreatePackagingConfigurationResponseTypeDef",
    ) -> "dc_td.CreatePackagingConfigurationResponse":
        return dc_td.CreatePackagingConfigurationResponse.make_one(res)

    def create_packaging_group(
        self,
        res: "bs_td.CreatePackagingGroupResponseTypeDef",
    ) -> "dc_td.CreatePackagingGroupResponse":
        return dc_td.CreatePackagingGroupResponse.make_one(res)

    def describe_asset(
        self,
        res: "bs_td.DescribeAssetResponseTypeDef",
    ) -> "dc_td.DescribeAssetResponse":
        return dc_td.DescribeAssetResponse.make_one(res)

    def describe_packaging_configuration(
        self,
        res: "bs_td.DescribePackagingConfigurationResponseTypeDef",
    ) -> "dc_td.DescribePackagingConfigurationResponse":
        return dc_td.DescribePackagingConfigurationResponse.make_one(res)

    def describe_packaging_group(
        self,
        res: "bs_td.DescribePackagingGroupResponseTypeDef",
    ) -> "dc_td.DescribePackagingGroupResponse":
        return dc_td.DescribePackagingGroupResponse.make_one(res)

    def list_assets(
        self,
        res: "bs_td.ListAssetsResponseTypeDef",
    ) -> "dc_td.ListAssetsResponse":
        return dc_td.ListAssetsResponse.make_one(res)

    def list_packaging_configurations(
        self,
        res: "bs_td.ListPackagingConfigurationsResponseTypeDef",
    ) -> "dc_td.ListPackagingConfigurationsResponse":
        return dc_td.ListPackagingConfigurationsResponse.make_one(res)

    def list_packaging_groups(
        self,
        res: "bs_td.ListPackagingGroupsResponseTypeDef",
    ) -> "dc_td.ListPackagingGroupsResponse":
        return dc_td.ListPackagingGroupsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_packaging_group(
        self,
        res: "bs_td.UpdatePackagingGroupResponseTypeDef",
    ) -> "dc_td.UpdatePackagingGroupResponse":
        return dc_td.UpdatePackagingGroupResponse.make_one(res)


mediapackage_vod_caster = MEDIAPACKAGE_VODCaster()
