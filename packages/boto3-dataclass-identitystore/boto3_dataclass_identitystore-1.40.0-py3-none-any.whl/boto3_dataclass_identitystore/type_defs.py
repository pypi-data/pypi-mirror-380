# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_identitystore import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Address:
    boto3_raw_data: "type_defs.AddressTypeDef" = dataclasses.field()

    StreetAddress = field("StreetAddress")
    Locality = field("Locality")
    Region = field("Region")
    PostalCode = field("PostalCode")
    Country = field("Country")
    Formatted = field("Formatted")
    Type = field("Type")
    Primary = field("Primary")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddressTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalId:
    boto3_raw_data: "type_defs.ExternalIdTypeDef" = dataclasses.field()

    Issuer = field("Issuer")
    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExternalIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExternalIdTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UniqueAttribute:
    boto3_raw_data: "type_defs.UniqueAttributeTypeDef" = dataclasses.field()

    AttributePath = field("AttributePath")
    AttributeValue = field("AttributeValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UniqueAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UniqueAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeOperation:
    boto3_raw_data: "type_defs.AttributeOperationTypeDef" = dataclasses.field()

    AttributePath = field("AttributePath")
    AttributeValue = field("AttributeValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeOperationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberId:
    boto3_raw_data: "type_defs.MemberIdTypeDef" = dataclasses.field()

    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberIdTypeDef"]]
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
class CreateGroupRequest:
    boto3_raw_data: "type_defs.CreateGroupRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    DisplayName = field("DisplayName")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Email:
    boto3_raw_data: "type_defs.EmailTypeDef" = dataclasses.field()

    Value = field("Value")
    Type = field("Type")
    Primary = field("Primary")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Name:
    boto3_raw_data: "type_defs.NameTypeDef" = dataclasses.field()

    Formatted = field("Formatted")
    FamilyName = field("FamilyName")
    GivenName = field("GivenName")
    MiddleName = field("MiddleName")
    HonorificPrefix = field("HonorificPrefix")
    HonorificSuffix = field("HonorificSuffix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NameTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NameTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumber:
    boto3_raw_data: "type_defs.PhoneNumberTypeDef" = dataclasses.field()

    Value = field("Value")
    Type = field("Type")
    Primary = field("Primary")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PhoneNumberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGroupMembershipRequest:
    boto3_raw_data: "type_defs.DeleteGroupMembershipRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityStoreId = field("IdentityStoreId")
    MembershipId = field("MembershipId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGroupMembershipRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGroupMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGroupRequest:
    boto3_raw_data: "type_defs.DeleteGroupRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    GroupId = field("GroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUserRequest:
    boto3_raw_data: "type_defs.DeleteUserRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    UserId = field("UserId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGroupMembershipRequest:
    boto3_raw_data: "type_defs.DescribeGroupMembershipRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityStoreId = field("IdentityStoreId")
    MembershipId = field("MembershipId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGroupMembershipRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGroupMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGroupRequest:
    boto3_raw_data: "type_defs.DescribeGroupRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    GroupId = field("GroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserRequest:
    boto3_raw_data: "type_defs.DescribeUserRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    UserId = field("UserId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    AttributePath = field("AttributePath")
    AttributeValue = field("AttributeValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
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
class ListGroupMembershipsRequest:
    boto3_raw_data: "type_defs.ListGroupMembershipsRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    GroupId = field("GroupId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupMembershipsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembershipsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Group:
    boto3_raw_data: "type_defs.GroupTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    IdentityStoreId = field("IdentityStoreId")
    DisplayName = field("DisplayName")

    @cached_property
    def ExternalIds(self):  # pragma: no cover
        return ExternalId.make_many(self.boto3_raw_data["ExternalIds"])

    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AlternateIdentifier:
    boto3_raw_data: "type_defs.AlternateIdentifierTypeDef" = dataclasses.field()

    @cached_property
    def ExternalId(self):  # pragma: no cover
        return ExternalId.make_one(self.boto3_raw_data["ExternalId"])

    @cached_property
    def UniqueAttribute(self):  # pragma: no cover
        return UniqueAttribute.make_one(self.boto3_raw_data["UniqueAttribute"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AlternateIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AlternateIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupRequest:
    boto3_raw_data: "type_defs.UpdateGroupRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    GroupId = field("GroupId")

    @cached_property
    def Operations(self):  # pragma: no cover
        return AttributeOperation.make_many(self.boto3_raw_data["Operations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserRequest:
    boto3_raw_data: "type_defs.UpdateUserRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    UserId = field("UserId")

    @cached_property
    def Operations(self):  # pragma: no cover
        return AttributeOperation.make_many(self.boto3_raw_data["Operations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupMembershipRequest:
    boto3_raw_data: "type_defs.CreateGroupMembershipRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityStoreId = field("IdentityStoreId")
    GroupId = field("GroupId")

    @cached_property
    def MemberId(self):  # pragma: no cover
        return MemberId.make_one(self.boto3_raw_data["MemberId"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupMembershipRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupMembershipIdRequest:
    boto3_raw_data: "type_defs.GetGroupMembershipIdRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    GroupId = field("GroupId")

    @cached_property
    def MemberId(self):  # pragma: no cover
        return MemberId.make_one(self.boto3_raw_data["MemberId"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGroupMembershipIdRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupMembershipIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupMembershipExistenceResult:
    boto3_raw_data: "type_defs.GroupMembershipExistenceResultTypeDef" = (
        dataclasses.field()
    )

    GroupId = field("GroupId")

    @cached_property
    def MemberId(self):  # pragma: no cover
        return MemberId.make_one(self.boto3_raw_data["MemberId"])

    MembershipExists = field("MembershipExists")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GroupMembershipExistenceResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupMembershipExistenceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupMembership:
    boto3_raw_data: "type_defs.GroupMembershipTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    MembershipId = field("MembershipId")
    GroupId = field("GroupId")

    @cached_property
    def MemberId(self):  # pragma: no cover
        return MemberId.make_one(self.boto3_raw_data["MemberId"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupMembershipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupMembershipTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsMemberInGroupsRequest:
    boto3_raw_data: "type_defs.IsMemberInGroupsRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def MemberId(self):  # pragma: no cover
        return MemberId.make_one(self.boto3_raw_data["MemberId"])

    GroupIds = field("GroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsMemberInGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsMemberInGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupMembershipsForMemberRequest:
    boto3_raw_data: "type_defs.ListGroupMembershipsForMemberRequestTypeDef" = (
        dataclasses.field()
    )

    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def MemberId(self):  # pragma: no cover
        return MemberId.make_one(self.boto3_raw_data["MemberId"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGroupMembershipsForMemberRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembershipsForMemberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupMembershipResponse:
    boto3_raw_data: "type_defs.CreateGroupMembershipResponseTypeDef" = (
        dataclasses.field()
    )

    MembershipId = field("MembershipId")
    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateGroupMembershipResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupMembershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupResponse:
    boto3_raw_data: "type_defs.CreateGroupResponseTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserResponse:
    boto3_raw_data: "type_defs.CreateUserResponseTypeDef" = dataclasses.field()

    UserId = field("UserId")
    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGroupMembershipResponse:
    boto3_raw_data: "type_defs.DescribeGroupMembershipResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityStoreId = field("IdentityStoreId")
    MembershipId = field("MembershipId")
    GroupId = field("GroupId")

    @cached_property
    def MemberId(self):  # pragma: no cover
        return MemberId.make_one(self.boto3_raw_data["MemberId"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGroupMembershipResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGroupMembershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGroupResponse:
    boto3_raw_data: "type_defs.DescribeGroupResponseTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    DisplayName = field("DisplayName")

    @cached_property
    def ExternalIds(self):  # pragma: no cover
        return ExternalId.make_many(self.boto3_raw_data["ExternalIds"])

    Description = field("Description")
    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupIdResponse:
    boto3_raw_data: "type_defs.GetGroupIdResponseTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGroupIdResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupIdResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupMembershipIdResponse:
    boto3_raw_data: "type_defs.GetGroupMembershipIdResponseTypeDef" = (
        dataclasses.field()
    )

    MembershipId = field("MembershipId")
    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGroupMembershipIdResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupMembershipIdResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserIdResponse:
    boto3_raw_data: "type_defs.GetUserIdResponseTypeDef" = dataclasses.field()

    UserId = field("UserId")
    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetUserIdResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserIdResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserRequest:
    boto3_raw_data: "type_defs.CreateUserRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    UserName = field("UserName")

    @cached_property
    def Name(self):  # pragma: no cover
        return Name.make_one(self.boto3_raw_data["Name"])

    DisplayName = field("DisplayName")
    NickName = field("NickName")
    ProfileUrl = field("ProfileUrl")

    @cached_property
    def Emails(self):  # pragma: no cover
        return Email.make_many(self.boto3_raw_data["Emails"])

    @cached_property
    def Addresses(self):  # pragma: no cover
        return Address.make_many(self.boto3_raw_data["Addresses"])

    @cached_property
    def PhoneNumbers(self):  # pragma: no cover
        return PhoneNumber.make_many(self.boto3_raw_data["PhoneNumbers"])

    UserType = field("UserType")
    Title = field("Title")
    PreferredLanguage = field("PreferredLanguage")
    Locale = field("Locale")
    Timezone = field("Timezone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateUserRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUserResponse:
    boto3_raw_data: "type_defs.DescribeUserResponseTypeDef" = dataclasses.field()

    UserName = field("UserName")
    UserId = field("UserId")

    @cached_property
    def ExternalIds(self):  # pragma: no cover
        return ExternalId.make_many(self.boto3_raw_data["ExternalIds"])

    @cached_property
    def Name(self):  # pragma: no cover
        return Name.make_one(self.boto3_raw_data["Name"])

    DisplayName = field("DisplayName")
    NickName = field("NickName")
    ProfileUrl = field("ProfileUrl")

    @cached_property
    def Emails(self):  # pragma: no cover
        return Email.make_many(self.boto3_raw_data["Emails"])

    @cached_property
    def Addresses(self):  # pragma: no cover
        return Address.make_many(self.boto3_raw_data["Addresses"])

    @cached_property
    def PhoneNumbers(self):  # pragma: no cover
        return PhoneNumber.make_many(self.boto3_raw_data["PhoneNumbers"])

    UserType = field("UserType")
    Title = field("Title")
    PreferredLanguage = field("PreferredLanguage")
    Locale = field("Locale")
    Timezone = field("Timezone")
    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUserResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUserResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class User:
    boto3_raw_data: "type_defs.UserTypeDef" = dataclasses.field()

    UserId = field("UserId")
    IdentityStoreId = field("IdentityStoreId")
    UserName = field("UserName")

    @cached_property
    def ExternalIds(self):  # pragma: no cover
        return ExternalId.make_many(self.boto3_raw_data["ExternalIds"])

    @cached_property
    def Name(self):  # pragma: no cover
        return Name.make_one(self.boto3_raw_data["Name"])

    DisplayName = field("DisplayName")
    NickName = field("NickName")
    ProfileUrl = field("ProfileUrl")

    @cached_property
    def Emails(self):  # pragma: no cover
        return Email.make_many(self.boto3_raw_data["Emails"])

    @cached_property
    def Addresses(self):  # pragma: no cover
        return Address.make_many(self.boto3_raw_data["Addresses"])

    @cached_property
    def PhoneNumbers(self):  # pragma: no cover
        return PhoneNumber.make_many(self.boto3_raw_data["PhoneNumbers"])

    UserType = field("UserType")
    Title = field("Title")
    PreferredLanguage = field("PreferredLanguage")
    Locale = field("Locale")
    Timezone = field("Timezone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsRequest:
    boto3_raw_data: "type_defs.ListGroupsRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGroupsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersRequest:
    boto3_raw_data: "type_defs.ListUsersRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupMembershipsForMemberRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupMembershipsForMemberRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def MemberId(self):  # pragma: no cover
        return MemberId.make_one(self.boto3_raw_data["MemberId"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGroupMembershipsForMemberRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembershipsForMemberRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupMembershipsRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupMembershipsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    IdentityStoreId = field("IdentityStoreId")
    GroupId = field("GroupId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGroupMembershipsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembershipsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupsRequestPaginateTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersRequestPaginate:
    boto3_raw_data: "type_defs.ListUsersRequestPaginateTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUsersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsResponse:
    boto3_raw_data: "type_defs.ListGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Groups(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["Groups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupIdRequest:
    boto3_raw_data: "type_defs.GetGroupIdRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def AlternateIdentifier(self):  # pragma: no cover
        return AlternateIdentifier.make_one(self.boto3_raw_data["AlternateIdentifier"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGroupIdRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserIdRequest:
    boto3_raw_data: "type_defs.GetUserIdRequestTypeDef" = dataclasses.field()

    IdentityStoreId = field("IdentityStoreId")

    @cached_property
    def AlternateIdentifier(self):  # pragma: no cover
        return AlternateIdentifier.make_one(self.boto3_raw_data["AlternateIdentifier"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetUserIdRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserIdRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsMemberInGroupsResponse:
    boto3_raw_data: "type_defs.IsMemberInGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Results(self):  # pragma: no cover
        return GroupMembershipExistenceResult.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsMemberInGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsMemberInGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupMembershipsForMemberResponse:
    boto3_raw_data: "type_defs.ListGroupMembershipsForMemberResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GroupMemberships(self):  # pragma: no cover
        return GroupMembership.make_many(self.boto3_raw_data["GroupMemberships"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGroupMembershipsForMemberResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembershipsForMemberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupMembershipsResponse:
    boto3_raw_data: "type_defs.ListGroupMembershipsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def GroupMemberships(self):  # pragma: no cover
        return GroupMembership.make_many(self.boto3_raw_data["GroupMemberships"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupMembershipsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembershipsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsersResponse:
    boto3_raw_data: "type_defs.ListUsersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Users(self):  # pragma: no cover
        return User.make_many(self.boto3_raw_data["Users"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
