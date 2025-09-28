# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ssm_quicksetup import type_defs as bs_td


class SSM_QUICKSETUPCaster:

    def create_configuration_manager(
        self,
        res: "bs_td.CreateConfigurationManagerOutputTypeDef",
    ) -> "dc_td.CreateConfigurationManagerOutput":
        return dc_td.CreateConfigurationManagerOutput.make_one(res)

    def delete_configuration_manager(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_configuration(
        self,
        res: "bs_td.GetConfigurationOutputTypeDef",
    ) -> "dc_td.GetConfigurationOutput":
        return dc_td.GetConfigurationOutput.make_one(res)

    def get_configuration_manager(
        self,
        res: "bs_td.GetConfigurationManagerOutputTypeDef",
    ) -> "dc_td.GetConfigurationManagerOutput":
        return dc_td.GetConfigurationManagerOutput.make_one(res)

    def get_service_settings(
        self,
        res: "bs_td.GetServiceSettingsOutputTypeDef",
    ) -> "dc_td.GetServiceSettingsOutput":
        return dc_td.GetServiceSettingsOutput.make_one(res)

    def list_configuration_managers(
        self,
        res: "bs_td.ListConfigurationManagersOutputTypeDef",
    ) -> "dc_td.ListConfigurationManagersOutput":
        return dc_td.ListConfigurationManagersOutput.make_one(res)

    def list_configurations(
        self,
        res: "bs_td.ListConfigurationsOutputTypeDef",
    ) -> "dc_td.ListConfigurationsOutput":
        return dc_td.ListConfigurationsOutput.make_one(res)

    def list_quick_setup_types(
        self,
        res: "bs_td.ListQuickSetupTypesOutputTypeDef",
    ) -> "dc_td.ListQuickSetupTypesOutput":
        return dc_td.ListQuickSetupTypesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_configuration_definition(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_configuration_manager(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_service_settings(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


ssm_quicksetup_caster = SSM_QUICKSETUPCaster()
