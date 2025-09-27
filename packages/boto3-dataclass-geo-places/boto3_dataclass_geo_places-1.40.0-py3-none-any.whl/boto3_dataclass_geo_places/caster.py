# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_geo_places import type_defs as bs_td


class GEO_PLACESCaster:

    def autocomplete(
        self,
        res: "bs_td.AutocompleteResponseTypeDef",
    ) -> "dc_td.AutocompleteResponse":
        return dc_td.AutocompleteResponse.make_one(res)

    def geocode(
        self,
        res: "bs_td.GeocodeResponseTypeDef",
    ) -> "dc_td.GeocodeResponse":
        return dc_td.GeocodeResponse.make_one(res)

    def get_place(
        self,
        res: "bs_td.GetPlaceResponseTypeDef",
    ) -> "dc_td.GetPlaceResponse":
        return dc_td.GetPlaceResponse.make_one(res)

    def reverse_geocode(
        self,
        res: "bs_td.ReverseGeocodeResponseTypeDef",
    ) -> "dc_td.ReverseGeocodeResponse":
        return dc_td.ReverseGeocodeResponse.make_one(res)

    def search_nearby(
        self,
        res: "bs_td.SearchNearbyResponseTypeDef",
    ) -> "dc_td.SearchNearbyResponse":
        return dc_td.SearchNearbyResponse.make_one(res)

    def search_text(
        self,
        res: "bs_td.SearchTextResponseTypeDef",
    ) -> "dc_td.SearchTextResponse":
        return dc_td.SearchTextResponse.make_one(res)

    def suggest(
        self,
        res: "bs_td.SuggestResponseTypeDef",
    ) -> "dc_td.SuggestResponse":
        return dc_td.SuggestResponse.make_one(res)


geo_places_caster = GEO_PLACESCaster()
