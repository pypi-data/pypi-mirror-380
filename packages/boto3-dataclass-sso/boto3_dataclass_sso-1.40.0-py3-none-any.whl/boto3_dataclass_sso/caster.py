# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sso import type_defs as bs_td


class SSOCaster:

    def get_role_credentials(
        self,
        res: "bs_td.GetRoleCredentialsResponseTypeDef",
    ) -> "dc_td.GetRoleCredentialsResponse":
        return dc_td.GetRoleCredentialsResponse.make_one(res)

    def list_account_roles(
        self,
        res: "bs_td.ListAccountRolesResponseTypeDef",
    ) -> "dc_td.ListAccountRolesResponse":
        return dc_td.ListAccountRolesResponse.make_one(res)

    def list_accounts(
        self,
        res: "bs_td.ListAccountsResponseTypeDef",
    ) -> "dc_td.ListAccountsResponse":
        return dc_td.ListAccountsResponse.make_one(res)

    def logout(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


sso_caster = SSOCaster()
