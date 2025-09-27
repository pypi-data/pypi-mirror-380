# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotsitewise import type_defs as bs_td


class IOTSITEWISECaster:

    def associate_assets(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def associate_time_series_to_asset_property(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def batch_associate_project_assets(
        self,
        res: "bs_td.BatchAssociateProjectAssetsResponseTypeDef",
    ) -> "dc_td.BatchAssociateProjectAssetsResponse":
        return dc_td.BatchAssociateProjectAssetsResponse.make_one(res)

    def batch_disassociate_project_assets(
        self,
        res: "bs_td.BatchDisassociateProjectAssetsResponseTypeDef",
    ) -> "dc_td.BatchDisassociateProjectAssetsResponse":
        return dc_td.BatchDisassociateProjectAssetsResponse.make_one(res)

    def batch_get_asset_property_aggregates(
        self,
        res: "bs_td.BatchGetAssetPropertyAggregatesResponseTypeDef",
    ) -> "dc_td.BatchGetAssetPropertyAggregatesResponse":
        return dc_td.BatchGetAssetPropertyAggregatesResponse.make_one(res)

    def batch_get_asset_property_value(
        self,
        res: "bs_td.BatchGetAssetPropertyValueResponseTypeDef",
    ) -> "dc_td.BatchGetAssetPropertyValueResponse":
        return dc_td.BatchGetAssetPropertyValueResponse.make_one(res)

    def batch_get_asset_property_value_history(
        self,
        res: "bs_td.BatchGetAssetPropertyValueHistoryResponseTypeDef",
    ) -> "dc_td.BatchGetAssetPropertyValueHistoryResponse":
        return dc_td.BatchGetAssetPropertyValueHistoryResponse.make_one(res)

    def batch_put_asset_property_value(
        self,
        res: "bs_td.BatchPutAssetPropertyValueResponseTypeDef",
    ) -> "dc_td.BatchPutAssetPropertyValueResponse":
        return dc_td.BatchPutAssetPropertyValueResponse.make_one(res)

    def create_access_policy(
        self,
        res: "bs_td.CreateAccessPolicyResponseTypeDef",
    ) -> "dc_td.CreateAccessPolicyResponse":
        return dc_td.CreateAccessPolicyResponse.make_one(res)

    def create_asset(
        self,
        res: "bs_td.CreateAssetResponseTypeDef",
    ) -> "dc_td.CreateAssetResponse":
        return dc_td.CreateAssetResponse.make_one(res)

    def create_asset_model(
        self,
        res: "bs_td.CreateAssetModelResponseTypeDef",
    ) -> "dc_td.CreateAssetModelResponse":
        return dc_td.CreateAssetModelResponse.make_one(res)

    def create_asset_model_composite_model(
        self,
        res: "bs_td.CreateAssetModelCompositeModelResponseTypeDef",
    ) -> "dc_td.CreateAssetModelCompositeModelResponse":
        return dc_td.CreateAssetModelCompositeModelResponse.make_one(res)

    def create_bulk_import_job(
        self,
        res: "bs_td.CreateBulkImportJobResponseTypeDef",
    ) -> "dc_td.CreateBulkImportJobResponse":
        return dc_td.CreateBulkImportJobResponse.make_one(res)

    def create_computation_model(
        self,
        res: "bs_td.CreateComputationModelResponseTypeDef",
    ) -> "dc_td.CreateComputationModelResponse":
        return dc_td.CreateComputationModelResponse.make_one(res)

    def create_dashboard(
        self,
        res: "bs_td.CreateDashboardResponseTypeDef",
    ) -> "dc_td.CreateDashboardResponse":
        return dc_td.CreateDashboardResponse.make_one(res)

    def create_dataset(
        self,
        res: "bs_td.CreateDatasetResponseTypeDef",
    ) -> "dc_td.CreateDatasetResponse":
        return dc_td.CreateDatasetResponse.make_one(res)

    def create_gateway(
        self,
        res: "bs_td.CreateGatewayResponseTypeDef",
    ) -> "dc_td.CreateGatewayResponse":
        return dc_td.CreateGatewayResponse.make_one(res)

    def create_portal(
        self,
        res: "bs_td.CreatePortalResponseTypeDef",
    ) -> "dc_td.CreatePortalResponse":
        return dc_td.CreatePortalResponse.make_one(res)

    def create_project(
        self,
        res: "bs_td.CreateProjectResponseTypeDef",
    ) -> "dc_td.CreateProjectResponse":
        return dc_td.CreateProjectResponse.make_one(res)

    def delete_asset(
        self,
        res: "bs_td.DeleteAssetResponseTypeDef",
    ) -> "dc_td.DeleteAssetResponse":
        return dc_td.DeleteAssetResponse.make_one(res)

    def delete_asset_model(
        self,
        res: "bs_td.DeleteAssetModelResponseTypeDef",
    ) -> "dc_td.DeleteAssetModelResponse":
        return dc_td.DeleteAssetModelResponse.make_one(res)

    def delete_asset_model_composite_model(
        self,
        res: "bs_td.DeleteAssetModelCompositeModelResponseTypeDef",
    ) -> "dc_td.DeleteAssetModelCompositeModelResponse":
        return dc_td.DeleteAssetModelCompositeModelResponse.make_one(res)

    def delete_asset_model_interface_relationship(
        self,
        res: "bs_td.DeleteAssetModelInterfaceRelationshipResponseTypeDef",
    ) -> "dc_td.DeleteAssetModelInterfaceRelationshipResponse":
        return dc_td.DeleteAssetModelInterfaceRelationshipResponse.make_one(res)

    def delete_computation_model(
        self,
        res: "bs_td.DeleteComputationModelResponseTypeDef",
    ) -> "dc_td.DeleteComputationModelResponse":
        return dc_td.DeleteComputationModelResponse.make_one(res)

    def delete_dataset(
        self,
        res: "bs_td.DeleteDatasetResponseTypeDef",
    ) -> "dc_td.DeleteDatasetResponse":
        return dc_td.DeleteDatasetResponse.make_one(res)

    def delete_gateway(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_portal(
        self,
        res: "bs_td.DeletePortalResponseTypeDef",
    ) -> "dc_td.DeletePortalResponse":
        return dc_td.DeletePortalResponse.make_one(res)

    def delete_time_series(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_access_policy(
        self,
        res: "bs_td.DescribeAccessPolicyResponseTypeDef",
    ) -> "dc_td.DescribeAccessPolicyResponse":
        return dc_td.DescribeAccessPolicyResponse.make_one(res)

    def describe_action(
        self,
        res: "bs_td.DescribeActionResponseTypeDef",
    ) -> "dc_td.DescribeActionResponse":
        return dc_td.DescribeActionResponse.make_one(res)

    def describe_asset(
        self,
        res: "bs_td.DescribeAssetResponseTypeDef",
    ) -> "dc_td.DescribeAssetResponse":
        return dc_td.DescribeAssetResponse.make_one(res)

    def describe_asset_composite_model(
        self,
        res: "bs_td.DescribeAssetCompositeModelResponseTypeDef",
    ) -> "dc_td.DescribeAssetCompositeModelResponse":
        return dc_td.DescribeAssetCompositeModelResponse.make_one(res)

    def describe_asset_model(
        self,
        res: "bs_td.DescribeAssetModelResponseTypeDef",
    ) -> "dc_td.DescribeAssetModelResponse":
        return dc_td.DescribeAssetModelResponse.make_one(res)

    def describe_asset_model_composite_model(
        self,
        res: "bs_td.DescribeAssetModelCompositeModelResponseTypeDef",
    ) -> "dc_td.DescribeAssetModelCompositeModelResponse":
        return dc_td.DescribeAssetModelCompositeModelResponse.make_one(res)

    def describe_asset_model_interface_relationship(
        self,
        res: "bs_td.DescribeAssetModelInterfaceRelationshipResponseTypeDef",
    ) -> "dc_td.DescribeAssetModelInterfaceRelationshipResponse":
        return dc_td.DescribeAssetModelInterfaceRelationshipResponse.make_one(res)

    def describe_asset_property(
        self,
        res: "bs_td.DescribeAssetPropertyResponseTypeDef",
    ) -> "dc_td.DescribeAssetPropertyResponse":
        return dc_td.DescribeAssetPropertyResponse.make_one(res)

    def describe_bulk_import_job(
        self,
        res: "bs_td.DescribeBulkImportJobResponseTypeDef",
    ) -> "dc_td.DescribeBulkImportJobResponse":
        return dc_td.DescribeBulkImportJobResponse.make_one(res)

    def describe_computation_model(
        self,
        res: "bs_td.DescribeComputationModelResponseTypeDef",
    ) -> "dc_td.DescribeComputationModelResponse":
        return dc_td.DescribeComputationModelResponse.make_one(res)

    def describe_computation_model_execution_summary(
        self,
        res: "bs_td.DescribeComputationModelExecutionSummaryResponseTypeDef",
    ) -> "dc_td.DescribeComputationModelExecutionSummaryResponse":
        return dc_td.DescribeComputationModelExecutionSummaryResponse.make_one(res)

    def describe_dashboard(
        self,
        res: "bs_td.DescribeDashboardResponseTypeDef",
    ) -> "dc_td.DescribeDashboardResponse":
        return dc_td.DescribeDashboardResponse.make_one(res)

    def describe_dataset(
        self,
        res: "bs_td.DescribeDatasetResponseTypeDef",
    ) -> "dc_td.DescribeDatasetResponse":
        return dc_td.DescribeDatasetResponse.make_one(res)

    def describe_default_encryption_configuration(
        self,
        res: "bs_td.DescribeDefaultEncryptionConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeDefaultEncryptionConfigurationResponse":
        return dc_td.DescribeDefaultEncryptionConfigurationResponse.make_one(res)

    def describe_execution(
        self,
        res: "bs_td.DescribeExecutionResponseTypeDef",
    ) -> "dc_td.DescribeExecutionResponse":
        return dc_td.DescribeExecutionResponse.make_one(res)

    def describe_gateway(
        self,
        res: "bs_td.DescribeGatewayResponseTypeDef",
    ) -> "dc_td.DescribeGatewayResponse":
        return dc_td.DescribeGatewayResponse.make_one(res)

    def describe_gateway_capability_configuration(
        self,
        res: "bs_td.DescribeGatewayCapabilityConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeGatewayCapabilityConfigurationResponse":
        return dc_td.DescribeGatewayCapabilityConfigurationResponse.make_one(res)

    def describe_logging_options(
        self,
        res: "bs_td.DescribeLoggingOptionsResponseTypeDef",
    ) -> "dc_td.DescribeLoggingOptionsResponse":
        return dc_td.DescribeLoggingOptionsResponse.make_one(res)

    def describe_portal(
        self,
        res: "bs_td.DescribePortalResponseTypeDef",
    ) -> "dc_td.DescribePortalResponse":
        return dc_td.DescribePortalResponse.make_one(res)

    def describe_project(
        self,
        res: "bs_td.DescribeProjectResponseTypeDef",
    ) -> "dc_td.DescribeProjectResponse":
        return dc_td.DescribeProjectResponse.make_one(res)

    def describe_storage_configuration(
        self,
        res: "bs_td.DescribeStorageConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeStorageConfigurationResponse":
        return dc_td.DescribeStorageConfigurationResponse.make_one(res)

    def describe_time_series(
        self,
        res: "bs_td.DescribeTimeSeriesResponseTypeDef",
    ) -> "dc_td.DescribeTimeSeriesResponse":
        return dc_td.DescribeTimeSeriesResponse.make_one(res)

    def disassociate_assets(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_time_series_from_asset_property(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def execute_action(
        self,
        res: "bs_td.ExecuteActionResponseTypeDef",
    ) -> "dc_td.ExecuteActionResponse":
        return dc_td.ExecuteActionResponse.make_one(res)

    def execute_query(
        self,
        res: "bs_td.ExecuteQueryResponseTypeDef",
    ) -> "dc_td.ExecuteQueryResponse":
        return dc_td.ExecuteQueryResponse.make_one(res)

    def get_asset_property_aggregates(
        self,
        res: "bs_td.GetAssetPropertyAggregatesResponseTypeDef",
    ) -> "dc_td.GetAssetPropertyAggregatesResponse":
        return dc_td.GetAssetPropertyAggregatesResponse.make_one(res)

    def get_asset_property_value(
        self,
        res: "bs_td.GetAssetPropertyValueResponseTypeDef",
    ) -> "dc_td.GetAssetPropertyValueResponse":
        return dc_td.GetAssetPropertyValueResponse.make_one(res)

    def get_asset_property_value_history(
        self,
        res: "bs_td.GetAssetPropertyValueHistoryResponseTypeDef",
    ) -> "dc_td.GetAssetPropertyValueHistoryResponse":
        return dc_td.GetAssetPropertyValueHistoryResponse.make_one(res)

    def get_interpolated_asset_property_values(
        self,
        res: "bs_td.GetInterpolatedAssetPropertyValuesResponseTypeDef",
    ) -> "dc_td.GetInterpolatedAssetPropertyValuesResponse":
        return dc_td.GetInterpolatedAssetPropertyValuesResponse.make_one(res)

    def invoke_assistant(
        self,
        res: "bs_td.InvokeAssistantResponseTypeDef",
    ) -> "dc_td.InvokeAssistantResponse":
        return dc_td.InvokeAssistantResponse.make_one(res)

    def list_access_policies(
        self,
        res: "bs_td.ListAccessPoliciesResponseTypeDef",
    ) -> "dc_td.ListAccessPoliciesResponse":
        return dc_td.ListAccessPoliciesResponse.make_one(res)

    def list_actions(
        self,
        res: "bs_td.ListActionsResponseTypeDef",
    ) -> "dc_td.ListActionsResponse":
        return dc_td.ListActionsResponse.make_one(res)

    def list_asset_model_composite_models(
        self,
        res: "bs_td.ListAssetModelCompositeModelsResponseTypeDef",
    ) -> "dc_td.ListAssetModelCompositeModelsResponse":
        return dc_td.ListAssetModelCompositeModelsResponse.make_one(res)

    def list_asset_model_properties(
        self,
        res: "bs_td.ListAssetModelPropertiesResponseTypeDef",
    ) -> "dc_td.ListAssetModelPropertiesResponse":
        return dc_td.ListAssetModelPropertiesResponse.make_one(res)

    def list_asset_models(
        self,
        res: "bs_td.ListAssetModelsResponseTypeDef",
    ) -> "dc_td.ListAssetModelsResponse":
        return dc_td.ListAssetModelsResponse.make_one(res)

    def list_asset_properties(
        self,
        res: "bs_td.ListAssetPropertiesResponseTypeDef",
    ) -> "dc_td.ListAssetPropertiesResponse":
        return dc_td.ListAssetPropertiesResponse.make_one(res)

    def list_asset_relationships(
        self,
        res: "bs_td.ListAssetRelationshipsResponseTypeDef",
    ) -> "dc_td.ListAssetRelationshipsResponse":
        return dc_td.ListAssetRelationshipsResponse.make_one(res)

    def list_assets(
        self,
        res: "bs_td.ListAssetsResponseTypeDef",
    ) -> "dc_td.ListAssetsResponse":
        return dc_td.ListAssetsResponse.make_one(res)

    def list_associated_assets(
        self,
        res: "bs_td.ListAssociatedAssetsResponseTypeDef",
    ) -> "dc_td.ListAssociatedAssetsResponse":
        return dc_td.ListAssociatedAssetsResponse.make_one(res)

    def list_bulk_import_jobs(
        self,
        res: "bs_td.ListBulkImportJobsResponseTypeDef",
    ) -> "dc_td.ListBulkImportJobsResponse":
        return dc_td.ListBulkImportJobsResponse.make_one(res)

    def list_composition_relationships(
        self,
        res: "bs_td.ListCompositionRelationshipsResponseTypeDef",
    ) -> "dc_td.ListCompositionRelationshipsResponse":
        return dc_td.ListCompositionRelationshipsResponse.make_one(res)

    def list_computation_model_data_binding_usages(
        self,
        res: "bs_td.ListComputationModelDataBindingUsagesResponseTypeDef",
    ) -> "dc_td.ListComputationModelDataBindingUsagesResponse":
        return dc_td.ListComputationModelDataBindingUsagesResponse.make_one(res)

    def list_computation_model_resolve_to_resources(
        self,
        res: "bs_td.ListComputationModelResolveToResourcesResponseTypeDef",
    ) -> "dc_td.ListComputationModelResolveToResourcesResponse":
        return dc_td.ListComputationModelResolveToResourcesResponse.make_one(res)

    def list_computation_models(
        self,
        res: "bs_td.ListComputationModelsResponseTypeDef",
    ) -> "dc_td.ListComputationModelsResponse":
        return dc_td.ListComputationModelsResponse.make_one(res)

    def list_dashboards(
        self,
        res: "bs_td.ListDashboardsResponseTypeDef",
    ) -> "dc_td.ListDashboardsResponse":
        return dc_td.ListDashboardsResponse.make_one(res)

    def list_datasets(
        self,
        res: "bs_td.ListDatasetsResponseTypeDef",
    ) -> "dc_td.ListDatasetsResponse":
        return dc_td.ListDatasetsResponse.make_one(res)

    def list_executions(
        self,
        res: "bs_td.ListExecutionsResponseTypeDef",
    ) -> "dc_td.ListExecutionsResponse":
        return dc_td.ListExecutionsResponse.make_one(res)

    def list_gateways(
        self,
        res: "bs_td.ListGatewaysResponseTypeDef",
    ) -> "dc_td.ListGatewaysResponse":
        return dc_td.ListGatewaysResponse.make_one(res)

    def list_interface_relationships(
        self,
        res: "bs_td.ListInterfaceRelationshipsResponseTypeDef",
    ) -> "dc_td.ListInterfaceRelationshipsResponse":
        return dc_td.ListInterfaceRelationshipsResponse.make_one(res)

    def list_portals(
        self,
        res: "bs_td.ListPortalsResponseTypeDef",
    ) -> "dc_td.ListPortalsResponse":
        return dc_td.ListPortalsResponse.make_one(res)

    def list_project_assets(
        self,
        res: "bs_td.ListProjectAssetsResponseTypeDef",
    ) -> "dc_td.ListProjectAssetsResponse":
        return dc_td.ListProjectAssetsResponse.make_one(res)

    def list_projects(
        self,
        res: "bs_td.ListProjectsResponseTypeDef",
    ) -> "dc_td.ListProjectsResponse":
        return dc_td.ListProjectsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_time_series(
        self,
        res: "bs_td.ListTimeSeriesResponseTypeDef",
    ) -> "dc_td.ListTimeSeriesResponse":
        return dc_td.ListTimeSeriesResponse.make_one(res)

    def put_asset_model_interface_relationship(
        self,
        res: "bs_td.PutAssetModelInterfaceRelationshipResponseTypeDef",
    ) -> "dc_td.PutAssetModelInterfaceRelationshipResponse":
        return dc_td.PutAssetModelInterfaceRelationshipResponse.make_one(res)

    def put_default_encryption_configuration(
        self,
        res: "bs_td.PutDefaultEncryptionConfigurationResponseTypeDef",
    ) -> "dc_td.PutDefaultEncryptionConfigurationResponse":
        return dc_td.PutDefaultEncryptionConfigurationResponse.make_one(res)

    def put_storage_configuration(
        self,
        res: "bs_td.PutStorageConfigurationResponseTypeDef",
    ) -> "dc_td.PutStorageConfigurationResponse":
        return dc_td.PutStorageConfigurationResponse.make_one(res)

    def update_asset(
        self,
        res: "bs_td.UpdateAssetResponseTypeDef",
    ) -> "dc_td.UpdateAssetResponse":
        return dc_td.UpdateAssetResponse.make_one(res)

    def update_asset_model(
        self,
        res: "bs_td.UpdateAssetModelResponseTypeDef",
    ) -> "dc_td.UpdateAssetModelResponse":
        return dc_td.UpdateAssetModelResponse.make_one(res)

    def update_asset_model_composite_model(
        self,
        res: "bs_td.UpdateAssetModelCompositeModelResponseTypeDef",
    ) -> "dc_td.UpdateAssetModelCompositeModelResponse":
        return dc_td.UpdateAssetModelCompositeModelResponse.make_one(res)

    def update_asset_property(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_computation_model(
        self,
        res: "bs_td.UpdateComputationModelResponseTypeDef",
    ) -> "dc_td.UpdateComputationModelResponse":
        return dc_td.UpdateComputationModelResponse.make_one(res)

    def update_dataset(
        self,
        res: "bs_td.UpdateDatasetResponseTypeDef",
    ) -> "dc_td.UpdateDatasetResponse":
        return dc_td.UpdateDatasetResponse.make_one(res)

    def update_gateway(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_gateway_capability_configuration(
        self,
        res: "bs_td.UpdateGatewayCapabilityConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateGatewayCapabilityConfigurationResponse":
        return dc_td.UpdateGatewayCapabilityConfigurationResponse.make_one(res)

    def update_portal(
        self,
        res: "bs_td.UpdatePortalResponseTypeDef",
    ) -> "dc_td.UpdatePortalResponse":
        return dc_td.UpdatePortalResponse.make_one(res)


iotsitewise_caster = IOTSITEWISECaster()
