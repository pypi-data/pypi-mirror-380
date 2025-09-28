# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_support_app import type_defs as bs_td


class SUPPORT_APPCaster:

    def get_account_alias(
        self,
        res: "bs_td.GetAccountAliasResultTypeDef",
    ) -> "dc_td.GetAccountAliasResult":
        return dc_td.GetAccountAliasResult.make_one(res)

    def list_slack_channel_configurations(
        self,
        res: "bs_td.ListSlackChannelConfigurationsResultTypeDef",
    ) -> "dc_td.ListSlackChannelConfigurationsResult":
        return dc_td.ListSlackChannelConfigurationsResult.make_one(res)

    def list_slack_workspace_configurations(
        self,
        res: "bs_td.ListSlackWorkspaceConfigurationsResultTypeDef",
    ) -> "dc_td.ListSlackWorkspaceConfigurationsResult":
        return dc_td.ListSlackWorkspaceConfigurationsResult.make_one(res)

    def register_slack_workspace_for_organization(
        self,
        res: "bs_td.RegisterSlackWorkspaceForOrganizationResultTypeDef",
    ) -> "dc_td.RegisterSlackWorkspaceForOrganizationResult":
        return dc_td.RegisterSlackWorkspaceForOrganizationResult.make_one(res)

    def update_slack_channel_configuration(
        self,
        res: "bs_td.UpdateSlackChannelConfigurationResultTypeDef",
    ) -> "dc_td.UpdateSlackChannelConfigurationResult":
        return dc_td.UpdateSlackChannelConfigurationResult.make_one(res)


support_app_caster = SUPPORT_APPCaster()
