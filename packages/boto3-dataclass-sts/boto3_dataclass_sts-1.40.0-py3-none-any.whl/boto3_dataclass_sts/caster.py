# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sts import type_defs as bs_td


class STSCaster:

    def assume_role(
        self,
        res: "bs_td.AssumeRoleResponseTypeDef",
    ) -> "dc_td.AssumeRoleResponse":
        return dc_td.AssumeRoleResponse.make_one(res)

    def assume_role_with_saml(
        self,
        res: "bs_td.AssumeRoleWithSAMLResponseTypeDef",
    ) -> "dc_td.AssumeRoleWithSAMLResponse":
        return dc_td.AssumeRoleWithSAMLResponse.make_one(res)

    def assume_role_with_web_identity(
        self,
        res: "bs_td.AssumeRoleWithWebIdentityResponseTypeDef",
    ) -> "dc_td.AssumeRoleWithWebIdentityResponse":
        return dc_td.AssumeRoleWithWebIdentityResponse.make_one(res)

    def assume_root(
        self,
        res: "bs_td.AssumeRootResponseTypeDef",
    ) -> "dc_td.AssumeRootResponse":
        return dc_td.AssumeRootResponse.make_one(res)

    def decode_authorization_message(
        self,
        res: "bs_td.DecodeAuthorizationMessageResponseTypeDef",
    ) -> "dc_td.DecodeAuthorizationMessageResponse":
        return dc_td.DecodeAuthorizationMessageResponse.make_one(res)

    def get_access_key_info(
        self,
        res: "bs_td.GetAccessKeyInfoResponseTypeDef",
    ) -> "dc_td.GetAccessKeyInfoResponse":
        return dc_td.GetAccessKeyInfoResponse.make_one(res)

    def get_caller_identity(
        self,
        res: "bs_td.GetCallerIdentityResponseTypeDef",
    ) -> "dc_td.GetCallerIdentityResponse":
        return dc_td.GetCallerIdentityResponse.make_one(res)

    def get_federation_token(
        self,
        res: "bs_td.GetFederationTokenResponseTypeDef",
    ) -> "dc_td.GetFederationTokenResponse":
        return dc_td.GetFederationTokenResponse.make_one(res)

    def get_session_token(
        self,
        res: "bs_td.GetSessionTokenResponseTypeDef",
    ) -> "dc_td.GetSessionTokenResponse":
        return dc_td.GetSessionTokenResponse.make_one(res)


sts_caster = STSCaster()
