# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_geo_maps import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class GetGlyphsRequest:
    boto3_raw_data: "type_defs.GetGlyphsRequestTypeDef" = dataclasses.field()

    FontStack = field("FontStack")
    FontUnicodeRange = field("FontUnicodeRange")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGlyphsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGlyphsRequestTypeDef"]
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
class GetSpritesRequest:
    boto3_raw_data: "type_defs.GetSpritesRequestTypeDef" = dataclasses.field()

    FileName = field("FileName")
    Style = field("Style")
    ColorScheme = field("ColorScheme")
    Variant = field("Variant")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSpritesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSpritesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStaticMapRequest:
    boto3_raw_data: "type_defs.GetStaticMapRequestTypeDef" = dataclasses.field()

    Height = field("Height")
    FileName = field("FileName")
    Width = field("Width")
    BoundingBox = field("BoundingBox")
    BoundedPositions = field("BoundedPositions")
    Center = field("Center")
    ColorScheme = field("ColorScheme")
    CompactOverlay = field("CompactOverlay")
    CropLabels = field("CropLabels")
    GeoJsonOverlay = field("GeoJsonOverlay")
    Key = field("Key")
    LabelSize = field("LabelSize")
    Language = field("Language")
    Padding = field("Padding")
    PoliticalView = field("PoliticalView")
    PointsOfInterests = field("PointsOfInterests")
    Radius = field("Radius")
    ScaleBarUnit = field("ScaleBarUnit")
    Style = field("Style")
    Zoom = field("Zoom")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStaticMapRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStaticMapRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStyleDescriptorRequest:
    boto3_raw_data: "type_defs.GetStyleDescriptorRequestTypeDef" = dataclasses.field()

    Style = field("Style")
    ColorScheme = field("ColorScheme")
    PoliticalView = field("PoliticalView")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStyleDescriptorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStyleDescriptorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTileRequest:
    boto3_raw_data: "type_defs.GetTileRequestTypeDef" = dataclasses.field()

    Tileset = field("Tileset")
    Z = field("Z")
    X = field("X")
    Y = field("Y")
    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTileRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTileRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGlyphsResponse:
    boto3_raw_data: "type_defs.GetGlyphsResponseTypeDef" = dataclasses.field()

    Blob = field("Blob")
    ContentType = field("ContentType")
    CacheControl = field("CacheControl")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGlyphsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGlyphsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSpritesResponse:
    boto3_raw_data: "type_defs.GetSpritesResponseTypeDef" = dataclasses.field()

    Blob = field("Blob")
    ContentType = field("ContentType")
    CacheControl = field("CacheControl")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSpritesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSpritesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStaticMapResponse:
    boto3_raw_data: "type_defs.GetStaticMapResponseTypeDef" = dataclasses.field()

    Blob = field("Blob")
    ContentType = field("ContentType")
    CacheControl = field("CacheControl")
    ETag = field("ETag")
    PricingBucket = field("PricingBucket")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStaticMapResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStaticMapResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStyleDescriptorResponse:
    boto3_raw_data: "type_defs.GetStyleDescriptorResponseTypeDef" = dataclasses.field()

    Blob = field("Blob")
    ContentType = field("ContentType")
    CacheControl = field("CacheControl")
    ETag = field("ETag")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStyleDescriptorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStyleDescriptorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTileResponse:
    boto3_raw_data: "type_defs.GetTileResponseTypeDef" = dataclasses.field()

    Blob = field("Blob")
    ContentType = field("ContentType")
    CacheControl = field("CacheControl")
    ETag = field("ETag")
    PricingBucket = field("PricingBucket")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTileResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTileResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
