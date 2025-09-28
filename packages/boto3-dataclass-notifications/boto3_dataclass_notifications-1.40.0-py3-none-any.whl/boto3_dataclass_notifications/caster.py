# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_notifications import type_defs as bs_td


class NOTIFICATIONSCaster:

    def create_event_rule(
        self,
        res: "bs_td.CreateEventRuleResponseTypeDef",
    ) -> "dc_td.CreateEventRuleResponse":
        return dc_td.CreateEventRuleResponse.make_one(res)

    def create_notification_configuration(
        self,
        res: "bs_td.CreateNotificationConfigurationResponseTypeDef",
    ) -> "dc_td.CreateNotificationConfigurationResponse":
        return dc_td.CreateNotificationConfigurationResponse.make_one(res)

    def deregister_notification_hub(
        self,
        res: "bs_td.DeregisterNotificationHubResponseTypeDef",
    ) -> "dc_td.DeregisterNotificationHubResponse":
        return dc_td.DeregisterNotificationHubResponse.make_one(res)

    def get_event_rule(
        self,
        res: "bs_td.GetEventRuleResponseTypeDef",
    ) -> "dc_td.GetEventRuleResponse":
        return dc_td.GetEventRuleResponse.make_one(res)

    def get_managed_notification_child_event(
        self,
        res: "bs_td.GetManagedNotificationChildEventResponseTypeDef",
    ) -> "dc_td.GetManagedNotificationChildEventResponse":
        return dc_td.GetManagedNotificationChildEventResponse.make_one(res)

    def get_managed_notification_configuration(
        self,
        res: "bs_td.GetManagedNotificationConfigurationResponseTypeDef",
    ) -> "dc_td.GetManagedNotificationConfigurationResponse":
        return dc_td.GetManagedNotificationConfigurationResponse.make_one(res)

    def get_managed_notification_event(
        self,
        res: "bs_td.GetManagedNotificationEventResponseTypeDef",
    ) -> "dc_td.GetManagedNotificationEventResponse":
        return dc_td.GetManagedNotificationEventResponse.make_one(res)

    def get_notification_configuration(
        self,
        res: "bs_td.GetNotificationConfigurationResponseTypeDef",
    ) -> "dc_td.GetNotificationConfigurationResponse":
        return dc_td.GetNotificationConfigurationResponse.make_one(res)

    def get_notification_event(
        self,
        res: "bs_td.GetNotificationEventResponseTypeDef",
    ) -> "dc_td.GetNotificationEventResponse":
        return dc_td.GetNotificationEventResponse.make_one(res)

    def get_notifications_access_for_organization(
        self,
        res: "bs_td.GetNotificationsAccessForOrganizationResponseTypeDef",
    ) -> "dc_td.GetNotificationsAccessForOrganizationResponse":
        return dc_td.GetNotificationsAccessForOrganizationResponse.make_one(res)

    def list_channels(
        self,
        res: "bs_td.ListChannelsResponseTypeDef",
    ) -> "dc_td.ListChannelsResponse":
        return dc_td.ListChannelsResponse.make_one(res)

    def list_event_rules(
        self,
        res: "bs_td.ListEventRulesResponseTypeDef",
    ) -> "dc_td.ListEventRulesResponse":
        return dc_td.ListEventRulesResponse.make_one(res)

    def list_managed_notification_channel_associations(
        self,
        res: "bs_td.ListManagedNotificationChannelAssociationsResponseTypeDef",
    ) -> "dc_td.ListManagedNotificationChannelAssociationsResponse":
        return dc_td.ListManagedNotificationChannelAssociationsResponse.make_one(res)

    def list_managed_notification_child_events(
        self,
        res: "bs_td.ListManagedNotificationChildEventsResponseTypeDef",
    ) -> "dc_td.ListManagedNotificationChildEventsResponse":
        return dc_td.ListManagedNotificationChildEventsResponse.make_one(res)

    def list_managed_notification_configurations(
        self,
        res: "bs_td.ListManagedNotificationConfigurationsResponseTypeDef",
    ) -> "dc_td.ListManagedNotificationConfigurationsResponse":
        return dc_td.ListManagedNotificationConfigurationsResponse.make_one(res)

    def list_managed_notification_events(
        self,
        res: "bs_td.ListManagedNotificationEventsResponseTypeDef",
    ) -> "dc_td.ListManagedNotificationEventsResponse":
        return dc_td.ListManagedNotificationEventsResponse.make_one(res)

    def list_member_accounts(
        self,
        res: "bs_td.ListMemberAccountsResponseTypeDef",
    ) -> "dc_td.ListMemberAccountsResponse":
        return dc_td.ListMemberAccountsResponse.make_one(res)

    def list_notification_configurations(
        self,
        res: "bs_td.ListNotificationConfigurationsResponseTypeDef",
    ) -> "dc_td.ListNotificationConfigurationsResponse":
        return dc_td.ListNotificationConfigurationsResponse.make_one(res)

    def list_notification_events(
        self,
        res: "bs_td.ListNotificationEventsResponseTypeDef",
    ) -> "dc_td.ListNotificationEventsResponse":
        return dc_td.ListNotificationEventsResponse.make_one(res)

    def list_notification_hubs(
        self,
        res: "bs_td.ListNotificationHubsResponseTypeDef",
    ) -> "dc_td.ListNotificationHubsResponse":
        return dc_td.ListNotificationHubsResponse.make_one(res)

    def list_organizational_units(
        self,
        res: "bs_td.ListOrganizationalUnitsResponseTypeDef",
    ) -> "dc_td.ListOrganizationalUnitsResponse":
        return dc_td.ListOrganizationalUnitsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def register_notification_hub(
        self,
        res: "bs_td.RegisterNotificationHubResponseTypeDef",
    ) -> "dc_td.RegisterNotificationHubResponse":
        return dc_td.RegisterNotificationHubResponse.make_one(res)

    def update_event_rule(
        self,
        res: "bs_td.UpdateEventRuleResponseTypeDef",
    ) -> "dc_td.UpdateEventRuleResponse":
        return dc_td.UpdateEventRuleResponse.make_one(res)

    def update_notification_configuration(
        self,
        res: "bs_td.UpdateNotificationConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateNotificationConfigurationResponse":
        return dc_td.UpdateNotificationConfigurationResponse.make_one(res)


notifications_caster = NOTIFICATIONSCaster()
