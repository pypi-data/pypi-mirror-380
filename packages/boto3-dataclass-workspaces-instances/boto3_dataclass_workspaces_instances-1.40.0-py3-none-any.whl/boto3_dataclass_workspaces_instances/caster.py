# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workspaces_instances import type_defs as bs_td


class WORKSPACES_INSTANCESCaster:

    def create_volume(
        self,
        res: "bs_td.CreateVolumeResponseTypeDef",
    ) -> "dc_td.CreateVolumeResponse":
        return dc_td.CreateVolumeResponse.make_one(res)

    def create_workspace_instance(
        self,
        res: "bs_td.CreateWorkspaceInstanceResponseTypeDef",
    ) -> "dc_td.CreateWorkspaceInstanceResponse":
        return dc_td.CreateWorkspaceInstanceResponse.make_one(res)

    def get_workspace_instance(
        self,
        res: "bs_td.GetWorkspaceInstanceResponseTypeDef",
    ) -> "dc_td.GetWorkspaceInstanceResponse":
        return dc_td.GetWorkspaceInstanceResponse.make_one(res)

    def list_instance_types(
        self,
        res: "bs_td.ListInstanceTypesResponseTypeDef",
    ) -> "dc_td.ListInstanceTypesResponse":
        return dc_td.ListInstanceTypesResponse.make_one(res)

    def list_regions(
        self,
        res: "bs_td.ListRegionsResponseTypeDef",
    ) -> "dc_td.ListRegionsResponse":
        return dc_td.ListRegionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_workspace_instances(
        self,
        res: "bs_td.ListWorkspaceInstancesResponseTypeDef",
    ) -> "dc_td.ListWorkspaceInstancesResponse":
        return dc_td.ListWorkspaceInstancesResponse.make_one(res)


workspaces_instances_caster = WORKSPACES_INSTANCESCaster()
