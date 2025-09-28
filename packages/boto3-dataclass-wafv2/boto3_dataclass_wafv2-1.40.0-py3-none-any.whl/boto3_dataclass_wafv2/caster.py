# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_wafv2 import type_defs as bs_td


class WAFV2Caster:

    def check_capacity(
        self,
        res: "bs_td.CheckCapacityResponseTypeDef",
    ) -> "dc_td.CheckCapacityResponse":
        return dc_td.CheckCapacityResponse.make_one(res)

    def create_api_key(
        self,
        res: "bs_td.CreateAPIKeyResponseTypeDef",
    ) -> "dc_td.CreateAPIKeyResponse":
        return dc_td.CreateAPIKeyResponse.make_one(res)

    def create_ip_set(
        self,
        res: "bs_td.CreateIPSetResponseTypeDef",
    ) -> "dc_td.CreateIPSetResponse":
        return dc_td.CreateIPSetResponse.make_one(res)

    def create_regex_pattern_set(
        self,
        res: "bs_td.CreateRegexPatternSetResponseTypeDef",
    ) -> "dc_td.CreateRegexPatternSetResponse":
        return dc_td.CreateRegexPatternSetResponse.make_one(res)

    def create_rule_group(
        self,
        res: "bs_td.CreateRuleGroupResponseTypeDef",
    ) -> "dc_td.CreateRuleGroupResponse":
        return dc_td.CreateRuleGroupResponse.make_one(res)

    def create_web_acl(
        self,
        res: "bs_td.CreateWebACLResponseTypeDef",
    ) -> "dc_td.CreateWebACLResponse":
        return dc_td.CreateWebACLResponse.make_one(res)

    def delete_firewall_manager_rule_groups(
        self,
        res: "bs_td.DeleteFirewallManagerRuleGroupsResponseTypeDef",
    ) -> "dc_td.DeleteFirewallManagerRuleGroupsResponse":
        return dc_td.DeleteFirewallManagerRuleGroupsResponse.make_one(res)

    def describe_all_managed_products(
        self,
        res: "bs_td.DescribeAllManagedProductsResponseTypeDef",
    ) -> "dc_td.DescribeAllManagedProductsResponse":
        return dc_td.DescribeAllManagedProductsResponse.make_one(res)

    def describe_managed_products_by_vendor(
        self,
        res: "bs_td.DescribeManagedProductsByVendorResponseTypeDef",
    ) -> "dc_td.DescribeManagedProductsByVendorResponse":
        return dc_td.DescribeManagedProductsByVendorResponse.make_one(res)

    def describe_managed_rule_group(
        self,
        res: "bs_td.DescribeManagedRuleGroupResponseTypeDef",
    ) -> "dc_td.DescribeManagedRuleGroupResponse":
        return dc_td.DescribeManagedRuleGroupResponse.make_one(res)

    def generate_mobile_sdk_release_url(
        self,
        res: "bs_td.GenerateMobileSdkReleaseUrlResponseTypeDef",
    ) -> "dc_td.GenerateMobileSdkReleaseUrlResponse":
        return dc_td.GenerateMobileSdkReleaseUrlResponse.make_one(res)

    def get_decrypted_api_key(
        self,
        res: "bs_td.GetDecryptedAPIKeyResponseTypeDef",
    ) -> "dc_td.GetDecryptedAPIKeyResponse":
        return dc_td.GetDecryptedAPIKeyResponse.make_one(res)

    def get_ip_set(
        self,
        res: "bs_td.GetIPSetResponseTypeDef",
    ) -> "dc_td.GetIPSetResponse":
        return dc_td.GetIPSetResponse.make_one(res)

    def get_logging_configuration(
        self,
        res: "bs_td.GetLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.GetLoggingConfigurationResponse":
        return dc_td.GetLoggingConfigurationResponse.make_one(res)

    def get_managed_rule_set(
        self,
        res: "bs_td.GetManagedRuleSetResponseTypeDef",
    ) -> "dc_td.GetManagedRuleSetResponse":
        return dc_td.GetManagedRuleSetResponse.make_one(res)

    def get_mobile_sdk_release(
        self,
        res: "bs_td.GetMobileSdkReleaseResponseTypeDef",
    ) -> "dc_td.GetMobileSdkReleaseResponse":
        return dc_td.GetMobileSdkReleaseResponse.make_one(res)

    def get_permission_policy(
        self,
        res: "bs_td.GetPermissionPolicyResponseTypeDef",
    ) -> "dc_td.GetPermissionPolicyResponse":
        return dc_td.GetPermissionPolicyResponse.make_one(res)

    def get_rate_based_statement_managed_keys(
        self,
        res: "bs_td.GetRateBasedStatementManagedKeysResponseTypeDef",
    ) -> "dc_td.GetRateBasedStatementManagedKeysResponse":
        return dc_td.GetRateBasedStatementManagedKeysResponse.make_one(res)

    def get_regex_pattern_set(
        self,
        res: "bs_td.GetRegexPatternSetResponseTypeDef",
    ) -> "dc_td.GetRegexPatternSetResponse":
        return dc_td.GetRegexPatternSetResponse.make_one(res)

    def get_rule_group(
        self,
        res: "bs_td.GetRuleGroupResponseTypeDef",
    ) -> "dc_td.GetRuleGroupResponse":
        return dc_td.GetRuleGroupResponse.make_one(res)

    def get_sampled_requests(
        self,
        res: "bs_td.GetSampledRequestsResponseTypeDef",
    ) -> "dc_td.GetSampledRequestsResponse":
        return dc_td.GetSampledRequestsResponse.make_one(res)

    def get_web_acl(
        self,
        res: "bs_td.GetWebACLResponseTypeDef",
    ) -> "dc_td.GetWebACLResponse":
        return dc_td.GetWebACLResponse.make_one(res)

    def get_web_acl_for_resource(
        self,
        res: "bs_td.GetWebACLForResourceResponseTypeDef",
    ) -> "dc_td.GetWebACLForResourceResponse":
        return dc_td.GetWebACLForResourceResponse.make_one(res)

    def list_api_keys(
        self,
        res: "bs_td.ListAPIKeysResponseTypeDef",
    ) -> "dc_td.ListAPIKeysResponse":
        return dc_td.ListAPIKeysResponse.make_one(res)

    def list_available_managed_rule_group_versions(
        self,
        res: "bs_td.ListAvailableManagedRuleGroupVersionsResponseTypeDef",
    ) -> "dc_td.ListAvailableManagedRuleGroupVersionsResponse":
        return dc_td.ListAvailableManagedRuleGroupVersionsResponse.make_one(res)

    def list_available_managed_rule_groups(
        self,
        res: "bs_td.ListAvailableManagedRuleGroupsResponseTypeDef",
    ) -> "dc_td.ListAvailableManagedRuleGroupsResponse":
        return dc_td.ListAvailableManagedRuleGroupsResponse.make_one(res)

    def list_ip_sets(
        self,
        res: "bs_td.ListIPSetsResponseTypeDef",
    ) -> "dc_td.ListIPSetsResponse":
        return dc_td.ListIPSetsResponse.make_one(res)

    def list_logging_configurations(
        self,
        res: "bs_td.ListLoggingConfigurationsResponseTypeDef",
    ) -> "dc_td.ListLoggingConfigurationsResponse":
        return dc_td.ListLoggingConfigurationsResponse.make_one(res)

    def list_managed_rule_sets(
        self,
        res: "bs_td.ListManagedRuleSetsResponseTypeDef",
    ) -> "dc_td.ListManagedRuleSetsResponse":
        return dc_td.ListManagedRuleSetsResponse.make_one(res)

    def list_mobile_sdk_releases(
        self,
        res: "bs_td.ListMobileSdkReleasesResponseTypeDef",
    ) -> "dc_td.ListMobileSdkReleasesResponse":
        return dc_td.ListMobileSdkReleasesResponse.make_one(res)

    def list_regex_pattern_sets(
        self,
        res: "bs_td.ListRegexPatternSetsResponseTypeDef",
    ) -> "dc_td.ListRegexPatternSetsResponse":
        return dc_td.ListRegexPatternSetsResponse.make_one(res)

    def list_resources_for_web_acl(
        self,
        res: "bs_td.ListResourcesForWebACLResponseTypeDef",
    ) -> "dc_td.ListResourcesForWebACLResponse":
        return dc_td.ListResourcesForWebACLResponse.make_one(res)

    def list_rule_groups(
        self,
        res: "bs_td.ListRuleGroupsResponseTypeDef",
    ) -> "dc_td.ListRuleGroupsResponse":
        return dc_td.ListRuleGroupsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_web_acls(
        self,
        res: "bs_td.ListWebACLsResponseTypeDef",
    ) -> "dc_td.ListWebACLsResponse":
        return dc_td.ListWebACLsResponse.make_one(res)

    def put_logging_configuration(
        self,
        res: "bs_td.PutLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.PutLoggingConfigurationResponse":
        return dc_td.PutLoggingConfigurationResponse.make_one(res)

    def put_managed_rule_set_versions(
        self,
        res: "bs_td.PutManagedRuleSetVersionsResponseTypeDef",
    ) -> "dc_td.PutManagedRuleSetVersionsResponse":
        return dc_td.PutManagedRuleSetVersionsResponse.make_one(res)

    def update_ip_set(
        self,
        res: "bs_td.UpdateIPSetResponseTypeDef",
    ) -> "dc_td.UpdateIPSetResponse":
        return dc_td.UpdateIPSetResponse.make_one(res)

    def update_managed_rule_set_version_expiry_date(
        self,
        res: "bs_td.UpdateManagedRuleSetVersionExpiryDateResponseTypeDef",
    ) -> "dc_td.UpdateManagedRuleSetVersionExpiryDateResponse":
        return dc_td.UpdateManagedRuleSetVersionExpiryDateResponse.make_one(res)

    def update_regex_pattern_set(
        self,
        res: "bs_td.UpdateRegexPatternSetResponseTypeDef",
    ) -> "dc_td.UpdateRegexPatternSetResponse":
        return dc_td.UpdateRegexPatternSetResponse.make_one(res)

    def update_rule_group(
        self,
        res: "bs_td.UpdateRuleGroupResponseTypeDef",
    ) -> "dc_td.UpdateRuleGroupResponse":
        return dc_td.UpdateRuleGroupResponse.make_one(res)

    def update_web_acl(
        self,
        res: "bs_td.UpdateWebACLResponseTypeDef",
    ) -> "dc_td.UpdateWebACLResponse":
        return dc_td.UpdateWebACLResponse.make_one(res)


wafv2_caster = WAFV2Caster()
