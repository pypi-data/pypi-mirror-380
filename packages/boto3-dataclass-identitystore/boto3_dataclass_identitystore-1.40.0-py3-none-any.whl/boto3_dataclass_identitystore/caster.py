# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_identitystore import type_defs as bs_td


class IDENTITYSTORECaster:

    def create_group(
        self,
        res: "bs_td.CreateGroupResponseTypeDef",
    ) -> "dc_td.CreateGroupResponse":
        return dc_td.CreateGroupResponse.make_one(res)

    def create_group_membership(
        self,
        res: "bs_td.CreateGroupMembershipResponseTypeDef",
    ) -> "dc_td.CreateGroupMembershipResponse":
        return dc_td.CreateGroupMembershipResponse.make_one(res)

    def create_user(
        self,
        res: "bs_td.CreateUserResponseTypeDef",
    ) -> "dc_td.CreateUserResponse":
        return dc_td.CreateUserResponse.make_one(res)

    def describe_group(
        self,
        res: "bs_td.DescribeGroupResponseTypeDef",
    ) -> "dc_td.DescribeGroupResponse":
        return dc_td.DescribeGroupResponse.make_one(res)

    def describe_group_membership(
        self,
        res: "bs_td.DescribeGroupMembershipResponseTypeDef",
    ) -> "dc_td.DescribeGroupMembershipResponse":
        return dc_td.DescribeGroupMembershipResponse.make_one(res)

    def describe_user(
        self,
        res: "bs_td.DescribeUserResponseTypeDef",
    ) -> "dc_td.DescribeUserResponse":
        return dc_td.DescribeUserResponse.make_one(res)

    def get_group_id(
        self,
        res: "bs_td.GetGroupIdResponseTypeDef",
    ) -> "dc_td.GetGroupIdResponse":
        return dc_td.GetGroupIdResponse.make_one(res)

    def get_group_membership_id(
        self,
        res: "bs_td.GetGroupMembershipIdResponseTypeDef",
    ) -> "dc_td.GetGroupMembershipIdResponse":
        return dc_td.GetGroupMembershipIdResponse.make_one(res)

    def get_user_id(
        self,
        res: "bs_td.GetUserIdResponseTypeDef",
    ) -> "dc_td.GetUserIdResponse":
        return dc_td.GetUserIdResponse.make_one(res)

    def is_member_in_groups(
        self,
        res: "bs_td.IsMemberInGroupsResponseTypeDef",
    ) -> "dc_td.IsMemberInGroupsResponse":
        return dc_td.IsMemberInGroupsResponse.make_one(res)

    def list_group_memberships(
        self,
        res: "bs_td.ListGroupMembershipsResponseTypeDef",
    ) -> "dc_td.ListGroupMembershipsResponse":
        return dc_td.ListGroupMembershipsResponse.make_one(res)

    def list_group_memberships_for_member(
        self,
        res: "bs_td.ListGroupMembershipsForMemberResponseTypeDef",
    ) -> "dc_td.ListGroupMembershipsForMemberResponse":
        return dc_td.ListGroupMembershipsForMemberResponse.make_one(res)

    def list_groups(
        self,
        res: "bs_td.ListGroupsResponseTypeDef",
    ) -> "dc_td.ListGroupsResponse":
        return dc_td.ListGroupsResponse.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResponseTypeDef",
    ) -> "dc_td.ListUsersResponse":
        return dc_td.ListUsersResponse.make_one(res)


identitystore_caster = IDENTITYSTORECaster()
