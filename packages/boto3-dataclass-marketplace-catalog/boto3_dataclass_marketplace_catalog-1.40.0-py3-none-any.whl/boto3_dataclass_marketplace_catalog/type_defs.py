# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_marketplace_catalog import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AmiProductEntityIdFilter:
    boto3_raw_data: "type_defs.AmiProductEntityIdFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AmiProductEntityIdFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmiProductEntityIdFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmiProductTitleFilter:
    boto3_raw_data: "type_defs.AmiProductTitleFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AmiProductTitleFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmiProductTitleFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmiProductVisibilityFilter:
    boto3_raw_data: "type_defs.AmiProductVisibilityFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AmiProductVisibilityFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmiProductVisibilityFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmiProductLastModifiedDateFilterDateRange:
    boto3_raw_data: "type_defs.AmiProductLastModifiedDateFilterDateRangeTypeDef" = (
        dataclasses.field()
    )

    AfterValue = field("AfterValue")
    BeforeValue = field("BeforeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmiProductLastModifiedDateFilterDateRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmiProductLastModifiedDateFilterDateRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmiProductSort:
    boto3_raw_data: "type_defs.AmiProductSortTypeDef" = dataclasses.field()

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AmiProductSortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AmiProductSortTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmiProductSummary:
    boto3_raw_data: "type_defs.AmiProductSummaryTypeDef" = dataclasses.field()

    ProductTitle = field("ProductTitle")
    Visibility = field("Visibility")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AmiProductSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmiProductSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityRequest:
    boto3_raw_data: "type_defs.EntityRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    EntityId = field("EntityId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDescribeErrorDetail:
    boto3_raw_data: "type_defs.BatchDescribeErrorDetailTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDescribeErrorDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDescribeErrorDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityDetail:
    boto3_raw_data: "type_defs.EntityDetailTypeDef" = dataclasses.field()

    EntityType = field("EntityType")
    EntityArn = field("EntityArn")
    EntityIdentifier = field("EntityIdentifier")
    LastModifiedDate = field("LastModifiedDate")
    DetailsDocument = field("DetailsDocument")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityDetailTypeDef"]],
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
class CancelChangeSetRequest:
    boto3_raw_data: "type_defs.CancelChangeSetRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    ChangeSetId = field("ChangeSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelChangeSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelChangeSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeSetSummaryListItem:
    boto3_raw_data: "type_defs.ChangeSetSummaryListItemTypeDef" = dataclasses.field()

    ChangeSetId = field("ChangeSetId")
    ChangeSetArn = field("ChangeSetArn")
    ChangeSetName = field("ChangeSetName")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Status = field("Status")
    EntityIdList = field("EntityIdList")
    FailureCode = field("FailureCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeSetSummaryListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeSetSummaryListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Entity:
    boto3_raw_data: "type_defs.EntityTypeDef" = dataclasses.field()

    Type = field("Type")
    Identifier = field("Identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetail:
    boto3_raw_data: "type_defs.ErrorDetailTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerProductEntityIdFilter:
    boto3_raw_data: "type_defs.ContainerProductEntityIdFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContainerProductEntityIdFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerProductEntityIdFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerProductTitleFilter:
    boto3_raw_data: "type_defs.ContainerProductTitleFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerProductTitleFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerProductTitleFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerProductVisibilityFilter:
    boto3_raw_data: "type_defs.ContainerProductVisibilityFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContainerProductVisibilityFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerProductVisibilityFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerProductLastModifiedDateFilterDateRange:
    boto3_raw_data: (
        "type_defs.ContainerProductLastModifiedDateFilterDateRangeTypeDef"
    ) = dataclasses.field()

    AfterValue = field("AfterValue")
    BeforeValue = field("BeforeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContainerProductLastModifiedDateFilterDateRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ContainerProductLastModifiedDateFilterDateRangeTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerProductSort:
    boto3_raw_data: "type_defs.ContainerProductSortTypeDef" = dataclasses.field()

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerProductSortTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerProductSortTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerProductSummary:
    boto3_raw_data: "type_defs.ContainerProductSummaryTypeDef" = dataclasses.field()

    ProductTitle = field("ProductTitle")
    Visibility = field("Visibility")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerProductSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerProductSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductEntityIdFilter:
    boto3_raw_data: "type_defs.DataProductEntityIdFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProductEntityIdFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductEntityIdFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductTitleFilter:
    boto3_raw_data: "type_defs.DataProductTitleFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProductTitleFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductTitleFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductVisibilityFilter:
    boto3_raw_data: "type_defs.DataProductVisibilityFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProductVisibilityFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductVisibilityFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductLastModifiedDateFilterDateRange:
    boto3_raw_data: "type_defs.DataProductLastModifiedDateFilterDateRangeTypeDef" = (
        dataclasses.field()
    )

    AfterValue = field("AfterValue")
    BeforeValue = field("BeforeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataProductLastModifiedDateFilterDateRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductLastModifiedDateFilterDateRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductSort:
    boto3_raw_data: "type_defs.DataProductSortTypeDef" = dataclasses.field()

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataProductSortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataProductSortTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductSummary:
    boto3_raw_data: "type_defs.DataProductSummaryTypeDef" = dataclasses.field()

    ProductTitle = field("ProductTitle")
    Visibility = field("Visibility")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProductSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyRequest:
    boto3_raw_data: "type_defs.DeleteResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChangeSetRequest:
    boto3_raw_data: "type_defs.DescribeChangeSetRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    ChangeSetId = field("ChangeSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChangeSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChangeSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntityRequest:
    boto3_raw_data: "type_defs.DescribeEntityRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    EntityId = field("EntityId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEntityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MachineLearningProductSummary:
    boto3_raw_data: "type_defs.MachineLearningProductSummaryTypeDef" = (
        dataclasses.field()
    )

    ProductTitle = field("ProductTitle")
    Visibility = field("Visibility")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MachineLearningProductSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MachineLearningProductSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferSummary:
    boto3_raw_data: "type_defs.OfferSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    ProductId = field("ProductId")
    ResaleAuthorizationId = field("ResaleAuthorizationId")
    ReleaseDate = field("ReleaseDate")
    AvailabilityEndDate = field("AvailabilityEndDate")
    BuyerAccounts = field("BuyerAccounts")
    State = field("State")
    Targeting = field("Targeting")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OfferSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OfferSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationSummary:
    boto3_raw_data: "type_defs.ResaleAuthorizationSummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    ProductId = field("ProductId")
    ProductName = field("ProductName")
    ManufacturerAccountId = field("ManufacturerAccountId")
    ManufacturerLegalName = field("ManufacturerLegalName")
    ResellerAccountID = field("ResellerAccountID")
    ResellerLegalName = field("ResellerLegalName")
    Status = field("Status")
    OfferExtendedStatus = field("OfferExtendedStatus")
    CreatedDate = field("CreatedDate")
    AvailabilityEndDate = field("AvailabilityEndDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResaleAuthorizationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SaaSProductSummary:
    boto3_raw_data: "type_defs.SaaSProductSummaryTypeDef" = dataclasses.field()

    ProductTitle = field("ProductTitle")
    Visibility = field("Visibility")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SaaSProductSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SaaSProductSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MachineLearningProductSort:
    boto3_raw_data: "type_defs.MachineLearningProductSortTypeDef" = dataclasses.field()

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MachineLearningProductSortTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MachineLearningProductSortTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferSort:
    boto3_raw_data: "type_defs.OfferSortTypeDef" = dataclasses.field()

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OfferSortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OfferSortTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationSort:
    boto3_raw_data: "type_defs.ResaleAuthorizationSortTypeDef" = dataclasses.field()

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResaleAuthorizationSortTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationSortTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SaaSProductSort:
    boto3_raw_data: "type_defs.SaaSProductSortTypeDef" = dataclasses.field()

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SaaSProductSortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SaaSProductSortTypeDef"]],
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
    ValueList = field("ValueList")

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
class GetResourcePolicyRequest:
    boto3_raw_data: "type_defs.GetResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyRequestTypeDef"]
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
class Sort:
    boto3_raw_data: "type_defs.SortTypeDef" = dataclasses.field()

    SortBy = field("SortBy")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortTypeDef"]]
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
class MachineLearningProductEntityIdFilter:
    boto3_raw_data: "type_defs.MachineLearningProductEntityIdFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MachineLearningProductEntityIdFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MachineLearningProductEntityIdFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MachineLearningProductTitleFilter:
    boto3_raw_data: "type_defs.MachineLearningProductTitleFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MachineLearningProductTitleFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MachineLearningProductTitleFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MachineLearningProductVisibilityFilter:
    boto3_raw_data: "type_defs.MachineLearningProductVisibilityFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MachineLearningProductVisibilityFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MachineLearningProductVisibilityFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MachineLearningProductLastModifiedDateFilterDateRange:
    boto3_raw_data: (
        "type_defs.MachineLearningProductLastModifiedDateFilterDateRangeTypeDef"
    ) = dataclasses.field()

    AfterValue = field("AfterValue")
    BeforeValue = field("BeforeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MachineLearningProductLastModifiedDateFilterDateRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.MachineLearningProductLastModifiedDateFilterDateRangeTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferAvailabilityEndDateFilterDateRange:
    boto3_raw_data: "type_defs.OfferAvailabilityEndDateFilterDateRangeTypeDef" = (
        dataclasses.field()
    )

    AfterValue = field("AfterValue")
    BeforeValue = field("BeforeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OfferAvailabilityEndDateFilterDateRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferAvailabilityEndDateFilterDateRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferBuyerAccountsFilter:
    boto3_raw_data: "type_defs.OfferBuyerAccountsFilterTypeDef" = dataclasses.field()

    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OfferBuyerAccountsFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferBuyerAccountsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferEntityIdFilter:
    boto3_raw_data: "type_defs.OfferEntityIdFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OfferEntityIdFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferEntityIdFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferNameFilter:
    boto3_raw_data: "type_defs.OfferNameFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OfferNameFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OfferNameFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferProductIdFilter:
    boto3_raw_data: "type_defs.OfferProductIdFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OfferProductIdFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferProductIdFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferResaleAuthorizationIdFilter:
    boto3_raw_data: "type_defs.OfferResaleAuthorizationIdFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OfferResaleAuthorizationIdFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferResaleAuthorizationIdFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferStateFilter:
    boto3_raw_data: "type_defs.OfferStateFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OfferStateFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferStateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferTargetingFilter:
    boto3_raw_data: "type_defs.OfferTargetingFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OfferTargetingFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferTargetingFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferLastModifiedDateFilterDateRange:
    boto3_raw_data: "type_defs.OfferLastModifiedDateFilterDateRangeTypeDef" = (
        dataclasses.field()
    )

    AfterValue = field("AfterValue")
    BeforeValue = field("BeforeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OfferLastModifiedDateFilterDateRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferLastModifiedDateFilterDateRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferReleaseDateFilterDateRange:
    boto3_raw_data: "type_defs.OfferReleaseDateFilterDateRangeTypeDef" = (
        dataclasses.field()
    )

    AfterValue = field("AfterValue")
    BeforeValue = field("BeforeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OfferReleaseDateFilterDateRangeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferReleaseDateFilterDateRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Policy = field("Policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationAvailabilityEndDateFilterDateRange:
    boto3_raw_data: (
        "type_defs.ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef"
    ) = dataclasses.field()

    AfterValue = field("AfterValue")
    BeforeValue = field("BeforeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationCreatedDateFilterDateRange:
    boto3_raw_data: "type_defs.ResaleAuthorizationCreatedDateFilterDateRangeTypeDef" = (
        dataclasses.field()
    )

    AfterValue = field("AfterValue")
    BeforeValue = field("BeforeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationCreatedDateFilterDateRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationCreatedDateFilterDateRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationEntityIdFilter:
    boto3_raw_data: "type_defs.ResaleAuthorizationEntityIdFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationEntityIdFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationEntityIdFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationManufacturerAccountIdFilter:
    boto3_raw_data: (
        "type_defs.ResaleAuthorizationManufacturerAccountIdFilterTypeDef"
    ) = dataclasses.field()

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationManufacturerAccountIdFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ResaleAuthorizationManufacturerAccountIdFilterTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationManufacturerLegalNameFilter:
    boto3_raw_data: (
        "type_defs.ResaleAuthorizationManufacturerLegalNameFilterTypeDef"
    ) = dataclasses.field()

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationManufacturerLegalNameFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ResaleAuthorizationManufacturerLegalNameFilterTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationNameFilter:
    boto3_raw_data: "type_defs.ResaleAuthorizationNameFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResaleAuthorizationNameFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationNameFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationOfferExtendedStatusFilter:
    boto3_raw_data: "type_defs.ResaleAuthorizationOfferExtendedStatusFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationOfferExtendedStatusFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationOfferExtendedStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationProductIdFilter:
    boto3_raw_data: "type_defs.ResaleAuthorizationProductIdFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationProductIdFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationProductIdFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationProductNameFilter:
    boto3_raw_data: "type_defs.ResaleAuthorizationProductNameFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationProductNameFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationProductNameFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationResellerAccountIDFilter:
    boto3_raw_data: "type_defs.ResaleAuthorizationResellerAccountIDFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationResellerAccountIDFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationResellerAccountIDFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationResellerLegalNameFilter:
    boto3_raw_data: "type_defs.ResaleAuthorizationResellerLegalNameFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationResellerLegalNameFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationResellerLegalNameFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationStatusFilter:
    boto3_raw_data: "type_defs.ResaleAuthorizationStatusFilterTypeDef" = (
        dataclasses.field()
    )

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResaleAuthorizationStatusFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationLastModifiedDateFilterDateRange:
    boto3_raw_data: (
        "type_defs.ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef"
    ) = dataclasses.field()

    AfterValue = field("AfterValue")
    BeforeValue = field("BeforeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SaaSProductEntityIdFilter:
    boto3_raw_data: "type_defs.SaaSProductEntityIdFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SaaSProductEntityIdFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SaaSProductEntityIdFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SaaSProductTitleFilter:
    boto3_raw_data: "type_defs.SaaSProductTitleFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")
    WildCardValue = field("WildCardValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SaaSProductTitleFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SaaSProductTitleFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SaaSProductVisibilityFilter:
    boto3_raw_data: "type_defs.SaaSProductVisibilityFilterTypeDef" = dataclasses.field()

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SaaSProductVisibilityFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SaaSProductVisibilityFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SaaSProductLastModifiedDateFilterDateRange:
    boto3_raw_data: "type_defs.SaaSProductLastModifiedDateFilterDateRangeTypeDef" = (
        dataclasses.field()
    )

    AfterValue = field("AfterValue")
    BeforeValue = field("BeforeValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SaaSProductLastModifiedDateFilterDateRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SaaSProductLastModifiedDateFilterDateRangeTypeDef"]
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
class AmiProductLastModifiedDateFilter:
    boto3_raw_data: "type_defs.AmiProductLastModifiedDateFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DateRange(self):  # pragma: no cover
        return AmiProductLastModifiedDateFilterDateRange.make_one(
            self.boto3_raw_data["DateRange"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AmiProductLastModifiedDateFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmiProductLastModifiedDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDescribeEntitiesRequest:
    boto3_raw_data: "type_defs.BatchDescribeEntitiesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntityRequestList(self):  # pragma: no cover
        return EntityRequest.make_many(self.boto3_raw_data["EntityRequestList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDescribeEntitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDescribeEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDescribeEntitiesResponse:
    boto3_raw_data: "type_defs.BatchDescribeEntitiesResponseTypeDef" = (
        dataclasses.field()
    )

    EntityDetails = field("EntityDetails")
    Errors = field("Errors")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDescribeEntitiesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDescribeEntitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelChangeSetResponse:
    boto3_raw_data: "type_defs.CancelChangeSetResponseTypeDef" = dataclasses.field()

    ChangeSetId = field("ChangeSetId")
    ChangeSetArn = field("ChangeSetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelChangeSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelChangeSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEntityResponse:
    boto3_raw_data: "type_defs.DescribeEntityResponseTypeDef" = dataclasses.field()

    EntityType = field("EntityType")
    EntityIdentifier = field("EntityIdentifier")
    EntityArn = field("EntityArn")
    LastModifiedDate = field("LastModifiedDate")
    Details = field("Details")
    DetailsDocument = field("DetailsDocument")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEntityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEntityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyResponse:
    boto3_raw_data: "type_defs.GetResourcePolicyResponseTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChangeSetResponse:
    boto3_raw_data: "type_defs.StartChangeSetResponseTypeDef" = dataclasses.field()

    ChangeSetId = field("ChangeSetId")
    ChangeSetArn = field("ChangeSetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartChangeSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartChangeSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChangeSetsResponse:
    boto3_raw_data: "type_defs.ListChangeSetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ChangeSetSummaryList(self):  # pragma: no cover
        return ChangeSetSummaryListItem.make_many(
            self.boto3_raw_data["ChangeSetSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChangeSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChangeSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeSummary:
    boto3_raw_data: "type_defs.ChangeSummaryTypeDef" = dataclasses.field()

    ChangeType = field("ChangeType")

    @cached_property
    def Entity(self):  # pragma: no cover
        return Entity.make_one(self.boto3_raw_data["Entity"])

    Details = field("Details")
    DetailsDocument = field("DetailsDocument")

    @cached_property
    def ErrorDetailList(self):  # pragma: no cover
        return ErrorDetail.make_many(self.boto3_raw_data["ErrorDetailList"])

    ChangeName = field("ChangeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangeSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChangeSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Change:
    boto3_raw_data: "type_defs.ChangeTypeDef" = dataclasses.field()

    ChangeType = field("ChangeType")

    @cached_property
    def Entity(self):  # pragma: no cover
        return Entity.make_one(self.boto3_raw_data["Entity"])

    @cached_property
    def EntityTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["EntityTags"])

    Details = field("Details")
    DetailsDocument = field("DetailsDocument")
    ChangeName = field("ChangeName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class ContainerProductLastModifiedDateFilter:
    boto3_raw_data: "type_defs.ContainerProductLastModifiedDateFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DateRange(self):  # pragma: no cover
        return ContainerProductLastModifiedDateFilterDateRange.make_one(
            self.boto3_raw_data["DateRange"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContainerProductLastModifiedDateFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerProductLastModifiedDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductLastModifiedDateFilter:
    boto3_raw_data: "type_defs.DataProductLastModifiedDateFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DateRange(self):  # pragma: no cover
        return DataProductLastModifiedDateFilterDateRange.make_one(
            self.boto3_raw_data["DateRange"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataProductLastModifiedDateFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductLastModifiedDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntitySummary:
    boto3_raw_data: "type_defs.EntitySummaryTypeDef" = dataclasses.field()

    Name = field("Name")
    EntityType = field("EntityType")
    EntityId = field("EntityId")
    EntityArn = field("EntityArn")
    LastModifiedDate = field("LastModifiedDate")
    Visibility = field("Visibility")

    @cached_property
    def AmiProductSummary(self):  # pragma: no cover
        return AmiProductSummary.make_one(self.boto3_raw_data["AmiProductSummary"])

    @cached_property
    def ContainerProductSummary(self):  # pragma: no cover
        return ContainerProductSummary.make_one(
            self.boto3_raw_data["ContainerProductSummary"]
        )

    @cached_property
    def DataProductSummary(self):  # pragma: no cover
        return DataProductSummary.make_one(self.boto3_raw_data["DataProductSummary"])

    @cached_property
    def SaaSProductSummary(self):  # pragma: no cover
        return SaaSProductSummary.make_one(self.boto3_raw_data["SaaSProductSummary"])

    @cached_property
    def OfferSummary(self):  # pragma: no cover
        return OfferSummary.make_one(self.boto3_raw_data["OfferSummary"])

    @cached_property
    def ResaleAuthorizationSummary(self):  # pragma: no cover
        return ResaleAuthorizationSummary.make_one(
            self.boto3_raw_data["ResaleAuthorizationSummary"]
        )

    @cached_property
    def MachineLearningProductSummary(self):  # pragma: no cover
        return MachineLearningProductSummary.make_one(
            self.boto3_raw_data["MachineLearningProductSummary"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntitySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntitySummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityTypeSort:
    boto3_raw_data: "type_defs.EntityTypeSortTypeDef" = dataclasses.field()

    @cached_property
    def DataProductSort(self):  # pragma: no cover
        return DataProductSort.make_one(self.boto3_raw_data["DataProductSort"])

    @cached_property
    def SaaSProductSort(self):  # pragma: no cover
        return SaaSProductSort.make_one(self.boto3_raw_data["SaaSProductSort"])

    @cached_property
    def AmiProductSort(self):  # pragma: no cover
        return AmiProductSort.make_one(self.boto3_raw_data["AmiProductSort"])

    @cached_property
    def OfferSort(self):  # pragma: no cover
        return OfferSort.make_one(self.boto3_raw_data["OfferSort"])

    @cached_property
    def ContainerProductSort(self):  # pragma: no cover
        return ContainerProductSort.make_one(
            self.boto3_raw_data["ContainerProductSort"]
        )

    @cached_property
    def ResaleAuthorizationSort(self):  # pragma: no cover
        return ResaleAuthorizationSort.make_one(
            self.boto3_raw_data["ResaleAuthorizationSort"]
        )

    @cached_property
    def MachineLearningProductSort(self):  # pragma: no cover
        return MachineLearningProductSort.make_one(
            self.boto3_raw_data["MachineLearningProductSort"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityTypeSortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityTypeSortTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChangeSetsRequestPaginate:
    boto3_raw_data: "type_defs.ListChangeSetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Catalog = field("Catalog")

    @cached_property
    def FilterList(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["FilterList"])

    @cached_property
    def Sort(self):  # pragma: no cover
        return Sort.make_one(self.boto3_raw_data["Sort"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListChangeSetsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChangeSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChangeSetsRequest:
    boto3_raw_data: "type_defs.ListChangeSetsRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")

    @cached_property
    def FilterList(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["FilterList"])

    @cached_property
    def Sort(self):  # pragma: no cover
        return Sort.make_one(self.boto3_raw_data["Sort"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChangeSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChangeSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MachineLearningProductLastModifiedDateFilter:
    boto3_raw_data: "type_defs.MachineLearningProductLastModifiedDateFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DateRange(self):  # pragma: no cover
        return MachineLearningProductLastModifiedDateFilterDateRange.make_one(
            self.boto3_raw_data["DateRange"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MachineLearningProductLastModifiedDateFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MachineLearningProductLastModifiedDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferAvailabilityEndDateFilter:
    boto3_raw_data: "type_defs.OfferAvailabilityEndDateFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DateRange(self):  # pragma: no cover
        return OfferAvailabilityEndDateFilterDateRange.make_one(
            self.boto3_raw_data["DateRange"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OfferAvailabilityEndDateFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferAvailabilityEndDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferLastModifiedDateFilter:
    boto3_raw_data: "type_defs.OfferLastModifiedDateFilterTypeDef" = dataclasses.field()

    @cached_property
    def DateRange(self):  # pragma: no cover
        return OfferLastModifiedDateFilterDateRange.make_one(
            self.boto3_raw_data["DateRange"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OfferLastModifiedDateFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferLastModifiedDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferReleaseDateFilter:
    boto3_raw_data: "type_defs.OfferReleaseDateFilterTypeDef" = dataclasses.field()

    @cached_property
    def DateRange(self):  # pragma: no cover
        return OfferReleaseDateFilterDateRange.make_one(
            self.boto3_raw_data["DateRange"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OfferReleaseDateFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OfferReleaseDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationAvailabilityEndDateFilter:
    boto3_raw_data: "type_defs.ResaleAuthorizationAvailabilityEndDateFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DateRange(self):  # pragma: no cover
        return ResaleAuthorizationAvailabilityEndDateFilterDateRange.make_one(
            self.boto3_raw_data["DateRange"]
        )

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationAvailabilityEndDateFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationAvailabilityEndDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationCreatedDateFilter:
    boto3_raw_data: "type_defs.ResaleAuthorizationCreatedDateFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DateRange(self):  # pragma: no cover
        return ResaleAuthorizationCreatedDateFilterDateRange.make_one(
            self.boto3_raw_data["DateRange"]
        )

    ValueList = field("ValueList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationCreatedDateFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationCreatedDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationLastModifiedDateFilter:
    boto3_raw_data: "type_defs.ResaleAuthorizationLastModifiedDateFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DateRange(self):  # pragma: no cover
        return ResaleAuthorizationLastModifiedDateFilterDateRange.make_one(
            self.boto3_raw_data["DateRange"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResaleAuthorizationLastModifiedDateFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationLastModifiedDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SaaSProductLastModifiedDateFilter:
    boto3_raw_data: "type_defs.SaaSProductLastModifiedDateFilterTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DateRange(self):  # pragma: no cover
        return SaaSProductLastModifiedDateFilterDateRange.make_one(
            self.boto3_raw_data["DateRange"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SaaSProductLastModifiedDateFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SaaSProductLastModifiedDateFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmiProductFilters:
    boto3_raw_data: "type_defs.AmiProductFiltersTypeDef" = dataclasses.field()

    @cached_property
    def EntityId(self):  # pragma: no cover
        return AmiProductEntityIdFilter.make_one(self.boto3_raw_data["EntityId"])

    @cached_property
    def LastModifiedDate(self):  # pragma: no cover
        return AmiProductLastModifiedDateFilter.make_one(
            self.boto3_raw_data["LastModifiedDate"]
        )

    @cached_property
    def ProductTitle(self):  # pragma: no cover
        return AmiProductTitleFilter.make_one(self.boto3_raw_data["ProductTitle"])

    @cached_property
    def Visibility(self):  # pragma: no cover
        return AmiProductVisibilityFilter.make_one(self.boto3_raw_data["Visibility"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AmiProductFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmiProductFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChangeSetResponse:
    boto3_raw_data: "type_defs.DescribeChangeSetResponseTypeDef" = dataclasses.field()

    ChangeSetId = field("ChangeSetId")
    ChangeSetArn = field("ChangeSetArn")
    ChangeSetName = field("ChangeSetName")
    Intent = field("Intent")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Status = field("Status")
    FailureCode = field("FailureCode")
    FailureDescription = field("FailureDescription")

    @cached_property
    def ChangeSet(self):  # pragma: no cover
        return ChangeSummary.make_many(self.boto3_raw_data["ChangeSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChangeSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChangeSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChangeSetRequest:
    boto3_raw_data: "type_defs.StartChangeSetRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")

    @cached_property
    def ChangeSet(self):  # pragma: no cover
        return Change.make_many(self.boto3_raw_data["ChangeSet"])

    ChangeSetName = field("ChangeSetName")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def ChangeSetTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["ChangeSetTags"])

    Intent = field("Intent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartChangeSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartChangeSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerProductFilters:
    boto3_raw_data: "type_defs.ContainerProductFiltersTypeDef" = dataclasses.field()

    @cached_property
    def EntityId(self):  # pragma: no cover
        return ContainerProductEntityIdFilter.make_one(self.boto3_raw_data["EntityId"])

    @cached_property
    def LastModifiedDate(self):  # pragma: no cover
        return ContainerProductLastModifiedDateFilter.make_one(
            self.boto3_raw_data["LastModifiedDate"]
        )

    @cached_property
    def ProductTitle(self):  # pragma: no cover
        return ContainerProductTitleFilter.make_one(self.boto3_raw_data["ProductTitle"])

    @cached_property
    def Visibility(self):  # pragma: no cover
        return ContainerProductVisibilityFilter.make_one(
            self.boto3_raw_data["Visibility"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContainerProductFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerProductFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductFilters:
    boto3_raw_data: "type_defs.DataProductFiltersTypeDef" = dataclasses.field()

    @cached_property
    def EntityId(self):  # pragma: no cover
        return DataProductEntityIdFilter.make_one(self.boto3_raw_data["EntityId"])

    @cached_property
    def ProductTitle(self):  # pragma: no cover
        return DataProductTitleFilter.make_one(self.boto3_raw_data["ProductTitle"])

    @cached_property
    def Visibility(self):  # pragma: no cover
        return DataProductVisibilityFilter.make_one(self.boto3_raw_data["Visibility"])

    @cached_property
    def LastModifiedDate(self):  # pragma: no cover
        return DataProductLastModifiedDateFilter.make_one(
            self.boto3_raw_data["LastModifiedDate"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProductFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesResponse:
    boto3_raw_data: "type_defs.ListEntitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def EntitySummaryList(self):  # pragma: no cover
        return EntitySummary.make_many(self.boto3_raw_data["EntitySummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MachineLearningProductFilters:
    boto3_raw_data: "type_defs.MachineLearningProductFiltersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EntityId(self):  # pragma: no cover
        return MachineLearningProductEntityIdFilter.make_one(
            self.boto3_raw_data["EntityId"]
        )

    @cached_property
    def LastModifiedDate(self):  # pragma: no cover
        return MachineLearningProductLastModifiedDateFilter.make_one(
            self.boto3_raw_data["LastModifiedDate"]
        )

    @cached_property
    def ProductTitle(self):  # pragma: no cover
        return MachineLearningProductTitleFilter.make_one(
            self.boto3_raw_data["ProductTitle"]
        )

    @cached_property
    def Visibility(self):  # pragma: no cover
        return MachineLearningProductVisibilityFilter.make_one(
            self.boto3_raw_data["Visibility"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MachineLearningProductFiltersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MachineLearningProductFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OfferFilters:
    boto3_raw_data: "type_defs.OfferFiltersTypeDef" = dataclasses.field()

    @cached_property
    def EntityId(self):  # pragma: no cover
        return OfferEntityIdFilter.make_one(self.boto3_raw_data["EntityId"])

    @cached_property
    def Name(self):  # pragma: no cover
        return OfferNameFilter.make_one(self.boto3_raw_data["Name"])

    @cached_property
    def ProductId(self):  # pragma: no cover
        return OfferProductIdFilter.make_one(self.boto3_raw_data["ProductId"])

    @cached_property
    def ResaleAuthorizationId(self):  # pragma: no cover
        return OfferResaleAuthorizationIdFilter.make_one(
            self.boto3_raw_data["ResaleAuthorizationId"]
        )

    @cached_property
    def ReleaseDate(self):  # pragma: no cover
        return OfferReleaseDateFilter.make_one(self.boto3_raw_data["ReleaseDate"])

    @cached_property
    def AvailabilityEndDate(self):  # pragma: no cover
        return OfferAvailabilityEndDateFilter.make_one(
            self.boto3_raw_data["AvailabilityEndDate"]
        )

    @cached_property
    def BuyerAccounts(self):  # pragma: no cover
        return OfferBuyerAccountsFilter.make_one(self.boto3_raw_data["BuyerAccounts"])

    @cached_property
    def State(self):  # pragma: no cover
        return OfferStateFilter.make_one(self.boto3_raw_data["State"])

    @cached_property
    def Targeting(self):  # pragma: no cover
        return OfferTargetingFilter.make_one(self.boto3_raw_data["Targeting"])

    @cached_property
    def LastModifiedDate(self):  # pragma: no cover
        return OfferLastModifiedDateFilter.make_one(
            self.boto3_raw_data["LastModifiedDate"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OfferFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OfferFiltersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResaleAuthorizationFilters:
    boto3_raw_data: "type_defs.ResaleAuthorizationFiltersTypeDef" = dataclasses.field()

    @cached_property
    def EntityId(self):  # pragma: no cover
        return ResaleAuthorizationEntityIdFilter.make_one(
            self.boto3_raw_data["EntityId"]
        )

    @cached_property
    def Name(self):  # pragma: no cover
        return ResaleAuthorizationNameFilter.make_one(self.boto3_raw_data["Name"])

    @cached_property
    def ProductId(self):  # pragma: no cover
        return ResaleAuthorizationProductIdFilter.make_one(
            self.boto3_raw_data["ProductId"]
        )

    @cached_property
    def CreatedDate(self):  # pragma: no cover
        return ResaleAuthorizationCreatedDateFilter.make_one(
            self.boto3_raw_data["CreatedDate"]
        )

    @cached_property
    def AvailabilityEndDate(self):  # pragma: no cover
        return ResaleAuthorizationAvailabilityEndDateFilter.make_one(
            self.boto3_raw_data["AvailabilityEndDate"]
        )

    @cached_property
    def ManufacturerAccountId(self):  # pragma: no cover
        return ResaleAuthorizationManufacturerAccountIdFilter.make_one(
            self.boto3_raw_data["ManufacturerAccountId"]
        )

    @cached_property
    def ProductName(self):  # pragma: no cover
        return ResaleAuthorizationProductNameFilter.make_one(
            self.boto3_raw_data["ProductName"]
        )

    @cached_property
    def ManufacturerLegalName(self):  # pragma: no cover
        return ResaleAuthorizationManufacturerLegalNameFilter.make_one(
            self.boto3_raw_data["ManufacturerLegalName"]
        )

    @cached_property
    def ResellerAccountID(self):  # pragma: no cover
        return ResaleAuthorizationResellerAccountIDFilter.make_one(
            self.boto3_raw_data["ResellerAccountID"]
        )

    @cached_property
    def ResellerLegalName(self):  # pragma: no cover
        return ResaleAuthorizationResellerLegalNameFilter.make_one(
            self.boto3_raw_data["ResellerLegalName"]
        )

    @cached_property
    def Status(self):  # pragma: no cover
        return ResaleAuthorizationStatusFilter.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def OfferExtendedStatus(self):  # pragma: no cover
        return ResaleAuthorizationOfferExtendedStatusFilter.make_one(
            self.boto3_raw_data["OfferExtendedStatus"]
        )

    @cached_property
    def LastModifiedDate(self):  # pragma: no cover
        return ResaleAuthorizationLastModifiedDateFilter.make_one(
            self.boto3_raw_data["LastModifiedDate"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResaleAuthorizationFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResaleAuthorizationFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SaaSProductFilters:
    boto3_raw_data: "type_defs.SaaSProductFiltersTypeDef" = dataclasses.field()

    @cached_property
    def EntityId(self):  # pragma: no cover
        return SaaSProductEntityIdFilter.make_one(self.boto3_raw_data["EntityId"])

    @cached_property
    def ProductTitle(self):  # pragma: no cover
        return SaaSProductTitleFilter.make_one(self.boto3_raw_data["ProductTitle"])

    @cached_property
    def Visibility(self):  # pragma: no cover
        return SaaSProductVisibilityFilter.make_one(self.boto3_raw_data["Visibility"])

    @cached_property
    def LastModifiedDate(self):  # pragma: no cover
        return SaaSProductLastModifiedDateFilter.make_one(
            self.boto3_raw_data["LastModifiedDate"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SaaSProductFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SaaSProductFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EntityTypeFilters:
    boto3_raw_data: "type_defs.EntityTypeFiltersTypeDef" = dataclasses.field()

    @cached_property
    def DataProductFilters(self):  # pragma: no cover
        return DataProductFilters.make_one(self.boto3_raw_data["DataProductFilters"])

    @cached_property
    def SaaSProductFilters(self):  # pragma: no cover
        return SaaSProductFilters.make_one(self.boto3_raw_data["SaaSProductFilters"])

    @cached_property
    def AmiProductFilters(self):  # pragma: no cover
        return AmiProductFilters.make_one(self.boto3_raw_data["AmiProductFilters"])

    @cached_property
    def OfferFilters(self):  # pragma: no cover
        return OfferFilters.make_one(self.boto3_raw_data["OfferFilters"])

    @cached_property
    def ContainerProductFilters(self):  # pragma: no cover
        return ContainerProductFilters.make_one(
            self.boto3_raw_data["ContainerProductFilters"]
        )

    @cached_property
    def ResaleAuthorizationFilters(self):  # pragma: no cover
        return ResaleAuthorizationFilters.make_one(
            self.boto3_raw_data["ResaleAuthorizationFilters"]
        )

    @cached_property
    def MachineLearningProductFilters(self):  # pragma: no cover
        return MachineLearningProductFilters.make_one(
            self.boto3_raw_data["MachineLearningProductFilters"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityTypeFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EntityTypeFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesRequestPaginate:
    boto3_raw_data: "type_defs.ListEntitiesRequestPaginateTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    EntityType = field("EntityType")

    @cached_property
    def FilterList(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["FilterList"])

    @cached_property
    def Sort(self):  # pragma: no cover
        return Sort.make_one(self.boto3_raw_data["Sort"])

    OwnershipType = field("OwnershipType")

    @cached_property
    def EntityTypeFilters(self):  # pragma: no cover
        return EntityTypeFilters.make_one(self.boto3_raw_data["EntityTypeFilters"])

    @cached_property
    def EntityTypeSort(self):  # pragma: no cover
        return EntityTypeSort.make_one(self.boto3_raw_data["EntityTypeSort"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntitiesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntitiesRequest:
    boto3_raw_data: "type_defs.ListEntitiesRequestTypeDef" = dataclasses.field()

    Catalog = field("Catalog")
    EntityType = field("EntityType")

    @cached_property
    def FilterList(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["FilterList"])

    @cached_property
    def Sort(self):  # pragma: no cover
        return Sort.make_one(self.boto3_raw_data["Sort"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    OwnershipType = field("OwnershipType")

    @cached_property
    def EntityTypeFilters(self):  # pragma: no cover
        return EntityTypeFilters.make_one(self.boto3_raw_data["EntityTypeFilters"])

    @cached_property
    def EntityTypeSort(self):  # pragma: no cover
        return EntityTypeSort.make_one(self.boto3_raw_data["EntityTypeSort"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
