# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mturk import type_defs as bs_td


class MTURKCaster:

    def create_hit(
        self,
        res: "bs_td.CreateHITResponseTypeDef",
    ) -> "dc_td.CreateHITResponse":
        return dc_td.CreateHITResponse.make_one(res)

    def create_hit_type(
        self,
        res: "bs_td.CreateHITTypeResponseTypeDef",
    ) -> "dc_td.CreateHITTypeResponse":
        return dc_td.CreateHITTypeResponse.make_one(res)

    def create_hit_with_hit_type(
        self,
        res: "bs_td.CreateHITWithHITTypeResponseTypeDef",
    ) -> "dc_td.CreateHITWithHITTypeResponse":
        return dc_td.CreateHITWithHITTypeResponse.make_one(res)

    def create_qualification_type(
        self,
        res: "bs_td.CreateQualificationTypeResponseTypeDef",
    ) -> "dc_td.CreateQualificationTypeResponse":
        return dc_td.CreateQualificationTypeResponse.make_one(res)

    def get_account_balance(
        self,
        res: "bs_td.GetAccountBalanceResponseTypeDef",
    ) -> "dc_td.GetAccountBalanceResponse":
        return dc_td.GetAccountBalanceResponse.make_one(res)

    def get_assignment(
        self,
        res: "bs_td.GetAssignmentResponseTypeDef",
    ) -> "dc_td.GetAssignmentResponse":
        return dc_td.GetAssignmentResponse.make_one(res)

    def get_file_upload_url(
        self,
        res: "bs_td.GetFileUploadURLResponseTypeDef",
    ) -> "dc_td.GetFileUploadURLResponse":
        return dc_td.GetFileUploadURLResponse.make_one(res)

    def get_hit(
        self,
        res: "bs_td.GetHITResponseTypeDef",
    ) -> "dc_td.GetHITResponse":
        return dc_td.GetHITResponse.make_one(res)

    def get_qualification_score(
        self,
        res: "bs_td.GetQualificationScoreResponseTypeDef",
    ) -> "dc_td.GetQualificationScoreResponse":
        return dc_td.GetQualificationScoreResponse.make_one(res)

    def get_qualification_type(
        self,
        res: "bs_td.GetQualificationTypeResponseTypeDef",
    ) -> "dc_td.GetQualificationTypeResponse":
        return dc_td.GetQualificationTypeResponse.make_one(res)

    def list_assignments_for_hit(
        self,
        res: "bs_td.ListAssignmentsForHITResponseTypeDef",
    ) -> "dc_td.ListAssignmentsForHITResponse":
        return dc_td.ListAssignmentsForHITResponse.make_one(res)

    def list_bonus_payments(
        self,
        res: "bs_td.ListBonusPaymentsResponseTypeDef",
    ) -> "dc_td.ListBonusPaymentsResponse":
        return dc_td.ListBonusPaymentsResponse.make_one(res)

    def list_hits(
        self,
        res: "bs_td.ListHITsResponseTypeDef",
    ) -> "dc_td.ListHITsResponse":
        return dc_td.ListHITsResponse.make_one(res)

    def list_hits_for_qualification_type(
        self,
        res: "bs_td.ListHITsForQualificationTypeResponseTypeDef",
    ) -> "dc_td.ListHITsForQualificationTypeResponse":
        return dc_td.ListHITsForQualificationTypeResponse.make_one(res)

    def list_qualification_requests(
        self,
        res: "bs_td.ListQualificationRequestsResponseTypeDef",
    ) -> "dc_td.ListQualificationRequestsResponse":
        return dc_td.ListQualificationRequestsResponse.make_one(res)

    def list_qualification_types(
        self,
        res: "bs_td.ListQualificationTypesResponseTypeDef",
    ) -> "dc_td.ListQualificationTypesResponse":
        return dc_td.ListQualificationTypesResponse.make_one(res)

    def list_review_policy_results_for_hit(
        self,
        res: "bs_td.ListReviewPolicyResultsForHITResponseTypeDef",
    ) -> "dc_td.ListReviewPolicyResultsForHITResponse":
        return dc_td.ListReviewPolicyResultsForHITResponse.make_one(res)

    def list_reviewable_hits(
        self,
        res: "bs_td.ListReviewableHITsResponseTypeDef",
    ) -> "dc_td.ListReviewableHITsResponse":
        return dc_td.ListReviewableHITsResponse.make_one(res)

    def list_worker_blocks(
        self,
        res: "bs_td.ListWorkerBlocksResponseTypeDef",
    ) -> "dc_td.ListWorkerBlocksResponse":
        return dc_td.ListWorkerBlocksResponse.make_one(res)

    def list_workers_with_qualification_type(
        self,
        res: "bs_td.ListWorkersWithQualificationTypeResponseTypeDef",
    ) -> "dc_td.ListWorkersWithQualificationTypeResponse":
        return dc_td.ListWorkersWithQualificationTypeResponse.make_one(res)

    def notify_workers(
        self,
        res: "bs_td.NotifyWorkersResponseTypeDef",
    ) -> "dc_td.NotifyWorkersResponse":
        return dc_td.NotifyWorkersResponse.make_one(res)

    def update_qualification_type(
        self,
        res: "bs_td.UpdateQualificationTypeResponseTypeDef",
    ) -> "dc_td.UpdateQualificationTypeResponse":
        return dc_td.UpdateQualificationTypeResponse.make_one(res)


mturk_caster = MTURKCaster()
