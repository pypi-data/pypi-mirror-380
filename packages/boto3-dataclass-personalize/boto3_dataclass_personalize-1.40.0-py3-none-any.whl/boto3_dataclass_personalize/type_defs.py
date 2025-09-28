# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_personalize import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AlgorithmImage:
    boto3_raw_data: "type_defs.AlgorithmImageTypeDef" = dataclasses.field()

    dockerURI = field("dockerURI")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlgorithmImageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlgorithmImageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoMLConfigOutput:
    boto3_raw_data: "type_defs.AutoMLConfigOutputTypeDef" = dataclasses.field()

    metricName = field("metricName")
    recipeList = field("recipeList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoMLConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoMLConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoMLConfig:
    boto3_raw_data: "type_defs.AutoMLConfigTypeDef" = dataclasses.field()

    metricName = field("metricName")
    recipeList = field("recipeList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoMLConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoMLConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoMLResult:
    boto3_raw_data: "type_defs.AutoMLResultTypeDef" = dataclasses.field()

    bestRecipeArn = field("bestRecipeArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoMLResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoMLResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoTrainingConfig:
    boto3_raw_data: "type_defs.AutoTrainingConfigTypeDef" = dataclasses.field()

    schedulingExpression = field("schedulingExpression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoTrainingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoTrainingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchInferenceJobConfigOutput:
    boto3_raw_data: "type_defs.BatchInferenceJobConfigOutputTypeDef" = (
        dataclasses.field()
    )

    itemExplorationConfig = field("itemExplorationConfig")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchInferenceJobConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchInferenceJobConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchInferenceJobConfig:
    boto3_raw_data: "type_defs.BatchInferenceJobConfigTypeDef" = dataclasses.field()

    itemExplorationConfig = field("itemExplorationConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchInferenceJobConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchInferenceJobConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataConfig:
    boto3_raw_data: "type_defs.S3DataConfigTypeDef" = dataclasses.field()

    path = field("path")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DataConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3DataConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchInferenceJobSummary:
    boto3_raw_data: "type_defs.BatchInferenceJobSummaryTypeDef" = dataclasses.field()

    batchInferenceJobArn = field("batchInferenceJobArn")
    jobName = field("jobName")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")
    solutionVersionArn = field("solutionVersionArn")
    batchInferenceJobMode = field("batchInferenceJobMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchInferenceJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchInferenceJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchSegmentJobSummary:
    boto3_raw_data: "type_defs.BatchSegmentJobSummaryTypeDef" = dataclasses.field()

    batchSegmentJobArn = field("batchSegmentJobArn")
    jobName = field("jobName")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")
    solutionVersionArn = field("solutionVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchSegmentJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchSegmentJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignConfigOutput:
    boto3_raw_data: "type_defs.CampaignConfigOutputTypeDef" = dataclasses.field()

    itemExplorationConfig = field("itemExplorationConfig")
    enableMetadataWithRecommendations = field("enableMetadataWithRecommendations")
    syncWithLatestSolutionVersion = field("syncWithLatestSolutionVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CampaignConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignConfig:
    boto3_raw_data: "type_defs.CampaignConfigTypeDef" = dataclasses.field()

    itemExplorationConfig = field("itemExplorationConfig")
    enableMetadataWithRecommendations = field("enableMetadataWithRecommendations")
    syncWithLatestSolutionVersion = field("syncWithLatestSolutionVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CampaignConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignSummary:
    boto3_raw_data: "type_defs.CampaignSummaryTypeDef" = dataclasses.field()

    name = field("name")
    campaignArn = field("campaignArn")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CampaignSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CategoricalHyperParameterRangeOutput:
    boto3_raw_data: "type_defs.CategoricalHyperParameterRangeOutputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CategoricalHyperParameterRangeOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CategoricalHyperParameterRangeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CategoricalHyperParameterRange:
    boto3_raw_data: "type_defs.CategoricalHyperParameterRangeTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CategoricalHyperParameterRangeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CategoricalHyperParameterRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinuousHyperParameterRange:
    boto3_raw_data: "type_defs.ContinuousHyperParameterRangeTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    minValue = field("minValue")
    maxValue = field("maxValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ContinuousHyperParameterRangeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinuousHyperParameterRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    tagKey = field("tagKey")
    tagValue = field("tagValue")

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
class DataSource:
    boto3_raw_data: "type_defs.DataSourceTypeDef" = dataclasses.field()

    dataLocation = field("dataLocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricAttribute:
    boto3_raw_data: "type_defs.MetricAttributeTypeDef" = dataclasses.field()

    eventType = field("eventType")
    metricName = field("metricName")
    expression = field("expression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSchemaRequest:
    boto3_raw_data: "type_defs.CreateSchemaRequestTypeDef" = dataclasses.field()

    name = field("name")
    schema = field("schema")
    domain = field("domain")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataDeletionJobSummary:
    boto3_raw_data: "type_defs.DataDeletionJobSummaryTypeDef" = dataclasses.field()

    dataDeletionJobArn = field("dataDeletionJobArn")
    datasetGroupArn = field("datasetGroupArn")
    jobName = field("jobName")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataDeletionJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataDeletionJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetExportJobSummary:
    boto3_raw_data: "type_defs.DatasetExportJobSummaryTypeDef" = dataclasses.field()

    datasetExportJobArn = field("datasetExportJobArn")
    jobName = field("jobName")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetExportJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetExportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetGroupSummary:
    boto3_raw_data: "type_defs.DatasetGroupSummaryTypeDef" = dataclasses.field()

    name = field("name")
    datasetGroupArn = field("datasetGroupArn")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")
    domain = field("domain")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetGroupSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetGroupSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetGroup:
    boto3_raw_data: "type_defs.DatasetGroupTypeDef" = dataclasses.field()

    name = field("name")
    datasetGroupArn = field("datasetGroupArn")
    status = field("status")
    roleArn = field("roleArn")
    kmsKeyArn = field("kmsKeyArn")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")
    domain = field("domain")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetImportJobSummary:
    boto3_raw_data: "type_defs.DatasetImportJobSummaryTypeDef" = dataclasses.field()

    datasetImportJobArn = field("datasetImportJobArn")
    jobName = field("jobName")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")
    importMode = field("importMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetImportJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetImportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetSchemaSummary:
    boto3_raw_data: "type_defs.DatasetSchemaSummaryTypeDef" = dataclasses.field()

    name = field("name")
    schemaArn = field("schemaArn")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    domain = field("domain")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetSchemaSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetSchemaSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetSchema:
    boto3_raw_data: "type_defs.DatasetSchemaTypeDef" = dataclasses.field()

    name = field("name")
    schemaArn = field("schemaArn")
    schema = field("schema")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    domain = field("domain")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetSchemaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetSummary:
    boto3_raw_data: "type_defs.DatasetSummaryTypeDef" = dataclasses.field()

    name = field("name")
    datasetArn = field("datasetArn")
    datasetType = field("datasetType")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetUpdateSummary:
    boto3_raw_data: "type_defs.DatasetUpdateSummaryTypeDef" = dataclasses.field()

    schemaArn = field("schemaArn")
    status = field("status")
    failureReason = field("failureReason")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetUpdateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetUpdateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultCategoricalHyperParameterRange:
    boto3_raw_data: "type_defs.DefaultCategoricalHyperParameterRangeTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    values = field("values")
    isTunable = field("isTunable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DefaultCategoricalHyperParameterRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultCategoricalHyperParameterRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultContinuousHyperParameterRange:
    boto3_raw_data: "type_defs.DefaultContinuousHyperParameterRangeTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    minValue = field("minValue")
    maxValue = field("maxValue")
    isTunable = field("isTunable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DefaultContinuousHyperParameterRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultContinuousHyperParameterRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultIntegerHyperParameterRange:
    boto3_raw_data: "type_defs.DefaultIntegerHyperParameterRangeTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    minValue = field("minValue")
    maxValue = field("maxValue")
    isTunable = field("isTunable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DefaultIntegerHyperParameterRangeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultIntegerHyperParameterRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCampaignRequest:
    boto3_raw_data: "type_defs.DeleteCampaignRequestTypeDef" = dataclasses.field()

    campaignArn = field("campaignArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetGroupRequest:
    boto3_raw_data: "type_defs.DeleteDatasetGroupRequestTypeDef" = dataclasses.field()

    datasetGroupArn = field("datasetGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDatasetRequest:
    boto3_raw_data: "type_defs.DeleteDatasetRequestTypeDef" = dataclasses.field()

    datasetArn = field("datasetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventTrackerRequest:
    boto3_raw_data: "type_defs.DeleteEventTrackerRequestTypeDef" = dataclasses.field()

    eventTrackerArn = field("eventTrackerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventTrackerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventTrackerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFilterRequest:
    boto3_raw_data: "type_defs.DeleteFilterRequestTypeDef" = dataclasses.field()

    filterArn = field("filterArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMetricAttributionRequest:
    boto3_raw_data: "type_defs.DeleteMetricAttributionRequestTypeDef" = (
        dataclasses.field()
    )

    metricAttributionArn = field("metricAttributionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMetricAttributionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMetricAttributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRecommenderRequest:
    boto3_raw_data: "type_defs.DeleteRecommenderRequestTypeDef" = dataclasses.field()

    recommenderArn = field("recommenderArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRecommenderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRecommenderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSchemaRequest:
    boto3_raw_data: "type_defs.DeleteSchemaRequestTypeDef" = dataclasses.field()

    schemaArn = field("schemaArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSolutionRequest:
    boto3_raw_data: "type_defs.DeleteSolutionRequestTypeDef" = dataclasses.field()

    solutionArn = field("solutionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSolutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSolutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlgorithmRequest:
    boto3_raw_data: "type_defs.DescribeAlgorithmRequestTypeDef" = dataclasses.field()

    algorithmArn = field("algorithmArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlgorithmRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlgorithmRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBatchInferenceJobRequest:
    boto3_raw_data: "type_defs.DescribeBatchInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    batchInferenceJobArn = field("batchInferenceJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBatchInferenceJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBatchInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBatchSegmentJobRequest:
    boto3_raw_data: "type_defs.DescribeBatchSegmentJobRequestTypeDef" = (
        dataclasses.field()
    )

    batchSegmentJobArn = field("batchSegmentJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBatchSegmentJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBatchSegmentJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCampaignRequest:
    boto3_raw_data: "type_defs.DescribeCampaignRequestTypeDef" = dataclasses.field()

    campaignArn = field("campaignArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataDeletionJobRequest:
    boto3_raw_data: "type_defs.DescribeDataDeletionJobRequestTypeDef" = (
        dataclasses.field()
    )

    dataDeletionJobArn = field("dataDeletionJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDataDeletionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataDeletionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetExportJobRequest:
    boto3_raw_data: "type_defs.DescribeDatasetExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    datasetExportJobArn = field("datasetExportJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDatasetExportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetGroupRequest:
    boto3_raw_data: "type_defs.DescribeDatasetGroupRequestTypeDef" = dataclasses.field()

    datasetGroupArn = field("datasetGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetImportJobRequest:
    boto3_raw_data: "type_defs.DescribeDatasetImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    datasetImportJobArn = field("datasetImportJobArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDatasetImportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetRequest:
    boto3_raw_data: "type_defs.DescribeDatasetRequestTypeDef" = dataclasses.field()

    datasetArn = field("datasetArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventTrackerRequest:
    boto3_raw_data: "type_defs.DescribeEventTrackerRequestTypeDef" = dataclasses.field()

    eventTrackerArn = field("eventTrackerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventTrackerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventTrackerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTracker:
    boto3_raw_data: "type_defs.EventTrackerTypeDef" = dataclasses.field()

    name = field("name")
    eventTrackerArn = field("eventTrackerArn")
    accountId = field("accountId")
    trackingId = field("trackingId")
    datasetGroupArn = field("datasetGroupArn")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTrackerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTrackerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFeatureTransformationRequest:
    boto3_raw_data: "type_defs.DescribeFeatureTransformationRequestTypeDef" = (
        dataclasses.field()
    )

    featureTransformationArn = field("featureTransformationArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFeatureTransformationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFeatureTransformationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FeatureTransformation:
    boto3_raw_data: "type_defs.FeatureTransformationTypeDef" = dataclasses.field()

    name = field("name")
    featureTransformationArn = field("featureTransformationArn")
    defaultParameters = field("defaultParameters")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FeatureTransformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FeatureTransformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFilterRequest:
    boto3_raw_data: "type_defs.DescribeFilterRequestTypeDef" = dataclasses.field()

    filterArn = field("filterArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFilterRequestTypeDef"]
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

    name = field("name")
    filterArn = field("filterArn")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    datasetGroupArn = field("datasetGroupArn")
    failureReason = field("failureReason")
    filterExpression = field("filterExpression")
    status = field("status")

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
class DescribeMetricAttributionRequest:
    boto3_raw_data: "type_defs.DescribeMetricAttributionRequestTypeDef" = (
        dataclasses.field()
    )

    metricAttributionArn = field("metricAttributionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMetricAttributionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetricAttributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecipeRequest:
    boto3_raw_data: "type_defs.DescribeRecipeRequestTypeDef" = dataclasses.field()

    recipeArn = field("recipeArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRecipeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecipeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recipe:
    boto3_raw_data: "type_defs.RecipeTypeDef" = dataclasses.field()

    name = field("name")
    recipeArn = field("recipeArn")
    algorithmArn = field("algorithmArn")
    featureTransformationArn = field("featureTransformationArn")
    status = field("status")
    description = field("description")
    creationDateTime = field("creationDateTime")
    recipeType = field("recipeType")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecipeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecipeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecommenderRequest:
    boto3_raw_data: "type_defs.DescribeRecommenderRequestTypeDef" = dataclasses.field()

    recommenderArn = field("recommenderArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRecommenderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecommenderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSchemaRequest:
    boto3_raw_data: "type_defs.DescribeSchemaRequestTypeDef" = dataclasses.field()

    schemaArn = field("schemaArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSolutionRequest:
    boto3_raw_data: "type_defs.DescribeSolutionRequestTypeDef" = dataclasses.field()

    solutionArn = field("solutionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSolutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSolutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSolutionVersionRequest:
    boto3_raw_data: "type_defs.DescribeSolutionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    solutionVersionArn = field("solutionVersionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSolutionVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSolutionVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventParameters:
    boto3_raw_data: "type_defs.EventParametersTypeDef" = dataclasses.field()

    eventType = field("eventType")
    eventValueThreshold = field("eventValueThreshold")
    weight = field("weight")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTrackerSummary:
    boto3_raw_data: "type_defs.EventTrackerSummaryTypeDef" = dataclasses.field()

    name = field("name")
    eventTrackerArn = field("eventTrackerArn")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventTrackerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventTrackerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldsForThemeGeneration:
    boto3_raw_data: "type_defs.FieldsForThemeGenerationTypeDef" = dataclasses.field()

    itemName = field("itemName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldsForThemeGenerationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldsForThemeGenerationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterSummary:
    boto3_raw_data: "type_defs.FilterSummaryTypeDef" = dataclasses.field()

    name = field("name")
    filterArn = field("filterArn")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    datasetGroupArn = field("datasetGroupArn")
    failureReason = field("failureReason")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolutionMetricsRequest:
    boto3_raw_data: "type_defs.GetSolutionMetricsRequestTypeDef" = dataclasses.field()

    solutionVersionArn = field("solutionVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolutionMetricsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolutionMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HPOObjective:
    boto3_raw_data: "type_defs.HPOObjectiveTypeDef" = dataclasses.field()

    type = field("type")
    metricName = field("metricName")
    metricRegex = field("metricRegex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HPOObjectiveTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HPOObjectiveTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HPOResourceConfig:
    boto3_raw_data: "type_defs.HPOResourceConfigTypeDef" = dataclasses.field()

    maxNumberOfTrainingJobs = field("maxNumberOfTrainingJobs")
    maxParallelTrainingJobs = field("maxParallelTrainingJobs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HPOResourceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HPOResourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegerHyperParameterRange:
    boto3_raw_data: "type_defs.IntegerHyperParameterRangeTypeDef" = dataclasses.field()

    name = field("name")
    minValue = field("minValue")
    maxValue = field("maxValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegerHyperParameterRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegerHyperParameterRangeTypeDef"]
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
class ListBatchInferenceJobsRequest:
    boto3_raw_data: "type_defs.ListBatchInferenceJobsRequestTypeDef" = (
        dataclasses.field()
    )

    solutionVersionArn = field("solutionVersionArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBatchInferenceJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchInferenceJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchSegmentJobsRequest:
    boto3_raw_data: "type_defs.ListBatchSegmentJobsRequestTypeDef" = dataclasses.field()

    solutionVersionArn = field("solutionVersionArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBatchSegmentJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchSegmentJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCampaignsRequest:
    boto3_raw_data: "type_defs.ListCampaignsRequestTypeDef" = dataclasses.field()

    solutionArn = field("solutionArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCampaignsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCampaignsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataDeletionJobsRequest:
    boto3_raw_data: "type_defs.ListDataDeletionJobsRequestTypeDef" = dataclasses.field()

    datasetGroupArn = field("datasetGroupArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataDeletionJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataDeletionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetExportJobsRequest:
    boto3_raw_data: "type_defs.ListDatasetExportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    datasetArn = field("datasetArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetExportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetExportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetGroupsRequest:
    boto3_raw_data: "type_defs.ListDatasetGroupsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetImportJobsRequest:
    boto3_raw_data: "type_defs.ListDatasetImportJobsRequestTypeDef" = (
        dataclasses.field()
    )

    datasetArn = field("datasetArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsRequest:
    boto3_raw_data: "type_defs.ListDatasetsRequestTypeDef" = dataclasses.field()

    datasetGroupArn = field("datasetGroupArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventTrackersRequest:
    boto3_raw_data: "type_defs.ListEventTrackersRequestTypeDef" = dataclasses.field()

    datasetGroupArn = field("datasetGroupArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventTrackersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventTrackersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFiltersRequest:
    boto3_raw_data: "type_defs.ListFiltersRequestTypeDef" = dataclasses.field()

    datasetGroupArn = field("datasetGroupArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFiltersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFiltersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricAttributionMetricsRequest:
    boto3_raw_data: "type_defs.ListMetricAttributionMetricsRequestTypeDef" = (
        dataclasses.field()
    )

    metricAttributionArn = field("metricAttributionArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMetricAttributionMetricsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricAttributionMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricAttributionsRequest:
    boto3_raw_data: "type_defs.ListMetricAttributionsRequestTypeDef" = (
        dataclasses.field()
    )

    datasetGroupArn = field("datasetGroupArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMetricAttributionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricAttributionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricAttributionSummary:
    boto3_raw_data: "type_defs.MetricAttributionSummaryTypeDef" = dataclasses.field()

    name = field("name")
    metricAttributionArn = field("metricAttributionArn")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricAttributionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricAttributionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecipesRequest:
    boto3_raw_data: "type_defs.ListRecipesRequestTypeDef" = dataclasses.field()

    recipeProvider = field("recipeProvider")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    domain = field("domain")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecipesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecipesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecipeSummary:
    boto3_raw_data: "type_defs.RecipeSummaryTypeDef" = dataclasses.field()

    name = field("name")
    recipeArn = field("recipeArn")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    domain = field("domain")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecipeSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecipeSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendersRequest:
    boto3_raw_data: "type_defs.ListRecommendersRequestTypeDef" = dataclasses.field()

    datasetGroupArn = field("datasetGroupArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemasRequest:
    boto3_raw_data: "type_defs.ListSchemasRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchemasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolutionVersionsRequest:
    boto3_raw_data: "type_defs.ListSolutionVersionsRequestTypeDef" = dataclasses.field()

    solutionArn = field("solutionArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolutionVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolutionVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SolutionVersionSummary:
    boto3_raw_data: "type_defs.SolutionVersionSummaryTypeDef" = dataclasses.field()

    solutionVersionArn = field("solutionVersionArn")
    status = field("status")
    trainingMode = field("trainingMode")
    trainingType = field("trainingType")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SolutionVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SolutionVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolutionsRequest:
    boto3_raw_data: "type_defs.ListSolutionsRequestTypeDef" = dataclasses.field()

    datasetGroupArn = field("datasetGroupArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolutionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SolutionSummary:
    boto3_raw_data: "type_defs.SolutionSummaryTypeDef" = dataclasses.field()

    name = field("name")
    solutionArn = field("solutionArn")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    recipeArn = field("recipeArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SolutionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SolutionSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

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
class OptimizationObjective:
    boto3_raw_data: "type_defs.OptimizationObjectiveTypeDef" = dataclasses.field()

    itemAttribute = field("itemAttribute")
    objectiveSensitivity = field("objectiveSensitivity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptimizationObjectiveTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptimizationObjectiveTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingDataConfigOutput:
    boto3_raw_data: "type_defs.TrainingDataConfigOutputTypeDef" = dataclasses.field()

    excludedDatasetColumns = field("excludedDatasetColumns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainingDataConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainingDataConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingDataConfig:
    boto3_raw_data: "type_defs.TrainingDataConfigTypeDef" = dataclasses.field()

    excludedDatasetColumns = field("excludedDatasetColumns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainingDataConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainingDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TunedHPOParams:
    boto3_raw_data: "type_defs.TunedHPOParamsTypeDef" = dataclasses.field()

    algorithmHyperParameters = field("algorithmHyperParameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TunedHPOParamsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TunedHPOParamsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRecommenderRequest:
    boto3_raw_data: "type_defs.StartRecommenderRequestTypeDef" = dataclasses.field()

    recommenderArn = field("recommenderArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRecommenderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRecommenderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopRecommenderRequest:
    boto3_raw_data: "type_defs.StopRecommenderRequestTypeDef" = dataclasses.field()

    recommenderArn = field("recommenderArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopRecommenderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopRecommenderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSolutionVersionCreationRequest:
    boto3_raw_data: "type_defs.StopSolutionVersionCreationRequestTypeDef" = (
        dataclasses.field()
    )

    solutionVersionArn = field("solutionVersionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopSolutionVersionCreationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSolutionVersionCreationRequestTypeDef"]
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

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class UpdateDatasetRequest:
    boto3_raw_data: "type_defs.UpdateDatasetRequestTypeDef" = dataclasses.field()

    datasetArn = field("datasetArn")
    schemaArn = field("schemaArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchInferenceJobInput:
    boto3_raw_data: "type_defs.BatchInferenceJobInputTypeDef" = dataclasses.field()

    @cached_property
    def s3DataSource(self):  # pragma: no cover
        return S3DataConfig.make_one(self.boto3_raw_data["s3DataSource"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchInferenceJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchInferenceJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchInferenceJobOutput:
    boto3_raw_data: "type_defs.BatchInferenceJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def s3DataDestination(self):  # pragma: no cover
        return S3DataConfig.make_one(self.boto3_raw_data["s3DataDestination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchInferenceJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchInferenceJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchSegmentJobInput:
    boto3_raw_data: "type_defs.BatchSegmentJobInputTypeDef" = dataclasses.field()

    @cached_property
    def s3DataSource(self):  # pragma: no cover
        return S3DataConfig.make_one(self.boto3_raw_data["s3DataSource"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchSegmentJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchSegmentJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchSegmentJobOutput:
    boto3_raw_data: "type_defs.BatchSegmentJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def s3DataDestination(self):  # pragma: no cover
        return S3DataConfig.make_one(self.boto3_raw_data["s3DataDestination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchSegmentJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchSegmentJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetExportJobOutput:
    boto3_raw_data: "type_defs.DatasetExportJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def s3DataDestination(self):  # pragma: no cover
        return S3DataConfig.make_one(self.boto3_raw_data["s3DataDestination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasetExportJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetExportJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricAttributionOutput:
    boto3_raw_data: "type_defs.MetricAttributionOutputTypeDef" = dataclasses.field()

    roleArn = field("roleArn")

    @cached_property
    def s3DataDestination(self):  # pragma: no cover
        return S3DataConfig.make_one(self.boto3_raw_data["s3DataDestination"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricAttributionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricAttributionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CampaignUpdateSummary:
    boto3_raw_data: "type_defs.CampaignUpdateSummaryTypeDef" = dataclasses.field()

    solutionVersionArn = field("solutionVersionArn")
    minProvisionedTPS = field("minProvisionedTPS")

    @cached_property
    def campaignConfig(self):  # pragma: no cover
        return CampaignConfigOutput.make_one(self.boto3_raw_data["campaignConfig"])

    status = field("status")
    failureReason = field("failureReason")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CampaignUpdateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CampaignUpdateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetGroupRequest:
    boto3_raw_data: "type_defs.CreateDatasetGroupRequestTypeDef" = dataclasses.field()

    name = field("name")
    roleArn = field("roleArn")
    kmsKeyArn = field("kmsKeyArn")
    domain = field("domain")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetRequest:
    boto3_raw_data: "type_defs.CreateDatasetRequestTypeDef" = dataclasses.field()

    name = field("name")
    schemaArn = field("schemaArn")
    datasetGroupArn = field("datasetGroupArn")
    datasetType = field("datasetType")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventTrackerRequest:
    boto3_raw_data: "type_defs.CreateEventTrackerRequestTypeDef" = dataclasses.field()

    name = field("name")
    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventTrackerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventTrackerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFilterRequest:
    boto3_raw_data: "type_defs.CreateFilterRequestTypeDef" = dataclasses.field()

    name = field("name")
    datasetGroupArn = field("datasetGroupArn")
    filterExpression = field("filterExpression")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSolutionVersionRequest:
    boto3_raw_data: "type_defs.CreateSolutionVersionRequestTypeDef" = (
        dataclasses.field()
    )

    solutionArn = field("solutionArn")
    name = field("name")
    trainingMode = field("trainingMode")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSolutionVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSolutionVersionRequestTypeDef"]
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

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class CreateBatchInferenceJobResponse:
    boto3_raw_data: "type_defs.CreateBatchInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    batchInferenceJobArn = field("batchInferenceJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBatchInferenceJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBatchInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBatchSegmentJobResponse:
    boto3_raw_data: "type_defs.CreateBatchSegmentJobResponseTypeDef" = (
        dataclasses.field()
    )

    batchSegmentJobArn = field("batchSegmentJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBatchSegmentJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBatchSegmentJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCampaignResponse:
    boto3_raw_data: "type_defs.CreateCampaignResponseTypeDef" = dataclasses.field()

    campaignArn = field("campaignArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataDeletionJobResponse:
    boto3_raw_data: "type_defs.CreateDataDeletionJobResponseTypeDef" = (
        dataclasses.field()
    )

    dataDeletionJobArn = field("dataDeletionJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataDeletionJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataDeletionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetExportJobResponse:
    boto3_raw_data: "type_defs.CreateDatasetExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    datasetExportJobArn = field("datasetExportJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDatasetExportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetGroupResponse:
    boto3_raw_data: "type_defs.CreateDatasetGroupResponseTypeDef" = dataclasses.field()

    datasetGroupArn = field("datasetGroupArn")
    domain = field("domain")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetImportJobResponse:
    boto3_raw_data: "type_defs.CreateDatasetImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    datasetImportJobArn = field("datasetImportJobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDatasetImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetResponse:
    boto3_raw_data: "type_defs.CreateDatasetResponseTypeDef" = dataclasses.field()

    datasetArn = field("datasetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventTrackerResponse:
    boto3_raw_data: "type_defs.CreateEventTrackerResponseTypeDef" = dataclasses.field()

    eventTrackerArn = field("eventTrackerArn")
    trackingId = field("trackingId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventTrackerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventTrackerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFilterResponse:
    boto3_raw_data: "type_defs.CreateFilterResponseTypeDef" = dataclasses.field()

    filterArn = field("filterArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMetricAttributionResponse:
    boto3_raw_data: "type_defs.CreateMetricAttributionResponseTypeDef" = (
        dataclasses.field()
    )

    metricAttributionArn = field("metricAttributionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMetricAttributionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMetricAttributionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRecommenderResponse:
    boto3_raw_data: "type_defs.CreateRecommenderResponseTypeDef" = dataclasses.field()

    recommenderArn = field("recommenderArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRecommenderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRecommenderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSchemaResponse:
    boto3_raw_data: "type_defs.CreateSchemaResponseTypeDef" = dataclasses.field()

    schemaArn = field("schemaArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSchemaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSolutionResponse:
    boto3_raw_data: "type_defs.CreateSolutionResponseTypeDef" = dataclasses.field()

    solutionArn = field("solutionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSolutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSolutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSolutionVersionResponse:
    boto3_raw_data: "type_defs.CreateSolutionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    solutionVersionArn = field("solutionVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSolutionVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSolutionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSolutionMetricsResponse:
    boto3_raw_data: "type_defs.GetSolutionMetricsResponseTypeDef" = dataclasses.field()

    solutionVersionArn = field("solutionVersionArn")
    metrics = field("metrics")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSolutionMetricsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSolutionMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchInferenceJobsResponse:
    boto3_raw_data: "type_defs.ListBatchInferenceJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def batchInferenceJobs(self):  # pragma: no cover
        return BatchInferenceJobSummary.make_many(
            self.boto3_raw_data["batchInferenceJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBatchInferenceJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchInferenceJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchSegmentJobsResponse:
    boto3_raw_data: "type_defs.ListBatchSegmentJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def batchSegmentJobs(self):  # pragma: no cover
        return BatchSegmentJobSummary.make_many(self.boto3_raw_data["batchSegmentJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBatchSegmentJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchSegmentJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCampaignsResponse:
    boto3_raw_data: "type_defs.ListCampaignsResponseTypeDef" = dataclasses.field()

    @cached_property
    def campaigns(self):  # pragma: no cover
        return CampaignSummary.make_many(self.boto3_raw_data["campaigns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCampaignsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCampaignsResponseTypeDef"]
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

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class StartRecommenderResponse:
    boto3_raw_data: "type_defs.StartRecommenderResponseTypeDef" = dataclasses.field()

    recommenderArn = field("recommenderArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRecommenderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRecommenderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopRecommenderResponse:
    boto3_raw_data: "type_defs.StopRecommenderResponseTypeDef" = dataclasses.field()

    recommenderArn = field("recommenderArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopRecommenderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopRecommenderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignResponse:
    boto3_raw_data: "type_defs.UpdateCampaignResponseTypeDef" = dataclasses.field()

    campaignArn = field("campaignArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDatasetResponse:
    boto3_raw_data: "type_defs.UpdateDatasetResponseTypeDef" = dataclasses.field()

    datasetArn = field("datasetArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMetricAttributionResponse:
    boto3_raw_data: "type_defs.UpdateMetricAttributionResponseTypeDef" = (
        dataclasses.field()
    )

    metricAttributionArn = field("metricAttributionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMetricAttributionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMetricAttributionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecommenderResponse:
    boto3_raw_data: "type_defs.UpdateRecommenderResponseTypeDef" = dataclasses.field()

    recommenderArn = field("recommenderArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRecommenderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecommenderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSolutionResponse:
    boto3_raw_data: "type_defs.UpdateSolutionResponseTypeDef" = dataclasses.field()

    solutionArn = field("solutionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSolutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSolutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataDeletionJobRequest:
    boto3_raw_data: "type_defs.CreateDataDeletionJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobName = field("jobName")
    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def dataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["dataSource"])

    roleArn = field("roleArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataDeletionJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataDeletionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetImportJobRequest:
    boto3_raw_data: "type_defs.CreateDatasetImportJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobName = field("jobName")
    datasetArn = field("datasetArn")

    @cached_property
    def dataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["dataSource"])

    roleArn = field("roleArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    importMode = field("importMode")
    publishAttributionMetricsToS3 = field("publishAttributionMetricsToS3")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDatasetImportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataDeletionJob:
    boto3_raw_data: "type_defs.DataDeletionJobTypeDef" = dataclasses.field()

    jobName = field("jobName")
    dataDeletionJobArn = field("dataDeletionJobArn")
    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def dataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["dataSource"])

    roleArn = field("roleArn")
    status = field("status")
    numDeleted = field("numDeleted")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataDeletionJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataDeletionJobTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetImportJob:
    boto3_raw_data: "type_defs.DatasetImportJobTypeDef" = dataclasses.field()

    jobName = field("jobName")
    datasetImportJobArn = field("datasetImportJobArn")
    datasetArn = field("datasetArn")

    @cached_property
    def dataSource(self):  # pragma: no cover
        return DataSource.make_one(self.boto3_raw_data["dataSource"])

    roleArn = field("roleArn")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")
    importMode = field("importMode")
    publishAttributionMetricsToS3 = field("publishAttributionMetricsToS3")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetImportJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetImportJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricAttributionMetricsResponse:
    boto3_raw_data: "type_defs.ListMetricAttributionMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def metrics(self):  # pragma: no cover
        return MetricAttribute.make_many(self.boto3_raw_data["metrics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMetricAttributionMetricsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricAttributionMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataDeletionJobsResponse:
    boto3_raw_data: "type_defs.ListDataDeletionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataDeletionJobs(self):  # pragma: no cover
        return DataDeletionJobSummary.make_many(self.boto3_raw_data["dataDeletionJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataDeletionJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataDeletionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetExportJobsResponse:
    boto3_raw_data: "type_defs.ListDatasetExportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def datasetExportJobs(self):  # pragma: no cover
        return DatasetExportJobSummary.make_many(
            self.boto3_raw_data["datasetExportJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDatasetExportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetExportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetGroupsResponse:
    boto3_raw_data: "type_defs.ListDatasetGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def datasetGroups(self):  # pragma: no cover
        return DatasetGroupSummary.make_many(self.boto3_raw_data["datasetGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetGroupResponse:
    boto3_raw_data: "type_defs.DescribeDatasetGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def datasetGroup(self):  # pragma: no cover
        return DatasetGroup.make_one(self.boto3_raw_data["datasetGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetImportJobsResponse:
    boto3_raw_data: "type_defs.ListDatasetImportJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def datasetImportJobs(self):  # pragma: no cover
        return DatasetImportJobSummary.make_many(
            self.boto3_raw_data["datasetImportJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDatasetImportJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemasResponse:
    boto3_raw_data: "type_defs.ListSchemasResponseTypeDef" = dataclasses.field()

    @cached_property
    def schemas(self):  # pragma: no cover
        return DatasetSchemaSummary.make_many(self.boto3_raw_data["schemas"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchemasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSchemaResponse:
    boto3_raw_data: "type_defs.DescribeSchemaResponseTypeDef" = dataclasses.field()

    @cached_property
    def schema(self):  # pragma: no cover
        return DatasetSchema.make_one(self.boto3_raw_data["schema"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSchemaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsResponse:
    boto3_raw_data: "type_defs.ListDatasetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def datasets(self):  # pragma: no cover
        return DatasetSummary.make_many(self.boto3_raw_data["datasets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dataset:
    boto3_raw_data: "type_defs.DatasetTypeDef" = dataclasses.field()

    name = field("name")
    datasetArn = field("datasetArn")
    datasetGroupArn = field("datasetGroupArn")
    datasetType = field("datasetType")
    schemaArn = field("schemaArn")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def latestDatasetUpdate(self):  # pragma: no cover
        return DatasetUpdateSummary.make_one(self.boto3_raw_data["latestDatasetUpdate"])

    trackingId = field("trackingId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatasetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultHyperParameterRanges:
    boto3_raw_data: "type_defs.DefaultHyperParameterRangesTypeDef" = dataclasses.field()

    @cached_property
    def integerHyperParameterRanges(self):  # pragma: no cover
        return DefaultIntegerHyperParameterRange.make_many(
            self.boto3_raw_data["integerHyperParameterRanges"]
        )

    @cached_property
    def continuousHyperParameterRanges(self):  # pragma: no cover
        return DefaultContinuousHyperParameterRange.make_many(
            self.boto3_raw_data["continuousHyperParameterRanges"]
        )

    @cached_property
    def categoricalHyperParameterRanges(self):  # pragma: no cover
        return DefaultCategoricalHyperParameterRange.make_many(
            self.boto3_raw_data["categoricalHyperParameterRanges"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefaultHyperParameterRangesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultHyperParameterRangesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventTrackerResponse:
    boto3_raw_data: "type_defs.DescribeEventTrackerResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def eventTracker(self):  # pragma: no cover
        return EventTracker.make_one(self.boto3_raw_data["eventTracker"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventTrackerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventTrackerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFeatureTransformationResponse:
    boto3_raw_data: "type_defs.DescribeFeatureTransformationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def featureTransformation(self):  # pragma: no cover
        return FeatureTransformation.make_one(
            self.boto3_raw_data["featureTransformation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFeatureTransformationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFeatureTransformationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFilterResponse:
    boto3_raw_data: "type_defs.DescribeFilterResponseTypeDef" = dataclasses.field()

    @cached_property
    def filter(self):  # pragma: no cover
        return Filter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecipeResponse:
    boto3_raw_data: "type_defs.DescribeRecipeResponseTypeDef" = dataclasses.field()

    @cached_property
    def recipe(self):  # pragma: no cover
        return Recipe.make_one(self.boto3_raw_data["recipe"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRecipeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecipeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventsConfigOutput:
    boto3_raw_data: "type_defs.EventsConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def eventParametersList(self):  # pragma: no cover
        return EventParameters.make_many(self.boto3_raw_data["eventParametersList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventsConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventsConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventsConfig:
    boto3_raw_data: "type_defs.EventsConfigTypeDef" = dataclasses.field()

    @cached_property
    def eventParametersList(self):  # pragma: no cover
        return EventParameters.make_many(self.boto3_raw_data["eventParametersList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventsConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventsConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventTrackersResponse:
    boto3_raw_data: "type_defs.ListEventTrackersResponseTypeDef" = dataclasses.field()

    @cached_property
    def eventTrackers(self):  # pragma: no cover
        return EventTrackerSummary.make_many(self.boto3_raw_data["eventTrackers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventTrackersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventTrackersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThemeGenerationConfig:
    boto3_raw_data: "type_defs.ThemeGenerationConfigTypeDef" = dataclasses.field()

    @cached_property
    def fieldsForThemeGeneration(self):  # pragma: no cover
        return FieldsForThemeGeneration.make_one(
            self.boto3_raw_data["fieldsForThemeGeneration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThemeGenerationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThemeGenerationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFiltersResponse:
    boto3_raw_data: "type_defs.ListFiltersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return FilterSummary.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFiltersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFiltersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HyperParameterRangesOutput:
    boto3_raw_data: "type_defs.HyperParameterRangesOutputTypeDef" = dataclasses.field()

    @cached_property
    def integerHyperParameterRanges(self):  # pragma: no cover
        return IntegerHyperParameterRange.make_many(
            self.boto3_raw_data["integerHyperParameterRanges"]
        )

    @cached_property
    def continuousHyperParameterRanges(self):  # pragma: no cover
        return ContinuousHyperParameterRange.make_many(
            self.boto3_raw_data["continuousHyperParameterRanges"]
        )

    @cached_property
    def categoricalHyperParameterRanges(self):  # pragma: no cover
        return CategoricalHyperParameterRangeOutput.make_many(
            self.boto3_raw_data["categoricalHyperParameterRanges"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HyperParameterRangesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HyperParameterRangesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HyperParameterRanges:
    boto3_raw_data: "type_defs.HyperParameterRangesTypeDef" = dataclasses.field()

    @cached_property
    def integerHyperParameterRanges(self):  # pragma: no cover
        return IntegerHyperParameterRange.make_many(
            self.boto3_raw_data["integerHyperParameterRanges"]
        )

    @cached_property
    def continuousHyperParameterRanges(self):  # pragma: no cover
        return ContinuousHyperParameterRange.make_many(
            self.boto3_raw_data["continuousHyperParameterRanges"]
        )

    @cached_property
    def categoricalHyperParameterRanges(self):  # pragma: no cover
        return CategoricalHyperParameterRange.make_many(
            self.boto3_raw_data["categoricalHyperParameterRanges"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HyperParameterRangesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HyperParameterRangesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchInferenceJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListBatchInferenceJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    solutionVersionArn = field("solutionVersionArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBatchInferenceJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchInferenceJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBatchSegmentJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListBatchSegmentJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    solutionVersionArn = field("solutionVersionArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBatchSegmentJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBatchSegmentJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCampaignsRequestPaginate:
    boto3_raw_data: "type_defs.ListCampaignsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    solutionArn = field("solutionArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCampaignsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCampaignsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetExportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetExportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    datasetArn = field("datasetArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDatasetExportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetExportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetGroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDatasetGroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetImportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetImportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    datasetArn = field("datasetArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDatasetImportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetImportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasetsRequestPaginate:
    boto3_raw_data: "type_defs.ListDatasetsRequestPaginateTypeDef" = dataclasses.field()

    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDatasetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventTrackersRequestPaginate:
    boto3_raw_data: "type_defs.ListEventTrackersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventTrackersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventTrackersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFiltersRequestPaginate:
    boto3_raw_data: "type_defs.ListFiltersRequestPaginateTypeDef" = dataclasses.field()

    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFiltersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFiltersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricAttributionMetricsRequestPaginate:
    boto3_raw_data: "type_defs.ListMetricAttributionMetricsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    metricAttributionArn = field("metricAttributionArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMetricAttributionMetricsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricAttributionMetricsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricAttributionsRequestPaginate:
    boto3_raw_data: "type_defs.ListMetricAttributionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMetricAttributionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricAttributionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecipesRequestPaginate:
    boto3_raw_data: "type_defs.ListRecipesRequestPaginateTypeDef" = dataclasses.field()

    recipeProvider = field("recipeProvider")
    domain = field("domain")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecipesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecipesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendersRequestPaginate:
    boto3_raw_data: "type_defs.ListRecommendersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRecommendersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemasRequestPaginate:
    boto3_raw_data: "type_defs.ListSchemasRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchemasRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemasRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolutionVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSolutionVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    solutionArn = field("solutionArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSolutionVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolutionVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolutionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSolutionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolutionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolutionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetricAttributionsResponse:
    boto3_raw_data: "type_defs.ListMetricAttributionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def metricAttributions(self):  # pragma: no cover
        return MetricAttributionSummary.make_many(
            self.boto3_raw_data["metricAttributions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMetricAttributionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetricAttributionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecipesResponse:
    boto3_raw_data: "type_defs.ListRecipesResponseTypeDef" = dataclasses.field()

    @cached_property
    def recipes(self):  # pragma: no cover
        return RecipeSummary.make_many(self.boto3_raw_data["recipes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecipesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecipesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolutionVersionsResponse:
    boto3_raw_data: "type_defs.ListSolutionVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def solutionVersions(self):  # pragma: no cover
        return SolutionVersionSummary.make_many(self.boto3_raw_data["solutionVersions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolutionVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolutionVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSolutionsResponse:
    boto3_raw_data: "type_defs.ListSolutionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def solutions(self):  # pragma: no cover
        return SolutionSummary.make_many(self.boto3_raw_data["solutions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSolutionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSolutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommenderConfigOutput:
    boto3_raw_data: "type_defs.RecommenderConfigOutputTypeDef" = dataclasses.field()

    itemExplorationConfig = field("itemExplorationConfig")
    minRecommendationRequestsPerSecond = field("minRecommendationRequestsPerSecond")

    @cached_property
    def trainingDataConfig(self):  # pragma: no cover
        return TrainingDataConfigOutput.make_one(
            self.boto3_raw_data["trainingDataConfig"]
        )

    enableMetadataWithRecommendations = field("enableMetadataWithRecommendations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommenderConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommenderConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommenderConfig:
    boto3_raw_data: "type_defs.RecommenderConfigTypeDef" = dataclasses.field()

    itemExplorationConfig = field("itemExplorationConfig")
    minRecommendationRequestsPerSecond = field("minRecommendationRequestsPerSecond")

    @cached_property
    def trainingDataConfig(self):  # pragma: no cover
        return TrainingDataConfig.make_one(self.boto3_raw_data["trainingDataConfig"])

    enableMetadataWithRecommendations = field("enableMetadataWithRecommendations")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommenderConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommenderConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchSegmentJob:
    boto3_raw_data: "type_defs.BatchSegmentJobTypeDef" = dataclasses.field()

    jobName = field("jobName")
    batchSegmentJobArn = field("batchSegmentJobArn")
    filterArn = field("filterArn")
    failureReason = field("failureReason")
    solutionVersionArn = field("solutionVersionArn")
    numResults = field("numResults")

    @cached_property
    def jobInput(self):  # pragma: no cover
        return BatchSegmentJobInput.make_one(self.boto3_raw_data["jobInput"])

    @cached_property
    def jobOutput(self):  # pragma: no cover
        return BatchSegmentJobOutput.make_one(self.boto3_raw_data["jobOutput"])

    roleArn = field("roleArn")
    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchSegmentJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchSegmentJobTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBatchSegmentJobRequest:
    boto3_raw_data: "type_defs.CreateBatchSegmentJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobName = field("jobName")
    solutionVersionArn = field("solutionVersionArn")

    @cached_property
    def jobInput(self):  # pragma: no cover
        return BatchSegmentJobInput.make_one(self.boto3_raw_data["jobInput"])

    @cached_property
    def jobOutput(self):  # pragma: no cover
        return BatchSegmentJobOutput.make_one(self.boto3_raw_data["jobOutput"])

    roleArn = field("roleArn")
    filterArn = field("filterArn")
    numResults = field("numResults")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBatchSegmentJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBatchSegmentJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDatasetExportJobRequest:
    boto3_raw_data: "type_defs.CreateDatasetExportJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobName = field("jobName")
    datasetArn = field("datasetArn")
    roleArn = field("roleArn")

    @cached_property
    def jobOutput(self):  # pragma: no cover
        return DatasetExportJobOutput.make_one(self.boto3_raw_data["jobOutput"])

    ingestionMode = field("ingestionMode")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDatasetExportJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDatasetExportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasetExportJob:
    boto3_raw_data: "type_defs.DatasetExportJobTypeDef" = dataclasses.field()

    jobName = field("jobName")
    datasetExportJobArn = field("datasetExportJobArn")
    datasetArn = field("datasetArn")
    ingestionMode = field("ingestionMode")
    roleArn = field("roleArn")
    status = field("status")

    @cached_property
    def jobOutput(self):  # pragma: no cover
        return DatasetExportJobOutput.make_one(self.boto3_raw_data["jobOutput"])

    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatasetExportJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasetExportJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMetricAttributionRequest:
    boto3_raw_data: "type_defs.CreateMetricAttributionRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def metrics(self):  # pragma: no cover
        return MetricAttribute.make_many(self.boto3_raw_data["metrics"])

    @cached_property
    def metricsOutputConfig(self):  # pragma: no cover
        return MetricAttributionOutput.make_one(
            self.boto3_raw_data["metricsOutputConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMetricAttributionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMetricAttributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricAttribution:
    boto3_raw_data: "type_defs.MetricAttributionTypeDef" = dataclasses.field()

    name = field("name")
    metricAttributionArn = field("metricAttributionArn")
    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def metricsOutputConfig(self):  # pragma: no cover
        return MetricAttributionOutput.make_one(
            self.boto3_raw_data["metricsOutputConfig"]
        )

    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricAttributionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricAttributionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMetricAttributionRequest:
    boto3_raw_data: "type_defs.UpdateMetricAttributionRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def addMetrics(self):  # pragma: no cover
        return MetricAttribute.make_many(self.boto3_raw_data["addMetrics"])

    removeMetrics = field("removeMetrics")

    @cached_property
    def metricsOutputConfig(self):  # pragma: no cover
        return MetricAttributionOutput.make_one(
            self.boto3_raw_data["metricsOutputConfig"]
        )

    metricAttributionArn = field("metricAttributionArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMetricAttributionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMetricAttributionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Campaign:
    boto3_raw_data: "type_defs.CampaignTypeDef" = dataclasses.field()

    name = field("name")
    campaignArn = field("campaignArn")
    solutionVersionArn = field("solutionVersionArn")
    minProvisionedTPS = field("minProvisionedTPS")

    @cached_property
    def campaignConfig(self):  # pragma: no cover
        return CampaignConfigOutput.make_one(self.boto3_raw_data["campaignConfig"])

    status = field("status")
    failureReason = field("failureReason")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def latestCampaignUpdate(self):  # pragma: no cover
        return CampaignUpdateSummary.make_one(
            self.boto3_raw_data["latestCampaignUpdate"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CampaignTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CampaignTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCampaignRequest:
    boto3_raw_data: "type_defs.CreateCampaignRequestTypeDef" = dataclasses.field()

    name = field("name")
    solutionVersionArn = field("solutionVersionArn")
    minProvisionedTPS = field("minProvisionedTPS")
    campaignConfig = field("campaignConfig")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCampaignRequest:
    boto3_raw_data: "type_defs.UpdateCampaignRequestTypeDef" = dataclasses.field()

    campaignArn = field("campaignArn")
    solutionVersionArn = field("solutionVersionArn")
    minProvisionedTPS = field("minProvisionedTPS")
    campaignConfig = field("campaignConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCampaignRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCampaignRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataDeletionJobResponse:
    boto3_raw_data: "type_defs.DescribeDataDeletionJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataDeletionJob(self):  # pragma: no cover
        return DataDeletionJob.make_one(self.boto3_raw_data["dataDeletionJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDataDeletionJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataDeletionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetImportJobResponse:
    boto3_raw_data: "type_defs.DescribeDatasetImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def datasetImportJob(self):  # pragma: no cover
        return DatasetImportJob.make_one(self.boto3_raw_data["datasetImportJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDatasetImportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetResponse:
    boto3_raw_data: "type_defs.DescribeDatasetResponseTypeDef" = dataclasses.field()

    @cached_property
    def dataset(self):  # pragma: no cover
        return Dataset.make_one(self.boto3_raw_data["dataset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDatasetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Algorithm:
    boto3_raw_data: "type_defs.AlgorithmTypeDef" = dataclasses.field()

    name = field("name")
    algorithmArn = field("algorithmArn")

    @cached_property
    def algorithmImage(self):  # pragma: no cover
        return AlgorithmImage.make_one(self.boto3_raw_data["algorithmImage"])

    defaultHyperParameters = field("defaultHyperParameters")

    @cached_property
    def defaultHyperParameterRanges(self):  # pragma: no cover
        return DefaultHyperParameterRanges.make_one(
            self.boto3_raw_data["defaultHyperParameterRanges"]
        )

    defaultResourceConfig = field("defaultResourceConfig")
    trainingInputMode = field("trainingInputMode")
    roleArn = field("roleArn")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlgorithmTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlgorithmTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SolutionUpdateConfigOutput:
    boto3_raw_data: "type_defs.SolutionUpdateConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def autoTrainingConfig(self):  # pragma: no cover
        return AutoTrainingConfig.make_one(self.boto3_raw_data["autoTrainingConfig"])

    @cached_property
    def eventsConfig(self):  # pragma: no cover
        return EventsConfigOutput.make_one(self.boto3_raw_data["eventsConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SolutionUpdateConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SolutionUpdateConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SolutionUpdateConfig:
    boto3_raw_data: "type_defs.SolutionUpdateConfigTypeDef" = dataclasses.field()

    @cached_property
    def autoTrainingConfig(self):  # pragma: no cover
        return AutoTrainingConfig.make_one(self.boto3_raw_data["autoTrainingConfig"])

    @cached_property
    def eventsConfig(self):  # pragma: no cover
        return EventsConfig.make_one(self.boto3_raw_data["eventsConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SolutionUpdateConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SolutionUpdateConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchInferenceJob:
    boto3_raw_data: "type_defs.BatchInferenceJobTypeDef" = dataclasses.field()

    jobName = field("jobName")
    batchInferenceJobArn = field("batchInferenceJobArn")
    filterArn = field("filterArn")
    failureReason = field("failureReason")
    solutionVersionArn = field("solutionVersionArn")
    numResults = field("numResults")

    @cached_property
    def jobInput(self):  # pragma: no cover
        return BatchInferenceJobInput.make_one(self.boto3_raw_data["jobInput"])

    @cached_property
    def jobOutput(self):  # pragma: no cover
        return BatchInferenceJobOutput.make_one(self.boto3_raw_data["jobOutput"])

    @cached_property
    def batchInferenceJobConfig(self):  # pragma: no cover
        return BatchInferenceJobConfigOutput.make_one(
            self.boto3_raw_data["batchInferenceJobConfig"]
        )

    roleArn = field("roleArn")
    batchInferenceJobMode = field("batchInferenceJobMode")

    @cached_property
    def themeGenerationConfig(self):  # pragma: no cover
        return ThemeGenerationConfig.make_one(
            self.boto3_raw_data["themeGenerationConfig"]
        )

    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchInferenceJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchInferenceJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBatchInferenceJobRequest:
    boto3_raw_data: "type_defs.CreateBatchInferenceJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobName = field("jobName")
    solutionVersionArn = field("solutionVersionArn")

    @cached_property
    def jobInput(self):  # pragma: no cover
        return BatchInferenceJobInput.make_one(self.boto3_raw_data["jobInput"])

    @cached_property
    def jobOutput(self):  # pragma: no cover
        return BatchInferenceJobOutput.make_one(self.boto3_raw_data["jobOutput"])

    roleArn = field("roleArn")
    filterArn = field("filterArn")
    numResults = field("numResults")
    batchInferenceJobConfig = field("batchInferenceJobConfig")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    batchInferenceJobMode = field("batchInferenceJobMode")

    @cached_property
    def themeGenerationConfig(self):  # pragma: no cover
        return ThemeGenerationConfig.make_one(
            self.boto3_raw_data["themeGenerationConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBatchInferenceJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBatchInferenceJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HPOConfigOutput:
    boto3_raw_data: "type_defs.HPOConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def hpoObjective(self):  # pragma: no cover
        return HPOObjective.make_one(self.boto3_raw_data["hpoObjective"])

    @cached_property
    def hpoResourceConfig(self):  # pragma: no cover
        return HPOResourceConfig.make_one(self.boto3_raw_data["hpoResourceConfig"])

    @cached_property
    def algorithmHyperParameterRanges(self):  # pragma: no cover
        return HyperParameterRangesOutput.make_one(
            self.boto3_raw_data["algorithmHyperParameterRanges"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HPOConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HPOConfigOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HPOConfig:
    boto3_raw_data: "type_defs.HPOConfigTypeDef" = dataclasses.field()

    @cached_property
    def hpoObjective(self):  # pragma: no cover
        return HPOObjective.make_one(self.boto3_raw_data["hpoObjective"])

    @cached_property
    def hpoResourceConfig(self):  # pragma: no cover
        return HPOResourceConfig.make_one(self.boto3_raw_data["hpoResourceConfig"])

    @cached_property
    def algorithmHyperParameterRanges(self):  # pragma: no cover
        return HyperParameterRanges.make_one(
            self.boto3_raw_data["algorithmHyperParameterRanges"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HPOConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HPOConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommenderSummary:
    boto3_raw_data: "type_defs.RecommenderSummaryTypeDef" = dataclasses.field()

    name = field("name")
    recommenderArn = field("recommenderArn")
    datasetGroupArn = field("datasetGroupArn")
    recipeArn = field("recipeArn")

    @cached_property
    def recommenderConfig(self):  # pragma: no cover
        return RecommenderConfigOutput.make_one(
            self.boto3_raw_data["recommenderConfig"]
        )

    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommenderSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommenderSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommenderUpdateSummary:
    boto3_raw_data: "type_defs.RecommenderUpdateSummaryTypeDef" = dataclasses.field()

    @cached_property
    def recommenderConfig(self):  # pragma: no cover
        return RecommenderConfigOutput.make_one(
            self.boto3_raw_data["recommenderConfig"]
        )

    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    status = field("status")
    failureReason = field("failureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommenderUpdateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommenderUpdateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBatchSegmentJobResponse:
    boto3_raw_data: "type_defs.DescribeBatchSegmentJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def batchSegmentJob(self):  # pragma: no cover
        return BatchSegmentJob.make_one(self.boto3_raw_data["batchSegmentJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBatchSegmentJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBatchSegmentJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDatasetExportJobResponse:
    boto3_raw_data: "type_defs.DescribeDatasetExportJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def datasetExportJob(self):  # pragma: no cover
        return DatasetExportJob.make_one(self.boto3_raw_data["datasetExportJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDatasetExportJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDatasetExportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetricAttributionResponse:
    boto3_raw_data: "type_defs.DescribeMetricAttributionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def metricAttribution(self):  # pragma: no cover
        return MetricAttribution.make_one(self.boto3_raw_data["metricAttribution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetricAttributionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetricAttributionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCampaignResponse:
    boto3_raw_data: "type_defs.DescribeCampaignResponseTypeDef" = dataclasses.field()

    @cached_property
    def campaign(self):  # pragma: no cover
        return Campaign.make_one(self.boto3_raw_data["campaign"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCampaignResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCampaignResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAlgorithmResponse:
    boto3_raw_data: "type_defs.DescribeAlgorithmResponseTypeDef" = dataclasses.field()

    @cached_property
    def algorithm(self):  # pragma: no cover
        return Algorithm.make_one(self.boto3_raw_data["algorithm"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAlgorithmResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAlgorithmResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SolutionUpdateSummary:
    boto3_raw_data: "type_defs.SolutionUpdateSummaryTypeDef" = dataclasses.field()

    @cached_property
    def solutionUpdateConfig(self):  # pragma: no cover
        return SolutionUpdateConfigOutput.make_one(
            self.boto3_raw_data["solutionUpdateConfig"]
        )

    status = field("status")
    performAutoTraining = field("performAutoTraining")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReason = field("failureReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SolutionUpdateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SolutionUpdateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBatchInferenceJobResponse:
    boto3_raw_data: "type_defs.DescribeBatchInferenceJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def batchInferenceJob(self):  # pragma: no cover
        return BatchInferenceJob.make_one(self.boto3_raw_data["batchInferenceJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBatchInferenceJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBatchInferenceJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SolutionConfigOutput:
    boto3_raw_data: "type_defs.SolutionConfigOutputTypeDef" = dataclasses.field()

    eventValueThreshold = field("eventValueThreshold")

    @cached_property
    def hpoConfig(self):  # pragma: no cover
        return HPOConfigOutput.make_one(self.boto3_raw_data["hpoConfig"])

    algorithmHyperParameters = field("algorithmHyperParameters")
    featureTransformationParameters = field("featureTransformationParameters")

    @cached_property
    def autoMLConfig(self):  # pragma: no cover
        return AutoMLConfigOutput.make_one(self.boto3_raw_data["autoMLConfig"])

    @cached_property
    def eventsConfig(self):  # pragma: no cover
        return EventsConfigOutput.make_one(self.boto3_raw_data["eventsConfig"])

    @cached_property
    def optimizationObjective(self):  # pragma: no cover
        return OptimizationObjective.make_one(
            self.boto3_raw_data["optimizationObjective"]
        )

    @cached_property
    def trainingDataConfig(self):  # pragma: no cover
        return TrainingDataConfigOutput.make_one(
            self.boto3_raw_data["trainingDataConfig"]
        )

    @cached_property
    def autoTrainingConfig(self):  # pragma: no cover
        return AutoTrainingConfig.make_one(self.boto3_raw_data["autoTrainingConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SolutionConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SolutionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SolutionConfig:
    boto3_raw_data: "type_defs.SolutionConfigTypeDef" = dataclasses.field()

    eventValueThreshold = field("eventValueThreshold")

    @cached_property
    def hpoConfig(self):  # pragma: no cover
        return HPOConfig.make_one(self.boto3_raw_data["hpoConfig"])

    algorithmHyperParameters = field("algorithmHyperParameters")
    featureTransformationParameters = field("featureTransformationParameters")

    @cached_property
    def autoMLConfig(self):  # pragma: no cover
        return AutoMLConfig.make_one(self.boto3_raw_data["autoMLConfig"])

    @cached_property
    def eventsConfig(self):  # pragma: no cover
        return EventsConfig.make_one(self.boto3_raw_data["eventsConfig"])

    @cached_property
    def optimizationObjective(self):  # pragma: no cover
        return OptimizationObjective.make_one(
            self.boto3_raw_data["optimizationObjective"]
        )

    @cached_property
    def trainingDataConfig(self):  # pragma: no cover
        return TrainingDataConfig.make_one(self.boto3_raw_data["trainingDataConfig"])

    @cached_property
    def autoTrainingConfig(self):  # pragma: no cover
        return AutoTrainingConfig.make_one(self.boto3_raw_data["autoTrainingConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SolutionConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SolutionConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendersResponse:
    boto3_raw_data: "type_defs.ListRecommendersResponseTypeDef" = dataclasses.field()

    @cached_property
    def recommenders(self):  # pragma: no cover
        return RecommenderSummary.make_many(self.boto3_raw_data["recommenders"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRecommendersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recommender:
    boto3_raw_data: "type_defs.RecommenderTypeDef" = dataclasses.field()

    recommenderArn = field("recommenderArn")
    datasetGroupArn = field("datasetGroupArn")
    name = field("name")
    recipeArn = field("recipeArn")

    @cached_property
    def recommenderConfig(self):  # pragma: no cover
        return RecommenderConfigOutput.make_one(
            self.boto3_raw_data["recommenderConfig"]
        )

    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    status = field("status")
    failureReason = field("failureReason")

    @cached_property
    def latestRecommenderUpdate(self):  # pragma: no cover
        return RecommenderUpdateSummary.make_one(
            self.boto3_raw_data["latestRecommenderUpdate"]
        )

    modelMetrics = field("modelMetrics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommenderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecommenderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRecommenderRequest:
    boto3_raw_data: "type_defs.CreateRecommenderRequestTypeDef" = dataclasses.field()

    name = field("name")
    datasetGroupArn = field("datasetGroupArn")
    recipeArn = field("recipeArn")
    recommenderConfig = field("recommenderConfig")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRecommenderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRecommenderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRecommenderRequest:
    boto3_raw_data: "type_defs.UpdateRecommenderRequestTypeDef" = dataclasses.field()

    recommenderArn = field("recommenderArn")
    recommenderConfig = field("recommenderConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRecommenderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRecommenderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSolutionRequest:
    boto3_raw_data: "type_defs.UpdateSolutionRequestTypeDef" = dataclasses.field()

    solutionArn = field("solutionArn")
    performAutoTraining = field("performAutoTraining")
    solutionUpdateConfig = field("solutionUpdateConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSolutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSolutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Solution:
    boto3_raw_data: "type_defs.SolutionTypeDef" = dataclasses.field()

    name = field("name")
    solutionArn = field("solutionArn")
    performHPO = field("performHPO")
    performAutoML = field("performAutoML")
    performAutoTraining = field("performAutoTraining")
    recipeArn = field("recipeArn")
    datasetGroupArn = field("datasetGroupArn")
    eventType = field("eventType")

    @cached_property
    def solutionConfig(self):  # pragma: no cover
        return SolutionConfigOutput.make_one(self.boto3_raw_data["solutionConfig"])

    @cached_property
    def autoMLResult(self):  # pragma: no cover
        return AutoMLResult.make_one(self.boto3_raw_data["autoMLResult"])

    status = field("status")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def latestSolutionVersion(self):  # pragma: no cover
        return SolutionVersionSummary.make_one(
            self.boto3_raw_data["latestSolutionVersion"]
        )

    @cached_property
    def latestSolutionUpdate(self):  # pragma: no cover
        return SolutionUpdateSummary.make_one(
            self.boto3_raw_data["latestSolutionUpdate"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SolutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SolutionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SolutionVersion:
    boto3_raw_data: "type_defs.SolutionVersionTypeDef" = dataclasses.field()

    name = field("name")
    solutionVersionArn = field("solutionVersionArn")
    solutionArn = field("solutionArn")
    performHPO = field("performHPO")
    performAutoML = field("performAutoML")
    recipeArn = field("recipeArn")
    eventType = field("eventType")
    datasetGroupArn = field("datasetGroupArn")

    @cached_property
    def solutionConfig(self):  # pragma: no cover
        return SolutionConfigOutput.make_one(self.boto3_raw_data["solutionConfig"])

    trainingHours = field("trainingHours")
    trainingMode = field("trainingMode")

    @cached_property
    def tunedHPOParams(self):  # pragma: no cover
        return TunedHPOParams.make_one(self.boto3_raw_data["tunedHPOParams"])

    status = field("status")
    failureReason = field("failureReason")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    trainingType = field("trainingType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SolutionVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SolutionVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecommenderResponse:
    boto3_raw_data: "type_defs.DescribeRecommenderResponseTypeDef" = dataclasses.field()

    @cached_property
    def recommender(self):  # pragma: no cover
        return Recommender.make_one(self.boto3_raw_data["recommender"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRecommenderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecommenderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSolutionResponse:
    boto3_raw_data: "type_defs.DescribeSolutionResponseTypeDef" = dataclasses.field()

    @cached_property
    def solution(self):  # pragma: no cover
        return Solution.make_one(self.boto3_raw_data["solution"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSolutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSolutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSolutionVersionResponse:
    boto3_raw_data: "type_defs.DescribeSolutionVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def solutionVersion(self):  # pragma: no cover
        return SolutionVersion.make_one(self.boto3_raw_data["solutionVersion"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSolutionVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSolutionVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSolutionRequest:
    boto3_raw_data: "type_defs.CreateSolutionRequestTypeDef" = dataclasses.field()

    name = field("name")
    datasetGroupArn = field("datasetGroupArn")
    performHPO = field("performHPO")
    performAutoML = field("performAutoML")
    performAutoTraining = field("performAutoTraining")
    recipeArn = field("recipeArn")
    eventType = field("eventType")
    solutionConfig = field("solutionConfig")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSolutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSolutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
