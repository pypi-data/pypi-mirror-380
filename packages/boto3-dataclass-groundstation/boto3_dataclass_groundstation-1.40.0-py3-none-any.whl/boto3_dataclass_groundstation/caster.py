# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_groundstation import type_defs as bs_td


class GROUNDSTATIONCaster:

    def cancel_contact(
        self,
        res: "bs_td.ContactIdResponseTypeDef",
    ) -> "dc_td.ContactIdResponse":
        return dc_td.ContactIdResponse.make_one(res)

    def create_config(
        self,
        res: "bs_td.ConfigIdResponseTypeDef",
    ) -> "dc_td.ConfigIdResponse":
        return dc_td.ConfigIdResponse.make_one(res)

    def create_dataflow_endpoint_group(
        self,
        res: "bs_td.DataflowEndpointGroupIdResponseTypeDef",
    ) -> "dc_td.DataflowEndpointGroupIdResponse":
        return dc_td.DataflowEndpointGroupIdResponse.make_one(res)

    def create_ephemeris(
        self,
        res: "bs_td.EphemerisIdResponseTypeDef",
    ) -> "dc_td.EphemerisIdResponse":
        return dc_td.EphemerisIdResponse.make_one(res)

    def create_mission_profile(
        self,
        res: "bs_td.MissionProfileIdResponseTypeDef",
    ) -> "dc_td.MissionProfileIdResponse":
        return dc_td.MissionProfileIdResponse.make_one(res)

    def delete_config(
        self,
        res: "bs_td.ConfigIdResponseTypeDef",
    ) -> "dc_td.ConfigIdResponse":
        return dc_td.ConfigIdResponse.make_one(res)

    def delete_dataflow_endpoint_group(
        self,
        res: "bs_td.DataflowEndpointGroupIdResponseTypeDef",
    ) -> "dc_td.DataflowEndpointGroupIdResponse":
        return dc_td.DataflowEndpointGroupIdResponse.make_one(res)

    def delete_ephemeris(
        self,
        res: "bs_td.EphemerisIdResponseTypeDef",
    ) -> "dc_td.EphemerisIdResponse":
        return dc_td.EphemerisIdResponse.make_one(res)

    def delete_mission_profile(
        self,
        res: "bs_td.MissionProfileIdResponseTypeDef",
    ) -> "dc_td.MissionProfileIdResponse":
        return dc_td.MissionProfileIdResponse.make_one(res)

    def describe_contact(
        self,
        res: "bs_td.DescribeContactResponseTypeDef",
    ) -> "dc_td.DescribeContactResponse":
        return dc_td.DescribeContactResponse.make_one(res)

    def describe_ephemeris(
        self,
        res: "bs_td.DescribeEphemerisResponseTypeDef",
    ) -> "dc_td.DescribeEphemerisResponse":
        return dc_td.DescribeEphemerisResponse.make_one(res)

    def get_agent_configuration(
        self,
        res: "bs_td.GetAgentConfigurationResponseTypeDef",
    ) -> "dc_td.GetAgentConfigurationResponse":
        return dc_td.GetAgentConfigurationResponse.make_one(res)

    def get_config(
        self,
        res: "bs_td.GetConfigResponseTypeDef",
    ) -> "dc_td.GetConfigResponse":
        return dc_td.GetConfigResponse.make_one(res)

    def get_dataflow_endpoint_group(
        self,
        res: "bs_td.GetDataflowEndpointGroupResponseTypeDef",
    ) -> "dc_td.GetDataflowEndpointGroupResponse":
        return dc_td.GetDataflowEndpointGroupResponse.make_one(res)

    def get_minute_usage(
        self,
        res: "bs_td.GetMinuteUsageResponseTypeDef",
    ) -> "dc_td.GetMinuteUsageResponse":
        return dc_td.GetMinuteUsageResponse.make_one(res)

    def get_mission_profile(
        self,
        res: "bs_td.GetMissionProfileResponseTypeDef",
    ) -> "dc_td.GetMissionProfileResponse":
        return dc_td.GetMissionProfileResponse.make_one(res)

    def get_satellite(
        self,
        res: "bs_td.GetSatelliteResponseTypeDef",
    ) -> "dc_td.GetSatelliteResponse":
        return dc_td.GetSatelliteResponse.make_one(res)

    def list_configs(
        self,
        res: "bs_td.ListConfigsResponseTypeDef",
    ) -> "dc_td.ListConfigsResponse":
        return dc_td.ListConfigsResponse.make_one(res)

    def list_contacts(
        self,
        res: "bs_td.ListContactsResponseTypeDef",
    ) -> "dc_td.ListContactsResponse":
        return dc_td.ListContactsResponse.make_one(res)

    def list_dataflow_endpoint_groups(
        self,
        res: "bs_td.ListDataflowEndpointGroupsResponseTypeDef",
    ) -> "dc_td.ListDataflowEndpointGroupsResponse":
        return dc_td.ListDataflowEndpointGroupsResponse.make_one(res)

    def list_ephemerides(
        self,
        res: "bs_td.ListEphemeridesResponseTypeDef",
    ) -> "dc_td.ListEphemeridesResponse":
        return dc_td.ListEphemeridesResponse.make_one(res)

    def list_ground_stations(
        self,
        res: "bs_td.ListGroundStationsResponseTypeDef",
    ) -> "dc_td.ListGroundStationsResponse":
        return dc_td.ListGroundStationsResponse.make_one(res)

    def list_mission_profiles(
        self,
        res: "bs_td.ListMissionProfilesResponseTypeDef",
    ) -> "dc_td.ListMissionProfilesResponse":
        return dc_td.ListMissionProfilesResponse.make_one(res)

    def list_satellites(
        self,
        res: "bs_td.ListSatellitesResponseTypeDef",
    ) -> "dc_td.ListSatellitesResponse":
        return dc_td.ListSatellitesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def register_agent(
        self,
        res: "bs_td.RegisterAgentResponseTypeDef",
    ) -> "dc_td.RegisterAgentResponse":
        return dc_td.RegisterAgentResponse.make_one(res)

    def reserve_contact(
        self,
        res: "bs_td.ContactIdResponseTypeDef",
    ) -> "dc_td.ContactIdResponse":
        return dc_td.ContactIdResponse.make_one(res)

    def update_agent_status(
        self,
        res: "bs_td.UpdateAgentStatusResponseTypeDef",
    ) -> "dc_td.UpdateAgentStatusResponse":
        return dc_td.UpdateAgentStatusResponse.make_one(res)

    def update_config(
        self,
        res: "bs_td.ConfigIdResponseTypeDef",
    ) -> "dc_td.ConfigIdResponse":
        return dc_td.ConfigIdResponse.make_one(res)

    def update_ephemeris(
        self,
        res: "bs_td.EphemerisIdResponseTypeDef",
    ) -> "dc_td.EphemerisIdResponse":
        return dc_td.EphemerisIdResponse.make_one(res)

    def update_mission_profile(
        self,
        res: "bs_td.MissionProfileIdResponseTypeDef",
    ) -> "dc_td.MissionProfileIdResponse":
        return dc_td.MissionProfileIdResponse.make_one(res)


groundstation_caster = GROUNDSTATIONCaster()
