# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sts import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class PolicyDescriptorType:
    boto3_raw_data: "type_defs.PolicyDescriptorTypeTypeDef" = dataclasses.field()

    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyDescriptorTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyDescriptorTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvidedContext:
    boto3_raw_data: "type_defs.ProvidedContextTypeDef" = dataclasses.field()

    ProviderArn = field("ProviderArn")
    ContextAssertion = field("ContextAssertion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProvidedContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProvidedContextTypeDef"]],
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
class AssumedRoleUser:
    boto3_raw_data: "type_defs.AssumedRoleUserTypeDef" = dataclasses.field()

    AssumedRoleId = field("AssumedRoleId")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssumedRoleUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssumedRoleUserTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Credentials:
    boto3_raw_data: "type_defs.CredentialsTypeDef" = dataclasses.field()

    AccessKeyId = field("AccessKeyId")
    SecretAccessKey = field("SecretAccessKey")
    SessionToken = field("SessionToken")
    Expiration = field("Expiration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CredentialsTypeDef"]]
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
class DecodeAuthorizationMessageRequest:
    boto3_raw_data: "type_defs.DecodeAuthorizationMessageRequestTypeDef" = (
        dataclasses.field()
    )

    EncodedMessage = field("EncodedMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DecodeAuthorizationMessageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecodeAuthorizationMessageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FederatedUser:
    boto3_raw_data: "type_defs.FederatedUserTypeDef" = dataclasses.field()

    FederatedUserId = field("FederatedUserId")
    Arn = field("Arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FederatedUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FederatedUserTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessKeyInfoRequest:
    boto3_raw_data: "type_defs.GetAccessKeyInfoRequestTypeDef" = dataclasses.field()

    AccessKeyId = field("AccessKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessKeyInfoRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessKeyInfoRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionTokenRequest:
    boto3_raw_data: "type_defs.GetSessionTokenRequestTypeDef" = dataclasses.field()

    DurationSeconds = field("DurationSeconds")
    SerialNumber = field("SerialNumber")
    TokenCode = field("TokenCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeRoleWithSAMLRequest:
    boto3_raw_data: "type_defs.AssumeRoleWithSAMLRequestTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    PrincipalArn = field("PrincipalArn")
    SAMLAssertion = field("SAMLAssertion")

    @cached_property
    def PolicyArns(self):  # pragma: no cover
        return PolicyDescriptorType.make_many(self.boto3_raw_data["PolicyArns"])

    Policy = field("Policy")
    DurationSeconds = field("DurationSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssumeRoleWithSAMLRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeRoleWithSAMLRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeRoleWithWebIdentityRequest:
    boto3_raw_data: "type_defs.AssumeRoleWithWebIdentityRequestTypeDef" = (
        dataclasses.field()
    )

    RoleArn = field("RoleArn")
    RoleSessionName = field("RoleSessionName")
    WebIdentityToken = field("WebIdentityToken")
    ProviderId = field("ProviderId")

    @cached_property
    def PolicyArns(self):  # pragma: no cover
        return PolicyDescriptorType.make_many(self.boto3_raw_data["PolicyArns"])

    Policy = field("Policy")
    DurationSeconds = field("DurationSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeRoleWithWebIdentityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeRoleWithWebIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeRootRequest:
    boto3_raw_data: "type_defs.AssumeRootRequestTypeDef" = dataclasses.field()

    TargetPrincipal = field("TargetPrincipal")

    @cached_property
    def TaskPolicyArn(self):  # pragma: no cover
        return PolicyDescriptorType.make_one(self.boto3_raw_data["TaskPolicyArn"])

    DurationSeconds = field("DurationSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssumeRootRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeRootRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeRoleRequest:
    boto3_raw_data: "type_defs.AssumeRoleRequestTypeDef" = dataclasses.field()

    RoleArn = field("RoleArn")
    RoleSessionName = field("RoleSessionName")

    @cached_property
    def PolicyArns(self):  # pragma: no cover
        return PolicyDescriptorType.make_many(self.boto3_raw_data["PolicyArns"])

    Policy = field("Policy")
    DurationSeconds = field("DurationSeconds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    TransitiveTagKeys = field("TransitiveTagKeys")
    ExternalId = field("ExternalId")
    SerialNumber = field("SerialNumber")
    TokenCode = field("TokenCode")
    SourceIdentity = field("SourceIdentity")

    @cached_property
    def ProvidedContexts(self):  # pragma: no cover
        return ProvidedContext.make_many(self.boto3_raw_data["ProvidedContexts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssumeRoleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeRoleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFederationTokenRequest:
    boto3_raw_data: "type_defs.GetFederationTokenRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Policy = field("Policy")

    @cached_property
    def PolicyArns(self):  # pragma: no cover
        return PolicyDescriptorType.make_many(self.boto3_raw_data["PolicyArns"])

    DurationSeconds = field("DurationSeconds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFederationTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFederationTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeRoleResponse:
    boto3_raw_data: "type_defs.AssumeRoleResponseTypeDef" = dataclasses.field()

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["Credentials"])

    @cached_property
    def AssumedRoleUser(self):  # pragma: no cover
        return AssumedRoleUser.make_one(self.boto3_raw_data["AssumedRoleUser"])

    PackedPolicySize = field("PackedPolicySize")
    SourceIdentity = field("SourceIdentity")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssumeRoleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeRoleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeRoleWithSAMLResponse:
    boto3_raw_data: "type_defs.AssumeRoleWithSAMLResponseTypeDef" = dataclasses.field()

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["Credentials"])

    @cached_property
    def AssumedRoleUser(self):  # pragma: no cover
        return AssumedRoleUser.make_one(self.boto3_raw_data["AssumedRoleUser"])

    PackedPolicySize = field("PackedPolicySize")
    Subject = field("Subject")
    SubjectType = field("SubjectType")
    Issuer = field("Issuer")
    Audience = field("Audience")
    NameQualifier = field("NameQualifier")
    SourceIdentity = field("SourceIdentity")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssumeRoleWithSAMLResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeRoleWithSAMLResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeRoleWithWebIdentityResponse:
    boto3_raw_data: "type_defs.AssumeRoleWithWebIdentityResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["Credentials"])

    SubjectFromWebIdentityToken = field("SubjectFromWebIdentityToken")

    @cached_property
    def AssumedRoleUser(self):  # pragma: no cover
        return AssumedRoleUser.make_one(self.boto3_raw_data["AssumedRoleUser"])

    PackedPolicySize = field("PackedPolicySize")
    Provider = field("Provider")
    Audience = field("Audience")
    SourceIdentity = field("SourceIdentity")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssumeRoleWithWebIdentityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeRoleWithWebIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeRootResponse:
    boto3_raw_data: "type_defs.AssumeRootResponseTypeDef" = dataclasses.field()

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["Credentials"])

    SourceIdentity = field("SourceIdentity")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssumeRootResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeRootResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecodeAuthorizationMessageResponse:
    boto3_raw_data: "type_defs.DecodeAuthorizationMessageResponseTypeDef" = (
        dataclasses.field()
    )

    DecodedMessage = field("DecodedMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DecodeAuthorizationMessageResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecodeAuthorizationMessageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessKeyInfoResponse:
    boto3_raw_data: "type_defs.GetAccessKeyInfoResponseTypeDef" = dataclasses.field()

    Account = field("Account")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessKeyInfoResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessKeyInfoResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCallerIdentityResponse:
    boto3_raw_data: "type_defs.GetCallerIdentityResponseTypeDef" = dataclasses.field()

    UserId = field("UserId")
    Account = field("Account")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCallerIdentityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCallerIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSessionTokenResponse:
    boto3_raw_data: "type_defs.GetSessionTokenResponseTypeDef" = dataclasses.field()

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["Credentials"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSessionTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSessionTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFederationTokenResponse:
    boto3_raw_data: "type_defs.GetFederationTokenResponseTypeDef" = dataclasses.field()

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["Credentials"])

    @cached_property
    def FederatedUser(self):  # pragma: no cover
        return FederatedUser.make_one(self.boto3_raw_data["FederatedUser"])

    PackedPolicySize = field("PackedPolicySize")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFederationTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFederationTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
