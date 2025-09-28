# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_resource_explorer_2 import type_defs as bs_td


class RESOURCE_EXPLORER_2Caster:

    def associate_default_view(
        self,
        res: "bs_td.AssociateDefaultViewOutputTypeDef",
    ) -> "dc_td.AssociateDefaultViewOutput":
        return dc_td.AssociateDefaultViewOutput.make_one(res)

    def batch_get_view(
        self,
        res: "bs_td.BatchGetViewOutputTypeDef",
    ) -> "dc_td.BatchGetViewOutput":
        return dc_td.BatchGetViewOutput.make_one(res)

    def create_index(
        self,
        res: "bs_td.CreateIndexOutputTypeDef",
    ) -> "dc_td.CreateIndexOutput":
        return dc_td.CreateIndexOutput.make_one(res)

    def create_view(
        self,
        res: "bs_td.CreateViewOutputTypeDef",
    ) -> "dc_td.CreateViewOutput":
        return dc_td.CreateViewOutput.make_one(res)

    def delete_index(
        self,
        res: "bs_td.DeleteIndexOutputTypeDef",
    ) -> "dc_td.DeleteIndexOutput":
        return dc_td.DeleteIndexOutput.make_one(res)

    def delete_view(
        self,
        res: "bs_td.DeleteViewOutputTypeDef",
    ) -> "dc_td.DeleteViewOutput":
        return dc_td.DeleteViewOutput.make_one(res)

    def disassociate_default_view(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_account_level_service_configuration(
        self,
        res: "bs_td.GetAccountLevelServiceConfigurationOutputTypeDef",
    ) -> "dc_td.GetAccountLevelServiceConfigurationOutput":
        return dc_td.GetAccountLevelServiceConfigurationOutput.make_one(res)

    def get_default_view(
        self,
        res: "bs_td.GetDefaultViewOutputTypeDef",
    ) -> "dc_td.GetDefaultViewOutput":
        return dc_td.GetDefaultViewOutput.make_one(res)

    def get_index(
        self,
        res: "bs_td.GetIndexOutputTypeDef",
    ) -> "dc_td.GetIndexOutput":
        return dc_td.GetIndexOutput.make_one(res)

    def get_managed_view(
        self,
        res: "bs_td.GetManagedViewOutputTypeDef",
    ) -> "dc_td.GetManagedViewOutput":
        return dc_td.GetManagedViewOutput.make_one(res)

    def get_view(
        self,
        res: "bs_td.GetViewOutputTypeDef",
    ) -> "dc_td.GetViewOutput":
        return dc_td.GetViewOutput.make_one(res)

    def list_indexes(
        self,
        res: "bs_td.ListIndexesOutputTypeDef",
    ) -> "dc_td.ListIndexesOutput":
        return dc_td.ListIndexesOutput.make_one(res)

    def list_indexes_for_members(
        self,
        res: "bs_td.ListIndexesForMembersOutputTypeDef",
    ) -> "dc_td.ListIndexesForMembersOutput":
        return dc_td.ListIndexesForMembersOutput.make_one(res)

    def list_managed_views(
        self,
        res: "bs_td.ListManagedViewsOutputTypeDef",
    ) -> "dc_td.ListManagedViewsOutput":
        return dc_td.ListManagedViewsOutput.make_one(res)

    def list_resources(
        self,
        res: "bs_td.ListResourcesOutputTypeDef",
    ) -> "dc_td.ListResourcesOutput":
        return dc_td.ListResourcesOutput.make_one(res)

    def list_supported_resource_types(
        self,
        res: "bs_td.ListSupportedResourceTypesOutputTypeDef",
    ) -> "dc_td.ListSupportedResourceTypesOutput":
        return dc_td.ListSupportedResourceTypesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def list_views(
        self,
        res: "bs_td.ListViewsOutputTypeDef",
    ) -> "dc_td.ListViewsOutput":
        return dc_td.ListViewsOutput.make_one(res)

    def search(
        self,
        res: "bs_td.SearchOutputTypeDef",
    ) -> "dc_td.SearchOutput":
        return dc_td.SearchOutput.make_one(res)

    def update_index_type(
        self,
        res: "bs_td.UpdateIndexTypeOutputTypeDef",
    ) -> "dc_td.UpdateIndexTypeOutput":
        return dc_td.UpdateIndexTypeOutput.make_one(res)

    def update_view(
        self,
        res: "bs_td.UpdateViewOutputTypeDef",
    ) -> "dc_td.UpdateViewOutput":
        return dc_td.UpdateViewOutput.make_one(res)


resource_explorer_2_caster = RESOURCE_EXPLORER_2Caster()
