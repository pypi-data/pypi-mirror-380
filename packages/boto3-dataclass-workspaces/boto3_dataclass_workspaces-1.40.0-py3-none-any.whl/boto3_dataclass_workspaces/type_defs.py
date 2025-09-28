# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_workspaces import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptAccountLinkInvitationRequest:
    boto3_raw_data: "type_defs.AcceptAccountLinkInvitationRequestTypeDef" = (
        dataclasses.field()
    )

    LinkId = field("LinkId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptAccountLinkInvitationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptAccountLinkInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountLink:
    boto3_raw_data: "type_defs.AccountLinkTypeDef" = dataclasses.field()

    AccountLinkId = field("AccountLinkId")
    AccountLinkStatus = field("AccountLinkStatus")
    SourceAccountId = field("SourceAccountId")
    TargetAccountId = field("TargetAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountLinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountLinkTypeDef"]]
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
class AccessEndpoint:
    boto3_raw_data: "type_defs.AccessEndpointTypeDef" = dataclasses.field()

    AccessEndpointType = field("AccessEndpointType")
    VpcEndpointId = field("VpcEndpointId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessEndpointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountModification:
    boto3_raw_data: "type_defs.AccountModificationTypeDef" = dataclasses.field()

    ModificationState = field("ModificationState")
    DedicatedTenancySupport = field("DedicatedTenancySupport")
    DedicatedTenancyManagementCidrRange = field("DedicatedTenancyManagementCidrRange")
    StartTime = field("StartTime")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountModificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountModificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActiveDirectoryConfig:
    boto3_raw_data: "type_defs.ActiveDirectoryConfigTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ServiceAccountSecretArn = field("ServiceAccountSecretArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActiveDirectoryConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActiveDirectoryConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociationStateReason:
    boto3_raw_data: "type_defs.AssociationStateReasonTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociationStateReasonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociationStateReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSettingsRequest:
    boto3_raw_data: "type_defs.ApplicationSettingsRequestTypeDef" = dataclasses.field()

    Status = field("Status")
    SettingsGroup = field("SettingsGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationSettingsResponse:
    boto3_raw_data: "type_defs.ApplicationSettingsResponseTypeDef" = dataclasses.field()

    Status = field("Status")
    SettingsGroup = field("SettingsGroup")
    S3BucketName = field("S3BucketName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateConnectionAliasRequest:
    boto3_raw_data: "type_defs.AssociateConnectionAliasRequestTypeDef" = (
        dataclasses.field()
    )

    AliasId = field("AliasId")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateConnectionAliasRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateConnectionAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateIpGroupsRequest:
    boto3_raw_data: "type_defs.AssociateIpGroupsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    GroupIds = field("GroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateIpGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateIpGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateWorkspaceApplicationRequest:
    boto3_raw_data: "type_defs.AssociateWorkspaceApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    WorkspaceId = field("WorkspaceId")
    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateWorkspaceApplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateWorkspaceApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpRuleItem:
    boto3_raw_data: "type_defs.IpRuleItemTypeDef" = dataclasses.field()

    ipRule = field("ipRule")
    ruleDesc = field("ruleDesc")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpRuleItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpRuleItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityStatus:
    boto3_raw_data: "type_defs.CapacityStatusTypeDef" = dataclasses.field()

    AvailableUserSessions = field("AvailableUserSessions")
    DesiredUserSessions = field("DesiredUserSessions")
    ActualUserSessions = field("ActualUserSessions")
    ActiveUserSessions = field("ActiveUserSessions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapacityStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CapacityStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Capacity:
    boto3_raw_data: "type_defs.CapacityTypeDef" = dataclasses.field()

    DesiredUserSessions = field("DesiredUserSessions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapacityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CapacityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateBasedAuthProperties:
    boto3_raw_data: "type_defs.CertificateBasedAuthPropertiesTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    CertificateAuthorityArn = field("CertificateAuthorityArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CertificateBasedAuthPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CertificateBasedAuthPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientProperties:
    boto3_raw_data: "type_defs.ClientPropertiesTypeDef" = dataclasses.field()

    ReconnectEnabled = field("ReconnectEnabled")
    LogUploadEnabled = field("LogUploadEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClientPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeType:
    boto3_raw_data: "type_defs.ComputeTypeTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputeTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComputeTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectClientAddIn:
    boto3_raw_data: "type_defs.ConnectClientAddInTypeDef" = dataclasses.field()

    AddInId = field("AddInId")
    ResourceId = field("ResourceId")
    Name = field("Name")
    URL = field("URL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectClientAddInTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectClientAddInTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionAliasAssociation:
    boto3_raw_data: "type_defs.ConnectionAliasAssociationTypeDef" = dataclasses.field()

    AssociationStatus = field("AssociationStatus")
    AssociatedAccountId = field("AssociatedAccountId")
    ResourceId = field("ResourceId")
    ConnectionIdentifier = field("ConnectionIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionAliasAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionAliasAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionAliasPermission:
    boto3_raw_data: "type_defs.ConnectionAliasPermissionTypeDef" = dataclasses.field()

    SharedAccountId = field("SharedAccountId")
    AllowAssociation = field("AllowAssociation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionAliasPermissionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionAliasPermissionTypeDef"]
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
class CreateAccountLinkInvitationRequest:
    boto3_raw_data: "type_defs.CreateAccountLinkInvitationRequestTypeDef" = (
        dataclasses.field()
    )

    TargetAccountId = field("TargetAccountId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAccountLinkInvitationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccountLinkInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectClientAddInRequest:
    boto3_raw_data: "type_defs.CreateConnectClientAddInRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")
    Name = field("Name")
    URL = field("URL")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConnectClientAddInRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectClientAddInRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingCreateStandbyWorkspacesRequest:
    boto3_raw_data: "type_defs.PendingCreateStandbyWorkspacesRequestTypeDef" = (
        dataclasses.field()
    )

    UserName = field("UserName")
    DirectoryId = field("DirectoryId")
    State = field("State")
    WorkspaceId = field("WorkspaceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PendingCreateStandbyWorkspacesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingCreateStandbyWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RootStorage:
    boto3_raw_data: "type_defs.RootStorageTypeDef" = dataclasses.field()

    Capacity = field("Capacity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RootStorageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RootStorageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserStorage:
    boto3_raw_data: "type_defs.UserStorageTypeDef" = dataclasses.field()

    Capacity = field("Capacity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserStorageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserStorageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperatingSystem:
    boto3_raw_data: "type_defs.OperatingSystemTypeDef" = dataclasses.field()

    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OperatingSystemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OperatingSystemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeoutSettings:
    boto3_raw_data: "type_defs.TimeoutSettingsTypeDef" = dataclasses.field()

    DisconnectTimeoutInSeconds = field("DisconnectTimeoutInSeconds")
    IdleDisconnectTimeoutInSeconds = field("IdleDisconnectTimeoutInSeconds")
    MaxUserDurationInSeconds = field("MaxUserDurationInSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeoutSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeoutSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomWorkspaceImageImportErrorDetails:
    boto3_raw_data: "type_defs.CustomWorkspaceImageImportErrorDetailsTypeDef" = (
        dataclasses.field()
    )

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomWorkspaceImageImportErrorDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomWorkspaceImageImportErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataReplicationSettings:
    boto3_raw_data: "type_defs.DataReplicationSettingsTypeDef" = dataclasses.field()

    DataReplication = field("DataReplication")
    RecoverySnapshotTime = field("RecoverySnapshotTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataReplicationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataReplicationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultClientBrandingAttributes:
    boto3_raw_data: "type_defs.DefaultClientBrandingAttributesTypeDef" = (
        dataclasses.field()
    )

    LogoUrl = field("LogoUrl")
    SupportEmail = field("SupportEmail")
    SupportLink = field("SupportLink")
    ForgotPasswordLink = field("ForgotPasswordLink")
    LoginMessage = field("LoginMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DefaultClientBrandingAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultClientBrandingAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultWorkspaceCreationProperties:
    boto3_raw_data: "type_defs.DefaultWorkspaceCreationPropertiesTypeDef" = (
        dataclasses.field()
    )

    EnableInternetAccess = field("EnableInternetAccess")
    DefaultOu = field("DefaultOu")
    CustomSecurityGroupId = field("CustomSecurityGroupId")
    UserEnabledAsLocalAdministrator = field("UserEnabledAsLocalAdministrator")
    EnableMaintenanceMode = field("EnableMaintenanceMode")
    InstanceIamRoleArn = field("InstanceIamRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DefaultWorkspaceCreationPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultWorkspaceCreationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountLinkInvitationRequest:
    boto3_raw_data: "type_defs.DeleteAccountLinkInvitationRequestTypeDef" = (
        dataclasses.field()
    )

    LinkId = field("LinkId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAccountLinkInvitationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccountLinkInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClientBrandingRequest:
    boto3_raw_data: "type_defs.DeleteClientBrandingRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    Platforms = field("Platforms")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClientBrandingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClientBrandingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectClientAddInRequest:
    boto3_raw_data: "type_defs.DeleteConnectClientAddInRequestTypeDef" = (
        dataclasses.field()
    )

    AddInId = field("AddInId")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteConnectClientAddInRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectClientAddInRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionAliasRequest:
    boto3_raw_data: "type_defs.DeleteConnectionAliasRequestTypeDef" = (
        dataclasses.field()
    )

    AliasId = field("AliasId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIpGroupRequest:
    boto3_raw_data: "type_defs.DeleteIpGroupRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIpGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIpGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTagsRequest:
    boto3_raw_data: "type_defs.DeleteTagsRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceBundleRequest:
    boto3_raw_data: "type_defs.DeleteWorkspaceBundleRequestTypeDef" = (
        dataclasses.field()
    )

    BundleId = field("BundleId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkspaceBundleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceBundleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkspaceImageRequest:
    boto3_raw_data: "type_defs.DeleteWorkspaceImageRequestTypeDef" = dataclasses.field()

    ImageId = field("ImageId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkspaceImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkspaceImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeployWorkspaceApplicationsRequest:
    boto3_raw_data: "type_defs.DeployWorkspaceApplicationsRequestTypeDef" = (
        dataclasses.field()
    )

    WorkspaceId = field("WorkspaceId")
    Force = field("Force")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeployWorkspaceApplicationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeployWorkspaceApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterWorkspaceDirectoryRequest:
    boto3_raw_data: "type_defs.DeregisterWorkspaceDirectoryRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterWorkspaceDirectoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterWorkspaceDirectoryRequestTypeDef"]
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
class DescribeAccountModificationsRequest:
    boto3_raw_data: "type_defs.DescribeAccountModificationsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountModificationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountModificationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationAssociationsRequest:
    boto3_raw_data: "type_defs.DescribeApplicationAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    AssociatedResourceTypes = field("AssociatedResourceTypes")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationsRequest:
    boto3_raw_data: "type_defs.DescribeApplicationsRequestTypeDef" = dataclasses.field()

    ApplicationIds = field("ApplicationIds")
    ComputeTypeNames = field("ComputeTypeNames")
    LicenseType = field("LicenseType")
    OperatingSystemNames = field("OperatingSystemNames")
    Owner = field("Owner")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkSpaceApplication:
    boto3_raw_data: "type_defs.WorkSpaceApplicationTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Created = field("Created")
    Description = field("Description")
    LicenseType = field("LicenseType")
    Name = field("Name")
    Owner = field("Owner")
    State = field("State")
    SupportedComputeTypeNames = field("SupportedComputeTypeNames")
    SupportedOperatingSystemNames = field("SupportedOperatingSystemNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkSpaceApplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkSpaceApplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBundleAssociationsRequest:
    boto3_raw_data: "type_defs.DescribeBundleAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    BundleId = field("BundleId")
    AssociatedResourceTypes = field("AssociatedResourceTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBundleAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBundleAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClientBrandingRequest:
    boto3_raw_data: "type_defs.DescribeClientBrandingRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClientBrandingRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClientBrandingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IosClientBrandingAttributes:
    boto3_raw_data: "type_defs.IosClientBrandingAttributesTypeDef" = dataclasses.field()

    LogoUrl = field("LogoUrl")
    Logo2xUrl = field("Logo2xUrl")
    Logo3xUrl = field("Logo3xUrl")
    SupportEmail = field("SupportEmail")
    SupportLink = field("SupportLink")
    ForgotPasswordLink = field("ForgotPasswordLink")
    LoginMessage = field("LoginMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IosClientBrandingAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IosClientBrandingAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClientPropertiesRequest:
    boto3_raw_data: "type_defs.DescribeClientPropertiesRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceIds = field("ResourceIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClientPropertiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClientPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectClientAddInsRequest:
    boto3_raw_data: "type_defs.DescribeConnectClientAddInsRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConnectClientAddInsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectClientAddInsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionAliasPermissionsRequest:
    boto3_raw_data: "type_defs.DescribeConnectionAliasPermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    AliasId = field("AliasId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConnectionAliasPermissionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionAliasPermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionAliasesRequest:
    boto3_raw_data: "type_defs.DescribeConnectionAliasesRequestTypeDef" = (
        dataclasses.field()
    )

    AliasIds = field("AliasIds")
    ResourceId = field("ResourceId")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConnectionAliasesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomWorkspaceImageImportRequest:
    boto3_raw_data: "type_defs.DescribeCustomWorkspaceImageImportRequestTypeDef" = (
        dataclasses.field()
    )

    ImageId = field("ImageId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomWorkspaceImageImportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomWorkspaceImageImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageSourceIdentifier:
    boto3_raw_data: "type_defs.ImageSourceIdentifierTypeDef" = dataclasses.field()

    Ec2ImportTaskId = field("Ec2ImportTaskId")
    ImageBuildVersionArn = field("ImageBuildVersionArn")
    Ec2ImageId = field("Ec2ImageId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageSourceIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageSourceIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageAssociationsRequest:
    boto3_raw_data: "type_defs.DescribeImageAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    ImageId = field("ImageId")
    AssociatedResourceTypes = field("AssociatedResourceTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeImageAssociationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIpGroupsRequest:
    boto3_raw_data: "type_defs.DescribeIpGroupsRequestTypeDef" = dataclasses.field()

    GroupIds = field("GroupIds")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIpGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIpGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsRequest:
    boto3_raw_data: "type_defs.DescribeTagsRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceAssociationsRequest:
    boto3_raw_data: "type_defs.DescribeWorkspaceAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    WorkspaceId = field("WorkspaceId")
    AssociatedResourceTypes = field("AssociatedResourceTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceBundlesRequest:
    boto3_raw_data: "type_defs.DescribeWorkspaceBundlesRequestTypeDef" = (
        dataclasses.field()
    )

    BundleIds = field("BundleIds")
    Owner = field("Owner")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorkspaceBundlesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceBundlesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceDirectoriesFilter:
    boto3_raw_data: "type_defs.DescribeWorkspaceDirectoriesFilterTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceDirectoriesFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceDirectoriesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceImagePermissionsRequest:
    boto3_raw_data: "type_defs.DescribeWorkspaceImagePermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    ImageId = field("ImageId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceImagePermissionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceImagePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImagePermission:
    boto3_raw_data: "type_defs.ImagePermissionTypeDef" = dataclasses.field()

    SharedAccountId = field("SharedAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImagePermissionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImagePermissionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceImagesRequest:
    boto3_raw_data: "type_defs.DescribeWorkspaceImagesRequestTypeDef" = (
        dataclasses.field()
    )

    ImageIds = field("ImageIds")
    ImageType = field("ImageType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorkspaceImagesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceImagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceSnapshotsRequest:
    boto3_raw_data: "type_defs.DescribeWorkspaceSnapshotsRequestTypeDef" = (
        dataclasses.field()
    )

    WorkspaceId = field("WorkspaceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceSnapshotsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceSnapshotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Snapshot:
    boto3_raw_data: "type_defs.SnapshotTypeDef" = dataclasses.field()

    SnapshotTime = field("SnapshotTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnapshotTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SnapshotTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspacesConnectionStatusRequest:
    boto3_raw_data: "type_defs.DescribeWorkspacesConnectionStatusRequestTypeDef" = (
        dataclasses.field()
    )

    WorkspaceIds = field("WorkspaceIds")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspacesConnectionStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspacesConnectionStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceConnectionStatus:
    boto3_raw_data: "type_defs.WorkspaceConnectionStatusTypeDef" = dataclasses.field()

    WorkspaceId = field("WorkspaceId")
    ConnectionState = field("ConnectionState")
    ConnectionStateCheckTimestamp = field("ConnectionStateCheckTimestamp")
    LastKnownUserConnectionTimestamp = field("LastKnownUserConnectionTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspaceConnectionStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceConnectionStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspacesPoolSessionsRequest:
    boto3_raw_data: "type_defs.DescribeWorkspacesPoolSessionsRequestTypeDef" = (
        dataclasses.field()
    )

    PoolId = field("PoolId")
    UserId = field("UserId")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspacesPoolSessionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspacesPoolSessionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspacesPoolsFilter:
    boto3_raw_data: "type_defs.DescribeWorkspacesPoolsFilterTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Values = field("Values")
    Operator = field("Operator")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorkspacesPoolsFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspacesPoolsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspacesRequest:
    boto3_raw_data: "type_defs.DescribeWorkspacesRequestTypeDef" = dataclasses.field()

    WorkspaceIds = field("WorkspaceIds")
    DirectoryId = field("DirectoryId")
    UserName = field("UserName")
    BundleId = field("BundleId")
    Limit = field("Limit")
    NextToken = field("NextToken")
    WorkspaceName = field("WorkspaceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorkspacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateConnectionAliasRequest:
    boto3_raw_data: "type_defs.DisassociateConnectionAliasRequestTypeDef" = (
        dataclasses.field()
    )

    AliasId = field("AliasId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateConnectionAliasRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateConnectionAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateIpGroupsRequest:
    boto3_raw_data: "type_defs.DisassociateIpGroupsRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    GroupIds = field("GroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateIpGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateIpGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateWorkspaceApplicationRequest:
    boto3_raw_data: "type_defs.DisassociateWorkspaceApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    WorkspaceId = field("WorkspaceId")
    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateWorkspaceApplicationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateWorkspaceApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetails:
    boto3_raw_data: "type_defs.ErrorDetailsTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedWorkspaceChangeRequest:
    boto3_raw_data: "type_defs.FailedWorkspaceChangeRequestTypeDef" = (
        dataclasses.field()
    )

    WorkspaceId = field("WorkspaceId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailedWorkspaceChangeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedWorkspaceChangeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountLinkRequest:
    boto3_raw_data: "type_defs.GetAccountLinkRequestTypeDef" = dataclasses.field()

    LinkId = field("LinkId")
    LinkedAccountId = field("LinkedAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountLinkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalAcceleratorForDirectory:
    boto3_raw_data: "type_defs.GlobalAcceleratorForDirectoryTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")
    PreferredProtocol = field("PreferredProtocol")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GlobalAcceleratorForDirectoryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalAcceleratorForDirectoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalAcceleratorForWorkSpace:
    boto3_raw_data: "type_defs.GlobalAcceleratorForWorkSpaceTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")
    PreferredProtocol = field("PreferredProtocol")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GlobalAcceleratorForWorkSpaceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlobalAcceleratorForWorkSpaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IDCConfig:
    boto3_raw_data: "type_defs.IDCConfigTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IDCConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IDCConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountLinksRequest:
    boto3_raw_data: "type_defs.ListAccountLinksRequestTypeDef" = dataclasses.field()

    LinkStatusFilter = field("LinkStatusFilter")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountLinksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountLinksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableManagementCidrRangesRequest:
    boto3_raw_data: "type_defs.ListAvailableManagementCidrRangesRequestTypeDef" = (
        dataclasses.field()
    )

    ManagementCidrRangeConstraint = field("ManagementCidrRangeConstraint")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableManagementCidrRangesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableManagementCidrRangesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MicrosoftEntraConfig:
    boto3_raw_data: "type_defs.MicrosoftEntraConfigTypeDef" = dataclasses.field()

    TenantId = field("TenantId")
    ApplicationConfigSecretArn = field("ApplicationConfigSecretArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MicrosoftEntraConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MicrosoftEntraConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MigrateWorkspaceRequest:
    boto3_raw_data: "type_defs.MigrateWorkspaceRequestTypeDef" = dataclasses.field()

    SourceWorkspaceId = field("SourceWorkspaceId")
    BundleId = field("BundleId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MigrateWorkspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MigrateWorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModificationState:
    boto3_raw_data: "type_defs.ModificationStateTypeDef" = dataclasses.field()

    Resource = field("Resource")
    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModificationStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModificationStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyAccountRequest:
    boto3_raw_data: "type_defs.ModifyAccountRequestTypeDef" = dataclasses.field()

    DedicatedTenancySupport = field("DedicatedTenancySupport")
    DedicatedTenancyManagementCidrRange = field("DedicatedTenancyManagementCidrRange")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyEndpointEncryptionModeRequest:
    boto3_raw_data: "type_defs.ModifyEndpointEncryptionModeRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    EndpointEncryptionMode = field("EndpointEncryptionMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyEndpointEncryptionModeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyEndpointEncryptionModeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamlProperties:
    boto3_raw_data: "type_defs.SamlPropertiesTypeDef" = dataclasses.field()

    Status = field("Status")
    UserAccessUrl = field("UserAccessUrl")
    RelayStateParameterName = field("RelayStateParameterName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SamlPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SamlPropertiesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfservicePermissions:
    boto3_raw_data: "type_defs.SelfservicePermissionsTypeDef" = dataclasses.field()

    RestartWorkspace = field("RestartWorkspace")
    IncreaseVolumeSize = field("IncreaseVolumeSize")
    ChangeComputeType = field("ChangeComputeType")
    SwitchRunningMode = field("SwitchRunningMode")
    RebuildWorkspace = field("RebuildWorkspace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelfservicePermissionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfservicePermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceCreationProperties:
    boto3_raw_data: "type_defs.WorkspaceCreationPropertiesTypeDef" = dataclasses.field()

    EnableInternetAccess = field("EnableInternetAccess")
    DefaultOu = field("DefaultOu")
    CustomSecurityGroupId = field("CustomSecurityGroupId")
    UserEnabledAsLocalAdministrator = field("UserEnabledAsLocalAdministrator")
    EnableMaintenanceMode = field("EnableMaintenanceMode")
    InstanceIamRoleArn = field("InstanceIamRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspaceCreationPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceCreationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyWorkspaceStateRequest:
    boto3_raw_data: "type_defs.ModifyWorkspaceStateRequestTypeDef" = dataclasses.field()

    WorkspaceId = field("WorkspaceId")
    WorkspaceState = field("WorkspaceState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyWorkspaceStateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyWorkspaceStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAccessConfiguration:
    boto3_raw_data: "type_defs.NetworkAccessConfigurationTypeDef" = dataclasses.field()

    EniPrivateIpAddress = field("EniPrivateIpAddress")
    EniId = field("EniId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NetworkAccessConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkAccessConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootRequest:
    boto3_raw_data: "type_defs.RebootRequestTypeDef" = dataclasses.field()

    WorkspaceId = field("WorkspaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RebootRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RebootRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebuildRequest:
    boto3_raw_data: "type_defs.RebuildRequestTypeDef" = dataclasses.field()

    WorkspaceId = field("WorkspaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RebuildRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RebuildRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectAccountLinkInvitationRequest:
    boto3_raw_data: "type_defs.RejectAccountLinkInvitationRequestTypeDef" = (
        dataclasses.field()
    )

    LinkId = field("LinkId")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectAccountLinkInvitationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectAccountLinkInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedWorkspaceProperties:
    boto3_raw_data: "type_defs.RelatedWorkspacePropertiesTypeDef" = dataclasses.field()

    WorkspaceId = field("WorkspaceId")
    Region = field("Region")
    State = field("State")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelatedWorkspacePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelatedWorkspacePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreWorkspaceRequest:
    boto3_raw_data: "type_defs.RestoreWorkspaceRequestTypeDef" = dataclasses.field()

    WorkspaceId = field("WorkspaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreWorkspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreWorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeIpRulesRequest:
    boto3_raw_data: "type_defs.RevokeIpRulesRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")
    UserRules = field("UserRules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeIpRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeIpRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StandbyWorkspacesProperties:
    boto3_raw_data: "type_defs.StandbyWorkspacesPropertiesTypeDef" = dataclasses.field()

    StandbyWorkspaceId = field("StandbyWorkspaceId")
    DataReplication = field("DataReplication")
    RecoverySnapshotTime = field("RecoverySnapshotTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StandbyWorkspacesPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StandbyWorkspacesPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRequest:
    boto3_raw_data: "type_defs.StartRequestTypeDef" = dataclasses.field()

    WorkspaceId = field("WorkspaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartWorkspacesPoolRequest:
    boto3_raw_data: "type_defs.StartWorkspacesPoolRequestTypeDef" = dataclasses.field()

    PoolId = field("PoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartWorkspacesPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartWorkspacesPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopRequest:
    boto3_raw_data: "type_defs.StopRequestTypeDef" = dataclasses.field()

    WorkspaceId = field("WorkspaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopRequestTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopWorkspacesPoolRequest:
    boto3_raw_data: "type_defs.StopWorkspacesPoolRequestTypeDef" = dataclasses.field()

    PoolId = field("PoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopWorkspacesPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopWorkspacesPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageConnector:
    boto3_raw_data: "type_defs.StorageConnectorTypeDef" = dataclasses.field()

    ConnectorType = field("ConnectorType")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StorageConnectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageConnectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserSetting:
    boto3_raw_data: "type_defs.UserSettingTypeDef" = dataclasses.field()

    Action = field("Action")
    Permission = field("Permission")
    MaximumLength = field("MaximumLength")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserSettingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateRequest:
    boto3_raw_data: "type_defs.TerminateRequestTypeDef" = dataclasses.field()

    WorkspaceId = field("WorkspaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TerminateRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateWorkspacesPoolRequest:
    boto3_raw_data: "type_defs.TerminateWorkspacesPoolRequestTypeDef" = (
        dataclasses.field()
    )

    PoolId = field("PoolId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TerminateWorkspacesPoolRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateWorkspacesPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateWorkspacesPoolSessionRequest:
    boto3_raw_data: "type_defs.TerminateWorkspacesPoolSessionRequestTypeDef" = (
        dataclasses.field()
    )

    SessionId = field("SessionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TerminateWorkspacesPoolSessionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateWorkspacesPoolSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectClientAddInRequest:
    boto3_raw_data: "type_defs.UpdateConnectClientAddInRequestTypeDef" = (
        dataclasses.field()
    )

    AddInId = field("AddInId")
    ResourceId = field("ResourceId")
    Name = field("Name")
    URL = field("URL")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateConnectClientAddInRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectClientAddInRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResult:
    boto3_raw_data: "type_defs.UpdateResultTypeDef" = dataclasses.field()

    UpdateAvailable = field("UpdateAvailable")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkspaceBundleRequest:
    boto3_raw_data: "type_defs.UpdateWorkspaceBundleRequestTypeDef" = (
        dataclasses.field()
    )

    BundleId = field("BundleId")
    ImageId = field("ImageId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkspaceBundleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkspaceBundleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkspaceImagePermissionRequest:
    boto3_raw_data: "type_defs.UpdateWorkspaceImagePermissionRequestTypeDef" = (
        dataclasses.field()
    )

    ImageId = field("ImageId")
    AllowCopyImage = field("AllowCopyImage")
    SharedAccountId = field("SharedAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateWorkspaceImagePermissionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkspaceImagePermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspacesPoolError:
    boto3_raw_data: "type_defs.WorkspacesPoolErrorTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspacesPoolErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspacesPoolErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptAccountLinkInvitationResult:
    boto3_raw_data: "type_defs.AcceptAccountLinkInvitationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountLink(self):  # pragma: no cover
        return AccountLink.make_one(self.boto3_raw_data["AccountLink"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AcceptAccountLinkInvitationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptAccountLinkInvitationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateConnectionAliasResult:
    boto3_raw_data: "type_defs.AssociateConnectionAliasResultTypeDef" = (
        dataclasses.field()
    )

    ConnectionIdentifier = field("ConnectionIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateConnectionAliasResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateConnectionAliasResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyWorkspaceImageResult:
    boto3_raw_data: "type_defs.CopyWorkspaceImageResultTypeDef" = dataclasses.field()

    ImageId = field("ImageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyWorkspaceImageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyWorkspaceImageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccountLinkInvitationResult:
    boto3_raw_data: "type_defs.CreateAccountLinkInvitationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountLink(self):  # pragma: no cover
        return AccountLink.make_one(self.boto3_raw_data["AccountLink"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAccountLinkInvitationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccountLinkInvitationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectClientAddInResult:
    boto3_raw_data: "type_defs.CreateConnectClientAddInResultTypeDef" = (
        dataclasses.field()
    )

    AddInId = field("AddInId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConnectClientAddInResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectClientAddInResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionAliasResult:
    boto3_raw_data: "type_defs.CreateConnectionAliasResultTypeDef" = dataclasses.field()

    AliasId = field("AliasId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionAliasResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionAliasResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIpGroupResult:
    boto3_raw_data: "type_defs.CreateIpGroupResultTypeDef" = dataclasses.field()

    GroupId = field("GroupId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIpGroupResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIpGroupResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUpdatedWorkspaceImageResult:
    boto3_raw_data: "type_defs.CreateUpdatedWorkspaceImageResultTypeDef" = (
        dataclasses.field()
    )

    ImageId = field("ImageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateUpdatedWorkspaceImageResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUpdatedWorkspaceImageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountLinkInvitationResult:
    boto3_raw_data: "type_defs.DeleteAccountLinkInvitationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountLink(self):  # pragma: no cover
        return AccountLink.make_one(self.boto3_raw_data["AccountLink"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAccountLinkInvitationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccountLinkInvitationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountResult:
    boto3_raw_data: "type_defs.DescribeAccountResultTypeDef" = dataclasses.field()

    DedicatedTenancySupport = field("DedicatedTenancySupport")
    DedicatedTenancyManagementCidrRange = field("DedicatedTenancyManagementCidrRange")
    DedicatedTenancyAccountType = field("DedicatedTenancyAccountType")
    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccountResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountLinkResult:
    boto3_raw_data: "type_defs.GetAccountLinkResultTypeDef" = dataclasses.field()

    @cached_property
    def AccountLink(self):  # pragma: no cover
        return AccountLink.make_one(self.boto3_raw_data["AccountLink"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountLinkResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountLinkResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportCustomWorkspaceImageResult:
    boto3_raw_data: "type_defs.ImportCustomWorkspaceImageResultTypeDef" = (
        dataclasses.field()
    )

    ImageId = field("ImageId")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ImportCustomWorkspaceImageResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportCustomWorkspaceImageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportWorkspaceImageResult:
    boto3_raw_data: "type_defs.ImportWorkspaceImageResultTypeDef" = dataclasses.field()

    ImageId = field("ImageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportWorkspaceImageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportWorkspaceImageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountLinksResult:
    boto3_raw_data: "type_defs.ListAccountLinksResultTypeDef" = dataclasses.field()

    @cached_property
    def AccountLinks(self):  # pragma: no cover
        return AccountLink.make_many(self.boto3_raw_data["AccountLinks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountLinksResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountLinksResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableManagementCidrRangesResult:
    boto3_raw_data: "type_defs.ListAvailableManagementCidrRangesResultTypeDef" = (
        dataclasses.field()
    )

    ManagementCidrRanges = field("ManagementCidrRanges")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableManagementCidrRangesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableManagementCidrRangesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MigrateWorkspaceResult:
    boto3_raw_data: "type_defs.MigrateWorkspaceResultTypeDef" = dataclasses.field()

    SourceWorkspaceId = field("SourceWorkspaceId")
    TargetWorkspaceId = field("TargetWorkspaceId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MigrateWorkspaceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MigrateWorkspaceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyAccountResult:
    boto3_raw_data: "type_defs.ModifyAccountResultTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyAccountResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyAccountResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterWorkspaceDirectoryResult:
    boto3_raw_data: "type_defs.RegisterWorkspaceDirectoryResultTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RegisterWorkspaceDirectoryResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterWorkspaceDirectoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectAccountLinkInvitationResult:
    boto3_raw_data: "type_defs.RejectAccountLinkInvitationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountLink(self):  # pragma: no cover
        return AccountLink.make_one(self.boto3_raw_data["AccountLink"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RejectAccountLinkInvitationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectAccountLinkInvitationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessEndpointConfigOutput:
    boto3_raw_data: "type_defs.AccessEndpointConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def AccessEndpoints(self):  # pragma: no cover
        return AccessEndpoint.make_many(self.boto3_raw_data["AccessEndpoints"])

    InternetFallbackProtocols = field("InternetFallbackProtocols")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessEndpointConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessEndpointConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessEndpointConfig:
    boto3_raw_data: "type_defs.AccessEndpointConfigTypeDef" = dataclasses.field()

    @cached_property
    def AccessEndpoints(self):  # pragma: no cover
        return AccessEndpoint.make_many(self.boto3_raw_data["AccessEndpoints"])

    InternetFallbackProtocols = field("InternetFallbackProtocols")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessEndpointConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessEndpointConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountModificationsResult:
    boto3_raw_data: "type_defs.DescribeAccountModificationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountModifications(self):  # pragma: no cover
        return AccountModification.make_many(
            self.boto3_raw_data["AccountModifications"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountModificationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountModificationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationResourceAssociation:
    boto3_raw_data: "type_defs.ApplicationResourceAssociationTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    AssociatedResourceId = field("AssociatedResourceId")
    AssociatedResourceType = field("AssociatedResourceType")
    Created = field("Created")
    LastUpdatedTime = field("LastUpdatedTime")
    State = field("State")

    @cached_property
    def StateReason(self):  # pragma: no cover
        return AssociationStateReason.make_one(self.boto3_raw_data["StateReason"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApplicationResourceAssociationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationResourceAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BundleResourceAssociation:
    boto3_raw_data: "type_defs.BundleResourceAssociationTypeDef" = dataclasses.field()

    AssociatedResourceId = field("AssociatedResourceId")
    AssociatedResourceType = field("AssociatedResourceType")
    BundleId = field("BundleId")
    Created = field("Created")
    LastUpdatedTime = field("LastUpdatedTime")
    State = field("State")

    @cached_property
    def StateReason(self):  # pragma: no cover
        return AssociationStateReason.make_one(self.boto3_raw_data["StateReason"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BundleResourceAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BundleResourceAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageResourceAssociation:
    boto3_raw_data: "type_defs.ImageResourceAssociationTypeDef" = dataclasses.field()

    AssociatedResourceId = field("AssociatedResourceId")
    AssociatedResourceType = field("AssociatedResourceType")
    Created = field("Created")
    LastUpdatedTime = field("LastUpdatedTime")
    ImageId = field("ImageId")
    State = field("State")

    @cached_property
    def StateReason(self):  # pragma: no cover
        return AssociationStateReason.make_one(self.boto3_raw_data["StateReason"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageResourceAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageResourceAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceResourceAssociation:
    boto3_raw_data: "type_defs.WorkspaceResourceAssociationTypeDef" = (
        dataclasses.field()
    )

    AssociatedResourceId = field("AssociatedResourceId")
    AssociatedResourceType = field("AssociatedResourceType")
    Created = field("Created")
    LastUpdatedTime = field("LastUpdatedTime")
    State = field("State")

    @cached_property
    def StateReason(self):  # pragma: no cover
        return AssociationStateReason.make_one(self.boto3_raw_data["StateReason"])

    WorkspaceId = field("WorkspaceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspaceResourceAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceResourceAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizeIpRulesRequest:
    boto3_raw_data: "type_defs.AuthorizeIpRulesRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")

    @cached_property
    def UserRules(self):  # pragma: no cover
        return IpRuleItem.make_many(self.boto3_raw_data["UserRules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizeIpRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizeIpRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRulesOfIpGroupRequest:
    boto3_raw_data: "type_defs.UpdateRulesOfIpGroupRequestTypeDef" = dataclasses.field()

    GroupId = field("GroupId")

    @cached_property
    def UserRules(self):  # pragma: no cover
        return IpRuleItem.make_many(self.boto3_raw_data["UserRules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRulesOfIpGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRulesOfIpGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspacesIpGroup:
    boto3_raw_data: "type_defs.WorkspacesIpGroupTypeDef" = dataclasses.field()

    groupId = field("groupId")
    groupName = field("groupName")
    groupDesc = field("groupDesc")

    @cached_property
    def userRules(self):  # pragma: no cover
        return IpRuleItem.make_many(self.boto3_raw_data["userRules"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkspacesIpGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspacesIpGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultImportClientBrandingAttributes:
    boto3_raw_data: "type_defs.DefaultImportClientBrandingAttributesTypeDef" = (
        dataclasses.field()
    )

    Logo = field("Logo")
    SupportEmail = field("SupportEmail")
    SupportLink = field("SupportLink")
    ForgotPasswordLink = field("ForgotPasswordLink")
    LoginMessage = field("LoginMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DefaultImportClientBrandingAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultImportClientBrandingAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IosImportClientBrandingAttributes:
    boto3_raw_data: "type_defs.IosImportClientBrandingAttributesTypeDef" = (
        dataclasses.field()
    )

    Logo = field("Logo")
    Logo2x = field("Logo2x")
    Logo3x = field("Logo3x")
    SupportEmail = field("SupportEmail")
    SupportLink = field("SupportLink")
    ForgotPasswordLink = field("ForgotPasswordLink")
    LoginMessage = field("LoginMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IosImportClientBrandingAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IosImportClientBrandingAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCertificateBasedAuthPropertiesRequest:
    boto3_raw_data: "type_defs.ModifyCertificateBasedAuthPropertiesRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")

    @cached_property
    def CertificateBasedAuthProperties(self):  # pragma: no cover
        return CertificateBasedAuthProperties.make_one(
            self.boto3_raw_data["CertificateBasedAuthProperties"]
        )

    PropertiesToDelete = field("PropertiesToDelete")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyCertificateBasedAuthPropertiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCertificateBasedAuthPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientPropertiesResult:
    boto3_raw_data: "type_defs.ClientPropertiesResultTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @cached_property
    def ClientProperties(self):  # pragma: no cover
        return ClientProperties.make_one(self.boto3_raw_data["ClientProperties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClientPropertiesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClientPropertiesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyClientPropertiesRequest:
    boto3_raw_data: "type_defs.ModifyClientPropertiesRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")

    @cached_property
    def ClientProperties(self):  # pragma: no cover
        return ClientProperties.make_one(self.boto3_raw_data["ClientProperties"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyClientPropertiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyClientPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectClientAddInsResult:
    boto3_raw_data: "type_defs.DescribeConnectClientAddInsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AddIns(self):  # pragma: no cover
        return ConnectClientAddIn.make_many(self.boto3_raw_data["AddIns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConnectClientAddInsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectClientAddInsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionAlias:
    boto3_raw_data: "type_defs.ConnectionAliasTypeDef" = dataclasses.field()

    ConnectionString = field("ConnectionString")
    AliasId = field("AliasId")
    State = field("State")
    OwnerAccountId = field("OwnerAccountId")

    @cached_property
    def Associations(self):  # pragma: no cover
        return ConnectionAliasAssociation.make_many(self.boto3_raw_data["Associations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionAliasTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectionAliasTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionAliasPermissionsResult:
    boto3_raw_data: "type_defs.DescribeConnectionAliasPermissionsResultTypeDef" = (
        dataclasses.field()
    )

    AliasId = field("AliasId")

    @cached_property
    def ConnectionAliasPermissions(self):  # pragma: no cover
        return ConnectionAliasPermission.make_many(
            self.boto3_raw_data["ConnectionAliasPermissions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConnectionAliasPermissionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionAliasPermissionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionAliasPermissionRequest:
    boto3_raw_data: "type_defs.UpdateConnectionAliasPermissionRequestTypeDef" = (
        dataclasses.field()
    )

    AliasId = field("AliasId")

    @cached_property
    def ConnectionAliasPermission(self):  # pragma: no cover
        return ConnectionAliasPermission.make_one(
            self.boto3_raw_data["ConnectionAliasPermission"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConnectionAliasPermissionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionAliasPermissionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyWorkspaceImageRequest:
    boto3_raw_data: "type_defs.CopyWorkspaceImageRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    SourceImageId = field("SourceImageId")
    SourceRegion = field("SourceRegion")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CopyWorkspaceImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CopyWorkspaceImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionAliasRequest:
    boto3_raw_data: "type_defs.CreateConnectionAliasRequestTypeDef" = (
        dataclasses.field()
    )

    ConnectionString = field("ConnectionString")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIpGroupRequest:
    boto3_raw_data: "type_defs.CreateIpGroupRequestTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    GroupDesc = field("GroupDesc")

    @cached_property
    def UserRules(self):  # pragma: no cover
        return IpRuleItem.make_many(self.boto3_raw_data["UserRules"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIpGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIpGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTagsRequest:
    boto3_raw_data: "type_defs.CreateTagsRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUpdatedWorkspaceImageRequest:
    boto3_raw_data: "type_defs.CreateUpdatedWorkspaceImageRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Description = field("Description")
    SourceImageId = field("SourceImageId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateUpdatedWorkspaceImageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUpdatedWorkspaceImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceImageRequest:
    boto3_raw_data: "type_defs.CreateWorkspaceImageRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    WorkspaceId = field("WorkspaceId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspaceImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsResult:
    boto3_raw_data: "type_defs.DescribeTagsResultTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportWorkspaceImageRequest:
    boto3_raw_data: "type_defs.ImportWorkspaceImageRequestTypeDef" = dataclasses.field()

    Ec2ImageId = field("Ec2ImageId")
    IngestionProcess = field("IngestionProcess")
    ImageName = field("ImageName")
    ImageDescription = field("ImageDescription")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Applications = field("Applications")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportWorkspaceImageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportWorkspaceImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StandbyWorkspaceOutput:
    boto3_raw_data: "type_defs.StandbyWorkspaceOutputTypeDef" = dataclasses.field()

    PrimaryWorkspaceId = field("PrimaryWorkspaceId")
    DirectoryId = field("DirectoryId")
    VolumeEncryptionKey = field("VolumeEncryptionKey")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DataReplication = field("DataReplication")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StandbyWorkspaceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StandbyWorkspaceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StandbyWorkspace:
    boto3_raw_data: "type_defs.StandbyWorkspaceTypeDef" = dataclasses.field()

    PrimaryWorkspaceId = field("PrimaryWorkspaceId")
    DirectoryId = field("DirectoryId")
    VolumeEncryptionKey = field("VolumeEncryptionKey")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DataReplication = field("DataReplication")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StandbyWorkspaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StandbyWorkspaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceBundleRequest:
    boto3_raw_data: "type_defs.CreateWorkspaceBundleRequestTypeDef" = (
        dataclasses.field()
    )

    BundleName = field("BundleName")
    BundleDescription = field("BundleDescription")
    ImageId = field("ImageId")

    @cached_property
    def ComputeType(self):  # pragma: no cover
        return ComputeType.make_one(self.boto3_raw_data["ComputeType"])

    @cached_property
    def UserStorage(self):  # pragma: no cover
        return UserStorage.make_one(self.boto3_raw_data["UserStorage"])

    @cached_property
    def RootStorage(self):  # pragma: no cover
        return RootStorage.make_one(self.boto3_raw_data["RootStorage"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspaceBundleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceBundleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceBundle:
    boto3_raw_data: "type_defs.WorkspaceBundleTypeDef" = dataclasses.field()

    BundleId = field("BundleId")
    Name = field("Name")
    Owner = field("Owner")
    Description = field("Description")
    ImageId = field("ImageId")

    @cached_property
    def RootStorage(self):  # pragma: no cover
        return RootStorage.make_one(self.boto3_raw_data["RootStorage"])

    @cached_property
    def UserStorage(self):  # pragma: no cover
        return UserStorage.make_one(self.boto3_raw_data["UserStorage"])

    @cached_property
    def ComputeType(self):  # pragma: no cover
        return ComputeType.make_one(self.boto3_raw_data["ComputeType"])

    LastUpdatedTime = field("LastUpdatedTime")
    CreationTime = field("CreationTime")
    State = field("State")
    BundleType = field("BundleType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkspaceBundleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkspaceBundleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceImageResult:
    boto3_raw_data: "type_defs.CreateWorkspaceImageResultTypeDef" = dataclasses.field()

    ImageId = field("ImageId")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def OperatingSystem(self):  # pragma: no cover
        return OperatingSystem.make_one(self.boto3_raw_data["OperatingSystem"])

    State = field("State")
    RequiredTenancy = field("RequiredTenancy")
    Created = field("Created")
    OwnerAccountId = field("OwnerAccountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspaceImageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceImageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspacesPoolRequest:
    boto3_raw_data: "type_defs.CreateWorkspacesPoolRequestTypeDef" = dataclasses.field()

    PoolName = field("PoolName")
    Description = field("Description")
    BundleId = field("BundleId")
    DirectoryId = field("DirectoryId")

    @cached_property
    def Capacity(self):  # pragma: no cover
        return Capacity.make_one(self.boto3_raw_data["Capacity"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ApplicationSettings(self):  # pragma: no cover
        return ApplicationSettingsRequest.make_one(
            self.boto3_raw_data["ApplicationSettings"]
        )

    @cached_property
    def TimeoutSettings(self):  # pragma: no cover
        return TimeoutSettings.make_one(self.boto3_raw_data["TimeoutSettings"])

    RunningMode = field("RunningMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspacesPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspacesPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkspacesPoolRequest:
    boto3_raw_data: "type_defs.UpdateWorkspacesPoolRequestTypeDef" = dataclasses.field()

    PoolId = field("PoolId")
    Description = field("Description")
    BundleId = field("BundleId")
    DirectoryId = field("DirectoryId")

    @cached_property
    def Capacity(self):  # pragma: no cover
        return Capacity.make_one(self.boto3_raw_data["Capacity"])

    @cached_property
    def ApplicationSettings(self):  # pragma: no cover
        return ApplicationSettingsRequest.make_one(
            self.boto3_raw_data["ApplicationSettings"]
        )

    @cached_property
    def TimeoutSettings(self):  # pragma: no cover
        return TimeoutSettings.make_one(self.boto3_raw_data["TimeoutSettings"])

    RunningMode = field("RunningMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkspacesPoolRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkspacesPoolRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountModificationsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeAccountModificationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountModificationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountModificationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIpGroupsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeIpGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    GroupIds = field("GroupIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeIpGroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIpGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceBundlesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeWorkspaceBundlesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    BundleIds = field("BundleIds")
    Owner = field("Owner")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceBundlesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceBundlesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceImagesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeWorkspaceImagesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ImageIds = field("ImageIds")
    ImageType = field("ImageType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceImagesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceImagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspacesConnectionStatusRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeWorkspacesConnectionStatusRequestPaginateTypeDef"
    ) = dataclasses.field()

    WorkspaceIds = field("WorkspaceIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspacesConnectionStatusRequestPaginateTypeDef"
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
                "type_defs.DescribeWorkspacesConnectionStatusRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspacesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeWorkspacesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    WorkspaceIds = field("WorkspaceIds")
    DirectoryId = field("DirectoryId")
    UserName = field("UserName")
    BundleId = field("BundleId")
    WorkspaceName = field("WorkspaceName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspacesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspacesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountLinksRequestPaginate:
    boto3_raw_data: "type_defs.ListAccountLinksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    LinkStatusFilter = field("LinkStatusFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountLinksRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountLinksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableManagementCidrRangesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAvailableManagementCidrRangesRequestPaginateTypeDef"
    ) = dataclasses.field()

    ManagementCidrRangeConstraint = field("ManagementCidrRangeConstraint")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableManagementCidrRangesRequestPaginateTypeDef"
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
                "type_defs.ListAvailableManagementCidrRangesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationsResult:
    boto3_raw_data: "type_defs.DescribeApplicationsResultTypeDef" = dataclasses.field()

    @cached_property
    def Applications(self):  # pragma: no cover
        return WorkSpaceApplication.make_many(self.boto3_raw_data["Applications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClientBrandingResult:
    boto3_raw_data: "type_defs.DescribeClientBrandingResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DeviceTypeWindows(self):  # pragma: no cover
        return DefaultClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeWindows"]
        )

    @cached_property
    def DeviceTypeOsx(self):  # pragma: no cover
        return DefaultClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeOsx"]
        )

    @cached_property
    def DeviceTypeAndroid(self):  # pragma: no cover
        return DefaultClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeAndroid"]
        )

    @cached_property
    def DeviceTypeIos(self):  # pragma: no cover
        return IosClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeIos"]
        )

    @cached_property
    def DeviceTypeLinux(self):  # pragma: no cover
        return DefaultClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeLinux"]
        )

    @cached_property
    def DeviceTypeWeb(self):  # pragma: no cover
        return DefaultClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeWeb"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClientBrandingResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClientBrandingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportClientBrandingResult:
    boto3_raw_data: "type_defs.ImportClientBrandingResultTypeDef" = dataclasses.field()

    @cached_property
    def DeviceTypeWindows(self):  # pragma: no cover
        return DefaultClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeWindows"]
        )

    @cached_property
    def DeviceTypeOsx(self):  # pragma: no cover
        return DefaultClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeOsx"]
        )

    @cached_property
    def DeviceTypeAndroid(self):  # pragma: no cover
        return DefaultClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeAndroid"]
        )

    @cached_property
    def DeviceTypeIos(self):  # pragma: no cover
        return IosClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeIos"]
        )

    @cached_property
    def DeviceTypeLinux(self):  # pragma: no cover
        return DefaultClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeLinux"]
        )

    @cached_property
    def DeviceTypeWeb(self):  # pragma: no cover
        return DefaultClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeWeb"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportClientBrandingResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportClientBrandingResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomWorkspaceImageImportResult:
    boto3_raw_data: "type_defs.DescribeCustomWorkspaceImageImportResultTypeDef" = (
        dataclasses.field()
    )

    ImageId = field("ImageId")
    InfrastructureConfigurationArn = field("InfrastructureConfigurationArn")
    State = field("State")
    Created = field("Created")
    LastUpdatedTime = field("LastUpdatedTime")

    @cached_property
    def ImageSource(self):  # pragma: no cover
        return ImageSourceIdentifier.make_one(self.boto3_raw_data["ImageSource"])

    ImageBuilderInstanceId = field("ImageBuilderInstanceId")

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return CustomWorkspaceImageImportErrorDetails.make_many(
            self.boto3_raw_data["ErrorDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomWorkspaceImageImportResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomWorkspaceImageImportResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportCustomWorkspaceImageRequest:
    boto3_raw_data: "type_defs.ImportCustomWorkspaceImageRequestTypeDef" = (
        dataclasses.field()
    )

    ImageName = field("ImageName")
    ImageDescription = field("ImageDescription")
    ComputeType = field("ComputeType")
    Protocol = field("Protocol")

    @cached_property
    def ImageSource(self):  # pragma: no cover
        return ImageSourceIdentifier.make_one(self.boto3_raw_data["ImageSource"])

    InfrastructureConfigurationArn = field("InfrastructureConfigurationArn")
    Platform = field("Platform")
    OsVersion = field("OsVersion")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportCustomWorkspaceImageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportCustomWorkspaceImageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceDirectoriesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeWorkspaceDirectoriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryIds = field("DirectoryIds")
    WorkspaceDirectoryNames = field("WorkspaceDirectoryNames")
    Limit = field("Limit")

    @cached_property
    def Filters(self):  # pragma: no cover
        return DescribeWorkspaceDirectoriesFilter.make_many(
            self.boto3_raw_data["Filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceDirectoriesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceDirectoriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceDirectoriesRequest:
    boto3_raw_data: "type_defs.DescribeWorkspaceDirectoriesRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryIds = field("DirectoryIds")
    WorkspaceDirectoryNames = field("WorkspaceDirectoryNames")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return DescribeWorkspaceDirectoriesFilter.make_many(
            self.boto3_raw_data["Filters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceDirectoriesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceDirectoriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceImagePermissionsResult:
    boto3_raw_data: "type_defs.DescribeWorkspaceImagePermissionsResultTypeDef" = (
        dataclasses.field()
    )

    ImageId = field("ImageId")

    @cached_property
    def ImagePermissions(self):  # pragma: no cover
        return ImagePermission.make_many(self.boto3_raw_data["ImagePermissions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceImagePermissionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceImagePermissionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceSnapshotsResult:
    boto3_raw_data: "type_defs.DescribeWorkspaceSnapshotsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RebuildSnapshots(self):  # pragma: no cover
        return Snapshot.make_many(self.boto3_raw_data["RebuildSnapshots"])

    @cached_property
    def RestoreSnapshots(self):  # pragma: no cover
        return Snapshot.make_many(self.boto3_raw_data["RestoreSnapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorkspaceSnapshotsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceSnapshotsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspacesConnectionStatusResult:
    boto3_raw_data: "type_defs.DescribeWorkspacesConnectionStatusResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WorkspacesConnectionStatus(self):  # pragma: no cover
        return WorkspaceConnectionStatus.make_many(
            self.boto3_raw_data["WorkspacesConnectionStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspacesConnectionStatusResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspacesConnectionStatusResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspacesPoolsRequest:
    boto3_raw_data: "type_defs.DescribeWorkspacesPoolsRequestTypeDef" = (
        dataclasses.field()
    )

    PoolIds = field("PoolIds")

    @cached_property
    def Filters(self):  # pragma: no cover
        return DescribeWorkspacesPoolsFilter.make_many(self.boto3_raw_data["Filters"])

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorkspacesPoolsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspacesPoolsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootWorkspacesResult:
    boto3_raw_data: "type_defs.RebootWorkspacesResultTypeDef" = dataclasses.field()

    @cached_property
    def FailedRequests(self):  # pragma: no cover
        return FailedWorkspaceChangeRequest.make_many(
            self.boto3_raw_data["FailedRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootWorkspacesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootWorkspacesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebuildWorkspacesResult:
    boto3_raw_data: "type_defs.RebuildWorkspacesResultTypeDef" = dataclasses.field()

    @cached_property
    def FailedRequests(self):  # pragma: no cover
        return FailedWorkspaceChangeRequest.make_many(
            self.boto3_raw_data["FailedRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebuildWorkspacesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebuildWorkspacesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartWorkspacesResult:
    boto3_raw_data: "type_defs.StartWorkspacesResultTypeDef" = dataclasses.field()

    @cached_property
    def FailedRequests(self):  # pragma: no cover
        return FailedWorkspaceChangeRequest.make_many(
            self.boto3_raw_data["FailedRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartWorkspacesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartWorkspacesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopWorkspacesResult:
    boto3_raw_data: "type_defs.StopWorkspacesResultTypeDef" = dataclasses.field()

    @cached_property
    def FailedRequests(self):  # pragma: no cover
        return FailedWorkspaceChangeRequest.make_many(
            self.boto3_raw_data["FailedRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopWorkspacesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopWorkspacesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateWorkspacesResult:
    boto3_raw_data: "type_defs.TerminateWorkspacesResultTypeDef" = dataclasses.field()

    @cached_property
    def FailedRequests(self):  # pragma: no cover
        return FailedWorkspaceChangeRequest.make_many(
            self.boto3_raw_data["FailedRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateWorkspacesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateWorkspacesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspacePropertiesOutput:
    boto3_raw_data: "type_defs.WorkspacePropertiesOutputTypeDef" = dataclasses.field()

    RunningMode = field("RunningMode")
    RunningModeAutoStopTimeoutInMinutes = field("RunningModeAutoStopTimeoutInMinutes")
    RootVolumeSizeGib = field("RootVolumeSizeGib")
    UserVolumeSizeGib = field("UserVolumeSizeGib")
    ComputeTypeName = field("ComputeTypeName")
    Protocols = field("Protocols")
    OperatingSystemName = field("OperatingSystemName")

    @cached_property
    def GlobalAccelerator(self):  # pragma: no cover
        return GlobalAcceleratorForWorkSpace.make_one(
            self.boto3_raw_data["GlobalAccelerator"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspacePropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspacePropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceProperties:
    boto3_raw_data: "type_defs.WorkspacePropertiesTypeDef" = dataclasses.field()

    RunningMode = field("RunningMode")
    RunningModeAutoStopTimeoutInMinutes = field("RunningModeAutoStopTimeoutInMinutes")
    RootVolumeSizeGib = field("RootVolumeSizeGib")
    UserVolumeSizeGib = field("UserVolumeSizeGib")
    ComputeTypeName = field("ComputeTypeName")
    Protocols = field("Protocols")
    OperatingSystemName = field("OperatingSystemName")

    @cached_property
    def GlobalAccelerator(self):  # pragma: no cover
        return GlobalAcceleratorForWorkSpace.make_one(
            self.boto3_raw_data["GlobalAccelerator"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspacePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspacePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterWorkspaceDirectoryRequest:
    boto3_raw_data: "type_defs.RegisterWorkspaceDirectoryRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryId = field("DirectoryId")
    SubnetIds = field("SubnetIds")
    EnableSelfService = field("EnableSelfService")
    Tenancy = field("Tenancy")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    WorkspaceDirectoryName = field("WorkspaceDirectoryName")
    WorkspaceDirectoryDescription = field("WorkspaceDirectoryDescription")
    UserIdentityType = field("UserIdentityType")
    IdcInstanceArn = field("IdcInstanceArn")

    @cached_property
    def MicrosoftEntraConfig(self):  # pragma: no cover
        return MicrosoftEntraConfig.make_one(
            self.boto3_raw_data["MicrosoftEntraConfig"]
        )

    WorkspaceType = field("WorkspaceType")

    @cached_property
    def ActiveDirectoryConfig(self):  # pragma: no cover
        return ActiveDirectoryConfig.make_one(
            self.boto3_raw_data["ActiveDirectoryConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterWorkspaceDirectoryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterWorkspaceDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifySamlPropertiesRequest:
    boto3_raw_data: "type_defs.ModifySamlPropertiesRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @cached_property
    def SamlProperties(self):  # pragma: no cover
        return SamlProperties.make_one(self.boto3_raw_data["SamlProperties"])

    PropertiesToDelete = field("PropertiesToDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifySamlPropertiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifySamlPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifySelfservicePermissionsRequest:
    boto3_raw_data: "type_defs.ModifySelfservicePermissionsRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")

    @cached_property
    def SelfservicePermissions(self):  # pragma: no cover
        return SelfservicePermissions.make_one(
            self.boto3_raw_data["SelfservicePermissions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifySelfservicePermissionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifySelfservicePermissionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyWorkspaceCreationPropertiesRequest:
    boto3_raw_data: "type_defs.ModifyWorkspaceCreationPropertiesRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")

    @cached_property
    def WorkspaceCreationProperties(self):  # pragma: no cover
        return WorkspaceCreationProperties.make_one(
            self.boto3_raw_data["WorkspaceCreationProperties"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyWorkspaceCreationPropertiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyWorkspaceCreationPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspacesPoolSession:
    boto3_raw_data: "type_defs.WorkspacesPoolSessionTypeDef" = dataclasses.field()

    SessionId = field("SessionId")
    PoolId = field("PoolId")
    UserId = field("UserId")
    AuthenticationType = field("AuthenticationType")
    ConnectionState = field("ConnectionState")
    InstanceId = field("InstanceId")
    ExpirationTime = field("ExpirationTime")

    @cached_property
    def NetworkAccessConfiguration(self):  # pragma: no cover
        return NetworkAccessConfiguration.make_one(
            self.boto3_raw_data["NetworkAccessConfiguration"]
        )

    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspacesPoolSessionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspacesPoolSessionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootWorkspacesRequest:
    boto3_raw_data: "type_defs.RebootWorkspacesRequestTypeDef" = dataclasses.field()

    @cached_property
    def RebootWorkspaceRequests(self):  # pragma: no cover
        return RebootRequest.make_many(self.boto3_raw_data["RebootWorkspaceRequests"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebootWorkspacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebuildWorkspacesRequest:
    boto3_raw_data: "type_defs.RebuildWorkspacesRequestTypeDef" = dataclasses.field()

    @cached_property
    def RebuildWorkspaceRequests(self):  # pragma: no cover
        return RebuildRequest.make_many(self.boto3_raw_data["RebuildWorkspaceRequests"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebuildWorkspacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebuildWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartWorkspacesRequest:
    boto3_raw_data: "type_defs.StartWorkspacesRequestTypeDef" = dataclasses.field()

    @cached_property
    def StartWorkspaceRequests(self):  # pragma: no cover
        return StartRequest.make_many(self.boto3_raw_data["StartWorkspaceRequests"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartWorkspacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopWorkspacesRequest:
    boto3_raw_data: "type_defs.StopWorkspacesRequestTypeDef" = dataclasses.field()

    @cached_property
    def StopWorkspaceRequests(self):  # pragma: no cover
        return StopRequest.make_many(self.boto3_raw_data["StopWorkspaceRequests"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopWorkspacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingPropertiesOutput:
    boto3_raw_data: "type_defs.StreamingPropertiesOutputTypeDef" = dataclasses.field()

    StreamingExperiencePreferredProtocol = field("StreamingExperiencePreferredProtocol")

    @cached_property
    def UserSettings(self):  # pragma: no cover
        return UserSetting.make_many(self.boto3_raw_data["UserSettings"])

    @cached_property
    def StorageConnectors(self):  # pragma: no cover
        return StorageConnector.make_many(self.boto3_raw_data["StorageConnectors"])

    @cached_property
    def GlobalAccelerator(self):  # pragma: no cover
        return GlobalAcceleratorForDirectory.make_one(
            self.boto3_raw_data["GlobalAccelerator"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingProperties:
    boto3_raw_data: "type_defs.StreamingPropertiesTypeDef" = dataclasses.field()

    StreamingExperiencePreferredProtocol = field("StreamingExperiencePreferredProtocol")

    @cached_property
    def UserSettings(self):  # pragma: no cover
        return UserSetting.make_many(self.boto3_raw_data["UserSettings"])

    @cached_property
    def StorageConnectors(self):  # pragma: no cover
        return StorageConnector.make_many(self.boto3_raw_data["StorageConnectors"])

    @cached_property
    def GlobalAccelerator(self):  # pragma: no cover
        return GlobalAcceleratorForDirectory.make_one(
            self.boto3_raw_data["GlobalAccelerator"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateWorkspacesRequest:
    boto3_raw_data: "type_defs.TerminateWorkspacesRequestTypeDef" = dataclasses.field()

    @cached_property
    def TerminateWorkspaceRequests(self):  # pragma: no cover
        return TerminateRequest.make_many(
            self.boto3_raw_data["TerminateWorkspaceRequests"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateWorkspacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceImage:
    boto3_raw_data: "type_defs.WorkspaceImageTypeDef" = dataclasses.field()

    ImageId = field("ImageId")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def OperatingSystem(self):  # pragma: no cover
        return OperatingSystem.make_one(self.boto3_raw_data["OperatingSystem"])

    State = field("State")
    RequiredTenancy = field("RequiredTenancy")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")
    Created = field("Created")
    OwnerAccountId = field("OwnerAccountId")

    @cached_property
    def Updates(self):  # pragma: no cover
        return UpdateResult.make_one(self.boto3_raw_data["Updates"])

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return ErrorDetails.make_many(self.boto3_raw_data["ErrorDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkspaceImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkspaceImageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspacesPool:
    boto3_raw_data: "type_defs.WorkspacesPoolTypeDef" = dataclasses.field()

    PoolId = field("PoolId")
    PoolArn = field("PoolArn")

    @cached_property
    def CapacityStatus(self):  # pragma: no cover
        return CapacityStatus.make_one(self.boto3_raw_data["CapacityStatus"])

    PoolName = field("PoolName")
    State = field("State")
    CreatedAt = field("CreatedAt")
    BundleId = field("BundleId")
    DirectoryId = field("DirectoryId")
    RunningMode = field("RunningMode")
    Description = field("Description")

    @cached_property
    def Errors(self):  # pragma: no cover
        return WorkspacesPoolError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def ApplicationSettings(self):  # pragma: no cover
        return ApplicationSettingsResponse.make_one(
            self.boto3_raw_data["ApplicationSettings"]
        )

    @cached_property
    def TimeoutSettings(self):  # pragma: no cover
        return TimeoutSettings.make_one(self.boto3_raw_data["TimeoutSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkspacesPoolTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkspacesPoolTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceAccessPropertiesOutput:
    boto3_raw_data: "type_defs.WorkspaceAccessPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    DeviceTypeWindows = field("DeviceTypeWindows")
    DeviceTypeOsx = field("DeviceTypeOsx")
    DeviceTypeWeb = field("DeviceTypeWeb")
    DeviceTypeIos = field("DeviceTypeIos")
    DeviceTypeAndroid = field("DeviceTypeAndroid")
    DeviceTypeChromeOs = field("DeviceTypeChromeOs")
    DeviceTypeZeroClient = field("DeviceTypeZeroClient")
    DeviceTypeLinux = field("DeviceTypeLinux")
    DeviceTypeWorkSpacesThinClient = field("DeviceTypeWorkSpacesThinClient")

    @cached_property
    def AccessEndpointConfig(self):  # pragma: no cover
        return AccessEndpointConfigOutput.make_one(
            self.boto3_raw_data["AccessEndpointConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WorkspaceAccessPropertiesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceAccessPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceAccessProperties:
    boto3_raw_data: "type_defs.WorkspaceAccessPropertiesTypeDef" = dataclasses.field()

    DeviceTypeWindows = field("DeviceTypeWindows")
    DeviceTypeOsx = field("DeviceTypeOsx")
    DeviceTypeWeb = field("DeviceTypeWeb")
    DeviceTypeIos = field("DeviceTypeIos")
    DeviceTypeAndroid = field("DeviceTypeAndroid")
    DeviceTypeChromeOs = field("DeviceTypeChromeOs")
    DeviceTypeZeroClient = field("DeviceTypeZeroClient")
    DeviceTypeLinux = field("DeviceTypeLinux")
    DeviceTypeWorkSpacesThinClient = field("DeviceTypeWorkSpacesThinClient")

    @cached_property
    def AccessEndpointConfig(self):  # pragma: no cover
        return AccessEndpointConfig.make_one(
            self.boto3_raw_data["AccessEndpointConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspaceAccessPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceAccessPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationAssociationsResult:
    boto3_raw_data: "type_defs.DescribeApplicationAssociationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Associations(self):  # pragma: no cover
        return ApplicationResourceAssociation.make_many(
            self.boto3_raw_data["Associations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationAssociationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationAssociationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBundleAssociationsResult:
    boto3_raw_data: "type_defs.DescribeBundleAssociationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Associations(self):  # pragma: no cover
        return BundleResourceAssociation.make_many(self.boto3_raw_data["Associations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBundleAssociationsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBundleAssociationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImageAssociationsResult:
    boto3_raw_data: "type_defs.DescribeImageAssociationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Associations(self):  # pragma: no cover
        return ImageResourceAssociation.make_many(self.boto3_raw_data["Associations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeImageAssociationsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImageAssociationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateWorkspaceApplicationResult:
    boto3_raw_data: "type_defs.AssociateWorkspaceApplicationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Association(self):  # pragma: no cover
        return WorkspaceResourceAssociation.make_one(self.boto3_raw_data["Association"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateWorkspaceApplicationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateWorkspaceApplicationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceAssociationsResult:
    boto3_raw_data: "type_defs.DescribeWorkspaceAssociationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Associations(self):  # pragma: no cover
        return WorkspaceResourceAssociation.make_many(
            self.boto3_raw_data["Associations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceAssociationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceAssociationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateWorkspaceApplicationResult:
    boto3_raw_data: "type_defs.DisassociateWorkspaceApplicationResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Association(self):  # pragma: no cover
        return WorkspaceResourceAssociation.make_one(self.boto3_raw_data["Association"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateWorkspaceApplicationResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateWorkspaceApplicationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkSpaceApplicationDeployment:
    boto3_raw_data: "type_defs.WorkSpaceApplicationDeploymentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Associations(self):  # pragma: no cover
        return WorkspaceResourceAssociation.make_many(
            self.boto3_raw_data["Associations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WorkSpaceApplicationDeploymentTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkSpaceApplicationDeploymentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIpGroupsResult:
    boto3_raw_data: "type_defs.DescribeIpGroupsResultTypeDef" = dataclasses.field()

    @cached_property
    def Result(self):  # pragma: no cover
        return WorkspacesIpGroup.make_many(self.boto3_raw_data["Result"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIpGroupsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIpGroupsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportClientBrandingRequest:
    boto3_raw_data: "type_defs.ImportClientBrandingRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @cached_property
    def DeviceTypeWindows(self):  # pragma: no cover
        return DefaultImportClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeWindows"]
        )

    @cached_property
    def DeviceTypeOsx(self):  # pragma: no cover
        return DefaultImportClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeOsx"]
        )

    @cached_property
    def DeviceTypeAndroid(self):  # pragma: no cover
        return DefaultImportClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeAndroid"]
        )

    @cached_property
    def DeviceTypeIos(self):  # pragma: no cover
        return IosImportClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeIos"]
        )

    @cached_property
    def DeviceTypeLinux(self):  # pragma: no cover
        return DefaultImportClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeLinux"]
        )

    @cached_property
    def DeviceTypeWeb(self):  # pragma: no cover
        return DefaultImportClientBrandingAttributes.make_one(
            self.boto3_raw_data["DeviceTypeWeb"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportClientBrandingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportClientBrandingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClientPropertiesResult:
    boto3_raw_data: "type_defs.DescribeClientPropertiesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ClientPropertiesList(self):  # pragma: no cover
        return ClientPropertiesResult.make_many(
            self.boto3_raw_data["ClientPropertiesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClientPropertiesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClientPropertiesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionAliasesResult:
    boto3_raw_data: "type_defs.DescribeConnectionAliasesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConnectionAliases(self):  # pragma: no cover
        return ConnectionAlias.make_many(self.boto3_raw_data["ConnectionAliases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConnectionAliasesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionAliasesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedCreateStandbyWorkspacesRequest:
    boto3_raw_data: "type_defs.FailedCreateStandbyWorkspacesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StandbyWorkspaceRequest(self):  # pragma: no cover
        return StandbyWorkspaceOutput.make_one(
            self.boto3_raw_data["StandbyWorkspaceRequest"]
        )

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FailedCreateStandbyWorkspacesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedCreateStandbyWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspaceBundleResult:
    boto3_raw_data: "type_defs.CreateWorkspaceBundleResultTypeDef" = dataclasses.field()

    @cached_property
    def WorkspaceBundle(self):  # pragma: no cover
        return WorkspaceBundle.make_one(self.boto3_raw_data["WorkspaceBundle"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspaceBundleResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspaceBundleResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceBundlesResult:
    boto3_raw_data: "type_defs.DescribeWorkspaceBundlesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Bundles(self):  # pragma: no cover
        return WorkspaceBundle.make_many(self.boto3_raw_data["Bundles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorkspaceBundlesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceBundlesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceRequestOutput:
    boto3_raw_data: "type_defs.WorkspaceRequestOutputTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    UserName = field("UserName")
    BundleId = field("BundleId")
    VolumeEncryptionKey = field("VolumeEncryptionKey")
    UserVolumeEncryptionEnabled = field("UserVolumeEncryptionEnabled")
    RootVolumeEncryptionEnabled = field("RootVolumeEncryptionEnabled")

    @cached_property
    def WorkspaceProperties(self):  # pragma: no cover
        return WorkspacePropertiesOutput.make_one(
            self.boto3_raw_data["WorkspaceProperties"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    WorkspaceName = field("WorkspaceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspaceRequestOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Workspace:
    boto3_raw_data: "type_defs.WorkspaceTypeDef" = dataclasses.field()

    WorkspaceId = field("WorkspaceId")
    DirectoryId = field("DirectoryId")
    UserName = field("UserName")
    IpAddress = field("IpAddress")
    State = field("State")
    BundleId = field("BundleId")
    SubnetId = field("SubnetId")
    ErrorMessage = field("ErrorMessage")
    ErrorCode = field("ErrorCode")
    ComputerName = field("ComputerName")
    VolumeEncryptionKey = field("VolumeEncryptionKey")
    UserVolumeEncryptionEnabled = field("UserVolumeEncryptionEnabled")
    RootVolumeEncryptionEnabled = field("RootVolumeEncryptionEnabled")
    WorkspaceName = field("WorkspaceName")

    @cached_property
    def WorkspaceProperties(self):  # pragma: no cover
        return WorkspacePropertiesOutput.make_one(
            self.boto3_raw_data["WorkspaceProperties"]
        )

    @cached_property
    def ModificationStates(self):  # pragma: no cover
        return ModificationState.make_many(self.boto3_raw_data["ModificationStates"])

    @cached_property
    def RelatedWorkspaces(self):  # pragma: no cover
        return RelatedWorkspaceProperties.make_many(
            self.boto3_raw_data["RelatedWorkspaces"]
        )

    @cached_property
    def DataReplicationSettings(self):  # pragma: no cover
        return DataReplicationSettings.make_one(
            self.boto3_raw_data["DataReplicationSettings"]
        )

    @cached_property
    def StandbyWorkspacesProperties(self):  # pragma: no cover
        return StandbyWorkspacesProperties.make_many(
            self.boto3_raw_data["StandbyWorkspacesProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkspaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkspaceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspacesPoolSessionsResult:
    boto3_raw_data: "type_defs.DescribeWorkspacesPoolSessionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sessions(self):  # pragma: no cover
        return WorkspacesPoolSession.make_many(self.boto3_raw_data["Sessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspacesPoolSessionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspacesPoolSessionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceImagesResult:
    boto3_raw_data: "type_defs.DescribeWorkspaceImagesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Images(self):  # pragma: no cover
        return WorkspaceImage.make_many(self.boto3_raw_data["Images"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorkspaceImagesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceImagesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspacesPoolResult:
    boto3_raw_data: "type_defs.CreateWorkspacesPoolResultTypeDef" = dataclasses.field()

    @cached_property
    def WorkspacesPool(self):  # pragma: no cover
        return WorkspacesPool.make_one(self.boto3_raw_data["WorkspacesPool"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspacesPoolResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspacesPoolResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspacesPoolsResult:
    boto3_raw_data: "type_defs.DescribeWorkspacesPoolsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WorkspacesPools(self):  # pragma: no cover
        return WorkspacesPool.make_many(self.boto3_raw_data["WorkspacesPools"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorkspacesPoolsResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspacesPoolsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkspacesPoolResult:
    boto3_raw_data: "type_defs.UpdateWorkspacesPoolResultTypeDef" = dataclasses.field()

    @cached_property
    def WorkspacesPool(self):  # pragma: no cover
        return WorkspacesPool.make_one(self.boto3_raw_data["WorkspacesPool"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWorkspacesPoolResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkspacesPoolResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceDirectory:
    boto3_raw_data: "type_defs.WorkspaceDirectoryTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    Alias = field("Alias")
    DirectoryName = field("DirectoryName")
    RegistrationCode = field("RegistrationCode")
    SubnetIds = field("SubnetIds")
    DnsIpAddresses = field("DnsIpAddresses")
    CustomerUserName = field("CustomerUserName")
    IamRoleId = field("IamRoleId")
    DirectoryType = field("DirectoryType")
    WorkspaceSecurityGroupId = field("WorkspaceSecurityGroupId")
    State = field("State")

    @cached_property
    def WorkspaceCreationProperties(self):  # pragma: no cover
        return DefaultWorkspaceCreationProperties.make_one(
            self.boto3_raw_data["WorkspaceCreationProperties"]
        )

    ipGroupIds = field("ipGroupIds")

    @cached_property
    def WorkspaceAccessProperties(self):  # pragma: no cover
        return WorkspaceAccessPropertiesOutput.make_one(
            self.boto3_raw_data["WorkspaceAccessProperties"]
        )

    Tenancy = field("Tenancy")

    @cached_property
    def SelfservicePermissions(self):  # pragma: no cover
        return SelfservicePermissions.make_one(
            self.boto3_raw_data["SelfservicePermissions"]
        )

    @cached_property
    def SamlProperties(self):  # pragma: no cover
        return SamlProperties.make_one(self.boto3_raw_data["SamlProperties"])

    @cached_property
    def CertificateBasedAuthProperties(self):  # pragma: no cover
        return CertificateBasedAuthProperties.make_one(
            self.boto3_raw_data["CertificateBasedAuthProperties"]
        )

    EndpointEncryptionMode = field("EndpointEncryptionMode")

    @cached_property
    def MicrosoftEntraConfig(self):  # pragma: no cover
        return MicrosoftEntraConfig.make_one(
            self.boto3_raw_data["MicrosoftEntraConfig"]
        )

    WorkspaceDirectoryName = field("WorkspaceDirectoryName")
    WorkspaceDirectoryDescription = field("WorkspaceDirectoryDescription")
    UserIdentityType = field("UserIdentityType")
    WorkspaceType = field("WorkspaceType")

    @cached_property
    def IDCConfig(self):  # pragma: no cover
        return IDCConfig.make_one(self.boto3_raw_data["IDCConfig"])

    @cached_property
    def ActiveDirectoryConfig(self):  # pragma: no cover
        return ActiveDirectoryConfig.make_one(
            self.boto3_raw_data["ActiveDirectoryConfig"]
        )

    @cached_property
    def StreamingProperties(self):  # pragma: no cover
        return StreamingPropertiesOutput.make_one(
            self.boto3_raw_data["StreamingProperties"]
        )

    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkspaceDirectoryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceDirectoryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeployWorkspaceApplicationsResult:
    boto3_raw_data: "type_defs.DeployWorkspaceApplicationsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Deployment(self):  # pragma: no cover
        return WorkSpaceApplicationDeployment.make_one(
            self.boto3_raw_data["Deployment"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeployWorkspaceApplicationsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeployWorkspaceApplicationsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStandbyWorkspacesResult:
    boto3_raw_data: "type_defs.CreateStandbyWorkspacesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FailedStandbyRequests(self):  # pragma: no cover
        return FailedCreateStandbyWorkspacesRequest.make_many(
            self.boto3_raw_data["FailedStandbyRequests"]
        )

    @cached_property
    def PendingStandbyRequests(self):  # pragma: no cover
        return PendingCreateStandbyWorkspacesRequest.make_many(
            self.boto3_raw_data["PendingStandbyRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateStandbyWorkspacesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStandbyWorkspacesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStandbyWorkspacesRequest:
    boto3_raw_data: "type_defs.CreateStandbyWorkspacesRequestTypeDef" = (
        dataclasses.field()
    )

    PrimaryRegion = field("PrimaryRegion")
    StandbyWorkspaces = field("StandbyWorkspaces")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateStandbyWorkspacesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStandbyWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedCreateWorkspaceRequest:
    boto3_raw_data: "type_defs.FailedCreateWorkspaceRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WorkspaceRequest(self):  # pragma: no cover
        return WorkspaceRequestOutput.make_one(self.boto3_raw_data["WorkspaceRequest"])

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailedCreateWorkspaceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedCreateWorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspacesResult:
    boto3_raw_data: "type_defs.DescribeWorkspacesResultTypeDef" = dataclasses.field()

    @cached_property
    def Workspaces(self):  # pragma: no cover
        return Workspace.make_many(self.boto3_raw_data["Workspaces"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorkspacesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspacesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyWorkspacePropertiesRequest:
    boto3_raw_data: "type_defs.ModifyWorkspacePropertiesRequestTypeDef" = (
        dataclasses.field()
    )

    WorkspaceId = field("WorkspaceId")
    WorkspaceProperties = field("WorkspaceProperties")
    DataReplication = field("DataReplication")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyWorkspacePropertiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyWorkspacePropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkspaceRequest:
    boto3_raw_data: "type_defs.WorkspaceRequestTypeDef" = dataclasses.field()

    DirectoryId = field("DirectoryId")
    UserName = field("UserName")
    BundleId = field("BundleId")
    VolumeEncryptionKey = field("VolumeEncryptionKey")
    UserVolumeEncryptionEnabled = field("UserVolumeEncryptionEnabled")
    RootVolumeEncryptionEnabled = field("RootVolumeEncryptionEnabled")
    WorkspaceProperties = field("WorkspaceProperties")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    WorkspaceName = field("WorkspaceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkspaceRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkspaceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyStreamingPropertiesRequest:
    boto3_raw_data: "type_defs.ModifyStreamingPropertiesRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")
    StreamingProperties = field("StreamingProperties")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyStreamingPropertiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyStreamingPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkspaceDirectoriesResult:
    boto3_raw_data: "type_defs.DescribeWorkspaceDirectoriesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Directories(self):  # pragma: no cover
        return WorkspaceDirectory.make_many(self.boto3_raw_data["Directories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeWorkspaceDirectoriesResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkspaceDirectoriesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyWorkspaceAccessPropertiesRequest:
    boto3_raw_data: "type_defs.ModifyWorkspaceAccessPropertiesRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceId = field("ResourceId")
    WorkspaceAccessProperties = field("WorkspaceAccessProperties")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyWorkspaceAccessPropertiesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyWorkspaceAccessPropertiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspacesResult:
    boto3_raw_data: "type_defs.CreateWorkspacesResultTypeDef" = dataclasses.field()

    @cached_property
    def FailedRequests(self):  # pragma: no cover
        return FailedCreateWorkspaceRequest.make_many(
            self.boto3_raw_data["FailedRequests"]
        )

    @cached_property
    def PendingRequests(self):  # pragma: no cover
        return Workspace.make_many(self.boto3_raw_data["PendingRequests"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspacesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspacesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkspacesRequest:
    boto3_raw_data: "type_defs.CreateWorkspacesRequestTypeDef" = dataclasses.field()

    Workspaces = field("Workspaces")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWorkspacesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkspacesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
