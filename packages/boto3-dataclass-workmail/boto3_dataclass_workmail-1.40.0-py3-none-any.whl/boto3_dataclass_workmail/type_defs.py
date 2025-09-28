# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workmail import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessControlRule:
    boto3_raw_data: "type_defs.AccessControlRuleTypeDef" = dataclasses.field()

    Name = field("Name")
    Effect = field("Effect")
    Description = field("Description")
    IpRanges = field("IpRanges")
    NotIpRanges = field("NotIpRanges")
    Actions = field("Actions")
    NotActions = field("NotActions")
    UserIds = field("UserIds")
    NotUserIds = field("NotUserIds")
    DateCreated = field("DateCreated")
    DateModified = field("DateModified")
    ImpersonationRoleIds = field("ImpersonationRoleIds")
    NotImpersonationRoleIds = field("NotImpersonationRoleIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessControlRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateDelegateToResourceRequest:
    boto3_raw_data: "type_defs.AssociateDelegateToResourceRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    ResourceId = field("ResourceId")
    EntityId = field("EntityId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateDelegateToResourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateDelegateToResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateMemberToGroupRequest:
    boto3_raw_data: "type_defs.AssociateMemberToGroupRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    GroupId = field("GroupId")
    MemberId = field("MemberId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateMemberToGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMemberToGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeImpersonationRoleRequest:
    boto3_raw_data: "type_defs.AssumeImpersonationRoleRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    ImpersonationRoleId = field("ImpersonationRoleId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeImpersonationRoleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeImpersonationRoleRequestTypeDef"]
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
class LambdaAvailabilityProvider:
    boto3_raw_data: "type_defs.LambdaAvailabilityProviderTypeDef" = dataclasses.field()

    LambdaArn = field("LambdaArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LambdaAvailabilityProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaAvailabilityProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedactedEwsAvailabilityProvider:
    boto3_raw_data: "type_defs.RedactedEwsAvailabilityProviderTypeDef" = (
        dataclasses.field()
    )

    EwsEndpoint = field("EwsEndpoint")
    EwsUsername = field("EwsUsername")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedactedEwsAvailabilityProviderTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedactedEwsAvailabilityProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BookingOptions:
    boto3_raw_data: "type_defs.BookingOptionsTypeDef" = dataclasses.field()

    AutoAcceptRequests = field("AutoAcceptRequests")
    AutoDeclineRecurringRequests = field("AutoDeclineRecurringRequests")
    AutoDeclineConflictingRequests = field("AutoDeclineConflictingRequests")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BookingOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BookingOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMailboxExportJobRequest:
    boto3_raw_data: "type_defs.CancelMailboxExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    ClientToken = field("ClientToken")
    JobId = field("JobId")
    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelMailboxExportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMailboxExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAliasRequest:
    boto3_raw_data: "type_defs.CreateAliasRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")
    Alias = field("Alias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EwsAvailabilityProvider:
    boto3_raw_data: "type_defs.EwsAvailabilityProviderTypeDef" = dataclasses.field()

    EwsEndpoint = field("EwsEndpoint")
    EwsUsername = field("EwsUsername")
    EwsPassword = field("EwsPassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EwsAvailabilityProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EwsAvailabilityProviderTypeDef"]
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

    OrganizationId = field("OrganizationId")
    Name = field("Name")
    HiddenFromGlobalAddressList = field("HiddenFromGlobalAddressList")

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
class CreateIdentityCenterApplicationRequest:
    boto3_raw_data: "type_defs.CreateIdentityCenterApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    InstanceArn = field("InstanceArn")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateIdentityCenterApplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdentityCenterApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMobileDeviceAccessRuleRequest:
    boto3_raw_data: "type_defs.CreateMobileDeviceAccessRuleRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    Name = field("Name")
    Effect = field("Effect")
    ClientToken = field("ClientToken")
    Description = field("Description")
    DeviceTypes = field("DeviceTypes")
    NotDeviceTypes = field("NotDeviceTypes")
    DeviceModels = field("DeviceModels")
    NotDeviceModels = field("NotDeviceModels")
    DeviceOperatingSystems = field("DeviceOperatingSystems")
    NotDeviceOperatingSystems = field("NotDeviceOperatingSystems")
    DeviceUserAgents = field("DeviceUserAgents")
    NotDeviceUserAgents = field("NotDeviceUserAgents")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMobileDeviceAccessRuleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMobileDeviceAccessRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Domain:
    boto3_raw_data: "type_defs.DomainTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    HostedZoneId = field("HostedZoneId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceRequest:
    boto3_raw_data: "type_defs.CreateResourceRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    Name = field("Name")
    Type = field("Type")
    Description = field("Description")
    HiddenFromGlobalAddressList = field("HiddenFromGlobalAddressList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceRequestTypeDef"]
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

    OrganizationId = field("OrganizationId")
    Name = field("Name")
    DisplayName = field("DisplayName")
    Password = field("Password")
    Role = field("Role")
    FirstName = field("FirstName")
    LastName = field("LastName")
    HiddenFromGlobalAddressList = field("HiddenFromGlobalAddressList")
    IdentityProviderUserId = field("IdentityProviderUserId")

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
class Delegate:
    boto3_raw_data: "type_defs.DelegateTypeDef" = dataclasses.field()

    Id = field("Id")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DelegateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DelegateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessControlRuleRequest:
    boto3_raw_data: "type_defs.DeleteAccessControlRuleRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAccessControlRuleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessControlRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAliasRequest:
    boto3_raw_data: "type_defs.DeleteAliasRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")
    Alias = field("Alias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAvailabilityConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteAvailabilityConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAvailabilityConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAvailabilityConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEmailMonitoringConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteEmailMonitoringConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEmailMonitoringConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEmailMonitoringConfigurationRequestTypeDef"]
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

    OrganizationId = field("OrganizationId")
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
class DeleteIdentityCenterApplicationRequest:
    boto3_raw_data: "type_defs.DeleteIdentityCenterApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteIdentityCenterApplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdentityCenterApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdentityProviderConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteIdentityProviderConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteIdentityProviderConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdentityProviderConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImpersonationRoleRequest:
    boto3_raw_data: "type_defs.DeleteImpersonationRoleRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    ImpersonationRoleId = field("ImpersonationRoleId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteImpersonationRoleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImpersonationRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMailboxPermissionsRequest:
    boto3_raw_data: "type_defs.DeleteMailboxPermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")
    GranteeId = field("GranteeId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMailboxPermissionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMailboxPermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMobileDeviceAccessOverrideRequest:
    boto3_raw_data: "type_defs.DeleteMobileDeviceAccessOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    UserId = field("UserId")
    DeviceId = field("DeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMobileDeviceAccessOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMobileDeviceAccessOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMobileDeviceAccessRuleRequest:
    boto3_raw_data: "type_defs.DeleteMobileDeviceAccessRuleRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    MobileDeviceAccessRuleId = field("MobileDeviceAccessRuleId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMobileDeviceAccessRuleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMobileDeviceAccessRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOrganizationRequest:
    boto3_raw_data: "type_defs.DeleteOrganizationRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    DeleteDirectory = field("DeleteDirectory")
    ClientToken = field("ClientToken")
    ForceDelete = field("ForceDelete")
    DeleteIdentityCenterApplication = field("DeleteIdentityCenterApplication")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOrganizationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOrganizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePersonalAccessTokenRequest:
    boto3_raw_data: "type_defs.DeletePersonalAccessTokenRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    PersonalAccessTokenId = field("PersonalAccessTokenId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePersonalAccessTokenRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePersonalAccessTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceRequest:
    boto3_raw_data: "type_defs.DeleteResourceRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRetentionPolicyRequest:
    boto3_raw_data: "type_defs.DeleteRetentionPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRetentionPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRetentionPolicyRequestTypeDef"]
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

    OrganizationId = field("OrganizationId")
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
class DeregisterFromWorkMailRequest:
    boto3_raw_data: "type_defs.DeregisterFromWorkMailRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterFromWorkMailRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterFromWorkMailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterMailDomainRequest:
    boto3_raw_data: "type_defs.DeregisterMailDomainRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterMailDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterMailDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEmailMonitoringConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeEmailMonitoringConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEmailMonitoringConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEmailMonitoringConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntityRequest:
    boto3_raw_data: "type_defs.DescribeEntityRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    Email = field("Email")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEntityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntityRequestTypeDef"]
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

    OrganizationId = field("OrganizationId")
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
class DescribeIdentityProviderConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeIdentityProviderConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeIdentityProviderConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityProviderConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityCenterConfiguration:
    boto3_raw_data: "type_defs.IdentityCenterConfigurationTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityCenterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityCenterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PersonalAccessTokenConfiguration:
    boto3_raw_data: "type_defs.PersonalAccessTokenConfigurationTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    LifetimeInDays = field("LifetimeInDays")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PersonalAccessTokenConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PersonalAccessTokenConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInboundDmarcSettingsRequest:
    boto3_raw_data: "type_defs.DescribeInboundDmarcSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInboundDmarcSettingsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInboundDmarcSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMailboxExportJobRequest:
    boto3_raw_data: "type_defs.DescribeMailboxExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMailboxExportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMailboxExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationRequest:
    boto3_raw_data: "type_defs.DescribeOrganizationRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeOrganizationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceRequest:
    boto3_raw_data: "type_defs.DescribeResourceRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceRequestTypeDef"]
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

    OrganizationId = field("OrganizationId")
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
class DisassociateDelegateFromResourceRequest:
    boto3_raw_data: "type_defs.DisassociateDelegateFromResourceRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    ResourceId = field("ResourceId")
    EntityId = field("EntityId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateDelegateFromResourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateDelegateFromResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMemberFromGroupRequest:
    boto3_raw_data: "type_defs.DisassociateMemberFromGroupRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    GroupId = field("GroupId")
    MemberId = field("MemberId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateMemberFromGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMemberFromGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DnsRecord:
    boto3_raw_data: "type_defs.DnsRecordTypeDef" = dataclasses.field()

    Type = field("Type")
    Hostname = field("Hostname")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DnsRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DnsRecordTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FolderConfiguration:
    boto3_raw_data: "type_defs.FolderConfigurationTypeDef" = dataclasses.field()

    Name = field("Name")
    Action = field("Action")
    Period = field("Period")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FolderConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FolderConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessControlEffectRequest:
    boto3_raw_data: "type_defs.GetAccessControlEffectRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    IpAddress = field("IpAddress")
    Action = field("Action")
    UserId = field("UserId")
    ImpersonationRoleId = field("ImpersonationRoleId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccessControlEffectRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessControlEffectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDefaultRetentionPolicyRequest:
    boto3_raw_data: "type_defs.GetDefaultRetentionPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDefaultRetentionPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDefaultRetentionPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImpersonationRoleEffectRequest:
    boto3_raw_data: "type_defs.GetImpersonationRoleEffectRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    ImpersonationRoleId = field("ImpersonationRoleId")
    TargetUser = field("TargetUser")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetImpersonationRoleEffectRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImpersonationRoleEffectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImpersonationMatchedRule:
    boto3_raw_data: "type_defs.ImpersonationMatchedRuleTypeDef" = dataclasses.field()

    ImpersonationRuleId = field("ImpersonationRuleId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImpersonationMatchedRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImpersonationMatchedRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImpersonationRoleRequest:
    boto3_raw_data: "type_defs.GetImpersonationRoleRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    ImpersonationRoleId = field("ImpersonationRoleId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImpersonationRoleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImpersonationRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImpersonationRuleOutput:
    boto3_raw_data: "type_defs.ImpersonationRuleOutputTypeDef" = dataclasses.field()

    ImpersonationRuleId = field("ImpersonationRuleId")
    Effect = field("Effect")
    Name = field("Name")
    Description = field("Description")
    TargetUsers = field("TargetUsers")
    NotTargetUsers = field("NotTargetUsers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImpersonationRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImpersonationRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMailDomainRequest:
    boto3_raw_data: "type_defs.GetMailDomainRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMailDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMailDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMailboxDetailsRequest:
    boto3_raw_data: "type_defs.GetMailboxDetailsRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    UserId = field("UserId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMailboxDetailsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMailboxDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMobileDeviceAccessEffectRequest:
    boto3_raw_data: "type_defs.GetMobileDeviceAccessEffectRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    DeviceType = field("DeviceType")
    DeviceModel = field("DeviceModel")
    DeviceOperatingSystem = field("DeviceOperatingSystem")
    DeviceUserAgent = field("DeviceUserAgent")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMobileDeviceAccessEffectRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMobileDeviceAccessEffectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MobileDeviceAccessMatchedRule:
    boto3_raw_data: "type_defs.MobileDeviceAccessMatchedRuleTypeDef" = (
        dataclasses.field()
    )

    MobileDeviceAccessRuleId = field("MobileDeviceAccessRuleId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MobileDeviceAccessMatchedRuleTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MobileDeviceAccessMatchedRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMobileDeviceAccessOverrideRequest:
    boto3_raw_data: "type_defs.GetMobileDeviceAccessOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    UserId = field("UserId")
    DeviceId = field("DeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMobileDeviceAccessOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMobileDeviceAccessOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPersonalAccessTokenMetadataRequest:
    boto3_raw_data: "type_defs.GetPersonalAccessTokenMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    PersonalAccessTokenId = field("PersonalAccessTokenId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPersonalAccessTokenMetadataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPersonalAccessTokenMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupIdentifier:
    boto3_raw_data: "type_defs.GroupIdentifierTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    GroupName = field("GroupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupIdentifierTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Group:
    boto3_raw_data: "type_defs.GroupTypeDef" = dataclasses.field()

    Id = field("Id")
    Email = field("Email")
    Name = field("Name")
    State = field("State")
    EnabledDate = field("EnabledDate")
    DisabledDate = field("DisabledDate")

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
class ImpersonationRole:
    boto3_raw_data: "type_defs.ImpersonationRoleTypeDef" = dataclasses.field()

    ImpersonationRoleId = field("ImpersonationRoleId")
    Name = field("Name")
    Type = field("Type")
    DateCreated = field("DateCreated")
    DateModified = field("DateModified")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImpersonationRoleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImpersonationRoleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImpersonationRule:
    boto3_raw_data: "type_defs.ImpersonationRuleTypeDef" = dataclasses.field()

    ImpersonationRuleId = field("ImpersonationRuleId")
    Effect = field("Effect")
    Name = field("Name")
    Description = field("Description")
    TargetUsers = field("TargetUsers")
    NotTargetUsers = field("NotTargetUsers")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImpersonationRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImpersonationRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessControlRulesRequest:
    boto3_raw_data: "type_defs.ListAccessControlRulesRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccessControlRulesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessControlRulesRequestTypeDef"]
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
class ListAliasesRequest:
    boto3_raw_data: "type_defs.ListAliasesRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAliasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailabilityConfigurationsRequest:
    boto3_raw_data: "type_defs.ListAvailabilityConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailabilityConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailabilityConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupMembersRequest:
    boto3_raw_data: "type_defs.ListGroupMembersRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    GroupId = field("GroupId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Member:
    boto3_raw_data: "type_defs.MemberTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Type = field("Type")
    State = field("State")
    EnabledDate = field("EnabledDate")
    DisabledDate = field("DisabledDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsFilters:
    boto3_raw_data: "type_defs.ListGroupsFiltersTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    PrimaryEmailPrefix = field("PrimaryEmailPrefix")
    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGroupsFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsForEntityFilters:
    boto3_raw_data: "type_defs.ListGroupsForEntityFiltersTypeDef" = dataclasses.field()

    GroupNamePrefix = field("GroupNamePrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsForEntityFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsForEntityFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImpersonationRolesRequest:
    boto3_raw_data: "type_defs.ListImpersonationRolesRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListImpersonationRolesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImpersonationRolesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMailDomainsRequest:
    boto3_raw_data: "type_defs.ListMailDomainsRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMailDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMailDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MailDomainSummary:
    boto3_raw_data: "type_defs.MailDomainSummaryTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DefaultDomain = field("DefaultDomain")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MailDomainSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MailDomainSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMailboxExportJobsRequest:
    boto3_raw_data: "type_defs.ListMailboxExportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMailboxExportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMailboxExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MailboxExportJob:
    boto3_raw_data: "type_defs.MailboxExportJobTypeDef" = dataclasses.field()

    JobId = field("JobId")
    EntityId = field("EntityId")
    Description = field("Description")
    S3BucketName = field("S3BucketName")
    S3Path = field("S3Path")
    EstimatedProgress = field("EstimatedProgress")
    State = field("State")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MailboxExportJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MailboxExportJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMailboxPermissionsRequest:
    boto3_raw_data: "type_defs.ListMailboxPermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMailboxPermissionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMailboxPermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Permission:
    boto3_raw_data: "type_defs.PermissionTypeDef" = dataclasses.field()

    GranteeId = field("GranteeId")
    GranteeType = field("GranteeType")
    PermissionValues = field("PermissionValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PermissionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMobileDeviceAccessOverridesRequest:
    boto3_raw_data: "type_defs.ListMobileDeviceAccessOverridesRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    UserId = field("UserId")
    DeviceId = field("DeviceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMobileDeviceAccessOverridesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMobileDeviceAccessOverridesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MobileDeviceAccessOverride:
    boto3_raw_data: "type_defs.MobileDeviceAccessOverrideTypeDef" = dataclasses.field()

    UserId = field("UserId")
    DeviceId = field("DeviceId")
    Effect = field("Effect")
    Description = field("Description")
    DateCreated = field("DateCreated")
    DateModified = field("DateModified")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MobileDeviceAccessOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MobileDeviceAccessOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMobileDeviceAccessRulesRequest:
    boto3_raw_data: "type_defs.ListMobileDeviceAccessRulesRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMobileDeviceAccessRulesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMobileDeviceAccessRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MobileDeviceAccessRule:
    boto3_raw_data: "type_defs.MobileDeviceAccessRuleTypeDef" = dataclasses.field()

    MobileDeviceAccessRuleId = field("MobileDeviceAccessRuleId")
    Name = field("Name")
    Description = field("Description")
    Effect = field("Effect")
    DeviceTypes = field("DeviceTypes")
    NotDeviceTypes = field("NotDeviceTypes")
    DeviceModels = field("DeviceModels")
    NotDeviceModels = field("NotDeviceModels")
    DeviceOperatingSystems = field("DeviceOperatingSystems")
    NotDeviceOperatingSystems = field("NotDeviceOperatingSystems")
    DeviceUserAgents = field("DeviceUserAgents")
    NotDeviceUserAgents = field("NotDeviceUserAgents")
    DateCreated = field("DateCreated")
    DateModified = field("DateModified")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MobileDeviceAccessRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MobileDeviceAccessRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationsRequest:
    boto3_raw_data: "type_defs.ListOrganizationsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOrganizationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationSummary:
    boto3_raw_data: "type_defs.OrganizationSummaryTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    Alias = field("Alias")
    DefaultMailDomain = field("DefaultMailDomain")
    ErrorMessage = field("ErrorMessage")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPersonalAccessTokensRequest:
    boto3_raw_data: "type_defs.ListPersonalAccessTokensRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    UserId = field("UserId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPersonalAccessTokensRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPersonalAccessTokensRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PersonalAccessTokenSummary:
    boto3_raw_data: "type_defs.PersonalAccessTokenSummaryTypeDef" = dataclasses.field()

    PersonalAccessTokenId = field("PersonalAccessTokenId")
    UserId = field("UserId")
    Name = field("Name")
    DateCreated = field("DateCreated")
    DateLastUsed = field("DateLastUsed")
    ExpiresTime = field("ExpiresTime")
    Scopes = field("Scopes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PersonalAccessTokenSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PersonalAccessTokenSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDelegatesRequest:
    boto3_raw_data: "type_defs.ListResourceDelegatesRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    ResourceId = field("ResourceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceDelegatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDelegatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesFilters:
    boto3_raw_data: "type_defs.ListResourcesFiltersTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    PrimaryEmailPrefix = field("PrimaryEmailPrefix")
    State = field("State")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourcesFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesFiltersTypeDef"]
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

    Id = field("Id")
    Email = field("Email")
    Name = field("Name")
    Type = field("Type")
    State = field("State")
    EnabledDate = field("EnabledDate")
    DisabledDate = field("DisabledDate")
    Description = field("Description")

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
class ListUsersFilters:
    boto3_raw_data: "type_defs.ListUsersFiltersTypeDef" = dataclasses.field()

    UsernamePrefix = field("UsernamePrefix")
    DisplayNamePrefix = field("DisplayNamePrefix")
    PrimaryEmailPrefix = field("PrimaryEmailPrefix")
    State = field("State")
    IdentityProviderUserIdPrefix = field("IdentityProviderUserIdPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsersFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUsersFiltersTypeDef"]
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

    Id = field("Id")
    Email = field("Email")
    Name = field("Name")
    DisplayName = field("DisplayName")
    State = field("State")
    UserRole = field("UserRole")
    EnabledDate = field("EnabledDate")
    DisabledDate = field("DisabledDate")
    IdentityProviderUserId = field("IdentityProviderUserId")
    IdentityProviderIdentityStoreId = field("IdentityProviderIdentityStoreId")

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
class PutAccessControlRuleRequest:
    boto3_raw_data: "type_defs.PutAccessControlRuleRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Effect = field("Effect")
    Description = field("Description")
    OrganizationId = field("OrganizationId")
    IpRanges = field("IpRanges")
    NotIpRanges = field("NotIpRanges")
    Actions = field("Actions")
    NotActions = field("NotActions")
    UserIds = field("UserIds")
    NotUserIds = field("NotUserIds")
    ImpersonationRoleIds = field("ImpersonationRoleIds")
    NotImpersonationRoleIds = field("NotImpersonationRoleIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccessControlRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccessControlRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEmailMonitoringConfigurationRequest:
    boto3_raw_data: "type_defs.PutEmailMonitoringConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    LogGroupArn = field("LogGroupArn")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutEmailMonitoringConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEmailMonitoringConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInboundDmarcSettingsRequest:
    boto3_raw_data: "type_defs.PutInboundDmarcSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    Enforced = field("Enforced")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutInboundDmarcSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInboundDmarcSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMailboxPermissionsRequest:
    boto3_raw_data: "type_defs.PutMailboxPermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")
    GranteeId = field("GranteeId")
    PermissionValues = field("PermissionValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMailboxPermissionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMailboxPermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMobileDeviceAccessOverrideRequest:
    boto3_raw_data: "type_defs.PutMobileDeviceAccessOverrideRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    UserId = field("UserId")
    DeviceId = field("DeviceId")
    Effect = field("Effect")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutMobileDeviceAccessOverrideRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMobileDeviceAccessOverrideRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterMailDomainRequest:
    boto3_raw_data: "type_defs.RegisterMailDomainRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    DomainName = field("DomainName")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterMailDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterMailDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterToWorkMailRequest:
    boto3_raw_data: "type_defs.RegisterToWorkMailRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")
    Email = field("Email")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterToWorkMailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterToWorkMailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetPasswordRequest:
    boto3_raw_data: "type_defs.ResetPasswordRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    UserId = field("UserId")
    Password = field("Password")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetPasswordRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetPasswordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMailboxExportJobRequest:
    boto3_raw_data: "type_defs.StartMailboxExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    ClientToken = field("ClientToken")
    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")
    RoleArn = field("RoleArn")
    KmsKeyArn = field("KmsKeyArn")
    S3BucketName = field("S3BucketName")
    S3Prefix = field("S3Prefix")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMailboxExportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMailboxExportJobRequestTypeDef"]
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
class UpdateDefaultMailDomainRequest:
    boto3_raw_data: "type_defs.UpdateDefaultMailDomainRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDefaultMailDomainRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDefaultMailDomainRequestTypeDef"]
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

    OrganizationId = field("OrganizationId")
    GroupId = field("GroupId")
    HiddenFromGlobalAddressList = field("HiddenFromGlobalAddressList")

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
class UpdateMailboxQuotaRequest:
    boto3_raw_data: "type_defs.UpdateMailboxQuotaRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    UserId = field("UserId")
    MailboxQuota = field("MailboxQuota")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMailboxQuotaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMailboxQuotaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMobileDeviceAccessRuleRequest:
    boto3_raw_data: "type_defs.UpdateMobileDeviceAccessRuleRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    MobileDeviceAccessRuleId = field("MobileDeviceAccessRuleId")
    Name = field("Name")
    Effect = field("Effect")
    Description = field("Description")
    DeviceTypes = field("DeviceTypes")
    NotDeviceTypes = field("NotDeviceTypes")
    DeviceModels = field("DeviceModels")
    NotDeviceModels = field("NotDeviceModels")
    DeviceOperatingSystems = field("DeviceOperatingSystems")
    NotDeviceOperatingSystems = field("NotDeviceOperatingSystems")
    DeviceUserAgents = field("DeviceUserAgents")
    NotDeviceUserAgents = field("NotDeviceUserAgents")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMobileDeviceAccessRuleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMobileDeviceAccessRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePrimaryEmailAddressRequest:
    boto3_raw_data: "type_defs.UpdatePrimaryEmailAddressRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")
    Email = field("Email")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdatePrimaryEmailAddressRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePrimaryEmailAddressRequestTypeDef"]
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

    OrganizationId = field("OrganizationId")
    UserId = field("UserId")
    Role = field("Role")
    DisplayName = field("DisplayName")
    FirstName = field("FirstName")
    LastName = field("LastName")
    HiddenFromGlobalAddressList = field("HiddenFromGlobalAddressList")
    Initials = field("Initials")
    Telephone = field("Telephone")
    Street = field("Street")
    JobTitle = field("JobTitle")
    City = field("City")
    Company = field("Company")
    ZipCode = field("ZipCode")
    Department = field("Department")
    Country = field("Country")
    Office = field("Office")
    IdentityProviderUserId = field("IdentityProviderUserId")

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
class AssumeImpersonationRoleResponse:
    boto3_raw_data: "type_defs.AssumeImpersonationRoleResponseTypeDef" = (
        dataclasses.field()
    )

    Token = field("Token")
    ExpiresIn = field("ExpiresIn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeImpersonationRoleResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeImpersonationRoleResponseTypeDef"]
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
class CreateIdentityCenterApplicationResponse:
    boto3_raw_data: "type_defs.CreateIdentityCenterApplicationResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateIdentityCenterApplicationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdentityCenterApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImpersonationRoleResponse:
    boto3_raw_data: "type_defs.CreateImpersonationRoleResponseTypeDef" = (
        dataclasses.field()
    )

    ImpersonationRoleId = field("ImpersonationRoleId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateImpersonationRoleResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImpersonationRoleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMobileDeviceAccessRuleResponse:
    boto3_raw_data: "type_defs.CreateMobileDeviceAccessRuleResponseTypeDef" = (
        dataclasses.field()
    )

    MobileDeviceAccessRuleId = field("MobileDeviceAccessRuleId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMobileDeviceAccessRuleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMobileDeviceAccessRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOrganizationResponse:
    boto3_raw_data: "type_defs.CreateOrganizationResponseTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOrganizationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOrganizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourceResponse:
    boto3_raw_data: "type_defs.CreateResourceResponseTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourceResponseTypeDef"]
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
class DeleteOrganizationResponse:
    boto3_raw_data: "type_defs.DeleteOrganizationResponseTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteOrganizationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOrganizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEmailMonitoringConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeEmailMonitoringConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    RoleArn = field("RoleArn")
    LogGroupArn = field("LogGroupArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEmailMonitoringConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEmailMonitoringConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntityResponse:
    boto3_raw_data: "type_defs.DescribeEntityResponseTypeDef" = dataclasses.field()

    EntityId = field("EntityId")
    Name = field("Name")
    Type = field("Type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEntityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntityResponseTypeDef"]
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
    Name = field("Name")
    Email = field("Email")
    State = field("State")
    EnabledDate = field("EnabledDate")
    DisabledDate = field("DisabledDate")
    HiddenFromGlobalAddressList = field("HiddenFromGlobalAddressList")

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
class DescribeInboundDmarcSettingsResponse:
    boto3_raw_data: "type_defs.DescribeInboundDmarcSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    Enforced = field("Enforced")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInboundDmarcSettingsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInboundDmarcSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMailboxExportJobResponse:
    boto3_raw_data: "type_defs.DescribeMailboxExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    EntityId = field("EntityId")
    Description = field("Description")
    RoleArn = field("RoleArn")
    KmsKeyArn = field("KmsKeyArn")
    S3BucketName = field("S3BucketName")
    S3Prefix = field("S3Prefix")
    S3Path = field("S3Path")
    EstimatedProgress = field("EstimatedProgress")
    State = field("State")
    ErrorInfo = field("ErrorInfo")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMailboxExportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMailboxExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationResponse:
    boto3_raw_data: "type_defs.DescribeOrganizationResponseTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    Alias = field("Alias")
    State = field("State")
    DirectoryId = field("DirectoryId")
    DirectoryType = field("DirectoryType")
    DefaultMailDomain = field("DefaultMailDomain")
    CompletedDate = field("CompletedDate")
    ErrorMessage = field("ErrorMessage")
    ARN = field("ARN")
    MigrationAdmin = field("MigrationAdmin")
    InteroperabilityEnabled = field("InteroperabilityEnabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeOrganizationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationResponseTypeDef"]
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

    UserId = field("UserId")
    Name = field("Name")
    Email = field("Email")
    DisplayName = field("DisplayName")
    State = field("State")
    UserRole = field("UserRole")
    EnabledDate = field("EnabledDate")
    DisabledDate = field("DisabledDate")
    MailboxProvisionedDate = field("MailboxProvisionedDate")
    MailboxDeprovisionedDate = field("MailboxDeprovisionedDate")
    FirstName = field("FirstName")
    LastName = field("LastName")
    HiddenFromGlobalAddressList = field("HiddenFromGlobalAddressList")
    Initials = field("Initials")
    Telephone = field("Telephone")
    Street = field("Street")
    JobTitle = field("JobTitle")
    City = field("City")
    Company = field("Company")
    ZipCode = field("ZipCode")
    Department = field("Department")
    Country = field("Country")
    Office = field("Office")
    IdentityProviderUserId = field("IdentityProviderUserId")
    IdentityProviderIdentityStoreId = field("IdentityProviderIdentityStoreId")

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
class GetAccessControlEffectResponse:
    boto3_raw_data: "type_defs.GetAccessControlEffectResponseTypeDef" = (
        dataclasses.field()
    )

    Effect = field("Effect")
    MatchedRules = field("MatchedRules")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAccessControlEffectResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessControlEffectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMailboxDetailsResponse:
    boto3_raw_data: "type_defs.GetMailboxDetailsResponseTypeDef" = dataclasses.field()

    MailboxQuota = field("MailboxQuota")
    MailboxSize = field("MailboxSize")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMailboxDetailsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMailboxDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMobileDeviceAccessOverrideResponse:
    boto3_raw_data: "type_defs.GetMobileDeviceAccessOverrideResponseTypeDef" = (
        dataclasses.field()
    )

    UserId = field("UserId")
    DeviceId = field("DeviceId")
    Effect = field("Effect")
    Description = field("Description")
    DateCreated = field("DateCreated")
    DateModified = field("DateModified")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMobileDeviceAccessOverrideResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMobileDeviceAccessOverrideResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPersonalAccessTokenMetadataResponse:
    boto3_raw_data: "type_defs.GetPersonalAccessTokenMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    PersonalAccessTokenId = field("PersonalAccessTokenId")
    UserId = field("UserId")
    Name = field("Name")
    DateCreated = field("DateCreated")
    DateLastUsed = field("DateLastUsed")
    ExpiresTime = field("ExpiresTime")
    Scopes = field("Scopes")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPersonalAccessTokenMetadataResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPersonalAccessTokenMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessControlRulesResponse:
    boto3_raw_data: "type_defs.ListAccessControlRulesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Rules(self):  # pragma: no cover
        return AccessControlRule.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccessControlRulesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessControlRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesResponse:
    boto3_raw_data: "type_defs.ListAliasesResponseTypeDef" = dataclasses.field()

    Aliases = field("Aliases")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAliasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMailboxExportJobResponse:
    boto3_raw_data: "type_defs.StartMailboxExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMailboxExportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMailboxExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestAvailabilityConfigurationResponse:
    boto3_raw_data: "type_defs.TestAvailabilityConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    TestPassed = field("TestPassed")
    FailureReason = field("FailureReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TestAvailabilityConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestAvailabilityConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailabilityConfiguration:
    boto3_raw_data: "type_defs.AvailabilityConfigurationTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ProviderType = field("ProviderType")

    @cached_property
    def EwsProvider(self):  # pragma: no cover
        return RedactedEwsAvailabilityProvider.make_one(
            self.boto3_raw_data["EwsProvider"]
        )

    @cached_property
    def LambdaProvider(self):  # pragma: no cover
        return LambdaAvailabilityProvider.make_one(
            self.boto3_raw_data["LambdaProvider"]
        )

    DateCreated = field("DateCreated")
    DateModified = field("DateModified")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailabilityConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceResponse:
    boto3_raw_data: "type_defs.DescribeResourceResponseTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    Email = field("Email")
    Name = field("Name")
    Type = field("Type")

    @cached_property
    def BookingOptions(self):  # pragma: no cover
        return BookingOptions.make_one(self.boto3_raw_data["BookingOptions"])

    State = field("State")
    EnabledDate = field("EnabledDate")
    DisabledDate = field("DisabledDate")
    Description = field("Description")
    HiddenFromGlobalAddressList = field("HiddenFromGlobalAddressList")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceRequest:
    boto3_raw_data: "type_defs.UpdateResourceRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    ResourceId = field("ResourceId")
    Name = field("Name")

    @cached_property
    def BookingOptions(self):  # pragma: no cover
        return BookingOptions.make_one(self.boto3_raw_data["BookingOptions"])

    Description = field("Description")
    Type = field("Type")
    HiddenFromGlobalAddressList = field("HiddenFromGlobalAddressList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAvailabilityConfigurationRequest:
    boto3_raw_data: "type_defs.CreateAvailabilityConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    DomainName = field("DomainName")
    ClientToken = field("ClientToken")

    @cached_property
    def EwsProvider(self):  # pragma: no cover
        return EwsAvailabilityProvider.make_one(self.boto3_raw_data["EwsProvider"])

    @cached_property
    def LambdaProvider(self):  # pragma: no cover
        return LambdaAvailabilityProvider.make_one(
            self.boto3_raw_data["LambdaProvider"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAvailabilityConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAvailabilityConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestAvailabilityConfigurationRequest:
    boto3_raw_data: "type_defs.TestAvailabilityConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    DomainName = field("DomainName")

    @cached_property
    def EwsProvider(self):  # pragma: no cover
        return EwsAvailabilityProvider.make_one(self.boto3_raw_data["EwsProvider"])

    @cached_property
    def LambdaProvider(self):  # pragma: no cover
        return LambdaAvailabilityProvider.make_one(
            self.boto3_raw_data["LambdaProvider"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TestAvailabilityConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestAvailabilityConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAvailabilityConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateAvailabilityConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    DomainName = field("DomainName")

    @cached_property
    def EwsProvider(self):  # pragma: no cover
        return EwsAvailabilityProvider.make_one(self.boto3_raw_data["EwsProvider"])

    @cached_property
    def LambdaProvider(self):  # pragma: no cover
        return LambdaAvailabilityProvider.make_one(
            self.boto3_raw_data["LambdaProvider"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAvailabilityConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAvailabilityConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateOrganizationRequest:
    boto3_raw_data: "type_defs.CreateOrganizationRequestTypeDef" = dataclasses.field()

    Alias = field("Alias")
    DirectoryId = field("DirectoryId")
    ClientToken = field("ClientToken")

    @cached_property
    def Domains(self):  # pragma: no cover
        return Domain.make_many(self.boto3_raw_data["Domains"])

    KmsKeyArn = field("KmsKeyArn")
    EnableInteroperability = field("EnableInteroperability")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateOrganizationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateOrganizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDelegatesResponse:
    boto3_raw_data: "type_defs.ListResourceDelegatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Delegates(self):  # pragma: no cover
        return Delegate.make_many(self.boto3_raw_data["Delegates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceDelegatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDelegatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIdentityProviderConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeIdentityProviderConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    AuthenticationMode = field("AuthenticationMode")

    @cached_property
    def IdentityCenterConfiguration(self):  # pragma: no cover
        return IdentityCenterConfiguration.make_one(
            self.boto3_raw_data["IdentityCenterConfiguration"]
        )

    @cached_property
    def PersonalAccessTokenConfiguration(self):  # pragma: no cover
        return PersonalAccessTokenConfiguration.make_one(
            self.boto3_raw_data["PersonalAccessTokenConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeIdentityProviderConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityProviderConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutIdentityProviderConfigurationRequest:
    boto3_raw_data: "type_defs.PutIdentityProviderConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    AuthenticationMode = field("AuthenticationMode")

    @cached_property
    def IdentityCenterConfiguration(self):  # pragma: no cover
        return IdentityCenterConfiguration.make_one(
            self.boto3_raw_data["IdentityCenterConfiguration"]
        )

    @cached_property
    def PersonalAccessTokenConfiguration(self):  # pragma: no cover
        return PersonalAccessTokenConfiguration.make_one(
            self.boto3_raw_data["PersonalAccessTokenConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutIdentityProviderConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIdentityProviderConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMailDomainResponse:
    boto3_raw_data: "type_defs.GetMailDomainResponseTypeDef" = dataclasses.field()

    @cached_property
    def Records(self):  # pragma: no cover
        return DnsRecord.make_many(self.boto3_raw_data["Records"])

    IsTestDomain = field("IsTestDomain")
    IsDefault = field("IsDefault")
    OwnershipVerificationStatus = field("OwnershipVerificationStatus")
    DkimVerificationStatus = field("DkimVerificationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMailDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMailDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDefaultRetentionPolicyResponse:
    boto3_raw_data: "type_defs.GetDefaultRetentionPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def FolderConfigurations(self):  # pragma: no cover
        return FolderConfiguration.make_many(
            self.boto3_raw_data["FolderConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDefaultRetentionPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDefaultRetentionPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRetentionPolicyRequest:
    boto3_raw_data: "type_defs.PutRetentionPolicyRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    Name = field("Name")

    @cached_property
    def FolderConfigurations(self):  # pragma: no cover
        return FolderConfiguration.make_many(
            self.boto3_raw_data["FolderConfigurations"]
        )

    Id = field("Id")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRetentionPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRetentionPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImpersonationRoleEffectResponse:
    boto3_raw_data: "type_defs.GetImpersonationRoleEffectResponseTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Effect = field("Effect")

    @cached_property
    def MatchedRules(self):  # pragma: no cover
        return ImpersonationMatchedRule.make_many(self.boto3_raw_data["MatchedRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetImpersonationRoleEffectResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImpersonationRoleEffectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImpersonationRoleResponse:
    boto3_raw_data: "type_defs.GetImpersonationRoleResponseTypeDef" = (
        dataclasses.field()
    )

    ImpersonationRoleId = field("ImpersonationRoleId")
    Name = field("Name")
    Type = field("Type")
    Description = field("Description")

    @cached_property
    def Rules(self):  # pragma: no cover
        return ImpersonationRuleOutput.make_many(self.boto3_raw_data["Rules"])

    DateCreated = field("DateCreated")
    DateModified = field("DateModified")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImpersonationRoleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImpersonationRoleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMobileDeviceAccessEffectResponse:
    boto3_raw_data: "type_defs.GetMobileDeviceAccessEffectResponseTypeDef" = (
        dataclasses.field()
    )

    Effect = field("Effect")

    @cached_property
    def MatchedRules(self):  # pragma: no cover
        return MobileDeviceAccessMatchedRule.make_many(
            self.boto3_raw_data["MatchedRules"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMobileDeviceAccessEffectResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMobileDeviceAccessEffectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupsForEntityResponse:
    boto3_raw_data: "type_defs.ListGroupsForEntityResponseTypeDef" = dataclasses.field()

    @cached_property
    def Groups(self):  # pragma: no cover
        return GroupIdentifier.make_many(self.boto3_raw_data["Groups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsForEntityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsForEntityResponseTypeDef"]
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
class ListImpersonationRolesResponse:
    boto3_raw_data: "type_defs.ListImpersonationRolesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Roles(self):  # pragma: no cover
        return ImpersonationRole.make_many(self.boto3_raw_data["Roles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListImpersonationRolesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImpersonationRolesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesRequestPaginate:
    boto3_raw_data: "type_defs.ListAliasesRequestPaginateTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAliasesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailabilityConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListAvailabilityConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailabilityConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailabilityConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupMembersRequestPaginate:
    boto3_raw_data: "type_defs.ListGroupMembersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    GroupId = field("GroupId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGroupMembersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMailboxPermissionsRequestPaginate:
    boto3_raw_data: "type_defs.ListMailboxPermissionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMailboxPermissionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMailboxPermissionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationsRequestPaginate:
    boto3_raw_data: "type_defs.ListOrganizationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOrganizationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPersonalAccessTokensRequestPaginate:
    boto3_raw_data: "type_defs.ListPersonalAccessTokensRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    UserId = field("UserId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPersonalAccessTokensRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPersonalAccessTokensRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceDelegatesRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceDelegatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    ResourceId = field("ResourceId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceDelegatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceDelegatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGroupMembersResponse:
    boto3_raw_data: "type_defs.ListGroupMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Members(self):  # pragma: no cover
        return Member.make_many(self.boto3_raw_data["Members"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupMembersResponseTypeDef"]
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

    OrganizationId = field("OrganizationId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListGroupsFilters.make_one(self.boto3_raw_data["Filters"])

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
class ListGroupsRequest:
    boto3_raw_data: "type_defs.ListGroupsRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListGroupsFilters.make_one(self.boto3_raw_data["Filters"])

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
class ListGroupsForEntityRequest:
    boto3_raw_data: "type_defs.ListGroupsForEntityRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    EntityId = field("EntityId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListGroupsForEntityFilters.make_one(self.boto3_raw_data["Filters"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGroupsForEntityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGroupsForEntityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMailDomainsResponse:
    boto3_raw_data: "type_defs.ListMailDomainsResponseTypeDef" = dataclasses.field()

    @cached_property
    def MailDomains(self):  # pragma: no cover
        return MailDomainSummary.make_many(self.boto3_raw_data["MailDomains"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMailDomainsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMailDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMailboxExportJobsResponse:
    boto3_raw_data: "type_defs.ListMailboxExportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Jobs(self):  # pragma: no cover
        return MailboxExportJob.make_many(self.boto3_raw_data["Jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMailboxExportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMailboxExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMailboxPermissionsResponse:
    boto3_raw_data: "type_defs.ListMailboxPermissionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Permissions(self):  # pragma: no cover
        return Permission.make_many(self.boto3_raw_data["Permissions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMailboxPermissionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMailboxPermissionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMobileDeviceAccessOverridesResponse:
    boto3_raw_data: "type_defs.ListMobileDeviceAccessOverridesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Overrides(self):  # pragma: no cover
        return MobileDeviceAccessOverride.make_many(self.boto3_raw_data["Overrides"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMobileDeviceAccessOverridesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMobileDeviceAccessOverridesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMobileDeviceAccessRulesResponse:
    boto3_raw_data: "type_defs.ListMobileDeviceAccessRulesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Rules(self):  # pragma: no cover
        return MobileDeviceAccessRule.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMobileDeviceAccessRulesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMobileDeviceAccessRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationsResponse:
    boto3_raw_data: "type_defs.ListOrganizationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def OrganizationSummaries(self):  # pragma: no cover
        return OrganizationSummary.make_many(
            self.boto3_raw_data["OrganizationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListOrganizationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPersonalAccessTokensResponse:
    boto3_raw_data: "type_defs.ListPersonalAccessTokensResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PersonalAccessTokenSummaries(self):  # pragma: no cover
        return PersonalAccessTokenSummary.make_many(
            self.boto3_raw_data["PersonalAccessTokenSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPersonalAccessTokensResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPersonalAccessTokensResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListResourcesFilters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourcesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesRequest:
    boto3_raw_data: "type_defs.ListResourcesRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListResourcesFilters.make_one(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourcesResponse:
    boto3_raw_data: "type_defs.ListResourcesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Resources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["Resources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourcesResponseTypeDef"]
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

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class ListUsersRequestPaginate:
    boto3_raw_data: "type_defs.ListUsersRequestPaginateTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListUsersFilters.make_one(self.boto3_raw_data["Filters"])

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
class ListUsersRequest:
    boto3_raw_data: "type_defs.ListUsersRequestTypeDef" = dataclasses.field()

    OrganizationId = field("OrganizationId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ListUsersFilters.make_one(self.boto3_raw_data["Filters"])

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


@dataclasses.dataclass(frozen=True)
class ListAvailabilityConfigurationsResponse:
    boto3_raw_data: "type_defs.ListAvailabilityConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AvailabilityConfigurations(self):  # pragma: no cover
        return AvailabilityConfiguration.make_many(
            self.boto3_raw_data["AvailabilityConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailabilityConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailabilityConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateImpersonationRoleRequest:
    boto3_raw_data: "type_defs.CreateImpersonationRoleRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    Name = field("Name")
    Type = field("Type")
    Rules = field("Rules")
    ClientToken = field("ClientToken")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateImpersonationRoleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateImpersonationRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateImpersonationRoleRequest:
    boto3_raw_data: "type_defs.UpdateImpersonationRoleRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationId = field("OrganizationId")
    ImpersonationRoleId = field("ImpersonationRoleId")
    Name = field("Name")
    Type = field("Type")
    Rules = field("Rules")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateImpersonationRoleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateImpersonationRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
