# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sagemaker_geospatial import type_defs as bs_td


class SAGEMAKER_GEOSPATIALCaster:

    def export_earth_observation_job(
        self,
        res: "bs_td.ExportEarthObservationJobOutputTypeDef",
    ) -> "dc_td.ExportEarthObservationJobOutput":
        return dc_td.ExportEarthObservationJobOutput.make_one(res)

    def export_vector_enrichment_job(
        self,
        res: "bs_td.ExportVectorEnrichmentJobOutputTypeDef",
    ) -> "dc_td.ExportVectorEnrichmentJobOutput":
        return dc_td.ExportVectorEnrichmentJobOutput.make_one(res)

    def get_earth_observation_job(
        self,
        res: "bs_td.GetEarthObservationJobOutputTypeDef",
    ) -> "dc_td.GetEarthObservationJobOutput":
        return dc_td.GetEarthObservationJobOutput.make_one(res)

    def get_raster_data_collection(
        self,
        res: "bs_td.GetRasterDataCollectionOutputTypeDef",
    ) -> "dc_td.GetRasterDataCollectionOutput":
        return dc_td.GetRasterDataCollectionOutput.make_one(res)

    def get_tile(
        self,
        res: "bs_td.GetTileOutputTypeDef",
    ) -> "dc_td.GetTileOutput":
        return dc_td.GetTileOutput.make_one(res)

    def get_vector_enrichment_job(
        self,
        res: "bs_td.GetVectorEnrichmentJobOutputTypeDef",
    ) -> "dc_td.GetVectorEnrichmentJobOutput":
        return dc_td.GetVectorEnrichmentJobOutput.make_one(res)

    def list_earth_observation_jobs(
        self,
        res: "bs_td.ListEarthObservationJobOutputTypeDef",
    ) -> "dc_td.ListEarthObservationJobOutput":
        return dc_td.ListEarthObservationJobOutput.make_one(res)

    def list_raster_data_collections(
        self,
        res: "bs_td.ListRasterDataCollectionsOutputTypeDef",
    ) -> "dc_td.ListRasterDataCollectionsOutput":
        return dc_td.ListRasterDataCollectionsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_vector_enrichment_jobs(
        self,
        res: "bs_td.ListVectorEnrichmentJobOutputTypeDef",
    ) -> "dc_td.ListVectorEnrichmentJobOutput":
        return dc_td.ListVectorEnrichmentJobOutput.make_one(res)

    def search_raster_data_collection(
        self,
        res: "bs_td.SearchRasterDataCollectionOutputTypeDef",
    ) -> "dc_td.SearchRasterDataCollectionOutput":
        return dc_td.SearchRasterDataCollectionOutput.make_one(res)

    def start_earth_observation_job(
        self,
        res: "bs_td.StartEarthObservationJobOutputTypeDef",
    ) -> "dc_td.StartEarthObservationJobOutput":
        return dc_td.StartEarthObservationJobOutput.make_one(res)

    def start_vector_enrichment_job(
        self,
        res: "bs_td.StartVectorEnrichmentJobOutputTypeDef",
    ) -> "dc_td.StartVectorEnrichmentJobOutput":
        return dc_td.StartVectorEnrichmentJobOutput.make_one(res)


sagemaker_geospatial_caster = SAGEMAKER_GEOSPATIALCaster()
