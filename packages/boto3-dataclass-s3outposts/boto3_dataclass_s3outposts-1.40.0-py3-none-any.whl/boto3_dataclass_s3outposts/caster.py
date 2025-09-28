# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_s3outposts import type_defs as bs_td


class S3OUTPOSTSCaster:

    def create_endpoint(
        self,
        res: "bs_td.CreateEndpointResultTypeDef",
    ) -> "dc_td.CreateEndpointResult":
        return dc_td.CreateEndpointResult.make_one(res)

    def delete_endpoint(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def list_endpoints(
        self,
        res: "bs_td.ListEndpointsResultTypeDef",
    ) -> "dc_td.ListEndpointsResult":
        return dc_td.ListEndpointsResult.make_one(res)

    def list_outposts_with_s3(
        self,
        res: "bs_td.ListOutpostsWithS3ResultTypeDef",
    ) -> "dc_td.ListOutpostsWithS3Result":
        return dc_td.ListOutpostsWithS3Result.make_one(res)

    def list_shared_endpoints(
        self,
        res: "bs_td.ListSharedEndpointsResultTypeDef",
    ) -> "dc_td.ListSharedEndpointsResult":
        return dc_td.ListSharedEndpointsResult.make_one(res)


s3outposts_caster = S3OUTPOSTSCaster()
