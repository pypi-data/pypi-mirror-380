# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_shield import type_defs as bs_td


class SHIELDCaster:

    def create_protection(
        self,
        res: "bs_td.CreateProtectionResponseTypeDef",
    ) -> "dc_td.CreateProtectionResponse":
        return dc_td.CreateProtectionResponse.make_one(res)

    def describe_attack(
        self,
        res: "bs_td.DescribeAttackResponseTypeDef",
    ) -> "dc_td.DescribeAttackResponse":
        return dc_td.DescribeAttackResponse.make_one(res)

    def describe_attack_statistics(
        self,
        res: "bs_td.DescribeAttackStatisticsResponseTypeDef",
    ) -> "dc_td.DescribeAttackStatisticsResponse":
        return dc_td.DescribeAttackStatisticsResponse.make_one(res)

    def describe_drt_access(
        self,
        res: "bs_td.DescribeDRTAccessResponseTypeDef",
    ) -> "dc_td.DescribeDRTAccessResponse":
        return dc_td.DescribeDRTAccessResponse.make_one(res)

    def describe_emergency_contact_settings(
        self,
        res: "bs_td.DescribeEmergencyContactSettingsResponseTypeDef",
    ) -> "dc_td.DescribeEmergencyContactSettingsResponse":
        return dc_td.DescribeEmergencyContactSettingsResponse.make_one(res)

    def describe_protection(
        self,
        res: "bs_td.DescribeProtectionResponseTypeDef",
    ) -> "dc_td.DescribeProtectionResponse":
        return dc_td.DescribeProtectionResponse.make_one(res)

    def describe_protection_group(
        self,
        res: "bs_td.DescribeProtectionGroupResponseTypeDef",
    ) -> "dc_td.DescribeProtectionGroupResponse":
        return dc_td.DescribeProtectionGroupResponse.make_one(res)

    def describe_subscription(
        self,
        res: "bs_td.DescribeSubscriptionResponseTypeDef",
    ) -> "dc_td.DescribeSubscriptionResponse":
        return dc_td.DescribeSubscriptionResponse.make_one(res)

    def get_subscription_state(
        self,
        res: "bs_td.GetSubscriptionStateResponseTypeDef",
    ) -> "dc_td.GetSubscriptionStateResponse":
        return dc_td.GetSubscriptionStateResponse.make_one(res)

    def list_attacks(
        self,
        res: "bs_td.ListAttacksResponseTypeDef",
    ) -> "dc_td.ListAttacksResponse":
        return dc_td.ListAttacksResponse.make_one(res)

    def list_protection_groups(
        self,
        res: "bs_td.ListProtectionGroupsResponseTypeDef",
    ) -> "dc_td.ListProtectionGroupsResponse":
        return dc_td.ListProtectionGroupsResponse.make_one(res)

    def list_protections(
        self,
        res: "bs_td.ListProtectionsResponseTypeDef",
    ) -> "dc_td.ListProtectionsResponse":
        return dc_td.ListProtectionsResponse.make_one(res)

    def list_resources_in_protection_group(
        self,
        res: "bs_td.ListResourcesInProtectionGroupResponseTypeDef",
    ) -> "dc_td.ListResourcesInProtectionGroupResponse":
        return dc_td.ListResourcesInProtectionGroupResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)


shield_caster = SHIELDCaster()
