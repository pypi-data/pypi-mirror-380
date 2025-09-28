# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sso_oidc import type_defs as bs_td


class SSO_OIDCCaster:

    def create_token(
        self,
        res: "bs_td.CreateTokenResponseTypeDef",
    ) -> "dc_td.CreateTokenResponse":
        return dc_td.CreateTokenResponse.make_one(res)

    def create_token_with_iam(
        self,
        res: "bs_td.CreateTokenWithIAMResponseTypeDef",
    ) -> "dc_td.CreateTokenWithIAMResponse":
        return dc_td.CreateTokenWithIAMResponse.make_one(res)

    def register_client(
        self,
        res: "bs_td.RegisterClientResponseTypeDef",
    ) -> "dc_td.RegisterClientResponse":
        return dc_td.RegisterClientResponse.make_one(res)

    def start_device_authorization(
        self,
        res: "bs_td.StartDeviceAuthorizationResponseTypeDef",
    ) -> "dc_td.StartDeviceAuthorizationResponse":
        return dc_td.StartDeviceAuthorizationResponse.make_one(res)


sso_oidc_caster = SSO_OIDCCaster()
