# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_osis import type_defs as bs_td


class OSISCaster:

    def create_pipeline(
        self,
        res: "bs_td.CreatePipelineResponseTypeDef",
    ) -> "dc_td.CreatePipelineResponse":
        return dc_td.CreatePipelineResponse.make_one(res)

    def create_pipeline_endpoint(
        self,
        res: "bs_td.CreatePipelineEndpointResponseTypeDef",
    ) -> "dc_td.CreatePipelineEndpointResponse":
        return dc_td.CreatePipelineEndpointResponse.make_one(res)

    def get_pipeline(
        self,
        res: "bs_td.GetPipelineResponseTypeDef",
    ) -> "dc_td.GetPipelineResponse":
        return dc_td.GetPipelineResponse.make_one(res)

    def get_pipeline_blueprint(
        self,
        res: "bs_td.GetPipelineBlueprintResponseTypeDef",
    ) -> "dc_td.GetPipelineBlueprintResponse":
        return dc_td.GetPipelineBlueprintResponse.make_one(res)

    def get_pipeline_change_progress(
        self,
        res: "bs_td.GetPipelineChangeProgressResponseTypeDef",
    ) -> "dc_td.GetPipelineChangeProgressResponse":
        return dc_td.GetPipelineChangeProgressResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def list_pipeline_blueprints(
        self,
        res: "bs_td.ListPipelineBlueprintsResponseTypeDef",
    ) -> "dc_td.ListPipelineBlueprintsResponse":
        return dc_td.ListPipelineBlueprintsResponse.make_one(res)

    def list_pipeline_endpoint_connections(
        self,
        res: "bs_td.ListPipelineEndpointConnectionsResponseTypeDef",
    ) -> "dc_td.ListPipelineEndpointConnectionsResponse":
        return dc_td.ListPipelineEndpointConnectionsResponse.make_one(res)

    def list_pipeline_endpoints(
        self,
        res: "bs_td.ListPipelineEndpointsResponseTypeDef",
    ) -> "dc_td.ListPipelineEndpointsResponse":
        return dc_td.ListPipelineEndpointsResponse.make_one(res)

    def list_pipelines(
        self,
        res: "bs_td.ListPipelinesResponseTypeDef",
    ) -> "dc_td.ListPipelinesResponse":
        return dc_td.ListPipelinesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def revoke_pipeline_endpoint_connections(
        self,
        res: "bs_td.RevokePipelineEndpointConnectionsResponseTypeDef",
    ) -> "dc_td.RevokePipelineEndpointConnectionsResponse":
        return dc_td.RevokePipelineEndpointConnectionsResponse.make_one(res)

    def start_pipeline(
        self,
        res: "bs_td.StartPipelineResponseTypeDef",
    ) -> "dc_td.StartPipelineResponse":
        return dc_td.StartPipelineResponse.make_one(res)

    def stop_pipeline(
        self,
        res: "bs_td.StopPipelineResponseTypeDef",
    ) -> "dc_td.StopPipelineResponse":
        return dc_td.StopPipelineResponse.make_one(res)

    def update_pipeline(
        self,
        res: "bs_td.UpdatePipelineResponseTypeDef",
    ) -> "dc_td.UpdatePipelineResponse":
        return dc_td.UpdatePipelineResponse.make_one(res)

    def validate_pipeline(
        self,
        res: "bs_td.ValidatePipelineResponseTypeDef",
    ) -> "dc_td.ValidatePipelineResponse":
        return dc_td.ValidatePipelineResponse.make_one(res)


osis_caster = OSISCaster()
