# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_security_ir import type_defs as bs_td


class SECURITY_IRCaster:

    def batch_get_member_account_details(
        self,
        res: "bs_td.BatchGetMemberAccountDetailsResponseTypeDef",
    ) -> "dc_td.BatchGetMemberAccountDetailsResponse":
        return dc_td.BatchGetMemberAccountDetailsResponse.make_one(res)

    def cancel_membership(
        self,
        res: "bs_td.CancelMembershipResponseTypeDef",
    ) -> "dc_td.CancelMembershipResponse":
        return dc_td.CancelMembershipResponse.make_one(res)

    def close_case(
        self,
        res: "bs_td.CloseCaseResponseTypeDef",
    ) -> "dc_td.CloseCaseResponse":
        return dc_td.CloseCaseResponse.make_one(res)

    def create_case(
        self,
        res: "bs_td.CreateCaseResponseTypeDef",
    ) -> "dc_td.CreateCaseResponse":
        return dc_td.CreateCaseResponse.make_one(res)

    def create_case_comment(
        self,
        res: "bs_td.CreateCaseCommentResponseTypeDef",
    ) -> "dc_td.CreateCaseCommentResponse":
        return dc_td.CreateCaseCommentResponse.make_one(res)

    def create_membership(
        self,
        res: "bs_td.CreateMembershipResponseTypeDef",
    ) -> "dc_td.CreateMembershipResponse":
        return dc_td.CreateMembershipResponse.make_one(res)

    def get_case(
        self,
        res: "bs_td.GetCaseResponseTypeDef",
    ) -> "dc_td.GetCaseResponse":
        return dc_td.GetCaseResponse.make_one(res)

    def get_case_attachment_download_url(
        self,
        res: "bs_td.GetCaseAttachmentDownloadUrlResponseTypeDef",
    ) -> "dc_td.GetCaseAttachmentDownloadUrlResponse":
        return dc_td.GetCaseAttachmentDownloadUrlResponse.make_one(res)

    def get_case_attachment_upload_url(
        self,
        res: "bs_td.GetCaseAttachmentUploadUrlResponseTypeDef",
    ) -> "dc_td.GetCaseAttachmentUploadUrlResponse":
        return dc_td.GetCaseAttachmentUploadUrlResponse.make_one(res)

    def get_membership(
        self,
        res: "bs_td.GetMembershipResponseTypeDef",
    ) -> "dc_td.GetMembershipResponse":
        return dc_td.GetMembershipResponse.make_one(res)

    def list_case_edits(
        self,
        res: "bs_td.ListCaseEditsResponseTypeDef",
    ) -> "dc_td.ListCaseEditsResponse":
        return dc_td.ListCaseEditsResponse.make_one(res)

    def list_cases(
        self,
        res: "bs_td.ListCasesResponseTypeDef",
    ) -> "dc_td.ListCasesResponse":
        return dc_td.ListCasesResponse.make_one(res)

    def list_comments(
        self,
        res: "bs_td.ListCommentsResponseTypeDef",
    ) -> "dc_td.ListCommentsResponse":
        return dc_td.ListCommentsResponse.make_one(res)

    def list_memberships(
        self,
        res: "bs_td.ListMembershipsResponseTypeDef",
    ) -> "dc_td.ListMembershipsResponse":
        return dc_td.ListMembershipsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def update_case_comment(
        self,
        res: "bs_td.UpdateCaseCommentResponseTypeDef",
    ) -> "dc_td.UpdateCaseCommentResponse":
        return dc_td.UpdateCaseCommentResponse.make_one(res)

    def update_case_status(
        self,
        res: "bs_td.UpdateCaseStatusResponseTypeDef",
    ) -> "dc_td.UpdateCaseStatusResponse":
        return dc_td.UpdateCaseStatusResponse.make_one(res)

    def update_resolver_type(
        self,
        res: "bs_td.UpdateResolverTypeResponseTypeDef",
    ) -> "dc_td.UpdateResolverTypeResponse":
        return dc_td.UpdateResolverTypeResponse.make_one(res)


security_ir_caster = SECURITY_IRCaster()
