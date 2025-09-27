# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iot_managed_integrations import type_defs as bs_td


class IOT_MANAGED_INTEGRATIONSCaster:

    def create_account_association(
        self,
        res: "bs_td.CreateAccountAssociationResponseTypeDef",
    ) -> "dc_td.CreateAccountAssociationResponse":
        return dc_td.CreateAccountAssociationResponse.make_one(res)

    def create_cloud_connector(
        self,
        res: "bs_td.CreateCloudConnectorResponseTypeDef",
    ) -> "dc_td.CreateCloudConnectorResponse":
        return dc_td.CreateCloudConnectorResponse.make_one(res)

    def create_connector_destination(
        self,
        res: "bs_td.CreateConnectorDestinationResponseTypeDef",
    ) -> "dc_td.CreateConnectorDestinationResponse":
        return dc_td.CreateConnectorDestinationResponse.make_one(res)

    def create_credential_locker(
        self,
        res: "bs_td.CreateCredentialLockerResponseTypeDef",
    ) -> "dc_td.CreateCredentialLockerResponse":
        return dc_td.CreateCredentialLockerResponse.make_one(res)

    def create_destination(
        self,
        res: "bs_td.CreateDestinationResponseTypeDef",
    ) -> "dc_td.CreateDestinationResponse":
        return dc_td.CreateDestinationResponse.make_one(res)

    def create_event_log_configuration(
        self,
        res: "bs_td.CreateEventLogConfigurationResponseTypeDef",
    ) -> "dc_td.CreateEventLogConfigurationResponse":
        return dc_td.CreateEventLogConfigurationResponse.make_one(res)

    def create_managed_thing(
        self,
        res: "bs_td.CreateManagedThingResponseTypeDef",
    ) -> "dc_td.CreateManagedThingResponse":
        return dc_td.CreateManagedThingResponse.make_one(res)

    def create_notification_configuration(
        self,
        res: "bs_td.CreateNotificationConfigurationResponseTypeDef",
    ) -> "dc_td.CreateNotificationConfigurationResponse":
        return dc_td.CreateNotificationConfigurationResponse.make_one(res)

    def create_ota_task(
        self,
        res: "bs_td.CreateOtaTaskResponseTypeDef",
    ) -> "dc_td.CreateOtaTaskResponse":
        return dc_td.CreateOtaTaskResponse.make_one(res)

    def create_ota_task_configuration(
        self,
        res: "bs_td.CreateOtaTaskConfigurationResponseTypeDef",
    ) -> "dc_td.CreateOtaTaskConfigurationResponse":
        return dc_td.CreateOtaTaskConfigurationResponse.make_one(res)

    def create_provisioning_profile(
        self,
        res: "bs_td.CreateProvisioningProfileResponseTypeDef",
    ) -> "dc_td.CreateProvisioningProfileResponse":
        return dc_td.CreateProvisioningProfileResponse.make_one(res)

    def delete_account_association(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_cloud_connector(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_connector_destination(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_credential_locker(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_destination(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_event_log_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_managed_thing(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_notification_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_ota_task(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_ota_task_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_provisioning_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_account_association(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_account_association(
        self,
        res: "bs_td.GetAccountAssociationResponseTypeDef",
    ) -> "dc_td.GetAccountAssociationResponse":
        return dc_td.GetAccountAssociationResponse.make_one(res)

    def get_cloud_connector(
        self,
        res: "bs_td.GetCloudConnectorResponseTypeDef",
    ) -> "dc_td.GetCloudConnectorResponse":
        return dc_td.GetCloudConnectorResponse.make_one(res)

    def get_connector_destination(
        self,
        res: "bs_td.GetConnectorDestinationResponseTypeDef",
    ) -> "dc_td.GetConnectorDestinationResponse":
        return dc_td.GetConnectorDestinationResponse.make_one(res)

    def get_credential_locker(
        self,
        res: "bs_td.GetCredentialLockerResponseTypeDef",
    ) -> "dc_td.GetCredentialLockerResponse":
        return dc_td.GetCredentialLockerResponse.make_one(res)

    def get_custom_endpoint(
        self,
        res: "bs_td.GetCustomEndpointResponseTypeDef",
    ) -> "dc_td.GetCustomEndpointResponse":
        return dc_td.GetCustomEndpointResponse.make_one(res)

    def get_default_encryption_configuration(
        self,
        res: "bs_td.GetDefaultEncryptionConfigurationResponseTypeDef",
    ) -> "dc_td.GetDefaultEncryptionConfigurationResponse":
        return dc_td.GetDefaultEncryptionConfigurationResponse.make_one(res)

    def get_destination(
        self,
        res: "bs_td.GetDestinationResponseTypeDef",
    ) -> "dc_td.GetDestinationResponse":
        return dc_td.GetDestinationResponse.make_one(res)

    def get_device_discovery(
        self,
        res: "bs_td.GetDeviceDiscoveryResponseTypeDef",
    ) -> "dc_td.GetDeviceDiscoveryResponse":
        return dc_td.GetDeviceDiscoveryResponse.make_one(res)

    def get_event_log_configuration(
        self,
        res: "bs_td.GetEventLogConfigurationResponseTypeDef",
    ) -> "dc_td.GetEventLogConfigurationResponse":
        return dc_td.GetEventLogConfigurationResponse.make_one(res)

    def get_hub_configuration(
        self,
        res: "bs_td.GetHubConfigurationResponseTypeDef",
    ) -> "dc_td.GetHubConfigurationResponse":
        return dc_td.GetHubConfigurationResponse.make_one(res)

    def get_managed_thing(
        self,
        res: "bs_td.GetManagedThingResponseTypeDef",
    ) -> "dc_td.GetManagedThingResponse":
        return dc_td.GetManagedThingResponse.make_one(res)

    def get_managed_thing_capabilities(
        self,
        res: "bs_td.GetManagedThingCapabilitiesResponseTypeDef",
    ) -> "dc_td.GetManagedThingCapabilitiesResponse":
        return dc_td.GetManagedThingCapabilitiesResponse.make_one(res)

    def get_managed_thing_connectivity_data(
        self,
        res: "bs_td.GetManagedThingConnectivityDataResponseTypeDef",
    ) -> "dc_td.GetManagedThingConnectivityDataResponse":
        return dc_td.GetManagedThingConnectivityDataResponse.make_one(res)

    def get_managed_thing_meta_data(
        self,
        res: "bs_td.GetManagedThingMetaDataResponseTypeDef",
    ) -> "dc_td.GetManagedThingMetaDataResponse":
        return dc_td.GetManagedThingMetaDataResponse.make_one(res)

    def get_managed_thing_state(
        self,
        res: "bs_td.GetManagedThingStateResponseTypeDef",
    ) -> "dc_td.GetManagedThingStateResponse":
        return dc_td.GetManagedThingStateResponse.make_one(res)

    def get_notification_configuration(
        self,
        res: "bs_td.GetNotificationConfigurationResponseTypeDef",
    ) -> "dc_td.GetNotificationConfigurationResponse":
        return dc_td.GetNotificationConfigurationResponse.make_one(res)

    def get_ota_task(
        self,
        res: "bs_td.GetOtaTaskResponseTypeDef",
    ) -> "dc_td.GetOtaTaskResponse":
        return dc_td.GetOtaTaskResponse.make_one(res)

    def get_ota_task_configuration(
        self,
        res: "bs_td.GetOtaTaskConfigurationResponseTypeDef",
    ) -> "dc_td.GetOtaTaskConfigurationResponse":
        return dc_td.GetOtaTaskConfigurationResponse.make_one(res)

    def get_provisioning_profile(
        self,
        res: "bs_td.GetProvisioningProfileResponseTypeDef",
    ) -> "dc_td.GetProvisioningProfileResponse":
        return dc_td.GetProvisioningProfileResponse.make_one(res)

    def get_runtime_log_configuration(
        self,
        res: "bs_td.GetRuntimeLogConfigurationResponseTypeDef",
    ) -> "dc_td.GetRuntimeLogConfigurationResponse":
        return dc_td.GetRuntimeLogConfigurationResponse.make_one(res)

    def get_schema_version(
        self,
        res: "bs_td.GetSchemaVersionResponseTypeDef",
    ) -> "dc_td.GetSchemaVersionResponse":
        return dc_td.GetSchemaVersionResponse.make_one(res)

    def list_account_associations(
        self,
        res: "bs_td.ListAccountAssociationsResponseTypeDef",
    ) -> "dc_td.ListAccountAssociationsResponse":
        return dc_td.ListAccountAssociationsResponse.make_one(res)

    def list_cloud_connectors(
        self,
        res: "bs_td.ListCloudConnectorsResponseTypeDef",
    ) -> "dc_td.ListCloudConnectorsResponse":
        return dc_td.ListCloudConnectorsResponse.make_one(res)

    def list_connector_destinations(
        self,
        res: "bs_td.ListConnectorDestinationsResponseTypeDef",
    ) -> "dc_td.ListConnectorDestinationsResponse":
        return dc_td.ListConnectorDestinationsResponse.make_one(res)

    def list_credential_lockers(
        self,
        res: "bs_td.ListCredentialLockersResponseTypeDef",
    ) -> "dc_td.ListCredentialLockersResponse":
        return dc_td.ListCredentialLockersResponse.make_one(res)

    def list_destinations(
        self,
        res: "bs_td.ListDestinationsResponseTypeDef",
    ) -> "dc_td.ListDestinationsResponse":
        return dc_td.ListDestinationsResponse.make_one(res)

    def list_device_discoveries(
        self,
        res: "bs_td.ListDeviceDiscoveriesResponseTypeDef",
    ) -> "dc_td.ListDeviceDiscoveriesResponse":
        return dc_td.ListDeviceDiscoveriesResponse.make_one(res)

    def list_discovered_devices(
        self,
        res: "bs_td.ListDiscoveredDevicesResponseTypeDef",
    ) -> "dc_td.ListDiscoveredDevicesResponse":
        return dc_td.ListDiscoveredDevicesResponse.make_one(res)

    def list_event_log_configurations(
        self,
        res: "bs_td.ListEventLogConfigurationsResponseTypeDef",
    ) -> "dc_td.ListEventLogConfigurationsResponse":
        return dc_td.ListEventLogConfigurationsResponse.make_one(res)

    def list_managed_thing_account_associations(
        self,
        res: "bs_td.ListManagedThingAccountAssociationsResponseTypeDef",
    ) -> "dc_td.ListManagedThingAccountAssociationsResponse":
        return dc_td.ListManagedThingAccountAssociationsResponse.make_one(res)

    def list_managed_thing_schemas(
        self,
        res: "bs_td.ListManagedThingSchemasResponseTypeDef",
    ) -> "dc_td.ListManagedThingSchemasResponse":
        return dc_td.ListManagedThingSchemasResponse.make_one(res)

    def list_managed_things(
        self,
        res: "bs_td.ListManagedThingsResponseTypeDef",
    ) -> "dc_td.ListManagedThingsResponse":
        return dc_td.ListManagedThingsResponse.make_one(res)

    def list_notification_configurations(
        self,
        res: "bs_td.ListNotificationConfigurationsResponseTypeDef",
    ) -> "dc_td.ListNotificationConfigurationsResponse":
        return dc_td.ListNotificationConfigurationsResponse.make_one(res)

    def list_ota_task_configurations(
        self,
        res: "bs_td.ListOtaTaskConfigurationsResponseTypeDef",
    ) -> "dc_td.ListOtaTaskConfigurationsResponse":
        return dc_td.ListOtaTaskConfigurationsResponse.make_one(res)

    def list_ota_task_executions(
        self,
        res: "bs_td.ListOtaTaskExecutionsResponseTypeDef",
    ) -> "dc_td.ListOtaTaskExecutionsResponse":
        return dc_td.ListOtaTaskExecutionsResponse.make_one(res)

    def list_ota_tasks(
        self,
        res: "bs_td.ListOtaTasksResponseTypeDef",
    ) -> "dc_td.ListOtaTasksResponse":
        return dc_td.ListOtaTasksResponse.make_one(res)

    def list_provisioning_profiles(
        self,
        res: "bs_td.ListProvisioningProfilesResponseTypeDef",
    ) -> "dc_td.ListProvisioningProfilesResponse":
        return dc_td.ListProvisioningProfilesResponse.make_one(res)

    def list_schema_versions(
        self,
        res: "bs_td.ListSchemaVersionsResponseTypeDef",
    ) -> "dc_td.ListSchemaVersionsResponse":
        return dc_td.ListSchemaVersionsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_default_encryption_configuration(
        self,
        res: "bs_td.PutDefaultEncryptionConfigurationResponseTypeDef",
    ) -> "dc_td.PutDefaultEncryptionConfigurationResponse":
        return dc_td.PutDefaultEncryptionConfigurationResponse.make_one(res)

    def put_hub_configuration(
        self,
        res: "bs_td.PutHubConfigurationResponseTypeDef",
    ) -> "dc_td.PutHubConfigurationResponse":
        return dc_td.PutHubConfigurationResponse.make_one(res)

    def put_runtime_log_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def register_account_association(
        self,
        res: "bs_td.RegisterAccountAssociationResponseTypeDef",
    ) -> "dc_td.RegisterAccountAssociationResponse":
        return dc_td.RegisterAccountAssociationResponse.make_one(res)

    def register_custom_endpoint(
        self,
        res: "bs_td.RegisterCustomEndpointResponseTypeDef",
    ) -> "dc_td.RegisterCustomEndpointResponse":
        return dc_td.RegisterCustomEndpointResponse.make_one(res)

    def reset_runtime_log_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def send_connector_event(
        self,
        res: "bs_td.SendConnectorEventResponseTypeDef",
    ) -> "dc_td.SendConnectorEventResponse":
        return dc_td.SendConnectorEventResponse.make_one(res)

    def send_managed_thing_command(
        self,
        res: "bs_td.SendManagedThingCommandResponseTypeDef",
    ) -> "dc_td.SendManagedThingCommandResponse":
        return dc_td.SendManagedThingCommandResponse.make_one(res)

    def start_account_association_refresh(
        self,
        res: "bs_td.StartAccountAssociationRefreshResponseTypeDef",
    ) -> "dc_td.StartAccountAssociationRefreshResponse":
        return dc_td.StartAccountAssociationRefreshResponse.make_one(res)

    def start_device_discovery(
        self,
        res: "bs_td.StartDeviceDiscoveryResponseTypeDef",
    ) -> "dc_td.StartDeviceDiscoveryResponse":
        return dc_td.StartDeviceDiscoveryResponse.make_one(res)

    def update_account_association(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_cloud_connector(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_connector_destination(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_destination(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_event_log_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_managed_thing(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_notification_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_ota_task(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


iot_managed_integrations_caster = IOT_MANAGED_INTEGRATIONSCaster()
