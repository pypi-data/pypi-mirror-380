# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_marketplace_agreement import type_defs as bs_td


class MARKETPLACE_AGREEMENTCaster:

    def describe_agreement(
        self,
        res: "bs_td.DescribeAgreementOutputTypeDef",
    ) -> "dc_td.DescribeAgreementOutput":
        return dc_td.DescribeAgreementOutput.make_one(res)

    def get_agreement_terms(
        self,
        res: "bs_td.GetAgreementTermsOutputTypeDef",
    ) -> "dc_td.GetAgreementTermsOutput":
        return dc_td.GetAgreementTermsOutput.make_one(res)

    def search_agreements(
        self,
        res: "bs_td.SearchAgreementsOutputTypeDef",
    ) -> "dc_td.SearchAgreementsOutput":
        return dc_td.SearchAgreementsOutput.make_one(res)


marketplace_agreement_caster = MARKETPLACE_AGREEMENTCaster()
