# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ssm_contacts import type_defs as bs_td


class SSM_CONTACTSCaster:

    def create_contact(
        self,
        res: "bs_td.CreateContactResultTypeDef",
    ) -> "dc_td.CreateContactResult":
        return dc_td.CreateContactResult.make_one(res)

    def create_contact_channel(
        self,
        res: "bs_td.CreateContactChannelResultTypeDef",
    ) -> "dc_td.CreateContactChannelResult":
        return dc_td.CreateContactChannelResult.make_one(res)

    def create_rotation(
        self,
        res: "bs_td.CreateRotationResultTypeDef",
    ) -> "dc_td.CreateRotationResult":
        return dc_td.CreateRotationResult.make_one(res)

    def create_rotation_override(
        self,
        res: "bs_td.CreateRotationOverrideResultTypeDef",
    ) -> "dc_td.CreateRotationOverrideResult":
        return dc_td.CreateRotationOverrideResult.make_one(res)

    def describe_engagement(
        self,
        res: "bs_td.DescribeEngagementResultTypeDef",
    ) -> "dc_td.DescribeEngagementResult":
        return dc_td.DescribeEngagementResult.make_one(res)

    def describe_page(
        self,
        res: "bs_td.DescribePageResultTypeDef",
    ) -> "dc_td.DescribePageResult":
        return dc_td.DescribePageResult.make_one(res)

    def get_contact(
        self,
        res: "bs_td.GetContactResultTypeDef",
    ) -> "dc_td.GetContactResult":
        return dc_td.GetContactResult.make_one(res)

    def get_contact_channel(
        self,
        res: "bs_td.GetContactChannelResultTypeDef",
    ) -> "dc_td.GetContactChannelResult":
        return dc_td.GetContactChannelResult.make_one(res)

    def get_contact_policy(
        self,
        res: "bs_td.GetContactPolicyResultTypeDef",
    ) -> "dc_td.GetContactPolicyResult":
        return dc_td.GetContactPolicyResult.make_one(res)

    def get_rotation(
        self,
        res: "bs_td.GetRotationResultTypeDef",
    ) -> "dc_td.GetRotationResult":
        return dc_td.GetRotationResult.make_one(res)

    def get_rotation_override(
        self,
        res: "bs_td.GetRotationOverrideResultTypeDef",
    ) -> "dc_td.GetRotationOverrideResult":
        return dc_td.GetRotationOverrideResult.make_one(res)

    def list_contact_channels(
        self,
        res: "bs_td.ListContactChannelsResultTypeDef",
    ) -> "dc_td.ListContactChannelsResult":
        return dc_td.ListContactChannelsResult.make_one(res)

    def list_contacts(
        self,
        res: "bs_td.ListContactsResultTypeDef",
    ) -> "dc_td.ListContactsResult":
        return dc_td.ListContactsResult.make_one(res)

    def list_engagements(
        self,
        res: "bs_td.ListEngagementsResultTypeDef",
    ) -> "dc_td.ListEngagementsResult":
        return dc_td.ListEngagementsResult.make_one(res)

    def list_page_receipts(
        self,
        res: "bs_td.ListPageReceiptsResultTypeDef",
    ) -> "dc_td.ListPageReceiptsResult":
        return dc_td.ListPageReceiptsResult.make_one(res)

    def list_page_resolutions(
        self,
        res: "bs_td.ListPageResolutionsResultTypeDef",
    ) -> "dc_td.ListPageResolutionsResult":
        return dc_td.ListPageResolutionsResult.make_one(res)

    def list_pages_by_contact(
        self,
        res: "bs_td.ListPagesByContactResultTypeDef",
    ) -> "dc_td.ListPagesByContactResult":
        return dc_td.ListPagesByContactResult.make_one(res)

    def list_pages_by_engagement(
        self,
        res: "bs_td.ListPagesByEngagementResultTypeDef",
    ) -> "dc_td.ListPagesByEngagementResult":
        return dc_td.ListPagesByEngagementResult.make_one(res)

    def list_preview_rotation_shifts(
        self,
        res: "bs_td.ListPreviewRotationShiftsResultTypeDef",
    ) -> "dc_td.ListPreviewRotationShiftsResult":
        return dc_td.ListPreviewRotationShiftsResult.make_one(res)

    def list_rotation_overrides(
        self,
        res: "bs_td.ListRotationOverridesResultTypeDef",
    ) -> "dc_td.ListRotationOverridesResult":
        return dc_td.ListRotationOverridesResult.make_one(res)

    def list_rotation_shifts(
        self,
        res: "bs_td.ListRotationShiftsResultTypeDef",
    ) -> "dc_td.ListRotationShiftsResult":
        return dc_td.ListRotationShiftsResult.make_one(res)

    def list_rotations(
        self,
        res: "bs_td.ListRotationsResultTypeDef",
    ) -> "dc_td.ListRotationsResult":
        return dc_td.ListRotationsResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResultTypeDef",
    ) -> "dc_td.ListTagsForResourceResult":
        return dc_td.ListTagsForResourceResult.make_one(res)

    def start_engagement(
        self,
        res: "bs_td.StartEngagementResultTypeDef",
    ) -> "dc_td.StartEngagementResult":
        return dc_td.StartEngagementResult.make_one(res)


ssm_contacts_caster = SSM_CONTACTSCaster()
