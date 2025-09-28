# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sso_admin import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessControlAttributeValueOutput:
    boto3_raw_data: "type_defs.AccessControlAttributeValueOutputTypeDef" = (
        dataclasses.field()
    )

    Source = field("Source")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AccessControlAttributeValueOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlAttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControlAttributeValue:
    boto3_raw_data: "type_defs.AccessControlAttributeValueTypeDef" = dataclasses.field()

    Source = field("Source")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessControlAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountAssignmentForPrincipal:
    boto3_raw_data: "type_defs.AccountAssignmentForPrincipalTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    PermissionSetArn = field("PermissionSetArn")
    PrincipalId = field("PrincipalId")
    PrincipalType = field("PrincipalType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AccountAssignmentForPrincipalTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAssignmentForPrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountAssignmentOperationStatusMetadata:
    boto3_raw_data: "type_defs.AccountAssignmentOperationStatusMetadataTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    RequestId = field("RequestId")
    CreatedDate = field("CreatedDate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AccountAssignmentOperationStatusMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAssignmentOperationStatusMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountAssignmentOperationStatus:
    boto3_raw_data: "type_defs.AccountAssignmentOperationStatusTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    RequestId = field("RequestId")
    FailureReason = field("FailureReason")
    TargetId = field("TargetId")
    TargetType = field("TargetType")
    PermissionSetArn = field("PermissionSetArn")
    PrincipalType = field("PrincipalType")
    PrincipalId = field("PrincipalId")
    CreatedDate = field("CreatedDate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AccountAssignmentOperationStatusTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAssignmentOperationStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountAssignment:
    boto3_raw_data: "type_defs.AccountAssignmentTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    PermissionSetArn = field("PermissionSetArn")
    PrincipalType = field("PrincipalType")
    PrincipalId = field("PrincipalId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountAssignmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAssignmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationAssignmentForPrincipal:
    boto3_raw_data: "type_defs.ApplicationAssignmentForPrincipalTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    PrincipalId = field("PrincipalId")
    PrincipalType = field("PrincipalType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationAssignmentForPrincipalTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationAssignmentForPrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationAssignment:
    boto3_raw_data: "type_defs.ApplicationAssignmentTypeDef" = dataclasses.field()

    ApplicationArn = field("ApplicationArn")
    PrincipalId = field("PrincipalId")
    PrincipalType = field("PrincipalType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationAssignmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationAssignmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisplayData:
    boto3_raw_data: "type_defs.DisplayDataTypeDef" = dataclasses.field()

    DisplayName = field("DisplayName")
    IconUrl = field("IconUrl")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DisplayDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DisplayDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomerManagedPolicyReference:
    boto3_raw_data: "type_defs.CustomerManagedPolicyReferenceTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Path = field("Path")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomerManagedPolicyReferenceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerManagedPolicyReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachManagedPolicyToPermissionSetRequest:
    boto3_raw_data: "type_defs.AttachManagedPolicyToPermissionSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")
    ManagedPolicyArn = field("ManagedPolicyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachManagedPolicyToPermissionSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachManagedPolicyToPermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachedManagedPolicy:
    boto3_raw_data: "type_defs.AttachedManagedPolicyTypeDef" = dataclasses.field()

    Name = field("Name")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachedManagedPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachedManagedPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamAuthenticationMethodOutput:
    boto3_raw_data: "type_defs.IamAuthenticationMethodOutputTypeDef" = (
        dataclasses.field()
    )

    ActorPolicy = field("ActorPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IamAuthenticationMethodOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamAuthenticationMethodOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamAuthenticationMethod:
    boto3_raw_data: "type_defs.IamAuthenticationMethodTypeDef" = dataclasses.field()

    ActorPolicy = field("ActorPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamAuthenticationMethodTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamAuthenticationMethodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizationCodeGrantOutput:
    boto3_raw_data: "type_defs.AuthorizationCodeGrantOutputTypeDef" = (
        dataclasses.field()
    )

    RedirectUris = field("RedirectUris")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizationCodeGrantOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizationCodeGrantOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizationCodeGrant:
    boto3_raw_data: "type_defs.AuthorizationCodeGrantTypeDef" = dataclasses.field()

    RedirectUris = field("RedirectUris")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizationCodeGrantTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizationCodeGrantTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizedTokenIssuerOutput:
    boto3_raw_data: "type_defs.AuthorizedTokenIssuerOutputTypeDef" = dataclasses.field()

    TrustedTokenIssuerArn = field("TrustedTokenIssuerArn")
    AuthorizedAudiences = field("AuthorizedAudiences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizedTokenIssuerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizedTokenIssuerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizedTokenIssuer:
    boto3_raw_data: "type_defs.AuthorizedTokenIssuerTypeDef" = dataclasses.field()

    TrustedTokenIssuerArn = field("TrustedTokenIssuerArn")
    AuthorizedAudiences = field("AuthorizedAudiences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizedTokenIssuerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizedTokenIssuerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccountAssignmentRequest:
    boto3_raw_data: "type_defs.CreateAccountAssignmentRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    TargetId = field("TargetId")
    TargetType = field("TargetType")
    PermissionSetArn = field("PermissionSetArn")
    PrincipalType = field("PrincipalType")
    PrincipalId = field("PrincipalId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAccountAssignmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccountAssignmentRequestTypeDef"]
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
class CreateApplicationAssignmentRequest:
    boto3_raw_data: "type_defs.CreateApplicationAssignmentRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    PrincipalId = field("PrincipalId")
    PrincipalType = field("PrincipalType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateApplicationAssignmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationAssignmentRequestTypeDef"]
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
class PermissionSet:
    boto3_raw_data: "type_defs.PermissionSetTypeDef" = dataclasses.field()

    Name = field("Name")
    PermissionSetArn = field("PermissionSetArn")
    Description = field("Description")
    CreatedDate = field("CreatedDate")
    SessionDuration = field("SessionDuration")
    RelayState = field("RelayState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PermissionSetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountAssignmentRequest:
    boto3_raw_data: "type_defs.DeleteAccountAssignmentRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    TargetId = field("TargetId")
    TargetType = field("TargetType")
    PermissionSetArn = field("PermissionSetArn")
    PrincipalType = field("PrincipalType")
    PrincipalId = field("PrincipalId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAccountAssignmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccountAssignmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationAccessScopeRequest:
    boto3_raw_data: "type_defs.DeleteApplicationAccessScopeRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    Scope = field("Scope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationAccessScopeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationAccessScopeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationAssignmentRequest:
    boto3_raw_data: "type_defs.DeleteApplicationAssignmentRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    PrincipalId = field("PrincipalId")
    PrincipalType = field("PrincipalType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationAssignmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationAssignmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationAuthenticationMethodRequest:
    boto3_raw_data: "type_defs.DeleteApplicationAuthenticationMethodRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    AuthenticationMethodType = field("AuthenticationMethodType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteApplicationAuthenticationMethodRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationAuthenticationMethodRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationGrantRequest:
    boto3_raw_data: "type_defs.DeleteApplicationGrantRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    GrantType = field("GrantType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteApplicationGrantRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationRequest:
    boto3_raw_data: "type_defs.DeleteApplicationRequestTypeDef" = dataclasses.field()

    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInlinePolicyFromPermissionSetRequest:
    boto3_raw_data: "type_defs.DeleteInlinePolicyFromPermissionSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteInlinePolicyFromPermissionSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInlinePolicyFromPermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceAccessControlAttributeConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DeleteInstanceAccessControlAttributeConfigurationRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteInstanceAccessControlAttributeConfigurationRequestTypeDef"
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
                "type_defs.DeleteInstanceAccessControlAttributeConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceRequest:
    boto3_raw_data: "type_defs.DeleteInstanceRequestTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePermissionSetRequest:
    boto3_raw_data: "type_defs.DeletePermissionSetRequestTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePermissionSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePermissionsBoundaryFromPermissionSetRequest:
    boto3_raw_data: (
        "type_defs.DeletePermissionsBoundaryFromPermissionSetRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePermissionsBoundaryFromPermissionSetRequestTypeDef"
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
                "type_defs.DeletePermissionsBoundaryFromPermissionSetRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrustedTokenIssuerRequest:
    boto3_raw_data: "type_defs.DeleteTrustedTokenIssuerRequestTypeDef" = (
        dataclasses.field()
    )

    TrustedTokenIssuerArn = field("TrustedTokenIssuerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteTrustedTokenIssuerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrustedTokenIssuerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountAssignmentCreationStatusRequest:
    boto3_raw_data: (
        "type_defs.DescribeAccountAssignmentCreationStatusRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    AccountAssignmentCreationRequestId = field("AccountAssignmentCreationRequestId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountAssignmentCreationStatusRequestTypeDef"
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
                "type_defs.DescribeAccountAssignmentCreationStatusRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountAssignmentDeletionStatusRequest:
    boto3_raw_data: (
        "type_defs.DescribeAccountAssignmentDeletionStatusRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    AccountAssignmentDeletionRequestId = field("AccountAssignmentDeletionRequestId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountAssignmentDeletionStatusRequestTypeDef"
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
                "type_defs.DescribeAccountAssignmentDeletionStatusRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationAssignmentRequest:
    boto3_raw_data: "type_defs.DescribeApplicationAssignmentRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    PrincipalId = field("PrincipalId")
    PrincipalType = field("PrincipalType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationAssignmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationAssignmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationProviderRequest:
    boto3_raw_data: "type_defs.DescribeApplicationProviderRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationProviderArn = field("ApplicationProviderArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationProviderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationProviderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationRequest:
    boto3_raw_data: "type_defs.DescribeApplicationRequestTypeDef" = dataclasses.field()

    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceAccessControlAttributeConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DescribeInstanceAccessControlAttributeConfigurationRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceAccessControlAttributeConfigurationRequestTypeDef"
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
                "type_defs.DescribeInstanceAccessControlAttributeConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceRequest:
    boto3_raw_data: "type_defs.DescribeInstanceRequestTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfigurationDetails:
    boto3_raw_data: "type_defs.EncryptionConfigurationDetailsTypeDef" = (
        dataclasses.field()
    )

    KeyType = field("KeyType")
    KmsKeyArn = field("KmsKeyArn")
    EncryptionStatus = field("EncryptionStatus")
    EncryptionStatusReason = field("EncryptionStatusReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePermissionSetProvisioningStatusRequest:
    boto3_raw_data: (
        "type_defs.DescribePermissionSetProvisioningStatusRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    ProvisionPermissionSetRequestId = field("ProvisionPermissionSetRequestId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePermissionSetProvisioningStatusRequestTypeDef"
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
                "type_defs.DescribePermissionSetProvisioningStatusRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionSetProvisioningStatus:
    boto3_raw_data: "type_defs.PermissionSetProvisioningStatusTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    RequestId = field("RequestId")
    AccountId = field("AccountId")
    PermissionSetArn = field("PermissionSetArn")
    FailureReason = field("FailureReason")
    CreatedDate = field("CreatedDate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PermissionSetProvisioningStatusTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PermissionSetProvisioningStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePermissionSetRequest:
    boto3_raw_data: "type_defs.DescribePermissionSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePermissionSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustedTokenIssuerRequest:
    boto3_raw_data: "type_defs.DescribeTrustedTokenIssuerRequestTypeDef" = (
        dataclasses.field()
    )

    TrustedTokenIssuerArn = field("TrustedTokenIssuerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustedTokenIssuerRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustedTokenIssuerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachManagedPolicyFromPermissionSetRequest:
    boto3_raw_data: "type_defs.DetachManagedPolicyFromPermissionSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")
    ManagedPolicyArn = field("ManagedPolicyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachManagedPolicyFromPermissionSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachManagedPolicyFromPermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    KeyType = field("KeyType")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationAccessScopeRequest:
    boto3_raw_data: "type_defs.GetApplicationAccessScopeRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    Scope = field("Scope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetApplicationAccessScopeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationAccessScopeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationAssignmentConfigurationRequest:
    boto3_raw_data: "type_defs.GetApplicationAssignmentConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationAssignmentConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationAssignmentConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationAuthenticationMethodRequest:
    boto3_raw_data: "type_defs.GetApplicationAuthenticationMethodRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    AuthenticationMethodType = field("AuthenticationMethodType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationAuthenticationMethodRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationAuthenticationMethodRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationGrantRequest:
    boto3_raw_data: "type_defs.GetApplicationGrantRequestTypeDef" = dataclasses.field()

    ApplicationArn = field("ApplicationArn")
    GrantType = field("GrantType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationSessionConfigurationRequest:
    boto3_raw_data: "type_defs.GetApplicationSessionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationSessionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationSessionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInlinePolicyForPermissionSetRequest:
    boto3_raw_data: "type_defs.GetInlinePolicyForPermissionSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInlinePolicyForPermissionSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInlinePolicyForPermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPermissionsBoundaryForPermissionSetRequest:
    boto3_raw_data: "type_defs.GetPermissionsBoundaryForPermissionSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPermissionsBoundaryForPermissionSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPermissionsBoundaryForPermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceMetadata:
    boto3_raw_data: "type_defs.InstanceMetadataTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    IdentityStoreId = field("IdentityStoreId")
    OwnerAccountId = field("OwnerAccountId")
    Name = field("Name")
    CreatedDate = field("CreatedDate")
    Status = field("Status")
    StatusReason = field("StatusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperationStatusFilter:
    boto3_raw_data: "type_defs.OperationStatusFilterTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OperationStatusFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OperationStatusFilterTypeDef"]
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
class ListAccountAssignmentsFilter:
    boto3_raw_data: "type_defs.ListAccountAssignmentsFilterTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountAssignmentsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssignmentsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentsRequest:
    boto3_raw_data: "type_defs.ListAccountAssignmentsRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    AccountId = field("AccountId")
    PermissionSetArn = field("PermissionSetArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountAssignmentsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssignmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountsForProvisionedPermissionSetRequest:
    boto3_raw_data: (
        "type_defs.ListAccountsForProvisionedPermissionSetRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")
    ProvisioningStatus = field("ProvisioningStatus")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountsForProvisionedPermissionSetRequestTypeDef"
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
                "type_defs.ListAccountsForProvisionedPermissionSetRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAccessScopesRequest:
    boto3_raw_data: "type_defs.ListApplicationAccessScopesRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAccessScopesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationAccessScopesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScopeDetails:
    boto3_raw_data: "type_defs.ScopeDetailsTypeDef" = dataclasses.field()

    Scope = field("Scope")
    AuthorizedTargets = field("AuthorizedTargets")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAssignmentsFilter:
    boto3_raw_data: "type_defs.ListApplicationAssignmentsFilterTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationAssignmentsFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationAssignmentsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAssignmentsRequest:
    boto3_raw_data: "type_defs.ListApplicationAssignmentsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAssignmentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationAssignmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAuthenticationMethodsRequest:
    boto3_raw_data: "type_defs.ListApplicationAuthenticationMethodsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAuthenticationMethodsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationAuthenticationMethodsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationGrantsRequest:
    boto3_raw_data: "type_defs.ListApplicationGrantsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationGrantsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationGrantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationProvidersRequest:
    boto3_raw_data: "type_defs.ListApplicationProvidersRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationProvidersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationProvidersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsFilter:
    boto3_raw_data: "type_defs.ListApplicationsFilterTypeDef" = dataclasses.field()

    ApplicationAccount = field("ApplicationAccount")
    ApplicationProvider = field("ApplicationProvider")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomerManagedPolicyReferencesInPermissionSetRequest:
    boto3_raw_data: (
        "type_defs.ListCustomerManagedPolicyReferencesInPermissionSetRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomerManagedPolicyReferencesInPermissionSetRequestTypeDef"
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
                "type_defs.ListCustomerManagedPolicyReferencesInPermissionSetRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesRequest:
    boto3_raw_data: "type_defs.ListInstancesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedPoliciesInPermissionSetRequest:
    boto3_raw_data: "type_defs.ListManagedPoliciesInPermissionSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedPoliciesInPermissionSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedPoliciesInPermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionSetProvisioningStatusMetadata:
    boto3_raw_data: "type_defs.PermissionSetProvisioningStatusMetadataTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    RequestId = field("RequestId")
    CreatedDate = field("CreatedDate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PermissionSetProvisioningStatusMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PermissionSetProvisioningStatusMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionSetsProvisionedToAccountRequest:
    boto3_raw_data: "type_defs.ListPermissionSetsProvisionedToAccountRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    AccountId = field("AccountId")
    ProvisioningStatus = field("ProvisioningStatus")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPermissionSetsProvisionedToAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionSetsProvisionedToAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionSetsRequest:
    boto3_raw_data: "type_defs.ListPermissionSetsRequestTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPermissionSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionSetsRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")
    InstanceArn = field("InstanceArn")
    NextToken = field("NextToken")

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
class ListTrustedTokenIssuersRequest:
    boto3_raw_data: "type_defs.ListTrustedTokenIssuersRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTrustedTokenIssuersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrustedTokenIssuersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedTokenIssuerMetadata:
    boto3_raw_data: "type_defs.TrustedTokenIssuerMetadataTypeDef" = dataclasses.field()

    TrustedTokenIssuerArn = field("TrustedTokenIssuerArn")
    Name = field("Name")
    TrustedTokenIssuerType = field("TrustedTokenIssuerType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrustedTokenIssuerMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedTokenIssuerMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OidcJwtConfiguration:
    boto3_raw_data: "type_defs.OidcJwtConfigurationTypeDef" = dataclasses.field()

    IssuerUrl = field("IssuerUrl")
    ClaimAttributePath = field("ClaimAttributePath")
    IdentityStoreAttributePath = field("IdentityStoreAttributePath")
    JwksRetrievalOption = field("JwksRetrievalOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OidcJwtConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OidcJwtConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OidcJwtUpdateConfiguration:
    boto3_raw_data: "type_defs.OidcJwtUpdateConfigurationTypeDef" = dataclasses.field()

    ClaimAttributePath = field("ClaimAttributePath")
    IdentityStoreAttributePath = field("IdentityStoreAttributePath")
    JwksRetrievalOption = field("JwksRetrievalOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OidcJwtUpdateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OidcJwtUpdateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignInOptions:
    boto3_raw_data: "type_defs.SignInOptionsTypeDef" = dataclasses.field()

    Origin = field("Origin")
    ApplicationUrl = field("ApplicationUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignInOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SignInOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionPermissionSetRequest:
    boto3_raw_data: "type_defs.ProvisionPermissionSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")
    TargetType = field("TargetType")
    TargetId = field("TargetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisionPermissionSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionPermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutApplicationAccessScopeRequest:
    boto3_raw_data: "type_defs.PutApplicationAccessScopeRequestTypeDef" = (
        dataclasses.field()
    )

    Scope = field("Scope")
    ApplicationArn = field("ApplicationArn")
    AuthorizedTargets = field("AuthorizedTargets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutApplicationAccessScopeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutApplicationAccessScopeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutApplicationAssignmentConfigurationRequest:
    boto3_raw_data: "type_defs.PutApplicationAssignmentConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    AssignmentRequired = field("AssignmentRequired")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutApplicationAssignmentConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutApplicationAssignmentConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutApplicationSessionConfigurationRequest:
    boto3_raw_data: "type_defs.PutApplicationSessionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    UserBackgroundSessionApplicationStatus = field(
        "UserBackgroundSessionApplicationStatus"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutApplicationSessionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutApplicationSessionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInlinePolicyToPermissionSetRequest:
    boto3_raw_data: "type_defs.PutInlinePolicyToPermissionSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")
    InlinePolicy = field("InlinePolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutInlinePolicyToPermissionSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInlinePolicyToPermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceServerScopeDetails:
    boto3_raw_data: "type_defs.ResourceServerScopeDetailsTypeDef" = dataclasses.field()

    LongDescription = field("LongDescription")
    DetailedTitle = field("DetailedTitle")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceServerScopeDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceServerScopeDetailsTypeDef"]
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

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")
    InstanceArn = field("InstanceArn")

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
class UpdatePermissionSetRequest:
    boto3_raw_data: "type_defs.UpdatePermissionSetRequestTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")
    Description = field("Description")
    SessionDuration = field("SessionDuration")
    RelayState = field("RelayState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePermissionSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControlAttributeOutput:
    boto3_raw_data: "type_defs.AccessControlAttributeOutputTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")

    @cached_property
    def Value(self):  # pragma: no cover
        return AccessControlAttributeValueOutput.make_one(self.boto3_raw_data["Value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessControlAttributeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlAttributeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessControlAttribute:
    boto3_raw_data: "type_defs.AccessControlAttributeTypeDef" = dataclasses.field()

    Key = field("Key")

    @cached_property
    def Value(self):  # pragma: no cover
        return AccessControlAttributeValue.make_one(self.boto3_raw_data["Value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessControlAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessControlAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachCustomerManagedPolicyReferenceToPermissionSetRequest:
    boto3_raw_data: (
        "type_defs.AttachCustomerManagedPolicyReferenceToPermissionSetRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")

    @cached_property
    def CustomerManagedPolicyReference(self):  # pragma: no cover
        return CustomerManagedPolicyReference.make_one(
            self.boto3_raw_data["CustomerManagedPolicyReference"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachCustomerManagedPolicyReferenceToPermissionSetRequestTypeDef"
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
                "type_defs.AttachCustomerManagedPolicyReferenceToPermissionSetRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachCustomerManagedPolicyReferenceFromPermissionSetRequest:
    boto3_raw_data: (
        "type_defs.DetachCustomerManagedPolicyReferenceFromPermissionSetRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")

    @cached_property
    def CustomerManagedPolicyReference(self):  # pragma: no cover
        return CustomerManagedPolicyReference.make_one(
            self.boto3_raw_data["CustomerManagedPolicyReference"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachCustomerManagedPolicyReferenceFromPermissionSetRequestTypeDef"
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
                "type_defs.DetachCustomerManagedPolicyReferenceFromPermissionSetRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionsBoundary:
    boto3_raw_data: "type_defs.PermissionsBoundaryTypeDef" = dataclasses.field()

    @cached_property
    def CustomerManagedPolicyReference(self):  # pragma: no cover
        return CustomerManagedPolicyReference.make_one(
            self.boto3_raw_data["CustomerManagedPolicyReference"]
        )

    ManagedPolicyArn = field("ManagedPolicyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PermissionsBoundaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PermissionsBoundaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationMethodOutput:
    boto3_raw_data: "type_defs.AuthenticationMethodOutputTypeDef" = dataclasses.field()

    @cached_property
    def Iam(self):  # pragma: no cover
        return IamAuthenticationMethodOutput.make_one(self.boto3_raw_data["Iam"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationMethodOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationMethodOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationMethod:
    boto3_raw_data: "type_defs.AuthenticationMethodTypeDef" = dataclasses.field()

    @cached_property
    def Iam(self):  # pragma: no cover
        return IamAuthenticationMethod.make_one(self.boto3_raw_data["Iam"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationMethodTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationMethodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JwtBearerGrantOutput:
    boto3_raw_data: "type_defs.JwtBearerGrantOutputTypeDef" = dataclasses.field()

    @cached_property
    def AuthorizedTokenIssuers(self):  # pragma: no cover
        return AuthorizedTokenIssuerOutput.make_many(
            self.boto3_raw_data["AuthorizedTokenIssuers"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JwtBearerGrantOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JwtBearerGrantOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JwtBearerGrant:
    boto3_raw_data: "type_defs.JwtBearerGrantTypeDef" = dataclasses.field()

    @cached_property
    def AuthorizedTokenIssuers(self):  # pragma: no cover
        return AuthorizedTokenIssuer.make_many(
            self.boto3_raw_data["AuthorizedTokenIssuers"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JwtBearerGrantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JwtBearerGrantTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccountAssignmentResponse:
    boto3_raw_data: "type_defs.CreateAccountAssignmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountAssignmentCreationStatus(self):  # pragma: no cover
        return AccountAssignmentOperationStatus.make_one(
            self.boto3_raw_data["AccountAssignmentCreationStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAccountAssignmentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccountAssignmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationResponse:
    boto3_raw_data: "type_defs.CreateApplicationResponseTypeDef" = dataclasses.field()

    ApplicationArn = field("ApplicationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceResponse:
    boto3_raw_data: "type_defs.CreateInstanceResponseTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrustedTokenIssuerResponse:
    boto3_raw_data: "type_defs.CreateTrustedTokenIssuerResponseTypeDef" = (
        dataclasses.field()
    )

    TrustedTokenIssuerArn = field("TrustedTokenIssuerArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateTrustedTokenIssuerResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrustedTokenIssuerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountAssignmentResponse:
    boto3_raw_data: "type_defs.DeleteAccountAssignmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountAssignmentDeletionStatus(self):  # pragma: no cover
        return AccountAssignmentOperationStatus.make_one(
            self.boto3_raw_data["AccountAssignmentDeletionStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAccountAssignmentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccountAssignmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountAssignmentCreationStatusResponse:
    boto3_raw_data: (
        "type_defs.DescribeAccountAssignmentCreationStatusResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AccountAssignmentCreationStatus(self):  # pragma: no cover
        return AccountAssignmentOperationStatus.make_one(
            self.boto3_raw_data["AccountAssignmentCreationStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountAssignmentCreationStatusResponseTypeDef"
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
                "type_defs.DescribeAccountAssignmentCreationStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountAssignmentDeletionStatusResponse:
    boto3_raw_data: (
        "type_defs.DescribeAccountAssignmentDeletionStatusResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AccountAssignmentDeletionStatus(self):  # pragma: no cover
        return AccountAssignmentOperationStatus.make_one(
            self.boto3_raw_data["AccountAssignmentDeletionStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountAssignmentDeletionStatusResponseTypeDef"
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
                "type_defs.DescribeAccountAssignmentDeletionStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationAssignmentResponse:
    boto3_raw_data: "type_defs.DescribeApplicationAssignmentResponseTypeDef" = (
        dataclasses.field()
    )

    PrincipalType = field("PrincipalType")
    PrincipalId = field("PrincipalId")
    ApplicationArn = field("ApplicationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationAssignmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationAssignmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationAccessScopeResponse:
    boto3_raw_data: "type_defs.GetApplicationAccessScopeResponseTypeDef" = (
        dataclasses.field()
    )

    Scope = field("Scope")
    AuthorizedTargets = field("AuthorizedTargets")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationAccessScopeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationAccessScopeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationAssignmentConfigurationResponse:
    boto3_raw_data: "type_defs.GetApplicationAssignmentConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    AssignmentRequired = field("AssignmentRequired")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationAssignmentConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationAssignmentConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationSessionConfigurationResponse:
    boto3_raw_data: "type_defs.GetApplicationSessionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    UserBackgroundSessionApplicationStatus = field(
        "UserBackgroundSessionApplicationStatus"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationSessionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationSessionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInlinePolicyForPermissionSetResponse:
    boto3_raw_data: "type_defs.GetInlinePolicyForPermissionSetResponseTypeDef" = (
        dataclasses.field()
    )

    InlinePolicy = field("InlinePolicy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetInlinePolicyForPermissionSetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInlinePolicyForPermissionSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentCreationStatusResponse:
    boto3_raw_data: "type_defs.ListAccountAssignmentCreationStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountAssignmentsCreationStatus(self):  # pragma: no cover
        return AccountAssignmentOperationStatusMetadata.make_many(
            self.boto3_raw_data["AccountAssignmentsCreationStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAssignmentCreationStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssignmentCreationStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentDeletionStatusResponse:
    boto3_raw_data: "type_defs.ListAccountAssignmentDeletionStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountAssignmentsDeletionStatus(self):  # pragma: no cover
        return AccountAssignmentOperationStatusMetadata.make_many(
            self.boto3_raw_data["AccountAssignmentsDeletionStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAssignmentDeletionStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssignmentDeletionStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentsForPrincipalResponse:
    boto3_raw_data: "type_defs.ListAccountAssignmentsForPrincipalResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountAssignments(self):  # pragma: no cover
        return AccountAssignmentForPrincipal.make_many(
            self.boto3_raw_data["AccountAssignments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAssignmentsForPrincipalResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssignmentsForPrincipalResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentsResponse:
    boto3_raw_data: "type_defs.ListAccountAssignmentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountAssignments(self):  # pragma: no cover
        return AccountAssignment.make_many(self.boto3_raw_data["AccountAssignments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountAssignmentsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssignmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountsForProvisionedPermissionSetResponse:
    boto3_raw_data: (
        "type_defs.ListAccountsForProvisionedPermissionSetResponseTypeDef"
    ) = dataclasses.field()

    AccountIds = field("AccountIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountsForProvisionedPermissionSetResponseTypeDef"
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
                "type_defs.ListAccountsForProvisionedPermissionSetResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAssignmentsForPrincipalResponse:
    boto3_raw_data: (
        "type_defs.ListApplicationAssignmentsForPrincipalResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ApplicationAssignments(self):  # pragma: no cover
        return ApplicationAssignmentForPrincipal.make_many(
            self.boto3_raw_data["ApplicationAssignments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAssignmentsForPrincipalResponseTypeDef"
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
                "type_defs.ListApplicationAssignmentsForPrincipalResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAssignmentsResponse:
    boto3_raw_data: "type_defs.ListApplicationAssignmentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationAssignments(self):  # pragma: no cover
        return ApplicationAssignment.make_many(
            self.boto3_raw_data["ApplicationAssignments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAssignmentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationAssignmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomerManagedPolicyReferencesInPermissionSetResponse:
    boto3_raw_data: (
        "type_defs.ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def CustomerManagedPolicyReferences(self):  # pragma: no cover
        return CustomerManagedPolicyReference.make_many(
            self.boto3_raw_data["CustomerManagedPolicyReferences"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef"
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
                "type_defs.ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedPoliciesInPermissionSetResponse:
    boto3_raw_data: "type_defs.ListManagedPoliciesInPermissionSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AttachedManagedPolicies(self):  # pragma: no cover
        return AttachedManagedPolicy.make_many(
            self.boto3_raw_data["AttachedManagedPolicies"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedPoliciesInPermissionSetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedPoliciesInPermissionSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionSetsProvisionedToAccountResponse:
    boto3_raw_data: (
        "type_defs.ListPermissionSetsProvisionedToAccountResponseTypeDef"
    ) = dataclasses.field()

    PermissionSets = field("PermissionSets")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPermissionSetsProvisionedToAccountResponseTypeDef"
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
                "type_defs.ListPermissionSetsProvisionedToAccountResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionSetsResponse:
    boto3_raw_data: "type_defs.ListPermissionSetsResponseTypeDef" = dataclasses.field()

    PermissionSets = field("PermissionSets")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPermissionSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceRequest:
    boto3_raw_data: "type_defs.CreateInstanceRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePermissionSetRequest:
    boto3_raw_data: "type_defs.CreatePermissionSetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    InstanceArn = field("InstanceArn")
    Description = field("Description")
    SessionDuration = field("SessionDuration")
    RelayState = field("RelayState")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePermissionSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePermissionSetRequestTypeDef"]
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

    NextToken = field("NextToken")

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

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    InstanceArn = field("InstanceArn")

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
class CreatePermissionSetResponse:
    boto3_raw_data: "type_defs.CreatePermissionSetResponseTypeDef" = dataclasses.field()

    @cached_property
    def PermissionSet(self):  # pragma: no cover
        return PermissionSet.make_one(self.boto3_raw_data["PermissionSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePermissionSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePermissionSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePermissionSetResponse:
    boto3_raw_data: "type_defs.DescribePermissionSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PermissionSet(self):  # pragma: no cover
        return PermissionSet.make_one(self.boto3_raw_data["PermissionSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePermissionSetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePermissionSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceResponse:
    boto3_raw_data: "type_defs.DescribeInstanceResponseTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    IdentityStoreId = field("IdentityStoreId")
    OwnerAccountId = field("OwnerAccountId")
    Name = field("Name")
    CreatedDate = field("CreatedDate")
    Status = field("Status")
    StatusReason = field("StatusReason")

    @cached_property
    def EncryptionConfigurationDetails(self):  # pragma: no cover
        return EncryptionConfigurationDetails.make_one(
            self.boto3_raw_data["EncryptionConfigurationDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInstanceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePermissionSetProvisioningStatusResponse:
    boto3_raw_data: (
        "type_defs.DescribePermissionSetProvisioningStatusResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PermissionSetProvisioningStatus(self):  # pragma: no cover
        return PermissionSetProvisioningStatus.make_one(
            self.boto3_raw_data["PermissionSetProvisioningStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePermissionSetProvisioningStatusResponseTypeDef"
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
                "type_defs.DescribePermissionSetProvisioningStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionPermissionSetResponse:
    boto3_raw_data: "type_defs.ProvisionPermissionSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PermissionSetProvisioningStatus(self):  # pragma: no cover
        return PermissionSetProvisioningStatus.make_one(
            self.boto3_raw_data["PermissionSetProvisioningStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisionPermissionSetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionPermissionSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInstanceRequest:
    boto3_raw_data: "type_defs.UpdateInstanceRequestTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    Name = field("Name")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateInstanceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesResponse:
    boto3_raw_data: "type_defs.ListInstancesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Instances(self):  # pragma: no cover
        return InstanceMetadata.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentCreationStatusRequest:
    boto3_raw_data: "type_defs.ListAccountAssignmentCreationStatusRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filter(self):  # pragma: no cover
        return OperationStatusFilter.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAssignmentCreationStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssignmentCreationStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentDeletionStatusRequest:
    boto3_raw_data: "type_defs.ListAccountAssignmentDeletionStatusRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filter(self):  # pragma: no cover
        return OperationStatusFilter.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAssignmentDeletionStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssignmentDeletionStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionSetProvisioningStatusRequest:
    boto3_raw_data: "type_defs.ListPermissionSetProvisioningStatusRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filter(self):  # pragma: no cover
        return OperationStatusFilter.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPermissionSetProvisioningStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionSetProvisioningStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentCreationStatusRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAccountAssignmentCreationStatusRequestPaginateTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")

    @cached_property
    def Filter(self):  # pragma: no cover
        return OperationStatusFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAssignmentCreationStatusRequestPaginateTypeDef"
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
                "type_defs.ListAccountAssignmentCreationStatusRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentDeletionStatusRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAccountAssignmentDeletionStatusRequestPaginateTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")

    @cached_property
    def Filter(self):  # pragma: no cover
        return OperationStatusFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAssignmentDeletionStatusRequestPaginateTypeDef"
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
                "type_defs.ListAccountAssignmentDeletionStatusRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListAccountAssignmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    AccountId = field("AccountId")
    PermissionSetArn = field("PermissionSetArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAssignmentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssignmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountsForProvisionedPermissionSetRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAccountsForProvisionedPermissionSetRequestPaginateTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")
    ProvisioningStatus = field("ProvisioningStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountsForProvisionedPermissionSetRequestPaginateTypeDef"
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
                "type_defs.ListAccountsForProvisionedPermissionSetRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAccessScopesRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationAccessScopesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAccessScopesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationAccessScopesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAssignmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationAssignmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAssignmentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationAssignmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAuthenticationMethodsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListApplicationAuthenticationMethodsRequestPaginateTypeDef"
    ) = dataclasses.field()

    ApplicationArn = field("ApplicationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAuthenticationMethodsRequestPaginateTypeDef"
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
                "type_defs.ListApplicationAuthenticationMethodsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationGrantsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationGrantsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationGrantsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationGrantsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationProvidersRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationProvidersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationProvidersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationProvidersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomerManagedPolicyReferencesInPermissionSetRequestPaginate:
    boto3_raw_data: "type_defs.ListCustomerManagedPolicyReferencesInPermissionSetRequestPaginateTypeDef" = (dataclasses.field())

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomerManagedPolicyReferencesInPermissionSetRequestPaginateTypeDef"
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
                "type_defs.ListCustomerManagedPolicyReferencesInPermissionSetRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInstancesRequestPaginate:
    boto3_raw_data: "type_defs.ListInstancesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInstancesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInstancesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedPoliciesInPermissionSetRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListManagedPoliciesInPermissionSetRequestPaginateTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedPoliciesInPermissionSetRequestPaginateTypeDef"
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
                "type_defs.ListManagedPoliciesInPermissionSetRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionSetProvisioningStatusRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListPermissionSetProvisioningStatusRequestPaginateTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")

    @cached_property
    def Filter(self):  # pragma: no cover
        return OperationStatusFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPermissionSetProvisioningStatusRequestPaginateTypeDef"
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
                "type_defs.ListPermissionSetProvisioningStatusRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionSetsProvisionedToAccountRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListPermissionSetsProvisionedToAccountRequestPaginateTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    AccountId = field("AccountId")
    ProvisioningStatus = field("ProvisioningStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPermissionSetsProvisionedToAccountRequestPaginateTypeDef"
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
                "type_defs.ListPermissionSetsProvisionedToAccountRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionSetsRequestPaginate:
    boto3_raw_data: "type_defs.ListPermissionSetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPermissionSetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequestPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    InstanceArn = field("InstanceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTagsForResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrustedTokenIssuersRequestPaginate:
    boto3_raw_data: "type_defs.ListTrustedTokenIssuersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrustedTokenIssuersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrustedTokenIssuersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentsForPrincipalRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAccountAssignmentsForPrincipalRequestPaginateTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    PrincipalId = field("PrincipalId")
    PrincipalType = field("PrincipalType")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ListAccountAssignmentsFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAssignmentsForPrincipalRequestPaginateTypeDef"
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
                "type_defs.ListAccountAssignmentsForPrincipalRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountAssignmentsForPrincipalRequest:
    boto3_raw_data: "type_defs.ListAccountAssignmentsForPrincipalRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PrincipalId = field("PrincipalId")
    PrincipalType = field("PrincipalType")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ListAccountAssignmentsFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountAssignmentsForPrincipalRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountAssignmentsForPrincipalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAccessScopesResponse:
    boto3_raw_data: "type_defs.ListApplicationAccessScopesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Scopes(self):  # pragma: no cover
        return ScopeDetails.make_many(self.boto3_raw_data["Scopes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAccessScopesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationAccessScopesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAssignmentsForPrincipalRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListApplicationAssignmentsForPrincipalRequestPaginateTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    PrincipalId = field("PrincipalId")
    PrincipalType = field("PrincipalType")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ListApplicationAssignmentsFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAssignmentsForPrincipalRequestPaginateTypeDef"
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
                "type_defs.ListApplicationAssignmentsForPrincipalRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAssignmentsForPrincipalRequest:
    boto3_raw_data: "type_defs.ListApplicationAssignmentsForPrincipalRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PrincipalId = field("PrincipalId")
    PrincipalType = field("PrincipalType")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ListApplicationAssignmentsFilter.make_one(self.boto3_raw_data["Filter"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAssignmentsForPrincipalRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationAssignmentsForPrincipalRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ListApplicationsFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequest:
    boto3_raw_data: "type_defs.ListApplicationsRequestTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ListApplicationsFilter.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPermissionSetProvisioningStatusResponse:
    boto3_raw_data: "type_defs.ListPermissionSetProvisioningStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PermissionSetsProvisioningStatus(self):  # pragma: no cover
        return PermissionSetProvisioningStatusMetadata.make_many(
            self.boto3_raw_data["PermissionSetsProvisioningStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPermissionSetProvisioningStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPermissionSetProvisioningStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrustedTokenIssuersResponse:
    boto3_raw_data: "type_defs.ListTrustedTokenIssuersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrustedTokenIssuers(self):  # pragma: no cover
        return TrustedTokenIssuerMetadata.make_many(
            self.boto3_raw_data["TrustedTokenIssuers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTrustedTokenIssuersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrustedTokenIssuersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedTokenIssuerConfiguration:
    boto3_raw_data: "type_defs.TrustedTokenIssuerConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OidcJwtConfiguration(self):  # pragma: no cover
        return OidcJwtConfiguration.make_one(
            self.boto3_raw_data["OidcJwtConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TrustedTokenIssuerConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedTokenIssuerConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustedTokenIssuerUpdateConfiguration:
    boto3_raw_data: "type_defs.TrustedTokenIssuerUpdateConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OidcJwtConfiguration(self):  # pragma: no cover
        return OidcJwtUpdateConfiguration.make_one(
            self.boto3_raw_data["OidcJwtConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrustedTokenIssuerUpdateConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustedTokenIssuerUpdateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PortalOptions:
    boto3_raw_data: "type_defs.PortalOptionsTypeDef" = dataclasses.field()

    @cached_property
    def SignInOptions(self):  # pragma: no cover
        return SignInOptions.make_one(self.boto3_raw_data["SignInOptions"])

    Visibility = field("Visibility")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PortalOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PortalOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationPortalOptions:
    boto3_raw_data: "type_defs.UpdateApplicationPortalOptionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SignInOptions(self):  # pragma: no cover
        return SignInOptions.make_one(self.boto3_raw_data["SignInOptions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateApplicationPortalOptionsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationPortalOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceServerConfig:
    boto3_raw_data: "type_defs.ResourceServerConfigTypeDef" = dataclasses.field()

    Scopes = field("Scopes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceServerConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceServerConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceAccessControlAttributeConfigurationOutput:
    boto3_raw_data: (
        "type_defs.InstanceAccessControlAttributeConfigurationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AccessControlAttributes(self):  # pragma: no cover
        return AccessControlAttributeOutput.make_many(
            self.boto3_raw_data["AccessControlAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceAccessControlAttributeConfigurationOutputTypeDef"
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
                "type_defs.InstanceAccessControlAttributeConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceAccessControlAttributeConfiguration:
    boto3_raw_data: "type_defs.InstanceAccessControlAttributeConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessControlAttributes(self):  # pragma: no cover
        return AccessControlAttribute.make_many(
            self.boto3_raw_data["AccessControlAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InstanceAccessControlAttributeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceAccessControlAttributeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPermissionsBoundaryForPermissionSetResponse:
    boto3_raw_data: (
        "type_defs.GetPermissionsBoundaryForPermissionSetResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PermissionsBoundary(self):  # pragma: no cover
        return PermissionsBoundary.make_one(self.boto3_raw_data["PermissionsBoundary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPermissionsBoundaryForPermissionSetResponseTypeDef"
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
                "type_defs.GetPermissionsBoundaryForPermissionSetResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPermissionsBoundaryToPermissionSetRequest:
    boto3_raw_data: "type_defs.PutPermissionsBoundaryToPermissionSetRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    PermissionSetArn = field("PermissionSetArn")

    @cached_property
    def PermissionsBoundary(self):  # pragma: no cover
        return PermissionsBoundary.make_one(self.boto3_raw_data["PermissionsBoundary"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutPermissionsBoundaryToPermissionSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPermissionsBoundaryToPermissionSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationMethodItem:
    boto3_raw_data: "type_defs.AuthenticationMethodItemTypeDef" = dataclasses.field()

    AuthenticationMethodType = field("AuthenticationMethodType")

    @cached_property
    def AuthenticationMethod(self):  # pragma: no cover
        return AuthenticationMethodOutput.make_one(
            self.boto3_raw_data["AuthenticationMethod"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationMethodItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationMethodItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationAuthenticationMethodResponse:
    boto3_raw_data: "type_defs.GetApplicationAuthenticationMethodResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuthenticationMethod(self):  # pragma: no cover
        return AuthenticationMethodOutput.make_one(
            self.boto3_raw_data["AuthenticationMethod"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetApplicationAuthenticationMethodResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationAuthenticationMethodResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantOutput:
    boto3_raw_data: "type_defs.GrantOutputTypeDef" = dataclasses.field()

    @cached_property
    def AuthorizationCode(self):  # pragma: no cover
        return AuthorizationCodeGrantOutput.make_one(
            self.boto3_raw_data["AuthorizationCode"]
        )

    @cached_property
    def JwtBearer(self):  # pragma: no cover
        return JwtBearerGrantOutput.make_one(self.boto3_raw_data["JwtBearer"])

    RefreshToken = field("RefreshToken")
    TokenExchange = field("TokenExchange")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrantOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Grant:
    boto3_raw_data: "type_defs.GrantTypeDef" = dataclasses.field()

    @cached_property
    def AuthorizationCode(self):  # pragma: no cover
        return AuthorizationCodeGrant.make_one(self.boto3_raw_data["AuthorizationCode"])

    @cached_property
    def JwtBearer(self):  # pragma: no cover
        return JwtBearerGrant.make_one(self.boto3_raw_data["JwtBearer"])

    RefreshToken = field("RefreshToken")
    TokenExchange = field("TokenExchange")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrantTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrustedTokenIssuerRequest:
    boto3_raw_data: "type_defs.CreateTrustedTokenIssuerRequestTypeDef" = (
        dataclasses.field()
    )

    InstanceArn = field("InstanceArn")
    Name = field("Name")
    TrustedTokenIssuerType = field("TrustedTokenIssuerType")

    @cached_property
    def TrustedTokenIssuerConfiguration(self):  # pragma: no cover
        return TrustedTokenIssuerConfiguration.make_one(
            self.boto3_raw_data["TrustedTokenIssuerConfiguration"]
        )

    ClientToken = field("ClientToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateTrustedTokenIssuerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrustedTokenIssuerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustedTokenIssuerResponse:
    boto3_raw_data: "type_defs.DescribeTrustedTokenIssuerResponseTypeDef" = (
        dataclasses.field()
    )

    TrustedTokenIssuerArn = field("TrustedTokenIssuerArn")
    Name = field("Name")
    TrustedTokenIssuerType = field("TrustedTokenIssuerType")

    @cached_property
    def TrustedTokenIssuerConfiguration(self):  # pragma: no cover
        return TrustedTokenIssuerConfiguration.make_one(
            self.boto3_raw_data["TrustedTokenIssuerConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustedTokenIssuerResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustedTokenIssuerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrustedTokenIssuerRequest:
    boto3_raw_data: "type_defs.UpdateTrustedTokenIssuerRequestTypeDef" = (
        dataclasses.field()
    )

    TrustedTokenIssuerArn = field("TrustedTokenIssuerArn")
    Name = field("Name")

    @cached_property
    def TrustedTokenIssuerConfiguration(self):  # pragma: no cover
        return TrustedTokenIssuerUpdateConfiguration.make_one(
            self.boto3_raw_data["TrustedTokenIssuerConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateTrustedTokenIssuerRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrustedTokenIssuerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Application:
    boto3_raw_data: "type_defs.ApplicationTypeDef" = dataclasses.field()

    ApplicationArn = field("ApplicationArn")
    ApplicationProviderArn = field("ApplicationProviderArn")
    Name = field("Name")
    ApplicationAccount = field("ApplicationAccount")
    InstanceArn = field("InstanceArn")
    Status = field("Status")

    @cached_property
    def PortalOptions(self):  # pragma: no cover
        return PortalOptions.make_one(self.boto3_raw_data["PortalOptions"])

    Description = field("Description")
    CreatedDate = field("CreatedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApplicationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationRequest:
    boto3_raw_data: "type_defs.CreateApplicationRequestTypeDef" = dataclasses.field()

    InstanceArn = field("InstanceArn")
    ApplicationProviderArn = field("ApplicationProviderArn")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def PortalOptions(self):  # pragma: no cover
        return PortalOptions.make_one(self.boto3_raw_data["PortalOptions"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Status = field("Status")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationResponse:
    boto3_raw_data: "type_defs.DescribeApplicationResponseTypeDef" = dataclasses.field()

    ApplicationArn = field("ApplicationArn")
    ApplicationProviderArn = field("ApplicationProviderArn")
    Name = field("Name")
    ApplicationAccount = field("ApplicationAccount")
    InstanceArn = field("InstanceArn")
    Status = field("Status")

    @cached_property
    def PortalOptions(self):  # pragma: no cover
        return PortalOptions.make_one(self.boto3_raw_data["PortalOptions"])

    Description = field("Description")
    CreatedDate = field("CreatedDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationRequest:
    boto3_raw_data: "type_defs.UpdateApplicationRequestTypeDef" = dataclasses.field()

    ApplicationArn = field("ApplicationArn")
    Name = field("Name")
    Description = field("Description")
    Status = field("Status")

    @cached_property
    def PortalOptions(self):  # pragma: no cover
        return UpdateApplicationPortalOptions.make_one(
            self.boto3_raw_data["PortalOptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationProvider:
    boto3_raw_data: "type_defs.ApplicationProviderTypeDef" = dataclasses.field()

    ApplicationProviderArn = field("ApplicationProviderArn")
    FederationProtocol = field("FederationProtocol")

    @cached_property
    def DisplayData(self):  # pragma: no cover
        return DisplayData.make_one(self.boto3_raw_data["DisplayData"])

    @cached_property
    def ResourceServerConfig(self):  # pragma: no cover
        return ResourceServerConfig.make_one(
            self.boto3_raw_data["ResourceServerConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationProviderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationProviderResponse:
    boto3_raw_data: "type_defs.DescribeApplicationProviderResponseTypeDef" = (
        dataclasses.field()
    )

    ApplicationProviderArn = field("ApplicationProviderArn")
    FederationProtocol = field("FederationProtocol")

    @cached_property
    def DisplayData(self):  # pragma: no cover
        return DisplayData.make_one(self.boto3_raw_data["DisplayData"])

    @cached_property
    def ResourceServerConfig(self):  # pragma: no cover
        return ResourceServerConfig.make_one(
            self.boto3_raw_data["ResourceServerConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationProviderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceAccessControlAttributeConfigurationResponse:
    boto3_raw_data: (
        "type_defs.DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef"
    ) = dataclasses.field()

    Status = field("Status")
    StatusReason = field("StatusReason")

    @cached_property
    def InstanceAccessControlAttributeConfiguration(self):  # pragma: no cover
        return InstanceAccessControlAttributeConfigurationOutput.make_one(
            self.boto3_raw_data["InstanceAccessControlAttributeConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef"
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
                "type_defs.DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationAuthenticationMethodsResponse:
    boto3_raw_data: "type_defs.ListApplicationAuthenticationMethodsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AuthenticationMethods(self):  # pragma: no cover
        return AuthenticationMethodItem.make_many(
            self.boto3_raw_data["AuthenticationMethods"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListApplicationAuthenticationMethodsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationAuthenticationMethodsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutApplicationAuthenticationMethodRequest:
    boto3_raw_data: "type_defs.PutApplicationAuthenticationMethodRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationArn = field("ApplicationArn")
    AuthenticationMethodType = field("AuthenticationMethodType")
    AuthenticationMethod = field("AuthenticationMethod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutApplicationAuthenticationMethodRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutApplicationAuthenticationMethodRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationGrantResponse:
    boto3_raw_data: "type_defs.GetApplicationGrantResponseTypeDef" = dataclasses.field()

    @cached_property
    def Grant(self):  # pragma: no cover
        return GrantOutput.make_one(self.boto3_raw_data["Grant"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationGrantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationGrantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantItem:
    boto3_raw_data: "type_defs.GrantItemTypeDef" = dataclasses.field()

    GrantType = field("GrantType")

    @cached_property
    def Grant(self):  # pragma: no cover
        return GrantOutput.make_one(self.boto3_raw_data["Grant"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrantItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsResponse:
    boto3_raw_data: "type_defs.ListApplicationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Applications(self):  # pragma: no cover
        return Application.make_many(self.boto3_raw_data["Applications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationProvidersResponse:
    boto3_raw_data: "type_defs.ListApplicationProvidersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationProviders(self):  # pragma: no cover
        return ApplicationProvider.make_many(
            self.boto3_raw_data["ApplicationProviders"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationProvidersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceAccessControlAttributeConfigurationRequest:
    boto3_raw_data: (
        "type_defs.CreateInstanceAccessControlAttributeConfigurationRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    InstanceAccessControlAttributeConfiguration = field(
        "InstanceAccessControlAttributeConfiguration"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateInstanceAccessControlAttributeConfigurationRequestTypeDef"
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
                "type_defs.CreateInstanceAccessControlAttributeConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInstanceAccessControlAttributeConfigurationRequest:
    boto3_raw_data: (
        "type_defs.UpdateInstanceAccessControlAttributeConfigurationRequestTypeDef"
    ) = dataclasses.field()

    InstanceArn = field("InstanceArn")
    InstanceAccessControlAttributeConfiguration = field(
        "InstanceAccessControlAttributeConfiguration"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateInstanceAccessControlAttributeConfigurationRequestTypeDef"
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
                "type_defs.UpdateInstanceAccessControlAttributeConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationGrantsResponse:
    boto3_raw_data: "type_defs.ListApplicationGrantsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Grants(self):  # pragma: no cover
        return GrantItem.make_many(self.boto3_raw_data["Grants"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationGrantsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationGrantsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutApplicationGrantRequest:
    boto3_raw_data: "type_defs.PutApplicationGrantRequestTypeDef" = dataclasses.field()

    ApplicationArn = field("ApplicationArn")
    GrantType = field("GrantType")
    Grant = field("Grant")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutApplicationGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutApplicationGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
