# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_medialive import type_defs as bs_td


class MEDIALIVECaster:

    def batch_delete(
        self,
        res: "bs_td.BatchDeleteResponseTypeDef",
    ) -> "dc_td.BatchDeleteResponse":
        return dc_td.BatchDeleteResponse.make_one(res)

    def batch_start(
        self,
        res: "bs_td.BatchStartResponseTypeDef",
    ) -> "dc_td.BatchStartResponse":
        return dc_td.BatchStartResponse.make_one(res)

    def batch_stop(
        self,
        res: "bs_td.BatchStopResponseTypeDef",
    ) -> "dc_td.BatchStopResponse":
        return dc_td.BatchStopResponse.make_one(res)

    def batch_update_schedule(
        self,
        res: "bs_td.BatchUpdateScheduleResponseTypeDef",
    ) -> "dc_td.BatchUpdateScheduleResponse":
        return dc_td.BatchUpdateScheduleResponse.make_one(res)

    def create_channel(
        self,
        res: "bs_td.CreateChannelResponseTypeDef",
    ) -> "dc_td.CreateChannelResponse":
        return dc_td.CreateChannelResponse.make_one(res)

    def create_input(
        self,
        res: "bs_td.CreateInputResponseTypeDef",
    ) -> "dc_td.CreateInputResponse":
        return dc_td.CreateInputResponse.make_one(res)

    def create_input_security_group(
        self,
        res: "bs_td.CreateInputSecurityGroupResponseTypeDef",
    ) -> "dc_td.CreateInputSecurityGroupResponse":
        return dc_td.CreateInputSecurityGroupResponse.make_one(res)

    def create_multiplex(
        self,
        res: "bs_td.CreateMultiplexResponseTypeDef",
    ) -> "dc_td.CreateMultiplexResponse":
        return dc_td.CreateMultiplexResponse.make_one(res)

    def create_multiplex_program(
        self,
        res: "bs_td.CreateMultiplexProgramResponseTypeDef",
    ) -> "dc_td.CreateMultiplexProgramResponse":
        return dc_td.CreateMultiplexProgramResponse.make_one(res)

    def create_partner_input(
        self,
        res: "bs_td.CreatePartnerInputResponseTypeDef",
    ) -> "dc_td.CreatePartnerInputResponse":
        return dc_td.CreatePartnerInputResponse.make_one(res)

    def create_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_channel(
        self,
        res: "bs_td.DeleteChannelResponseTypeDef",
    ) -> "dc_td.DeleteChannelResponse":
        return dc_td.DeleteChannelResponse.make_one(res)

    def delete_multiplex(
        self,
        res: "bs_td.DeleteMultiplexResponseTypeDef",
    ) -> "dc_td.DeleteMultiplexResponse":
        return dc_td.DeleteMultiplexResponse.make_one(res)

    def delete_multiplex_program(
        self,
        res: "bs_td.DeleteMultiplexProgramResponseTypeDef",
    ) -> "dc_td.DeleteMultiplexProgramResponse":
        return dc_td.DeleteMultiplexProgramResponse.make_one(res)

    def delete_reservation(
        self,
        res: "bs_td.DeleteReservationResponseTypeDef",
    ) -> "dc_td.DeleteReservationResponse":
        return dc_td.DeleteReservationResponse.make_one(res)

    def delete_tags(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_account_configuration(
        self,
        res: "bs_td.DescribeAccountConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeAccountConfigurationResponse":
        return dc_td.DescribeAccountConfigurationResponse.make_one(res)

    def describe_channel(
        self,
        res: "bs_td.DescribeChannelResponseTypeDef",
    ) -> "dc_td.DescribeChannelResponse":
        return dc_td.DescribeChannelResponse.make_one(res)

    def describe_input(
        self,
        res: "bs_td.DescribeInputResponseTypeDef",
    ) -> "dc_td.DescribeInputResponse":
        return dc_td.DescribeInputResponse.make_one(res)

    def describe_input_device(
        self,
        res: "bs_td.DescribeInputDeviceResponseTypeDef",
    ) -> "dc_td.DescribeInputDeviceResponse":
        return dc_td.DescribeInputDeviceResponse.make_one(res)

    def describe_input_device_thumbnail(
        self,
        res: "bs_td.DescribeInputDeviceThumbnailResponseTypeDef",
    ) -> "dc_td.DescribeInputDeviceThumbnailResponse":
        return dc_td.DescribeInputDeviceThumbnailResponse.make_one(res)

    def describe_input_security_group(
        self,
        res: "bs_td.DescribeInputSecurityGroupResponseTypeDef",
    ) -> "dc_td.DescribeInputSecurityGroupResponse":
        return dc_td.DescribeInputSecurityGroupResponse.make_one(res)

    def describe_multiplex(
        self,
        res: "bs_td.DescribeMultiplexResponseTypeDef",
    ) -> "dc_td.DescribeMultiplexResponse":
        return dc_td.DescribeMultiplexResponse.make_one(res)

    def describe_multiplex_program(
        self,
        res: "bs_td.DescribeMultiplexProgramResponseTypeDef",
    ) -> "dc_td.DescribeMultiplexProgramResponse":
        return dc_td.DescribeMultiplexProgramResponse.make_one(res)

    def describe_offering(
        self,
        res: "bs_td.DescribeOfferingResponseTypeDef",
    ) -> "dc_td.DescribeOfferingResponse":
        return dc_td.DescribeOfferingResponse.make_one(res)

    def describe_reservation(
        self,
        res: "bs_td.DescribeReservationResponseTypeDef",
    ) -> "dc_td.DescribeReservationResponse":
        return dc_td.DescribeReservationResponse.make_one(res)

    def describe_schedule(
        self,
        res: "bs_td.DescribeScheduleResponseTypeDef",
    ) -> "dc_td.DescribeScheduleResponse":
        return dc_td.DescribeScheduleResponse.make_one(res)

    def describe_thumbnails(
        self,
        res: "bs_td.DescribeThumbnailsResponseTypeDef",
    ) -> "dc_td.DescribeThumbnailsResponse":
        return dc_td.DescribeThumbnailsResponse.make_one(res)

    def list_channels(
        self,
        res: "bs_td.ListChannelsResponseTypeDef",
    ) -> "dc_td.ListChannelsResponse":
        return dc_td.ListChannelsResponse.make_one(res)

    def list_input_device_transfers(
        self,
        res: "bs_td.ListInputDeviceTransfersResponseTypeDef",
    ) -> "dc_td.ListInputDeviceTransfersResponse":
        return dc_td.ListInputDeviceTransfersResponse.make_one(res)

    def list_input_devices(
        self,
        res: "bs_td.ListInputDevicesResponseTypeDef",
    ) -> "dc_td.ListInputDevicesResponse":
        return dc_td.ListInputDevicesResponse.make_one(res)

    def list_input_security_groups(
        self,
        res: "bs_td.ListInputSecurityGroupsResponseTypeDef",
    ) -> "dc_td.ListInputSecurityGroupsResponse":
        return dc_td.ListInputSecurityGroupsResponse.make_one(res)

    def list_inputs(
        self,
        res: "bs_td.ListInputsResponseTypeDef",
    ) -> "dc_td.ListInputsResponse":
        return dc_td.ListInputsResponse.make_one(res)

    def list_multiplex_programs(
        self,
        res: "bs_td.ListMultiplexProgramsResponseTypeDef",
    ) -> "dc_td.ListMultiplexProgramsResponse":
        return dc_td.ListMultiplexProgramsResponse.make_one(res)

    def list_multiplexes(
        self,
        res: "bs_td.ListMultiplexesResponseTypeDef",
    ) -> "dc_td.ListMultiplexesResponse":
        return dc_td.ListMultiplexesResponse.make_one(res)

    def list_offerings(
        self,
        res: "bs_td.ListOfferingsResponseTypeDef",
    ) -> "dc_td.ListOfferingsResponse":
        return dc_td.ListOfferingsResponse.make_one(res)

    def list_reservations(
        self,
        res: "bs_td.ListReservationsResponseTypeDef",
    ) -> "dc_td.ListReservationsResponse":
        return dc_td.ListReservationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def purchase_offering(
        self,
        res: "bs_td.PurchaseOfferingResponseTypeDef",
    ) -> "dc_td.PurchaseOfferingResponse":
        return dc_td.PurchaseOfferingResponse.make_one(res)

    def start_channel(
        self,
        res: "bs_td.StartChannelResponseTypeDef",
    ) -> "dc_td.StartChannelResponse":
        return dc_td.StartChannelResponse.make_one(res)

    def start_multiplex(
        self,
        res: "bs_td.StartMultiplexResponseTypeDef",
    ) -> "dc_td.StartMultiplexResponse":
        return dc_td.StartMultiplexResponse.make_one(res)

    def stop_channel(
        self,
        res: "bs_td.StopChannelResponseTypeDef",
    ) -> "dc_td.StopChannelResponse":
        return dc_td.StopChannelResponse.make_one(res)

    def stop_multiplex(
        self,
        res: "bs_td.StopMultiplexResponseTypeDef",
    ) -> "dc_td.StopMultiplexResponse":
        return dc_td.StopMultiplexResponse.make_one(res)

    def update_account_configuration(
        self,
        res: "bs_td.UpdateAccountConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateAccountConfigurationResponse":
        return dc_td.UpdateAccountConfigurationResponse.make_one(res)

    def update_channel(
        self,
        res: "bs_td.UpdateChannelResponseTypeDef",
    ) -> "dc_td.UpdateChannelResponse":
        return dc_td.UpdateChannelResponse.make_one(res)

    def update_channel_class(
        self,
        res: "bs_td.UpdateChannelClassResponseTypeDef",
    ) -> "dc_td.UpdateChannelClassResponse":
        return dc_td.UpdateChannelClassResponse.make_one(res)

    def update_input(
        self,
        res: "bs_td.UpdateInputResponseTypeDef",
    ) -> "dc_td.UpdateInputResponse":
        return dc_td.UpdateInputResponse.make_one(res)

    def update_input_device(
        self,
        res: "bs_td.UpdateInputDeviceResponseTypeDef",
    ) -> "dc_td.UpdateInputDeviceResponse":
        return dc_td.UpdateInputDeviceResponse.make_one(res)

    def update_input_security_group(
        self,
        res: "bs_td.UpdateInputSecurityGroupResponseTypeDef",
    ) -> "dc_td.UpdateInputSecurityGroupResponse":
        return dc_td.UpdateInputSecurityGroupResponse.make_one(res)

    def update_multiplex(
        self,
        res: "bs_td.UpdateMultiplexResponseTypeDef",
    ) -> "dc_td.UpdateMultiplexResponse":
        return dc_td.UpdateMultiplexResponse.make_one(res)

    def update_multiplex_program(
        self,
        res: "bs_td.UpdateMultiplexProgramResponseTypeDef",
    ) -> "dc_td.UpdateMultiplexProgramResponse":
        return dc_td.UpdateMultiplexProgramResponse.make_one(res)

    def update_reservation(
        self,
        res: "bs_td.UpdateReservationResponseTypeDef",
    ) -> "dc_td.UpdateReservationResponse":
        return dc_td.UpdateReservationResponse.make_one(res)

    def restart_channel_pipelines(
        self,
        res: "bs_td.RestartChannelPipelinesResponseTypeDef",
    ) -> "dc_td.RestartChannelPipelinesResponse":
        return dc_td.RestartChannelPipelinesResponse.make_one(res)

    def create_cloud_watch_alarm_template(
        self,
        res: "bs_td.CreateCloudWatchAlarmTemplateResponseTypeDef",
    ) -> "dc_td.CreateCloudWatchAlarmTemplateResponse":
        return dc_td.CreateCloudWatchAlarmTemplateResponse.make_one(res)

    def create_cloud_watch_alarm_template_group(
        self,
        res: "bs_td.CreateCloudWatchAlarmTemplateGroupResponseTypeDef",
    ) -> "dc_td.CreateCloudWatchAlarmTemplateGroupResponse":
        return dc_td.CreateCloudWatchAlarmTemplateGroupResponse.make_one(res)

    def create_event_bridge_rule_template(
        self,
        res: "bs_td.CreateEventBridgeRuleTemplateResponseTypeDef",
    ) -> "dc_td.CreateEventBridgeRuleTemplateResponse":
        return dc_td.CreateEventBridgeRuleTemplateResponse.make_one(res)

    def create_event_bridge_rule_template_group(
        self,
        res: "bs_td.CreateEventBridgeRuleTemplateGroupResponseTypeDef",
    ) -> "dc_td.CreateEventBridgeRuleTemplateGroupResponse":
        return dc_td.CreateEventBridgeRuleTemplateGroupResponse.make_one(res)

    def create_signal_map(
        self,
        res: "bs_td.CreateSignalMapResponseTypeDef",
    ) -> "dc_td.CreateSignalMapResponse":
        return dc_td.CreateSignalMapResponse.make_one(res)

    def delete_cloud_watch_alarm_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_cloud_watch_alarm_template_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_event_bridge_rule_template(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_event_bridge_rule_template_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_signal_map(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_cloud_watch_alarm_template(
        self,
        res: "bs_td.GetCloudWatchAlarmTemplateResponseTypeDef",
    ) -> "dc_td.GetCloudWatchAlarmTemplateResponse":
        return dc_td.GetCloudWatchAlarmTemplateResponse.make_one(res)

    def get_cloud_watch_alarm_template_group(
        self,
        res: "bs_td.GetCloudWatchAlarmTemplateGroupResponseTypeDef",
    ) -> "dc_td.GetCloudWatchAlarmTemplateGroupResponse":
        return dc_td.GetCloudWatchAlarmTemplateGroupResponse.make_one(res)

    def get_event_bridge_rule_template(
        self,
        res: "bs_td.GetEventBridgeRuleTemplateResponseTypeDef",
    ) -> "dc_td.GetEventBridgeRuleTemplateResponse":
        return dc_td.GetEventBridgeRuleTemplateResponse.make_one(res)

    def get_event_bridge_rule_template_group(
        self,
        res: "bs_td.GetEventBridgeRuleTemplateGroupResponseTypeDef",
    ) -> "dc_td.GetEventBridgeRuleTemplateGroupResponse":
        return dc_td.GetEventBridgeRuleTemplateGroupResponse.make_one(res)

    def get_signal_map(
        self,
        res: "bs_td.GetSignalMapResponseTypeDef",
    ) -> "dc_td.GetSignalMapResponse":
        return dc_td.GetSignalMapResponse.make_one(res)

    def list_cloud_watch_alarm_template_groups(
        self,
        res: "bs_td.ListCloudWatchAlarmTemplateGroupsResponseTypeDef",
    ) -> "dc_td.ListCloudWatchAlarmTemplateGroupsResponse":
        return dc_td.ListCloudWatchAlarmTemplateGroupsResponse.make_one(res)

    def list_cloud_watch_alarm_templates(
        self,
        res: "bs_td.ListCloudWatchAlarmTemplatesResponseTypeDef",
    ) -> "dc_td.ListCloudWatchAlarmTemplatesResponse":
        return dc_td.ListCloudWatchAlarmTemplatesResponse.make_one(res)

    def list_event_bridge_rule_template_groups(
        self,
        res: "bs_td.ListEventBridgeRuleTemplateGroupsResponseTypeDef",
    ) -> "dc_td.ListEventBridgeRuleTemplateGroupsResponse":
        return dc_td.ListEventBridgeRuleTemplateGroupsResponse.make_one(res)

    def list_event_bridge_rule_templates(
        self,
        res: "bs_td.ListEventBridgeRuleTemplatesResponseTypeDef",
    ) -> "dc_td.ListEventBridgeRuleTemplatesResponse":
        return dc_td.ListEventBridgeRuleTemplatesResponse.make_one(res)

    def list_signal_maps(
        self,
        res: "bs_td.ListSignalMapsResponseTypeDef",
    ) -> "dc_td.ListSignalMapsResponse":
        return dc_td.ListSignalMapsResponse.make_one(res)

    def start_delete_monitor_deployment(
        self,
        res: "bs_td.StartDeleteMonitorDeploymentResponseTypeDef",
    ) -> "dc_td.StartDeleteMonitorDeploymentResponse":
        return dc_td.StartDeleteMonitorDeploymentResponse.make_one(res)

    def start_monitor_deployment(
        self,
        res: "bs_td.StartMonitorDeploymentResponseTypeDef",
    ) -> "dc_td.StartMonitorDeploymentResponse":
        return dc_td.StartMonitorDeploymentResponse.make_one(res)

    def start_update_signal_map(
        self,
        res: "bs_td.StartUpdateSignalMapResponseTypeDef",
    ) -> "dc_td.StartUpdateSignalMapResponse":
        return dc_td.StartUpdateSignalMapResponse.make_one(res)

    def update_cloud_watch_alarm_template(
        self,
        res: "bs_td.UpdateCloudWatchAlarmTemplateResponseTypeDef",
    ) -> "dc_td.UpdateCloudWatchAlarmTemplateResponse":
        return dc_td.UpdateCloudWatchAlarmTemplateResponse.make_one(res)

    def update_cloud_watch_alarm_template_group(
        self,
        res: "bs_td.UpdateCloudWatchAlarmTemplateGroupResponseTypeDef",
    ) -> "dc_td.UpdateCloudWatchAlarmTemplateGroupResponse":
        return dc_td.UpdateCloudWatchAlarmTemplateGroupResponse.make_one(res)

    def update_event_bridge_rule_template(
        self,
        res: "bs_td.UpdateEventBridgeRuleTemplateResponseTypeDef",
    ) -> "dc_td.UpdateEventBridgeRuleTemplateResponse":
        return dc_td.UpdateEventBridgeRuleTemplateResponse.make_one(res)

    def update_event_bridge_rule_template_group(
        self,
        res: "bs_td.UpdateEventBridgeRuleTemplateGroupResponseTypeDef",
    ) -> "dc_td.UpdateEventBridgeRuleTemplateGroupResponse":
        return dc_td.UpdateEventBridgeRuleTemplateGroupResponse.make_one(res)

    def create_channel_placement_group(
        self,
        res: "bs_td.CreateChannelPlacementGroupResponseTypeDef",
    ) -> "dc_td.CreateChannelPlacementGroupResponse":
        return dc_td.CreateChannelPlacementGroupResponse.make_one(res)

    def create_cluster(
        self,
        res: "bs_td.CreateClusterResponseTypeDef",
    ) -> "dc_td.CreateClusterResponse":
        return dc_td.CreateClusterResponse.make_one(res)

    def create_network(
        self,
        res: "bs_td.CreateNetworkResponseTypeDef",
    ) -> "dc_td.CreateNetworkResponse":
        return dc_td.CreateNetworkResponse.make_one(res)

    def create_node(
        self,
        res: "bs_td.CreateNodeResponseTypeDef",
    ) -> "dc_td.CreateNodeResponse":
        return dc_td.CreateNodeResponse.make_one(res)

    def create_node_registration_script(
        self,
        res: "bs_td.CreateNodeRegistrationScriptResponseTypeDef",
    ) -> "dc_td.CreateNodeRegistrationScriptResponse":
        return dc_td.CreateNodeRegistrationScriptResponse.make_one(res)

    def delete_channel_placement_group(
        self,
        res: "bs_td.DeleteChannelPlacementGroupResponseTypeDef",
    ) -> "dc_td.DeleteChannelPlacementGroupResponse":
        return dc_td.DeleteChannelPlacementGroupResponse.make_one(res)

    def delete_cluster(
        self,
        res: "bs_td.DeleteClusterResponseTypeDef",
    ) -> "dc_td.DeleteClusterResponse":
        return dc_td.DeleteClusterResponse.make_one(res)

    def delete_network(
        self,
        res: "bs_td.DeleteNetworkResponseTypeDef",
    ) -> "dc_td.DeleteNetworkResponse":
        return dc_td.DeleteNetworkResponse.make_one(res)

    def delete_node(
        self,
        res: "bs_td.DeleteNodeResponseTypeDef",
    ) -> "dc_td.DeleteNodeResponse":
        return dc_td.DeleteNodeResponse.make_one(res)

    def describe_channel_placement_group(
        self,
        res: "bs_td.DescribeChannelPlacementGroupResponseTypeDef",
    ) -> "dc_td.DescribeChannelPlacementGroupResponse":
        return dc_td.DescribeChannelPlacementGroupResponse.make_one(res)

    def describe_cluster(
        self,
        res: "bs_td.DescribeClusterResponseTypeDef",
    ) -> "dc_td.DescribeClusterResponse":
        return dc_td.DescribeClusterResponse.make_one(res)

    def describe_network(
        self,
        res: "bs_td.DescribeNetworkResponseTypeDef",
    ) -> "dc_td.DescribeNetworkResponse":
        return dc_td.DescribeNetworkResponse.make_one(res)

    def describe_node(
        self,
        res: "bs_td.DescribeNodeResponseTypeDef",
    ) -> "dc_td.DescribeNodeResponse":
        return dc_td.DescribeNodeResponse.make_one(res)

    def list_channel_placement_groups(
        self,
        res: "bs_td.ListChannelPlacementGroupsResponseTypeDef",
    ) -> "dc_td.ListChannelPlacementGroupsResponse":
        return dc_td.ListChannelPlacementGroupsResponse.make_one(res)

    def list_clusters(
        self,
        res: "bs_td.ListClustersResponseTypeDef",
    ) -> "dc_td.ListClustersResponse":
        return dc_td.ListClustersResponse.make_one(res)

    def list_networks(
        self,
        res: "bs_td.ListNetworksResponseTypeDef",
    ) -> "dc_td.ListNetworksResponse":
        return dc_td.ListNetworksResponse.make_one(res)

    def list_nodes(
        self,
        res: "bs_td.ListNodesResponseTypeDef",
    ) -> "dc_td.ListNodesResponse":
        return dc_td.ListNodesResponse.make_one(res)

    def update_channel_placement_group(
        self,
        res: "bs_td.UpdateChannelPlacementGroupResponseTypeDef",
    ) -> "dc_td.UpdateChannelPlacementGroupResponse":
        return dc_td.UpdateChannelPlacementGroupResponse.make_one(res)

    def update_cluster(
        self,
        res: "bs_td.UpdateClusterResponseTypeDef",
    ) -> "dc_td.UpdateClusterResponse":
        return dc_td.UpdateClusterResponse.make_one(res)

    def update_network(
        self,
        res: "bs_td.UpdateNetworkResponseTypeDef",
    ) -> "dc_td.UpdateNetworkResponse":
        return dc_td.UpdateNetworkResponse.make_one(res)

    def update_node(
        self,
        res: "bs_td.UpdateNodeResponseTypeDef",
    ) -> "dc_td.UpdateNodeResponse":
        return dc_td.UpdateNodeResponse.make_one(res)

    def update_node_state(
        self,
        res: "bs_td.UpdateNodeStateResponseTypeDef",
    ) -> "dc_td.UpdateNodeStateResponse":
        return dc_td.UpdateNodeStateResponse.make_one(res)

    def list_versions(
        self,
        res: "bs_td.ListVersionsResponseTypeDef",
    ) -> "dc_td.ListVersionsResponse":
        return dc_td.ListVersionsResponse.make_one(res)

    def create_sdi_source(
        self,
        res: "bs_td.CreateSdiSourceResponseTypeDef",
    ) -> "dc_td.CreateSdiSourceResponse":
        return dc_td.CreateSdiSourceResponse.make_one(res)

    def delete_sdi_source(
        self,
        res: "bs_td.DeleteSdiSourceResponseTypeDef",
    ) -> "dc_td.DeleteSdiSourceResponse":
        return dc_td.DeleteSdiSourceResponse.make_one(res)

    def describe_sdi_source(
        self,
        res: "bs_td.DescribeSdiSourceResponseTypeDef",
    ) -> "dc_td.DescribeSdiSourceResponse":
        return dc_td.DescribeSdiSourceResponse.make_one(res)

    def list_sdi_sources(
        self,
        res: "bs_td.ListSdiSourcesResponseTypeDef",
    ) -> "dc_td.ListSdiSourcesResponse":
        return dc_td.ListSdiSourcesResponse.make_one(res)

    def update_sdi_source(
        self,
        res: "bs_td.UpdateSdiSourceResponseTypeDef",
    ) -> "dc_td.UpdateSdiSourceResponse":
        return dc_td.UpdateSdiSourceResponse.make_one(res)


medialive_caster = MEDIALIVECaster()
