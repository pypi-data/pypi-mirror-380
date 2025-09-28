# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_waf import type_defs as bs_td


class WAFCaster:

    def create_byte_match_set(
        self,
        res: "bs_td.CreateByteMatchSetResponseTypeDef",
    ) -> "dc_td.CreateByteMatchSetResponse":
        return dc_td.CreateByteMatchSetResponse.make_one(res)

    def create_geo_match_set(
        self,
        res: "bs_td.CreateGeoMatchSetResponseTypeDef",
    ) -> "dc_td.CreateGeoMatchSetResponse":
        return dc_td.CreateGeoMatchSetResponse.make_one(res)

    def create_ip_set(
        self,
        res: "bs_td.CreateIPSetResponseTypeDef",
    ) -> "dc_td.CreateIPSetResponse":
        return dc_td.CreateIPSetResponse.make_one(res)

    def create_rate_based_rule(
        self,
        res: "bs_td.CreateRateBasedRuleResponseTypeDef",
    ) -> "dc_td.CreateRateBasedRuleResponse":
        return dc_td.CreateRateBasedRuleResponse.make_one(res)

    def create_regex_match_set(
        self,
        res: "bs_td.CreateRegexMatchSetResponseTypeDef",
    ) -> "dc_td.CreateRegexMatchSetResponse":
        return dc_td.CreateRegexMatchSetResponse.make_one(res)

    def create_regex_pattern_set(
        self,
        res: "bs_td.CreateRegexPatternSetResponseTypeDef",
    ) -> "dc_td.CreateRegexPatternSetResponse":
        return dc_td.CreateRegexPatternSetResponse.make_one(res)

    def create_rule(
        self,
        res: "bs_td.CreateRuleResponseTypeDef",
    ) -> "dc_td.CreateRuleResponse":
        return dc_td.CreateRuleResponse.make_one(res)

    def create_rule_group(
        self,
        res: "bs_td.CreateRuleGroupResponseTypeDef",
    ) -> "dc_td.CreateRuleGroupResponse":
        return dc_td.CreateRuleGroupResponse.make_one(res)

    def create_size_constraint_set(
        self,
        res: "bs_td.CreateSizeConstraintSetResponseTypeDef",
    ) -> "dc_td.CreateSizeConstraintSetResponse":
        return dc_td.CreateSizeConstraintSetResponse.make_one(res)

    def create_sql_injection_match_set(
        self,
        res: "bs_td.CreateSqlInjectionMatchSetResponseTypeDef",
    ) -> "dc_td.CreateSqlInjectionMatchSetResponse":
        return dc_td.CreateSqlInjectionMatchSetResponse.make_one(res)

    def create_web_acl(
        self,
        res: "bs_td.CreateWebACLResponseTypeDef",
    ) -> "dc_td.CreateWebACLResponse":
        return dc_td.CreateWebACLResponse.make_one(res)

    def create_web_acl_migration_stack(
        self,
        res: "bs_td.CreateWebACLMigrationStackResponseTypeDef",
    ) -> "dc_td.CreateWebACLMigrationStackResponse":
        return dc_td.CreateWebACLMigrationStackResponse.make_one(res)

    def create_xss_match_set(
        self,
        res: "bs_td.CreateXssMatchSetResponseTypeDef",
    ) -> "dc_td.CreateXssMatchSetResponse":
        return dc_td.CreateXssMatchSetResponse.make_one(res)

    def delete_byte_match_set(
        self,
        res: "bs_td.DeleteByteMatchSetResponseTypeDef",
    ) -> "dc_td.DeleteByteMatchSetResponse":
        return dc_td.DeleteByteMatchSetResponse.make_one(res)

    def delete_geo_match_set(
        self,
        res: "bs_td.DeleteGeoMatchSetResponseTypeDef",
    ) -> "dc_td.DeleteGeoMatchSetResponse":
        return dc_td.DeleteGeoMatchSetResponse.make_one(res)

    def delete_ip_set(
        self,
        res: "bs_td.DeleteIPSetResponseTypeDef",
    ) -> "dc_td.DeleteIPSetResponse":
        return dc_td.DeleteIPSetResponse.make_one(res)

    def delete_rate_based_rule(
        self,
        res: "bs_td.DeleteRateBasedRuleResponseTypeDef",
    ) -> "dc_td.DeleteRateBasedRuleResponse":
        return dc_td.DeleteRateBasedRuleResponse.make_one(res)

    def delete_regex_match_set(
        self,
        res: "bs_td.DeleteRegexMatchSetResponseTypeDef",
    ) -> "dc_td.DeleteRegexMatchSetResponse":
        return dc_td.DeleteRegexMatchSetResponse.make_one(res)

    def delete_regex_pattern_set(
        self,
        res: "bs_td.DeleteRegexPatternSetResponseTypeDef",
    ) -> "dc_td.DeleteRegexPatternSetResponse":
        return dc_td.DeleteRegexPatternSetResponse.make_one(res)

    def delete_rule(
        self,
        res: "bs_td.DeleteRuleResponseTypeDef",
    ) -> "dc_td.DeleteRuleResponse":
        return dc_td.DeleteRuleResponse.make_one(res)

    def delete_rule_group(
        self,
        res: "bs_td.DeleteRuleGroupResponseTypeDef",
    ) -> "dc_td.DeleteRuleGroupResponse":
        return dc_td.DeleteRuleGroupResponse.make_one(res)

    def delete_size_constraint_set(
        self,
        res: "bs_td.DeleteSizeConstraintSetResponseTypeDef",
    ) -> "dc_td.DeleteSizeConstraintSetResponse":
        return dc_td.DeleteSizeConstraintSetResponse.make_one(res)

    def delete_sql_injection_match_set(
        self,
        res: "bs_td.DeleteSqlInjectionMatchSetResponseTypeDef",
    ) -> "dc_td.DeleteSqlInjectionMatchSetResponse":
        return dc_td.DeleteSqlInjectionMatchSetResponse.make_one(res)

    def delete_web_acl(
        self,
        res: "bs_td.DeleteWebACLResponseTypeDef",
    ) -> "dc_td.DeleteWebACLResponse":
        return dc_td.DeleteWebACLResponse.make_one(res)

    def delete_xss_match_set(
        self,
        res: "bs_td.DeleteXssMatchSetResponseTypeDef",
    ) -> "dc_td.DeleteXssMatchSetResponse":
        return dc_td.DeleteXssMatchSetResponse.make_one(res)

    def get_byte_match_set(
        self,
        res: "bs_td.GetByteMatchSetResponseTypeDef",
    ) -> "dc_td.GetByteMatchSetResponse":
        return dc_td.GetByteMatchSetResponse.make_one(res)

    def get_change_token(
        self,
        res: "bs_td.GetChangeTokenResponseTypeDef",
    ) -> "dc_td.GetChangeTokenResponse":
        return dc_td.GetChangeTokenResponse.make_one(res)

    def get_change_token_status(
        self,
        res: "bs_td.GetChangeTokenStatusResponseTypeDef",
    ) -> "dc_td.GetChangeTokenStatusResponse":
        return dc_td.GetChangeTokenStatusResponse.make_one(res)

    def get_geo_match_set(
        self,
        res: "bs_td.GetGeoMatchSetResponseTypeDef",
    ) -> "dc_td.GetGeoMatchSetResponse":
        return dc_td.GetGeoMatchSetResponse.make_one(res)

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

    def get_permission_policy(
        self,
        res: "bs_td.GetPermissionPolicyResponseTypeDef",
    ) -> "dc_td.GetPermissionPolicyResponse":
        return dc_td.GetPermissionPolicyResponse.make_one(res)

    def get_rate_based_rule(
        self,
        res: "bs_td.GetRateBasedRuleResponseTypeDef",
    ) -> "dc_td.GetRateBasedRuleResponse":
        return dc_td.GetRateBasedRuleResponse.make_one(res)

    def get_rate_based_rule_managed_keys(
        self,
        res: "bs_td.GetRateBasedRuleManagedKeysResponseTypeDef",
    ) -> "dc_td.GetRateBasedRuleManagedKeysResponse":
        return dc_td.GetRateBasedRuleManagedKeysResponse.make_one(res)

    def get_regex_match_set(
        self,
        res: "bs_td.GetRegexMatchSetResponseTypeDef",
    ) -> "dc_td.GetRegexMatchSetResponse":
        return dc_td.GetRegexMatchSetResponse.make_one(res)

    def get_regex_pattern_set(
        self,
        res: "bs_td.GetRegexPatternSetResponseTypeDef",
    ) -> "dc_td.GetRegexPatternSetResponse":
        return dc_td.GetRegexPatternSetResponse.make_one(res)

    def get_rule(
        self,
        res: "bs_td.GetRuleResponseTypeDef",
    ) -> "dc_td.GetRuleResponse":
        return dc_td.GetRuleResponse.make_one(res)

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

    def get_size_constraint_set(
        self,
        res: "bs_td.GetSizeConstraintSetResponseTypeDef",
    ) -> "dc_td.GetSizeConstraintSetResponse":
        return dc_td.GetSizeConstraintSetResponse.make_one(res)

    def get_sql_injection_match_set(
        self,
        res: "bs_td.GetSqlInjectionMatchSetResponseTypeDef",
    ) -> "dc_td.GetSqlInjectionMatchSetResponse":
        return dc_td.GetSqlInjectionMatchSetResponse.make_one(res)

    def get_web_acl(
        self,
        res: "bs_td.GetWebACLResponseTypeDef",
    ) -> "dc_td.GetWebACLResponse":
        return dc_td.GetWebACLResponse.make_one(res)

    def get_xss_match_set(
        self,
        res: "bs_td.GetXssMatchSetResponseTypeDef",
    ) -> "dc_td.GetXssMatchSetResponse":
        return dc_td.GetXssMatchSetResponse.make_one(res)

    def list_activated_rules_in_rule_group(
        self,
        res: "bs_td.ListActivatedRulesInRuleGroupResponseTypeDef",
    ) -> "dc_td.ListActivatedRulesInRuleGroupResponse":
        return dc_td.ListActivatedRulesInRuleGroupResponse.make_one(res)

    def list_byte_match_sets(
        self,
        res: "bs_td.ListByteMatchSetsResponseTypeDef",
    ) -> "dc_td.ListByteMatchSetsResponse":
        return dc_td.ListByteMatchSetsResponse.make_one(res)

    def list_geo_match_sets(
        self,
        res: "bs_td.ListGeoMatchSetsResponseTypeDef",
    ) -> "dc_td.ListGeoMatchSetsResponse":
        return dc_td.ListGeoMatchSetsResponse.make_one(res)

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

    def list_rate_based_rules(
        self,
        res: "bs_td.ListRateBasedRulesResponseTypeDef",
    ) -> "dc_td.ListRateBasedRulesResponse":
        return dc_td.ListRateBasedRulesResponse.make_one(res)

    def list_regex_match_sets(
        self,
        res: "bs_td.ListRegexMatchSetsResponseTypeDef",
    ) -> "dc_td.ListRegexMatchSetsResponse":
        return dc_td.ListRegexMatchSetsResponse.make_one(res)

    def list_regex_pattern_sets(
        self,
        res: "bs_td.ListRegexPatternSetsResponseTypeDef",
    ) -> "dc_td.ListRegexPatternSetsResponse":
        return dc_td.ListRegexPatternSetsResponse.make_one(res)

    def list_rule_groups(
        self,
        res: "bs_td.ListRuleGroupsResponseTypeDef",
    ) -> "dc_td.ListRuleGroupsResponse":
        return dc_td.ListRuleGroupsResponse.make_one(res)

    def list_rules(
        self,
        res: "bs_td.ListRulesResponseTypeDef",
    ) -> "dc_td.ListRulesResponse":
        return dc_td.ListRulesResponse.make_one(res)

    def list_size_constraint_sets(
        self,
        res: "bs_td.ListSizeConstraintSetsResponseTypeDef",
    ) -> "dc_td.ListSizeConstraintSetsResponse":
        return dc_td.ListSizeConstraintSetsResponse.make_one(res)

    def list_sql_injection_match_sets(
        self,
        res: "bs_td.ListSqlInjectionMatchSetsResponseTypeDef",
    ) -> "dc_td.ListSqlInjectionMatchSetsResponse":
        return dc_td.ListSqlInjectionMatchSetsResponse.make_one(res)

    def list_subscribed_rule_groups(
        self,
        res: "bs_td.ListSubscribedRuleGroupsResponseTypeDef",
    ) -> "dc_td.ListSubscribedRuleGroupsResponse":
        return dc_td.ListSubscribedRuleGroupsResponse.make_one(res)

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

    def list_xss_match_sets(
        self,
        res: "bs_td.ListXssMatchSetsResponseTypeDef",
    ) -> "dc_td.ListXssMatchSetsResponse":
        return dc_td.ListXssMatchSetsResponse.make_one(res)

    def put_logging_configuration(
        self,
        res: "bs_td.PutLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.PutLoggingConfigurationResponse":
        return dc_td.PutLoggingConfigurationResponse.make_one(res)

    def update_byte_match_set(
        self,
        res: "bs_td.UpdateByteMatchSetResponseTypeDef",
    ) -> "dc_td.UpdateByteMatchSetResponse":
        return dc_td.UpdateByteMatchSetResponse.make_one(res)

    def update_geo_match_set(
        self,
        res: "bs_td.UpdateGeoMatchSetResponseTypeDef",
    ) -> "dc_td.UpdateGeoMatchSetResponse":
        return dc_td.UpdateGeoMatchSetResponse.make_one(res)

    def update_ip_set(
        self,
        res: "bs_td.UpdateIPSetResponseTypeDef",
    ) -> "dc_td.UpdateIPSetResponse":
        return dc_td.UpdateIPSetResponse.make_one(res)

    def update_rate_based_rule(
        self,
        res: "bs_td.UpdateRateBasedRuleResponseTypeDef",
    ) -> "dc_td.UpdateRateBasedRuleResponse":
        return dc_td.UpdateRateBasedRuleResponse.make_one(res)

    def update_regex_match_set(
        self,
        res: "bs_td.UpdateRegexMatchSetResponseTypeDef",
    ) -> "dc_td.UpdateRegexMatchSetResponse":
        return dc_td.UpdateRegexMatchSetResponse.make_one(res)

    def update_regex_pattern_set(
        self,
        res: "bs_td.UpdateRegexPatternSetResponseTypeDef",
    ) -> "dc_td.UpdateRegexPatternSetResponse":
        return dc_td.UpdateRegexPatternSetResponse.make_one(res)

    def update_rule(
        self,
        res: "bs_td.UpdateRuleResponseTypeDef",
    ) -> "dc_td.UpdateRuleResponse":
        return dc_td.UpdateRuleResponse.make_one(res)

    def update_rule_group(
        self,
        res: "bs_td.UpdateRuleGroupResponseTypeDef",
    ) -> "dc_td.UpdateRuleGroupResponse":
        return dc_td.UpdateRuleGroupResponse.make_one(res)

    def update_size_constraint_set(
        self,
        res: "bs_td.UpdateSizeConstraintSetResponseTypeDef",
    ) -> "dc_td.UpdateSizeConstraintSetResponse":
        return dc_td.UpdateSizeConstraintSetResponse.make_one(res)

    def update_sql_injection_match_set(
        self,
        res: "bs_td.UpdateSqlInjectionMatchSetResponseTypeDef",
    ) -> "dc_td.UpdateSqlInjectionMatchSetResponse":
        return dc_td.UpdateSqlInjectionMatchSetResponse.make_one(res)

    def update_web_acl(
        self,
        res: "bs_td.UpdateWebACLResponseTypeDef",
    ) -> "dc_td.UpdateWebACLResponse":
        return dc_td.UpdateWebACLResponse.make_one(res)

    def update_xss_match_set(
        self,
        res: "bs_td.UpdateXssMatchSetResponseTypeDef",
    ) -> "dc_td.UpdateXssMatchSetResponse":
        return dc_td.UpdateXssMatchSetResponse.make_one(res)


waf_caster = WAFCaster()
