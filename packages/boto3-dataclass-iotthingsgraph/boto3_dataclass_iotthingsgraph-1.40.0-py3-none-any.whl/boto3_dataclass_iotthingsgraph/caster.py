# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotthingsgraph import type_defs as bs_td


class IOTTHINGSGRAPHCaster:

    def create_flow_template(
        self,
        res: "bs_td.CreateFlowTemplateResponseTypeDef",
    ) -> "dc_td.CreateFlowTemplateResponse":
        return dc_td.CreateFlowTemplateResponse.make_one(res)

    def create_system_instance(
        self,
        res: "bs_td.CreateSystemInstanceResponseTypeDef",
    ) -> "dc_td.CreateSystemInstanceResponse":
        return dc_td.CreateSystemInstanceResponse.make_one(res)

    def create_system_template(
        self,
        res: "bs_td.CreateSystemTemplateResponseTypeDef",
    ) -> "dc_td.CreateSystemTemplateResponse":
        return dc_td.CreateSystemTemplateResponse.make_one(res)

    def delete_namespace(
        self,
        res: "bs_td.DeleteNamespaceResponseTypeDef",
    ) -> "dc_td.DeleteNamespaceResponse":
        return dc_td.DeleteNamespaceResponse.make_one(res)

    def deploy_system_instance(
        self,
        res: "bs_td.DeploySystemInstanceResponseTypeDef",
    ) -> "dc_td.DeploySystemInstanceResponse":
        return dc_td.DeploySystemInstanceResponse.make_one(res)

    def describe_namespace(
        self,
        res: "bs_td.DescribeNamespaceResponseTypeDef",
    ) -> "dc_td.DescribeNamespaceResponse":
        return dc_td.DescribeNamespaceResponse.make_one(res)

    def get_entities(
        self,
        res: "bs_td.GetEntitiesResponseTypeDef",
    ) -> "dc_td.GetEntitiesResponse":
        return dc_td.GetEntitiesResponse.make_one(res)

    def get_flow_template(
        self,
        res: "bs_td.GetFlowTemplateResponseTypeDef",
    ) -> "dc_td.GetFlowTemplateResponse":
        return dc_td.GetFlowTemplateResponse.make_one(res)

    def get_flow_template_revisions(
        self,
        res: "bs_td.GetFlowTemplateRevisionsResponseTypeDef",
    ) -> "dc_td.GetFlowTemplateRevisionsResponse":
        return dc_td.GetFlowTemplateRevisionsResponse.make_one(res)

    def get_namespace_deletion_status(
        self,
        res: "bs_td.GetNamespaceDeletionStatusResponseTypeDef",
    ) -> "dc_td.GetNamespaceDeletionStatusResponse":
        return dc_td.GetNamespaceDeletionStatusResponse.make_one(res)

    def get_system_instance(
        self,
        res: "bs_td.GetSystemInstanceResponseTypeDef",
    ) -> "dc_td.GetSystemInstanceResponse":
        return dc_td.GetSystemInstanceResponse.make_one(res)

    def get_system_template(
        self,
        res: "bs_td.GetSystemTemplateResponseTypeDef",
    ) -> "dc_td.GetSystemTemplateResponse":
        return dc_td.GetSystemTemplateResponse.make_one(res)

    def get_system_template_revisions(
        self,
        res: "bs_td.GetSystemTemplateRevisionsResponseTypeDef",
    ) -> "dc_td.GetSystemTemplateRevisionsResponse":
        return dc_td.GetSystemTemplateRevisionsResponse.make_one(res)

    def get_upload_status(
        self,
        res: "bs_td.GetUploadStatusResponseTypeDef",
    ) -> "dc_td.GetUploadStatusResponse":
        return dc_td.GetUploadStatusResponse.make_one(res)

    def list_flow_execution_messages(
        self,
        res: "bs_td.ListFlowExecutionMessagesResponseTypeDef",
    ) -> "dc_td.ListFlowExecutionMessagesResponse":
        return dc_td.ListFlowExecutionMessagesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def search_entities(
        self,
        res: "bs_td.SearchEntitiesResponseTypeDef",
    ) -> "dc_td.SearchEntitiesResponse":
        return dc_td.SearchEntitiesResponse.make_one(res)

    def search_flow_executions(
        self,
        res: "bs_td.SearchFlowExecutionsResponseTypeDef",
    ) -> "dc_td.SearchFlowExecutionsResponse":
        return dc_td.SearchFlowExecutionsResponse.make_one(res)

    def search_flow_templates(
        self,
        res: "bs_td.SearchFlowTemplatesResponseTypeDef",
    ) -> "dc_td.SearchFlowTemplatesResponse":
        return dc_td.SearchFlowTemplatesResponse.make_one(res)

    def search_system_instances(
        self,
        res: "bs_td.SearchSystemInstancesResponseTypeDef",
    ) -> "dc_td.SearchSystemInstancesResponse":
        return dc_td.SearchSystemInstancesResponse.make_one(res)

    def search_system_templates(
        self,
        res: "bs_td.SearchSystemTemplatesResponseTypeDef",
    ) -> "dc_td.SearchSystemTemplatesResponse":
        return dc_td.SearchSystemTemplatesResponse.make_one(res)

    def search_things(
        self,
        res: "bs_td.SearchThingsResponseTypeDef",
    ) -> "dc_td.SearchThingsResponse":
        return dc_td.SearchThingsResponse.make_one(res)

    def undeploy_system_instance(
        self,
        res: "bs_td.UndeploySystemInstanceResponseTypeDef",
    ) -> "dc_td.UndeploySystemInstanceResponse":
        return dc_td.UndeploySystemInstanceResponse.make_one(res)

    def update_flow_template(
        self,
        res: "bs_td.UpdateFlowTemplateResponseTypeDef",
    ) -> "dc_td.UpdateFlowTemplateResponse":
        return dc_td.UpdateFlowTemplateResponse.make_one(res)

    def update_system_template(
        self,
        res: "bs_td.UpdateSystemTemplateResponseTypeDef",
    ) -> "dc_td.UpdateSystemTemplateResponse":
        return dc_td.UpdateSystemTemplateResponse.make_one(res)

    def upload_entity_definitions(
        self,
        res: "bs_td.UploadEntityDefinitionsResponseTypeDef",
    ) -> "dc_td.UploadEntityDefinitionsResponse":
        return dc_td.UploadEntityDefinitionsResponse.make_one(res)


iotthingsgraph_caster = IOTTHINGSGRAPHCaster()
