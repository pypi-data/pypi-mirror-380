# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotfleetwise import type_defs as bs_td


class IOTFLEETWISECaster:

    def batch_create_vehicle(
        self,
        res: "bs_td.BatchCreateVehicleResponseTypeDef",
    ) -> "dc_td.BatchCreateVehicleResponse":
        return dc_td.BatchCreateVehicleResponse.make_one(res)

    def batch_update_vehicle(
        self,
        res: "bs_td.BatchUpdateVehicleResponseTypeDef",
    ) -> "dc_td.BatchUpdateVehicleResponse":
        return dc_td.BatchUpdateVehicleResponse.make_one(res)

    def create_campaign(
        self,
        res: "bs_td.CreateCampaignResponseTypeDef",
    ) -> "dc_td.CreateCampaignResponse":
        return dc_td.CreateCampaignResponse.make_one(res)

    def create_decoder_manifest(
        self,
        res: "bs_td.CreateDecoderManifestResponseTypeDef",
    ) -> "dc_td.CreateDecoderManifestResponse":
        return dc_td.CreateDecoderManifestResponse.make_one(res)

    def create_fleet(
        self,
        res: "bs_td.CreateFleetResponseTypeDef",
    ) -> "dc_td.CreateFleetResponse":
        return dc_td.CreateFleetResponse.make_one(res)

    def create_model_manifest(
        self,
        res: "bs_td.CreateModelManifestResponseTypeDef",
    ) -> "dc_td.CreateModelManifestResponse":
        return dc_td.CreateModelManifestResponse.make_one(res)

    def create_signal_catalog(
        self,
        res: "bs_td.CreateSignalCatalogResponseTypeDef",
    ) -> "dc_td.CreateSignalCatalogResponse":
        return dc_td.CreateSignalCatalogResponse.make_one(res)

    def create_state_template(
        self,
        res: "bs_td.CreateStateTemplateResponseTypeDef",
    ) -> "dc_td.CreateStateTemplateResponse":
        return dc_td.CreateStateTemplateResponse.make_one(res)

    def create_vehicle(
        self,
        res: "bs_td.CreateVehicleResponseTypeDef",
    ) -> "dc_td.CreateVehicleResponse":
        return dc_td.CreateVehicleResponse.make_one(res)

    def delete_campaign(
        self,
        res: "bs_td.DeleteCampaignResponseTypeDef",
    ) -> "dc_td.DeleteCampaignResponse":
        return dc_td.DeleteCampaignResponse.make_one(res)

    def delete_decoder_manifest(
        self,
        res: "bs_td.DeleteDecoderManifestResponseTypeDef",
    ) -> "dc_td.DeleteDecoderManifestResponse":
        return dc_td.DeleteDecoderManifestResponse.make_one(res)

    def delete_fleet(
        self,
        res: "bs_td.DeleteFleetResponseTypeDef",
    ) -> "dc_td.DeleteFleetResponse":
        return dc_td.DeleteFleetResponse.make_one(res)

    def delete_model_manifest(
        self,
        res: "bs_td.DeleteModelManifestResponseTypeDef",
    ) -> "dc_td.DeleteModelManifestResponse":
        return dc_td.DeleteModelManifestResponse.make_one(res)

    def delete_signal_catalog(
        self,
        res: "bs_td.DeleteSignalCatalogResponseTypeDef",
    ) -> "dc_td.DeleteSignalCatalogResponse":
        return dc_td.DeleteSignalCatalogResponse.make_one(res)

    def delete_state_template(
        self,
        res: "bs_td.DeleteStateTemplateResponseTypeDef",
    ) -> "dc_td.DeleteStateTemplateResponse":
        return dc_td.DeleteStateTemplateResponse.make_one(res)

    def delete_vehicle(
        self,
        res: "bs_td.DeleteVehicleResponseTypeDef",
    ) -> "dc_td.DeleteVehicleResponse":
        return dc_td.DeleteVehicleResponse.make_one(res)

    def get_campaign(
        self,
        res: "bs_td.GetCampaignResponseTypeDef",
    ) -> "dc_td.GetCampaignResponse":
        return dc_td.GetCampaignResponse.make_one(res)

    def get_decoder_manifest(
        self,
        res: "bs_td.GetDecoderManifestResponseTypeDef",
    ) -> "dc_td.GetDecoderManifestResponse":
        return dc_td.GetDecoderManifestResponse.make_one(res)

    def get_encryption_configuration(
        self,
        res: "bs_td.GetEncryptionConfigurationResponseTypeDef",
    ) -> "dc_td.GetEncryptionConfigurationResponse":
        return dc_td.GetEncryptionConfigurationResponse.make_one(res)

    def get_fleet(
        self,
        res: "bs_td.GetFleetResponseTypeDef",
    ) -> "dc_td.GetFleetResponse":
        return dc_td.GetFleetResponse.make_one(res)

    def get_logging_options(
        self,
        res: "bs_td.GetLoggingOptionsResponseTypeDef",
    ) -> "dc_td.GetLoggingOptionsResponse":
        return dc_td.GetLoggingOptionsResponse.make_one(res)

    def get_model_manifest(
        self,
        res: "bs_td.GetModelManifestResponseTypeDef",
    ) -> "dc_td.GetModelManifestResponse":
        return dc_td.GetModelManifestResponse.make_one(res)

    def get_register_account_status(
        self,
        res: "bs_td.GetRegisterAccountStatusResponseTypeDef",
    ) -> "dc_td.GetRegisterAccountStatusResponse":
        return dc_td.GetRegisterAccountStatusResponse.make_one(res)

    def get_signal_catalog(
        self,
        res: "bs_td.GetSignalCatalogResponseTypeDef",
    ) -> "dc_td.GetSignalCatalogResponse":
        return dc_td.GetSignalCatalogResponse.make_one(res)

    def get_state_template(
        self,
        res: "bs_td.GetStateTemplateResponseTypeDef",
    ) -> "dc_td.GetStateTemplateResponse":
        return dc_td.GetStateTemplateResponse.make_one(res)

    def get_vehicle(
        self,
        res: "bs_td.GetVehicleResponseTypeDef",
    ) -> "dc_td.GetVehicleResponse":
        return dc_td.GetVehicleResponse.make_one(res)

    def get_vehicle_status(
        self,
        res: "bs_td.GetVehicleStatusResponseTypeDef",
    ) -> "dc_td.GetVehicleStatusResponse":
        return dc_td.GetVehicleStatusResponse.make_one(res)

    def import_decoder_manifest(
        self,
        res: "bs_td.ImportDecoderManifestResponseTypeDef",
    ) -> "dc_td.ImportDecoderManifestResponse":
        return dc_td.ImportDecoderManifestResponse.make_one(res)

    def import_signal_catalog(
        self,
        res: "bs_td.ImportSignalCatalogResponseTypeDef",
    ) -> "dc_td.ImportSignalCatalogResponse":
        return dc_td.ImportSignalCatalogResponse.make_one(res)

    def list_campaigns(
        self,
        res: "bs_td.ListCampaignsResponseTypeDef",
    ) -> "dc_td.ListCampaignsResponse":
        return dc_td.ListCampaignsResponse.make_one(res)

    def list_decoder_manifest_network_interfaces(
        self,
        res: "bs_td.ListDecoderManifestNetworkInterfacesResponseTypeDef",
    ) -> "dc_td.ListDecoderManifestNetworkInterfacesResponse":
        return dc_td.ListDecoderManifestNetworkInterfacesResponse.make_one(res)

    def list_decoder_manifest_signals(
        self,
        res: "bs_td.ListDecoderManifestSignalsResponseTypeDef",
    ) -> "dc_td.ListDecoderManifestSignalsResponse":
        return dc_td.ListDecoderManifestSignalsResponse.make_one(res)

    def list_decoder_manifests(
        self,
        res: "bs_td.ListDecoderManifestsResponseTypeDef",
    ) -> "dc_td.ListDecoderManifestsResponse":
        return dc_td.ListDecoderManifestsResponse.make_one(res)

    def list_fleets(
        self,
        res: "bs_td.ListFleetsResponseTypeDef",
    ) -> "dc_td.ListFleetsResponse":
        return dc_td.ListFleetsResponse.make_one(res)

    def list_fleets_for_vehicle(
        self,
        res: "bs_td.ListFleetsForVehicleResponseTypeDef",
    ) -> "dc_td.ListFleetsForVehicleResponse":
        return dc_td.ListFleetsForVehicleResponse.make_one(res)

    def list_model_manifest_nodes(
        self,
        res: "bs_td.ListModelManifestNodesResponseTypeDef",
    ) -> "dc_td.ListModelManifestNodesResponse":
        return dc_td.ListModelManifestNodesResponse.make_one(res)

    def list_model_manifests(
        self,
        res: "bs_td.ListModelManifestsResponseTypeDef",
    ) -> "dc_td.ListModelManifestsResponse":
        return dc_td.ListModelManifestsResponse.make_one(res)

    def list_signal_catalog_nodes(
        self,
        res: "bs_td.ListSignalCatalogNodesResponseTypeDef",
    ) -> "dc_td.ListSignalCatalogNodesResponse":
        return dc_td.ListSignalCatalogNodesResponse.make_one(res)

    def list_signal_catalogs(
        self,
        res: "bs_td.ListSignalCatalogsResponseTypeDef",
    ) -> "dc_td.ListSignalCatalogsResponse":
        return dc_td.ListSignalCatalogsResponse.make_one(res)

    def list_state_templates(
        self,
        res: "bs_td.ListStateTemplatesResponseTypeDef",
    ) -> "dc_td.ListStateTemplatesResponse":
        return dc_td.ListStateTemplatesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_vehicles(
        self,
        res: "bs_td.ListVehiclesResponseTypeDef",
    ) -> "dc_td.ListVehiclesResponse":
        return dc_td.ListVehiclesResponse.make_one(res)

    def list_vehicles_in_fleet(
        self,
        res: "bs_td.ListVehiclesInFleetResponseTypeDef",
    ) -> "dc_td.ListVehiclesInFleetResponse":
        return dc_td.ListVehiclesInFleetResponse.make_one(res)

    def put_encryption_configuration(
        self,
        res: "bs_td.PutEncryptionConfigurationResponseTypeDef",
    ) -> "dc_td.PutEncryptionConfigurationResponse":
        return dc_td.PutEncryptionConfigurationResponse.make_one(res)

    def register_account(
        self,
        res: "bs_td.RegisterAccountResponseTypeDef",
    ) -> "dc_td.RegisterAccountResponse":
        return dc_td.RegisterAccountResponse.make_one(res)

    def update_campaign(
        self,
        res: "bs_td.UpdateCampaignResponseTypeDef",
    ) -> "dc_td.UpdateCampaignResponse":
        return dc_td.UpdateCampaignResponse.make_one(res)

    def update_decoder_manifest(
        self,
        res: "bs_td.UpdateDecoderManifestResponseTypeDef",
    ) -> "dc_td.UpdateDecoderManifestResponse":
        return dc_td.UpdateDecoderManifestResponse.make_one(res)

    def update_fleet(
        self,
        res: "bs_td.UpdateFleetResponseTypeDef",
    ) -> "dc_td.UpdateFleetResponse":
        return dc_td.UpdateFleetResponse.make_one(res)

    def update_model_manifest(
        self,
        res: "bs_td.UpdateModelManifestResponseTypeDef",
    ) -> "dc_td.UpdateModelManifestResponse":
        return dc_td.UpdateModelManifestResponse.make_one(res)

    def update_signal_catalog(
        self,
        res: "bs_td.UpdateSignalCatalogResponseTypeDef",
    ) -> "dc_td.UpdateSignalCatalogResponse":
        return dc_td.UpdateSignalCatalogResponse.make_one(res)

    def update_state_template(
        self,
        res: "bs_td.UpdateStateTemplateResponseTypeDef",
    ) -> "dc_td.UpdateStateTemplateResponse":
        return dc_td.UpdateStateTemplateResponse.make_one(res)

    def update_vehicle(
        self,
        res: "bs_td.UpdateVehicleResponseTypeDef",
    ) -> "dc_td.UpdateVehicleResponse":
        return dc_td.UpdateVehicleResponse.make_one(res)


iotfleetwise_caster = IOTFLEETWISECaster()
