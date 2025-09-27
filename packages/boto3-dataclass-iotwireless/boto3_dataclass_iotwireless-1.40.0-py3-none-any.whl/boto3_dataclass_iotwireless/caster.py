# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotwireless import type_defs as bs_td


class IOTWIRELESSCaster:

    def associate_aws_account_with_partner_account(
        self,
        res: "bs_td.AssociateAwsAccountWithPartnerAccountResponseTypeDef",
    ) -> "dc_td.AssociateAwsAccountWithPartnerAccountResponse":
        return dc_td.AssociateAwsAccountWithPartnerAccountResponse.make_one(res)

    def associate_wireless_gateway_with_certificate(
        self,
        res: "bs_td.AssociateWirelessGatewayWithCertificateResponseTypeDef",
    ) -> "dc_td.AssociateWirelessGatewayWithCertificateResponse":
        return dc_td.AssociateWirelessGatewayWithCertificateResponse.make_one(res)

    def create_destination(
        self,
        res: "bs_td.CreateDestinationResponseTypeDef",
    ) -> "dc_td.CreateDestinationResponse":
        return dc_td.CreateDestinationResponse.make_one(res)

    def create_device_profile(
        self,
        res: "bs_td.CreateDeviceProfileResponseTypeDef",
    ) -> "dc_td.CreateDeviceProfileResponse":
        return dc_td.CreateDeviceProfileResponse.make_one(res)

    def create_fuota_task(
        self,
        res: "bs_td.CreateFuotaTaskResponseTypeDef",
    ) -> "dc_td.CreateFuotaTaskResponse":
        return dc_td.CreateFuotaTaskResponse.make_one(res)

    def create_multicast_group(
        self,
        res: "bs_td.CreateMulticastGroupResponseTypeDef",
    ) -> "dc_td.CreateMulticastGroupResponse":
        return dc_td.CreateMulticastGroupResponse.make_one(res)

    def create_network_analyzer_configuration(
        self,
        res: "bs_td.CreateNetworkAnalyzerConfigurationResponseTypeDef",
    ) -> "dc_td.CreateNetworkAnalyzerConfigurationResponse":
        return dc_td.CreateNetworkAnalyzerConfigurationResponse.make_one(res)

    def create_service_profile(
        self,
        res: "bs_td.CreateServiceProfileResponseTypeDef",
    ) -> "dc_td.CreateServiceProfileResponse":
        return dc_td.CreateServiceProfileResponse.make_one(res)

    def create_wireless_device(
        self,
        res: "bs_td.CreateWirelessDeviceResponseTypeDef",
    ) -> "dc_td.CreateWirelessDeviceResponse":
        return dc_td.CreateWirelessDeviceResponse.make_one(res)

    def create_wireless_gateway(
        self,
        res: "bs_td.CreateWirelessGatewayResponseTypeDef",
    ) -> "dc_td.CreateWirelessGatewayResponse":
        return dc_td.CreateWirelessGatewayResponse.make_one(res)

    def create_wireless_gateway_task(
        self,
        res: "bs_td.CreateWirelessGatewayTaskResponseTypeDef",
    ) -> "dc_td.CreateWirelessGatewayTaskResponse":
        return dc_td.CreateWirelessGatewayTaskResponse.make_one(res)

    def create_wireless_gateway_task_definition(
        self,
        res: "bs_td.CreateWirelessGatewayTaskDefinitionResponseTypeDef",
    ) -> "dc_td.CreateWirelessGatewayTaskDefinitionResponse":
        return dc_td.CreateWirelessGatewayTaskDefinitionResponse.make_one(res)

    def get_destination(
        self,
        res: "bs_td.GetDestinationResponseTypeDef",
    ) -> "dc_td.GetDestinationResponse":
        return dc_td.GetDestinationResponse.make_one(res)

    def get_device_profile(
        self,
        res: "bs_td.GetDeviceProfileResponseTypeDef",
    ) -> "dc_td.GetDeviceProfileResponse":
        return dc_td.GetDeviceProfileResponse.make_one(res)

    def get_event_configuration_by_resource_types(
        self,
        res: "bs_td.GetEventConfigurationByResourceTypesResponseTypeDef",
    ) -> "dc_td.GetEventConfigurationByResourceTypesResponse":
        return dc_td.GetEventConfigurationByResourceTypesResponse.make_one(res)

    def get_fuota_task(
        self,
        res: "bs_td.GetFuotaTaskResponseTypeDef",
    ) -> "dc_td.GetFuotaTaskResponse":
        return dc_td.GetFuotaTaskResponse.make_one(res)

    def get_log_levels_by_resource_types(
        self,
        res: "bs_td.GetLogLevelsByResourceTypesResponseTypeDef",
    ) -> "dc_td.GetLogLevelsByResourceTypesResponse":
        return dc_td.GetLogLevelsByResourceTypesResponse.make_one(res)

    def get_metric_configuration(
        self,
        res: "bs_td.GetMetricConfigurationResponseTypeDef",
    ) -> "dc_td.GetMetricConfigurationResponse":
        return dc_td.GetMetricConfigurationResponse.make_one(res)

    def get_metrics(
        self,
        res: "bs_td.GetMetricsResponseTypeDef",
    ) -> "dc_td.GetMetricsResponse":
        return dc_td.GetMetricsResponse.make_one(res)

    def get_multicast_group(
        self,
        res: "bs_td.GetMulticastGroupResponseTypeDef",
    ) -> "dc_td.GetMulticastGroupResponse":
        return dc_td.GetMulticastGroupResponse.make_one(res)

    def get_multicast_group_session(
        self,
        res: "bs_td.GetMulticastGroupSessionResponseTypeDef",
    ) -> "dc_td.GetMulticastGroupSessionResponse":
        return dc_td.GetMulticastGroupSessionResponse.make_one(res)

    def get_network_analyzer_configuration(
        self,
        res: "bs_td.GetNetworkAnalyzerConfigurationResponseTypeDef",
    ) -> "dc_td.GetNetworkAnalyzerConfigurationResponse":
        return dc_td.GetNetworkAnalyzerConfigurationResponse.make_one(res)

    def get_partner_account(
        self,
        res: "bs_td.GetPartnerAccountResponseTypeDef",
    ) -> "dc_td.GetPartnerAccountResponse":
        return dc_td.GetPartnerAccountResponse.make_one(res)

    def get_position(
        self,
        res: "bs_td.GetPositionResponseTypeDef",
    ) -> "dc_td.GetPositionResponse":
        return dc_td.GetPositionResponse.make_one(res)

    def get_position_configuration(
        self,
        res: "bs_td.GetPositionConfigurationResponseTypeDef",
    ) -> "dc_td.GetPositionConfigurationResponse":
        return dc_td.GetPositionConfigurationResponse.make_one(res)

    def get_position_estimate(
        self,
        res: "bs_td.GetPositionEstimateResponseTypeDef",
    ) -> "dc_td.GetPositionEstimateResponse":
        return dc_td.GetPositionEstimateResponse.make_one(res)

    def get_resource_event_configuration(
        self,
        res: "bs_td.GetResourceEventConfigurationResponseTypeDef",
    ) -> "dc_td.GetResourceEventConfigurationResponse":
        return dc_td.GetResourceEventConfigurationResponse.make_one(res)

    def get_resource_log_level(
        self,
        res: "bs_td.GetResourceLogLevelResponseTypeDef",
    ) -> "dc_td.GetResourceLogLevelResponse":
        return dc_td.GetResourceLogLevelResponse.make_one(res)

    def get_resource_position(
        self,
        res: "bs_td.GetResourcePositionResponseTypeDef",
    ) -> "dc_td.GetResourcePositionResponse":
        return dc_td.GetResourcePositionResponse.make_one(res)

    def get_service_endpoint(
        self,
        res: "bs_td.GetServiceEndpointResponseTypeDef",
    ) -> "dc_td.GetServiceEndpointResponse":
        return dc_td.GetServiceEndpointResponse.make_one(res)

    def get_service_profile(
        self,
        res: "bs_td.GetServiceProfileResponseTypeDef",
    ) -> "dc_td.GetServiceProfileResponse":
        return dc_td.GetServiceProfileResponse.make_one(res)

    def get_wireless_device(
        self,
        res: "bs_td.GetWirelessDeviceResponseTypeDef",
    ) -> "dc_td.GetWirelessDeviceResponse":
        return dc_td.GetWirelessDeviceResponse.make_one(res)

    def get_wireless_device_import_task(
        self,
        res: "bs_td.GetWirelessDeviceImportTaskResponseTypeDef",
    ) -> "dc_td.GetWirelessDeviceImportTaskResponse":
        return dc_td.GetWirelessDeviceImportTaskResponse.make_one(res)

    def get_wireless_device_statistics(
        self,
        res: "bs_td.GetWirelessDeviceStatisticsResponseTypeDef",
    ) -> "dc_td.GetWirelessDeviceStatisticsResponse":
        return dc_td.GetWirelessDeviceStatisticsResponse.make_one(res)

    def get_wireless_gateway(
        self,
        res: "bs_td.GetWirelessGatewayResponseTypeDef",
    ) -> "dc_td.GetWirelessGatewayResponse":
        return dc_td.GetWirelessGatewayResponse.make_one(res)

    def get_wireless_gateway_certificate(
        self,
        res: "bs_td.GetWirelessGatewayCertificateResponseTypeDef",
    ) -> "dc_td.GetWirelessGatewayCertificateResponse":
        return dc_td.GetWirelessGatewayCertificateResponse.make_one(res)

    def get_wireless_gateway_firmware_information(
        self,
        res: "bs_td.GetWirelessGatewayFirmwareInformationResponseTypeDef",
    ) -> "dc_td.GetWirelessGatewayFirmwareInformationResponse":
        return dc_td.GetWirelessGatewayFirmwareInformationResponse.make_one(res)

    def get_wireless_gateway_statistics(
        self,
        res: "bs_td.GetWirelessGatewayStatisticsResponseTypeDef",
    ) -> "dc_td.GetWirelessGatewayStatisticsResponse":
        return dc_td.GetWirelessGatewayStatisticsResponse.make_one(res)

    def get_wireless_gateway_task(
        self,
        res: "bs_td.GetWirelessGatewayTaskResponseTypeDef",
    ) -> "dc_td.GetWirelessGatewayTaskResponse":
        return dc_td.GetWirelessGatewayTaskResponse.make_one(res)

    def get_wireless_gateway_task_definition(
        self,
        res: "bs_td.GetWirelessGatewayTaskDefinitionResponseTypeDef",
    ) -> "dc_td.GetWirelessGatewayTaskDefinitionResponse":
        return dc_td.GetWirelessGatewayTaskDefinitionResponse.make_one(res)

    def list_destinations(
        self,
        res: "bs_td.ListDestinationsResponseTypeDef",
    ) -> "dc_td.ListDestinationsResponse":
        return dc_td.ListDestinationsResponse.make_one(res)

    def list_device_profiles(
        self,
        res: "bs_td.ListDeviceProfilesResponseTypeDef",
    ) -> "dc_td.ListDeviceProfilesResponse":
        return dc_td.ListDeviceProfilesResponse.make_one(res)

    def list_devices_for_wireless_device_import_task(
        self,
        res: "bs_td.ListDevicesForWirelessDeviceImportTaskResponseTypeDef",
    ) -> "dc_td.ListDevicesForWirelessDeviceImportTaskResponse":
        return dc_td.ListDevicesForWirelessDeviceImportTaskResponse.make_one(res)

    def list_event_configurations(
        self,
        res: "bs_td.ListEventConfigurationsResponseTypeDef",
    ) -> "dc_td.ListEventConfigurationsResponse":
        return dc_td.ListEventConfigurationsResponse.make_one(res)

    def list_fuota_tasks(
        self,
        res: "bs_td.ListFuotaTasksResponseTypeDef",
    ) -> "dc_td.ListFuotaTasksResponse":
        return dc_td.ListFuotaTasksResponse.make_one(res)

    def list_multicast_groups(
        self,
        res: "bs_td.ListMulticastGroupsResponseTypeDef",
    ) -> "dc_td.ListMulticastGroupsResponse":
        return dc_td.ListMulticastGroupsResponse.make_one(res)

    def list_multicast_groups_by_fuota_task(
        self,
        res: "bs_td.ListMulticastGroupsByFuotaTaskResponseTypeDef",
    ) -> "dc_td.ListMulticastGroupsByFuotaTaskResponse":
        return dc_td.ListMulticastGroupsByFuotaTaskResponse.make_one(res)

    def list_network_analyzer_configurations(
        self,
        res: "bs_td.ListNetworkAnalyzerConfigurationsResponseTypeDef",
    ) -> "dc_td.ListNetworkAnalyzerConfigurationsResponse":
        return dc_td.ListNetworkAnalyzerConfigurationsResponse.make_one(res)

    def list_partner_accounts(
        self,
        res: "bs_td.ListPartnerAccountsResponseTypeDef",
    ) -> "dc_td.ListPartnerAccountsResponse":
        return dc_td.ListPartnerAccountsResponse.make_one(res)

    def list_position_configurations(
        self,
        res: "bs_td.ListPositionConfigurationsResponseTypeDef",
    ) -> "dc_td.ListPositionConfigurationsResponse":
        return dc_td.ListPositionConfigurationsResponse.make_one(res)

    def list_queued_messages(
        self,
        res: "bs_td.ListQueuedMessagesResponseTypeDef",
    ) -> "dc_td.ListQueuedMessagesResponse":
        return dc_td.ListQueuedMessagesResponse.make_one(res)

    def list_service_profiles(
        self,
        res: "bs_td.ListServiceProfilesResponseTypeDef",
    ) -> "dc_td.ListServiceProfilesResponse":
        return dc_td.ListServiceProfilesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_wireless_device_import_tasks(
        self,
        res: "bs_td.ListWirelessDeviceImportTasksResponseTypeDef",
    ) -> "dc_td.ListWirelessDeviceImportTasksResponse":
        return dc_td.ListWirelessDeviceImportTasksResponse.make_one(res)

    def list_wireless_devices(
        self,
        res: "bs_td.ListWirelessDevicesResponseTypeDef",
    ) -> "dc_td.ListWirelessDevicesResponse":
        return dc_td.ListWirelessDevicesResponse.make_one(res)

    def list_wireless_gateway_task_definitions(
        self,
        res: "bs_td.ListWirelessGatewayTaskDefinitionsResponseTypeDef",
    ) -> "dc_td.ListWirelessGatewayTaskDefinitionsResponse":
        return dc_td.ListWirelessGatewayTaskDefinitionsResponse.make_one(res)

    def list_wireless_gateways(
        self,
        res: "bs_td.ListWirelessGatewaysResponseTypeDef",
    ) -> "dc_td.ListWirelessGatewaysResponse":
        return dc_td.ListWirelessGatewaysResponse.make_one(res)

    def send_data_to_multicast_group(
        self,
        res: "bs_td.SendDataToMulticastGroupResponseTypeDef",
    ) -> "dc_td.SendDataToMulticastGroupResponse":
        return dc_td.SendDataToMulticastGroupResponse.make_one(res)

    def send_data_to_wireless_device(
        self,
        res: "bs_td.SendDataToWirelessDeviceResponseTypeDef",
    ) -> "dc_td.SendDataToWirelessDeviceResponse":
        return dc_td.SendDataToWirelessDeviceResponse.make_one(res)

    def start_single_wireless_device_import_task(
        self,
        res: "bs_td.StartSingleWirelessDeviceImportTaskResponseTypeDef",
    ) -> "dc_td.StartSingleWirelessDeviceImportTaskResponse":
        return dc_td.StartSingleWirelessDeviceImportTaskResponse.make_one(res)

    def start_wireless_device_import_task(
        self,
        res: "bs_td.StartWirelessDeviceImportTaskResponseTypeDef",
    ) -> "dc_td.StartWirelessDeviceImportTaskResponse":
        return dc_td.StartWirelessDeviceImportTaskResponse.make_one(res)

    def test_wireless_device(
        self,
        res: "bs_td.TestWirelessDeviceResponseTypeDef",
    ) -> "dc_td.TestWirelessDeviceResponse":
        return dc_td.TestWirelessDeviceResponse.make_one(res)


iotwireless_caster = IOTWIRELESSCaster()
