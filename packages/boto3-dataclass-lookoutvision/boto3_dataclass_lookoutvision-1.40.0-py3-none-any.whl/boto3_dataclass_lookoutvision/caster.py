# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lookoutvision import type_defs as bs_td


class LOOKOUTVISIONCaster:

    def create_dataset(
        self,
        res: "bs_td.CreateDatasetResponseTypeDef",
    ) -> "dc_td.CreateDatasetResponse":
        return dc_td.CreateDatasetResponse.make_one(res)

    def create_model(
        self,
        res: "bs_td.CreateModelResponseTypeDef",
    ) -> "dc_td.CreateModelResponse":
        return dc_td.CreateModelResponse.make_one(res)

    def create_project(
        self,
        res: "bs_td.CreateProjectResponseTypeDef",
    ) -> "dc_td.CreateProjectResponse":
        return dc_td.CreateProjectResponse.make_one(res)

    def delete_model(
        self,
        res: "bs_td.DeleteModelResponseTypeDef",
    ) -> "dc_td.DeleteModelResponse":
        return dc_td.DeleteModelResponse.make_one(res)

    def delete_project(
        self,
        res: "bs_td.DeleteProjectResponseTypeDef",
    ) -> "dc_td.DeleteProjectResponse":
        return dc_td.DeleteProjectResponse.make_one(res)

    def describe_dataset(
        self,
        res: "bs_td.DescribeDatasetResponseTypeDef",
    ) -> "dc_td.DescribeDatasetResponse":
        return dc_td.DescribeDatasetResponse.make_one(res)

    def describe_model(
        self,
        res: "bs_td.DescribeModelResponseTypeDef",
    ) -> "dc_td.DescribeModelResponse":
        return dc_td.DescribeModelResponse.make_one(res)

    def describe_model_packaging_job(
        self,
        res: "bs_td.DescribeModelPackagingJobResponseTypeDef",
    ) -> "dc_td.DescribeModelPackagingJobResponse":
        return dc_td.DescribeModelPackagingJobResponse.make_one(res)

    def describe_project(
        self,
        res: "bs_td.DescribeProjectResponseTypeDef",
    ) -> "dc_td.DescribeProjectResponse":
        return dc_td.DescribeProjectResponse.make_one(res)

    def detect_anomalies(
        self,
        res: "bs_td.DetectAnomaliesResponseTypeDef",
    ) -> "dc_td.DetectAnomaliesResponse":
        return dc_td.DetectAnomaliesResponse.make_one(res)

    def list_dataset_entries(
        self,
        res: "bs_td.ListDatasetEntriesResponseTypeDef",
    ) -> "dc_td.ListDatasetEntriesResponse":
        return dc_td.ListDatasetEntriesResponse.make_one(res)

    def list_model_packaging_jobs(
        self,
        res: "bs_td.ListModelPackagingJobsResponseTypeDef",
    ) -> "dc_td.ListModelPackagingJobsResponse":
        return dc_td.ListModelPackagingJobsResponse.make_one(res)

    def list_models(
        self,
        res: "bs_td.ListModelsResponseTypeDef",
    ) -> "dc_td.ListModelsResponse":
        return dc_td.ListModelsResponse.make_one(res)

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

    def start_model(
        self,
        res: "bs_td.StartModelResponseTypeDef",
    ) -> "dc_td.StartModelResponse":
        return dc_td.StartModelResponse.make_one(res)

    def start_model_packaging_job(
        self,
        res: "bs_td.StartModelPackagingJobResponseTypeDef",
    ) -> "dc_td.StartModelPackagingJobResponse":
        return dc_td.StartModelPackagingJobResponse.make_one(res)

    def stop_model(
        self,
        res: "bs_td.StopModelResponseTypeDef",
    ) -> "dc_td.StopModelResponse":
        return dc_td.StopModelResponse.make_one(res)

    def update_dataset_entries(
        self,
        res: "bs_td.UpdateDatasetEntriesResponseTypeDef",
    ) -> "dc_td.UpdateDatasetEntriesResponse":
        return dc_td.UpdateDatasetEntriesResponse.make_one(res)


lookoutvision_caster = LOOKOUTVISIONCaster()
