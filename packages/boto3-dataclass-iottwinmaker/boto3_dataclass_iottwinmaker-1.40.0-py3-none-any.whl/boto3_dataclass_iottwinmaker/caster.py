# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iottwinmaker import type_defs as bs_td


class IOTTWINMAKERCaster:

    def batch_put_property_values(
        self,
        res: "bs_td.BatchPutPropertyValuesResponseTypeDef",
    ) -> "dc_td.BatchPutPropertyValuesResponse":
        return dc_td.BatchPutPropertyValuesResponse.make_one(res)

    def cancel_metadata_transfer_job(
        self,
        res: "bs_td.CancelMetadataTransferJobResponseTypeDef",
    ) -> "dc_td.CancelMetadataTransferJobResponse":
        return dc_td.CancelMetadataTransferJobResponse.make_one(res)

    def create_component_type(
        self,
        res: "bs_td.CreateComponentTypeResponseTypeDef",
    ) -> "dc_td.CreateComponentTypeResponse":
        return dc_td.CreateComponentTypeResponse.make_one(res)

    def create_entity(
        self,
        res: "bs_td.CreateEntityResponseTypeDef",
    ) -> "dc_td.CreateEntityResponse":
        return dc_td.CreateEntityResponse.make_one(res)

    def create_metadata_transfer_job(
        self,
        res: "bs_td.CreateMetadataTransferJobResponseTypeDef",
    ) -> "dc_td.CreateMetadataTransferJobResponse":
        return dc_td.CreateMetadataTransferJobResponse.make_one(res)

    def create_scene(
        self,
        res: "bs_td.CreateSceneResponseTypeDef",
    ) -> "dc_td.CreateSceneResponse":
        return dc_td.CreateSceneResponse.make_one(res)

    def create_sync_job(
        self,
        res: "bs_td.CreateSyncJobResponseTypeDef",
    ) -> "dc_td.CreateSyncJobResponse":
        return dc_td.CreateSyncJobResponse.make_one(res)

    def create_workspace(
        self,
        res: "bs_td.CreateWorkspaceResponseTypeDef",
    ) -> "dc_td.CreateWorkspaceResponse":
        return dc_td.CreateWorkspaceResponse.make_one(res)

    def delete_component_type(
        self,
        res: "bs_td.DeleteComponentTypeResponseTypeDef",
    ) -> "dc_td.DeleteComponentTypeResponse":
        return dc_td.DeleteComponentTypeResponse.make_one(res)

    def delete_entity(
        self,
        res: "bs_td.DeleteEntityResponseTypeDef",
    ) -> "dc_td.DeleteEntityResponse":
        return dc_td.DeleteEntityResponse.make_one(res)

    def delete_sync_job(
        self,
        res: "bs_td.DeleteSyncJobResponseTypeDef",
    ) -> "dc_td.DeleteSyncJobResponse":
        return dc_td.DeleteSyncJobResponse.make_one(res)

    def delete_workspace(
        self,
        res: "bs_td.DeleteWorkspaceResponseTypeDef",
    ) -> "dc_td.DeleteWorkspaceResponse":
        return dc_td.DeleteWorkspaceResponse.make_one(res)

    def execute_query(
        self,
        res: "bs_td.ExecuteQueryResponseTypeDef",
    ) -> "dc_td.ExecuteQueryResponse":
        return dc_td.ExecuteQueryResponse.make_one(res)

    def get_component_type(
        self,
        res: "bs_td.GetComponentTypeResponseTypeDef",
    ) -> "dc_td.GetComponentTypeResponse":
        return dc_td.GetComponentTypeResponse.make_one(res)

    def get_entity(
        self,
        res: "bs_td.GetEntityResponseTypeDef",
    ) -> "dc_td.GetEntityResponse":
        return dc_td.GetEntityResponse.make_one(res)

    def get_metadata_transfer_job(
        self,
        res: "bs_td.GetMetadataTransferJobResponseTypeDef",
    ) -> "dc_td.GetMetadataTransferJobResponse":
        return dc_td.GetMetadataTransferJobResponse.make_one(res)

    def get_pricing_plan(
        self,
        res: "bs_td.GetPricingPlanResponseTypeDef",
    ) -> "dc_td.GetPricingPlanResponse":
        return dc_td.GetPricingPlanResponse.make_one(res)

    def get_property_value(
        self,
        res: "bs_td.GetPropertyValueResponseTypeDef",
    ) -> "dc_td.GetPropertyValueResponse":
        return dc_td.GetPropertyValueResponse.make_one(res)

    def get_property_value_history(
        self,
        res: "bs_td.GetPropertyValueHistoryResponseTypeDef",
    ) -> "dc_td.GetPropertyValueHistoryResponse":
        return dc_td.GetPropertyValueHistoryResponse.make_one(res)

    def get_scene(
        self,
        res: "bs_td.GetSceneResponseTypeDef",
    ) -> "dc_td.GetSceneResponse":
        return dc_td.GetSceneResponse.make_one(res)

    def get_sync_job(
        self,
        res: "bs_td.GetSyncJobResponseTypeDef",
    ) -> "dc_td.GetSyncJobResponse":
        return dc_td.GetSyncJobResponse.make_one(res)

    def get_workspace(
        self,
        res: "bs_td.GetWorkspaceResponseTypeDef",
    ) -> "dc_td.GetWorkspaceResponse":
        return dc_td.GetWorkspaceResponse.make_one(res)

    def list_component_types(
        self,
        res: "bs_td.ListComponentTypesResponseTypeDef",
    ) -> "dc_td.ListComponentTypesResponse":
        return dc_td.ListComponentTypesResponse.make_one(res)

    def list_components(
        self,
        res: "bs_td.ListComponentsResponseTypeDef",
    ) -> "dc_td.ListComponentsResponse":
        return dc_td.ListComponentsResponse.make_one(res)

    def list_entities(
        self,
        res: "bs_td.ListEntitiesResponseTypeDef",
    ) -> "dc_td.ListEntitiesResponse":
        return dc_td.ListEntitiesResponse.make_one(res)

    def list_metadata_transfer_jobs(
        self,
        res: "bs_td.ListMetadataTransferJobsResponseTypeDef",
    ) -> "dc_td.ListMetadataTransferJobsResponse":
        return dc_td.ListMetadataTransferJobsResponse.make_one(res)

    def list_properties(
        self,
        res: "bs_td.ListPropertiesResponseTypeDef",
    ) -> "dc_td.ListPropertiesResponse":
        return dc_td.ListPropertiesResponse.make_one(res)

    def list_scenes(
        self,
        res: "bs_td.ListScenesResponseTypeDef",
    ) -> "dc_td.ListScenesResponse":
        return dc_td.ListScenesResponse.make_one(res)

    def list_sync_jobs(
        self,
        res: "bs_td.ListSyncJobsResponseTypeDef",
    ) -> "dc_td.ListSyncJobsResponse":
        return dc_td.ListSyncJobsResponse.make_one(res)

    def list_sync_resources(
        self,
        res: "bs_td.ListSyncResourcesResponseTypeDef",
    ) -> "dc_td.ListSyncResourcesResponse":
        return dc_td.ListSyncResourcesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_workspaces(
        self,
        res: "bs_td.ListWorkspacesResponseTypeDef",
    ) -> "dc_td.ListWorkspacesResponse":
        return dc_td.ListWorkspacesResponse.make_one(res)

    def update_component_type(
        self,
        res: "bs_td.UpdateComponentTypeResponseTypeDef",
    ) -> "dc_td.UpdateComponentTypeResponse":
        return dc_td.UpdateComponentTypeResponse.make_one(res)

    def update_entity(
        self,
        res: "bs_td.UpdateEntityResponseTypeDef",
    ) -> "dc_td.UpdateEntityResponse":
        return dc_td.UpdateEntityResponse.make_one(res)

    def update_pricing_plan(
        self,
        res: "bs_td.UpdatePricingPlanResponseTypeDef",
    ) -> "dc_td.UpdatePricingPlanResponse":
        return dc_td.UpdatePricingPlanResponse.make_one(res)

    def update_scene(
        self,
        res: "bs_td.UpdateSceneResponseTypeDef",
    ) -> "dc_td.UpdateSceneResponse":
        return dc_td.UpdateSceneResponse.make_one(res)

    def update_workspace(
        self,
        res: "bs_td.UpdateWorkspaceResponseTypeDef",
    ) -> "dc_td.UpdateWorkspaceResponse":
        return dc_td.UpdateWorkspaceResponse.make_one(res)


iottwinmaker_caster = IOTTWINMAKERCaster()
