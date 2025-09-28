# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sms import type_defs as bs_td


class SMSCaster:

    def create_app(
        self,
        res: "bs_td.CreateAppResponseTypeDef",
    ) -> "dc_td.CreateAppResponse":
        return dc_td.CreateAppResponse.make_one(res)

    def create_replication_job(
        self,
        res: "bs_td.CreateReplicationJobResponseTypeDef",
    ) -> "dc_td.CreateReplicationJobResponse":
        return dc_td.CreateReplicationJobResponse.make_one(res)

    def generate_change_set(
        self,
        res: "bs_td.GenerateChangeSetResponseTypeDef",
    ) -> "dc_td.GenerateChangeSetResponse":
        return dc_td.GenerateChangeSetResponse.make_one(res)

    def generate_template(
        self,
        res: "bs_td.GenerateTemplateResponseTypeDef",
    ) -> "dc_td.GenerateTemplateResponse":
        return dc_td.GenerateTemplateResponse.make_one(res)

    def get_app(
        self,
        res: "bs_td.GetAppResponseTypeDef",
    ) -> "dc_td.GetAppResponse":
        return dc_td.GetAppResponse.make_one(res)

    def get_app_launch_configuration(
        self,
        res: "bs_td.GetAppLaunchConfigurationResponseTypeDef",
    ) -> "dc_td.GetAppLaunchConfigurationResponse":
        return dc_td.GetAppLaunchConfigurationResponse.make_one(res)

    def get_app_replication_configuration(
        self,
        res: "bs_td.GetAppReplicationConfigurationResponseTypeDef",
    ) -> "dc_td.GetAppReplicationConfigurationResponse":
        return dc_td.GetAppReplicationConfigurationResponse.make_one(res)

    def get_app_validation_configuration(
        self,
        res: "bs_td.GetAppValidationConfigurationResponseTypeDef",
    ) -> "dc_td.GetAppValidationConfigurationResponse":
        return dc_td.GetAppValidationConfigurationResponse.make_one(res)

    def get_app_validation_output(
        self,
        res: "bs_td.GetAppValidationOutputResponseTypeDef",
    ) -> "dc_td.GetAppValidationOutputResponse":
        return dc_td.GetAppValidationOutputResponse.make_one(res)

    def get_connectors(
        self,
        res: "bs_td.GetConnectorsResponseTypeDef",
    ) -> "dc_td.GetConnectorsResponse":
        return dc_td.GetConnectorsResponse.make_one(res)

    def get_replication_jobs(
        self,
        res: "bs_td.GetReplicationJobsResponseTypeDef",
    ) -> "dc_td.GetReplicationJobsResponse":
        return dc_td.GetReplicationJobsResponse.make_one(res)

    def get_replication_runs(
        self,
        res: "bs_td.GetReplicationRunsResponseTypeDef",
    ) -> "dc_td.GetReplicationRunsResponse":
        return dc_td.GetReplicationRunsResponse.make_one(res)

    def get_servers(
        self,
        res: "bs_td.GetServersResponseTypeDef",
    ) -> "dc_td.GetServersResponse":
        return dc_td.GetServersResponse.make_one(res)

    def list_apps(
        self,
        res: "bs_td.ListAppsResponseTypeDef",
    ) -> "dc_td.ListAppsResponse":
        return dc_td.ListAppsResponse.make_one(res)

    def start_on_demand_replication_run(
        self,
        res: "bs_td.StartOnDemandReplicationRunResponseTypeDef",
    ) -> "dc_td.StartOnDemandReplicationRunResponse":
        return dc_td.StartOnDemandReplicationRunResponse.make_one(res)

    def update_app(
        self,
        res: "bs_td.UpdateAppResponseTypeDef",
    ) -> "dc_td.UpdateAppResponse":
        return dc_td.UpdateAppResponse.make_one(res)


sms_caster = SMSCaster()
