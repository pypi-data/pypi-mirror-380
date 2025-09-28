# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sdb import type_defs as bs_td


class SDBCaster:

    def batch_delete_attributes(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def batch_put_attributes(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_domain(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_attributes(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_domain(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def domain_metadata(
        self,
        res: "bs_td.DomainMetadataResultTypeDef",
    ) -> "dc_td.DomainMetadataResult":
        return dc_td.DomainMetadataResult.make_one(res)

    def get_attributes(
        self,
        res: "bs_td.GetAttributesResultTypeDef",
    ) -> "dc_td.GetAttributesResult":
        return dc_td.GetAttributesResult.make_one(res)

    def list_domains(
        self,
        res: "bs_td.ListDomainsResultTypeDef",
    ) -> "dc_td.ListDomainsResult":
        return dc_td.ListDomainsResult.make_one(res)

    def put_attributes(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def select(
        self,
        res: "bs_td.SelectResultTypeDef",
    ) -> "dc_td.SelectResult":
        return dc_td.SelectResult.make_one(res)


sdb_caster = SDBCaster()
