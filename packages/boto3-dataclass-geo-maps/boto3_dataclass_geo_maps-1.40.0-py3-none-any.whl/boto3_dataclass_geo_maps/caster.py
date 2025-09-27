# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_geo_maps import type_defs as bs_td


class GEO_MAPSCaster:

    def get_glyphs(
        self,
        res: "bs_td.GetGlyphsResponseTypeDef",
    ) -> "dc_td.GetGlyphsResponse":
        return dc_td.GetGlyphsResponse.make_one(res)

    def get_sprites(
        self,
        res: "bs_td.GetSpritesResponseTypeDef",
    ) -> "dc_td.GetSpritesResponse":
        return dc_td.GetSpritesResponse.make_one(res)

    def get_static_map(
        self,
        res: "bs_td.GetStaticMapResponseTypeDef",
    ) -> "dc_td.GetStaticMapResponse":
        return dc_td.GetStaticMapResponse.make_one(res)

    def get_style_descriptor(
        self,
        res: "bs_td.GetStyleDescriptorResponseTypeDef",
    ) -> "dc_td.GetStyleDescriptorResponse":
        return dc_td.GetStyleDescriptorResponse.make_one(res)

    def get_tile(
        self,
        res: "bs_td.GetTileResponseTypeDef",
    ) -> "dc_td.GetTileResponse":
        return dc_td.GetTileResponse.make_one(res)


geo_maps_caster = GEO_MAPSCaster()
