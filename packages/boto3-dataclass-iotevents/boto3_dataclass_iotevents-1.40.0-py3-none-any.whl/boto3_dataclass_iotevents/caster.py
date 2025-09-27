# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotevents import type_defs as bs_td


class IOTEVENTSCaster:

    def create_alarm_model(
        self,
        res: "bs_td.CreateAlarmModelResponseTypeDef",
    ) -> "dc_td.CreateAlarmModelResponse":
        return dc_td.CreateAlarmModelResponse.make_one(res)

    def create_detector_model(
        self,
        res: "bs_td.CreateDetectorModelResponseTypeDef",
    ) -> "dc_td.CreateDetectorModelResponse":
        return dc_td.CreateDetectorModelResponse.make_one(res)

    def create_input(
        self,
        res: "bs_td.CreateInputResponseTypeDef",
    ) -> "dc_td.CreateInputResponse":
        return dc_td.CreateInputResponse.make_one(res)

    def describe_alarm_model(
        self,
        res: "bs_td.DescribeAlarmModelResponseTypeDef",
    ) -> "dc_td.DescribeAlarmModelResponse":
        return dc_td.DescribeAlarmModelResponse.make_one(res)

    def describe_detector_model(
        self,
        res: "bs_td.DescribeDetectorModelResponseTypeDef",
    ) -> "dc_td.DescribeDetectorModelResponse":
        return dc_td.DescribeDetectorModelResponse.make_one(res)

    def describe_detector_model_analysis(
        self,
        res: "bs_td.DescribeDetectorModelAnalysisResponseTypeDef",
    ) -> "dc_td.DescribeDetectorModelAnalysisResponse":
        return dc_td.DescribeDetectorModelAnalysisResponse.make_one(res)

    def describe_input(
        self,
        res: "bs_td.DescribeInputResponseTypeDef",
    ) -> "dc_td.DescribeInputResponse":
        return dc_td.DescribeInputResponse.make_one(res)

    def describe_logging_options(
        self,
        res: "bs_td.DescribeLoggingOptionsResponseTypeDef",
    ) -> "dc_td.DescribeLoggingOptionsResponse":
        return dc_td.DescribeLoggingOptionsResponse.make_one(res)

    def get_detector_model_analysis_results(
        self,
        res: "bs_td.GetDetectorModelAnalysisResultsResponseTypeDef",
    ) -> "dc_td.GetDetectorModelAnalysisResultsResponse":
        return dc_td.GetDetectorModelAnalysisResultsResponse.make_one(res)

    def list_alarm_model_versions(
        self,
        res: "bs_td.ListAlarmModelVersionsResponseTypeDef",
    ) -> "dc_td.ListAlarmModelVersionsResponse":
        return dc_td.ListAlarmModelVersionsResponse.make_one(res)

    def list_alarm_models(
        self,
        res: "bs_td.ListAlarmModelsResponseTypeDef",
    ) -> "dc_td.ListAlarmModelsResponse":
        return dc_td.ListAlarmModelsResponse.make_one(res)

    def list_detector_model_versions(
        self,
        res: "bs_td.ListDetectorModelVersionsResponseTypeDef",
    ) -> "dc_td.ListDetectorModelVersionsResponse":
        return dc_td.ListDetectorModelVersionsResponse.make_one(res)

    def list_detector_models(
        self,
        res: "bs_td.ListDetectorModelsResponseTypeDef",
    ) -> "dc_td.ListDetectorModelsResponse":
        return dc_td.ListDetectorModelsResponse.make_one(res)

    def list_input_routings(
        self,
        res: "bs_td.ListInputRoutingsResponseTypeDef",
    ) -> "dc_td.ListInputRoutingsResponse":
        return dc_td.ListInputRoutingsResponse.make_one(res)

    def list_inputs(
        self,
        res: "bs_td.ListInputsResponseTypeDef",
    ) -> "dc_td.ListInputsResponse":
        return dc_td.ListInputsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_logging_options(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_detector_model_analysis(
        self,
        res: "bs_td.StartDetectorModelAnalysisResponseTypeDef",
    ) -> "dc_td.StartDetectorModelAnalysisResponse":
        return dc_td.StartDetectorModelAnalysisResponse.make_one(res)

    def update_alarm_model(
        self,
        res: "bs_td.UpdateAlarmModelResponseTypeDef",
    ) -> "dc_td.UpdateAlarmModelResponse":
        return dc_td.UpdateAlarmModelResponse.make_one(res)

    def update_detector_model(
        self,
        res: "bs_td.UpdateDetectorModelResponseTypeDef",
    ) -> "dc_td.UpdateDetectorModelResponse":
        return dc_td.UpdateDetectorModelResponse.make_one(res)

    def update_input(
        self,
        res: "bs_td.UpdateInputResponseTypeDef",
    ) -> "dc_td.UpdateInputResponse":
        return dc_td.UpdateInputResponse.make_one(res)


iotevents_caster = IOTEVENTSCaster()
