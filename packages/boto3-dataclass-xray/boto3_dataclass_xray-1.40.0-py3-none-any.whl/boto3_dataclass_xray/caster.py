# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_xray import type_defs as bs_td


class XRAYCaster:

    def batch_get_traces(
        self,
        res: "bs_td.BatchGetTracesResultTypeDef",
    ) -> "dc_td.BatchGetTracesResult":
        return dc_td.BatchGetTracesResult.make_one(res)

    def create_group(
        self,
        res: "bs_td.CreateGroupResultTypeDef",
    ) -> "dc_td.CreateGroupResult":
        return dc_td.CreateGroupResult.make_one(res)

    def create_sampling_rule(
        self,
        res: "bs_td.CreateSamplingRuleResultTypeDef",
    ) -> "dc_td.CreateSamplingRuleResult":
        return dc_td.CreateSamplingRuleResult.make_one(res)

    def delete_sampling_rule(
        self,
        res: "bs_td.DeleteSamplingRuleResultTypeDef",
    ) -> "dc_td.DeleteSamplingRuleResult":
        return dc_td.DeleteSamplingRuleResult.make_one(res)

    def get_encryption_config(
        self,
        res: "bs_td.GetEncryptionConfigResultTypeDef",
    ) -> "dc_td.GetEncryptionConfigResult":
        return dc_td.GetEncryptionConfigResult.make_one(res)

    def get_group(
        self,
        res: "bs_td.GetGroupResultTypeDef",
    ) -> "dc_td.GetGroupResult":
        return dc_td.GetGroupResult.make_one(res)

    def get_groups(
        self,
        res: "bs_td.GetGroupsResultTypeDef",
    ) -> "dc_td.GetGroupsResult":
        return dc_td.GetGroupsResult.make_one(res)

    def get_indexing_rules(
        self,
        res: "bs_td.GetIndexingRulesResultTypeDef",
    ) -> "dc_td.GetIndexingRulesResult":
        return dc_td.GetIndexingRulesResult.make_one(res)

    def get_insight(
        self,
        res: "bs_td.GetInsightResultTypeDef",
    ) -> "dc_td.GetInsightResult":
        return dc_td.GetInsightResult.make_one(res)

    def get_insight_events(
        self,
        res: "bs_td.GetInsightEventsResultTypeDef",
    ) -> "dc_td.GetInsightEventsResult":
        return dc_td.GetInsightEventsResult.make_one(res)

    def get_insight_impact_graph(
        self,
        res: "bs_td.GetInsightImpactGraphResultTypeDef",
    ) -> "dc_td.GetInsightImpactGraphResult":
        return dc_td.GetInsightImpactGraphResult.make_one(res)

    def get_insight_summaries(
        self,
        res: "bs_td.GetInsightSummariesResultTypeDef",
    ) -> "dc_td.GetInsightSummariesResult":
        return dc_td.GetInsightSummariesResult.make_one(res)

    def get_retrieved_traces_graph(
        self,
        res: "bs_td.GetRetrievedTracesGraphResultTypeDef",
    ) -> "dc_td.GetRetrievedTracesGraphResult":
        return dc_td.GetRetrievedTracesGraphResult.make_one(res)

    def get_sampling_rules(
        self,
        res: "bs_td.GetSamplingRulesResultTypeDef",
    ) -> "dc_td.GetSamplingRulesResult":
        return dc_td.GetSamplingRulesResult.make_one(res)

    def get_sampling_statistic_summaries(
        self,
        res: "bs_td.GetSamplingStatisticSummariesResultTypeDef",
    ) -> "dc_td.GetSamplingStatisticSummariesResult":
        return dc_td.GetSamplingStatisticSummariesResult.make_one(res)

    def get_sampling_targets(
        self,
        res: "bs_td.GetSamplingTargetsResultTypeDef",
    ) -> "dc_td.GetSamplingTargetsResult":
        return dc_td.GetSamplingTargetsResult.make_one(res)

    def get_service_graph(
        self,
        res: "bs_td.GetServiceGraphResultTypeDef",
    ) -> "dc_td.GetServiceGraphResult":
        return dc_td.GetServiceGraphResult.make_one(res)

    def get_time_series_service_statistics(
        self,
        res: "bs_td.GetTimeSeriesServiceStatisticsResultTypeDef",
    ) -> "dc_td.GetTimeSeriesServiceStatisticsResult":
        return dc_td.GetTimeSeriesServiceStatisticsResult.make_one(res)

    def get_trace_graph(
        self,
        res: "bs_td.GetTraceGraphResultTypeDef",
    ) -> "dc_td.GetTraceGraphResult":
        return dc_td.GetTraceGraphResult.make_one(res)

    def get_trace_segment_destination(
        self,
        res: "bs_td.GetTraceSegmentDestinationResultTypeDef",
    ) -> "dc_td.GetTraceSegmentDestinationResult":
        return dc_td.GetTraceSegmentDestinationResult.make_one(res)

    def get_trace_summaries(
        self,
        res: "bs_td.GetTraceSummariesResultTypeDef",
    ) -> "dc_td.GetTraceSummariesResult":
        return dc_td.GetTraceSummariesResult.make_one(res)

    def list_resource_policies(
        self,
        res: "bs_td.ListResourcePoliciesResultTypeDef",
    ) -> "dc_td.ListResourcePoliciesResult":
        return dc_td.ListResourcePoliciesResult.make_one(res)

    def list_retrieved_traces(
        self,
        res: "bs_td.ListRetrievedTracesResultTypeDef",
    ) -> "dc_td.ListRetrievedTracesResult":
        return dc_td.ListRetrievedTracesResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_encryption_config(
        self,
        res: "bs_td.PutEncryptionConfigResultTypeDef",
    ) -> "dc_td.PutEncryptionConfigResult":
        return dc_td.PutEncryptionConfigResult.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResultTypeDef",
    ) -> "dc_td.PutResourcePolicyResult":
        return dc_td.PutResourcePolicyResult.make_one(res)

    def put_trace_segments(
        self,
        res: "bs_td.PutTraceSegmentsResultTypeDef",
    ) -> "dc_td.PutTraceSegmentsResult":
        return dc_td.PutTraceSegmentsResult.make_one(res)

    def start_trace_retrieval(
        self,
        res: "bs_td.StartTraceRetrievalResultTypeDef",
    ) -> "dc_td.StartTraceRetrievalResult":
        return dc_td.StartTraceRetrievalResult.make_one(res)

    def update_group(
        self,
        res: "bs_td.UpdateGroupResultTypeDef",
    ) -> "dc_td.UpdateGroupResult":
        return dc_td.UpdateGroupResult.make_one(res)

    def update_indexing_rule(
        self,
        res: "bs_td.UpdateIndexingRuleResultTypeDef",
    ) -> "dc_td.UpdateIndexingRuleResult":
        return dc_td.UpdateIndexingRuleResult.make_one(res)

    def update_sampling_rule(
        self,
        res: "bs_td.UpdateSamplingRuleResultTypeDef",
    ) -> "dc_td.UpdateSamplingRuleResult":
        return dc_td.UpdateSamplingRuleResult.make_one(res)

    def update_trace_segment_destination(
        self,
        res: "bs_td.UpdateTraceSegmentDestinationResultTypeDef",
    ) -> "dc_td.UpdateTraceSegmentDestinationResult":
        return dc_td.UpdateTraceSegmentDestinationResult.make_one(res)


xray_caster = XRAYCaster()
