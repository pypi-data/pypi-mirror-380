# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_geo_places import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessPoint:
    boto3_raw_data: "type_defs.AccessPointTypeDef" = dataclasses.field()

    Position = field("Position")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessPointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Category:
    boto3_raw_data: "type_defs.CategoryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    LocalizedName = field("LocalizedName")
    Primary = field("Primary")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CategoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CategoryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecondaryAddressComponentMatchScore:
    boto3_raw_data: "type_defs.SecondaryAddressComponentMatchScoreTypeDef" = (
        dataclasses.field()
    )

    Number = field("Number")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SecondaryAddressComponentMatchScoreTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecondaryAddressComponentMatchScoreTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhonemeTranscription:
    boto3_raw_data: "type_defs.PhonemeTranscriptionTypeDef" = dataclasses.field()

    Value = field("Value")
    Language = field("Language")
    Preferred = field("Preferred")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhonemeTranscriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhonemeTranscriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Country:
    boto3_raw_data: "type_defs.CountryTypeDef" = dataclasses.field()

    Code2 = field("Code2")
    Code3 = field("Code3")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CountryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CountryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Region:
    boto3_raw_data: "type_defs.RegionTypeDef" = dataclasses.field()

    Code = field("Code")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecondaryAddressComponent:
    boto3_raw_data: "type_defs.SecondaryAddressComponentTypeDef" = dataclasses.field()

    Number = field("Number")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecondaryAddressComponentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecondaryAddressComponentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreetComponents:
    boto3_raw_data: "type_defs.StreetComponentsTypeDef" = dataclasses.field()

    BaseName = field("BaseName")
    Type = field("Type")
    TypePlacement = field("TypePlacement")
    TypeSeparator = field("TypeSeparator")
    Prefix = field("Prefix")
    Suffix = field("Suffix")
    Direction = field("Direction")
    Language = field("Language")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StreetComponentsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreetComponentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubRegion:
    boto3_raw_data: "type_defs.SubRegionTypeDef" = dataclasses.field()

    Code = field("Code")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubRegionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubRegionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Highlight:
    boto3_raw_data: "type_defs.HighlightTypeDef" = dataclasses.field()

    StartIndex = field("StartIndex")
    EndIndex = field("EndIndex")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HighlightTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HighlightTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCircle:
    boto3_raw_data: "type_defs.FilterCircleTypeDef" = dataclasses.field()

    Center = field("Center")
    Radius = field("Radius")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterCircleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterCircleTypeDef"]],
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
class BusinessChain:
    boto3_raw_data: "type_defs.BusinessChainTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BusinessChainTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BusinessChainTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FoodType:
    boto3_raw_data: "type_defs.FoodTypeTypeDef" = dataclasses.field()

    LocalizedName = field("LocalizedName")
    Id = field("Id")
    Primary = field("Primary")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FoodTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FoodTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeocodeFilter:
    boto3_raw_data: "type_defs.GeocodeFilterTypeDef" = dataclasses.field()

    IncludeCountries = field("IncludeCountries")
    IncludePlaceTypes = field("IncludePlaceTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeocodeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeocodeFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParsedQueryComponent:
    boto3_raw_data: "type_defs.ParsedQueryComponentTypeDef" = dataclasses.field()

    StartIndex = field("StartIndex")
    EndIndex = field("EndIndex")
    Value = field("Value")
    QueryComponent = field("QueryComponent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParsedQueryComponentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParsedQueryComponentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParsedQuerySecondaryAddressComponent:
    boto3_raw_data: "type_defs.ParsedQuerySecondaryAddressComponentTypeDef" = (
        dataclasses.field()
    )

    StartIndex = field("StartIndex")
    EndIndex = field("EndIndex")
    Value = field("Value")
    Number = field("Number")
    Designator = field("Designator")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParsedQuerySecondaryAddressComponentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParsedQuerySecondaryAddressComponentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeocodeQueryComponents:
    boto3_raw_data: "type_defs.GeocodeQueryComponentsTypeDef" = dataclasses.field()

    Country = field("Country")
    Region = field("Region")
    SubRegion = field("SubRegion")
    Locality = field("Locality")
    District = field("District")
    Street = field("Street")
    AddressNumber = field("AddressNumber")
    PostalCode = field("PostalCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeocodeQueryComponentsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeocodeQueryComponentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeZone:
    boto3_raw_data: "type_defs.TimeZoneTypeDef" = dataclasses.field()

    Name = field("Name")
    Offset = field("Offset")
    OffsetSeconds = field("OffsetSeconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeZoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeZoneTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPlaceRequest:
    boto3_raw_data: "type_defs.GetPlaceRequestTypeDef" = dataclasses.field()

    PlaceId = field("PlaceId")
    AdditionalFeatures = field("AdditionalFeatures")
    Language = field("Language")
    PoliticalView = field("PoliticalView")
    IntendedUse = field("IntendedUse")
    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPlaceRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetPlaceRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpeningHoursComponents:
    boto3_raw_data: "type_defs.OpeningHoursComponentsTypeDef" = dataclasses.field()

    OpenTime = field("OpenTime")
    OpenDuration = field("OpenDuration")
    Recurrence = field("Recurrence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpeningHoursComponentsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpeningHoursComponentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UspsZipPlus4:
    boto3_raw_data: "type_defs.UspsZipPlus4TypeDef" = dataclasses.field()

    RecordTypeCode = field("RecordTypeCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UspsZipPlus4TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UspsZipPlus4TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UspsZip:
    boto3_raw_data: "type_defs.UspsZipTypeDef" = dataclasses.field()

    ZipClassificationCode = field("ZipClassificationCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UspsZipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UspsZipTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryRefinement:
    boto3_raw_data: "type_defs.QueryRefinementTypeDef" = dataclasses.field()

    RefinedTerm = field("RefinedTerm")
    OriginalTerm = field("OriginalTerm")
    StartIndex = field("StartIndex")
    EndIndex = field("EndIndex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryRefinementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryRefinementTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReverseGeocodeFilter:
    boto3_raw_data: "type_defs.ReverseGeocodeFilterTypeDef" = dataclasses.field()

    IncludePlaceTypes = field("IncludePlaceTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReverseGeocodeFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReverseGeocodeFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchNearbyFilter:
    boto3_raw_data: "type_defs.SearchNearbyFilterTypeDef" = dataclasses.field()

    BoundingBox = field("BoundingBox")
    IncludeCountries = field("IncludeCountries")
    IncludeCategories = field("IncludeCategories")
    ExcludeCategories = field("ExcludeCategories")
    IncludeBusinessChains = field("IncludeBusinessChains")
    ExcludeBusinessChains = field("ExcludeBusinessChains")
    IncludeFoodTypes = field("IncludeFoodTypes")
    ExcludeFoodTypes = field("ExcludeFoodTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchNearbyFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchNearbyFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestQueryResult:
    boto3_raw_data: "type_defs.SuggestQueryResultTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    QueryType = field("QueryType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuggestQueryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuggestQueryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessRestriction:
    boto3_raw_data: "type_defs.AccessRestrictionTypeDef" = dataclasses.field()

    Restricted = field("Restricted")

    @cached_property
    def Categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["Categories"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessRestrictionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessRestrictionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactDetails:
    boto3_raw_data: "type_defs.ContactDetailsTypeDef" = dataclasses.field()

    Label = field("Label")
    Value = field("Value")

    @cached_property
    def Categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["Categories"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddressComponentMatchScores:
    boto3_raw_data: "type_defs.AddressComponentMatchScoresTypeDef" = dataclasses.field()

    Country = field("Country")
    Region = field("Region")
    SubRegion = field("SubRegion")
    Locality = field("Locality")
    District = field("District")
    SubDistrict = field("SubDistrict")
    PostalCode = field("PostalCode")
    Block = field("Block")
    SubBlock = field("SubBlock")
    Intersection = field("Intersection")
    AddressNumber = field("AddressNumber")
    Building = field("Building")

    @cached_property
    def SecondaryAddressComponents(self):  # pragma: no cover
        return SecondaryAddressComponentMatchScore.make_many(
            self.boto3_raw_data["SecondaryAddressComponents"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddressComponentMatchScoresTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddressComponentMatchScoresTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddressComponentPhonemes:
    boto3_raw_data: "type_defs.AddressComponentPhonemesTypeDef" = dataclasses.field()

    @cached_property
    def Country(self):  # pragma: no cover
        return PhonemeTranscription.make_many(self.boto3_raw_data["Country"])

    @cached_property
    def Region(self):  # pragma: no cover
        return PhonemeTranscription.make_many(self.boto3_raw_data["Region"])

    @cached_property
    def SubRegion(self):  # pragma: no cover
        return PhonemeTranscription.make_many(self.boto3_raw_data["SubRegion"])

    @cached_property
    def Locality(self):  # pragma: no cover
        return PhonemeTranscription.make_many(self.boto3_raw_data["Locality"])

    @cached_property
    def District(self):  # pragma: no cover
        return PhonemeTranscription.make_many(self.boto3_raw_data["District"])

    @cached_property
    def SubDistrict(self):  # pragma: no cover
        return PhonemeTranscription.make_many(self.boto3_raw_data["SubDistrict"])

    @cached_property
    def Block(self):  # pragma: no cover
        return PhonemeTranscription.make_many(self.boto3_raw_data["Block"])

    @cached_property
    def SubBlock(self):  # pragma: no cover
        return PhonemeTranscription.make_many(self.boto3_raw_data["SubBlock"])

    @cached_property
    def Street(self):  # pragma: no cover
        return PhonemeTranscription.make_many(self.boto3_raw_data["Street"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddressComponentPhonemesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddressComponentPhonemesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Address:
    boto3_raw_data: "type_defs.AddressTypeDef" = dataclasses.field()

    Label = field("Label")

    @cached_property
    def Country(self):  # pragma: no cover
        return Country.make_one(self.boto3_raw_data["Country"])

    @cached_property
    def Region(self):  # pragma: no cover
        return Region.make_one(self.boto3_raw_data["Region"])

    @cached_property
    def SubRegion(self):  # pragma: no cover
        return SubRegion.make_one(self.boto3_raw_data["SubRegion"])

    Locality = field("Locality")
    District = field("District")
    SubDistrict = field("SubDistrict")
    PostalCode = field("PostalCode")
    Block = field("Block")
    SubBlock = field("SubBlock")
    Intersection = field("Intersection")
    Street = field("Street")

    @cached_property
    def StreetComponents(self):  # pragma: no cover
        return StreetComponents.make_many(self.boto3_raw_data["StreetComponents"])

    AddressNumber = field("AddressNumber")
    Building = field("Building")

    @cached_property
    def SecondaryAddressComponents(self):  # pragma: no cover
        return SecondaryAddressComponent.make_many(
            self.boto3_raw_data["SecondaryAddressComponents"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddressTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountryHighlights:
    boto3_raw_data: "type_defs.CountryHighlightsTypeDef" = dataclasses.field()

    @cached_property
    def Code(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Code"])

    @cached_property
    def Name(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Name"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CountryHighlightsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CountryHighlightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegionHighlights:
    boto3_raw_data: "type_defs.RegionHighlightsTypeDef" = dataclasses.field()

    @cached_property
    def Code(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Code"])

    @cached_property
    def Name(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Name"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionHighlightsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegionHighlightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubRegionHighlights:
    boto3_raw_data: "type_defs.SubRegionHighlightsTypeDef" = dataclasses.field()

    @cached_property
    def Code(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Code"])

    @cached_property
    def Name(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Name"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubRegionHighlightsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubRegionHighlightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestAddressHighlights:
    boto3_raw_data: "type_defs.SuggestAddressHighlightsTypeDef" = dataclasses.field()

    @cached_property
    def Label(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Label"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuggestAddressHighlightsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuggestAddressHighlightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutocompleteFilter:
    boto3_raw_data: "type_defs.AutocompleteFilterTypeDef" = dataclasses.field()

    BoundingBox = field("BoundingBox")

    @cached_property
    def Circle(self):  # pragma: no cover
        return FilterCircle.make_one(self.boto3_raw_data["Circle"])

    IncludeCountries = field("IncludeCountries")
    IncludePlaceTypes = field("IncludePlaceTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutocompleteFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutocompleteFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTextFilter:
    boto3_raw_data: "type_defs.SearchTextFilterTypeDef" = dataclasses.field()

    BoundingBox = field("BoundingBox")

    @cached_property
    def Circle(self):  # pragma: no cover
        return FilterCircle.make_one(self.boto3_raw_data["Circle"])

    IncludeCountries = field("IncludeCountries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchTextFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTextFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestFilter:
    boto3_raw_data: "type_defs.SuggestFilterTypeDef" = dataclasses.field()

    BoundingBox = field("BoundingBox")

    @cached_property
    def Circle(self):  # pragma: no cover
        return FilterCircle.make_one(self.boto3_raw_data["Circle"])

    IncludeCountries = field("IncludeCountries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggestFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeocodeParsedQueryAddressComponents:
    boto3_raw_data: "type_defs.GeocodeParsedQueryAddressComponentsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Country(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["Country"])

    @cached_property
    def Region(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["Region"])

    @cached_property
    def SubRegion(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["SubRegion"])

    @cached_property
    def Locality(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["Locality"])

    @cached_property
    def District(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["District"])

    @cached_property
    def SubDistrict(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["SubDistrict"])

    @cached_property
    def PostalCode(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["PostalCode"])

    @cached_property
    def Block(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["Block"])

    @cached_property
    def SubBlock(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["SubBlock"])

    @cached_property
    def Street(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["Street"])

    @cached_property
    def AddressNumber(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["AddressNumber"])

    @cached_property
    def Building(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["Building"])

    @cached_property
    def SecondaryAddressComponents(self):  # pragma: no cover
        return ParsedQuerySecondaryAddressComponent.make_many(
            self.boto3_raw_data["SecondaryAddressComponents"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GeocodeParsedQueryAddressComponentsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeocodeParsedQueryAddressComponentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeocodeRequest:
    boto3_raw_data: "type_defs.GeocodeRequestTypeDef" = dataclasses.field()

    QueryText = field("QueryText")

    @cached_property
    def QueryComponents(self):  # pragma: no cover
        return GeocodeQueryComponents.make_one(self.boto3_raw_data["QueryComponents"])

    MaxResults = field("MaxResults")
    BiasPosition = field("BiasPosition")

    @cached_property
    def Filter(self):  # pragma: no cover
        return GeocodeFilter.make_one(self.boto3_raw_data["Filter"])

    AdditionalFeatures = field("AdditionalFeatures")
    Language = field("Language")
    PoliticalView = field("PoliticalView")
    IntendedUse = field("IntendedUse")
    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeocodeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeocodeRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpeningHours:
    boto3_raw_data: "type_defs.OpeningHoursTypeDef" = dataclasses.field()

    Display = field("Display")
    OpenNow = field("OpenNow")

    @cached_property
    def Components(self):  # pragma: no cover
        return OpeningHoursComponents.make_many(self.boto3_raw_data["Components"])

    @cached_property
    def Categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["Categories"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OpeningHoursTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OpeningHoursTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostalCodeDetails:
    boto3_raw_data: "type_defs.PostalCodeDetailsTypeDef" = dataclasses.field()

    PostalCode = field("PostalCode")
    PostalAuthority = field("PostalAuthority")
    PostalCodeType = field("PostalCodeType")

    @cached_property
    def UspsZip(self):  # pragma: no cover
        return UspsZip.make_one(self.boto3_raw_data["UspsZip"])

    @cached_property
    def UspsZipPlus4(self):  # pragma: no cover
        return UspsZipPlus4.make_one(self.boto3_raw_data["UspsZipPlus4"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PostalCodeDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostalCodeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReverseGeocodeRequest:
    boto3_raw_data: "type_defs.ReverseGeocodeRequestTypeDef" = dataclasses.field()

    QueryPosition = field("QueryPosition")
    QueryRadius = field("QueryRadius")
    MaxResults = field("MaxResults")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ReverseGeocodeFilter.make_one(self.boto3_raw_data["Filter"])

    AdditionalFeatures = field("AdditionalFeatures")
    Language = field("Language")
    PoliticalView = field("PoliticalView")
    IntendedUse = field("IntendedUse")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReverseGeocodeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReverseGeocodeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchNearbyRequest:
    boto3_raw_data: "type_defs.SearchNearbyRequestTypeDef" = dataclasses.field()

    QueryPosition = field("QueryPosition")
    QueryRadius = field("QueryRadius")
    MaxResults = field("MaxResults")

    @cached_property
    def Filter(self):  # pragma: no cover
        return SearchNearbyFilter.make_one(self.boto3_raw_data["Filter"])

    AdditionalFeatures = field("AdditionalFeatures")
    Language = field("Language")
    PoliticalView = field("PoliticalView")
    IntendedUse = field("IntendedUse")
    NextToken = field("NextToken")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchNearbyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchNearbyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Contacts:
    boto3_raw_data: "type_defs.ContactsTypeDef" = dataclasses.field()

    @cached_property
    def Phones(self):  # pragma: no cover
        return ContactDetails.make_many(self.boto3_raw_data["Phones"])

    @cached_property
    def Faxes(self):  # pragma: no cover
        return ContactDetails.make_many(self.boto3_raw_data["Faxes"])

    @cached_property
    def Websites(self):  # pragma: no cover
        return ContactDetails.make_many(self.boto3_raw_data["Websites"])

    @cached_property
    def Emails(self):  # pragma: no cover
        return ContactDetails.make_many(self.boto3_raw_data["Emails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentMatchScores:
    boto3_raw_data: "type_defs.ComponentMatchScoresTypeDef" = dataclasses.field()

    Title = field("Title")

    @cached_property
    def Address(self):  # pragma: no cover
        return AddressComponentMatchScores.make_one(self.boto3_raw_data["Address"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentMatchScoresTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentMatchScoresTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhonemeDetails:
    boto3_raw_data: "type_defs.PhonemeDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Title(self):  # pragma: no cover
        return PhonemeTranscription.make_many(self.boto3_raw_data["Title"])

    @cached_property
    def Address(self):  # pragma: no cover
        return AddressComponentPhonemes.make_one(self.boto3_raw_data["Address"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhonemeDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PhonemeDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Intersection:
    boto3_raw_data: "type_defs.IntersectionTypeDef" = dataclasses.field()

    PlaceId = field("PlaceId")
    Title = field("Title")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    Position = field("Position")
    Distance = field("Distance")
    RouteDistance = field("RouteDistance")
    MapView = field("MapView")

    @cached_property
    def AccessPoints(self):  # pragma: no cover
        return AccessPoint.make_many(self.boto3_raw_data["AccessPoints"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntersectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntersectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedPlace:
    boto3_raw_data: "type_defs.RelatedPlaceTypeDef" = dataclasses.field()

    PlaceId = field("PlaceId")
    PlaceType = field("PlaceType")
    Title = field("Title")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    Position = field("Position")

    @cached_property
    def AccessPoints(self):  # pragma: no cover
        return AccessPoint.make_many(self.boto3_raw_data["AccessPoints"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelatedPlaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelatedPlaceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutocompleteAddressHighlights:
    boto3_raw_data: "type_defs.AutocompleteAddressHighlightsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Label(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Label"])

    @cached_property
    def Country(self):  # pragma: no cover
        return CountryHighlights.make_one(self.boto3_raw_data["Country"])

    @cached_property
    def Region(self):  # pragma: no cover
        return RegionHighlights.make_one(self.boto3_raw_data["Region"])

    @cached_property
    def SubRegion(self):  # pragma: no cover
        return SubRegionHighlights.make_one(self.boto3_raw_data["SubRegion"])

    @cached_property
    def Locality(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Locality"])

    @cached_property
    def District(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["District"])

    @cached_property
    def SubDistrict(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["SubDistrict"])

    @cached_property
    def Street(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Street"])

    @cached_property
    def Block(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Block"])

    @cached_property
    def SubBlock(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["SubBlock"])

    @cached_property
    def Intersection(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Intersection"])

    @cached_property
    def PostalCode(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["PostalCode"])

    @cached_property
    def AddressNumber(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["AddressNumber"])

    @cached_property
    def Building(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Building"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutocompleteAddressHighlightsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutocompleteAddressHighlightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestHighlights:
    boto3_raw_data: "type_defs.SuggestHighlightsTypeDef" = dataclasses.field()

    @cached_property
    def Title(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Title"])

    @cached_property
    def Address(self):  # pragma: no cover
        return SuggestAddressHighlights.make_one(self.boto3_raw_data["Address"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestHighlightsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuggestHighlightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutocompleteRequest:
    boto3_raw_data: "type_defs.AutocompleteRequestTypeDef" = dataclasses.field()

    QueryText = field("QueryText")
    MaxResults = field("MaxResults")
    BiasPosition = field("BiasPosition")

    @cached_property
    def Filter(self):  # pragma: no cover
        return AutocompleteFilter.make_one(self.boto3_raw_data["Filter"])

    PostalCodeMode = field("PostalCodeMode")
    AdditionalFeatures = field("AdditionalFeatures")
    Language = field("Language")
    PoliticalView = field("PoliticalView")
    IntendedUse = field("IntendedUse")
    Key = field("Key")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutocompleteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutocompleteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTextRequest:
    boto3_raw_data: "type_defs.SearchTextRequestTypeDef" = dataclasses.field()

    QueryText = field("QueryText")
    QueryId = field("QueryId")
    MaxResults = field("MaxResults")
    BiasPosition = field("BiasPosition")

    @cached_property
    def Filter(self):  # pragma: no cover
        return SearchTextFilter.make_one(self.boto3_raw_data["Filter"])

    AdditionalFeatures = field("AdditionalFeatures")
    Language = field("Language")
    PoliticalView = field("PoliticalView")
    IntendedUse = field("IntendedUse")
    NextToken = field("NextToken")
    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchTextRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTextRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestRequest:
    boto3_raw_data: "type_defs.SuggestRequestTypeDef" = dataclasses.field()

    QueryText = field("QueryText")
    MaxResults = field("MaxResults")
    MaxQueryRefinements = field("MaxQueryRefinements")
    BiasPosition = field("BiasPosition")

    @cached_property
    def Filter(self):  # pragma: no cover
        return SuggestFilter.make_one(self.boto3_raw_data["Filter"])

    AdditionalFeatures = field("AdditionalFeatures")
    Language = field("Language")
    PoliticalView = field("PoliticalView")
    IntendedUse = field("IntendedUse")
    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggestRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeocodeParsedQuery:
    boto3_raw_data: "type_defs.GeocodeParsedQueryTypeDef" = dataclasses.field()

    @cached_property
    def Title(self):  # pragma: no cover
        return ParsedQueryComponent.make_many(self.boto3_raw_data["Title"])

    @cached_property
    def Address(self):  # pragma: no cover
        return GeocodeParsedQueryAddressComponents.make_one(
            self.boto3_raw_data["Address"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeocodeParsedQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeocodeParsedQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchScoreDetails:
    boto3_raw_data: "type_defs.MatchScoreDetailsTypeDef" = dataclasses.field()

    Overall = field("Overall")

    @cached_property
    def Components(self):  # pragma: no cover
        return ComponentMatchScores.make_one(self.boto3_raw_data["Components"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchScoreDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchScoreDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchNearbyResultItem:
    boto3_raw_data: "type_defs.SearchNearbyResultItemTypeDef" = dataclasses.field()

    PlaceId = field("PlaceId")
    PlaceType = field("PlaceType")
    Title = field("Title")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    AddressNumberCorrected = field("AddressNumberCorrected")
    Position = field("Position")
    Distance = field("Distance")
    MapView = field("MapView")

    @cached_property
    def Categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["Categories"])

    @cached_property
    def FoodTypes(self):  # pragma: no cover
        return FoodType.make_many(self.boto3_raw_data["FoodTypes"])

    @cached_property
    def BusinessChains(self):  # pragma: no cover
        return BusinessChain.make_many(self.boto3_raw_data["BusinessChains"])

    @cached_property
    def Contacts(self):  # pragma: no cover
        return Contacts.make_one(self.boto3_raw_data["Contacts"])

    @cached_property
    def OpeningHours(self):  # pragma: no cover
        return OpeningHours.make_many(self.boto3_raw_data["OpeningHours"])

    @cached_property
    def AccessPoints(self):  # pragma: no cover
        return AccessPoint.make_many(self.boto3_raw_data["AccessPoints"])

    @cached_property
    def AccessRestrictions(self):  # pragma: no cover
        return AccessRestriction.make_many(self.boto3_raw_data["AccessRestrictions"])

    @cached_property
    def TimeZone(self):  # pragma: no cover
        return TimeZone.make_one(self.boto3_raw_data["TimeZone"])

    PoliticalView = field("PoliticalView")

    @cached_property
    def Phonemes(self):  # pragma: no cover
        return PhonemeDetails.make_one(self.boto3_raw_data["Phonemes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchNearbyResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchNearbyResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTextResultItem:
    boto3_raw_data: "type_defs.SearchTextResultItemTypeDef" = dataclasses.field()

    PlaceId = field("PlaceId")
    PlaceType = field("PlaceType")
    Title = field("Title")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    AddressNumberCorrected = field("AddressNumberCorrected")
    Position = field("Position")
    Distance = field("Distance")
    MapView = field("MapView")

    @cached_property
    def Categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["Categories"])

    @cached_property
    def FoodTypes(self):  # pragma: no cover
        return FoodType.make_many(self.boto3_raw_data["FoodTypes"])

    @cached_property
    def BusinessChains(self):  # pragma: no cover
        return BusinessChain.make_many(self.boto3_raw_data["BusinessChains"])

    @cached_property
    def Contacts(self):  # pragma: no cover
        return Contacts.make_one(self.boto3_raw_data["Contacts"])

    @cached_property
    def OpeningHours(self):  # pragma: no cover
        return OpeningHours.make_many(self.boto3_raw_data["OpeningHours"])

    @cached_property
    def AccessPoints(self):  # pragma: no cover
        return AccessPoint.make_many(self.boto3_raw_data["AccessPoints"])

    @cached_property
    def AccessRestrictions(self):  # pragma: no cover
        return AccessRestriction.make_many(self.boto3_raw_data["AccessRestrictions"])

    @cached_property
    def TimeZone(self):  # pragma: no cover
        return TimeZone.make_one(self.boto3_raw_data["TimeZone"])

    PoliticalView = field("PoliticalView")

    @cached_property
    def Phonemes(self):  # pragma: no cover
        return PhonemeDetails.make_one(self.boto3_raw_data["Phonemes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchTextResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTextResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestPlaceResult:
    boto3_raw_data: "type_defs.SuggestPlaceResultTypeDef" = dataclasses.field()

    PlaceId = field("PlaceId")
    PlaceType = field("PlaceType")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    Position = field("Position")
    Distance = field("Distance")
    MapView = field("MapView")

    @cached_property
    def Categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["Categories"])

    @cached_property
    def FoodTypes(self):  # pragma: no cover
        return FoodType.make_many(self.boto3_raw_data["FoodTypes"])

    @cached_property
    def BusinessChains(self):  # pragma: no cover
        return BusinessChain.make_many(self.boto3_raw_data["BusinessChains"])

    @cached_property
    def AccessPoints(self):  # pragma: no cover
        return AccessPoint.make_many(self.boto3_raw_data["AccessPoints"])

    @cached_property
    def AccessRestrictions(self):  # pragma: no cover
        return AccessRestriction.make_many(self.boto3_raw_data["AccessRestrictions"])

    @cached_property
    def TimeZone(self):  # pragma: no cover
        return TimeZone.make_one(self.boto3_raw_data["TimeZone"])

    PoliticalView = field("PoliticalView")

    @cached_property
    def Phonemes(self):  # pragma: no cover
        return PhonemeDetails.make_one(self.boto3_raw_data["Phonemes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SuggestPlaceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuggestPlaceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReverseGeocodeResultItem:
    boto3_raw_data: "type_defs.ReverseGeocodeResultItemTypeDef" = dataclasses.field()

    PlaceId = field("PlaceId")
    PlaceType = field("PlaceType")
    Title = field("Title")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    AddressNumberCorrected = field("AddressNumberCorrected")

    @cached_property
    def PostalCodeDetails(self):  # pragma: no cover
        return PostalCodeDetails.make_many(self.boto3_raw_data["PostalCodeDetails"])

    Position = field("Position")
    Distance = field("Distance")
    MapView = field("MapView")

    @cached_property
    def Categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["Categories"])

    @cached_property
    def FoodTypes(self):  # pragma: no cover
        return FoodType.make_many(self.boto3_raw_data["FoodTypes"])

    @cached_property
    def AccessPoints(self):  # pragma: no cover
        return AccessPoint.make_many(self.boto3_raw_data["AccessPoints"])

    @cached_property
    def TimeZone(self):  # pragma: no cover
        return TimeZone.make_one(self.boto3_raw_data["TimeZone"])

    PoliticalView = field("PoliticalView")

    @cached_property
    def Intersections(self):  # pragma: no cover
        return Intersection.make_many(self.boto3_raw_data["Intersections"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReverseGeocodeResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReverseGeocodeResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPlaceResponse:
    boto3_raw_data: "type_defs.GetPlaceResponseTypeDef" = dataclasses.field()

    PlaceId = field("PlaceId")
    PlaceType = field("PlaceType")
    Title = field("Title")
    PricingBucket = field("PricingBucket")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    AddressNumberCorrected = field("AddressNumberCorrected")

    @cached_property
    def PostalCodeDetails(self):  # pragma: no cover
        return PostalCodeDetails.make_many(self.boto3_raw_data["PostalCodeDetails"])

    Position = field("Position")
    MapView = field("MapView")

    @cached_property
    def Categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["Categories"])

    @cached_property
    def FoodTypes(self):  # pragma: no cover
        return FoodType.make_many(self.boto3_raw_data["FoodTypes"])

    @cached_property
    def BusinessChains(self):  # pragma: no cover
        return BusinessChain.make_many(self.boto3_raw_data["BusinessChains"])

    @cached_property
    def Contacts(self):  # pragma: no cover
        return Contacts.make_one(self.boto3_raw_data["Contacts"])

    @cached_property
    def OpeningHours(self):  # pragma: no cover
        return OpeningHours.make_many(self.boto3_raw_data["OpeningHours"])

    @cached_property
    def AccessPoints(self):  # pragma: no cover
        return AccessPoint.make_many(self.boto3_raw_data["AccessPoints"])

    @cached_property
    def AccessRestrictions(self):  # pragma: no cover
        return AccessRestriction.make_many(self.boto3_raw_data["AccessRestrictions"])

    @cached_property
    def TimeZone(self):  # pragma: no cover
        return TimeZone.make_one(self.boto3_raw_data["TimeZone"])

    PoliticalView = field("PoliticalView")

    @cached_property
    def Phonemes(self):  # pragma: no cover
        return PhonemeDetails.make_one(self.boto3_raw_data["Phonemes"])

    @cached_property
    def MainAddress(self):  # pragma: no cover
        return RelatedPlace.make_one(self.boto3_raw_data["MainAddress"])

    @cached_property
    def SecondaryAddresses(self):  # pragma: no cover
        return RelatedPlace.make_many(self.boto3_raw_data["SecondaryAddresses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetPlaceResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPlaceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutocompleteHighlights:
    boto3_raw_data: "type_defs.AutocompleteHighlightsTypeDef" = dataclasses.field()

    @cached_property
    def Title(self):  # pragma: no cover
        return Highlight.make_many(self.boto3_raw_data["Title"])

    @cached_property
    def Address(self):  # pragma: no cover
        return AutocompleteAddressHighlights.make_one(self.boto3_raw_data["Address"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutocompleteHighlightsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutocompleteHighlightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeocodeResultItem:
    boto3_raw_data: "type_defs.GeocodeResultItemTypeDef" = dataclasses.field()

    PlaceId = field("PlaceId")
    PlaceType = field("PlaceType")
    Title = field("Title")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    AddressNumberCorrected = field("AddressNumberCorrected")

    @cached_property
    def PostalCodeDetails(self):  # pragma: no cover
        return PostalCodeDetails.make_many(self.boto3_raw_data["PostalCodeDetails"])

    Position = field("Position")
    Distance = field("Distance")
    MapView = field("MapView")

    @cached_property
    def Categories(self):  # pragma: no cover
        return Category.make_many(self.boto3_raw_data["Categories"])

    @cached_property
    def FoodTypes(self):  # pragma: no cover
        return FoodType.make_many(self.boto3_raw_data["FoodTypes"])

    @cached_property
    def AccessPoints(self):  # pragma: no cover
        return AccessPoint.make_many(self.boto3_raw_data["AccessPoints"])

    @cached_property
    def TimeZone(self):  # pragma: no cover
        return TimeZone.make_one(self.boto3_raw_data["TimeZone"])

    PoliticalView = field("PoliticalView")

    @cached_property
    def MatchScores(self):  # pragma: no cover
        return MatchScoreDetails.make_one(self.boto3_raw_data["MatchScores"])

    @cached_property
    def ParsedQuery(self):  # pragma: no cover
        return GeocodeParsedQuery.make_one(self.boto3_raw_data["ParsedQuery"])

    @cached_property
    def Intersections(self):  # pragma: no cover
        return Intersection.make_many(self.boto3_raw_data["Intersections"])

    @cached_property
    def MainAddress(self):  # pragma: no cover
        return RelatedPlace.make_one(self.boto3_raw_data["MainAddress"])

    @cached_property
    def SecondaryAddresses(self):  # pragma: no cover
        return RelatedPlace.make_many(self.boto3_raw_data["SecondaryAddresses"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeocodeResultItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeocodeResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchNearbyResponse:
    boto3_raw_data: "type_defs.SearchNearbyResponseTypeDef" = dataclasses.field()

    PricingBucket = field("PricingBucket")

    @cached_property
    def ResultItems(self):  # pragma: no cover
        return SearchNearbyResultItem.make_many(self.boto3_raw_data["ResultItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchNearbyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchNearbyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTextResponse:
    boto3_raw_data: "type_defs.SearchTextResponseTypeDef" = dataclasses.field()

    PricingBucket = field("PricingBucket")

    @cached_property
    def ResultItems(self):  # pragma: no cover
        return SearchTextResultItem.make_many(self.boto3_raw_data["ResultItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchTextResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTextResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestResultItem:
    boto3_raw_data: "type_defs.SuggestResultItemTypeDef" = dataclasses.field()

    Title = field("Title")
    SuggestResultItemType = field("SuggestResultItemType")

    @cached_property
    def Place(self):  # pragma: no cover
        return SuggestPlaceResult.make_one(self.boto3_raw_data["Place"])

    @cached_property
    def Query(self):  # pragma: no cover
        return SuggestQueryResult.make_one(self.boto3_raw_data["Query"])

    @cached_property
    def Highlights(self):  # pragma: no cover
        return SuggestHighlights.make_one(self.boto3_raw_data["Highlights"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestResultItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuggestResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReverseGeocodeResponse:
    boto3_raw_data: "type_defs.ReverseGeocodeResponseTypeDef" = dataclasses.field()

    PricingBucket = field("PricingBucket")

    @cached_property
    def ResultItems(self):  # pragma: no cover
        return ReverseGeocodeResultItem.make_many(self.boto3_raw_data["ResultItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReverseGeocodeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReverseGeocodeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutocompleteResultItem:
    boto3_raw_data: "type_defs.AutocompleteResultItemTypeDef" = dataclasses.field()

    PlaceId = field("PlaceId")
    PlaceType = field("PlaceType")
    Title = field("Title")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    Distance = field("Distance")
    Language = field("Language")
    PoliticalView = field("PoliticalView")

    @cached_property
    def Highlights(self):  # pragma: no cover
        return AutocompleteHighlights.make_one(self.boto3_raw_data["Highlights"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutocompleteResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutocompleteResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeocodeResponse:
    boto3_raw_data: "type_defs.GeocodeResponseTypeDef" = dataclasses.field()

    PricingBucket = field("PricingBucket")

    @cached_property
    def ResultItems(self):  # pragma: no cover
        return GeocodeResultItem.make_many(self.boto3_raw_data["ResultItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeocodeResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeocodeResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggestResponse:
    boto3_raw_data: "type_defs.SuggestResponseTypeDef" = dataclasses.field()

    PricingBucket = field("PricingBucket")

    @cached_property
    def ResultItems(self):  # pragma: no cover
        return SuggestResultItem.make_many(self.boto3_raw_data["ResultItems"])

    @cached_property
    def QueryRefinements(self):  # pragma: no cover
        return QueryRefinement.make_many(self.boto3_raw_data["QueryRefinements"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggestResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggestResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutocompleteResponse:
    boto3_raw_data: "type_defs.AutocompleteResponseTypeDef" = dataclasses.field()

    PricingBucket = field("PricingBucket")

    @cached_property
    def ResultItems(self):  # pragma: no cover
        return AutocompleteResultItem.make_many(self.boto3_raw_data["ResultItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutocompleteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutocompleteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
