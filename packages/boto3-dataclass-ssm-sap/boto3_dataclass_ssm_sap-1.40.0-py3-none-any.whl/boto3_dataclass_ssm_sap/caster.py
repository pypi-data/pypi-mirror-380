# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ssm_sap import type_defs as bs_td


class SSM_SAPCaster:

    def delete_resource_permission(
        self,
        res: "bs_td.DeleteResourcePermissionOutputTypeDef",
    ) -> "dc_td.DeleteResourcePermissionOutput":
        return dc_td.DeleteResourcePermissionOutput.make_one(res)

    def get_application(
        self,
        res: "bs_td.GetApplicationOutputTypeDef",
    ) -> "dc_td.GetApplicationOutput":
        return dc_td.GetApplicationOutput.make_one(res)

    def get_component(
        self,
        res: "bs_td.GetComponentOutputTypeDef",
    ) -> "dc_td.GetComponentOutput":
        return dc_td.GetComponentOutput.make_one(res)

    def get_configuration_check_operation(
        self,
        res: "bs_td.GetConfigurationCheckOperationOutputTypeDef",
    ) -> "dc_td.GetConfigurationCheckOperationOutput":
        return dc_td.GetConfigurationCheckOperationOutput.make_one(res)

    def get_database(
        self,
        res: "bs_td.GetDatabaseOutputTypeDef",
    ) -> "dc_td.GetDatabaseOutput":
        return dc_td.GetDatabaseOutput.make_one(res)

    def get_operation(
        self,
        res: "bs_td.GetOperationOutputTypeDef",
    ) -> "dc_td.GetOperationOutput":
        return dc_td.GetOperationOutput.make_one(res)

    def get_resource_permission(
        self,
        res: "bs_td.GetResourcePermissionOutputTypeDef",
    ) -> "dc_td.GetResourcePermissionOutput":
        return dc_td.GetResourcePermissionOutput.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsOutputTypeDef",
    ) -> "dc_td.ListApplicationsOutput":
        return dc_td.ListApplicationsOutput.make_one(res)

    def list_components(
        self,
        res: "bs_td.ListComponentsOutputTypeDef",
    ) -> "dc_td.ListComponentsOutput":
        return dc_td.ListComponentsOutput.make_one(res)

    def list_configuration_check_definitions(
        self,
        res: "bs_td.ListConfigurationCheckDefinitionsOutputTypeDef",
    ) -> "dc_td.ListConfigurationCheckDefinitionsOutput":
        return dc_td.ListConfigurationCheckDefinitionsOutput.make_one(res)

    def list_configuration_check_operations(
        self,
        res: "bs_td.ListConfigurationCheckOperationsOutputTypeDef",
    ) -> "dc_td.ListConfigurationCheckOperationsOutput":
        return dc_td.ListConfigurationCheckOperationsOutput.make_one(res)

    def list_databases(
        self,
        res: "bs_td.ListDatabasesOutputTypeDef",
    ) -> "dc_td.ListDatabasesOutput":
        return dc_td.ListDatabasesOutput.make_one(res)

    def list_operation_events(
        self,
        res: "bs_td.ListOperationEventsOutputTypeDef",
    ) -> "dc_td.ListOperationEventsOutput":
        return dc_td.ListOperationEventsOutput.make_one(res)

    def list_operations(
        self,
        res: "bs_td.ListOperationsOutputTypeDef",
    ) -> "dc_td.ListOperationsOutput":
        return dc_td.ListOperationsOutput.make_one(res)

    def list_sub_check_results(
        self,
        res: "bs_td.ListSubCheckResultsOutputTypeDef",
    ) -> "dc_td.ListSubCheckResultsOutput":
        return dc_td.ListSubCheckResultsOutput.make_one(res)

    def list_sub_check_rule_results(
        self,
        res: "bs_td.ListSubCheckRuleResultsOutputTypeDef",
    ) -> "dc_td.ListSubCheckRuleResultsOutput":
        return dc_td.ListSubCheckRuleResultsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_resource_permission(
        self,
        res: "bs_td.PutResourcePermissionOutputTypeDef",
    ) -> "dc_td.PutResourcePermissionOutput":
        return dc_td.PutResourcePermissionOutput.make_one(res)

    def register_application(
        self,
        res: "bs_td.RegisterApplicationOutputTypeDef",
    ) -> "dc_td.RegisterApplicationOutput":
        return dc_td.RegisterApplicationOutput.make_one(res)

    def start_application(
        self,
        res: "bs_td.StartApplicationOutputTypeDef",
    ) -> "dc_td.StartApplicationOutput":
        return dc_td.StartApplicationOutput.make_one(res)

    def start_application_refresh(
        self,
        res: "bs_td.StartApplicationRefreshOutputTypeDef",
    ) -> "dc_td.StartApplicationRefreshOutput":
        return dc_td.StartApplicationRefreshOutput.make_one(res)

    def start_configuration_checks(
        self,
        res: "bs_td.StartConfigurationChecksOutputTypeDef",
    ) -> "dc_td.StartConfigurationChecksOutput":
        return dc_td.StartConfigurationChecksOutput.make_one(res)

    def stop_application(
        self,
        res: "bs_td.StopApplicationOutputTypeDef",
    ) -> "dc_td.StopApplicationOutput":
        return dc_td.StopApplicationOutput.make_one(res)

    def update_application_settings(
        self,
        res: "bs_td.UpdateApplicationSettingsOutputTypeDef",
    ) -> "dc_td.UpdateApplicationSettingsOutput":
        return dc_td.UpdateApplicationSettingsOutput.make_one(res)


ssm_sap_caster = SSM_SAPCaster()
