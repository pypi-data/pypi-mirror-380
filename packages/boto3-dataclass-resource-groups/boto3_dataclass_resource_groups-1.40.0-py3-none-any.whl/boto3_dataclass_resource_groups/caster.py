# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_resource_groups import type_defs as bs_td


class RESOURCE_GROUPSCaster:

    def cancel_tag_sync_task(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_group(
        self,
        res: "bs_td.CreateGroupOutputTypeDef",
    ) -> "dc_td.CreateGroupOutput":
        return dc_td.CreateGroupOutput.make_one(res)

    def delete_group(
        self,
        res: "bs_td.DeleteGroupOutputTypeDef",
    ) -> "dc_td.DeleteGroupOutput":
        return dc_td.DeleteGroupOutput.make_one(res)

    def get_account_settings(
        self,
        res: "bs_td.GetAccountSettingsOutputTypeDef",
    ) -> "dc_td.GetAccountSettingsOutput":
        return dc_td.GetAccountSettingsOutput.make_one(res)

    def get_group(
        self,
        res: "bs_td.GetGroupOutputTypeDef",
    ) -> "dc_td.GetGroupOutput":
        return dc_td.GetGroupOutput.make_one(res)

    def get_group_configuration(
        self,
        res: "bs_td.GetGroupConfigurationOutputTypeDef",
    ) -> "dc_td.GetGroupConfigurationOutput":
        return dc_td.GetGroupConfigurationOutput.make_one(res)

    def get_group_query(
        self,
        res: "bs_td.GetGroupQueryOutputTypeDef",
    ) -> "dc_td.GetGroupQueryOutput":
        return dc_td.GetGroupQueryOutput.make_one(res)

    def get_tag_sync_task(
        self,
        res: "bs_td.GetTagSyncTaskOutputTypeDef",
    ) -> "dc_td.GetTagSyncTaskOutput":
        return dc_td.GetTagSyncTaskOutput.make_one(res)

    def get_tags(
        self,
        res: "bs_td.GetTagsOutputTypeDef",
    ) -> "dc_td.GetTagsOutput":
        return dc_td.GetTagsOutput.make_one(res)

    def group_resources(
        self,
        res: "bs_td.GroupResourcesOutputTypeDef",
    ) -> "dc_td.GroupResourcesOutput":
        return dc_td.GroupResourcesOutput.make_one(res)

    def list_group_resources(
        self,
        res: "bs_td.ListGroupResourcesOutputTypeDef",
    ) -> "dc_td.ListGroupResourcesOutput":
        return dc_td.ListGroupResourcesOutput.make_one(res)

    def list_grouping_statuses(
        self,
        res: "bs_td.ListGroupingStatusesOutputTypeDef",
    ) -> "dc_td.ListGroupingStatusesOutput":
        return dc_td.ListGroupingStatusesOutput.make_one(res)

    def list_groups(
        self,
        res: "bs_td.ListGroupsOutputTypeDef",
    ) -> "dc_td.ListGroupsOutput":
        return dc_td.ListGroupsOutput.make_one(res)

    def list_tag_sync_tasks(
        self,
        res: "bs_td.ListTagSyncTasksOutputTypeDef",
    ) -> "dc_td.ListTagSyncTasksOutput":
        return dc_td.ListTagSyncTasksOutput.make_one(res)

    def search_resources(
        self,
        res: "bs_td.SearchResourcesOutputTypeDef",
    ) -> "dc_td.SearchResourcesOutput":
        return dc_td.SearchResourcesOutput.make_one(res)

    def start_tag_sync_task(
        self,
        res: "bs_td.StartTagSyncTaskOutputTypeDef",
    ) -> "dc_td.StartTagSyncTaskOutput":
        return dc_td.StartTagSyncTaskOutput.make_one(res)

    def tag(
        self,
        res: "bs_td.TagOutputTypeDef",
    ) -> "dc_td.TagOutput":
        return dc_td.TagOutput.make_one(res)

    def ungroup_resources(
        self,
        res: "bs_td.UngroupResourcesOutputTypeDef",
    ) -> "dc_td.UngroupResourcesOutput":
        return dc_td.UngroupResourcesOutput.make_one(res)

    def untag(
        self,
        res: "bs_td.UntagOutputTypeDef",
    ) -> "dc_td.UntagOutput":
        return dc_td.UntagOutput.make_one(res)

    def update_account_settings(
        self,
        res: "bs_td.UpdateAccountSettingsOutputTypeDef",
    ) -> "dc_td.UpdateAccountSettingsOutput":
        return dc_td.UpdateAccountSettingsOutput.make_one(res)

    def update_group(
        self,
        res: "bs_td.UpdateGroupOutputTypeDef",
    ) -> "dc_td.UpdateGroupOutput":
        return dc_td.UpdateGroupOutput.make_one(res)

    def update_group_query(
        self,
        res: "bs_td.UpdateGroupQueryOutputTypeDef",
    ) -> "dc_td.UpdateGroupQueryOutput":
        return dc_td.UpdateGroupQueryOutput.make_one(res)


resource_groups_caster = RESOURCE_GROUPSCaster()
