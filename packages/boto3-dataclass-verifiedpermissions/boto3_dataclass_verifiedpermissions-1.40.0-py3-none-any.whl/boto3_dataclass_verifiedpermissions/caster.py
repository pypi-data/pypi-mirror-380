# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_verifiedpermissions import type_defs as bs_td


class VERIFIEDPERMISSIONSCaster:

    def batch_get_policy(
        self,
        res: "bs_td.BatchGetPolicyOutputTypeDef",
    ) -> "dc_td.BatchGetPolicyOutput":
        return dc_td.BatchGetPolicyOutput.make_one(res)

    def batch_is_authorized(
        self,
        res: "bs_td.BatchIsAuthorizedOutputTypeDef",
    ) -> "dc_td.BatchIsAuthorizedOutput":
        return dc_td.BatchIsAuthorizedOutput.make_one(res)

    def batch_is_authorized_with_token(
        self,
        res: "bs_td.BatchIsAuthorizedWithTokenOutputTypeDef",
    ) -> "dc_td.BatchIsAuthorizedWithTokenOutput":
        return dc_td.BatchIsAuthorizedWithTokenOutput.make_one(res)

    def create_identity_source(
        self,
        res: "bs_td.CreateIdentitySourceOutputTypeDef",
    ) -> "dc_td.CreateIdentitySourceOutput":
        return dc_td.CreateIdentitySourceOutput.make_one(res)

    def create_policy(
        self,
        res: "bs_td.CreatePolicyOutputTypeDef",
    ) -> "dc_td.CreatePolicyOutput":
        return dc_td.CreatePolicyOutput.make_one(res)

    def create_policy_store(
        self,
        res: "bs_td.CreatePolicyStoreOutputTypeDef",
    ) -> "dc_td.CreatePolicyStoreOutput":
        return dc_td.CreatePolicyStoreOutput.make_one(res)

    def create_policy_template(
        self,
        res: "bs_td.CreatePolicyTemplateOutputTypeDef",
    ) -> "dc_td.CreatePolicyTemplateOutput":
        return dc_td.CreatePolicyTemplateOutput.make_one(res)

    def get_identity_source(
        self,
        res: "bs_td.GetIdentitySourceOutputTypeDef",
    ) -> "dc_td.GetIdentitySourceOutput":
        return dc_td.GetIdentitySourceOutput.make_one(res)

    def get_policy(
        self,
        res: "bs_td.GetPolicyOutputTypeDef",
    ) -> "dc_td.GetPolicyOutput":
        return dc_td.GetPolicyOutput.make_one(res)

    def get_policy_store(
        self,
        res: "bs_td.GetPolicyStoreOutputTypeDef",
    ) -> "dc_td.GetPolicyStoreOutput":
        return dc_td.GetPolicyStoreOutput.make_one(res)

    def get_policy_template(
        self,
        res: "bs_td.GetPolicyTemplateOutputTypeDef",
    ) -> "dc_td.GetPolicyTemplateOutput":
        return dc_td.GetPolicyTemplateOutput.make_one(res)

    def get_schema(
        self,
        res: "bs_td.GetSchemaOutputTypeDef",
    ) -> "dc_td.GetSchemaOutput":
        return dc_td.GetSchemaOutput.make_one(res)

    def is_authorized(
        self,
        res: "bs_td.IsAuthorizedOutputTypeDef",
    ) -> "dc_td.IsAuthorizedOutput":
        return dc_td.IsAuthorizedOutput.make_one(res)

    def is_authorized_with_token(
        self,
        res: "bs_td.IsAuthorizedWithTokenOutputTypeDef",
    ) -> "dc_td.IsAuthorizedWithTokenOutput":
        return dc_td.IsAuthorizedWithTokenOutput.make_one(res)

    def list_identity_sources(
        self,
        res: "bs_td.ListIdentitySourcesOutputTypeDef",
    ) -> "dc_td.ListIdentitySourcesOutput":
        return dc_td.ListIdentitySourcesOutput.make_one(res)

    def list_policies(
        self,
        res: "bs_td.ListPoliciesOutputTypeDef",
    ) -> "dc_td.ListPoliciesOutput":
        return dc_td.ListPoliciesOutput.make_one(res)

    def list_policy_stores(
        self,
        res: "bs_td.ListPolicyStoresOutputTypeDef",
    ) -> "dc_td.ListPolicyStoresOutput":
        return dc_td.ListPolicyStoresOutput.make_one(res)

    def list_policy_templates(
        self,
        res: "bs_td.ListPolicyTemplatesOutputTypeDef",
    ) -> "dc_td.ListPolicyTemplatesOutput":
        return dc_td.ListPolicyTemplatesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def put_schema(
        self,
        res: "bs_td.PutSchemaOutputTypeDef",
    ) -> "dc_td.PutSchemaOutput":
        return dc_td.PutSchemaOutput.make_one(res)

    def update_identity_source(
        self,
        res: "bs_td.UpdateIdentitySourceOutputTypeDef",
    ) -> "dc_td.UpdateIdentitySourceOutput":
        return dc_td.UpdateIdentitySourceOutput.make_one(res)

    def update_policy(
        self,
        res: "bs_td.UpdatePolicyOutputTypeDef",
    ) -> "dc_td.UpdatePolicyOutput":
        return dc_td.UpdatePolicyOutput.make_one(res)

    def update_policy_store(
        self,
        res: "bs_td.UpdatePolicyStoreOutputTypeDef",
    ) -> "dc_td.UpdatePolicyStoreOutput":
        return dc_td.UpdatePolicyStoreOutput.make_one(res)

    def update_policy_template(
        self,
        res: "bs_td.UpdatePolicyTemplateOutputTypeDef",
    ) -> "dc_td.UpdatePolicyTemplateOutput":
        return dc_td.UpdatePolicyTemplateOutput.make_one(res)


verifiedpermissions_caster = VERIFIEDPERMISSIONSCaster()
