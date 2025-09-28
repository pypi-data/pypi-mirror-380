# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_sagemaker_geospatial import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class MultiPolygonGeometryInputOutput:
    boto3_raw_data: "type_defs.MultiPolygonGeometryInputOutputTypeDef" = (
        dataclasses.field()
    )

    Coordinates = field("Coordinates")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MultiPolygonGeometryInputOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiPolygonGeometryInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolygonGeometryInputOutput:
    boto3_raw_data: "type_defs.PolygonGeometryInputOutputTypeDef" = dataclasses.field()

    Coordinates = field("Coordinates")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolygonGeometryInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolygonGeometryInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetValue:
    boto3_raw_data: "type_defs.AssetValueTypeDef" = dataclasses.field()

    Href = field("Href")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudRemovalConfigInputOutput:
    boto3_raw_data: "type_defs.CloudRemovalConfigInputOutputTypeDef" = (
        dataclasses.field()
    )

    AlgorithmName = field("AlgorithmName")
    InterpolationValue = field("InterpolationValue")
    TargetBands = field("TargetBands")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudRemovalConfigInputOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudRemovalConfigInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudRemovalConfigInput:
    boto3_raw_data: "type_defs.CloudRemovalConfigInputTypeDef" = dataclasses.field()

    AlgorithmName = field("AlgorithmName")
    InterpolationValue = field("InterpolationValue")
    TargetBands = field("TargetBands")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudRemovalConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudRemovalConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Operation:
    boto3_raw_data: "type_defs.OperationTypeDef" = dataclasses.field()

    Equation = field("Equation")
    Name = field("Name")
    OutputType = field("OutputType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OperationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OperationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEarthObservationJobInput:
    boto3_raw_data: "type_defs.DeleteEarthObservationJobInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEarthObservationJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEarthObservationJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVectorEnrichmentJobInput:
    boto3_raw_data: "type_defs.DeleteVectorEnrichmentJobInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVectorEnrichmentJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVectorEnrichmentJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EarthObservationJobErrorDetails:
    boto3_raw_data: "type_defs.EarthObservationJobErrorDetailsTypeDef" = (
        dataclasses.field()
    )

    Message = field("Message")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EarthObservationJobErrorDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EarthObservationJobErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EoCloudCoverInput:
    boto3_raw_data: "type_defs.EoCloudCoverInputTypeDef" = dataclasses.field()

    LowerBound = field("LowerBound")
    UpperBound = field("UpperBound")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EoCloudCoverInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EoCloudCoverInputTypeDef"]
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
class ExportErrorDetailsOutput:
    boto3_raw_data: "type_defs.ExportErrorDetailsOutputTypeDef" = dataclasses.field()

    Message = field("Message")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportErrorDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportErrorDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportS3DataInput:
    boto3_raw_data: "type_defs.ExportS3DataInputTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportS3DataInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportS3DataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorEnrichmentJobS3Data:
    boto3_raw_data: "type_defs.VectorEnrichmentJobS3DataTypeDef" = dataclasses.field()

    S3Uri = field("S3Uri")
    KmsKeyId = field("KmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VectorEnrichmentJobS3DataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorEnrichmentJobS3DataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Maximum = field("Maximum")
    Minimum = field("Minimum")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoMosaicConfigInputOutput:
    boto3_raw_data: "type_defs.GeoMosaicConfigInputOutputTypeDef" = dataclasses.field()

    AlgorithmName = field("AlgorithmName")
    TargetBands = field("TargetBands")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeoMosaicConfigInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeoMosaicConfigInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoMosaicConfigInput:
    boto3_raw_data: "type_defs.GeoMosaicConfigInputTypeDef" = dataclasses.field()

    AlgorithmName = field("AlgorithmName")
    TargetBands = field("TargetBands")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeoMosaicConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeoMosaicConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Geometry:
    boto3_raw_data: "type_defs.GeometryTypeDef" = dataclasses.field()

    Coordinates = field("Coordinates")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeometryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeometryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEarthObservationJobInput:
    boto3_raw_data: "type_defs.GetEarthObservationJobInputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEarthObservationJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEarthObservationJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputBand:
    boto3_raw_data: "type_defs.OutputBandTypeDef" = dataclasses.field()

    BandName = field("BandName")
    OutputDataType = field("OutputDataType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputBandTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputBandTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRasterDataCollectionInput:
    boto3_raw_data: "type_defs.GetRasterDataCollectionInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRasterDataCollectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRasterDataCollectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTileInput:
    boto3_raw_data: "type_defs.GetTileInputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    ImageAssets = field("ImageAssets")
    Target = field("Target")
    x = field("x")
    y = field("y")
    z = field("z")
    ExecutionRoleArn = field("ExecutionRoleArn")
    ImageMask = field("ImageMask")
    OutputDataType = field("OutputDataType")
    OutputFormat = field("OutputFormat")
    PropertyFilters = field("PropertyFilters")
    TimeRangeFilter = field("TimeRangeFilter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTileInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTileInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVectorEnrichmentJobInput:
    boto3_raw_data: "type_defs.GetVectorEnrichmentJobInputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVectorEnrichmentJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVectorEnrichmentJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorEnrichmentJobErrorDetails:
    boto3_raw_data: "type_defs.VectorEnrichmentJobErrorDetailsTypeDef" = (
        dataclasses.field()
    )

    ErrorMessage = field("ErrorMessage")
    ErrorType = field("ErrorType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VectorEnrichmentJobErrorDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorEnrichmentJobErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorEnrichmentJobExportErrorDetails:
    boto3_raw_data: "type_defs.VectorEnrichmentJobExportErrorDetailsTypeDef" = (
        dataclasses.field()
    )

    Message = field("Message")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorEnrichmentJobExportErrorDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorEnrichmentJobExportErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Properties:
    boto3_raw_data: "type_defs.PropertiesTypeDef" = dataclasses.field()

    EoCloudCover = field("EoCloudCover")
    LandsatCloudCoverLand = field("LandsatCloudCoverLand")
    Platform = field("Platform")
    ViewOffNadir = field("ViewOffNadir")
    ViewSunAzimuth = field("ViewSunAzimuth")
    ViewSunElevation = field("ViewSunElevation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertiesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemporalStatisticsConfigInputOutput:
    boto3_raw_data: "type_defs.TemporalStatisticsConfigInputOutputTypeDef" = (
        dataclasses.field()
    )

    Statistics = field("Statistics")
    GroupBy = field("GroupBy")
    TargetBands = field("TargetBands")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TemporalStatisticsConfigInputOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemporalStatisticsConfigInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZonalStatisticsConfigInputOutput:
    boto3_raw_data: "type_defs.ZonalStatisticsConfigInputOutputTypeDef" = (
        dataclasses.field()
    )

    Statistics = field("Statistics")
    ZoneS3Path = field("ZoneS3Path")
    TargetBands = field("TargetBands")
    ZoneS3PathKmsKeyId = field("ZoneS3PathKmsKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ZonalStatisticsConfigInputOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZonalStatisticsConfigInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemporalStatisticsConfigInput:
    boto3_raw_data: "type_defs.TemporalStatisticsConfigInputTypeDef" = (
        dataclasses.field()
    )

    Statistics = field("Statistics")
    GroupBy = field("GroupBy")
    TargetBands = field("TargetBands")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TemporalStatisticsConfigInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemporalStatisticsConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZonalStatisticsConfigInput:
    boto3_raw_data: "type_defs.ZonalStatisticsConfigInputTypeDef" = dataclasses.field()

    Statistics = field("Statistics")
    ZoneS3Path = field("ZoneS3Path")
    TargetBands = field("TargetBands")
    ZoneS3PathKmsKeyId = field("ZoneS3PathKmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ZonalStatisticsConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZonalStatisticsConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LandsatCloudCoverLandInput:
    boto3_raw_data: "type_defs.LandsatCloudCoverLandInputTypeDef" = dataclasses.field()

    LowerBound = field("LowerBound")
    UpperBound = field("UpperBound")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LandsatCloudCoverLandInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LandsatCloudCoverLandInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEarthObservationJobInput:
    boto3_raw_data: "type_defs.ListEarthObservationJobInputTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SortBy = field("SortBy")
    SortOrder = field("SortOrder")
    StatusEquals = field("StatusEquals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEarthObservationJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEarthObservationJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEarthObservationJobOutputConfig:
    boto3_raw_data: "type_defs.ListEarthObservationJobOutputConfigTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    DurationInSeconds = field("DurationInSeconds")
    Name = field("Name")
    OperationType = field("OperationType")
    Status = field("Status")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEarthObservationJobOutputConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEarthObservationJobOutputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRasterDataCollectionsInput:
    boto3_raw_data: "type_defs.ListRasterDataCollectionsInputTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRasterDataCollectionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRasterDataCollectionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVectorEnrichmentJobInput:
    boto3_raw_data: "type_defs.ListVectorEnrichmentJobInputTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    SortBy = field("SortBy")
    SortOrder = field("SortOrder")
    StatusEquals = field("StatusEquals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVectorEnrichmentJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVectorEnrichmentJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVectorEnrichmentJobOutputConfig:
    boto3_raw_data: "type_defs.ListVectorEnrichmentJobOutputConfigTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    DurationInSeconds = field("DurationInSeconds")
    Name = field("Name")
    Status = field("Status")
    Type = field("Type")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVectorEnrichmentJobOutputConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVectorEnrichmentJobOutputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MapMatchingConfig:
    boto3_raw_data: "type_defs.MapMatchingConfigTypeDef" = dataclasses.field()

    IdAttributeName = field("IdAttributeName")
    TimestampAttributeName = field("TimestampAttributeName")
    XAttributeName = field("XAttributeName")
    YAttributeName = field("YAttributeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MapMatchingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MapMatchingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiPolygonGeometryInput:
    boto3_raw_data: "type_defs.MultiPolygonGeometryInputTypeDef" = dataclasses.field()

    Coordinates = field("Coordinates")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiPolygonGeometryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiPolygonGeometryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserDefined:
    boto3_raw_data: "type_defs.UserDefinedTypeDef" = dataclasses.field()

    Unit = field("Unit")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserDefinedTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserDefinedTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlatformInput:
    boto3_raw_data: "type_defs.PlatformInputTypeDef" = dataclasses.field()

    Value = field("Value")
    ComparisonOperator = field("ComparisonOperator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlatformInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlatformInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolygonGeometryInput:
    boto3_raw_data: "type_defs.PolygonGeometryInputTypeDef" = dataclasses.field()

    Coordinates = field("Coordinates")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolygonGeometryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolygonGeometryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewOffNadirInput:
    boto3_raw_data: "type_defs.ViewOffNadirInputTypeDef" = dataclasses.field()

    LowerBound = field("LowerBound")
    UpperBound = field("UpperBound")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ViewOffNadirInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViewOffNadirInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewSunAzimuthInput:
    boto3_raw_data: "type_defs.ViewSunAzimuthInputTypeDef" = dataclasses.field()

    LowerBound = field("LowerBound")
    UpperBound = field("UpperBound")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ViewSunAzimuthInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViewSunAzimuthInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ViewSunElevationInput:
    boto3_raw_data: "type_defs.ViewSunElevationInputTypeDef" = dataclasses.field()

    LowerBound = field("LowerBound")
    UpperBound = field("UpperBound")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ViewSunElevationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ViewSunElevationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeRangeFilterOutput:
    boto3_raw_data: "type_defs.TimeRangeFilterOutputTypeDef" = dataclasses.field()

    EndTime = field("EndTime")
    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeRangeFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeRangeFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReverseGeocodingConfig:
    boto3_raw_data: "type_defs.ReverseGeocodingConfigTypeDef" = dataclasses.field()

    XAttributeName = field("XAttributeName")
    YAttributeName = field("YAttributeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReverseGeocodingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReverseGeocodingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopEarthObservationJobInput:
    boto3_raw_data: "type_defs.StopEarthObservationJobInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopEarthObservationJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopEarthObservationJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopVectorEnrichmentJobInput:
    boto3_raw_data: "type_defs.StopVectorEnrichmentJobInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopVectorEnrichmentJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopVectorEnrichmentJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AreaOfInterestGeometryOutput:
    boto3_raw_data: "type_defs.AreaOfInterestGeometryOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MultiPolygonGeometry(self):  # pragma: no cover
        return MultiPolygonGeometryInputOutput.make_one(
            self.boto3_raw_data["MultiPolygonGeometry"]
        )

    @cached_property
    def PolygonGeometry(self):  # pragma: no cover
        return PolygonGeometryInputOutput.make_one(
            self.boto3_raw_data["PolygonGeometry"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AreaOfInterestGeometryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AreaOfInterestGeometryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomIndicesInputOutput:
    boto3_raw_data: "type_defs.CustomIndicesInputOutputTypeDef" = dataclasses.field()

    @cached_property
    def Operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["Operations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomIndicesInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomIndicesInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomIndicesInput:
    boto3_raw_data: "type_defs.CustomIndicesInputTypeDef" = dataclasses.field()

    @cached_property
    def Operations(self):  # pragma: no cover
        return Operation.make_many(self.boto3_raw_data["Operations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomIndicesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomIndicesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTileOutput:
    boto3_raw_data: "type_defs.GetTileOutputTypeDef" = dataclasses.field()

    BinaryFile = field("BinaryFile")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTileOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTileOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportErrorDetails:
    boto3_raw_data: "type_defs.ExportErrorDetailsTypeDef" = dataclasses.field()

    @cached_property
    def ExportResults(self):  # pragma: no cover
        return ExportErrorDetailsOutput.make_one(self.boto3_raw_data["ExportResults"])

    @cached_property
    def ExportSourceImages(self):  # pragma: no cover
        return ExportErrorDetailsOutput.make_one(
            self.boto3_raw_data["ExportSourceImages"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportErrorDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputConfigInput:
    boto3_raw_data: "type_defs.OutputConfigInputTypeDef" = dataclasses.field()

    @cached_property
    def S3Data(self):  # pragma: no cover
        return ExportS3DataInput.make_one(self.boto3_raw_data["S3Data"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputConfigInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportVectorEnrichmentJobOutputConfig:
    boto3_raw_data: "type_defs.ExportVectorEnrichmentJobOutputConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Data(self):  # pragma: no cover
        return VectorEnrichmentJobS3Data.make_one(self.boto3_raw_data["S3Data"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportVectorEnrichmentJobOutputConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportVectorEnrichmentJobOutputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorEnrichmentJobDataSourceConfigInput:
    boto3_raw_data: "type_defs.VectorEnrichmentJobDataSourceConfigInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def S3Data(self):  # pragma: no cover
        return VectorEnrichmentJobS3Data.make_one(self.boto3_raw_data["S3Data"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorEnrichmentJobDataSourceConfigInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorEnrichmentJobDataSourceConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRasterDataCollectionOutput:
    boto3_raw_data: "type_defs.GetRasterDataCollectionOutputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Description = field("Description")
    DescriptionPageUrl = field("DescriptionPageUrl")
    ImageSourceBands = field("ImageSourceBands")
    Name = field("Name")

    @cached_property
    def SupportedFilters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["SupportedFilters"])

    Tags = field("Tags")
    Type = field("Type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRasterDataCollectionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRasterDataCollectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RasterDataCollectionMetadata:
    boto3_raw_data: "type_defs.RasterDataCollectionMetadataTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Description = field("Description")
    Name = field("Name")

    @cached_property
    def SupportedFilters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["SupportedFilters"])

    Type = field("Type")
    DescriptionPageUrl = field("DescriptionPageUrl")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RasterDataCollectionMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RasterDataCollectionMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ItemSource:
    boto3_raw_data: "type_defs.ItemSourceTypeDef" = dataclasses.field()

    DateTime = field("DateTime")

    @cached_property
    def Geometry(self):  # pragma: no cover
        return Geometry.make_one(self.boto3_raw_data["Geometry"])

    Id = field("Id")
    Assets = field("Assets")

    @cached_property
    def Properties(self):  # pragma: no cover
        return Properties.make_one(self.boto3_raw_data["Properties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ItemSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ItemSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEarthObservationJobInputPaginate:
    boto3_raw_data: "type_defs.ListEarthObservationJobInputPaginateTypeDef" = (
        dataclasses.field()
    )

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")
    StatusEquals = field("StatusEquals")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEarthObservationJobInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEarthObservationJobInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRasterDataCollectionsInputPaginate:
    boto3_raw_data: "type_defs.ListRasterDataCollectionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRasterDataCollectionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRasterDataCollectionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVectorEnrichmentJobInputPaginate:
    boto3_raw_data: "type_defs.ListVectorEnrichmentJobInputPaginateTypeDef" = (
        dataclasses.field()
    )

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")
    StatusEquals = field("StatusEquals")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVectorEnrichmentJobInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVectorEnrichmentJobInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEarthObservationJobOutput:
    boto3_raw_data: "type_defs.ListEarthObservationJobOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EarthObservationJobSummaries(self):  # pragma: no cover
        return ListEarthObservationJobOutputConfig.make_many(
            self.boto3_raw_data["EarthObservationJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEarthObservationJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEarthObservationJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVectorEnrichmentJobOutput:
    boto3_raw_data: "type_defs.ListVectorEnrichmentJobOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VectorEnrichmentJobSummaries(self):  # pragma: no cover
        return ListVectorEnrichmentJobOutputConfig.make_many(
            self.boto3_raw_data["VectorEnrichmentJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVectorEnrichmentJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVectorEnrichmentJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputResolutionResamplingInput:
    boto3_raw_data: "type_defs.OutputResolutionResamplingInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UserDefined(self):  # pragma: no cover
        return UserDefined.make_one(self.boto3_raw_data["UserDefined"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OutputResolutionResamplingInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputResolutionResamplingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputResolutionStackInput:
    boto3_raw_data: "type_defs.OutputResolutionStackInputTypeDef" = dataclasses.field()

    Predefined = field("Predefined")

    @cached_property
    def UserDefined(self):  # pragma: no cover
        return UserDefined.make_one(self.boto3_raw_data["UserDefined"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputResolutionStackInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputResolutionStackInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Property:
    boto3_raw_data: "type_defs.PropertyTypeDef" = dataclasses.field()

    @cached_property
    def EoCloudCover(self):  # pragma: no cover
        return EoCloudCoverInput.make_one(self.boto3_raw_data["EoCloudCover"])

    @cached_property
    def LandsatCloudCoverLand(self):  # pragma: no cover
        return LandsatCloudCoverLandInput.make_one(
            self.boto3_raw_data["LandsatCloudCoverLand"]
        )

    @cached_property
    def Platform(self):  # pragma: no cover
        return PlatformInput.make_one(self.boto3_raw_data["Platform"])

    @cached_property
    def ViewOffNadir(self):  # pragma: no cover
        return ViewOffNadirInput.make_one(self.boto3_raw_data["ViewOffNadir"])

    @cached_property
    def ViewSunAzimuth(self):  # pragma: no cover
        return ViewSunAzimuthInput.make_one(self.boto3_raw_data["ViewSunAzimuth"])

    @cached_property
    def ViewSunElevation(self):  # pragma: no cover
        return ViewSunElevationInput.make_one(self.boto3_raw_data["ViewSunElevation"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorEnrichmentJobConfig:
    boto3_raw_data: "type_defs.VectorEnrichmentJobConfigTypeDef" = dataclasses.field()

    @cached_property
    def MapMatchingConfig(self):  # pragma: no cover
        return MapMatchingConfig.make_one(self.boto3_raw_data["MapMatchingConfig"])

    @cached_property
    def ReverseGeocodingConfig(self):  # pragma: no cover
        return ReverseGeocodingConfig.make_one(
            self.boto3_raw_data["ReverseGeocodingConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VectorEnrichmentJobConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorEnrichmentJobConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeRangeFilterInput:
    boto3_raw_data: "type_defs.TimeRangeFilterInputTypeDef" = dataclasses.field()

    EndTime = field("EndTime")
    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeRangeFilterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeRangeFilterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AreaOfInterestOutput:
    boto3_raw_data: "type_defs.AreaOfInterestOutputTypeDef" = dataclasses.field()

    @cached_property
    def AreaOfInterestGeometry(self):  # pragma: no cover
        return AreaOfInterestGeometryOutput.make_one(
            self.boto3_raw_data["AreaOfInterestGeometry"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AreaOfInterestOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AreaOfInterestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BandMathConfigInputOutput:
    boto3_raw_data: "type_defs.BandMathConfigInputOutputTypeDef" = dataclasses.field()

    @cached_property
    def CustomIndices(self):  # pragma: no cover
        return CustomIndicesInputOutput.make_one(self.boto3_raw_data["CustomIndices"])

    PredefinedIndices = field("PredefinedIndices")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BandMathConfigInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BandMathConfigInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BandMathConfigInput:
    boto3_raw_data: "type_defs.BandMathConfigInputTypeDef" = dataclasses.field()

    @cached_property
    def CustomIndices(self):  # pragma: no cover
        return CustomIndicesInput.make_one(self.boto3_raw_data["CustomIndices"])

    PredefinedIndices = field("PredefinedIndices")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BandMathConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BandMathConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportEarthObservationJobInput:
    boto3_raw_data: "type_defs.ExportEarthObservationJobInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return OutputConfigInput.make_one(self.boto3_raw_data["OutputConfig"])

    ClientToken = field("ClientToken")
    ExportSourceImages = field("ExportSourceImages")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportEarthObservationJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportEarthObservationJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportEarthObservationJobOutput:
    boto3_raw_data: "type_defs.ExportEarthObservationJobOutputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    ExecutionRoleArn = field("ExecutionRoleArn")
    ExportSourceImages = field("ExportSourceImages")
    ExportStatus = field("ExportStatus")

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return OutputConfigInput.make_one(self.boto3_raw_data["OutputConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportEarthObservationJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportEarthObservationJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportVectorEnrichmentJobInput:
    boto3_raw_data: "type_defs.ExportVectorEnrichmentJobInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return ExportVectorEnrichmentJobOutputConfig.make_one(
            self.boto3_raw_data["OutputConfig"]
        )

    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportVectorEnrichmentJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportVectorEnrichmentJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportVectorEnrichmentJobOutput:
    boto3_raw_data: "type_defs.ExportVectorEnrichmentJobOutputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    ExecutionRoleArn = field("ExecutionRoleArn")
    ExportStatus = field("ExportStatus")

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return ExportVectorEnrichmentJobOutputConfig.make_one(
            self.boto3_raw_data["OutputConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportVectorEnrichmentJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportVectorEnrichmentJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorEnrichmentJobInputConfig:
    boto3_raw_data: "type_defs.VectorEnrichmentJobInputConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DataSourceConfig(self):  # pragma: no cover
        return VectorEnrichmentJobDataSourceConfigInput.make_one(
            self.boto3_raw_data["DataSourceConfig"]
        )

    DocumentType = field("DocumentType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VectorEnrichmentJobInputConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorEnrichmentJobInputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRasterDataCollectionsOutput:
    boto3_raw_data: "type_defs.ListRasterDataCollectionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RasterDataCollectionSummaries(self):  # pragma: no cover
        return RasterDataCollectionMetadata.make_many(
            self.boto3_raw_data["RasterDataCollectionSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRasterDataCollectionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRasterDataCollectionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRasterDataCollectionOutput:
    boto3_raw_data: "type_defs.SearchRasterDataCollectionOutputTypeDef" = (
        dataclasses.field()
    )

    ApproximateResultCount = field("ApproximateResultCount")

    @cached_property
    def Items(self):  # pragma: no cover
        return ItemSource.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchRasterDataCollectionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRasterDataCollectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResamplingConfigInputOutput:
    boto3_raw_data: "type_defs.ResamplingConfigInputOutputTypeDef" = dataclasses.field()

    @cached_property
    def OutputResolution(self):  # pragma: no cover
        return OutputResolutionResamplingInput.make_one(
            self.boto3_raw_data["OutputResolution"]
        )

    AlgorithmName = field("AlgorithmName")
    TargetBands = field("TargetBands")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResamplingConfigInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResamplingConfigInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResamplingConfigInput:
    boto3_raw_data: "type_defs.ResamplingConfigInputTypeDef" = dataclasses.field()

    @cached_property
    def OutputResolution(self):  # pragma: no cover
        return OutputResolutionResamplingInput.make_one(
            self.boto3_raw_data["OutputResolution"]
        )

    AlgorithmName = field("AlgorithmName")
    TargetBands = field("TargetBands")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResamplingConfigInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResamplingConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackConfigInputOutput:
    boto3_raw_data: "type_defs.StackConfigInputOutputTypeDef" = dataclasses.field()

    @cached_property
    def OutputResolution(self):  # pragma: no cover
        return OutputResolutionStackInput.make_one(
            self.boto3_raw_data["OutputResolution"]
        )

    TargetBands = field("TargetBands")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackConfigInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackConfigInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackConfigInput:
    boto3_raw_data: "type_defs.StackConfigInputTypeDef" = dataclasses.field()

    @cached_property
    def OutputResolution(self):  # pragma: no cover
        return OutputResolutionStackInput.make_one(
            self.boto3_raw_data["OutputResolution"]
        )

    TargetBands = field("TargetBands")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackConfigInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AreaOfInterestGeometry:
    boto3_raw_data: "type_defs.AreaOfInterestGeometryTypeDef" = dataclasses.field()

    MultiPolygonGeometry = field("MultiPolygonGeometry")
    PolygonGeometry = field("PolygonGeometry")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AreaOfInterestGeometryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AreaOfInterestGeometryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyFilter:
    boto3_raw_data: "type_defs.PropertyFilterTypeDef" = dataclasses.field()

    @cached_property
    def Property(self):  # pragma: no cover
        return Property.make_one(self.boto3_raw_data["Property"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertyFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertyFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVectorEnrichmentJobOutput:
    boto3_raw_data: "type_defs.GetVectorEnrichmentJobOutputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    DurationInSeconds = field("DurationInSeconds")

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return VectorEnrichmentJobErrorDetails.make_one(
            self.boto3_raw_data["ErrorDetails"]
        )

    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def ExportErrorDetails(self):  # pragma: no cover
        return VectorEnrichmentJobExportErrorDetails.make_one(
            self.boto3_raw_data["ExportErrorDetails"]
        )

    ExportStatus = field("ExportStatus")

    @cached_property
    def InputConfig(self):  # pragma: no cover
        return VectorEnrichmentJobInputConfig.make_one(
            self.boto3_raw_data["InputConfig"]
        )

    @cached_property
    def JobConfig(self):  # pragma: no cover
        return VectorEnrichmentJobConfig.make_one(self.boto3_raw_data["JobConfig"])

    KmsKeyId = field("KmsKeyId")
    Name = field("Name")
    Status = field("Status")
    Tags = field("Tags")
    Type = field("Type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVectorEnrichmentJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVectorEnrichmentJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartVectorEnrichmentJobInput:
    boto3_raw_data: "type_defs.StartVectorEnrichmentJobInputTypeDef" = (
        dataclasses.field()
    )

    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def InputConfig(self):  # pragma: no cover
        return VectorEnrichmentJobInputConfig.make_one(
            self.boto3_raw_data["InputConfig"]
        )

    @cached_property
    def JobConfig(self):  # pragma: no cover
        return VectorEnrichmentJobConfig.make_one(self.boto3_raw_data["JobConfig"])

    Name = field("Name")
    ClientToken = field("ClientToken")
    KmsKeyId = field("KmsKeyId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartVectorEnrichmentJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartVectorEnrichmentJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartVectorEnrichmentJobOutput:
    boto3_raw_data: "type_defs.StartVectorEnrichmentJobOutputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    DurationInSeconds = field("DurationInSeconds")
    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def InputConfig(self):  # pragma: no cover
        return VectorEnrichmentJobInputConfig.make_one(
            self.boto3_raw_data["InputConfig"]
        )

    @cached_property
    def JobConfig(self):  # pragma: no cover
        return VectorEnrichmentJobConfig.make_one(self.boto3_raw_data["JobConfig"])

    KmsKeyId = field("KmsKeyId")
    Name = field("Name")
    Status = field("Status")
    Tags = field("Tags")
    Type = field("Type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartVectorEnrichmentJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartVectorEnrichmentJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobConfigInputOutput:
    boto3_raw_data: "type_defs.JobConfigInputOutputTypeDef" = dataclasses.field()

    @cached_property
    def BandMathConfig(self):  # pragma: no cover
        return BandMathConfigInputOutput.make_one(self.boto3_raw_data["BandMathConfig"])

    CloudMaskingConfig = field("CloudMaskingConfig")

    @cached_property
    def CloudRemovalConfig(self):  # pragma: no cover
        return CloudRemovalConfigInputOutput.make_one(
            self.boto3_raw_data["CloudRemovalConfig"]
        )

    @cached_property
    def GeoMosaicConfig(self):  # pragma: no cover
        return GeoMosaicConfigInputOutput.make_one(
            self.boto3_raw_data["GeoMosaicConfig"]
        )

    LandCoverSegmentationConfig = field("LandCoverSegmentationConfig")

    @cached_property
    def ResamplingConfig(self):  # pragma: no cover
        return ResamplingConfigInputOutput.make_one(
            self.boto3_raw_data["ResamplingConfig"]
        )

    @cached_property
    def StackConfig(self):  # pragma: no cover
        return StackConfigInputOutput.make_one(self.boto3_raw_data["StackConfig"])

    @cached_property
    def TemporalStatisticsConfig(self):  # pragma: no cover
        return TemporalStatisticsConfigInputOutput.make_one(
            self.boto3_raw_data["TemporalStatisticsConfig"]
        )

    @cached_property
    def ZonalStatisticsConfig(self):  # pragma: no cover
        return ZonalStatisticsConfigInputOutput.make_one(
            self.boto3_raw_data["ZonalStatisticsConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobConfigInputOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobConfigInputOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobConfigInput:
    boto3_raw_data: "type_defs.JobConfigInputTypeDef" = dataclasses.field()

    @cached_property
    def BandMathConfig(self):  # pragma: no cover
        return BandMathConfigInput.make_one(self.boto3_raw_data["BandMathConfig"])

    CloudMaskingConfig = field("CloudMaskingConfig")

    @cached_property
    def CloudRemovalConfig(self):  # pragma: no cover
        return CloudRemovalConfigInput.make_one(
            self.boto3_raw_data["CloudRemovalConfig"]
        )

    @cached_property
    def GeoMosaicConfig(self):  # pragma: no cover
        return GeoMosaicConfigInput.make_one(self.boto3_raw_data["GeoMosaicConfig"])

    LandCoverSegmentationConfig = field("LandCoverSegmentationConfig")

    @cached_property
    def ResamplingConfig(self):  # pragma: no cover
        return ResamplingConfigInput.make_one(self.boto3_raw_data["ResamplingConfig"])

    @cached_property
    def StackConfig(self):  # pragma: no cover
        return StackConfigInput.make_one(self.boto3_raw_data["StackConfig"])

    @cached_property
    def TemporalStatisticsConfig(self):  # pragma: no cover
        return TemporalStatisticsConfigInput.make_one(
            self.boto3_raw_data["TemporalStatisticsConfig"]
        )

    @cached_property
    def ZonalStatisticsConfig(self):  # pragma: no cover
        return ZonalStatisticsConfigInput.make_one(
            self.boto3_raw_data["ZonalStatisticsConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobConfigInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobConfigInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyFiltersOutput:
    boto3_raw_data: "type_defs.PropertyFiltersOutputTypeDef" = dataclasses.field()

    LogicalOperator = field("LogicalOperator")

    @cached_property
    def Properties(self):  # pragma: no cover
        return PropertyFilter.make_many(self.boto3_raw_data["Properties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyFiltersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyFiltersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyFilters:
    boto3_raw_data: "type_defs.PropertyFiltersTypeDef" = dataclasses.field()

    LogicalOperator = field("LogicalOperator")

    @cached_property
    def Properties(self):  # pragma: no cover
        return PropertyFilter.make_many(self.boto3_raw_data["Properties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PropertyFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PropertyFiltersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AreaOfInterest:
    boto3_raw_data: "type_defs.AreaOfInterestTypeDef" = dataclasses.field()

    AreaOfInterestGeometry = field("AreaOfInterestGeometry")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AreaOfInterestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AreaOfInterestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RasterDataCollectionQueryOutput:
    boto3_raw_data: "type_defs.RasterDataCollectionQueryOutputTypeDef" = (
        dataclasses.field()
    )

    RasterDataCollectionArn = field("RasterDataCollectionArn")
    RasterDataCollectionName = field("RasterDataCollectionName")

    @cached_property
    def TimeRangeFilter(self):  # pragma: no cover
        return TimeRangeFilterOutput.make_one(self.boto3_raw_data["TimeRangeFilter"])

    @cached_property
    def AreaOfInterest(self):  # pragma: no cover
        return AreaOfInterestOutput.make_one(self.boto3_raw_data["AreaOfInterest"])

    @cached_property
    def PropertyFilters(self):  # pragma: no cover
        return PropertyFiltersOutput.make_one(self.boto3_raw_data["PropertyFilters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RasterDataCollectionQueryOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RasterDataCollectionQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputConfigOutput:
    boto3_raw_data: "type_defs.InputConfigOutputTypeDef" = dataclasses.field()

    PreviousEarthObservationJobArn = field("PreviousEarthObservationJobArn")

    @cached_property
    def RasterDataCollectionQuery(self):  # pragma: no cover
        return RasterDataCollectionQueryOutput.make_one(
            self.boto3_raw_data["RasterDataCollectionQuery"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RasterDataCollectionQueryInput:
    boto3_raw_data: "type_defs.RasterDataCollectionQueryInputTypeDef" = (
        dataclasses.field()
    )

    RasterDataCollectionArn = field("RasterDataCollectionArn")

    @cached_property
    def TimeRangeFilter(self):  # pragma: no cover
        return TimeRangeFilterInput.make_one(self.boto3_raw_data["TimeRangeFilter"])

    AreaOfInterest = field("AreaOfInterest")
    PropertyFilters = field("PropertyFilters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RasterDataCollectionQueryInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RasterDataCollectionQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RasterDataCollectionQueryWithBandFilterInput:
    boto3_raw_data: "type_defs.RasterDataCollectionQueryWithBandFilterInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TimeRangeFilter(self):  # pragma: no cover
        return TimeRangeFilterInput.make_one(self.boto3_raw_data["TimeRangeFilter"])

    AreaOfInterest = field("AreaOfInterest")
    BandFilter = field("BandFilter")
    PropertyFilters = field("PropertyFilters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RasterDataCollectionQueryWithBandFilterInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RasterDataCollectionQueryWithBandFilterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEarthObservationJobOutput:
    boto3_raw_data: "type_defs.GetEarthObservationJobOutputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    DurationInSeconds = field("DurationInSeconds")

    @cached_property
    def ErrorDetails(self):  # pragma: no cover
        return EarthObservationJobErrorDetails.make_one(
            self.boto3_raw_data["ErrorDetails"]
        )

    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def ExportErrorDetails(self):  # pragma: no cover
        return ExportErrorDetails.make_one(self.boto3_raw_data["ExportErrorDetails"])

    ExportStatus = field("ExportStatus")

    @cached_property
    def InputConfig(self):  # pragma: no cover
        return InputConfigOutput.make_one(self.boto3_raw_data["InputConfig"])

    @cached_property
    def JobConfig(self):  # pragma: no cover
        return JobConfigInputOutput.make_one(self.boto3_raw_data["JobConfig"])

    KmsKeyId = field("KmsKeyId")
    Name = field("Name")

    @cached_property
    def OutputBands(self):  # pragma: no cover
        return OutputBand.make_many(self.boto3_raw_data["OutputBands"])

    Status = field("Status")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEarthObservationJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEarthObservationJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEarthObservationJobOutput:
    boto3_raw_data: "type_defs.StartEarthObservationJobOutputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    CreationTime = field("CreationTime")
    DurationInSeconds = field("DurationInSeconds")
    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def InputConfig(self):  # pragma: no cover
        return InputConfigOutput.make_one(self.boto3_raw_data["InputConfig"])

    @cached_property
    def JobConfig(self):  # pragma: no cover
        return JobConfigInputOutput.make_one(self.boto3_raw_data["JobConfig"])

    KmsKeyId = field("KmsKeyId")
    Name = field("Name")
    Status = field("Status")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartEarthObservationJobOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEarthObservationJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputConfigInput:
    boto3_raw_data: "type_defs.InputConfigInputTypeDef" = dataclasses.field()

    PreviousEarthObservationJobArn = field("PreviousEarthObservationJobArn")

    @cached_property
    def RasterDataCollectionQuery(self):  # pragma: no cover
        return RasterDataCollectionQueryInput.make_one(
            self.boto3_raw_data["RasterDataCollectionQuery"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputConfigInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputConfigInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRasterDataCollectionInput:
    boto3_raw_data: "type_defs.SearchRasterDataCollectionInputTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")

    @cached_property
    def RasterDataCollectionQuery(self):  # pragma: no cover
        return RasterDataCollectionQueryWithBandFilterInput.make_one(
            self.boto3_raw_data["RasterDataCollectionQuery"]
        )

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchRasterDataCollectionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRasterDataCollectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEarthObservationJobInput:
    boto3_raw_data: "type_defs.StartEarthObservationJobInputTypeDef" = (
        dataclasses.field()
    )

    ExecutionRoleArn = field("ExecutionRoleArn")

    @cached_property
    def InputConfig(self):  # pragma: no cover
        return InputConfigInput.make_one(self.boto3_raw_data["InputConfig"])

    JobConfig = field("JobConfig")
    Name = field("Name")
    ClientToken = field("ClientToken")
    KmsKeyId = field("KmsKeyId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartEarthObservationJobInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEarthObservationJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
