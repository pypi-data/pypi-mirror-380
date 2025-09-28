# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mediaconvert import type_defs as bs_td


class MEDIACONVERTCaster:

    def create_job(
        self,
        res: "bs_td.CreateJobResponseTypeDef",
    ) -> "dc_td.CreateJobResponse":
        return dc_td.CreateJobResponse.make_one(res)

    def create_job_template(
        self,
        res: "bs_td.CreateJobTemplateResponseTypeDef",
    ) -> "dc_td.CreateJobTemplateResponse":
        return dc_td.CreateJobTemplateResponse.make_one(res)

    def create_preset(
        self,
        res: "bs_td.CreatePresetResponseTypeDef",
    ) -> "dc_td.CreatePresetResponse":
        return dc_td.CreatePresetResponse.make_one(res)

    def create_queue(
        self,
        res: "bs_td.CreateQueueResponseTypeDef",
    ) -> "dc_td.CreateQueueResponse":
        return dc_td.CreateQueueResponse.make_one(res)

    def describe_endpoints(
        self,
        res: "bs_td.DescribeEndpointsResponseTypeDef",
    ) -> "dc_td.DescribeEndpointsResponse":
        return dc_td.DescribeEndpointsResponse.make_one(res)

    def get_job(
        self,
        res: "bs_td.GetJobResponseTypeDef",
    ) -> "dc_td.GetJobResponse":
        return dc_td.GetJobResponse.make_one(res)

    def get_job_template(
        self,
        res: "bs_td.GetJobTemplateResponseTypeDef",
    ) -> "dc_td.GetJobTemplateResponse":
        return dc_td.GetJobTemplateResponse.make_one(res)

    def get_policy(
        self,
        res: "bs_td.GetPolicyResponseTypeDef",
    ) -> "dc_td.GetPolicyResponse":
        return dc_td.GetPolicyResponse.make_one(res)

    def get_preset(
        self,
        res: "bs_td.GetPresetResponseTypeDef",
    ) -> "dc_td.GetPresetResponse":
        return dc_td.GetPresetResponse.make_one(res)

    def get_queue(
        self,
        res: "bs_td.GetQueueResponseTypeDef",
    ) -> "dc_td.GetQueueResponse":
        return dc_td.GetQueueResponse.make_one(res)

    def list_job_templates(
        self,
        res: "bs_td.ListJobTemplatesResponseTypeDef",
    ) -> "dc_td.ListJobTemplatesResponse":
        return dc_td.ListJobTemplatesResponse.make_one(res)

    def list_jobs(
        self,
        res: "bs_td.ListJobsResponseTypeDef",
    ) -> "dc_td.ListJobsResponse":
        return dc_td.ListJobsResponse.make_one(res)

    def list_presets(
        self,
        res: "bs_td.ListPresetsResponseTypeDef",
    ) -> "dc_td.ListPresetsResponse":
        return dc_td.ListPresetsResponse.make_one(res)

    def list_queues(
        self,
        res: "bs_td.ListQueuesResponseTypeDef",
    ) -> "dc_td.ListQueuesResponse":
        return dc_td.ListQueuesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_versions(
        self,
        res: "bs_td.ListVersionsResponseTypeDef",
    ) -> "dc_td.ListVersionsResponse":
        return dc_td.ListVersionsResponse.make_one(res)

    def probe(
        self,
        res: "bs_td.ProbeResponseTypeDef",
    ) -> "dc_td.ProbeResponse":
        return dc_td.ProbeResponse.make_one(res)

    def put_policy(
        self,
        res: "bs_td.PutPolicyResponseTypeDef",
    ) -> "dc_td.PutPolicyResponse":
        return dc_td.PutPolicyResponse.make_one(res)

    def search_jobs(
        self,
        res: "bs_td.SearchJobsResponseTypeDef",
    ) -> "dc_td.SearchJobsResponse":
        return dc_td.SearchJobsResponse.make_one(res)

    def update_job_template(
        self,
        res: "bs_td.UpdateJobTemplateResponseTypeDef",
    ) -> "dc_td.UpdateJobTemplateResponse":
        return dc_td.UpdateJobTemplateResponse.make_one(res)

    def update_preset(
        self,
        res: "bs_td.UpdatePresetResponseTypeDef",
    ) -> "dc_td.UpdatePresetResponse":
        return dc_td.UpdatePresetResponse.make_one(res)

    def update_queue(
        self,
        res: "bs_td.UpdateQueueResponseTypeDef",
    ) -> "dc_td.UpdateQueueResponse":
        return dc_td.UpdateQueueResponse.make_one(res)


mediaconvert_caster = MEDIACONVERTCaster()
