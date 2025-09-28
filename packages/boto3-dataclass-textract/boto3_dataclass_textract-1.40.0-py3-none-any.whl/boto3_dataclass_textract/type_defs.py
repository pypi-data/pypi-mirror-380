# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_textract import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AdapterOverview:
    boto3_raw_data: "type_defs.AdapterOverviewTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")
    AdapterName = field("AdapterName")
    CreationTime = field("CreationTime")
    FeatureTypes = field("FeatureTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdapterOverviewTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdapterOverviewTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Adapter:
    boto3_raw_data: "type_defs.AdapterTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")
    Version = field("Version")
    Pages = field("Pages")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdapterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdapterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Object:
    boto3_raw_data: "type_defs.S3ObjectTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationMetric:
    boto3_raw_data: "type_defs.EvaluationMetricTypeDef" = dataclasses.field()

    F1Score = field("F1Score")
    Precision = field("Precision")
    Recall = field("Recall")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdapterVersionOverview:
    boto3_raw_data: "type_defs.AdapterVersionOverviewTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")
    AdapterVersion = field("AdapterVersion")
    CreationTime = field("CreationTime")
    FeatureTypes = field("FeatureTypes")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdapterVersionOverviewTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdapterVersionOverviewTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentMetadata:
    boto3_raw_data: "type_defs.DocumentMetadataTypeDef" = dataclasses.field()

    Pages = field("Pages")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HumanLoopActivationOutput:
    boto3_raw_data: "type_defs.HumanLoopActivationOutputTypeDef" = dataclasses.field()

    HumanLoopArn = field("HumanLoopArn")
    HumanLoopActivationReasons = field("HumanLoopActivationReasons")
    HumanLoopActivationConditionsEvaluationResults = field(
        "HumanLoopActivationConditionsEvaluationResults"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HumanLoopActivationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HumanLoopActivationOutputTypeDef"]
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
class NormalizedValue:
    boto3_raw_data: "type_defs.NormalizedValueTypeDef" = dataclasses.field()

    Value = field("Value")
    ValueType = field("ValueType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NormalizedValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NormalizedValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryOutput:
    boto3_raw_data: "type_defs.QueryOutputTypeDef" = dataclasses.field()

    Text = field("Text")
    Alias = field("Alias")
    Pages = field("Pages")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Relationship:
    boto3_raw_data: "type_defs.RelationshipTypeDef" = dataclasses.field()

    Type = field("Type")
    Ids = field("Ids")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelationshipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelationshipTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BoundingBox:
    boto3_raw_data: "type_defs.BoundingBoxTypeDef" = dataclasses.field()

    Width = field("Width")
    Height = field("Height")
    Left = field("Left")
    Top = field("Top")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BoundingBoxTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BoundingBoxTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAdapterRequest:
    boto3_raw_data: "type_defs.CreateAdapterRequestTypeDef" = dataclasses.field()

    AdapterName = field("AdapterName")
    FeatureTypes = field("FeatureTypes")
    ClientRequestToken = field("ClientRequestToken")
    Description = field("Description")
    AutoUpdate = field("AutoUpdate")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAdapterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAdapterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputConfig:
    boto3_raw_data: "type_defs.OutputConfigTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    S3Prefix = field("S3Prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAdapterRequest:
    boto3_raw_data: "type_defs.DeleteAdapterRequestTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAdapterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAdapterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAdapterVersionRequest:
    boto3_raw_data: "type_defs.DeleteAdapterVersionRequestTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")
    AdapterVersion = field("AdapterVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAdapterVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAdapterVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectedSignature:
    boto3_raw_data: "type_defs.DetectedSignatureTypeDef" = dataclasses.field()

    Page = field("Page")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DetectedSignatureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectedSignatureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SplitDocument:
    boto3_raw_data: "type_defs.SplitDocumentTypeDef" = dataclasses.field()

    Index = field("Index")
    Pages = field("Pages")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SplitDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SplitDocumentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UndetectedSignature:
    boto3_raw_data: "type_defs.UndetectedSignatureTypeDef" = dataclasses.field()

    Page = field("Page")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UndetectedSignatureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UndetectedSignatureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpenseCurrency:
    boto3_raw_data: "type_defs.ExpenseCurrencyTypeDef" = dataclasses.field()

    Code = field("Code")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpenseCurrencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExpenseCurrencyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpenseGroupProperty:
    boto3_raw_data: "type_defs.ExpenseGroupPropertyTypeDef" = dataclasses.field()

    Types = field("Types")
    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpenseGroupPropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpenseGroupPropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpenseType:
    boto3_raw_data: "type_defs.ExpenseTypeTypeDef" = dataclasses.field()

    Text = field("Text")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpenseTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExpenseTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Point:
    boto3_raw_data: "type_defs.PointTypeDef" = dataclasses.field()

    X = field("X")
    Y = field("Y")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAdapterRequest:
    boto3_raw_data: "type_defs.GetAdapterRequestTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAdapterRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdapterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAdapterVersionRequest:
    boto3_raw_data: "type_defs.GetAdapterVersionRequestTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")
    AdapterVersion = field("AdapterVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAdapterVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdapterVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentAnalysisRequest:
    boto3_raw_data: "type_defs.GetDocumentAnalysisRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentAnalysisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Warning:
    boto3_raw_data: "type_defs.WarningTypeDef" = dataclasses.field()

    ErrorCode = field("ErrorCode")
    Pages = field("Pages")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WarningTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WarningTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentTextDetectionRequest:
    boto3_raw_data: "type_defs.GetDocumentTextDetectionRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDocumentTextDetectionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentTextDetectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExpenseAnalysisRequest:
    boto3_raw_data: "type_defs.GetExpenseAnalysisRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExpenseAnalysisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExpenseAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLendingAnalysisRequest:
    boto3_raw_data: "type_defs.GetLendingAnalysisRequestTypeDef" = dataclasses.field()

    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLendingAnalysisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLendingAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLendingAnalysisSummaryRequest:
    boto3_raw_data: "type_defs.GetLendingAnalysisSummaryRequestTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLendingAnalysisSummaryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLendingAnalysisSummaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HumanLoopDataAttributes:
    boto3_raw_data: "type_defs.HumanLoopDataAttributesTypeDef" = dataclasses.field()

    ContentClassifiers = field("ContentClassifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HumanLoopDataAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HumanLoopDataAttributesTypeDef"]
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
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

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
class NotificationChannel:
    boto3_raw_data: "type_defs.NotificationChannelTypeDef" = dataclasses.field()

    SNSTopicArn = field("SNSTopicArn")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationChannelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationChannelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Prediction:
    boto3_raw_data: "type_defs.PredictionTypeDef" = dataclasses.field()

    Value = field("Value")
    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredictionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PredictionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Query:
    boto3_raw_data: "type_defs.QueryTypeDef" = dataclasses.field()

    Text = field("Text")
    Alias = field("Alias")
    Pages = field("Pages")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
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

    ResourceARN = field("ResourceARN")
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
class UpdateAdapterRequest:
    boto3_raw_data: "type_defs.UpdateAdapterRequestTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")
    Description = field("Description")
    AdapterName = field("AdapterName")
    AutoUpdate = field("AutoUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAdapterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAdapterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdaptersConfig:
    boto3_raw_data: "type_defs.AdaptersConfigTypeDef" = dataclasses.field()

    @cached_property
    def Adapters(self):  # pragma: no cover
        return Adapter.make_many(self.boto3_raw_data["Adapters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdaptersConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdaptersConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdapterVersionDatasetConfig:
    boto3_raw_data: "type_defs.AdapterVersionDatasetConfigTypeDef" = dataclasses.field()

    @cached_property
    def ManifestS3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["ManifestS3Object"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdapterVersionDatasetConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdapterVersionDatasetConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentLocation:
    boto3_raw_data: "type_defs.DocumentLocationTypeDef" = dataclasses.field()

    @cached_property
    def S3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["S3Object"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdapterVersionEvaluationMetric:
    boto3_raw_data: "type_defs.AdapterVersionEvaluationMetricTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Baseline(self):  # pragma: no cover
        return EvaluationMetric.make_one(self.boto3_raw_data["Baseline"])

    @cached_property
    def AdapterVersion(self):  # pragma: no cover
        return EvaluationMetric.make_one(self.boto3_raw_data["AdapterVersion"])

    FeatureType = field("FeatureType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AdapterVersionEvaluationMetricTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdapterVersionEvaluationMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAdapterResponse:
    boto3_raw_data: "type_defs.CreateAdapterResponseTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAdapterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAdapterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAdapterVersionResponse:
    boto3_raw_data: "type_defs.CreateAdapterVersionResponseTypeDef" = (
        dataclasses.field()
    )

    AdapterId = field("AdapterId")
    AdapterVersion = field("AdapterVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAdapterVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAdapterVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAdapterResponse:
    boto3_raw_data: "type_defs.GetAdapterResponseTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")
    AdapterName = field("AdapterName")
    CreationTime = field("CreationTime")
    Description = field("Description")
    FeatureTypes = field("FeatureTypes")
    AutoUpdate = field("AutoUpdate")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAdapterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdapterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAdapterVersionsResponse:
    boto3_raw_data: "type_defs.ListAdapterVersionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def AdapterVersions(self):  # pragma: no cover
        return AdapterVersionOverview.make_many(self.boto3_raw_data["AdapterVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAdapterVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAdapterVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAdaptersResponse:
    boto3_raw_data: "type_defs.ListAdaptersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Adapters(self):  # pragma: no cover
        return AdapterOverview.make_many(self.boto3_raw_data["Adapters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAdaptersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAdaptersResponseTypeDef"]
        ],
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
class StartDocumentAnalysisResponse:
    boto3_raw_data: "type_defs.StartDocumentAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDocumentAnalysisResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDocumentAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDocumentTextDetectionResponse:
    boto3_raw_data: "type_defs.StartDocumentTextDetectionResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDocumentTextDetectionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDocumentTextDetectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExpenseAnalysisResponse:
    boto3_raw_data: "type_defs.StartExpenseAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExpenseAnalysisResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExpenseAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLendingAnalysisResponse:
    boto3_raw_data: "type_defs.StartLendingAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLendingAnalysisResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLendingAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAdapterResponse:
    boto3_raw_data: "type_defs.UpdateAdapterResponseTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")
    AdapterName = field("AdapterName")
    CreationTime = field("CreationTime")
    Description = field("Description")
    FeatureTypes = field("FeatureTypes")
    AutoUpdate = field("AutoUpdate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAdapterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAdapterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzeIDDetections:
    boto3_raw_data: "type_defs.AnalyzeIDDetectionsTypeDef" = dataclasses.field()

    Text = field("Text")

    @cached_property
    def NormalizedValue(self):  # pragma: no cover
        return NormalizedValue.make_one(self.boto3_raw_data["NormalizedValue"])

    Confidence = field("Confidence")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyzeIDDetectionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzeIDDetectionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Document:
    boto3_raw_data: "type_defs.DocumentTypeDef" = dataclasses.field()

    Bytes = field("Bytes")

    @cached_property
    def S3Object(self):  # pragma: no cover
        return S3Object.make_one(self.boto3_raw_data["S3Object"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentGroup:
    boto3_raw_data: "type_defs.DocumentGroupTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def SplitDocuments(self):  # pragma: no cover
        return SplitDocument.make_many(self.boto3_raw_data["SplitDocuments"])

    @cached_property
    def DetectedSignatures(self):  # pragma: no cover
        return DetectedSignature.make_many(self.boto3_raw_data["DetectedSignatures"])

    @cached_property
    def UndetectedSignatures(self):  # pragma: no cover
        return UndetectedSignature.make_many(
            self.boto3_raw_data["UndetectedSignatures"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocumentGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocumentGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Geometry:
    boto3_raw_data: "type_defs.GeometryTypeDef" = dataclasses.field()

    @cached_property
    def BoundingBox(self):  # pragma: no cover
        return BoundingBox.make_one(self.boto3_raw_data["BoundingBox"])

    @cached_property
    def Polygon(self):  # pragma: no cover
        return Point.make_many(self.boto3_raw_data["Polygon"])

    RotationAngle = field("RotationAngle")

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
class HumanLoopConfig:
    boto3_raw_data: "type_defs.HumanLoopConfigTypeDef" = dataclasses.field()

    HumanLoopName = field("HumanLoopName")
    FlowDefinitionArn = field("FlowDefinitionArn")

    @cached_property
    def DataAttributes(self):  # pragma: no cover
        return HumanLoopDataAttributes.make_one(self.boto3_raw_data["DataAttributes"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HumanLoopConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HumanLoopConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAdapterVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListAdapterVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AdapterId = field("AdapterId")
    AfterCreationTime = field("AfterCreationTime")
    BeforeCreationTime = field("BeforeCreationTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAdapterVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAdapterVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAdapterVersionsRequest:
    boto3_raw_data: "type_defs.ListAdapterVersionsRequestTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")
    AfterCreationTime = field("AfterCreationTime")
    BeforeCreationTime = field("BeforeCreationTime")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAdapterVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAdapterVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAdaptersRequestPaginate:
    boto3_raw_data: "type_defs.ListAdaptersRequestPaginateTypeDef" = dataclasses.field()

    AfterCreationTime = field("AfterCreationTime")
    BeforeCreationTime = field("BeforeCreationTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAdaptersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAdaptersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAdaptersRequest:
    boto3_raw_data: "type_defs.ListAdaptersRequestTypeDef" = dataclasses.field()

    AfterCreationTime = field("AfterCreationTime")
    BeforeCreationTime = field("BeforeCreationTime")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAdaptersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAdaptersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PageClassification:
    boto3_raw_data: "type_defs.PageClassificationTypeDef" = dataclasses.field()

    @cached_property
    def PageType(self):  # pragma: no cover
        return Prediction.make_many(self.boto3_raw_data["PageType"])

    @cached_property
    def PageNumber(self):  # pragma: no cover
        return Prediction.make_many(self.boto3_raw_data["PageNumber"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PageClassificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PageClassificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAdapterVersionRequest:
    boto3_raw_data: "type_defs.CreateAdapterVersionRequestTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")

    @cached_property
    def DatasetConfig(self):  # pragma: no cover
        return AdapterVersionDatasetConfig.make_one(
            self.boto3_raw_data["DatasetConfig"]
        )

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return OutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    ClientRequestToken = field("ClientRequestToken")
    KMSKeyId = field("KMSKeyId")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAdapterVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAdapterVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDocumentTextDetectionRequest:
    boto3_raw_data: "type_defs.StartDocumentTextDetectionRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentLocation(self):  # pragma: no cover
        return DocumentLocation.make_one(self.boto3_raw_data["DocumentLocation"])

    ClientRequestToken = field("ClientRequestToken")
    JobTag = field("JobTag")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return OutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    KMSKeyId = field("KMSKeyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartDocumentTextDetectionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDocumentTextDetectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExpenseAnalysisRequest:
    boto3_raw_data: "type_defs.StartExpenseAnalysisRequestTypeDef" = dataclasses.field()

    @cached_property
    def DocumentLocation(self):  # pragma: no cover
        return DocumentLocation.make_one(self.boto3_raw_data["DocumentLocation"])

    ClientRequestToken = field("ClientRequestToken")
    JobTag = field("JobTag")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return OutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    KMSKeyId = field("KMSKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExpenseAnalysisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExpenseAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLendingAnalysisRequest:
    boto3_raw_data: "type_defs.StartLendingAnalysisRequestTypeDef" = dataclasses.field()

    @cached_property
    def DocumentLocation(self):  # pragma: no cover
        return DocumentLocation.make_one(self.boto3_raw_data["DocumentLocation"])

    ClientRequestToken = field("ClientRequestToken")
    JobTag = field("JobTag")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return OutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    KMSKeyId = field("KMSKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLendingAnalysisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLendingAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAdapterVersionResponse:
    boto3_raw_data: "type_defs.GetAdapterVersionResponseTypeDef" = dataclasses.field()

    AdapterId = field("AdapterId")
    AdapterVersion = field("AdapterVersion")
    CreationTime = field("CreationTime")
    FeatureTypes = field("FeatureTypes")
    Status = field("Status")
    StatusMessage = field("StatusMessage")

    @cached_property
    def DatasetConfig(self):  # pragma: no cover
        return AdapterVersionDatasetConfig.make_one(
            self.boto3_raw_data["DatasetConfig"]
        )

    KMSKeyId = field("KMSKeyId")

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return OutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    @cached_property
    def EvaluationMetrics(self):  # pragma: no cover
        return AdapterVersionEvaluationMetric.make_many(
            self.boto3_raw_data["EvaluationMetrics"]
        )

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAdapterVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAdapterVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityDocumentField:
    boto3_raw_data: "type_defs.IdentityDocumentFieldTypeDef" = dataclasses.field()

    @cached_property
    def Type(self):  # pragma: no cover
        return AnalyzeIDDetections.make_one(self.boto3_raw_data["Type"])

    @cached_property
    def ValueDetection(self):  # pragma: no cover
        return AnalyzeIDDetections.make_one(self.boto3_raw_data["ValueDetection"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityDocumentFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityDocumentFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzeExpenseRequest:
    boto3_raw_data: "type_defs.AnalyzeExpenseRequestTypeDef" = dataclasses.field()

    @cached_property
    def Document(self):  # pragma: no cover
        return Document.make_one(self.boto3_raw_data["Document"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyzeExpenseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzeExpenseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzeIDRequest:
    boto3_raw_data: "type_defs.AnalyzeIDRequestTypeDef" = dataclasses.field()

    @cached_property
    def DocumentPages(self):  # pragma: no cover
        return Document.make_many(self.boto3_raw_data["DocumentPages"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalyzeIDRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzeIDRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectDocumentTextRequest:
    boto3_raw_data: "type_defs.DetectDocumentTextRequestTypeDef" = dataclasses.field()

    @cached_property
    def Document(self):  # pragma: no cover
        return Document.make_one(self.boto3_raw_data["Document"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectDocumentTextRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectDocumentTextRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LendingSummary:
    boto3_raw_data: "type_defs.LendingSummaryTypeDef" = dataclasses.field()

    @cached_property
    def DocumentGroups(self):  # pragma: no cover
        return DocumentGroup.make_many(self.boto3_raw_data["DocumentGroups"])

    UndetectedDocumentTypes = field("UndetectedDocumentTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LendingSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LendingSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Block:
    boto3_raw_data: "type_defs.BlockTypeDef" = dataclasses.field()

    BlockType = field("BlockType")
    Confidence = field("Confidence")
    Text = field("Text")
    TextType = field("TextType")
    RowIndex = field("RowIndex")
    ColumnIndex = field("ColumnIndex")
    RowSpan = field("RowSpan")
    ColumnSpan = field("ColumnSpan")

    @cached_property
    def Geometry(self):  # pragma: no cover
        return Geometry.make_one(self.boto3_raw_data["Geometry"])

    Id = field("Id")

    @cached_property
    def Relationships(self):  # pragma: no cover
        return Relationship.make_many(self.boto3_raw_data["Relationships"])

    EntityTypes = field("EntityTypes")
    SelectionStatus = field("SelectionStatus")
    Page = field("Page")

    @cached_property
    def Query(self):  # pragma: no cover
        return QueryOutput.make_one(self.boto3_raw_data["Query"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlockTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlockTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpenseDetection:
    boto3_raw_data: "type_defs.ExpenseDetectionTypeDef" = dataclasses.field()

    Text = field("Text")

    @cached_property
    def Geometry(self):  # pragma: no cover
        return Geometry.make_one(self.boto3_raw_data["Geometry"])

    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpenseDetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpenseDetectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LendingDetection:
    boto3_raw_data: "type_defs.LendingDetectionTypeDef" = dataclasses.field()

    Text = field("Text")
    SelectionStatus = field("SelectionStatus")

    @cached_property
    def Geometry(self):  # pragma: no cover
        return Geometry.make_one(self.boto3_raw_data["Geometry"])

    Confidence = field("Confidence")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LendingDetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LendingDetectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignatureDetection:
    boto3_raw_data: "type_defs.SignatureDetectionTypeDef" = dataclasses.field()

    Confidence = field("Confidence")

    @cached_property
    def Geometry(self):  # pragma: no cover
        return Geometry.make_one(self.boto3_raw_data["Geometry"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignatureDetectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignatureDetectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueriesConfig:
    boto3_raw_data: "type_defs.QueriesConfigTypeDef" = dataclasses.field()

    Queries = field("Queries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueriesConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueriesConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLendingAnalysisSummaryResponse:
    boto3_raw_data: "type_defs.GetLendingAnalysisSummaryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    JobStatus = field("JobStatus")

    @cached_property
    def Summary(self):  # pragma: no cover
        return LendingSummary.make_one(self.boto3_raw_data["Summary"])

    @cached_property
    def Warnings(self):  # pragma: no cover
        return Warning.make_many(self.boto3_raw_data["Warnings"])

    StatusMessage = field("StatusMessage")
    AnalyzeLendingModelVersion = field("AnalyzeLendingModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLendingAnalysisSummaryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLendingAnalysisSummaryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzeDocumentResponse:
    boto3_raw_data: "type_defs.AnalyzeDocumentResponseTypeDef" = dataclasses.field()

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    @cached_property
    def Blocks(self):  # pragma: no cover
        return Block.make_many(self.boto3_raw_data["Blocks"])

    @cached_property
    def HumanLoopActivationOutput(self):  # pragma: no cover
        return HumanLoopActivationOutput.make_one(
            self.boto3_raw_data["HumanLoopActivationOutput"]
        )

    AnalyzeDocumentModelVersion = field("AnalyzeDocumentModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyzeDocumentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzeDocumentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectDocumentTextResponse:
    boto3_raw_data: "type_defs.DetectDocumentTextResponseTypeDef" = dataclasses.field()

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    @cached_property
    def Blocks(self):  # pragma: no cover
        return Block.make_many(self.boto3_raw_data["Blocks"])

    DetectDocumentTextModelVersion = field("DetectDocumentTextModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectDocumentTextResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectDocumentTextResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentAnalysisResponse:
    boto3_raw_data: "type_defs.GetDocumentAnalysisResponseTypeDef" = dataclasses.field()

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    JobStatus = field("JobStatus")

    @cached_property
    def Blocks(self):  # pragma: no cover
        return Block.make_many(self.boto3_raw_data["Blocks"])

    @cached_property
    def Warnings(self):  # pragma: no cover
        return Warning.make_many(self.boto3_raw_data["Warnings"])

    StatusMessage = field("StatusMessage")
    AnalyzeDocumentModelVersion = field("AnalyzeDocumentModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDocumentAnalysisResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDocumentTextDetectionResponse:
    boto3_raw_data: "type_defs.GetDocumentTextDetectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    JobStatus = field("JobStatus")

    @cached_property
    def Blocks(self):  # pragma: no cover
        return Block.make_many(self.boto3_raw_data["Blocks"])

    @cached_property
    def Warnings(self):  # pragma: no cover
        return Warning.make_many(self.boto3_raw_data["Warnings"])

    StatusMessage = field("StatusMessage")
    DetectDocumentTextModelVersion = field("DetectDocumentTextModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDocumentTextDetectionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDocumentTextDetectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityDocument:
    boto3_raw_data: "type_defs.IdentityDocumentTypeDef" = dataclasses.field()

    DocumentIndex = field("DocumentIndex")

    @cached_property
    def IdentityDocumentFields(self):  # pragma: no cover
        return IdentityDocumentField.make_many(
            self.boto3_raw_data["IdentityDocumentFields"]
        )

    @cached_property
    def Blocks(self):  # pragma: no cover
        return Block.make_many(self.boto3_raw_data["Blocks"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdentityDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpenseField:
    boto3_raw_data: "type_defs.ExpenseFieldTypeDef" = dataclasses.field()

    @cached_property
    def Type(self):  # pragma: no cover
        return ExpenseType.make_one(self.boto3_raw_data["Type"])

    @cached_property
    def LabelDetection(self):  # pragma: no cover
        return ExpenseDetection.make_one(self.boto3_raw_data["LabelDetection"])

    @cached_property
    def ValueDetection(self):  # pragma: no cover
        return ExpenseDetection.make_one(self.boto3_raw_data["ValueDetection"])

    PageNumber = field("PageNumber")

    @cached_property
    def Currency(self):  # pragma: no cover
        return ExpenseCurrency.make_one(self.boto3_raw_data["Currency"])

    @cached_property
    def GroupProperties(self):  # pragma: no cover
        return ExpenseGroupProperty.make_many(self.boto3_raw_data["GroupProperties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpenseFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExpenseFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LendingField:
    boto3_raw_data: "type_defs.LendingFieldTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def KeyDetection(self):  # pragma: no cover
        return LendingDetection.make_one(self.boto3_raw_data["KeyDetection"])

    @cached_property
    def ValueDetections(self):  # pragma: no cover
        return LendingDetection.make_many(self.boto3_raw_data["ValueDetections"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LendingFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LendingFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzeDocumentRequest:
    boto3_raw_data: "type_defs.AnalyzeDocumentRequestTypeDef" = dataclasses.field()

    @cached_property
    def Document(self):  # pragma: no cover
        return Document.make_one(self.boto3_raw_data["Document"])

    FeatureTypes = field("FeatureTypes")

    @cached_property
    def HumanLoopConfig(self):  # pragma: no cover
        return HumanLoopConfig.make_one(self.boto3_raw_data["HumanLoopConfig"])

    @cached_property
    def QueriesConfig(self):  # pragma: no cover
        return QueriesConfig.make_one(self.boto3_raw_data["QueriesConfig"])

    @cached_property
    def AdaptersConfig(self):  # pragma: no cover
        return AdaptersConfig.make_one(self.boto3_raw_data["AdaptersConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyzeDocumentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzeDocumentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDocumentAnalysisRequest:
    boto3_raw_data: "type_defs.StartDocumentAnalysisRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DocumentLocation(self):  # pragma: no cover
        return DocumentLocation.make_one(self.boto3_raw_data["DocumentLocation"])

    FeatureTypes = field("FeatureTypes")
    ClientRequestToken = field("ClientRequestToken")
    JobTag = field("JobTag")

    @cached_property
    def NotificationChannel(self):  # pragma: no cover
        return NotificationChannel.make_one(self.boto3_raw_data["NotificationChannel"])

    @cached_property
    def OutputConfig(self):  # pragma: no cover
        return OutputConfig.make_one(self.boto3_raw_data["OutputConfig"])

    KMSKeyId = field("KMSKeyId")

    @cached_property
    def QueriesConfig(self):  # pragma: no cover
        return QueriesConfig.make_one(self.boto3_raw_data["QueriesConfig"])

    @cached_property
    def AdaptersConfig(self):  # pragma: no cover
        return AdaptersConfig.make_one(self.boto3_raw_data["AdaptersConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDocumentAnalysisRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDocumentAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzeIDResponse:
    boto3_raw_data: "type_defs.AnalyzeIDResponseTypeDef" = dataclasses.field()

    @cached_property
    def IdentityDocuments(self):  # pragma: no cover
        return IdentityDocument.make_many(self.boto3_raw_data["IdentityDocuments"])

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    AnalyzeIDModelVersion = field("AnalyzeIDModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalyzeIDResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzeIDResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineItemFields:
    boto3_raw_data: "type_defs.LineItemFieldsTypeDef" = dataclasses.field()

    @cached_property
    def LineItemExpenseFields(self):  # pragma: no cover
        return ExpenseField.make_many(self.boto3_raw_data["LineItemExpenseFields"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LineItemFieldsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LineItemFieldsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LendingDocument:
    boto3_raw_data: "type_defs.LendingDocumentTypeDef" = dataclasses.field()

    @cached_property
    def LendingFields(self):  # pragma: no cover
        return LendingField.make_many(self.boto3_raw_data["LendingFields"])

    @cached_property
    def SignatureDetections(self):  # pragma: no cover
        return SignatureDetection.make_many(self.boto3_raw_data["SignatureDetections"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LendingDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LendingDocumentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineItemGroup:
    boto3_raw_data: "type_defs.LineItemGroupTypeDef" = dataclasses.field()

    LineItemGroupIndex = field("LineItemGroupIndex")

    @cached_property
    def LineItems(self):  # pragma: no cover
        return LineItemFields.make_many(self.boto3_raw_data["LineItems"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LineItemGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LineItemGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpenseDocument:
    boto3_raw_data: "type_defs.ExpenseDocumentTypeDef" = dataclasses.field()

    ExpenseIndex = field("ExpenseIndex")

    @cached_property
    def SummaryFields(self):  # pragma: no cover
        return ExpenseField.make_many(self.boto3_raw_data["SummaryFields"])

    @cached_property
    def LineItemGroups(self):  # pragma: no cover
        return LineItemGroup.make_many(self.boto3_raw_data["LineItemGroups"])

    @cached_property
    def Blocks(self):  # pragma: no cover
        return Block.make_many(self.boto3_raw_data["Blocks"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpenseDocumentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExpenseDocumentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyzeExpenseResponse:
    boto3_raw_data: "type_defs.AnalyzeExpenseResponseTypeDef" = dataclasses.field()

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    @cached_property
    def ExpenseDocuments(self):  # pragma: no cover
        return ExpenseDocument.make_many(self.boto3_raw_data["ExpenseDocuments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyzeExpenseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyzeExpenseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Extraction:
    boto3_raw_data: "type_defs.ExtractionTypeDef" = dataclasses.field()

    @cached_property
    def LendingDocument(self):  # pragma: no cover
        return LendingDocument.make_one(self.boto3_raw_data["LendingDocument"])

    @cached_property
    def ExpenseDocument(self):  # pragma: no cover
        return ExpenseDocument.make_one(self.boto3_raw_data["ExpenseDocument"])

    @cached_property
    def IdentityDocument(self):  # pragma: no cover
        return IdentityDocument.make_one(self.boto3_raw_data["IdentityDocument"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtractionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExtractionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExpenseAnalysisResponse:
    boto3_raw_data: "type_defs.GetExpenseAnalysisResponseTypeDef" = dataclasses.field()

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    JobStatus = field("JobStatus")

    @cached_property
    def ExpenseDocuments(self):  # pragma: no cover
        return ExpenseDocument.make_many(self.boto3_raw_data["ExpenseDocuments"])

    @cached_property
    def Warnings(self):  # pragma: no cover
        return Warning.make_many(self.boto3_raw_data["Warnings"])

    StatusMessage = field("StatusMessage")
    AnalyzeExpenseModelVersion = field("AnalyzeExpenseModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExpenseAnalysisResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExpenseAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LendingResult:
    boto3_raw_data: "type_defs.LendingResultTypeDef" = dataclasses.field()

    Page = field("Page")

    @cached_property
    def PageClassification(self):  # pragma: no cover
        return PageClassification.make_one(self.boto3_raw_data["PageClassification"])

    @cached_property
    def Extractions(self):  # pragma: no cover
        return Extraction.make_many(self.boto3_raw_data["Extractions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LendingResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LendingResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLendingAnalysisResponse:
    boto3_raw_data: "type_defs.GetLendingAnalysisResponseTypeDef" = dataclasses.field()

    @cached_property
    def DocumentMetadata(self):  # pragma: no cover
        return DocumentMetadata.make_one(self.boto3_raw_data["DocumentMetadata"])

    JobStatus = field("JobStatus")

    @cached_property
    def Results(self):  # pragma: no cover
        return LendingResult.make_many(self.boto3_raw_data["Results"])

    @cached_property
    def Warnings(self):  # pragma: no cover
        return Warning.make_many(self.boto3_raw_data["Warnings"])

    StatusMessage = field("StatusMessage")
    AnalyzeLendingModelVersion = field("AnalyzeLendingModelVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLendingAnalysisResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLendingAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
