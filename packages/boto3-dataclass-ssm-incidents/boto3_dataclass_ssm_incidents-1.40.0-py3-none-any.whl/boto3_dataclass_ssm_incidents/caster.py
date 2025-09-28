# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ssm_incidents import type_defs as bs_td


class SSM_INCIDENTSCaster:

    def batch_get_incident_findings(
        self,
        res: "bs_td.BatchGetIncidentFindingsOutputTypeDef",
    ) -> "dc_td.BatchGetIncidentFindingsOutput":
        return dc_td.BatchGetIncidentFindingsOutput.make_one(res)

    def create_replication_set(
        self,
        res: "bs_td.CreateReplicationSetOutputTypeDef",
    ) -> "dc_td.CreateReplicationSetOutput":
        return dc_td.CreateReplicationSetOutput.make_one(res)

    def create_response_plan(
        self,
        res: "bs_td.CreateResponsePlanOutputTypeDef",
    ) -> "dc_td.CreateResponsePlanOutput":
        return dc_td.CreateResponsePlanOutput.make_one(res)

    def create_timeline_event(
        self,
        res: "bs_td.CreateTimelineEventOutputTypeDef",
    ) -> "dc_td.CreateTimelineEventOutput":
        return dc_td.CreateTimelineEventOutput.make_one(res)

    def get_incident_record(
        self,
        res: "bs_td.GetIncidentRecordOutputTypeDef",
    ) -> "dc_td.GetIncidentRecordOutput":
        return dc_td.GetIncidentRecordOutput.make_one(res)

    def get_replication_set(
        self,
        res: "bs_td.GetReplicationSetOutputTypeDef",
    ) -> "dc_td.GetReplicationSetOutput":
        return dc_td.GetReplicationSetOutput.make_one(res)

    def get_resource_policies(
        self,
        res: "bs_td.GetResourcePoliciesOutputTypeDef",
    ) -> "dc_td.GetResourcePoliciesOutput":
        return dc_td.GetResourcePoliciesOutput.make_one(res)

    def get_response_plan(
        self,
        res: "bs_td.GetResponsePlanOutputTypeDef",
    ) -> "dc_td.GetResponsePlanOutput":
        return dc_td.GetResponsePlanOutput.make_one(res)

    def get_timeline_event(
        self,
        res: "bs_td.GetTimelineEventOutputTypeDef",
    ) -> "dc_td.GetTimelineEventOutput":
        return dc_td.GetTimelineEventOutput.make_one(res)

    def list_incident_findings(
        self,
        res: "bs_td.ListIncidentFindingsOutputTypeDef",
    ) -> "dc_td.ListIncidentFindingsOutput":
        return dc_td.ListIncidentFindingsOutput.make_one(res)

    def list_incident_records(
        self,
        res: "bs_td.ListIncidentRecordsOutputTypeDef",
    ) -> "dc_td.ListIncidentRecordsOutput":
        return dc_td.ListIncidentRecordsOutput.make_one(res)

    def list_related_items(
        self,
        res: "bs_td.ListRelatedItemsOutputTypeDef",
    ) -> "dc_td.ListRelatedItemsOutput":
        return dc_td.ListRelatedItemsOutput.make_one(res)

    def list_replication_sets(
        self,
        res: "bs_td.ListReplicationSetsOutputTypeDef",
    ) -> "dc_td.ListReplicationSetsOutput":
        return dc_td.ListReplicationSetsOutput.make_one(res)

    def list_response_plans(
        self,
        res: "bs_td.ListResponsePlansOutputTypeDef",
    ) -> "dc_td.ListResponsePlansOutput":
        return dc_td.ListResponsePlansOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_timeline_events(
        self,
        res: "bs_td.ListTimelineEventsOutputTypeDef",
    ) -> "dc_td.ListTimelineEventsOutput":
        return dc_td.ListTimelineEventsOutput.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyOutputTypeDef",
    ) -> "dc_td.PutResourcePolicyOutput":
        return dc_td.PutResourcePolicyOutput.make_one(res)

    def start_incident(
        self,
        res: "bs_td.StartIncidentOutputTypeDef",
    ) -> "dc_td.StartIncidentOutput":
        return dc_td.StartIncidentOutput.make_one(res)


ssm_incidents_caster = SSM_INCIDENTSCaster()
