# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ssm_contacts import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptPageRequest:
    boto3_raw_data: "type_defs.AcceptPageRequestTypeDef" = dataclasses.field()

    PageId = field("PageId")
    AcceptType = field("AcceptType")
    AcceptCode = field("AcceptCode")
    ContactChannelId = field("ContactChannelId")
    Note = field("Note")
    AcceptCodeValidation = field("AcceptCodeValidation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AcceptPageRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptPageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateContactChannelRequest:
    boto3_raw_data: "type_defs.ActivateContactChannelRequestTypeDef" = (
        dataclasses.field()
    )

    ContactChannelId = field("ContactChannelId")
    ActivationCode = field("ActivationCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActivateContactChannelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateContactChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChannelTargetInfo:
    boto3_raw_data: "type_defs.ChannelTargetInfoTypeDef" = dataclasses.field()

    ContactChannelId = field("ContactChannelId")
    RetryIntervalInMinutes = field("RetryIntervalInMinutes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelTargetInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChannelTargetInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactChannelAddress:
    boto3_raw_data: "type_defs.ContactChannelAddressTypeDef" = dataclasses.field()

    SimpleAddress = field("SimpleAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContactChannelAddressTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactChannelAddressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactTargetInfo:
    boto3_raw_data: "type_defs.ContactTargetInfoTypeDef" = dataclasses.field()

    IsEssential = field("IsEssential")
    ContactId = field("ContactId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactTargetInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactTargetInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Contact:
    boto3_raw_data: "type_defs.ContactTypeDef" = dataclasses.field()

    ContactArn = field("ContactArn")
    Alias = field("Alias")
    Type = field("Type")
    DisplayName = field("DisplayName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HandOffTime:
    boto3_raw_data: "type_defs.HandOffTimeTypeDef" = dataclasses.field()

    HourOfDay = field("HourOfDay")
    MinuteOfHour = field("MinuteOfHour")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HandOffTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HandOffTimeTypeDef"]]
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
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateContactChannelRequest:
    boto3_raw_data: "type_defs.DeactivateContactChannelRequestTypeDef" = (
        dataclasses.field()
    )

    ContactChannelId = field("ContactChannelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeactivateContactChannelRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateContactChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContactChannelRequest:
    boto3_raw_data: "type_defs.DeleteContactChannelRequestTypeDef" = dataclasses.field()

    ContactChannelId = field("ContactChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteContactChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContactChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteContactRequest:
    boto3_raw_data: "type_defs.DeleteContactRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRotationOverrideRequest:
    boto3_raw_data: "type_defs.DeleteRotationOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    RotationId = field("RotationId")
    RotationOverrideId = field("RotationOverrideId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteRotationOverrideRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRotationOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRotationRequest:
    boto3_raw_data: "type_defs.DeleteRotationRequestTypeDef" = dataclasses.field()

    RotationId = field("RotationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRotationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRotationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngagementRequest:
    boto3_raw_data: "type_defs.DescribeEngagementRequestTypeDef" = dataclasses.field()

    EngagementId = field("EngagementId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEngagementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngagementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePageRequest:
    boto3_raw_data: "type_defs.DescribePageRequestTypeDef" = dataclasses.field()

    PageId = field("PageId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Engagement:
    boto3_raw_data: "type_defs.EngagementTypeDef" = dataclasses.field()

    EngagementArn = field("EngagementArn")
    ContactArn = field("ContactArn")
    Sender = field("Sender")
    IncidentId = field("IncidentId")
    StartTime = field("StartTime")
    StopTime = field("StopTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EngagementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EngagementTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactChannelRequest:
    boto3_raw_data: "type_defs.GetContactChannelRequestTypeDef" = dataclasses.field()

    ContactChannelId = field("ContactChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactPolicyRequest:
    boto3_raw_data: "type_defs.GetContactPolicyRequestTypeDef" = dataclasses.field()

    ContactArn = field("ContactArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactRequest:
    boto3_raw_data: "type_defs.GetContactRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetContactRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRotationOverrideRequest:
    boto3_raw_data: "type_defs.GetRotationOverrideRequestTypeDef" = dataclasses.field()

    RotationId = field("RotationId")
    RotationOverrideId = field("RotationOverrideId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRotationOverrideRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRotationOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRotationRequest:
    boto3_raw_data: "type_defs.GetRotationRequestTypeDef" = dataclasses.field()

    RotationId = field("RotationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRotationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRotationRequestTypeDef"]
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
class ListContactChannelsRequest:
    boto3_raw_data: "type_defs.ListContactChannelsRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactsRequest:
    boto3_raw_data: "type_defs.ListContactsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    AliasPrefix = field("AliasPrefix")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPageReceiptsRequest:
    boto3_raw_data: "type_defs.ListPageReceiptsRequestTypeDef" = dataclasses.field()

    PageId = field("PageId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPageReceiptsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPageReceiptsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Receipt:
    boto3_raw_data: "type_defs.ReceiptTypeDef" = dataclasses.field()

    ReceiptType = field("ReceiptType")
    ReceiptTime = field("ReceiptTime")
    ContactChannelArn = field("ContactChannelArn")
    ReceiptInfo = field("ReceiptInfo")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReceiptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReceiptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPageResolutionsRequest:
    boto3_raw_data: "type_defs.ListPageResolutionsRequestTypeDef" = dataclasses.field()

    PageId = field("PageId")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPageResolutionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPageResolutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolutionContact:
    boto3_raw_data: "type_defs.ResolutionContactTypeDef" = dataclasses.field()

    ContactArn = field("ContactArn")
    Type = field("Type")
    StageIndex = field("StageIndex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResolutionContactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResolutionContactTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPagesByContactRequest:
    boto3_raw_data: "type_defs.ListPagesByContactRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPagesByContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPagesByContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Page:
    boto3_raw_data: "type_defs.PageTypeDef" = dataclasses.field()

    PageArn = field("PageArn")
    EngagementArn = field("EngagementArn")
    ContactArn = field("ContactArn")
    Sender = field("Sender")
    IncidentId = field("IncidentId")
    SentTime = field("SentTime")
    DeliveryTime = field("DeliveryTime")
    ReadTime = field("ReadTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPagesByEngagementRequest:
    boto3_raw_data: "type_defs.ListPagesByEngagementRequestTypeDef" = (
        dataclasses.field()
    )

    EngagementId = field("EngagementId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPagesByEngagementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPagesByEngagementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RotationOverride:
    boto3_raw_data: "type_defs.RotationOverrideTypeDef" = dataclasses.field()

    RotationOverrideId = field("RotationOverrideId")
    NewContactIds = field("NewContactIds")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    CreateTime = field("CreateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RotationOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RotationOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRotationsRequest:
    boto3_raw_data: "type_defs.ListRotationsRequestTypeDef" = dataclasses.field()

    RotationNamePrefix = field("RotationNamePrefix")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRotationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRotationsRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class PutContactPolicyRequest:
    boto3_raw_data: "type_defs.PutContactPolicyRequestTypeDef" = dataclasses.field()

    ContactArn = field("ContactArn")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutContactPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutContactPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShiftDetails:
    boto3_raw_data: "type_defs.ShiftDetailsTypeDef" = dataclasses.field()

    OverriddenContactIds = field("OverriddenContactIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShiftDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShiftDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendActivationCodeRequest:
    boto3_raw_data: "type_defs.SendActivationCodeRequestTypeDef" = dataclasses.field()

    ContactChannelId = field("ContactChannelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SendActivationCodeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendActivationCodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEngagementRequest:
    boto3_raw_data: "type_defs.StartEngagementRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    Sender = field("Sender")
    Subject = field("Subject")
    Content = field("Content")
    PublicSubject = field("PublicSubject")
    PublicContent = field("PublicContent")
    IncidentId = field("IncidentId")
    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartEngagementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEngagementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopEngagementRequest:
    boto3_raw_data: "type_defs.StopEngagementRequestTypeDef" = dataclasses.field()

    EngagementId = field("EngagementId")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopEngagementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopEngagementRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")
    TagKeys = field("TagKeys")

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
class ContactChannel:
    boto3_raw_data: "type_defs.ContactChannelTypeDef" = dataclasses.field()

    ContactChannelArn = field("ContactChannelArn")
    ContactArn = field("ContactArn")
    Name = field("Name")

    @cached_property
    def DeliveryAddress(self):  # pragma: no cover
        return ContactChannelAddress.make_one(self.boto3_raw_data["DeliveryAddress"])

    ActivationStatus = field("ActivationStatus")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactChannelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactChannelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactChannelRequest:
    boto3_raw_data: "type_defs.CreateContactChannelRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    Name = field("Name")
    Type = field("Type")

    @cached_property
    def DeliveryAddress(self):  # pragma: no cover
        return ContactChannelAddress.make_one(self.boto3_raw_data["DeliveryAddress"])

    DeferActivation = field("DeferActivation")
    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactChannelRequest:
    boto3_raw_data: "type_defs.UpdateContactChannelRequestTypeDef" = dataclasses.field()

    ContactChannelId = field("ContactChannelId")
    Name = field("Name")

    @cached_property
    def DeliveryAddress(self):  # pragma: no cover
        return ContactChannelAddress.make_one(self.boto3_raw_data["DeliveryAddress"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContactChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Target:
    boto3_raw_data: "type_defs.TargetTypeDef" = dataclasses.field()

    @cached_property
    def ChannelTargetInfo(self):  # pragma: no cover
        return ChannelTargetInfo.make_one(self.boto3_raw_data["ChannelTargetInfo"])

    @cached_property
    def ContactTargetInfo(self):  # pragma: no cover
        return ContactTargetInfo.make_one(self.boto3_raw_data["ContactTargetInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CoverageTime:
    boto3_raw_data: "type_defs.CoverageTimeTypeDef" = dataclasses.field()

    @cached_property
    def Start(self):  # pragma: no cover
        return HandOffTime.make_one(self.boto3_raw_data["Start"])

    @cached_property
    def End(self):  # pragma: no cover
        return HandOffTime.make_one(self.boto3_raw_data["End"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoverageTimeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoverageTimeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonthlySetting:
    boto3_raw_data: "type_defs.MonthlySettingTypeDef" = dataclasses.field()

    DayOfMonth = field("DayOfMonth")

    @cached_property
    def HandOffTime(self):  # pragma: no cover
        return HandOffTime.make_one(self.boto3_raw_data["HandOffTime"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonthlySettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonthlySettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WeeklySetting:
    boto3_raw_data: "type_defs.WeeklySettingTypeDef" = dataclasses.field()

    DayOfWeek = field("DayOfWeek")

    @cached_property
    def HandOffTime(self):  # pragma: no cover
        return HandOffTime.make_one(self.boto3_raw_data["HandOffTime"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WeeklySettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WeeklySettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactChannelResult:
    boto3_raw_data: "type_defs.CreateContactChannelResultTypeDef" = dataclasses.field()

    ContactChannelArn = field("ContactChannelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactChannelResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactChannelResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactResult:
    boto3_raw_data: "type_defs.CreateContactResultTypeDef" = dataclasses.field()

    ContactArn = field("ContactArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRotationOverrideResult:
    boto3_raw_data: "type_defs.CreateRotationOverrideResultTypeDef" = (
        dataclasses.field()
    )

    RotationOverrideId = field("RotationOverrideId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRotationOverrideResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRotationOverrideResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRotationResult:
    boto3_raw_data: "type_defs.CreateRotationResultTypeDef" = dataclasses.field()

    RotationArn = field("RotationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRotationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRotationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngagementResult:
    boto3_raw_data: "type_defs.DescribeEngagementResultTypeDef" = dataclasses.field()

    ContactArn = field("ContactArn")
    EngagementArn = field("EngagementArn")
    Sender = field("Sender")
    Subject = field("Subject")
    Content = field("Content")
    PublicSubject = field("PublicSubject")
    PublicContent = field("PublicContent")
    IncidentId = field("IncidentId")
    StartTime = field("StartTime")
    StopTime = field("StopTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEngagementResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngagementResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePageResult:
    boto3_raw_data: "type_defs.DescribePageResultTypeDef" = dataclasses.field()

    PageArn = field("PageArn")
    EngagementArn = field("EngagementArn")
    ContactArn = field("ContactArn")
    Sender = field("Sender")
    Subject = field("Subject")
    Content = field("Content")
    PublicSubject = field("PublicSubject")
    PublicContent = field("PublicContent")
    IncidentId = field("IncidentId")
    SentTime = field("SentTime")
    ReadTime = field("ReadTime")
    DeliveryTime = field("DeliveryTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactChannelResult:
    boto3_raw_data: "type_defs.GetContactChannelResultTypeDef" = dataclasses.field()

    ContactArn = field("ContactArn")
    ContactChannelArn = field("ContactChannelArn")
    Name = field("Name")
    Type = field("Type")

    @cached_property
    def DeliveryAddress(self):  # pragma: no cover
        return ContactChannelAddress.make_one(self.boto3_raw_data["DeliveryAddress"])

    ActivationStatus = field("ActivationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactChannelResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactChannelResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactPolicyResult:
    boto3_raw_data: "type_defs.GetContactPolicyResultTypeDef" = dataclasses.field()

    ContactArn = field("ContactArn")
    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetContactPolicyResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactPolicyResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRotationOverrideResult:
    boto3_raw_data: "type_defs.GetRotationOverrideResultTypeDef" = dataclasses.field()

    RotationOverrideId = field("RotationOverrideId")
    RotationArn = field("RotationArn")
    NewContactIds = field("NewContactIds")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    CreateTime = field("CreateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRotationOverrideResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRotationOverrideResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactsResult:
    boto3_raw_data: "type_defs.ListContactsResultTypeDef" = dataclasses.field()

    @cached_property
    def Contacts(self):  # pragma: no cover
        return Contact.make_many(self.boto3_raw_data["Contacts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEngagementResult:
    boto3_raw_data: "type_defs.StartEngagementResultTypeDef" = dataclasses.field()

    EngagementArn = field("EngagementArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartEngagementResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEngagementResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResult:
    boto3_raw_data: "type_defs.ListTagsForResourceResultTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateRotationOverrideRequest:
    boto3_raw_data: "type_defs.CreateRotationOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    RotationId = field("RotationId")
    NewContactIds = field("NewContactIds")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateRotationOverrideRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRotationOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRotationOverridesRequest:
    boto3_raw_data: "type_defs.ListRotationOverridesRequestTypeDef" = (
        dataclasses.field()
    )

    RotationId = field("RotationId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRotationOverridesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRotationOverridesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRotationShiftsRequest:
    boto3_raw_data: "type_defs.ListRotationShiftsRequestTypeDef" = dataclasses.field()

    RotationId = field("RotationId")
    EndTime = field("EndTime")
    StartTime = field("StartTime")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRotationShiftsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRotationShiftsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreviewOverride:
    boto3_raw_data: "type_defs.PreviewOverrideTypeDef" = dataclasses.field()

    NewMembers = field("NewMembers")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PreviewOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PreviewOverrideTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeRange:
    boto3_raw_data: "type_defs.TimeRangeTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementsResult:
    boto3_raw_data: "type_defs.ListEngagementsResultTypeDef" = dataclasses.field()

    @cached_property
    def Engagements(self):  # pragma: no cover
        return Engagement.make_many(self.boto3_raw_data["Engagements"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEngagementsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactChannelsRequestPaginate:
    boto3_raw_data: "type_defs.ListContactChannelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ContactId = field("ContactId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListContactChannelsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactChannelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactsRequestPaginate:
    boto3_raw_data: "type_defs.ListContactsRequestPaginateTypeDef" = dataclasses.field()

    AliasPrefix = field("AliasPrefix")
    Type = field("Type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPageReceiptsRequestPaginate:
    boto3_raw_data: "type_defs.ListPageReceiptsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PageId = field("PageId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPageReceiptsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPageReceiptsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPageResolutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListPageResolutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PageId = field("PageId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPageResolutionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPageResolutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPagesByContactRequestPaginate:
    boto3_raw_data: "type_defs.ListPagesByContactRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ContactId = field("ContactId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPagesByContactRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPagesByContactRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPagesByEngagementRequestPaginate:
    boto3_raw_data: "type_defs.ListPagesByEngagementRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    EngagementId = field("EngagementId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPagesByEngagementRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPagesByEngagementRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRotationOverridesRequestPaginate:
    boto3_raw_data: "type_defs.ListRotationOverridesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    RotationId = field("RotationId")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRotationOverridesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRotationOverridesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRotationShiftsRequestPaginate:
    boto3_raw_data: "type_defs.ListRotationShiftsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    RotationId = field("RotationId")
    EndTime = field("EndTime")
    StartTime = field("StartTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRotationShiftsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRotationShiftsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRotationsRequestPaginate:
    boto3_raw_data: "type_defs.ListRotationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    RotationNamePrefix = field("RotationNamePrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRotationsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRotationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPageReceiptsResult:
    boto3_raw_data: "type_defs.ListPageReceiptsResultTypeDef" = dataclasses.field()

    @cached_property
    def Receipts(self):  # pragma: no cover
        return Receipt.make_many(self.boto3_raw_data["Receipts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPageReceiptsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPageReceiptsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPageResolutionsResult:
    boto3_raw_data: "type_defs.ListPageResolutionsResultTypeDef" = dataclasses.field()

    @cached_property
    def PageResolutions(self):  # pragma: no cover
        return ResolutionContact.make_many(self.boto3_raw_data["PageResolutions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPageResolutionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPageResolutionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPagesByContactResult:
    boto3_raw_data: "type_defs.ListPagesByContactResultTypeDef" = dataclasses.field()

    @cached_property
    def Pages(self):  # pragma: no cover
        return Page.make_many(self.boto3_raw_data["Pages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPagesByContactResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPagesByContactResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPagesByEngagementResult:
    boto3_raw_data: "type_defs.ListPagesByEngagementResultTypeDef" = dataclasses.field()

    @cached_property
    def Pages(self):  # pragma: no cover
        return Page.make_many(self.boto3_raw_data["Pages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPagesByEngagementResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPagesByEngagementResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRotationOverridesResult:
    boto3_raw_data: "type_defs.ListRotationOverridesResultTypeDef" = dataclasses.field()

    @cached_property
    def RotationOverrides(self):  # pragma: no cover
        return RotationOverride.make_many(self.boto3_raw_data["RotationOverrides"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRotationOverridesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRotationOverridesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RotationShift:
    boto3_raw_data: "type_defs.RotationShiftTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    ContactIds = field("ContactIds")
    Type = field("Type")

    @cached_property
    def ShiftDetails(self):  # pragma: no cover
        return ShiftDetails.make_one(self.boto3_raw_data["ShiftDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RotationShiftTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RotationShiftTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListContactChannelsResult:
    boto3_raw_data: "type_defs.ListContactChannelsResultTypeDef" = dataclasses.field()

    @cached_property
    def ContactChannels(self):  # pragma: no cover
        return ContactChannel.make_many(self.boto3_raw_data["ContactChannels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListContactChannelsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListContactChannelsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StageOutput:
    boto3_raw_data: "type_defs.StageOutputTypeDef" = dataclasses.field()

    DurationInMinutes = field("DurationInMinutes")

    @cached_property
    def Targets(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["Targets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stage:
    boto3_raw_data: "type_defs.StageTypeDef" = dataclasses.field()

    DurationInMinutes = field("DurationInMinutes")

    @cached_property
    def Targets(self):  # pragma: no cover
        return Target.make_many(self.boto3_raw_data["Targets"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurrenceSettingsOutput:
    boto3_raw_data: "type_defs.RecurrenceSettingsOutputTypeDef" = dataclasses.field()

    NumberOfOnCalls = field("NumberOfOnCalls")
    RecurrenceMultiplier = field("RecurrenceMultiplier")

    @cached_property
    def MonthlySettings(self):  # pragma: no cover
        return MonthlySetting.make_many(self.boto3_raw_data["MonthlySettings"])

    @cached_property
    def WeeklySettings(self):  # pragma: no cover
        return WeeklySetting.make_many(self.boto3_raw_data["WeeklySettings"])

    @cached_property
    def DailySettings(self):  # pragma: no cover
        return HandOffTime.make_many(self.boto3_raw_data["DailySettings"])

    ShiftCoverages = field("ShiftCoverages")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecurrenceSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecurrenceSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecurrenceSettings:
    boto3_raw_data: "type_defs.RecurrenceSettingsTypeDef" = dataclasses.field()

    NumberOfOnCalls = field("NumberOfOnCalls")
    RecurrenceMultiplier = field("RecurrenceMultiplier")

    @cached_property
    def MonthlySettings(self):  # pragma: no cover
        return MonthlySetting.make_many(self.boto3_raw_data["MonthlySettings"])

    @cached_property
    def WeeklySettings(self):  # pragma: no cover
        return WeeklySetting.make_many(self.boto3_raw_data["WeeklySettings"])

    @cached_property
    def DailySettings(self):  # pragma: no cover
        return HandOffTime.make_many(self.boto3_raw_data["DailySettings"])

    ShiftCoverages = field("ShiftCoverages")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecurrenceSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecurrenceSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementsRequestPaginate:
    boto3_raw_data: "type_defs.ListEngagementsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    IncidentId = field("IncidentId")

    @cached_property
    def TimeRangeValue(self):  # pragma: no cover
        return TimeRange.make_one(self.boto3_raw_data["TimeRangeValue"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEngagementsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEngagementsRequest:
    boto3_raw_data: "type_defs.ListEngagementsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    IncidentId = field("IncidentId")

    @cached_property
    def TimeRangeValue(self):  # pragma: no cover
        return TimeRange.make_one(self.boto3_raw_data["TimeRangeValue"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEngagementsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEngagementsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPreviewRotationShiftsResult:
    boto3_raw_data: "type_defs.ListPreviewRotationShiftsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RotationShifts(self):  # pragma: no cover
        return RotationShift.make_many(self.boto3_raw_data["RotationShifts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPreviewRotationShiftsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPreviewRotationShiftsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRotationShiftsResult:
    boto3_raw_data: "type_defs.ListRotationShiftsResultTypeDef" = dataclasses.field()

    @cached_property
    def RotationShifts(self):  # pragma: no cover
        return RotationShift.make_many(self.boto3_raw_data["RotationShifts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRotationShiftsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRotationShiftsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlanOutput:
    boto3_raw_data: "type_defs.PlanOutputTypeDef" = dataclasses.field()

    @cached_property
    def Stages(self):  # pragma: no cover
        return StageOutput.make_many(self.boto3_raw_data["Stages"])

    RotationIds = field("RotationIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlanOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlanOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Plan:
    boto3_raw_data: "type_defs.PlanTypeDef" = dataclasses.field()

    @cached_property
    def Stages(self):  # pragma: no cover
        return Stage.make_many(self.boto3_raw_data["Stages"])

    RotationIds = field("RotationIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRotationResult:
    boto3_raw_data: "type_defs.GetRotationResultTypeDef" = dataclasses.field()

    RotationArn = field("RotationArn")
    Name = field("Name")
    ContactIds = field("ContactIds")
    StartTime = field("StartTime")
    TimeZoneId = field("TimeZoneId")

    @cached_property
    def Recurrence(self):  # pragma: no cover
        return RecurrenceSettingsOutput.make_one(self.boto3_raw_data["Recurrence"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRotationResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRotationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rotation:
    boto3_raw_data: "type_defs.RotationTypeDef" = dataclasses.field()

    RotationArn = field("RotationArn")
    Name = field("Name")
    ContactIds = field("ContactIds")
    StartTime = field("StartTime")
    TimeZoneId = field("TimeZoneId")

    @cached_property
    def Recurrence(self):  # pragma: no cover
        return RecurrenceSettingsOutput.make_one(self.boto3_raw_data["Recurrence"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RotationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RotationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetContactResult:
    boto3_raw_data: "type_defs.GetContactResultTypeDef" = dataclasses.field()

    ContactArn = field("ContactArn")
    Alias = field("Alias")
    DisplayName = field("DisplayName")
    Type = field("Type")

    @cached_property
    def Plan(self):  # pragma: no cover
        return PlanOutput.make_one(self.boto3_raw_data["Plan"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetContactResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetContactResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRotationsResult:
    boto3_raw_data: "type_defs.ListRotationsResultTypeDef" = dataclasses.field()

    @cached_property
    def Rotations(self):  # pragma: no cover
        return Rotation.make_many(self.boto3_raw_data["Rotations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRotationsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRotationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRotationRequest:
    boto3_raw_data: "type_defs.CreateRotationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    ContactIds = field("ContactIds")
    TimeZoneId = field("TimeZoneId")
    Recurrence = field("Recurrence")
    StartTime = field("StartTime")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRotationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRotationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPreviewRotationShiftsRequestPaginate:
    boto3_raw_data: "type_defs.ListPreviewRotationShiftsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    EndTime = field("EndTime")
    Members = field("Members")
    TimeZoneId = field("TimeZoneId")
    Recurrence = field("Recurrence")
    RotationStartTime = field("RotationStartTime")
    StartTime = field("StartTime")

    @cached_property
    def Overrides(self):  # pragma: no cover
        return PreviewOverride.make_many(self.boto3_raw_data["Overrides"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPreviewRotationShiftsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPreviewRotationShiftsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPreviewRotationShiftsRequest:
    boto3_raw_data: "type_defs.ListPreviewRotationShiftsRequestTypeDef" = (
        dataclasses.field()
    )

    EndTime = field("EndTime")
    Members = field("Members")
    TimeZoneId = field("TimeZoneId")
    Recurrence = field("Recurrence")
    RotationStartTime = field("RotationStartTime")
    StartTime = field("StartTime")

    @cached_property
    def Overrides(self):  # pragma: no cover
        return PreviewOverride.make_many(self.boto3_raw_data["Overrides"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPreviewRotationShiftsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPreviewRotationShiftsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRotationRequest:
    boto3_raw_data: "type_defs.UpdateRotationRequestTypeDef" = dataclasses.field()

    RotationId = field("RotationId")
    Recurrence = field("Recurrence")
    ContactIds = field("ContactIds")
    StartTime = field("StartTime")
    TimeZoneId = field("TimeZoneId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRotationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRotationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateContactRequest:
    boto3_raw_data: "type_defs.CreateContactRequestTypeDef" = dataclasses.field()

    Alias = field("Alias")
    Type = field("Type")
    Plan = field("Plan")
    DisplayName = field("DisplayName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IdempotencyToken = field("IdempotencyToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateContactRequest:
    boto3_raw_data: "type_defs.UpdateContactRequestTypeDef" = dataclasses.field()

    ContactId = field("ContactId")
    DisplayName = field("DisplayName")
    Plan = field("Plan")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
