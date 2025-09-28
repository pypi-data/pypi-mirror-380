# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_notifications import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class SummarizationDimensionDetail:
    boto3_raw_data: "type_defs.SummarizationDimensionDetailTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SummarizationDimensionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SummarizationDimensionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregationKey:
    boto3_raw_data: "type_defs.AggregationKeyTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AggregationKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AggregationKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SummarizationDimensionOverview:
    boto3_raw_data: "type_defs.SummarizationDimensionOverviewTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    count = field("count")
    sampleValues = field("sampleValues")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SummarizationDimensionOverviewTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SummarizationDimensionOverviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateChannelRequest:
    boto3_raw_data: "type_defs.AssociateChannelRequestTypeDef" = dataclasses.field()

    arn = field("arn")
    notificationConfigurationArn = field("notificationConfigurationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateManagedNotificationAccountContactRequest:
    boto3_raw_data: (
        "type_defs.AssociateManagedNotificationAccountContactRequestTypeDef"
    ) = dataclasses.field()

    contactIdentifier = field("contactIdentifier")
    managedNotificationConfigurationArn = field("managedNotificationConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateManagedNotificationAccountContactRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AssociateManagedNotificationAccountContactRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateManagedNotificationAdditionalChannelRequest:
    boto3_raw_data: (
        "type_defs.AssociateManagedNotificationAdditionalChannelRequestTypeDef"
    ) = dataclasses.field()

    channelArn = field("channelArn")
    managedNotificationConfigurationArn = field("managedNotificationConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateManagedNotificationAdditionalChannelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AssociateManagedNotificationAdditionalChannelRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateOrganizationalUnitRequest:
    boto3_raw_data: "type_defs.AssociateOrganizationalUnitRequestTypeDef" = (
        dataclasses.field()
    )

    organizationalUnitId = field("organizationalUnitId")
    notificationConfigurationArn = field("notificationConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateOrganizationalUnitRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateOrganizationalUnitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventRuleRequest:
    boto3_raw_data: "type_defs.CreateEventRuleRequestTypeDef" = dataclasses.field()

    notificationConfigurationArn = field("notificationConfigurationArn")
    source = field("source")
    eventType = field("eventType")
    regions = field("regions")
    eventPattern = field("eventPattern")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventRuleStatusSummary:
    boto3_raw_data: "type_defs.EventRuleStatusSummaryTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventRuleStatusSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventRuleStatusSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNotificationConfigurationRequest:
    boto3_raw_data: "type_defs.CreateNotificationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")
    aggregationDuration = field("aggregationDuration")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateNotificationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNotificationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventRuleRequest:
    boto3_raw_data: "type_defs.DeleteEventRuleRequestTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNotificationConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteNotificationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteNotificationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNotificationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterNotificationHubRequest:
    boto3_raw_data: "type_defs.DeregisterNotificationHubRequestTypeDef" = (
        dataclasses.field()
    )

    notificationHubRegion = field("notificationHubRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterNotificationHubRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterNotificationHubRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationHubStatusSummary:
    boto3_raw_data: "type_defs.NotificationHubStatusSummaryTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationHubStatusSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationHubStatusSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dimension:
    boto3_raw_data: "type_defs.DimensionTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateChannelRequest:
    boto3_raw_data: "type_defs.DisassociateChannelRequestTypeDef" = dataclasses.field()

    arn = field("arn")
    notificationConfigurationArn = field("notificationConfigurationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateManagedNotificationAccountContactRequest:
    boto3_raw_data: (
        "type_defs.DisassociateManagedNotificationAccountContactRequestTypeDef"
    ) = dataclasses.field()

    contactIdentifier = field("contactIdentifier")
    managedNotificationConfigurationArn = field("managedNotificationConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateManagedNotificationAccountContactRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DisassociateManagedNotificationAccountContactRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateManagedNotificationAdditionalChannelRequest:
    boto3_raw_data: (
        "type_defs.DisassociateManagedNotificationAdditionalChannelRequestTypeDef"
    ) = dataclasses.field()

    channelArn = field("channelArn")
    managedNotificationConfigurationArn = field("managedNotificationConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateManagedNotificationAdditionalChannelRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DisassociateManagedNotificationAdditionalChannelRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateOrganizationalUnitRequest:
    boto3_raw_data: "type_defs.DisassociateOrganizationalUnitRequestTypeDef" = (
        dataclasses.field()
    )

    organizationalUnitId = field("organizationalUnitId")
    notificationConfigurationArn = field("notificationConfigurationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateOrganizationalUnitRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateOrganizationalUnitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventRuleRequest:
    boto3_raw_data: "type_defs.GetEventRuleRequestTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedNotificationChildEventRequest:
    boto3_raw_data: "type_defs.GetManagedNotificationChildEventRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    locale = field("locale")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetManagedNotificationChildEventRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedNotificationChildEventRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedNotificationConfigurationRequest:
    boto3_raw_data: "type_defs.GetManagedNotificationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetManagedNotificationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedNotificationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedNotificationEventRequest:
    boto3_raw_data: "type_defs.GetManagedNotificationEventRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    locale = field("locale")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetManagedNotificationEventRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedNotificationEventRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNotificationConfigurationRequest:
    boto3_raw_data: "type_defs.GetNotificationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNotificationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNotificationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNotificationEventRequest:
    boto3_raw_data: "type_defs.GetNotificationEventRequestTypeDef" = dataclasses.field()

    arn = field("arn")
    locale = field("locale")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNotificationEventRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNotificationEventRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationsAccessForOrganization:
    boto3_raw_data: "type_defs.NotificationsAccessForOrganizationTypeDef" = (
        dataclasses.field()
    )

    accessStatus = field("accessStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotificationsAccessForOrganizationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationsAccessForOrganizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsRequest:
    boto3_raw_data: "type_defs.ListChannelsRequestTypeDef" = dataclasses.field()

    notificationConfigurationArn = field("notificationConfigurationArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventRulesRequest:
    boto3_raw_data: "type_defs.ListEventRulesRequestTypeDef" = dataclasses.field()

    notificationConfigurationArn = field("notificationConfigurationArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationChannelAssociationsRequest:
    boto3_raw_data: (
        "type_defs.ListManagedNotificationChannelAssociationsRequestTypeDef"
    ) = dataclasses.field()

    managedNotificationConfigurationArn = field("managedNotificationConfigurationArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationChannelAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListManagedNotificationChannelAssociationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedNotificationChannelAssociationSummary:
    boto3_raw_data: "type_defs.ManagedNotificationChannelAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    channelIdentifier = field("channelIdentifier")
    channelType = field("channelType")
    overrideOption = field("overrideOption")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManagedNotificationChannelAssociationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedNotificationChannelAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationConfigurationsRequest:
    boto3_raw_data: "type_defs.ListManagedNotificationConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    channelIdentifier = field("channelIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedNotificationConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedNotificationConfigurationStructure:
    boto3_raw_data: "type_defs.ManagedNotificationConfigurationStructureTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManagedNotificationConfigurationStructureTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedNotificationConfigurationStructureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemberAccountsRequest:
    boto3_raw_data: "type_defs.ListMemberAccountsRequestTypeDef" = dataclasses.field()

    notificationConfigurationArn = field("notificationConfigurationArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    memberAccount = field("memberAccount")
    status = field("status")
    organizationalUnitId = field("organizationalUnitId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMemberAccountsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemberAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberAccount:
    boto3_raw_data: "type_defs.MemberAccountTypeDef" = dataclasses.field()

    accountId = field("accountId")
    status = field("status")
    statusReason = field("statusReason")
    organizationalUnitId = field("organizationalUnitId")
    notificationConfigurationArn = field("notificationConfigurationArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberAccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberAccountTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationConfigurationsRequest:
    boto3_raw_data: "type_defs.ListNotificationConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    eventRuleSource = field("eventRuleSource")
    channelArn = field("channelArn")
    status = field("status")
    subtype = field("subtype")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListNotificationConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationConfigurationStructure:
    boto3_raw_data: "type_defs.NotificationConfigurationStructureTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    description = field("description")
    status = field("status")
    creationTime = field("creationTime")
    aggregationDuration = field("aggregationDuration")
    subtype = field("subtype")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.NotificationConfigurationStructureTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationConfigurationStructureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationHubsRequest:
    boto3_raw_data: "type_defs.ListNotificationHubsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotificationHubsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationHubsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationalUnitsRequest:
    boto3_raw_data: "type_defs.ListOrganizationalUnitsRequestTypeDef" = (
        dataclasses.field()
    )

    notificationConfigurationArn = field("notificationConfigurationArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOrganizationalUnitsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationalUnitsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedSourceEventMetadataSummary:
    boto3_raw_data: "type_defs.ManagedSourceEventMetadataSummaryTypeDef" = (
        dataclasses.field()
    )

    source = field("source")
    eventType = field("eventType")
    eventOriginRegion = field("eventOriginRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManagedSourceEventMetadataSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedSourceEventMetadataSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageComponentsSummary:
    boto3_raw_data: "type_defs.MessageComponentsSummaryTypeDef" = dataclasses.field()

    headline = field("headline")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageComponentsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageComponentsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextPartValue:
    boto3_raw_data: "type_defs.TextPartValueTypeDef" = dataclasses.field()

    type = field("type")
    displayText = field("displayText")
    textByLocale = field("textByLocale")
    url = field("url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextPartValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextPartValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaElement:
    boto3_raw_data: "type_defs.MediaElementTypeDef" = dataclasses.field()

    mediaId = field("mediaId")
    type = field("type")
    url = field("url")
    caption = field("caption")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MediaElementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MediaElementTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceEventMetadataSummary:
    boto3_raw_data: "type_defs.SourceEventMetadataSummaryTypeDef" = dataclasses.field()

    source = field("source")
    eventType = field("eventType")
    eventOriginRegion = field("eventOriginRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceEventMetadataSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceEventMetadataSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterNotificationHubRequest:
    boto3_raw_data: "type_defs.RegisterNotificationHubRequestTypeDef" = (
        dataclasses.field()
    )

    notificationHubRegion = field("notificationHubRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterNotificationHubRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterNotificationHubRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    detailUrl = field("detailUrl")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    arn = field("arn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    arn = field("arn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventRuleRequest:
    boto3_raw_data: "type_defs.UpdateEventRuleRequestTypeDef" = dataclasses.field()

    arn = field("arn")
    eventPattern = field("eventPattern")
    regions = field("regions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNotificationConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateNotificationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    description = field("description")
    aggregationDuration = field("aggregationDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateNotificationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNotificationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregationDetail:
    boto3_raw_data: "type_defs.AggregationDetailTypeDef" = dataclasses.field()

    @cached_property
    def summarizationDimensions(self):  # pragma: no cover
        return SummarizationDimensionDetail.make_many(
            self.boto3_raw_data["summarizationDimensions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AggregationDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregationSummary:
    boto3_raw_data: "type_defs.AggregationSummaryTypeDef" = dataclasses.field()

    eventCount = field("eventCount")

    @cached_property
    def aggregatedBy(self):  # pragma: no cover
        return AggregationKey.make_many(self.boto3_raw_data["aggregatedBy"])

    @cached_property
    def aggregatedAccounts(self):  # pragma: no cover
        return SummarizationDimensionOverview.make_one(
            self.boto3_raw_data["aggregatedAccounts"]
        )

    @cached_property
    def aggregatedRegions(self):  # pragma: no cover
        return SummarizationDimensionOverview.make_one(
            self.boto3_raw_data["aggregatedRegions"]
        )

    @cached_property
    def aggregatedOrganizationalUnits(self):  # pragma: no cover
        return SummarizationDimensionOverview.make_one(
            self.boto3_raw_data["aggregatedOrganizationalUnits"]
        )

    @cached_property
    def additionalSummarizationDimensions(self):  # pragma: no cover
        return SummarizationDimensionOverview.make_many(
            self.boto3_raw_data["additionalSummarizationDimensions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventRuleStructure:
    boto3_raw_data: "type_defs.EventRuleStructureTypeDef" = dataclasses.field()

    arn = field("arn")
    notificationConfigurationArn = field("notificationConfigurationArn")
    creationTime = field("creationTime")
    source = field("source")
    eventType = field("eventType")
    eventPattern = field("eventPattern")
    regions = field("regions")
    managedRules = field("managedRules")
    statusSummaryByRegion = field("statusSummaryByRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventRuleStructureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventRuleStructureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventRuleResponse:
    boto3_raw_data: "type_defs.CreateEventRuleResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    notificationConfigurationArn = field("notificationConfigurationArn")
    statusSummaryByRegion = field("statusSummaryByRegion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNotificationConfigurationResponse:
    boto3_raw_data: "type_defs.CreateNotificationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateNotificationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNotificationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventRuleResponse:
    boto3_raw_data: "type_defs.GetEventRuleResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    notificationConfigurationArn = field("notificationConfigurationArn")
    creationTime = field("creationTime")
    source = field("source")
    eventType = field("eventType")
    eventPattern = field("eventPattern")
    regions = field("regions")
    managedRules = field("managedRules")
    statusSummaryByRegion = field("statusSummaryByRegion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedNotificationConfigurationResponse:
    boto3_raw_data: "type_defs.GetManagedNotificationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    description = field("description")
    category = field("category")
    subCategory = field("subCategory")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetManagedNotificationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedNotificationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNotificationConfigurationResponse:
    boto3_raw_data: "type_defs.GetNotificationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    description = field("description")
    status = field("status")
    creationTime = field("creationTime")
    aggregationDuration = field("aggregationDuration")
    subtype = field("subtype")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNotificationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNotificationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsResponse:
    boto3_raw_data: "type_defs.ListChannelsResponseTypeDef" = dataclasses.field()

    channels = field("channels")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationalUnitsResponse:
    boto3_raw_data: "type_defs.ListOrganizationalUnitsResponseTypeDef" = (
        dataclasses.field()
    )

    organizationalUnits = field("organizationalUnits")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOrganizationalUnitsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationalUnitsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventRuleResponse:
    boto3_raw_data: "type_defs.UpdateEventRuleResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    notificationConfigurationArn = field("notificationConfigurationArn")
    statusSummaryByRegion = field("statusSummaryByRegion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNotificationConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateNotificationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateNotificationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNotificationConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterNotificationHubResponse:
    boto3_raw_data: "type_defs.DeregisterNotificationHubResponseTypeDef" = (
        dataclasses.field()
    )

    notificationHubRegion = field("notificationHubRegion")

    @cached_property
    def statusSummary(self):  # pragma: no cover
        return NotificationHubStatusSummary.make_one(
            self.boto3_raw_data["statusSummary"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterNotificationHubResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterNotificationHubResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationHubOverview:
    boto3_raw_data: "type_defs.NotificationHubOverviewTypeDef" = dataclasses.field()

    notificationHubRegion = field("notificationHubRegion")

    @cached_property
    def statusSummary(self):  # pragma: no cover
        return NotificationHubStatusSummary.make_one(
            self.boto3_raw_data["statusSummary"]
        )

    creationTime = field("creationTime")
    lastActivationTime = field("lastActivationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationHubOverviewTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationHubOverviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterNotificationHubResponse:
    boto3_raw_data: "type_defs.RegisterNotificationHubResponseTypeDef" = (
        dataclasses.field()
    )

    notificationHubRegion = field("notificationHubRegion")

    @cached_property
    def statusSummary(self):  # pragma: no cover
        return NotificationHubStatusSummary.make_one(
            self.boto3_raw_data["statusSummary"]
        )

    creationTime = field("creationTime")
    lastActivationTime = field("lastActivationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterNotificationHubResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterNotificationHubResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageComponents:
    boto3_raw_data: "type_defs.MessageComponentsTypeDef" = dataclasses.field()

    headline = field("headline")
    paragraphSummary = field("paragraphSummary")
    completeDescription = field("completeDescription")

    @cached_property
    def dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["dimensions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageComponentsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageComponentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNotificationsAccessForOrganizationResponse:
    boto3_raw_data: "type_defs.GetNotificationsAccessForOrganizationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def notificationsAccessForOrganization(self):  # pragma: no cover
        return NotificationsAccessForOrganization.make_one(
            self.boto3_raw_data["notificationsAccessForOrganization"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNotificationsAccessForOrganizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNotificationsAccessForOrganizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsRequestPaginate:
    boto3_raw_data: "type_defs.ListChannelsRequestPaginateTypeDef" = dataclasses.field()

    notificationConfigurationArn = field("notificationConfigurationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListEventRulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    notificationConfigurationArn = field("notificationConfigurationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventRulesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationChannelAssociationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListManagedNotificationChannelAssociationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    managedNotificationConfigurationArn = field("managedNotificationConfigurationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationChannelAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListManagedNotificationChannelAssociationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationConfigurationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListManagedNotificationConfigurationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    channelIdentifier = field("channelIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListManagedNotificationConfigurationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemberAccountsRequestPaginate:
    boto3_raw_data: "type_defs.ListMemberAccountsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    notificationConfigurationArn = field("notificationConfigurationArn")
    memberAccount = field("memberAccount")
    status = field("status")
    organizationalUnitId = field("organizationalUnitId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMemberAccountsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemberAccountsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListNotificationConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    eventRuleSource = field("eventRuleSource")
    channelArn = field("channelArn")
    status = field("status")
    subtype = field("subtype")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListNotificationConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationHubsRequestPaginate:
    boto3_raw_data: "type_defs.ListNotificationHubsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListNotificationHubsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationHubsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationalUnitsRequestPaginate:
    boto3_raw_data: "type_defs.ListOrganizationalUnitsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    notificationConfigurationArn = field("notificationConfigurationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationalUnitsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationalUnitsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationChannelAssociationsResponse:
    boto3_raw_data: (
        "type_defs.ListManagedNotificationChannelAssociationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def channelAssociations(self):  # pragma: no cover
        return ManagedNotificationChannelAssociationSummary.make_many(
            self.boto3_raw_data["channelAssociations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationChannelAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListManagedNotificationChannelAssociationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationChildEventsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListManagedNotificationChildEventsRequestPaginateTypeDef"
    ) = dataclasses.field()

    aggregateManagedNotificationEventArn = field("aggregateManagedNotificationEventArn")
    startTime = field("startTime")
    endTime = field("endTime")
    locale = field("locale")
    relatedAccount = field("relatedAccount")
    organizationalUnitId = field("organizationalUnitId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationChildEventsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListManagedNotificationChildEventsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationChildEventsRequest:
    boto3_raw_data: "type_defs.ListManagedNotificationChildEventsRequestTypeDef" = (
        dataclasses.field()
    )

    aggregateManagedNotificationEventArn = field("aggregateManagedNotificationEventArn")
    startTime = field("startTime")
    endTime = field("endTime")
    locale = field("locale")
    maxResults = field("maxResults")
    relatedAccount = field("relatedAccount")
    organizationalUnitId = field("organizationalUnitId")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationChildEventsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedNotificationChildEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationEventsRequestPaginate:
    boto3_raw_data: "type_defs.ListManagedNotificationEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")
    locale = field("locale")
    source = field("source")
    organizationalUnitId = field("organizationalUnitId")
    relatedAccount = field("relatedAccount")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationEventsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedNotificationEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationEventsRequest:
    boto3_raw_data: "type_defs.ListManagedNotificationEventsRequestTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")
    locale = field("locale")
    source = field("source")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    organizationalUnitId = field("organizationalUnitId")
    relatedAccount = field("relatedAccount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationEventsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedNotificationEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationEventsRequestPaginate:
    boto3_raw_data: "type_defs.ListNotificationEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")
    locale = field("locale")
    source = field("source")
    includeChildEvents = field("includeChildEvents")
    aggregateNotificationEventArn = field("aggregateNotificationEventArn")
    organizationalUnitId = field("organizationalUnitId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListNotificationEventsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationEventsRequest:
    boto3_raw_data: "type_defs.ListNotificationEventsRequestTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")
    locale = field("locale")
    source = field("source")
    includeChildEvents = field("includeChildEvents")
    aggregateNotificationEventArn = field("aggregateNotificationEventArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    organizationalUnitId = field("organizationalUnitId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNotificationEventsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationConfigurationsResponse:
    boto3_raw_data: "type_defs.ListManagedNotificationConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def managedNotificationConfigurations(self):  # pragma: no cover
        return ManagedNotificationConfigurationStructure.make_many(
            self.boto3_raw_data["managedNotificationConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedNotificationConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMemberAccountsResponse:
    boto3_raw_data: "type_defs.ListMemberAccountsResponseTypeDef" = dataclasses.field()

    @cached_property
    def memberAccounts(self):  # pragma: no cover
        return MemberAccount.make_many(self.boto3_raw_data["memberAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMemberAccountsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMemberAccountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationConfigurationsResponse:
    boto3_raw_data: "type_defs.ListNotificationConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def notificationConfigurations(self):  # pragma: no cover
        return NotificationConfigurationStructure.make_many(
            self.boto3_raw_data["notificationConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListNotificationConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedNotificationEventSummary:
    boto3_raw_data: "type_defs.ManagedNotificationEventSummaryTypeDef" = (
        dataclasses.field()
    )

    schemaVersion = field("schemaVersion")

    @cached_property
    def sourceEventMetadata(self):  # pragma: no cover
        return ManagedSourceEventMetadataSummary.make_one(
            self.boto3_raw_data["sourceEventMetadata"]
        )

    @cached_property
    def messageComponents(self):  # pragma: no cover
        return MessageComponentsSummary.make_one(
            self.boto3_raw_data["messageComponents"]
        )

    eventStatus = field("eventStatus")
    notificationType = field("notificationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ManagedNotificationEventSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedNotificationEventSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationEventSummary:
    boto3_raw_data: "type_defs.NotificationEventSummaryTypeDef" = dataclasses.field()

    schemaVersion = field("schemaVersion")

    @cached_property
    def sourceEventMetadata(self):  # pragma: no cover
        return SourceEventMetadataSummary.make_one(
            self.boto3_raw_data["sourceEventMetadata"]
        )

    @cached_property
    def messageComponents(self):  # pragma: no cover
        return MessageComponentsSummary.make_one(
            self.boto3_raw_data["messageComponents"]
        )

    eventStatus = field("eventStatus")
    notificationType = field("notificationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationEventSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationEventSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceEventMetadata:
    boto3_raw_data: "type_defs.SourceEventMetadataTypeDef" = dataclasses.field()

    eventTypeVersion = field("eventTypeVersion")
    sourceEventId = field("sourceEventId")
    relatedAccount = field("relatedAccount")
    source = field("source")
    eventOccurrenceTime = field("eventOccurrenceTime")
    eventType = field("eventType")

    @cached_property
    def relatedResources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["relatedResources"])

    eventOriginRegion = field("eventOriginRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceEventMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceEventMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedNotificationChildEventSummary:
    boto3_raw_data: "type_defs.ManagedNotificationChildEventSummaryTypeDef" = (
        dataclasses.field()
    )

    schemaVersion = field("schemaVersion")

    @cached_property
    def sourceEventMetadata(self):  # pragma: no cover
        return ManagedSourceEventMetadataSummary.make_one(
            self.boto3_raw_data["sourceEventMetadata"]
        )

    @cached_property
    def messageComponents(self):  # pragma: no cover
        return MessageComponentsSummary.make_one(
            self.boto3_raw_data["messageComponents"]
        )

    @cached_property
    def aggregationDetail(self):  # pragma: no cover
        return AggregationDetail.make_one(self.boto3_raw_data["aggregationDetail"])

    eventStatus = field("eventStatus")
    notificationType = field("notificationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManagedNotificationChildEventSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedNotificationChildEventSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventRulesResponse:
    boto3_raw_data: "type_defs.ListEventRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def eventRules(self):  # pragma: no cover
        return EventRuleStructure.make_many(self.boto3_raw_data["eventRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventRulesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationHubsResponse:
    boto3_raw_data: "type_defs.ListNotificationHubsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def notificationHubs(self):  # pragma: no cover
        return NotificationHubOverview.make_many(
            self.boto3_raw_data["notificationHubs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotificationHubsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationHubsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedNotificationChildEvent:
    boto3_raw_data: "type_defs.ManagedNotificationChildEventTypeDef" = (
        dataclasses.field()
    )

    schemaVersion = field("schemaVersion")
    id = field("id")

    @cached_property
    def messageComponents(self):  # pragma: no cover
        return MessageComponents.make_one(self.boto3_raw_data["messageComponents"])

    notificationType = field("notificationType")
    aggregateManagedNotificationEventArn = field("aggregateManagedNotificationEventArn")
    textParts = field("textParts")
    sourceEventDetailUrl = field("sourceEventDetailUrl")
    sourceEventDetailUrlDisplayText = field("sourceEventDetailUrlDisplayText")
    eventStatus = field("eventStatus")
    startTime = field("startTime")
    endTime = field("endTime")
    organizationalUnitId = field("organizationalUnitId")

    @cached_property
    def aggregationDetail(self):  # pragma: no cover
        return AggregationDetail.make_one(self.boto3_raw_data["aggregationDetail"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ManagedNotificationChildEventTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedNotificationChildEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedNotificationEvent:
    boto3_raw_data: "type_defs.ManagedNotificationEventTypeDef" = dataclasses.field()

    schemaVersion = field("schemaVersion")
    id = field("id")

    @cached_property
    def messageComponents(self):  # pragma: no cover
        return MessageComponents.make_one(self.boto3_raw_data["messageComponents"])

    notificationType = field("notificationType")
    textParts = field("textParts")
    sourceEventDetailUrl = field("sourceEventDetailUrl")
    sourceEventDetailUrlDisplayText = field("sourceEventDetailUrlDisplayText")
    eventStatus = field("eventStatus")
    aggregationEventType = field("aggregationEventType")

    @cached_property
    def aggregationSummary(self):  # pragma: no cover
        return AggregationSummary.make_one(self.boto3_raw_data["aggregationSummary"])

    startTime = field("startTime")
    endTime = field("endTime")
    organizationalUnitId = field("organizationalUnitId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedNotificationEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedNotificationEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedNotificationEventOverview:
    boto3_raw_data: "type_defs.ManagedNotificationEventOverviewTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    managedNotificationConfigurationArn = field("managedNotificationConfigurationArn")
    relatedAccount = field("relatedAccount")
    creationTime = field("creationTime")

    @cached_property
    def notificationEvent(self):  # pragma: no cover
        return ManagedNotificationEventSummary.make_one(
            self.boto3_raw_data["notificationEvent"]
        )

    aggregationEventType = field("aggregationEventType")
    organizationalUnitId = field("organizationalUnitId")

    @cached_property
    def aggregationSummary(self):  # pragma: no cover
        return AggregationSummary.make_one(self.boto3_raw_data["aggregationSummary"])

    aggregatedNotificationRegions = field("aggregatedNotificationRegions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ManagedNotificationEventOverviewTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedNotificationEventOverviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationEventOverview:
    boto3_raw_data: "type_defs.NotificationEventOverviewTypeDef" = dataclasses.field()

    arn = field("arn")
    notificationConfigurationArn = field("notificationConfigurationArn")
    relatedAccount = field("relatedAccount")
    creationTime = field("creationTime")

    @cached_property
    def notificationEvent(self):  # pragma: no cover
        return NotificationEventSummary.make_one(
            self.boto3_raw_data["notificationEvent"]
        )

    aggregationEventType = field("aggregationEventType")
    aggregateNotificationEventArn = field("aggregateNotificationEventArn")

    @cached_property
    def aggregationSummary(self):  # pragma: no cover
        return AggregationSummary.make_one(self.boto3_raw_data["aggregationSummary"])

    organizationalUnitId = field("organizationalUnitId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationEventOverviewTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationEventOverviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationEvent:
    boto3_raw_data: "type_defs.NotificationEventTypeDef" = dataclasses.field()

    schemaVersion = field("schemaVersion")
    id = field("id")

    @cached_property
    def sourceEventMetadata(self):  # pragma: no cover
        return SourceEventMetadata.make_one(self.boto3_raw_data["sourceEventMetadata"])

    @cached_property
    def messageComponents(self):  # pragma: no cover
        return MessageComponents.make_one(self.boto3_raw_data["messageComponents"])

    notificationType = field("notificationType")
    textParts = field("textParts")

    @cached_property
    def media(self):  # pragma: no cover
        return MediaElement.make_many(self.boto3_raw_data["media"])

    sourceEventDetailUrl = field("sourceEventDetailUrl")
    sourceEventDetailUrlDisplayText = field("sourceEventDetailUrlDisplayText")
    eventStatus = field("eventStatus")
    aggregationEventType = field("aggregationEventType")
    aggregateNotificationEventArn = field("aggregateNotificationEventArn")

    @cached_property
    def aggregationSummary(self):  # pragma: no cover
        return AggregationSummary.make_one(self.boto3_raw_data["aggregationSummary"])

    startTime = field("startTime")
    endTime = field("endTime")
    organizationalUnitId = field("organizationalUnitId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NotificationEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedNotificationChildEventOverview:
    boto3_raw_data: "type_defs.ManagedNotificationChildEventOverviewTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    managedNotificationConfigurationArn = field("managedNotificationConfigurationArn")
    relatedAccount = field("relatedAccount")
    creationTime = field("creationTime")

    @cached_property
    def childEvent(self):  # pragma: no cover
        return ManagedNotificationChildEventSummary.make_one(
            self.boto3_raw_data["childEvent"]
        )

    aggregateManagedNotificationEventArn = field("aggregateManagedNotificationEventArn")
    organizationalUnitId = field("organizationalUnitId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ManagedNotificationChildEventOverviewTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedNotificationChildEventOverviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedNotificationChildEventResponse:
    boto3_raw_data: "type_defs.GetManagedNotificationChildEventResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    managedNotificationConfigurationArn = field("managedNotificationConfigurationArn")
    creationTime = field("creationTime")

    @cached_property
    def content(self):  # pragma: no cover
        return ManagedNotificationChildEvent.make_one(self.boto3_raw_data["content"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetManagedNotificationChildEventResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedNotificationChildEventResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedNotificationEventResponse:
    boto3_raw_data: "type_defs.GetManagedNotificationEventResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    managedNotificationConfigurationArn = field("managedNotificationConfigurationArn")
    creationTime = field("creationTime")

    @cached_property
    def content(self):  # pragma: no cover
        return ManagedNotificationEvent.make_one(self.boto3_raw_data["content"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetManagedNotificationEventResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedNotificationEventResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationEventsResponse:
    boto3_raw_data: "type_defs.ListManagedNotificationEventsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def managedNotificationEvents(self):  # pragma: no cover
        return ManagedNotificationEventOverview.make_many(
            self.boto3_raw_data["managedNotificationEvents"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationEventsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedNotificationEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationEventsResponse:
    boto3_raw_data: "type_defs.ListNotificationEventsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def notificationEvents(self):  # pragma: no cover
        return NotificationEventOverview.make_many(
            self.boto3_raw_data["notificationEvents"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNotificationEventsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNotificationEventResponse:
    boto3_raw_data: "type_defs.GetNotificationEventResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    notificationConfigurationArn = field("notificationConfigurationArn")
    creationTime = field("creationTime")

    @cached_property
    def content(self):  # pragma: no cover
        return NotificationEvent.make_one(self.boto3_raw_data["content"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetNotificationEventResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNotificationEventResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedNotificationChildEventsResponse:
    boto3_raw_data: "type_defs.ListManagedNotificationChildEventsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def managedNotificationChildEvents(self):  # pragma: no cover
        return ManagedNotificationChildEventOverview.make_many(
            self.boto3_raw_data["managedNotificationChildEvents"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedNotificationChildEventsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedNotificationChildEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
