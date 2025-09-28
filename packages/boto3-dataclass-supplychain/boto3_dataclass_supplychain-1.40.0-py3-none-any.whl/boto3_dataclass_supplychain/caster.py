# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_supplychain import type_defs as bs_td


class SUPPLYCHAINCaster:

    def create_bill_of_materials_import_job(
        self,
        res: "bs_td.CreateBillOfMaterialsImportJobResponseTypeDef",
    ) -> "dc_td.CreateBillOfMaterialsImportJobResponse":
        return dc_td.CreateBillOfMaterialsImportJobResponse.make_one(res)

    def create_data_integration_flow(
        self,
        res: "bs_td.CreateDataIntegrationFlowResponseTypeDef",
    ) -> "dc_td.CreateDataIntegrationFlowResponse":
        return dc_td.CreateDataIntegrationFlowResponse.make_one(res)

    def create_data_lake_dataset(
        self,
        res: "bs_td.CreateDataLakeDatasetResponseTypeDef",
    ) -> "dc_td.CreateDataLakeDatasetResponse":
        return dc_td.CreateDataLakeDatasetResponse.make_one(res)

    def create_data_lake_namespace(
        self,
        res: "bs_td.CreateDataLakeNamespaceResponseTypeDef",
    ) -> "dc_td.CreateDataLakeNamespaceResponse":
        return dc_td.CreateDataLakeNamespaceResponse.make_one(res)

    def create_instance(
        self,
        res: "bs_td.CreateInstanceResponseTypeDef",
    ) -> "dc_td.CreateInstanceResponse":
        return dc_td.CreateInstanceResponse.make_one(res)

    def delete_data_integration_flow(
        self,
        res: "bs_td.DeleteDataIntegrationFlowResponseTypeDef",
    ) -> "dc_td.DeleteDataIntegrationFlowResponse":
        return dc_td.DeleteDataIntegrationFlowResponse.make_one(res)

    def delete_data_lake_dataset(
        self,
        res: "bs_td.DeleteDataLakeDatasetResponseTypeDef",
    ) -> "dc_td.DeleteDataLakeDatasetResponse":
        return dc_td.DeleteDataLakeDatasetResponse.make_one(res)

    def delete_data_lake_namespace(
        self,
        res: "bs_td.DeleteDataLakeNamespaceResponseTypeDef",
    ) -> "dc_td.DeleteDataLakeNamespaceResponse":
        return dc_td.DeleteDataLakeNamespaceResponse.make_one(res)

    def delete_instance(
        self,
        res: "bs_td.DeleteInstanceResponseTypeDef",
    ) -> "dc_td.DeleteInstanceResponse":
        return dc_td.DeleteInstanceResponse.make_one(res)

    def get_bill_of_materials_import_job(
        self,
        res: "bs_td.GetBillOfMaterialsImportJobResponseTypeDef",
    ) -> "dc_td.GetBillOfMaterialsImportJobResponse":
        return dc_td.GetBillOfMaterialsImportJobResponse.make_one(res)

    def get_data_integration_event(
        self,
        res: "bs_td.GetDataIntegrationEventResponseTypeDef",
    ) -> "dc_td.GetDataIntegrationEventResponse":
        return dc_td.GetDataIntegrationEventResponse.make_one(res)

    def get_data_integration_flow(
        self,
        res: "bs_td.GetDataIntegrationFlowResponseTypeDef",
    ) -> "dc_td.GetDataIntegrationFlowResponse":
        return dc_td.GetDataIntegrationFlowResponse.make_one(res)

    def get_data_integration_flow_execution(
        self,
        res: "bs_td.GetDataIntegrationFlowExecutionResponseTypeDef",
    ) -> "dc_td.GetDataIntegrationFlowExecutionResponse":
        return dc_td.GetDataIntegrationFlowExecutionResponse.make_one(res)

    def get_data_lake_dataset(
        self,
        res: "bs_td.GetDataLakeDatasetResponseTypeDef",
    ) -> "dc_td.GetDataLakeDatasetResponse":
        return dc_td.GetDataLakeDatasetResponse.make_one(res)

    def get_data_lake_namespace(
        self,
        res: "bs_td.GetDataLakeNamespaceResponseTypeDef",
    ) -> "dc_td.GetDataLakeNamespaceResponse":
        return dc_td.GetDataLakeNamespaceResponse.make_one(res)

    def get_instance(
        self,
        res: "bs_td.GetInstanceResponseTypeDef",
    ) -> "dc_td.GetInstanceResponse":
        return dc_td.GetInstanceResponse.make_one(res)

    def list_data_integration_events(
        self,
        res: "bs_td.ListDataIntegrationEventsResponseTypeDef",
    ) -> "dc_td.ListDataIntegrationEventsResponse":
        return dc_td.ListDataIntegrationEventsResponse.make_one(res)

    def list_data_integration_flow_executions(
        self,
        res: "bs_td.ListDataIntegrationFlowExecutionsResponseTypeDef",
    ) -> "dc_td.ListDataIntegrationFlowExecutionsResponse":
        return dc_td.ListDataIntegrationFlowExecutionsResponse.make_one(res)

    def list_data_integration_flows(
        self,
        res: "bs_td.ListDataIntegrationFlowsResponseTypeDef",
    ) -> "dc_td.ListDataIntegrationFlowsResponse":
        return dc_td.ListDataIntegrationFlowsResponse.make_one(res)

    def list_data_lake_datasets(
        self,
        res: "bs_td.ListDataLakeDatasetsResponseTypeDef",
    ) -> "dc_td.ListDataLakeDatasetsResponse":
        return dc_td.ListDataLakeDatasetsResponse.make_one(res)

    def list_data_lake_namespaces(
        self,
        res: "bs_td.ListDataLakeNamespacesResponseTypeDef",
    ) -> "dc_td.ListDataLakeNamespacesResponse":
        return dc_td.ListDataLakeNamespacesResponse.make_one(res)

    def list_instances(
        self,
        res: "bs_td.ListInstancesResponseTypeDef",
    ) -> "dc_td.ListInstancesResponse":
        return dc_td.ListInstancesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def send_data_integration_event(
        self,
        res: "bs_td.SendDataIntegrationEventResponseTypeDef",
    ) -> "dc_td.SendDataIntegrationEventResponse":
        return dc_td.SendDataIntegrationEventResponse.make_one(res)

    def update_data_integration_flow(
        self,
        res: "bs_td.UpdateDataIntegrationFlowResponseTypeDef",
    ) -> "dc_td.UpdateDataIntegrationFlowResponse":
        return dc_td.UpdateDataIntegrationFlowResponse.make_one(res)

    def update_data_lake_dataset(
        self,
        res: "bs_td.UpdateDataLakeDatasetResponseTypeDef",
    ) -> "dc_td.UpdateDataLakeDatasetResponse":
        return dc_td.UpdateDataLakeDatasetResponse.make_one(res)

    def update_data_lake_namespace(
        self,
        res: "bs_td.UpdateDataLakeNamespaceResponseTypeDef",
    ) -> "dc_td.UpdateDataLakeNamespaceResponse":
        return dc_td.UpdateDataLakeNamespaceResponse.make_one(res)

    def update_instance(
        self,
        res: "bs_td.UpdateInstanceResponseTypeDef",
    ) -> "dc_td.UpdateInstanceResponse":
        return dc_td.UpdateInstanceResponse.make_one(res)


supplychain_caster = SUPPLYCHAINCaster()
