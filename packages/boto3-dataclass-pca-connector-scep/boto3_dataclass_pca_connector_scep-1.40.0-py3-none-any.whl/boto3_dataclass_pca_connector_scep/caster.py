# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pca_connector_scep import type_defs as bs_td


class PCA_CONNECTOR_SCEPCaster:

    def create_challenge(
        self,
        res: "bs_td.CreateChallengeResponseTypeDef",
    ) -> "dc_td.CreateChallengeResponse":
        return dc_td.CreateChallengeResponse.make_one(res)

    def create_connector(
        self,
        res: "bs_td.CreateConnectorResponseTypeDef",
    ) -> "dc_td.CreateConnectorResponse":
        return dc_td.CreateConnectorResponse.make_one(res)

    def delete_challenge(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_connector(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_challenge_metadata(
        self,
        res: "bs_td.GetChallengeMetadataResponseTypeDef",
    ) -> "dc_td.GetChallengeMetadataResponse":
        return dc_td.GetChallengeMetadataResponse.make_one(res)

    def get_challenge_password(
        self,
        res: "bs_td.GetChallengePasswordResponseTypeDef",
    ) -> "dc_td.GetChallengePasswordResponse":
        return dc_td.GetChallengePasswordResponse.make_one(res)

    def get_connector(
        self,
        res: "bs_td.GetConnectorResponseTypeDef",
    ) -> "dc_td.GetConnectorResponse":
        return dc_td.GetConnectorResponse.make_one(res)

    def list_challenge_metadata(
        self,
        res: "bs_td.ListChallengeMetadataResponseTypeDef",
    ) -> "dc_td.ListChallengeMetadataResponse":
        return dc_td.ListChallengeMetadataResponse.make_one(res)

    def list_connectors(
        self,
        res: "bs_td.ListConnectorsResponseTypeDef",
    ) -> "dc_td.ListConnectorsResponse":
        return dc_td.ListConnectorsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


pca_connector_scep_caster = PCA_CONNECTOR_SCEPCaster()
