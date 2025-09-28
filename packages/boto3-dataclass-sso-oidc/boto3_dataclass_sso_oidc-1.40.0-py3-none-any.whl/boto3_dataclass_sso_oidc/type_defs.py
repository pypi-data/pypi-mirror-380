# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sso_oidc import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AwsAdditionalDetails:
    boto3_raw_data: "type_defs.AwsAdditionalDetailsTypeDef" = dataclasses.field()

    identityContext = field("identityContext")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsAdditionalDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsAdditionalDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTokenRequest:
    boto3_raw_data: "type_defs.CreateTokenRequestTypeDef" = dataclasses.field()

    clientId = field("clientId")
    clientSecret = field("clientSecret")
    grantType = field("grantType")
    deviceCode = field("deviceCode")
    code = field("code")
    refreshToken = field("refreshToken")
    scope = field("scope")
    redirectUri = field("redirectUri")
    codeVerifier = field("codeVerifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTokenRequestTypeDef"]
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
class CreateTokenWithIAMRequest:
    boto3_raw_data: "type_defs.CreateTokenWithIAMRequestTypeDef" = dataclasses.field()

    clientId = field("clientId")
    grantType = field("grantType")
    code = field("code")
    refreshToken = field("refreshToken")
    assertion = field("assertion")
    scope = field("scope")
    redirectUri = field("redirectUri")
    subjectToken = field("subjectToken")
    subjectTokenType = field("subjectTokenType")
    requestedTokenType = field("requestedTokenType")
    codeVerifier = field("codeVerifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTokenWithIAMRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTokenWithIAMRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterClientRequest:
    boto3_raw_data: "type_defs.RegisterClientRequestTypeDef" = dataclasses.field()

    clientName = field("clientName")
    clientType = field("clientType")
    scopes = field("scopes")
    redirectUris = field("redirectUris")
    grantTypes = field("grantTypes")
    issuerUrl = field("issuerUrl")
    entitledApplicationArn = field("entitledApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterClientRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterClientRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDeviceAuthorizationRequest:
    boto3_raw_data: "type_defs.StartDeviceAuthorizationRequestTypeDef" = (
        dataclasses.field()
    )

    clientId = field("clientId")
    clientSecret = field("clientSecret")
    startUrl = field("startUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDeviceAuthorizationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDeviceAuthorizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTokenResponse:
    boto3_raw_data: "type_defs.CreateTokenResponseTypeDef" = dataclasses.field()

    accessToken = field("accessToken")
    tokenType = field("tokenType")
    expiresIn = field("expiresIn")
    refreshToken = field("refreshToken")
    idToken = field("idToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTokenWithIAMResponse:
    boto3_raw_data: "type_defs.CreateTokenWithIAMResponseTypeDef" = dataclasses.field()

    accessToken = field("accessToken")
    tokenType = field("tokenType")
    expiresIn = field("expiresIn")
    refreshToken = field("refreshToken")
    idToken = field("idToken")
    issuedTokenType = field("issuedTokenType")
    scope = field("scope")

    @cached_property
    def awsAdditionalDetails(self):  # pragma: no cover
        return AwsAdditionalDetails.make_one(
            self.boto3_raw_data["awsAdditionalDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTokenWithIAMResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTokenWithIAMResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterClientResponse:
    boto3_raw_data: "type_defs.RegisterClientResponseTypeDef" = dataclasses.field()

    clientId = field("clientId")
    clientSecret = field("clientSecret")
    clientIdIssuedAt = field("clientIdIssuedAt")
    clientSecretExpiresAt = field("clientSecretExpiresAt")
    authorizationEndpoint = field("authorizationEndpoint")
    tokenEndpoint = field("tokenEndpoint")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterClientResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterClientResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDeviceAuthorizationResponse:
    boto3_raw_data: "type_defs.StartDeviceAuthorizationResponseTypeDef" = (
        dataclasses.field()
    )

    deviceCode = field("deviceCode")
    userCode = field("userCode")
    verificationUri = field("verificationUri")
    verificationUriComplete = field("verificationUriComplete")
    expiresIn = field("expiresIn")
    interval = field("interval")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDeviceAuthorizationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDeviceAuthorizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
