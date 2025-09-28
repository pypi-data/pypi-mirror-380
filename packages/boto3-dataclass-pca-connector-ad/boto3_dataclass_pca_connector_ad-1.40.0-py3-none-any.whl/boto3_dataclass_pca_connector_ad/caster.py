# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pca_connector_ad import type_defs as bs_td


class PCA_CONNECTOR_ADCaster:

    def create_connector(
        self,
        res: "bs_td.CreateConnectorResponseTypeDef",
    ) -> "dc_td.CreateConnectorResponse":
        return dc_td.CreateConnectorResponse.make_one(res)

    def create_directory_registration(
        self,
        res: "bs_td.CreateDirectoryRegistrationResponseTypeDef",
    ) -> "dc_td.CreateDirectoryRegistrationResponse":
        return dc_td.CreateDirectoryRegistrationResponse.make_one(res)

    def create_service_principal_name(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_template(
        self,
        res: "bs_td.CreateTemplateResponseTypeDef",
    ) -> "dc_td.CreateTemplateResponse":
        return dc_td.CreateTemplateResponse.make_one(res)

    def create_template_group_access_control_entry(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_connector(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_directory_registration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_service_principal_name(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_template_group_access_control_entry(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_connector(
        self,
        res: "bs_td.GetConnectorResponseTypeDef",
    ) -> "dc_td.GetConnectorResponse":
        return dc_td.GetConnectorResponse.make_one(res)

    def get_directory_registration(
        self,
        res: "bs_td.GetDirectoryRegistrationResponseTypeDef",
    ) -> "dc_td.GetDirectoryRegistrationResponse":
        return dc_td.GetDirectoryRegistrationResponse.make_one(res)

    def get_service_principal_name(
        self,
        res: "bs_td.GetServicePrincipalNameResponseTypeDef",
    ) -> "dc_td.GetServicePrincipalNameResponse":
        return dc_td.GetServicePrincipalNameResponse.make_one(res)

    def get_template(
        self,
        res: "bs_td.GetTemplateResponseTypeDef",
    ) -> "dc_td.GetTemplateResponse":
        return dc_td.GetTemplateResponse.make_one(res)

    def get_template_group_access_control_entry(
        self,
        res: "bs_td.GetTemplateGroupAccessControlEntryResponseTypeDef",
    ) -> "dc_td.GetTemplateGroupAccessControlEntryResponse":
        return dc_td.GetTemplateGroupAccessControlEntryResponse.make_one(res)

    def list_connectors(
        self,
        res: "bs_td.ListConnectorsResponseTypeDef",
    ) -> "dc_td.ListConnectorsResponse":
        return dc_td.ListConnectorsResponse.make_one(res)

    def list_directory_registrations(
        self,
        res: "bs_td.ListDirectoryRegistrationsResponseTypeDef",
    ) -> "dc_td.ListDirectoryRegistrationsResponse":
        return dc_td.ListDirectoryRegistrationsResponse.make_one(res)

    def list_service_principal_names(
        self,
        res: "bs_td.ListServicePrincipalNamesResponseTypeDef",
    ) -> "dc_td.ListServicePrincipalNamesResponse":
        return dc_td.ListServicePrincipalNamesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_template_group_access_control_entries(
        self,
        res: "bs_td.ListTemplateGroupAccessControlEntriesResponseTypeDef",
    ) -> "dc_td.ListTemplateGroupAccessControlEntriesResponse":
        return dc_td.ListTemplateGroupAccessControlEntriesResponse.make_one(res)

    def list_templates(
        self,
        res: "bs_td.ListTemplatesResponseTypeDef",
    ) -> "dc_td.ListTemplatesResponse":
        return dc_td.ListTemplatesResponse.make_one(res)

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

    def update_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_template_group_access_control_entry(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


pca_connector_ad_caster = PCA_CONNECTOR_ADCaster()
