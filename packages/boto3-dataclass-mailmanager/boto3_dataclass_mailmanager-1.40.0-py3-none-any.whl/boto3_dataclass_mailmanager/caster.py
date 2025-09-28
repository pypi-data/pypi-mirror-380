# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mailmanager import type_defs as bs_td


class MAILMANAGERCaster:

    def create_addon_instance(
        self,
        res: "bs_td.CreateAddonInstanceResponseTypeDef",
    ) -> "dc_td.CreateAddonInstanceResponse":
        return dc_td.CreateAddonInstanceResponse.make_one(res)

    def create_addon_subscription(
        self,
        res: "bs_td.CreateAddonSubscriptionResponseTypeDef",
    ) -> "dc_td.CreateAddonSubscriptionResponse":
        return dc_td.CreateAddonSubscriptionResponse.make_one(res)

    def create_address_list(
        self,
        res: "bs_td.CreateAddressListResponseTypeDef",
    ) -> "dc_td.CreateAddressListResponse":
        return dc_td.CreateAddressListResponse.make_one(res)

    def create_address_list_import_job(
        self,
        res: "bs_td.CreateAddressListImportJobResponseTypeDef",
    ) -> "dc_td.CreateAddressListImportJobResponse":
        return dc_td.CreateAddressListImportJobResponse.make_one(res)

    def create_archive(
        self,
        res: "bs_td.CreateArchiveResponseTypeDef",
    ) -> "dc_td.CreateArchiveResponse":
        return dc_td.CreateArchiveResponse.make_one(res)

    def create_ingress_point(
        self,
        res: "bs_td.CreateIngressPointResponseTypeDef",
    ) -> "dc_td.CreateIngressPointResponse":
        return dc_td.CreateIngressPointResponse.make_one(res)

    def create_relay(
        self,
        res: "bs_td.CreateRelayResponseTypeDef",
    ) -> "dc_td.CreateRelayResponse":
        return dc_td.CreateRelayResponse.make_one(res)

    def create_rule_set(
        self,
        res: "bs_td.CreateRuleSetResponseTypeDef",
    ) -> "dc_td.CreateRuleSetResponse":
        return dc_td.CreateRuleSetResponse.make_one(res)

    def create_traffic_policy(
        self,
        res: "bs_td.CreateTrafficPolicyResponseTypeDef",
    ) -> "dc_td.CreateTrafficPolicyResponse":
        return dc_td.CreateTrafficPolicyResponse.make_one(res)

    def get_addon_instance(
        self,
        res: "bs_td.GetAddonInstanceResponseTypeDef",
    ) -> "dc_td.GetAddonInstanceResponse":
        return dc_td.GetAddonInstanceResponse.make_one(res)

    def get_addon_subscription(
        self,
        res: "bs_td.GetAddonSubscriptionResponseTypeDef",
    ) -> "dc_td.GetAddonSubscriptionResponse":
        return dc_td.GetAddonSubscriptionResponse.make_one(res)

    def get_address_list(
        self,
        res: "bs_td.GetAddressListResponseTypeDef",
    ) -> "dc_td.GetAddressListResponse":
        return dc_td.GetAddressListResponse.make_one(res)

    def get_address_list_import_job(
        self,
        res: "bs_td.GetAddressListImportJobResponseTypeDef",
    ) -> "dc_td.GetAddressListImportJobResponse":
        return dc_td.GetAddressListImportJobResponse.make_one(res)

    def get_archive(
        self,
        res: "bs_td.GetArchiveResponseTypeDef",
    ) -> "dc_td.GetArchiveResponse":
        return dc_td.GetArchiveResponse.make_one(res)

    def get_archive_export(
        self,
        res: "bs_td.GetArchiveExportResponseTypeDef",
    ) -> "dc_td.GetArchiveExportResponse":
        return dc_td.GetArchiveExportResponse.make_one(res)

    def get_archive_message(
        self,
        res: "bs_td.GetArchiveMessageResponseTypeDef",
    ) -> "dc_td.GetArchiveMessageResponse":
        return dc_td.GetArchiveMessageResponse.make_one(res)

    def get_archive_message_content(
        self,
        res: "bs_td.GetArchiveMessageContentResponseTypeDef",
    ) -> "dc_td.GetArchiveMessageContentResponse":
        return dc_td.GetArchiveMessageContentResponse.make_one(res)

    def get_archive_search(
        self,
        res: "bs_td.GetArchiveSearchResponseTypeDef",
    ) -> "dc_td.GetArchiveSearchResponse":
        return dc_td.GetArchiveSearchResponse.make_one(res)

    def get_archive_search_results(
        self,
        res: "bs_td.GetArchiveSearchResultsResponseTypeDef",
    ) -> "dc_td.GetArchiveSearchResultsResponse":
        return dc_td.GetArchiveSearchResultsResponse.make_one(res)

    def get_ingress_point(
        self,
        res: "bs_td.GetIngressPointResponseTypeDef",
    ) -> "dc_td.GetIngressPointResponse":
        return dc_td.GetIngressPointResponse.make_one(res)

    def get_member_of_address_list(
        self,
        res: "bs_td.GetMemberOfAddressListResponseTypeDef",
    ) -> "dc_td.GetMemberOfAddressListResponse":
        return dc_td.GetMemberOfAddressListResponse.make_one(res)

    def get_relay(
        self,
        res: "bs_td.GetRelayResponseTypeDef",
    ) -> "dc_td.GetRelayResponse":
        return dc_td.GetRelayResponse.make_one(res)

    def get_rule_set(
        self,
        res: "bs_td.GetRuleSetResponseTypeDef",
    ) -> "dc_td.GetRuleSetResponse":
        return dc_td.GetRuleSetResponse.make_one(res)

    def get_traffic_policy(
        self,
        res: "bs_td.GetTrafficPolicyResponseTypeDef",
    ) -> "dc_td.GetTrafficPolicyResponse":
        return dc_td.GetTrafficPolicyResponse.make_one(res)

    def list_addon_instances(
        self,
        res: "bs_td.ListAddonInstancesResponseTypeDef",
    ) -> "dc_td.ListAddonInstancesResponse":
        return dc_td.ListAddonInstancesResponse.make_one(res)

    def list_addon_subscriptions(
        self,
        res: "bs_td.ListAddonSubscriptionsResponseTypeDef",
    ) -> "dc_td.ListAddonSubscriptionsResponse":
        return dc_td.ListAddonSubscriptionsResponse.make_one(res)

    def list_address_list_import_jobs(
        self,
        res: "bs_td.ListAddressListImportJobsResponseTypeDef",
    ) -> "dc_td.ListAddressListImportJobsResponse":
        return dc_td.ListAddressListImportJobsResponse.make_one(res)

    def list_address_lists(
        self,
        res: "bs_td.ListAddressListsResponseTypeDef",
    ) -> "dc_td.ListAddressListsResponse":
        return dc_td.ListAddressListsResponse.make_one(res)

    def list_archive_exports(
        self,
        res: "bs_td.ListArchiveExportsResponseTypeDef",
    ) -> "dc_td.ListArchiveExportsResponse":
        return dc_td.ListArchiveExportsResponse.make_one(res)

    def list_archive_searches(
        self,
        res: "bs_td.ListArchiveSearchesResponseTypeDef",
    ) -> "dc_td.ListArchiveSearchesResponse":
        return dc_td.ListArchiveSearchesResponse.make_one(res)

    def list_archives(
        self,
        res: "bs_td.ListArchivesResponseTypeDef",
    ) -> "dc_td.ListArchivesResponse":
        return dc_td.ListArchivesResponse.make_one(res)

    def list_ingress_points(
        self,
        res: "bs_td.ListIngressPointsResponseTypeDef",
    ) -> "dc_td.ListIngressPointsResponse":
        return dc_td.ListIngressPointsResponse.make_one(res)

    def list_members_of_address_list(
        self,
        res: "bs_td.ListMembersOfAddressListResponseTypeDef",
    ) -> "dc_td.ListMembersOfAddressListResponse":
        return dc_td.ListMembersOfAddressListResponse.make_one(res)

    def list_relays(
        self,
        res: "bs_td.ListRelaysResponseTypeDef",
    ) -> "dc_td.ListRelaysResponse":
        return dc_td.ListRelaysResponse.make_one(res)

    def list_rule_sets(
        self,
        res: "bs_td.ListRuleSetsResponseTypeDef",
    ) -> "dc_td.ListRuleSetsResponse":
        return dc_td.ListRuleSetsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_traffic_policies(
        self,
        res: "bs_td.ListTrafficPoliciesResponseTypeDef",
    ) -> "dc_td.ListTrafficPoliciesResponse":
        return dc_td.ListTrafficPoliciesResponse.make_one(res)

    def start_archive_export(
        self,
        res: "bs_td.StartArchiveExportResponseTypeDef",
    ) -> "dc_td.StartArchiveExportResponse":
        return dc_td.StartArchiveExportResponse.make_one(res)

    def start_archive_search(
        self,
        res: "bs_td.StartArchiveSearchResponseTypeDef",
    ) -> "dc_td.StartArchiveSearchResponse":
        return dc_td.StartArchiveSearchResponse.make_one(res)


mailmanager_caster = MAILMANAGERCaster()
