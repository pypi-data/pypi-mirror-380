# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lexv2_models import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActiveContext:
    boto3_raw_data: "type_defs.ActiveContextTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActiveContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActiveContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedRecognitionSetting:
    boto3_raw_data: "type_defs.AdvancedRecognitionSettingTypeDef" = dataclasses.field()

    audioRecognitionStrategy = field("audioRecognitionStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedRecognitionSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedRecognitionSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionErrorDetails:
    boto3_raw_data: "type_defs.ExecutionErrorDetailsTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecutionErrorDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentTurnSpecification:
    boto3_raw_data: "type_defs.AgentTurnSpecificationTypeDef" = dataclasses.field()

    agentPrompt = field("agentPrompt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgentTurnSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgentTurnSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatedUtterancesFilter:
    boto3_raw_data: "type_defs.AggregatedUtterancesFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregatedUtterancesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatedUtterancesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatedUtterancesSortBy:
    boto3_raw_data: "type_defs.AggregatedUtterancesSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregatedUtterancesSortByTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatedUtterancesSortByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatedUtterancesSummary:
    boto3_raw_data: "type_defs.AggregatedUtterancesSummaryTypeDef" = dataclasses.field()

    utterance = field("utterance")
    hitCount = field("hitCount")
    missedCount = field("missedCount")
    utteranceFirstRecordedInAggregationDuration = field(
        "utteranceFirstRecordedInAggregationDuration"
    )
    utteranceLastRecordedInAggregationDuration = field(
        "utteranceLastRecordedInAggregationDuration"
    )
    containsDataFromDeletedResources = field("containsDataFromDeletedResources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregatedUtterancesSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatedUtterancesSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AllowedInputTypes:
    boto3_raw_data: "type_defs.AllowedInputTypesTypeDef" = dataclasses.field()

    allowAudioInput = field("allowAudioInput")
    allowDTMFInput = field("allowDTMFInput")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AllowedInputTypesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AllowedInputTypesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsBinBySpecification:
    boto3_raw_data: "type_defs.AnalyticsBinBySpecificationTypeDef" = dataclasses.field()

    name = field("name")
    interval = field("interval")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsBinBySpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsBinBySpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsBinKey:
    boto3_raw_data: "type_defs.AnalyticsBinKeyTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalyticsBinKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalyticsBinKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentFilter:
    boto3_raw_data: "type_defs.AnalyticsIntentFilterTypeDef" = dataclasses.field()

    name = field("name")
    operator = field("operator")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsIntentFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentGroupByKey:
    boto3_raw_data: "type_defs.AnalyticsIntentGroupByKeyTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsIntentGroupByKeyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentGroupByKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentGroupBySpecification:
    boto3_raw_data: "type_defs.AnalyticsIntentGroupBySpecificationTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AnalyticsIntentGroupBySpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentGroupBySpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentMetricResult:
    boto3_raw_data: "type_defs.AnalyticsIntentMetricResultTypeDef" = dataclasses.field()

    name = field("name")
    statistic = field("statistic")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsIntentMetricResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentMetricResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentMetric:
    boto3_raw_data: "type_defs.AnalyticsIntentMetricTypeDef" = dataclasses.field()

    name = field("name")
    statistic = field("statistic")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsIntentMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentNodeSummary:
    boto3_raw_data: "type_defs.AnalyticsIntentNodeSummaryTypeDef" = dataclasses.field()

    intentName = field("intentName")
    intentPath = field("intentPath")
    intentCount = field("intentCount")
    intentLevel = field("intentLevel")
    nodeType = field("nodeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsIntentNodeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentNodeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentStageFilter:
    boto3_raw_data: "type_defs.AnalyticsIntentStageFilterTypeDef" = dataclasses.field()

    name = field("name")
    operator = field("operator")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsIntentStageFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentStageFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentStageGroupByKey:
    boto3_raw_data: "type_defs.AnalyticsIntentStageGroupByKeyTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AnalyticsIntentStageGroupByKeyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentStageGroupByKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentStageGroupBySpecification:
    boto3_raw_data: "type_defs.AnalyticsIntentStageGroupBySpecificationTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AnalyticsIntentStageGroupBySpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentStageGroupBySpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentStageMetricResult:
    boto3_raw_data: "type_defs.AnalyticsIntentStageMetricResultTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    statistic = field("statistic")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AnalyticsIntentStageMetricResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentStageMetricResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentStageMetric:
    boto3_raw_data: "type_defs.AnalyticsIntentStageMetricTypeDef" = dataclasses.field()

    name = field("name")
    statistic = field("statistic")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsIntentStageMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentStageMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsPathFilter:
    boto3_raw_data: "type_defs.AnalyticsPathFilterTypeDef" = dataclasses.field()

    name = field("name")
    operator = field("operator")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsPathFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsPathFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsSessionFilter:
    boto3_raw_data: "type_defs.AnalyticsSessionFilterTypeDef" = dataclasses.field()

    name = field("name")
    operator = field("operator")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsSessionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsSessionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsSessionGroupByKey:
    boto3_raw_data: "type_defs.AnalyticsSessionGroupByKeyTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsSessionGroupByKeyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsSessionGroupByKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsSessionGroupBySpecification:
    boto3_raw_data: "type_defs.AnalyticsSessionGroupBySpecificationTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AnalyticsSessionGroupBySpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsSessionGroupBySpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsSessionMetricResult:
    boto3_raw_data: "type_defs.AnalyticsSessionMetricResultTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    statistic = field("statistic")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsSessionMetricResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsSessionMetricResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsSessionMetric:
    boto3_raw_data: "type_defs.AnalyticsSessionMetricTypeDef" = dataclasses.field()

    name = field("name")
    statistic = field("statistic")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsSessionMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsSessionMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsUtteranceAttributeResult:
    boto3_raw_data: "type_defs.AnalyticsUtteranceAttributeResultTypeDef" = (
        dataclasses.field()
    )

    lastUsedIntent = field("lastUsedIntent")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AnalyticsUtteranceAttributeResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsUtteranceAttributeResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsUtteranceAttribute:
    boto3_raw_data: "type_defs.AnalyticsUtteranceAttributeTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsUtteranceAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsUtteranceAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsUtteranceFilter:
    boto3_raw_data: "type_defs.AnalyticsUtteranceFilterTypeDef" = dataclasses.field()

    name = field("name")
    operator = field("operator")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsUtteranceFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsUtteranceFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsUtteranceGroupByKey:
    boto3_raw_data: "type_defs.AnalyticsUtteranceGroupByKeyTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsUtteranceGroupByKeyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsUtteranceGroupByKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsUtteranceGroupBySpecification:
    boto3_raw_data: "type_defs.AnalyticsUtteranceGroupBySpecificationTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AnalyticsUtteranceGroupBySpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsUtteranceGroupBySpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsUtteranceMetricResult:
    boto3_raw_data: "type_defs.AnalyticsUtteranceMetricResultTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    statistic = field("statistic")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AnalyticsUtteranceMetricResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsUtteranceMetricResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsUtteranceMetric:
    boto3_raw_data: "type_defs.AnalyticsUtteranceMetricTypeDef" = dataclasses.field()

    name = field("name")
    statistic = field("statistic")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsUtteranceMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsUtteranceMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatedTranscriptFilter:
    boto3_raw_data: "type_defs.AssociatedTranscriptFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatedTranscriptFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedTranscriptFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatedTranscript:
    boto3_raw_data: "type_defs.AssociatedTranscriptTypeDef" = dataclasses.field()

    transcript = field("transcript")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatedTranscriptTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedTranscriptTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioSpecification:
    boto3_raw_data: "type_defs.AudioSpecificationTypeDef" = dataclasses.field()

    maxLengthMs = field("maxLengthMs")
    endTimeoutMs = field("endTimeoutMs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DTMFSpecification:
    boto3_raw_data: "type_defs.DTMFSpecificationTypeDef" = dataclasses.field()

    maxLength = field("maxLength")
    endTimeoutMs = field("endTimeoutMs")
    deletionCharacter = field("deletionCharacter")
    endCharacter = field("endCharacter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DTMFSpecificationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DTMFSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketLogDestination:
    boto3_raw_data: "type_defs.S3BucketLogDestinationTypeDef" = dataclasses.field()

    s3BucketArn = field("s3BucketArn")
    logPrefix = field("logPrefix")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BucketLogDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketLogDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewCustomVocabularyItem:
    boto3_raw_data: "type_defs.NewCustomVocabularyItemTypeDef" = dataclasses.field()

    phrase = field("phrase")
    weight = field("weight")
    displayAs = field("displayAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NewCustomVocabularyItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NewCustomVocabularyItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomVocabularyItem:
    boto3_raw_data: "type_defs.CustomVocabularyItemTypeDef" = dataclasses.field()

    itemId = field("itemId")
    phrase = field("phrase")
    weight = field("weight")
    displayAs = field("displayAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomVocabularyItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomVocabularyItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedCustomVocabularyItem:
    boto3_raw_data: "type_defs.FailedCustomVocabularyItemTypeDef" = dataclasses.field()

    itemId = field("itemId")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailedCustomVocabularyItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedCustomVocabularyItemTypeDef"]
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
class CustomVocabularyEntryId:
    boto3_raw_data: "type_defs.CustomVocabularyEntryIdTypeDef" = dataclasses.field()

    itemId = field("itemId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomVocabularyEntryIdTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomVocabularyEntryIdTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockGuardrailConfiguration:
    boto3_raw_data: "type_defs.BedrockGuardrailConfigurationTypeDef" = (
        dataclasses.field()
    )

    identifier = field("identifier")
    version = field("version")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BedrockGuardrailConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockGuardrailConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockKnowledgeStoreExactResponseFields:
    boto3_raw_data: "type_defs.BedrockKnowledgeStoreExactResponseFieldsTypeDef" = (
        dataclasses.field()
    )

    answerField = field("answerField")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BedrockKnowledgeStoreExactResponseFieldsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockKnowledgeStoreExactResponseFieldsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotAliasHistoryEvent:
    boto3_raw_data: "type_defs.BotAliasHistoryEventTypeDef" = dataclasses.field()

    botVersion = field("botVersion")
    startDate = field("startDate")
    endDate = field("endDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotAliasHistoryEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotAliasHistoryEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotAliasReplicaSummary:
    boto3_raw_data: "type_defs.BotAliasReplicaSummaryTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botAliasReplicationStatus = field("botAliasReplicationStatus")
    botVersion = field("botVersion")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    failureReasons = field("failureReasons")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotAliasReplicaSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotAliasReplicaSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotAliasSummary:
    boto3_raw_data: "type_defs.BotAliasSummaryTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botAliasName = field("botAliasName")
    description = field("description")
    botVersion = field("botVersion")
    botAliasStatus = field("botAliasStatus")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotAliasSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BotAliasSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotAliasTestExecutionTarget:
    boto3_raw_data: "type_defs.BotAliasTestExecutionTargetTypeDef" = dataclasses.field()

    botId = field("botId")
    botAliasId = field("botAliasId")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotAliasTestExecutionTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotAliasTestExecutionTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotExportSpecification:
    boto3_raw_data: "type_defs.BotExportSpecificationTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotExportSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotExportSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotFilter:
    boto3_raw_data: "type_defs.BotFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BotFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataPrivacy:
    boto3_raw_data: "type_defs.DataPrivacyTypeDef" = dataclasses.field()

    childDirected = field("childDirected")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataPrivacyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataPrivacyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorLogSettings:
    boto3_raw_data: "type_defs.ErrorLogSettingsTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorLogSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ErrorLogSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotLocaleExportSpecification:
    boto3_raw_data: "type_defs.BotLocaleExportSpecificationTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotLocaleExportSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotLocaleExportSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotLocaleFilter:
    boto3_raw_data: "type_defs.BotLocaleFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotLocaleFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BotLocaleFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotLocaleHistoryEvent:
    boto3_raw_data: "type_defs.BotLocaleHistoryEventTypeDef" = dataclasses.field()

    event = field("event")
    eventDate = field("eventDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotLocaleHistoryEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotLocaleHistoryEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceSettings:
    boto3_raw_data: "type_defs.VoiceSettingsTypeDef" = dataclasses.field()

    voiceId = field("voiceId")
    engine = field("engine")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VoiceSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VoiceSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotLocaleSortBy:
    boto3_raw_data: "type_defs.BotLocaleSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotLocaleSortByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BotLocaleSortByTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotLocaleSummary:
    boto3_raw_data: "type_defs.BotLocaleSummaryTypeDef" = dataclasses.field()

    localeId = field("localeId")
    localeName = field("localeName")
    description = field("description")
    botLocaleStatus = field("botLocaleStatus")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    lastBuildSubmittedDateTime = field("lastBuildSubmittedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotLocaleSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotLocaleSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotMember:
    boto3_raw_data: "type_defs.BotMemberTypeDef" = dataclasses.field()

    botMemberId = field("botMemberId")
    botMemberName = field("botMemberName")
    botMemberAliasId = field("botMemberAliasId")
    botMemberAliasName = field("botMemberAliasName")
    botMemberVersion = field("botMemberVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BotMemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentStatistics:
    boto3_raw_data: "type_defs.IntentStatisticsTypeDef" = dataclasses.field()

    discoveredIntentCount = field("discoveredIntentCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotTypeStatistics:
    boto3_raw_data: "type_defs.SlotTypeStatisticsTypeDef" = dataclasses.field()

    discoveredSlotTypeCount = field("discoveredSlotTypeCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotTypeStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotTypeStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotRecommendationSummary:
    boto3_raw_data: "type_defs.BotRecommendationSummaryTypeDef" = dataclasses.field()

    botRecommendationStatus = field("botRecommendationStatus")
    botRecommendationId = field("botRecommendationId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotRecommendationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotRecommendationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotReplicaSummary:
    boto3_raw_data: "type_defs.BotReplicaSummaryTypeDef" = dataclasses.field()

    replicaRegion = field("replicaRegion")
    creationDateTime = field("creationDateTime")
    botReplicaStatus = field("botReplicaStatus")
    failureReasons = field("failureReasons")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotReplicaSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotReplicaSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotSortBy:
    boto3_raw_data: "type_defs.BotSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotSortByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BotSortByTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotSummary:
    boto3_raw_data: "type_defs.BotSummaryTypeDef" = dataclasses.field()

    botId = field("botId")
    botName = field("botName")
    description = field("description")
    botStatus = field("botStatus")
    latestBotVersion = field("latestBotVersion")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    botType = field("botType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BotSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotVersionLocaleDetails:
    boto3_raw_data: "type_defs.BotVersionLocaleDetailsTypeDef" = dataclasses.field()

    sourceBotVersion = field("sourceBotVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotVersionLocaleDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotVersionLocaleDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotVersionReplicaSortBy:
    boto3_raw_data: "type_defs.BotVersionReplicaSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotVersionReplicaSortByTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotVersionReplicaSortByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotVersionReplicaSummary:
    boto3_raw_data: "type_defs.BotVersionReplicaSummaryTypeDef" = dataclasses.field()

    botVersion = field("botVersion")
    botVersionReplicationStatus = field("botVersionReplicationStatus")
    creationDateTime = field("creationDateTime")
    failureReasons = field("failureReasons")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotVersionReplicaSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotVersionReplicaSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotVersionSortBy:
    boto3_raw_data: "type_defs.BotVersionSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotVersionSortByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotVersionSortByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotVersionSummary:
    boto3_raw_data: "type_defs.BotVersionSummaryTypeDef" = dataclasses.field()

    botName = field("botName")
    botVersion = field("botVersion")
    description = field("description")
    botStatus = field("botStatus")
    creationDateTime = field("creationDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BotVersionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildBotLocaleRequest:
    boto3_raw_data: "type_defs.BuildBotLocaleRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BuildBotLocaleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuildBotLocaleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuiltInIntentSortBy:
    boto3_raw_data: "type_defs.BuiltInIntentSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BuiltInIntentSortByTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuiltInIntentSortByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuiltInIntentSummary:
    boto3_raw_data: "type_defs.BuiltInIntentSummaryTypeDef" = dataclasses.field()

    intentSignature = field("intentSignature")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BuiltInIntentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuiltInIntentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuiltInSlotTypeSortBy:
    boto3_raw_data: "type_defs.BuiltInSlotTypeSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BuiltInSlotTypeSortByTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuiltInSlotTypeSortByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuiltInSlotTypeSummary:
    boto3_raw_data: "type_defs.BuiltInSlotTypeSummaryTypeDef" = dataclasses.field()

    slotTypeSignature = field("slotTypeSignature")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BuiltInSlotTypeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuiltInSlotTypeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Button:
    boto3_raw_data: "type_defs.ButtonTypeDef" = dataclasses.field()

    text = field("text")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ButtonTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ButtonTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchLogGroupLogDestination:
    boto3_raw_data: "type_defs.CloudWatchLogGroupLogDestinationTypeDef" = (
        dataclasses.field()
    )

    cloudWatchLogGroupArn = field("cloudWatchLogGroupArn")
    logPrefix = field("logPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CloudWatchLogGroupLogDestinationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchLogGroupLogDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaCodeHook:
    boto3_raw_data: "type_defs.LambdaCodeHookTypeDef" = dataclasses.field()

    lambdaARN = field("lambdaARN")
    codeHookInterfaceVersion = field("codeHookInterfaceVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LambdaCodeHookTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LambdaCodeHookTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubSlotTypeComposition:
    boto3_raw_data: "type_defs.SubSlotTypeCompositionTypeDef" = dataclasses.field()

    name = field("name")
    slotTypeId = field("slotTypeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubSlotTypeCompositionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubSlotTypeCompositionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Condition:
    boto3_raw_data: "type_defs.ConditionTypeDef" = dataclasses.field()

    expressionString = field("expressionString")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLevelIntentClassificationResultItem:
    boto3_raw_data: (
        "type_defs.ConversationLevelIntentClassificationResultItemTypeDef"
    ) = dataclasses.field()

    intentName = field("intentName")
    matchResult = field("matchResult")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConversationLevelIntentClassificationResultItemTypeDef"
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
                "type_defs.ConversationLevelIntentClassificationResultItemTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLevelResultDetail:
    boto3_raw_data: "type_defs.ConversationLevelResultDetailTypeDef" = (
        dataclasses.field()
    )

    endToEndResult = field("endToEndResult")
    speechTranscriptionResult = field("speechTranscriptionResult")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConversationLevelResultDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLevelResultDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLevelSlotResolutionResultItem:
    boto3_raw_data: "type_defs.ConversationLevelSlotResolutionResultItemTypeDef" = (
        dataclasses.field()
    )

    intentName = field("intentName")
    slotName = field("slotName")
    matchResult = field("matchResult")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConversationLevelSlotResolutionResultItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLevelSlotResolutionResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLevelTestResultsFilterBy:
    boto3_raw_data: "type_defs.ConversationLevelTestResultsFilterByTypeDef" = (
        dataclasses.field()
    )

    endToEndResult = field("endToEndResult")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConversationLevelTestResultsFilterByTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLevelTestResultsFilterByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLogsDataSourceFilterByOutput:
    boto3_raw_data: "type_defs.ConversationLogsDataSourceFilterByOutputTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")
    inputMode = field("inputMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConversationLogsDataSourceFilterByOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLogsDataSourceFilterByOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SentimentAnalysisSettings:
    boto3_raw_data: "type_defs.SentimentAnalysisSettingsTypeDef" = dataclasses.field()

    detectSentiment = field("detectSentiment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SentimentAnalysisSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SentimentAnalysisSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotReplicaRequest:
    boto3_raw_data: "type_defs.CreateBotReplicaRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    replicaRegion = field("replicaRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBotReplicaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotReplicaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DialogCodeHookSettings:
    boto3_raw_data: "type_defs.DialogCodeHookSettingsTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DialogCodeHookSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DialogCodeHookSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputContext:
    boto3_raw_data: "type_defs.InputContextTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KendraConfiguration:
    boto3_raw_data: "type_defs.KendraConfigurationTypeDef" = dataclasses.field()

    kendraIndex = field("kendraIndex")
    queryFilterStringEnabled = field("queryFilterStringEnabled")
    queryFilterString = field("queryFilterString")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KendraConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KendraConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputContext:
    boto3_raw_data: "type_defs.OutputContextTypeDef" = dataclasses.field()

    name = field("name")
    timeToLiveInSeconds = field("timeToLiveInSeconds")
    turnsToLive = field("turnsToLive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputContextTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SampleUtterance:
    boto3_raw_data: "type_defs.SampleUtteranceTypeDef" = dataclasses.field()

    utterance = field("utterance")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SampleUtteranceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SampleUtteranceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourcePolicyRequest:
    boto3_raw_data: "type_defs.CreateResourcePolicyRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    policy = field("policy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Principal:
    boto3_raw_data: "type_defs.PrincipalTypeDef" = dataclasses.field()

    service = field("service")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrincipalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrincipalTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultipleValuesSetting:
    boto3_raw_data: "type_defs.MultipleValuesSettingTypeDef" = dataclasses.field()

    allowMultipleValues = field("allowMultipleValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultipleValuesSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultipleValuesSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObfuscationSetting:
    boto3_raw_data: "type_defs.ObfuscationSettingTypeDef" = dataclasses.field()

    obfuscationSettingType = field("obfuscationSettingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObfuscationSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObfuscationSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomPayload:
    boto3_raw_data: "type_defs.CustomPayloadTypeDef" = dataclasses.field()

    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomPayloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomPayloadTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomVocabularyExportSpecification:
    boto3_raw_data: "type_defs.CustomVocabularyExportSpecificationTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomVocabularyExportSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomVocabularyExportSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomVocabularyImportSpecification:
    boto3_raw_data: "type_defs.CustomVocabularyImportSpecificationTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomVocabularyImportSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomVocabularyImportSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QnAKendraConfiguration:
    boto3_raw_data: "type_defs.QnAKendraConfigurationTypeDef" = dataclasses.field()

    kendraIndex = field("kendraIndex")
    queryFilterStringEnabled = field("queryFilterStringEnabled")
    queryFilterString = field("queryFilterString")
    exactResponse = field("exactResponse")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QnAKendraConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QnAKendraConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateRangeFilterOutput:
    boto3_raw_data: "type_defs.DateRangeFilterOutputTypeDef" = dataclasses.field()

    startDateTime = field("startDateTime")
    endDateTime = field("endDateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DateRangeFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DateRangeFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotAliasRequest:
    boto3_raw_data: "type_defs.DeleteBotAliasRequestTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botId = field("botId")
    skipResourceInUseCheck = field("skipResourceInUseCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBotAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotLocaleRequest:
    boto3_raw_data: "type_defs.DeleteBotLocaleRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBotLocaleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotLocaleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotReplicaRequest:
    boto3_raw_data: "type_defs.DeleteBotReplicaRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    replicaRegion = field("replicaRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBotReplicaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotReplicaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotRequest:
    boto3_raw_data: "type_defs.DeleteBotRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    skipResourceInUseCheck = field("skipResourceInUseCheck")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteBotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotVersionRequest:
    boto3_raw_data: "type_defs.DeleteBotVersionRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    skipResourceInUseCheck = field("skipResourceInUseCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBotVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomVocabularyRequest:
    boto3_raw_data: "type_defs.DeleteCustomVocabularyRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCustomVocabularyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomVocabularyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteExportRequest:
    boto3_raw_data: "type_defs.DeleteExportRequestTypeDef" = dataclasses.field()

    exportId = field("exportId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImportRequest:
    boto3_raw_data: "type_defs.DeleteImportRequestTypeDef" = dataclasses.field()

    importId = field("importId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIntentRequest:
    boto3_raw_data: "type_defs.DeleteIntentRequestTypeDef" = dataclasses.field()

    intentId = field("intentId")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIntentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIntentRequestTypeDef"]
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

    resourceArn = field("resourceArn")
    expectedRevisionId = field("expectedRevisionId")

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
class DeleteResourcePolicyStatementRequest:
    boto3_raw_data: "type_defs.DeleteResourcePolicyStatementRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    statementId = field("statementId")
    expectedRevisionId = field("expectedRevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteResourcePolicyStatementRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyStatementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSlotRequest:
    boto3_raw_data: "type_defs.DeleteSlotRequestTypeDef" = dataclasses.field()

    slotId = field("slotId")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    intentId = field("intentId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteSlotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSlotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSlotTypeRequest:
    boto3_raw_data: "type_defs.DeleteSlotTypeRequestTypeDef" = dataclasses.field()

    slotTypeId = field("slotTypeId")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    skipResourceInUseCheck = field("skipResourceInUseCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSlotTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSlotTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTestSetRequest:
    boto3_raw_data: "type_defs.DeleteTestSetRequestTypeDef" = dataclasses.field()

    testSetId = field("testSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTestSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTestSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteUtterancesRequest:
    boto3_raw_data: "type_defs.DeleteUtterancesRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    localeId = field("localeId")
    sessionId = field("sessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteUtterancesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteUtterancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotAliasRequest:
    boto3_raw_data: "type_defs.DescribeBotAliasRequestTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botId = field("botId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParentBotNetwork:
    boto3_raw_data: "type_defs.ParentBotNetworkTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParentBotNetworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParentBotNetworkTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotLocaleRequest:
    boto3_raw_data: "type_defs.DescribeBotLocaleRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotLocaleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotLocaleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotRecommendationRequest:
    boto3_raw_data: "type_defs.DescribeBotRecommendationRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botRecommendationId = field("botRecommendationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBotRecommendationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotRecommendationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionSetting:
    boto3_raw_data: "type_defs.EncryptionSettingTypeDef" = dataclasses.field()

    kmsKeyArn = field("kmsKeyArn")
    botLocaleExportPassword = field("botLocaleExportPassword")
    associatedTranscriptsPassword = field("associatedTranscriptsPassword")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotReplicaRequest:
    boto3_raw_data: "type_defs.DescribeBotReplicaRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    replicaRegion = field("replicaRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotReplicaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotReplicaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotRequest:
    boto3_raw_data: "type_defs.DescribeBotRequestTypeDef" = dataclasses.field()

    botId = field("botId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotResourceGenerationRequest:
    boto3_raw_data: "type_defs.DescribeBotResourceGenerationRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    generationId = field("generationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBotResourceGenerationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotResourceGenerationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotVersionRequest:
    boto3_raw_data: "type_defs.DescribeBotVersionRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomVocabularyMetadataRequest:
    boto3_raw_data: "type_defs.DescribeCustomVocabularyMetadataRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomVocabularyMetadataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomVocabularyMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExportRequest:
    boto3_raw_data: "type_defs.DescribeExportRequestTypeDef" = dataclasses.field()

    exportId = field("exportId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImportRequest:
    boto3_raw_data: "type_defs.DescribeImportRequestTypeDef" = dataclasses.field()

    importId = field("importId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIntentRequest:
    boto3_raw_data: "type_defs.DescribeIntentRequestTypeDef" = dataclasses.field()

    intentId = field("intentId")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIntentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIntentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotPriority:
    boto3_raw_data: "type_defs.SlotPriorityTypeDef" = dataclasses.field()

    priority = field("priority")
    slotId = field("slotId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotPriorityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotPriorityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePolicyRequest:
    boto3_raw_data: "type_defs.DescribeResourcePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourcePolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSlotRequest:
    boto3_raw_data: "type_defs.DescribeSlotRequestTypeDef" = dataclasses.field()

    slotId = field("slotId")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    intentId = field("intentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSlotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSlotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSlotTypeRequest:
    boto3_raw_data: "type_defs.DescribeSlotTypeRequestTypeDef" = dataclasses.field()

    slotTypeId = field("slotTypeId")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSlotTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSlotTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTestExecutionRequest:
    boto3_raw_data: "type_defs.DescribeTestExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    testExecutionId = field("testExecutionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTestExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTestExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTestSetDiscrepancyReportRequest:
    boto3_raw_data: "type_defs.DescribeTestSetDiscrepancyReportRequestTypeDef" = (
        dataclasses.field()
    )

    testSetDiscrepancyReportId = field("testSetDiscrepancyReportId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTestSetDiscrepancyReportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTestSetDiscrepancyReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTestSetGenerationRequest:
    boto3_raw_data: "type_defs.DescribeTestSetGenerationRequestTypeDef" = (
        dataclasses.field()
    )

    testSetGenerationId = field("testSetGenerationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTestSetGenerationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTestSetGenerationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetStorageLocation:
    boto3_raw_data: "type_defs.TestSetStorageLocationTypeDef" = dataclasses.field()

    s3BucketName = field("s3BucketName")
    s3Path = field("s3Path")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestSetStorageLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetStorageLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTestSetRequest:
    boto3_raw_data: "type_defs.DescribeTestSetRequestTypeDef" = dataclasses.field()

    testSetId = field("testSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTestSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTestSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DialogAction:
    boto3_raw_data: "type_defs.DialogActionTypeDef" = dataclasses.field()

    type = field("type")
    slotToElicit = field("slotToElicit")
    suppressNextMessage = field("suppressNextMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DialogActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DialogActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElicitationCodeHookInvocationSetting:
    boto3_raw_data: "type_defs.ElicitationCodeHookInvocationSettingTypeDef" = (
        dataclasses.field()
    )

    enableCodeHookInvocation = field("enableCodeHookInvocation")
    invocationLabel = field("invocationLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ElicitationCodeHookInvocationSettingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElicitationCodeHookInvocationSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExactResponseFields:
    boto3_raw_data: "type_defs.ExactResponseFieldsTypeDef" = dataclasses.field()

    questionField = field("questionField")
    answerField = field("answerField")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExactResponseFieldsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExactResponseFieldsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportFilter:
    boto3_raw_data: "type_defs.ExportFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetExportSpecification:
    boto3_raw_data: "type_defs.TestSetExportSpecificationTypeDef" = dataclasses.field()

    testSetId = field("testSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestSetExportSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetExportSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportSortBy:
    boto3_raw_data: "type_defs.ExportSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportSortByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportSortByTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateBotElementRequest:
    boto3_raw_data: "type_defs.GenerateBotElementRequestTypeDef" = dataclasses.field()

    intentId = field("intentId")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateBotElementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateBotElementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerationSortBy:
    boto3_raw_data: "type_defs.GenerationSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GenerationSortByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerationSortByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerationSummary:
    boto3_raw_data: "type_defs.GenerationSummaryTypeDef" = dataclasses.field()

    generationId = field("generationId")
    generationStatus = field("generationStatus")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GenerationSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTestExecutionArtifactsUrlRequest:
    boto3_raw_data: "type_defs.GetTestExecutionArtifactsUrlRequestTypeDef" = (
        dataclasses.field()
    )

    testExecutionId = field("testExecutionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTestExecutionArtifactsUrlRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTestExecutionArtifactsUrlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrammarSlotTypeSource:
    boto3_raw_data: "type_defs.GrammarSlotTypeSourceTypeDef" = dataclasses.field()

    s3BucketName = field("s3BucketName")
    s3ObjectKey = field("s3ObjectKey")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrammarSlotTypeSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrammarSlotTypeSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportFilter:
    boto3_raw_data: "type_defs.ImportFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportSortBy:
    boto3_raw_data: "type_defs.ImportSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportSortByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportSortByTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportSummary:
    boto3_raw_data: "type_defs.ImportSummaryTypeDef" = dataclasses.field()

    importId = field("importId")
    importedResourceId = field("importedResourceId")
    importedResourceName = field("importedResourceName")
    importStatus = field("importStatus")
    mergeStrategy = field("mergeStrategy")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    importedResourceType = field("importedResourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentClassificationTestResultItemCounts:
    boto3_raw_data: "type_defs.IntentClassificationTestResultItemCountsTypeDef" = (
        dataclasses.field()
    )

    totalResultCount = field("totalResultCount")
    intentMatchResultCounts = field("intentMatchResultCounts")
    speechTranscriptionResultCounts = field("speechTranscriptionResultCounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IntentClassificationTestResultItemCountsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentClassificationTestResultItemCountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentFilter:
    boto3_raw_data: "type_defs.IntentFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntentFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentSortBy:
    boto3_raw_data: "type_defs.IntentSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentSortByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntentSortByTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvokedIntentSample:
    boto3_raw_data: "type_defs.InvokedIntentSampleTypeDef" = dataclasses.field()

    intentName = field("intentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvokedIntentSampleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvokedIntentSampleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotAliasReplicasRequest:
    boto3_raw_data: "type_defs.ListBotAliasReplicasRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    replicaRegion = field("replicaRegion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBotAliasReplicasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotAliasReplicasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotAliasesRequest:
    boto3_raw_data: "type_defs.ListBotAliasesRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBotAliasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotRecommendationsRequest:
    boto3_raw_data: "type_defs.ListBotRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBotRecommendationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotReplicasRequest:
    boto3_raw_data: "type_defs.ListBotReplicasRequestTypeDef" = dataclasses.field()

    botId = field("botId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBotReplicasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotReplicasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomVocabularyItemsRequest:
    boto3_raw_data: "type_defs.ListCustomVocabularyItemsRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCustomVocabularyItemsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomVocabularyItemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendedIntentsRequest:
    boto3_raw_data: "type_defs.ListRecommendedIntentsRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botRecommendationId = field("botRecommendationId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRecommendedIntentsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendedIntentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendedIntentSummary:
    boto3_raw_data: "type_defs.RecommendedIntentSummaryTypeDef" = dataclasses.field()

    intentId = field("intentId")
    intentName = field("intentName")
    sampleUtterancesCount = field("sampleUtterancesCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendedIntentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendedIntentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionDataSortBy:
    boto3_raw_data: "type_defs.SessionDataSortByTypeDef" = dataclasses.field()

    name = field("name")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionDataSortByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionDataSortByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotTypeFilter:
    boto3_raw_data: "type_defs.SlotTypeFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotTypeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotTypeFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotTypeSortBy:
    boto3_raw_data: "type_defs.SlotTypeSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotTypeSortByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotTypeSortByTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotTypeSummary:
    boto3_raw_data: "type_defs.SlotTypeSummaryTypeDef" = dataclasses.field()

    slotTypeId = field("slotTypeId")
    slotTypeName = field("slotTypeName")
    description = field("description")
    parentSlotTypeSignature = field("parentSlotTypeSignature")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    slotTypeCategory = field("slotTypeCategory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotTypeSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotTypeSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotFilter:
    boto3_raw_data: "type_defs.SlotFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    operator = field("operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotSortBy:
    boto3_raw_data: "type_defs.SlotSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotSortByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotSortByTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceARN = field("resourceARN")

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
class TestExecutionSortBy:
    boto3_raw_data: "type_defs.TestExecutionSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestExecutionSortByTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestExecutionSortByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestSetRecordsRequest:
    boto3_raw_data: "type_defs.ListTestSetRecordsRequestTypeDef" = dataclasses.field()

    testSetId = field("testSetId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestSetRecordsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestSetRecordsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetSortBy:
    boto3_raw_data: "type_defs.TestSetSortByTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestSetSortByTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestSetSortByTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtteranceDataSortBy:
    boto3_raw_data: "type_defs.UtteranceDataSortByTypeDef" = dataclasses.field()

    name = field("name")
    order = field("order")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UtteranceDataSortByTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UtteranceDataSortByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlainTextMessage:
    boto3_raw_data: "type_defs.PlainTextMessageTypeDef" = dataclasses.field()

    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlainTextMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlainTextMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SSMLMessage:
    boto3_raw_data: "type_defs.SSMLMessageTypeDef" = dataclasses.field()

    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SSMLMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SSMLMessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NluImprovementSpecification:
    boto3_raw_data: "type_defs.NluImprovementSpecificationTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NluImprovementSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NluImprovementSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverallTestResultItem:
    boto3_raw_data: "type_defs.OverallTestResultItemTypeDef" = dataclasses.field()

    multiTurnConversation = field("multiTurnConversation")
    totalResultCount = field("totalResultCount")
    endToEndResultCounts = field("endToEndResultCounts")
    speechTranscriptionResultCounts = field("speechTranscriptionResultCounts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OverallTestResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OverallTestResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathFormatOutput:
    boto3_raw_data: "type_defs.PathFormatOutputTypeDef" = dataclasses.field()

    objectPrefixes = field("objectPrefixes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PathFormatOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PathFormatOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathFormat:
    boto3_raw_data: "type_defs.PathFormatTypeDef" = dataclasses.field()

    objectPrefixes = field("objectPrefixes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PathFormatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PathFormatTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextInputSpecification:
    boto3_raw_data: "type_defs.TextInputSpecificationTypeDef" = dataclasses.field()

    startTimeoutMs = field("startTimeoutMs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextInputSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextInputSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QInConnectAssistantConfiguration:
    boto3_raw_data: "type_defs.QInConnectAssistantConfigurationTypeDef" = (
        dataclasses.field()
    )

    assistantArn = field("assistantArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QInConnectAssistantConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QInConnectAssistantConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelativeAggregationDuration:
    boto3_raw_data: "type_defs.RelativeAggregationDurationTypeDef" = dataclasses.field()

    timeDimension = field("timeDimension")
    timeValue = field("timeValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelativeAggregationDurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelativeAggregationDurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeHintValue:
    boto3_raw_data: "type_defs.RuntimeHintValueTypeDef" = dataclasses.field()

    phrase = field("phrase")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuntimeHintValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeHintValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SampleValue:
    boto3_raw_data: "type_defs.SampleValueTypeDef" = dataclasses.field()

    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SampleValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SampleValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotDefaultValue:
    boto3_raw_data: "type_defs.SlotDefaultValueTypeDef" = dataclasses.field()

    defaultValue = field("defaultValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotDefaultValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotDefaultValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotResolutionSetting:
    boto3_raw_data: "type_defs.SlotResolutionSettingTypeDef" = dataclasses.field()

    slotResolutionStrategy = field("slotResolutionStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotResolutionSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotResolutionSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotResolutionTestResultItemCounts:
    boto3_raw_data: "type_defs.SlotResolutionTestResultItemCountsTypeDef" = (
        dataclasses.field()
    )

    totalResultCount = field("totalResultCount")
    slotMatchResultCounts = field("slotMatchResultCounts")
    speechTranscriptionResultCounts = field("speechTranscriptionResultCounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SlotResolutionTestResultItemCountsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotResolutionTestResultItemCountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotValue:
    boto3_raw_data: "type_defs.SlotValueTypeDef" = dataclasses.field()

    interpretedValue = field("interpretedValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotValueRegexFilter:
    boto3_raw_data: "type_defs.SlotValueRegexFilterTypeDef" = dataclasses.field()

    pattern = field("pattern")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotValueRegexFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotValueRegexFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBotResourceGenerationRequest:
    boto3_raw_data: "type_defs.StartBotResourceGenerationRequestTypeDef" = (
        dataclasses.field()
    )

    generationInputPrompt = field("generationInputPrompt")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartBotResourceGenerationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBotResourceGenerationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBotRecommendationRequest:
    boto3_raw_data: "type_defs.StopBotRecommendationRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botRecommendationId = field("botRecommendationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopBotRecommendationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopBotRecommendationRequestTypeDef"]
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

    resourceARN = field("resourceARN")
    tags = field("tags")

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
class TestSetIntentDiscrepancyItem:
    boto3_raw_data: "type_defs.TestSetIntentDiscrepancyItemTypeDef" = (
        dataclasses.field()
    )

    intentName = field("intentName")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestSetIntentDiscrepancyItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetIntentDiscrepancyItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetSlotDiscrepancyItem:
    boto3_raw_data: "type_defs.TestSetSlotDiscrepancyItemTypeDef" = dataclasses.field()

    intentName = field("intentName")
    slotName = field("slotName")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestSetSlotDiscrepancyItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetSlotDiscrepancyItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetDiscrepancyReportBotAliasTarget:
    boto3_raw_data: "type_defs.TestSetDiscrepancyReportBotAliasTargetTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botAliasId = field("botAliasId")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TestSetDiscrepancyReportBotAliasTargetTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetDiscrepancyReportBotAliasTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetImportInputLocation:
    boto3_raw_data: "type_defs.TestSetImportInputLocationTypeDef" = dataclasses.field()

    s3BucketName = field("s3BucketName")
    s3Path = field("s3Path")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestSetImportInputLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetImportInputLocationTypeDef"]
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

    resourceARN = field("resourceARN")
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
class UpdateExportRequest:
    boto3_raw_data: "type_defs.UpdateExportRequestTypeDef" = dataclasses.field()

    exportId = field("exportId")
    filePassword = field("filePassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourcePolicyRequest:
    boto3_raw_data: "type_defs.UpdateResourcePolicyRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    policy = field("policy")
    expectedRevisionId = field("expectedRevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTestSetRequest:
    boto3_raw_data: "type_defs.UpdateTestSetRequestTypeDef" = dataclasses.field()

    testSetId = field("testSetId")
    testSetName = field("testSetName")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTestSetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTestSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserTurnSlotOutput:
    boto3_raw_data: "type_defs.UserTurnSlotOutputTypeDef" = dataclasses.field()

    value = field("value")
    values = field("values")
    subSlots = field("subSlots")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserTurnSlotOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserTurnSlotOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtteranceAudioInputSpecification:
    boto3_raw_data: "type_defs.UtteranceAudioInputSpecificationTypeDef" = (
        dataclasses.field()
    )

    audioFileS3Location = field("audioFileS3Location")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UtteranceAudioInputSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UtteranceAudioInputSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AgentTurnResult:
    boto3_raw_data: "type_defs.AgentTurnResultTypeDef" = dataclasses.field()

    expectedAgentPrompt = field("expectedAgentPrompt")
    actualAgentPrompt = field("actualAgentPrompt")

    @cached_property
    def errorDetails(self):  # pragma: no cover
        return ExecutionErrorDetails.make_one(self.boto3_raw_data["errorDetails"])

    actualElicitedSlot = field("actualElicitedSlot")
    actualIntent = field("actualIntent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AgentTurnResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AgentTurnResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentResult:
    boto3_raw_data: "type_defs.AnalyticsIntentResultTypeDef" = dataclasses.field()

    @cached_property
    def binKeys(self):  # pragma: no cover
        return AnalyticsBinKey.make_many(self.boto3_raw_data["binKeys"])

    @cached_property
    def groupByKeys(self):  # pragma: no cover
        return AnalyticsIntentGroupByKey.make_many(self.boto3_raw_data["groupByKeys"])

    @cached_property
    def metricsResults(self):  # pragma: no cover
        return AnalyticsIntentMetricResult.make_many(
            self.boto3_raw_data["metricsResults"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsIntentResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsIntentStageResult:
    boto3_raw_data: "type_defs.AnalyticsIntentStageResultTypeDef" = dataclasses.field()

    @cached_property
    def binKeys(self):  # pragma: no cover
        return AnalyticsBinKey.make_many(self.boto3_raw_data["binKeys"])

    @cached_property
    def groupByKeys(self):  # pragma: no cover
        return AnalyticsIntentStageGroupByKey.make_many(
            self.boto3_raw_data["groupByKeys"]
        )

    @cached_property
    def metricsResults(self):  # pragma: no cover
        return AnalyticsIntentStageMetricResult.make_many(
            self.boto3_raw_data["metricsResults"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsIntentStageResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsIntentStageResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsSessionResult:
    boto3_raw_data: "type_defs.AnalyticsSessionResultTypeDef" = dataclasses.field()

    @cached_property
    def binKeys(self):  # pragma: no cover
        return AnalyticsBinKey.make_many(self.boto3_raw_data["binKeys"])

    @cached_property
    def groupByKeys(self):  # pragma: no cover
        return AnalyticsSessionGroupByKey.make_many(self.boto3_raw_data["groupByKeys"])

    @cached_property
    def metricsResults(self):  # pragma: no cover
        return AnalyticsSessionMetricResult.make_many(
            self.boto3_raw_data["metricsResults"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsSessionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsSessionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalyticsUtteranceResult:
    boto3_raw_data: "type_defs.AnalyticsUtteranceResultTypeDef" = dataclasses.field()

    @cached_property
    def binKeys(self):  # pragma: no cover
        return AnalyticsBinKey.make_many(self.boto3_raw_data["binKeys"])

    @cached_property
    def groupByKeys(self):  # pragma: no cover
        return AnalyticsUtteranceGroupByKey.make_many(
            self.boto3_raw_data["groupByKeys"]
        )

    @cached_property
    def metricsResults(self):  # pragma: no cover
        return AnalyticsUtteranceMetricResult.make_many(
            self.boto3_raw_data["metricsResults"]
        )

    @cached_property
    def attributeResults(self):  # pragma: no cover
        return AnalyticsUtteranceAttributeResult.make_many(
            self.boto3_raw_data["attributeResults"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalyticsUtteranceResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalyticsUtteranceResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAssociatedTranscriptsRequest:
    boto3_raw_data: "type_defs.SearchAssociatedTranscriptsRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botRecommendationId = field("botRecommendationId")

    @cached_property
    def filters(self):  # pragma: no cover
        return AssociatedTranscriptFilter.make_many(self.boto3_raw_data["filters"])

    searchOrder = field("searchOrder")
    maxResults = field("maxResults")
    nextIndex = field("nextIndex")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchAssociatedTranscriptsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAssociatedTranscriptsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioAndDTMFInputSpecification:
    boto3_raw_data: "type_defs.AudioAndDTMFInputSpecificationTypeDef" = (
        dataclasses.field()
    )

    startTimeoutMs = field("startTimeoutMs")

    @cached_property
    def audioSpecification(self):  # pragma: no cover
        return AudioSpecification.make_one(self.boto3_raw_data["audioSpecification"])

    @cached_property
    def dtmfSpecification(self):  # pragma: no cover
        return DTMFSpecification.make_one(self.boto3_raw_data["dtmfSpecification"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AudioAndDTMFInputSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioAndDTMFInputSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioLogDestination:
    boto3_raw_data: "type_defs.AudioLogDestinationTypeDef" = dataclasses.field()

    @cached_property
    def s3Bucket(self):  # pragma: no cover
        return S3BucketLogDestination.make_one(self.boto3_raw_data["s3Bucket"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AudioLogDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioLogDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateCustomVocabularyItemRequest:
    boto3_raw_data: "type_defs.BatchCreateCustomVocabularyItemRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def customVocabularyItemList(self):  # pragma: no cover
        return NewCustomVocabularyItem.make_many(
            self.boto3_raw_data["customVocabularyItemList"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateCustomVocabularyItemRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateCustomVocabularyItemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateCustomVocabularyItemRequest:
    boto3_raw_data: "type_defs.BatchUpdateCustomVocabularyItemRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def customVocabularyItemList(self):  # pragma: no cover
        return CustomVocabularyItem.make_many(
            self.boto3_raw_data["customVocabularyItemList"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateCustomVocabularyItemRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateCustomVocabularyItemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateCustomVocabularyItemResponse:
    boto3_raw_data: "type_defs.BatchCreateCustomVocabularyItemResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def errors(self):  # pragma: no cover
        return FailedCustomVocabularyItem.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def resources(self):  # pragma: no cover
        return CustomVocabularyItem.make_many(self.boto3_raw_data["resources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateCustomVocabularyItemResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateCustomVocabularyItemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteCustomVocabularyItemResponse:
    boto3_raw_data: "type_defs.BatchDeleteCustomVocabularyItemResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def errors(self):  # pragma: no cover
        return FailedCustomVocabularyItem.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def resources(self):  # pragma: no cover
        return CustomVocabularyItem.make_many(self.boto3_raw_data["resources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteCustomVocabularyItemResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteCustomVocabularyItemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateCustomVocabularyItemResponse:
    boto3_raw_data: "type_defs.BatchUpdateCustomVocabularyItemResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def errors(self):  # pragma: no cover
        return FailedCustomVocabularyItem.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def resources(self):  # pragma: no cover
        return CustomVocabularyItem.make_many(self.boto3_raw_data["resources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateCustomVocabularyItemResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateCustomVocabularyItemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildBotLocaleResponse:
    boto3_raw_data: "type_defs.BuildBotLocaleResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botLocaleStatus = field("botLocaleStatus")
    lastBuildSubmittedDateTime = field("lastBuildSubmittedDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BuildBotLocaleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuildBotLocaleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotReplicaResponse:
    boto3_raw_data: "type_defs.CreateBotReplicaResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    replicaRegion = field("replicaRegion")
    sourceRegion = field("sourceRegion")
    creationDateTime = field("creationDateTime")
    botReplicaStatus = field("botReplicaStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBotReplicaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotReplicaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourcePolicyResponse:
    boto3_raw_data: "type_defs.CreateResourcePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    revisionId = field("revisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourcePolicyStatementResponse:
    boto3_raw_data: "type_defs.CreateResourcePolicyStatementResponseTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    revisionId = field("revisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateResourcePolicyStatementResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourcePolicyStatementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUploadUrlResponse:
    boto3_raw_data: "type_defs.CreateUploadUrlResponseTypeDef" = dataclasses.field()

    importId = field("importId")
    uploadUrl = field("uploadUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUploadUrlResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUploadUrlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotAliasResponse:
    boto3_raw_data: "type_defs.DeleteBotAliasResponseTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botId = field("botId")
    botAliasStatus = field("botAliasStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBotAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotLocaleResponse:
    boto3_raw_data: "type_defs.DeleteBotLocaleResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botLocaleStatus = field("botLocaleStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBotLocaleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotLocaleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotReplicaResponse:
    boto3_raw_data: "type_defs.DeleteBotReplicaResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    replicaRegion = field("replicaRegion")
    botReplicaStatus = field("botReplicaStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBotReplicaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotReplicaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotResponse:
    boto3_raw_data: "type_defs.DeleteBotResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botStatus = field("botStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteBotResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBotVersionResponse:
    boto3_raw_data: "type_defs.DeleteBotVersionResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    botStatus = field("botStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBotVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBotVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomVocabularyResponse:
    boto3_raw_data: "type_defs.DeleteCustomVocabularyResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    customVocabularyStatus = field("customVocabularyStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCustomVocabularyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomVocabularyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteExportResponse:
    boto3_raw_data: "type_defs.DeleteExportResponseTypeDef" = dataclasses.field()

    exportId = field("exportId")
    exportStatus = field("exportStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteExportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImportResponse:
    boto3_raw_data: "type_defs.DeleteImportResponseTypeDef" = dataclasses.field()

    importId = field("importId")
    importStatus = field("importStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyResponse:
    boto3_raw_data: "type_defs.DeleteResourcePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    revisionId = field("revisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyStatementResponse:
    boto3_raw_data: "type_defs.DeleteResourcePolicyStatementResponseTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    revisionId = field("revisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteResourcePolicyStatementResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyStatementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotReplicaResponse:
    boto3_raw_data: "type_defs.DescribeBotReplicaResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    replicaRegion = field("replicaRegion")
    sourceRegion = field("sourceRegion")
    creationDateTime = field("creationDateTime")
    botReplicaStatus = field("botReplicaStatus")
    failureReasons = field("failureReasons")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotReplicaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotReplicaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotResourceGenerationResponse:
    boto3_raw_data: "type_defs.DescribeBotResourceGenerationResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    generationId = field("generationId")
    failureReasons = field("failureReasons")
    generationStatus = field("generationStatus")
    generationInputPrompt = field("generationInputPrompt")
    generatedBotLocaleUrl = field("generatedBotLocaleUrl")
    creationDateTime = field("creationDateTime")
    modelArn = field("modelArn")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBotResourceGenerationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotResourceGenerationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomVocabularyMetadataResponse:
    boto3_raw_data: "type_defs.DescribeCustomVocabularyMetadataResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    customVocabularyStatus = field("customVocabularyStatus")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomVocabularyMetadataResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomVocabularyMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePolicyResponse:
    boto3_raw_data: "type_defs.DescribeResourcePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    policy = field("policy")
    revisionId = field("revisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourcePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePolicyResponseTypeDef"]
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
class GetTestExecutionArtifactsUrlResponse:
    boto3_raw_data: "type_defs.GetTestExecutionArtifactsUrlResponseTypeDef" = (
        dataclasses.field()
    )

    testExecutionId = field("testExecutionId")
    downloadArtifactsUrl = field("downloadArtifactsUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTestExecutionArtifactsUrlResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTestExecutionArtifactsUrlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomVocabularyItemsResponse:
    boto3_raw_data: "type_defs.ListCustomVocabularyItemsResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def customVocabularyItems(self):  # pragma: no cover
        return CustomVocabularyItem.make_many(
            self.boto3_raw_data["customVocabularyItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomVocabularyItemsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomVocabularyItemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntentPathsResponse:
    boto3_raw_data: "type_defs.ListIntentPathsResponseTypeDef" = dataclasses.field()

    @cached_property
    def nodeSummaries(self):  # pragma: no cover
        return AnalyticsIntentNodeSummary.make_many(
            self.boto3_raw_data["nodeSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIntentPathsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntentPathsResponseTypeDef"]
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

    tags = field("tags")

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
class SearchAssociatedTranscriptsResponse:
    boto3_raw_data: "type_defs.SearchAssociatedTranscriptsResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botRecommendationId = field("botRecommendationId")
    nextIndex = field("nextIndex")

    @cached_property
    def associatedTranscripts(self):  # pragma: no cover
        return AssociatedTranscript.make_many(
            self.boto3_raw_data["associatedTranscripts"]
        )

    totalResults = field("totalResults")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchAssociatedTranscriptsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAssociatedTranscriptsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBotResourceGenerationResponse:
    boto3_raw_data: "type_defs.StartBotResourceGenerationResponseTypeDef" = (
        dataclasses.field()
    )

    generationInputPrompt = field("generationInputPrompt")
    generationId = field("generationId")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    generationStatus = field("generationStatus")
    creationDateTime = field("creationDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartBotResourceGenerationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBotResourceGenerationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopBotRecommendationResponse:
    boto3_raw_data: "type_defs.StopBotRecommendationResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botRecommendationStatus = field("botRecommendationStatus")
    botRecommendationId = field("botRecommendationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopBotRecommendationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopBotRecommendationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourcePolicyResponse:
    boto3_raw_data: "type_defs.UpdateResourcePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    revisionId = field("revisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteCustomVocabularyItemRequest:
    boto3_raw_data: "type_defs.BatchDeleteCustomVocabularyItemRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def customVocabularyItemList(self):  # pragma: no cover
        return CustomVocabularyEntryId.make_many(
            self.boto3_raw_data["customVocabularyItemList"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteCustomVocabularyItemRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteCustomVocabularyItemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockModelSpecification:
    boto3_raw_data: "type_defs.BedrockModelSpecificationTypeDef" = dataclasses.field()

    modelArn = field("modelArn")

    @cached_property
    def guardrail(self):  # pragma: no cover
        return BedrockGuardrailConfiguration.make_one(self.boto3_raw_data["guardrail"])

    traceStatus = field("traceStatus")
    customPrompt = field("customPrompt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BedrockModelSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockModelSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockKnowledgeStoreConfiguration:
    boto3_raw_data: "type_defs.BedrockKnowledgeStoreConfigurationTypeDef" = (
        dataclasses.field()
    )

    bedrockKnowledgeBaseArn = field("bedrockKnowledgeBaseArn")
    exactResponse = field("exactResponse")

    @cached_property
    def exactResponseFields(self):  # pragma: no cover
        return BedrockKnowledgeStoreExactResponseFields.make_one(
            self.boto3_raw_data["exactResponseFields"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BedrockKnowledgeStoreConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockKnowledgeStoreConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotAliasReplicasResponse:
    boto3_raw_data: "type_defs.ListBotAliasReplicasResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    sourceRegion = field("sourceRegion")
    replicaRegion = field("replicaRegion")

    @cached_property
    def botAliasReplicaSummaries(self):  # pragma: no cover
        return BotAliasReplicaSummary.make_many(
            self.boto3_raw_data["botAliasReplicaSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBotAliasReplicasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotAliasReplicasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotAliasesResponse:
    boto3_raw_data: "type_defs.ListBotAliasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def botAliasSummaries(self):  # pragma: no cover
        return BotAliasSummary.make_many(self.boto3_raw_data["botAliasSummaries"])

    botId = field("botId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBotAliasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestExecutionTarget:
    boto3_raw_data: "type_defs.TestExecutionTargetTypeDef" = dataclasses.field()

    @cached_property
    def botAliasTarget(self):  # pragma: no cover
        return BotAliasTestExecutionTarget.make_one(
            self.boto3_raw_data["botAliasTarget"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestExecutionTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestExecutionTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotImportSpecificationOutput:
    boto3_raw_data: "type_defs.BotImportSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    botName = field("botName")
    roleArn = field("roleArn")

    @cached_property
    def dataPrivacy(self):  # pragma: no cover
        return DataPrivacy.make_one(self.boto3_raw_data["dataPrivacy"])

    @cached_property
    def errorLogSettings(self):  # pragma: no cover
        return ErrorLogSettings.make_one(self.boto3_raw_data["errorLogSettings"])

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    botTags = field("botTags")
    testBotAliasTags = field("testBotAliasTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotImportSpecificationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotImportSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotImportSpecification:
    boto3_raw_data: "type_defs.BotImportSpecificationTypeDef" = dataclasses.field()

    botName = field("botName")
    roleArn = field("roleArn")

    @cached_property
    def dataPrivacy(self):  # pragma: no cover
        return DataPrivacy.make_one(self.boto3_raw_data["dataPrivacy"])

    @cached_property
    def errorLogSettings(self):  # pragma: no cover
        return ErrorLogSettings.make_one(self.boto3_raw_data["errorLogSettings"])

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    botTags = field("botTags")
    testBotAliasTags = field("testBotAliasTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotImportSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotImportSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotLocaleImportSpecification:
    boto3_raw_data: "type_defs.BotLocaleImportSpecificationTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    nluIntentConfidenceThreshold = field("nluIntentConfidenceThreshold")

    @cached_property
    def voiceSettings(self):  # pragma: no cover
        return VoiceSettings.make_one(self.boto3_raw_data["voiceSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotLocaleImportSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotLocaleImportSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotLocalesRequest:
    boto3_raw_data: "type_defs.ListBotLocalesRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return BotLocaleSortBy.make_one(self.boto3_raw_data["sortBy"])

    @cached_property
    def filters(self):  # pragma: no cover
        return BotLocaleFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBotLocalesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotLocalesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotLocalesResponse:
    boto3_raw_data: "type_defs.ListBotLocalesResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")

    @cached_property
    def botLocaleSummaries(self):  # pragma: no cover
        return BotLocaleSummary.make_many(self.boto3_raw_data["botLocaleSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBotLocalesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotLocalesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotRequest:
    boto3_raw_data: "type_defs.CreateBotRequestTypeDef" = dataclasses.field()

    botName = field("botName")
    roleArn = field("roleArn")

    @cached_property
    def dataPrivacy(self):  # pragma: no cover
        return DataPrivacy.make_one(self.boto3_raw_data["dataPrivacy"])

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    description = field("description")
    botTags = field("botTags")
    testBotAliasTags = field("testBotAliasTags")
    botType = field("botType")

    @cached_property
    def botMembers(self):  # pragma: no cover
        return BotMember.make_many(self.boto3_raw_data["botMembers"])

    @cached_property
    def errorLogSettings(self):  # pragma: no cover
        return ErrorLogSettings.make_one(self.boto3_raw_data["errorLogSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateBotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotResponse:
    boto3_raw_data: "type_defs.CreateBotResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botName = field("botName")
    description = field("description")
    roleArn = field("roleArn")

    @cached_property
    def dataPrivacy(self):  # pragma: no cover
        return DataPrivacy.make_one(self.boto3_raw_data["dataPrivacy"])

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    botStatus = field("botStatus")
    creationDateTime = field("creationDateTime")
    botTags = field("botTags")
    testBotAliasTags = field("testBotAliasTags")
    botType = field("botType")

    @cached_property
    def botMembers(self):  # pragma: no cover
        return BotMember.make_many(self.boto3_raw_data["botMembers"])

    @cached_property
    def errorLogSettings(self):  # pragma: no cover
        return ErrorLogSettings.make_one(self.boto3_raw_data["errorLogSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateBotResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotResponse:
    boto3_raw_data: "type_defs.DescribeBotResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botName = field("botName")
    description = field("description")
    roleArn = field("roleArn")

    @cached_property
    def dataPrivacy(self):  # pragma: no cover
        return DataPrivacy.make_one(self.boto3_raw_data["dataPrivacy"])

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    botStatus = field("botStatus")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    botType = field("botType")

    @cached_property
    def botMembers(self):  # pragma: no cover
        return BotMember.make_many(self.boto3_raw_data["botMembers"])

    failureReasons = field("failureReasons")

    @cached_property
    def errorLogSettings(self):  # pragma: no cover
        return ErrorLogSettings.make_one(self.boto3_raw_data["errorLogSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBotRequest:
    boto3_raw_data: "type_defs.UpdateBotRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botName = field("botName")
    roleArn = field("roleArn")

    @cached_property
    def dataPrivacy(self):  # pragma: no cover
        return DataPrivacy.make_one(self.boto3_raw_data["dataPrivacy"])

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    description = field("description")
    botType = field("botType")

    @cached_property
    def botMembers(self):  # pragma: no cover
        return BotMember.make_many(self.boto3_raw_data["botMembers"])

    @cached_property
    def errorLogSettings(self):  # pragma: no cover
        return ErrorLogSettings.make_one(self.boto3_raw_data["errorLogSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateBotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBotResponse:
    boto3_raw_data: "type_defs.UpdateBotResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botName = field("botName")
    description = field("description")
    roleArn = field("roleArn")

    @cached_property
    def dataPrivacy(self):  # pragma: no cover
        return DataPrivacy.make_one(self.boto3_raw_data["dataPrivacy"])

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    botStatus = field("botStatus")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    botType = field("botType")

    @cached_property
    def botMembers(self):  # pragma: no cover
        return BotMember.make_many(self.boto3_raw_data["botMembers"])

    @cached_property
    def errorLogSettings(self):  # pragma: no cover
        return ErrorLogSettings.make_one(self.boto3_raw_data["errorLogSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateBotResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotRecommendationResultStatistics:
    boto3_raw_data: "type_defs.BotRecommendationResultStatisticsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def intents(self):  # pragma: no cover
        return IntentStatistics.make_one(self.boto3_raw_data["intents"])

    @cached_property
    def slotTypes(self):  # pragma: no cover
        return SlotTypeStatistics.make_one(self.boto3_raw_data["slotTypes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BotRecommendationResultStatisticsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotRecommendationResultStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotRecommendationsResponse:
    boto3_raw_data: "type_defs.ListBotRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def botRecommendationSummaries(self):  # pragma: no cover
        return BotRecommendationSummary.make_many(
            self.boto3_raw_data["botRecommendationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBotRecommendationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotReplicasResponse:
    boto3_raw_data: "type_defs.ListBotReplicasResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    sourceRegion = field("sourceRegion")

    @cached_property
    def botReplicaSummaries(self):  # pragma: no cover
        return BotReplicaSummary.make_many(self.boto3_raw_data["botReplicaSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBotReplicasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotReplicasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotsRequest:
    boto3_raw_data: "type_defs.ListBotsRequestTypeDef" = dataclasses.field()

    @cached_property
    def sortBy(self):  # pragma: no cover
        return BotSortBy.make_one(self.boto3_raw_data["sortBy"])

    @cached_property
    def filters(self):  # pragma: no cover
        return BotFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBotsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListBotsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotsResponse:
    boto3_raw_data: "type_defs.ListBotsResponseTypeDef" = dataclasses.field()

    @cached_property
    def botSummaries(self):  # pragma: no cover
        return BotSummary.make_many(self.boto3_raw_data["botSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListBotsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotVersionRequest:
    boto3_raw_data: "type_defs.CreateBotVersionRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersionLocaleSpecification = field("botVersionLocaleSpecification")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBotVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotVersionResponse:
    boto3_raw_data: "type_defs.CreateBotVersionResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    description = field("description")
    botVersion = field("botVersion")
    botVersionLocaleSpecification = field("botVersionLocaleSpecification")
    botStatus = field("botStatus")
    creationDateTime = field("creationDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBotVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotVersionReplicasRequest:
    boto3_raw_data: "type_defs.ListBotVersionReplicasRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    replicaRegion = field("replicaRegion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return BotVersionReplicaSortBy.make_one(self.boto3_raw_data["sortBy"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBotVersionReplicasRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotVersionReplicasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotVersionReplicasResponse:
    boto3_raw_data: "type_defs.ListBotVersionReplicasResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    sourceRegion = field("sourceRegion")
    replicaRegion = field("replicaRegion")

    @cached_property
    def botVersionReplicaSummaries(self):  # pragma: no cover
        return BotVersionReplicaSummary.make_many(
            self.boto3_raw_data["botVersionReplicaSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBotVersionReplicasResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotVersionReplicasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotVersionsRequest:
    boto3_raw_data: "type_defs.ListBotVersionsRequestTypeDef" = dataclasses.field()

    botId = field("botId")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return BotVersionSortBy.make_one(self.boto3_raw_data["sortBy"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBotVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotVersionsResponse:
    boto3_raw_data: "type_defs.ListBotVersionsResponseTypeDef" = dataclasses.field()

    botId = field("botId")

    @cached_property
    def botVersionSummaries(self):  # pragma: no cover
        return BotVersionSummary.make_many(self.boto3_raw_data["botVersionSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBotVersionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuiltInIntentsRequest:
    boto3_raw_data: "type_defs.ListBuiltInIntentsRequestTypeDef" = dataclasses.field()

    localeId = field("localeId")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return BuiltInIntentSortBy.make_one(self.boto3_raw_data["sortBy"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBuiltInIntentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuiltInIntentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuiltInIntentsResponse:
    boto3_raw_data: "type_defs.ListBuiltInIntentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def builtInIntentSummaries(self):  # pragma: no cover
        return BuiltInIntentSummary.make_many(
            self.boto3_raw_data["builtInIntentSummaries"]
        )

    localeId = field("localeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBuiltInIntentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuiltInIntentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuiltInSlotTypesRequest:
    boto3_raw_data: "type_defs.ListBuiltInSlotTypesRequestTypeDef" = dataclasses.field()

    localeId = field("localeId")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return BuiltInSlotTypeSortBy.make_one(self.boto3_raw_data["sortBy"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBuiltInSlotTypesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuiltInSlotTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBuiltInSlotTypesResponse:
    boto3_raw_data: "type_defs.ListBuiltInSlotTypesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def builtInSlotTypeSummaries(self):  # pragma: no cover
        return BuiltInSlotTypeSummary.make_many(
            self.boto3_raw_data["builtInSlotTypeSummaries"]
        )

    localeId = field("localeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBuiltInSlotTypesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBuiltInSlotTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageResponseCardOutput:
    boto3_raw_data: "type_defs.ImageResponseCardOutputTypeDef" = dataclasses.field()

    title = field("title")
    subtitle = field("subtitle")
    imageUrl = field("imageUrl")

    @cached_property
    def buttons(self):  # pragma: no cover
        return Button.make_many(self.boto3_raw_data["buttons"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImageResponseCardOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageResponseCardOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImageResponseCard:
    boto3_raw_data: "type_defs.ImageResponseCardTypeDef" = dataclasses.field()

    title = field("title")
    subtitle = field("subtitle")
    imageUrl = field("imageUrl")

    @cached_property
    def buttons(self):  # pragma: no cover
        return Button.make_many(self.boto3_raw_data["buttons"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImageResponseCardTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImageResponseCardTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextLogDestination:
    boto3_raw_data: "type_defs.TextLogDestinationTypeDef" = dataclasses.field()

    @cached_property
    def cloudWatch(self):  # pragma: no cover
        return CloudWatchLogGroupLogDestination.make_one(
            self.boto3_raw_data["cloudWatch"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextLogDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextLogDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodeHookSpecification:
    boto3_raw_data: "type_defs.CodeHookSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def lambdaCodeHook(self):  # pragma: no cover
        return LambdaCodeHook.make_one(self.boto3_raw_data["lambdaCodeHook"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodeHookSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodeHookSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositeSlotTypeSettingOutput:
    boto3_raw_data: "type_defs.CompositeSlotTypeSettingOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def subSlots(self):  # pragma: no cover
        return SubSlotTypeComposition.make_many(self.boto3_raw_data["subSlots"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CompositeSlotTypeSettingOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositeSlotTypeSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompositeSlotTypeSetting:
    boto3_raw_data: "type_defs.CompositeSlotTypeSettingTypeDef" = dataclasses.field()

    @cached_property
    def subSlots(self):  # pragma: no cover
        return SubSlotTypeComposition.make_many(self.boto3_raw_data["subSlots"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompositeSlotTypeSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompositeSlotTypeSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLevelTestResultItem:
    boto3_raw_data: "type_defs.ConversationLevelTestResultItemTypeDef" = (
        dataclasses.field()
    )

    conversationId = field("conversationId")
    endToEndResult = field("endToEndResult")

    @cached_property
    def intentClassificationResults(self):  # pragma: no cover
        return ConversationLevelIntentClassificationResultItem.make_many(
            self.boto3_raw_data["intentClassificationResults"]
        )

    @cached_property
    def slotResolutionResults(self):  # pragma: no cover
        return ConversationLevelSlotResolutionResultItem.make_many(
            self.boto3_raw_data["slotResolutionResults"]
        )

    speechTranscriptionResult = field("speechTranscriptionResult")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConversationLevelTestResultItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLevelTestResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestExecutionResultFilterBy:
    boto3_raw_data: "type_defs.TestExecutionResultFilterByTypeDef" = dataclasses.field()

    resultTypeFilter = field("resultTypeFilter")

    @cached_property
    def conversationLevelTestResultsFilterBy(self):  # pragma: no cover
        return ConversationLevelTestResultsFilterBy.make_one(
            self.boto3_raw_data["conversationLevelTestResultsFilterBy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestExecutionResultFilterByTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestExecutionResultFilterByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLogsDataSourceOutput:
    boto3_raw_data: "type_defs.ConversationLogsDataSourceOutputTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botAliasId = field("botAliasId")
    localeId = field("localeId")

    @cached_property
    def filter(self):  # pragma: no cover
        return ConversationLogsDataSourceFilterByOutput.make_one(
            self.boto3_raw_data["filter"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConversationLogsDataSourceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLogsDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLogsDataSourceFilterBy:
    boto3_raw_data: "type_defs.ConversationLogsDataSourceFilterByTypeDef" = (
        dataclasses.field()
    )

    startTime = field("startTime")
    endTime = field("endTime")
    inputMode = field("inputMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConversationLogsDataSourceFilterByTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLogsDataSourceFilterByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateRangeFilter:
    boto3_raw_data: "type_defs.DateRangeFilterTypeDef" = dataclasses.field()

    startDateTime = field("startDateTime")
    endDateTime = field("endDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateRangeFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateRangeFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntentMetricsRequest:
    boto3_raw_data: "type_defs.ListIntentMetricsRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    startDateTime = field("startDateTime")
    endDateTime = field("endDateTime")

    @cached_property
    def metrics(self):  # pragma: no cover
        return AnalyticsIntentMetric.make_many(self.boto3_raw_data["metrics"])

    @cached_property
    def binBy(self):  # pragma: no cover
        return AnalyticsBinBySpecification.make_many(self.boto3_raw_data["binBy"])

    @cached_property
    def groupBy(self):  # pragma: no cover
        return AnalyticsIntentGroupBySpecification.make_many(
            self.boto3_raw_data["groupBy"]
        )

    @cached_property
    def filters(self):  # pragma: no cover
        return AnalyticsIntentFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIntentMetricsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntentMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntentPathsRequest:
    boto3_raw_data: "type_defs.ListIntentPathsRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    startDateTime = field("startDateTime")
    endDateTime = field("endDateTime")
    intentPath = field("intentPath")

    @cached_property
    def filters(self):  # pragma: no cover
        return AnalyticsPathFilter.make_many(self.boto3_raw_data["filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIntentPathsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntentPathsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntentStageMetricsRequest:
    boto3_raw_data: "type_defs.ListIntentStageMetricsRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    startDateTime = field("startDateTime")
    endDateTime = field("endDateTime")

    @cached_property
    def metrics(self):  # pragma: no cover
        return AnalyticsIntentStageMetric.make_many(self.boto3_raw_data["metrics"])

    @cached_property
    def binBy(self):  # pragma: no cover
        return AnalyticsBinBySpecification.make_many(self.boto3_raw_data["binBy"])

    @cached_property
    def groupBy(self):  # pragma: no cover
        return AnalyticsIntentStageGroupBySpecification.make_many(
            self.boto3_raw_data["groupBy"]
        )

    @cached_property
    def filters(self):  # pragma: no cover
        return AnalyticsIntentStageFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIntentStageMetricsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntentStageMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionMetricsRequest:
    boto3_raw_data: "type_defs.ListSessionMetricsRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    startDateTime = field("startDateTime")
    endDateTime = field("endDateTime")

    @cached_property
    def metrics(self):  # pragma: no cover
        return AnalyticsSessionMetric.make_many(self.boto3_raw_data["metrics"])

    @cached_property
    def binBy(self):  # pragma: no cover
        return AnalyticsBinBySpecification.make_many(self.boto3_raw_data["binBy"])

    @cached_property
    def groupBy(self):  # pragma: no cover
        return AnalyticsSessionGroupBySpecification.make_many(
            self.boto3_raw_data["groupBy"]
        )

    @cached_property
    def filters(self):  # pragma: no cover
        return AnalyticsSessionFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionMetricsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUtteranceMetricsRequest:
    boto3_raw_data: "type_defs.ListUtteranceMetricsRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    startDateTime = field("startDateTime")
    endDateTime = field("endDateTime")

    @cached_property
    def metrics(self):  # pragma: no cover
        return AnalyticsUtteranceMetric.make_many(self.boto3_raw_data["metrics"])

    @cached_property
    def binBy(self):  # pragma: no cover
        return AnalyticsBinBySpecification.make_many(self.boto3_raw_data["binBy"])

    @cached_property
    def groupBy(self):  # pragma: no cover
        return AnalyticsUtteranceGroupBySpecification.make_many(
            self.boto3_raw_data["groupBy"]
        )

    @cached_property
    def attributes(self):  # pragma: no cover
        return AnalyticsUtteranceAttribute.make_many(self.boto3_raw_data["attributes"])

    @cached_property
    def filters(self):  # pragma: no cover
        return AnalyticsUtteranceFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUtteranceMetricsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUtteranceMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentSummary:
    boto3_raw_data: "type_defs.IntentSummaryTypeDef" = dataclasses.field()

    intentId = field("intentId")
    intentName = field("intentName")
    description = field("description")
    parentIntentSignature = field("parentIntentSignature")

    @cached_property
    def inputContexts(self):  # pragma: no cover
        return InputContext.make_many(self.boto3_raw_data["inputContexts"])

    @cached_property
    def outputContexts(self):  # pragma: no cover
        return OutputContext.make_many(self.boto3_raw_data["outputContexts"])

    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntentSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateBotElementResponse:
    boto3_raw_data: "type_defs.GenerateBotElementResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    intentId = field("intentId")

    @cached_property
    def sampleUtterances(self):  # pragma: no cover
        return SampleUtterance.make_many(self.boto3_raw_data["sampleUtterances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateBotElementResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateBotElementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateResourcePolicyStatementRequest:
    boto3_raw_data: "type_defs.CreateResourcePolicyStatementRequestTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    statementId = field("statementId")
    effect = field("effect")

    @cached_property
    def principal(self):  # pragma: no cover
        return Principal.make_many(self.boto3_raw_data["principal"])

    action = field("action")
    condition = field("condition")
    expectedRevisionId = field("expectedRevisionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateResourcePolicyStatementRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateResourcePolicyStatementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LexTranscriptFilterOutput:
    boto3_raw_data: "type_defs.LexTranscriptFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def dateRangeFilter(self):  # pragma: no cover
        return DateRangeFilterOutput.make_one(self.boto3_raw_data["dateRangeFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LexTranscriptFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LexTranscriptFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotAliasRequestWait:
    boto3_raw_data: "type_defs.DescribeBotAliasRequestWaitTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botId = field("botId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotAliasRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotAliasRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotLocaleRequestWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeBotLocaleRequestWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBotLocaleRequestWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotLocaleRequestWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotLocaleRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeBotLocaleRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBotLocaleRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotLocaleRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotLocaleRequestWait:
    boto3_raw_data: "type_defs.DescribeBotLocaleRequestWaitTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotLocaleRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotLocaleRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotRequestWait:
    boto3_raw_data: "type_defs.DescribeBotRequestWaitTypeDef" = dataclasses.field()

    botId = field("botId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotVersionRequestWait:
    boto3_raw_data: "type_defs.DescribeBotVersionRequestWaitTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeBotVersionRequestWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotVersionRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExportRequestWait:
    boto3_raw_data: "type_defs.DescribeExportRequestWaitTypeDef" = dataclasses.field()

    exportId = field("exportId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExportRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExportRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImportRequestWait:
    boto3_raw_data: "type_defs.DescribeImportRequestWaitTypeDef" = dataclasses.field()

    importId = field("importId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImportRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImportRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotVersionResponse:
    boto3_raw_data: "type_defs.DescribeBotVersionResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botName = field("botName")
    botVersion = field("botVersion")
    description = field("description")
    roleArn = field("roleArn")

    @cached_property
    def dataPrivacy(self):  # pragma: no cover
        return DataPrivacy.make_one(self.boto3_raw_data["dataPrivacy"])

    idleSessionTTLInSeconds = field("idleSessionTTLInSeconds")
    botStatus = field("botStatus")
    failureReasons = field("failureReasons")
    creationDateTime = field("creationDateTime")

    @cached_property
    def parentBotNetworks(self):  # pragma: no cover
        return ParentBotNetwork.make_many(self.boto3_raw_data["parentBotNetworks"])

    botType = field("botType")

    @cached_property
    def botMembers(self):  # pragma: no cover
        return BotMember.make_many(self.boto3_raw_data["botMembers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBotRecommendationRequest:
    boto3_raw_data: "type_defs.UpdateBotRecommendationRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botRecommendationId = field("botRecommendationId")

    @cached_property
    def encryptionSetting(self):  # pragma: no cover
        return EncryptionSetting.make_one(self.boto3_raw_data["encryptionSetting"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateBotRecommendationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBotRecommendationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTestSetResponse:
    boto3_raw_data: "type_defs.DescribeTestSetResponseTypeDef" = dataclasses.field()

    testSetId = field("testSetId")
    testSetName = field("testSetName")
    description = field("description")
    modality = field("modality")
    status = field("status")
    roleArn = field("roleArn")
    numTurns = field("numTurns")

    @cached_property
    def storageLocation(self):  # pragma: no cover
        return TestSetStorageLocation.make_one(self.boto3_raw_data["storageLocation"])

    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTestSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTestSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetSummary:
    boto3_raw_data: "type_defs.TestSetSummaryTypeDef" = dataclasses.field()

    testSetId = field("testSetId")
    testSetName = field("testSetName")
    description = field("description")
    modality = field("modality")
    status = field("status")
    roleArn = field("roleArn")
    numTurns = field("numTurns")

    @cached_property
    def storageLocation(self):  # pragma: no cover
        return TestSetStorageLocation.make_one(self.boto3_raw_data["storageLocation"])

    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestSetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestSetSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTestSetResponse:
    boto3_raw_data: "type_defs.UpdateTestSetResponseTypeDef" = dataclasses.field()

    testSetId = field("testSetId")
    testSetName = field("testSetName")
    description = field("description")
    modality = field("modality")
    status = field("status")
    roleArn = field("roleArn")
    numTurns = field("numTurns")

    @cached_property
    def storageLocation(self):  # pragma: no cover
        return TestSetStorageLocation.make_one(self.boto3_raw_data["storageLocation"])

    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTestSetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTestSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpensearchConfigurationOutput:
    boto3_raw_data: "type_defs.OpensearchConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    domainEndpoint = field("domainEndpoint")
    indexName = field("indexName")
    exactResponse = field("exactResponse")

    @cached_property
    def exactResponseFields(self):  # pragma: no cover
        return ExactResponseFields.make_one(self.boto3_raw_data["exactResponseFields"])

    includeFields = field("includeFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OpensearchConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpensearchConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpensearchConfiguration:
    boto3_raw_data: "type_defs.OpensearchConfigurationTypeDef" = dataclasses.field()

    domainEndpoint = field("domainEndpoint")
    indexName = field("indexName")
    exactResponse = field("exactResponse")

    @cached_property
    def exactResponseFields(self):  # pragma: no cover
        return ExactResponseFields.make_one(self.boto3_raw_data["exactResponseFields"])

    includeFields = field("includeFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpensearchConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpensearchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportResourceSpecification:
    boto3_raw_data: "type_defs.ExportResourceSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def botExportSpecification(self):  # pragma: no cover
        return BotExportSpecification.make_one(
            self.boto3_raw_data["botExportSpecification"]
        )

    @cached_property
    def botLocaleExportSpecification(self):  # pragma: no cover
        return BotLocaleExportSpecification.make_one(
            self.boto3_raw_data["botLocaleExportSpecification"]
        )

    @cached_property
    def customVocabularyExportSpecification(self):  # pragma: no cover
        return CustomVocabularyExportSpecification.make_one(
            self.boto3_raw_data["customVocabularyExportSpecification"]
        )

    @cached_property
    def testSetExportSpecification(self):  # pragma: no cover
        return TestSetExportSpecification.make_one(
            self.boto3_raw_data["testSetExportSpecification"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportResourceSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportResourceSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportsRequest:
    boto3_raw_data: "type_defs.ListExportsRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return ExportSortBy.make_one(self.boto3_raw_data["sortBy"])

    @cached_property
    def filters(self):  # pragma: no cover
        return ExportFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotResourceGenerationsRequest:
    boto3_raw_data: "type_defs.ListBotResourceGenerationsRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return GenerationSortBy.make_one(self.boto3_raw_data["sortBy"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBotResourceGenerationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotResourceGenerationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBotResourceGenerationsResponse:
    boto3_raw_data: "type_defs.ListBotResourceGenerationsResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def generationSummaries(self):  # pragma: no cover
        return GenerationSummary.make_many(self.boto3_raw_data["generationSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBotResourceGenerationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBotResourceGenerationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrammarSlotTypeSetting:
    boto3_raw_data: "type_defs.GrammarSlotTypeSettingTypeDef" = dataclasses.field()

    @cached_property
    def source(self):  # pragma: no cover
        return GrammarSlotTypeSource.make_one(self.boto3_raw_data["source"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrammarSlotTypeSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrammarSlotTypeSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsRequest:
    boto3_raw_data: "type_defs.ListImportsRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return ImportSortBy.make_one(self.boto3_raw_data["sortBy"])

    @cached_property
    def filters(self):  # pragma: no cover
        return ImportFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    localeId = field("localeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsResponse:
    boto3_raw_data: "type_defs.ListImportsResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")

    @cached_property
    def importSummaries(self):  # pragma: no cover
        return ImportSummary.make_many(self.boto3_raw_data["importSummaries"])

    localeId = field("localeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentClassificationTestResultItem:
    boto3_raw_data: "type_defs.IntentClassificationTestResultItemTypeDef" = (
        dataclasses.field()
    )

    intentName = field("intentName")
    multiTurnConversation = field("multiTurnConversation")

    @cached_property
    def resultCounts(self):  # pragma: no cover
        return IntentClassificationTestResultItemCounts.make_one(
            self.boto3_raw_data["resultCounts"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IntentClassificationTestResultItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentClassificationTestResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntentsRequest:
    boto3_raw_data: "type_defs.ListIntentsRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return IntentSortBy.make_one(self.boto3_raw_data["sortBy"])

    @cached_property
    def filters(self):  # pragma: no cover
        return IntentFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIntentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionSpecification:
    boto3_raw_data: "type_defs.SessionSpecificationTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    channel = field("channel")
    sessionId = field("sessionId")
    conversationStartTime = field("conversationStartTime")
    conversationEndTime = field("conversationEndTime")
    conversationDurationSeconds = field("conversationDurationSeconds")
    conversationEndState = field("conversationEndState")
    mode = field("mode")
    numberOfTurns = field("numberOfTurns")

    @cached_property
    def invokedIntentSamples(self):  # pragma: no cover
        return InvokedIntentSample.make_many(
            self.boto3_raw_data["invokedIntentSamples"]
        )

    originatingRequestId = field("originatingRequestId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRecommendedIntentsResponse:
    boto3_raw_data: "type_defs.ListRecommendedIntentsResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botRecommendationId = field("botRecommendationId")

    @cached_property
    def summaryList(self):  # pragma: no cover
        return RecommendedIntentSummary.make_many(self.boto3_raw_data["summaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRecommendedIntentsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRecommendedIntentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionAnalyticsDataRequest:
    boto3_raw_data: "type_defs.ListSessionAnalyticsDataRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    startDateTime = field("startDateTime")
    endDateTime = field("endDateTime")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return SessionDataSortBy.make_one(self.boto3_raw_data["sortBy"])

    @cached_property
    def filters(self):  # pragma: no cover
        return AnalyticsSessionFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSessionAnalyticsDataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionAnalyticsDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSlotTypesRequest:
    boto3_raw_data: "type_defs.ListSlotTypesRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return SlotTypeSortBy.make_one(self.boto3_raw_data["sortBy"])

    @cached_property
    def filters(self):  # pragma: no cover
        return SlotTypeFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSlotTypesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSlotTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSlotTypesResponse:
    boto3_raw_data: "type_defs.ListSlotTypesResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def slotTypeSummaries(self):  # pragma: no cover
        return SlotTypeSummary.make_many(self.boto3_raw_data["slotTypeSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSlotTypesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSlotTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSlotsRequest:
    boto3_raw_data: "type_defs.ListSlotsRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    intentId = field("intentId")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return SlotSortBy.make_one(self.boto3_raw_data["sortBy"])

    @cached_property
    def filters(self):  # pragma: no cover
        return SlotFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListSlotsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSlotsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestExecutionsRequest:
    boto3_raw_data: "type_defs.ListTestExecutionsRequestTypeDef" = dataclasses.field()

    @cached_property
    def sortBy(self):  # pragma: no cover
        return TestExecutionSortBy.make_one(self.boto3_raw_data["sortBy"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestExecutionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestExecutionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestSetsRequest:
    boto3_raw_data: "type_defs.ListTestSetsRequestTypeDef" = dataclasses.field()

    @cached_property
    def sortBy(self):  # pragma: no cover
        return TestSetSortBy.make_one(self.boto3_raw_data["sortBy"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestSetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUtteranceAnalyticsDataRequest:
    boto3_raw_data: "type_defs.ListUtteranceAnalyticsDataRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    startDateTime = field("startDateTime")
    endDateTime = field("endDateTime")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return UtteranceDataSortBy.make_one(self.boto3_raw_data["sortBy"])

    @cached_property
    def filters(self):  # pragma: no cover
        return AnalyticsUtteranceFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUtteranceAnalyticsDataRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUtteranceAnalyticsDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverallTestResults:
    boto3_raw_data: "type_defs.OverallTestResultsTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return OverallTestResultItem.make_many(self.boto3_raw_data["items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OverallTestResultsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OverallTestResultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QInConnectIntentConfiguration:
    boto3_raw_data: "type_defs.QInConnectIntentConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def qInConnectAssistantConfiguration(self):  # pragma: no cover
        return QInConnectAssistantConfiguration.make_one(
            self.boto3_raw_data["qInConnectAssistantConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QInConnectIntentConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QInConnectIntentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtteranceAggregationDuration:
    boto3_raw_data: "type_defs.UtteranceAggregationDurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def relativeAggregationDuration(self):  # pragma: no cover
        return RelativeAggregationDuration.make_one(
            self.boto3_raw_data["relativeAggregationDuration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UtteranceAggregationDurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UtteranceAggregationDurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeHintDetails:
    boto3_raw_data: "type_defs.RuntimeHintDetailsTypeDef" = dataclasses.field()

    @cached_property
    def runtimeHintValues(self):  # pragma: no cover
        return RuntimeHintValue.make_many(self.boto3_raw_data["runtimeHintValues"])

    subSlotHints = field("subSlotHints")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuntimeHintDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuntimeHintDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotTypeValueOutput:
    boto3_raw_data: "type_defs.SlotTypeValueOutputTypeDef" = dataclasses.field()

    @cached_property
    def sampleValue(self):  # pragma: no cover
        return SampleValue.make_one(self.boto3_raw_data["sampleValue"])

    @cached_property
    def synonyms(self):  # pragma: no cover
        return SampleValue.make_many(self.boto3_raw_data["synonyms"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotTypeValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotTypeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotTypeValue:
    boto3_raw_data: "type_defs.SlotTypeValueTypeDef" = dataclasses.field()

    @cached_property
    def sampleValue(self):  # pragma: no cover
        return SampleValue.make_one(self.boto3_raw_data["sampleValue"])

    @cached_property
    def synonyms(self):  # pragma: no cover
        return SampleValue.make_many(self.boto3_raw_data["synonyms"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotTypeValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotTypeValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotDefaultValueSpecificationOutput:
    boto3_raw_data: "type_defs.SlotDefaultValueSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def defaultValueList(self):  # pragma: no cover
        return SlotDefaultValue.make_many(self.boto3_raw_data["defaultValueList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SlotDefaultValueSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotDefaultValueSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotDefaultValueSpecification:
    boto3_raw_data: "type_defs.SlotDefaultValueSpecificationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def defaultValueList(self):  # pragma: no cover
        return SlotDefaultValue.make_many(self.boto3_raw_data["defaultValueList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SlotDefaultValueSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotDefaultValueSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotResolutionTestResultItem:
    boto3_raw_data: "type_defs.SlotResolutionTestResultItemTypeDef" = (
        dataclasses.field()
    )

    slotName = field("slotName")

    @cached_property
    def resultCounts(self):  # pragma: no cover
        return SlotResolutionTestResultItemCounts.make_one(
            self.boto3_raw_data["resultCounts"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotResolutionTestResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotResolutionTestResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotValueOverrideOutput:
    boto3_raw_data: "type_defs.SlotValueOverrideOutputTypeDef" = dataclasses.field()

    shape = field("shape")

    @cached_property
    def value(self):  # pragma: no cover
        return SlotValue.make_one(self.boto3_raw_data["value"])

    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotValueOverrideOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotValueOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotValueOverride:
    boto3_raw_data: "type_defs.SlotValueOverrideTypeDef" = dataclasses.field()

    shape = field("shape")

    @cached_property
    def value(self):  # pragma: no cover
        return SlotValue.make_one(self.boto3_raw_data["value"])

    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotValueOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotValueOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotValueSelectionSetting:
    boto3_raw_data: "type_defs.SlotValueSelectionSettingTypeDef" = dataclasses.field()

    resolutionStrategy = field("resolutionStrategy")

    @cached_property
    def regexFilter(self):  # pragma: no cover
        return SlotValueRegexFilter.make_one(self.boto3_raw_data["regexFilter"])

    @cached_property
    def advancedRecognitionSetting(self):  # pragma: no cover
        return AdvancedRecognitionSetting.make_one(
            self.boto3_raw_data["advancedRecognitionSetting"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotValueSelectionSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotValueSelectionSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetDiscrepancyErrors:
    boto3_raw_data: "type_defs.TestSetDiscrepancyErrorsTypeDef" = dataclasses.field()

    @cached_property
    def intentDiscrepancies(self):  # pragma: no cover
        return TestSetIntentDiscrepancyItem.make_many(
            self.boto3_raw_data["intentDiscrepancies"]
        )

    @cached_property
    def slotDiscrepancies(self):  # pragma: no cover
        return TestSetSlotDiscrepancyItem.make_many(
            self.boto3_raw_data["slotDiscrepancies"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestSetDiscrepancyErrorsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetDiscrepancyErrorsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetDiscrepancyReportResourceTarget:
    boto3_raw_data: "type_defs.TestSetDiscrepancyReportResourceTargetTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def botAliasTarget(self):  # pragma: no cover
        return TestSetDiscrepancyReportBotAliasTarget.make_one(
            self.boto3_raw_data["botAliasTarget"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TestSetDiscrepancyReportResourceTargetTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetDiscrepancyReportResourceTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetImportResourceSpecificationOutput:
    boto3_raw_data: "type_defs.TestSetImportResourceSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    testSetName = field("testSetName")
    roleArn = field("roleArn")

    @cached_property
    def storageLocation(self):  # pragma: no cover
        return TestSetStorageLocation.make_one(self.boto3_raw_data["storageLocation"])

    @cached_property
    def importInputLocation(self):  # pragma: no cover
        return TestSetImportInputLocation.make_one(
            self.boto3_raw_data["importInputLocation"]
        )

    modality = field("modality")
    description = field("description")
    testSetTags = field("testSetTags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TestSetImportResourceSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetImportResourceSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetImportResourceSpecification:
    boto3_raw_data: "type_defs.TestSetImportResourceSpecificationTypeDef" = (
        dataclasses.field()
    )

    testSetName = field("testSetName")
    roleArn = field("roleArn")

    @cached_property
    def storageLocation(self):  # pragma: no cover
        return TestSetStorageLocation.make_one(self.boto3_raw_data["storageLocation"])

    @cached_property
    def importInputLocation(self):  # pragma: no cover
        return TestSetImportInputLocation.make_one(
            self.boto3_raw_data["importInputLocation"]
        )

    modality = field("modality")
    description = field("description")
    testSetTags = field("testSetTags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TestSetImportResourceSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetImportResourceSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserTurnIntentOutput:
    boto3_raw_data: "type_defs.UserTurnIntentOutputTypeDef" = dataclasses.field()

    name = field("name")
    slots = field("slots")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserTurnIntentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserTurnIntentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtteranceInputSpecification:
    boto3_raw_data: "type_defs.UtteranceInputSpecificationTypeDef" = dataclasses.field()

    textInput = field("textInput")

    @cached_property
    def audioInput(self):  # pragma: no cover
        return UtteranceAudioInputSpecification.make_one(
            self.boto3_raw_data["audioInput"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UtteranceInputSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UtteranceInputSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntentMetricsResponse:
    boto3_raw_data: "type_defs.ListIntentMetricsResponseTypeDef" = dataclasses.field()

    botId = field("botId")

    @cached_property
    def results(self):  # pragma: no cover
        return AnalyticsIntentResult.make_many(self.boto3_raw_data["results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIntentMetricsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntentMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntentStageMetricsResponse:
    boto3_raw_data: "type_defs.ListIntentStageMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")

    @cached_property
    def results(self):  # pragma: no cover
        return AnalyticsIntentStageResult.make_many(self.boto3_raw_data["results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIntentStageMetricsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntentStageMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionMetricsResponse:
    boto3_raw_data: "type_defs.ListSessionMetricsResponseTypeDef" = dataclasses.field()

    botId = field("botId")

    @cached_property
    def results(self):  # pragma: no cover
        return AnalyticsSessionResult.make_many(self.boto3_raw_data["results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSessionMetricsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUtteranceMetricsResponse:
    boto3_raw_data: "type_defs.ListUtteranceMetricsResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")

    @cached_property
    def results(self):  # pragma: no cover
        return AnalyticsUtteranceResult.make_many(self.boto3_raw_data["results"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUtteranceMetricsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUtteranceMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptAttemptSpecification:
    boto3_raw_data: "type_defs.PromptAttemptSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def allowedInputTypes(self):  # pragma: no cover
        return AllowedInputTypes.make_one(self.boto3_raw_data["allowedInputTypes"])

    allowInterrupt = field("allowInterrupt")

    @cached_property
    def audioAndDTMFInputSpecification(self):  # pragma: no cover
        return AudioAndDTMFInputSpecification.make_one(
            self.boto3_raw_data["audioAndDTMFInputSpecification"]
        )

    @cached_property
    def textInputSpecification(self):  # pragma: no cover
        return TextInputSpecification.make_one(
            self.boto3_raw_data["textInputSpecification"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptAttemptSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptAttemptSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioLogSetting:
    boto3_raw_data: "type_defs.AudioLogSettingTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @cached_property
    def destination(self):  # pragma: no cover
        return AudioLogDestination.make_one(self.boto3_raw_data["destination"])

    selectiveLoggingEnabled = field("selectiveLoggingEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioLogSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AudioLogSettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescriptiveBotBuilderSpecification:
    boto3_raw_data: "type_defs.DescriptiveBotBuilderSpecificationTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")

    @cached_property
    def bedrockModelSpecification(self):  # pragma: no cover
        return BedrockModelSpecification.make_one(
            self.boto3_raw_data["bedrockModelSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescriptiveBotBuilderSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescriptiveBotBuilderSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SampleUtteranceGenerationSpecification:
    boto3_raw_data: "type_defs.SampleUtteranceGenerationSpecificationTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")

    @cached_property
    def bedrockModelSpecification(self):  # pragma: no cover
        return BedrockModelSpecification.make_one(
            self.boto3_raw_data["bedrockModelSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SampleUtteranceGenerationSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SampleUtteranceGenerationSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotResolutionImprovementSpecification:
    boto3_raw_data: "type_defs.SlotResolutionImprovementSpecificationTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")

    @cached_property
    def bedrockModelSpecification(self):  # pragma: no cover
        return BedrockModelSpecification.make_one(
            self.boto3_raw_data["bedrockModelSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SlotResolutionImprovementSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotResolutionImprovementSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTestExecutionResponse:
    boto3_raw_data: "type_defs.DescribeTestExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    testExecutionId = field("testExecutionId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    testExecutionStatus = field("testExecutionStatus")
    testSetId = field("testSetId")
    testSetName = field("testSetName")

    @cached_property
    def target(self):  # pragma: no cover
        return TestExecutionTarget.make_one(self.boto3_raw_data["target"])

    apiMode = field("apiMode")
    testExecutionModality = field("testExecutionModality")
    failureReasons = field("failureReasons")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTestExecutionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTestExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTestExecutionRequest:
    boto3_raw_data: "type_defs.StartTestExecutionRequestTypeDef" = dataclasses.field()

    testSetId = field("testSetId")

    @cached_property
    def target(self):  # pragma: no cover
        return TestExecutionTarget.make_one(self.boto3_raw_data["target"])

    apiMode = field("apiMode")
    testExecutionModality = field("testExecutionModality")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTestExecutionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTestExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTestExecutionResponse:
    boto3_raw_data: "type_defs.StartTestExecutionResponseTypeDef" = dataclasses.field()

    testExecutionId = field("testExecutionId")
    creationDateTime = field("creationDateTime")
    testSetId = field("testSetId")

    @cached_property
    def target(self):  # pragma: no cover
        return TestExecutionTarget.make_one(self.boto3_raw_data["target"])

    apiMode = field("apiMode")
    testExecutionModality = field("testExecutionModality")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTestExecutionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTestExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestExecutionSummary:
    boto3_raw_data: "type_defs.TestExecutionSummaryTypeDef" = dataclasses.field()

    testExecutionId = field("testExecutionId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    testExecutionStatus = field("testExecutionStatus")
    testSetId = field("testSetId")
    testSetName = field("testSetName")

    @cached_property
    def target(self):  # pragma: no cover
        return TestExecutionTarget.make_one(self.boto3_raw_data["target"])

    apiMode = field("apiMode")
    testExecutionModality = field("testExecutionModality")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestExecutionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestExecutionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotRecommendationResults:
    boto3_raw_data: "type_defs.BotRecommendationResultsTypeDef" = dataclasses.field()

    botLocaleExportUrl = field("botLocaleExportUrl")
    associatedTranscriptsUrl = field("associatedTranscriptsUrl")

    @cached_property
    def statistics(self):  # pragma: no cover
        return BotRecommendationResultStatistics.make_one(
            self.boto3_raw_data["statistics"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotRecommendationResultsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotRecommendationResultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageOutput:
    boto3_raw_data: "type_defs.MessageOutputTypeDef" = dataclasses.field()

    @cached_property
    def plainTextMessage(self):  # pragma: no cover
        return PlainTextMessage.make_one(self.boto3_raw_data["plainTextMessage"])

    @cached_property
    def customPayload(self):  # pragma: no cover
        return CustomPayload.make_one(self.boto3_raw_data["customPayload"])

    @cached_property
    def ssmlMessage(self):  # pragma: no cover
        return SSMLMessage.make_one(self.boto3_raw_data["ssmlMessage"])

    @cached_property
    def imageResponseCard(self):  # pragma: no cover
        return ImageResponseCardOutput.make_one(
            self.boto3_raw_data["imageResponseCard"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtteranceBotResponse:
    boto3_raw_data: "type_defs.UtteranceBotResponseTypeDef" = dataclasses.field()

    content = field("content")
    contentType = field("contentType")

    @cached_property
    def imageResponseCard(self):  # pragma: no cover
        return ImageResponseCardOutput.make_one(
            self.boto3_raw_data["imageResponseCard"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UtteranceBotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UtteranceBotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Message:
    boto3_raw_data: "type_defs.MessageTypeDef" = dataclasses.field()

    @cached_property
    def plainTextMessage(self):  # pragma: no cover
        return PlainTextMessage.make_one(self.boto3_raw_data["plainTextMessage"])

    @cached_property
    def customPayload(self):  # pragma: no cover
        return CustomPayload.make_one(self.boto3_raw_data["customPayload"])

    @cached_property
    def ssmlMessage(self):  # pragma: no cover
        return SSMLMessage.make_one(self.boto3_raw_data["ssmlMessage"])

    @cached_property
    def imageResponseCard(self):  # pragma: no cover
        return ImageResponseCard.make_one(self.boto3_raw_data["imageResponseCard"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextLogSetting:
    boto3_raw_data: "type_defs.TextLogSettingTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @cached_property
    def destination(self):  # pragma: no cover
        return TextLogDestination.make_one(self.boto3_raw_data["destination"])

    selectiveLoggingEnabled = field("selectiveLoggingEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextLogSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextLogSettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BotAliasLocaleSettings:
    boto3_raw_data: "type_defs.BotAliasLocaleSettingsTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @cached_property
    def codeHookSpecification(self):  # pragma: no cover
        return CodeHookSpecification.make_one(
            self.boto3_raw_data["codeHookSpecification"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BotAliasLocaleSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BotAliasLocaleSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLevelTestResults:
    boto3_raw_data: "type_defs.ConversationLevelTestResultsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return ConversationLevelTestResultItem.make_many(self.boto3_raw_data["items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConversationLevelTestResultsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLevelTestResultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestExecutionResultItemsRequest:
    boto3_raw_data: "type_defs.ListTestExecutionResultItemsRequestTypeDef" = (
        dataclasses.field()
    )

    testExecutionId = field("testExecutionId")

    @cached_property
    def resultFilterBy(self):  # pragma: no cover
        return TestExecutionResultFilterBy.make_one(
            self.boto3_raw_data["resultFilterBy"]
        )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTestExecutionResultItemsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestExecutionResultItemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetGenerationDataSourceOutput:
    boto3_raw_data: "type_defs.TestSetGenerationDataSourceOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def conversationLogsDataSource(self):  # pragma: no cover
        return ConversationLogsDataSourceOutput.make_one(
            self.boto3_raw_data["conversationLogsDataSource"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TestSetGenerationDataSourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetGenerationDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLogsDataSource:
    boto3_raw_data: "type_defs.ConversationLogsDataSourceTypeDef" = dataclasses.field()

    botId = field("botId")
    botAliasId = field("botAliasId")
    localeId = field("localeId")

    @cached_property
    def filter(self):  # pragma: no cover
        return ConversationLogsDataSourceFilterBy.make_one(
            self.boto3_raw_data["filter"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConversationLogsDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLogsDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LexTranscriptFilter:
    boto3_raw_data: "type_defs.LexTranscriptFilterTypeDef" = dataclasses.field()

    @cached_property
    def dateRangeFilter(self):  # pragma: no cover
        return DateRangeFilter.make_one(self.boto3_raw_data["dateRangeFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LexTranscriptFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LexTranscriptFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntentsResponse:
    boto3_raw_data: "type_defs.ListIntentsResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def intentSummaries(self):  # pragma: no cover
        return IntentSummary.make_many(self.boto3_raw_data["intentSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIntentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranscriptFilterOutput:
    boto3_raw_data: "type_defs.TranscriptFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def lexTranscriptFilter(self):  # pragma: no cover
        return LexTranscriptFilterOutput.make_one(
            self.boto3_raw_data["lexTranscriptFilter"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranscriptFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranscriptFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestSetsResponse:
    boto3_raw_data: "type_defs.ListTestSetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def testSets(self):  # pragma: no cover
        return TestSetSummary.make_many(self.boto3_raw_data["testSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestSetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfigurationOutput:
    boto3_raw_data: "type_defs.DataSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def opensearchConfiguration(self):  # pragma: no cover
        return OpensearchConfigurationOutput.make_one(
            self.boto3_raw_data["opensearchConfiguration"]
        )

    @cached_property
    def kendraConfiguration(self):  # pragma: no cover
        return QnAKendraConfiguration.make_one(
            self.boto3_raw_data["kendraConfiguration"]
        )

    @cached_property
    def bedrockKnowledgeStoreConfiguration(self):  # pragma: no cover
        return BedrockKnowledgeStoreConfiguration.make_one(
            self.boto3_raw_data["bedrockKnowledgeStoreConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataSourceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfiguration:
    boto3_raw_data: "type_defs.DataSourceConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def opensearchConfiguration(self):  # pragma: no cover
        return OpensearchConfiguration.make_one(
            self.boto3_raw_data["opensearchConfiguration"]
        )

    @cached_property
    def kendraConfiguration(self):  # pragma: no cover
        return QnAKendraConfiguration.make_one(
            self.boto3_raw_data["kendraConfiguration"]
        )

    @cached_property
    def bedrockKnowledgeStoreConfiguration(self):  # pragma: no cover
        return BedrockKnowledgeStoreConfiguration.make_one(
            self.boto3_raw_data["bedrockKnowledgeStoreConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExportRequest:
    boto3_raw_data: "type_defs.CreateExportRequestTypeDef" = dataclasses.field()

    @cached_property
    def resourceSpecification(self):  # pragma: no cover
        return ExportResourceSpecification.make_one(
            self.boto3_raw_data["resourceSpecification"]
        )

    fileFormat = field("fileFormat")
    filePassword = field("filePassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExportResponse:
    boto3_raw_data: "type_defs.CreateExportResponseTypeDef" = dataclasses.field()

    exportId = field("exportId")

    @cached_property
    def resourceSpecification(self):  # pragma: no cover
        return ExportResourceSpecification.make_one(
            self.boto3_raw_data["resourceSpecification"]
        )

    fileFormat = field("fileFormat")
    exportStatus = field("exportStatus")
    creationDateTime = field("creationDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExportResponse:
    boto3_raw_data: "type_defs.DescribeExportResponseTypeDef" = dataclasses.field()

    exportId = field("exportId")

    @cached_property
    def resourceSpecification(self):  # pragma: no cover
        return ExportResourceSpecification.make_one(
            self.boto3_raw_data["resourceSpecification"]
        )

    fileFormat = field("fileFormat")
    exportStatus = field("exportStatus")
    failureReasons = field("failureReasons")
    downloadUrl = field("downloadUrl")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportSummary:
    boto3_raw_data: "type_defs.ExportSummaryTypeDef" = dataclasses.field()

    exportId = field("exportId")

    @cached_property
    def resourceSpecification(self):  # pragma: no cover
        return ExportResourceSpecification.make_one(
            self.boto3_raw_data["resourceSpecification"]
        )

    fileFormat = field("fileFormat")
    exportStatus = field("exportStatus")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExportResponse:
    boto3_raw_data: "type_defs.UpdateExportResponseTypeDef" = dataclasses.field()

    exportId = field("exportId")

    @cached_property
    def resourceSpecification(self):  # pragma: no cover
        return ExportResourceSpecification.make_one(
            self.boto3_raw_data["resourceSpecification"]
        )

    fileFormat = field("fileFormat")
    exportStatus = field("exportStatus")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateExportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSourceSetting:
    boto3_raw_data: "type_defs.ExternalSourceSettingTypeDef" = dataclasses.field()

    @cached_property
    def grammarSlotTypeSetting(self):  # pragma: no cover
        return GrammarSlotTypeSetting.make_one(
            self.boto3_raw_data["grammarSlotTypeSetting"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExternalSourceSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalSourceSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentClassificationTestResults:
    boto3_raw_data: "type_defs.IntentClassificationTestResultsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return IntentClassificationTestResultItem.make_many(
            self.boto3_raw_data["items"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IntentClassificationTestResultsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentClassificationTestResultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSessionAnalyticsDataResponse:
    boto3_raw_data: "type_defs.ListSessionAnalyticsDataResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")

    @cached_property
    def sessions(self):  # pragma: no cover
        return SessionSpecification.make_many(self.boto3_raw_data["sessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSessionAnalyticsDataResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSessionAnalyticsDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAggregatedUtterancesRequest:
    boto3_raw_data: "type_defs.ListAggregatedUtterancesRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    localeId = field("localeId")

    @cached_property
    def aggregationDuration(self):  # pragma: no cover
        return UtteranceAggregationDuration.make_one(
            self.boto3_raw_data["aggregationDuration"]
        )

    botAliasId = field("botAliasId")
    botVersion = field("botVersion")

    @cached_property
    def sortBy(self):  # pragma: no cover
        return AggregatedUtterancesSortBy.make_one(self.boto3_raw_data["sortBy"])

    @cached_property
    def filters(self):  # pragma: no cover
        return AggregatedUtterancesFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAggregatedUtterancesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAggregatedUtterancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAggregatedUtterancesResponse:
    boto3_raw_data: "type_defs.ListAggregatedUtterancesResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botAliasId = field("botAliasId")
    botVersion = field("botVersion")
    localeId = field("localeId")

    @cached_property
    def aggregationDuration(self):  # pragma: no cover
        return UtteranceAggregationDuration.make_one(
            self.boto3_raw_data["aggregationDuration"]
        )

    aggregationWindowStartTime = field("aggregationWindowStartTime")
    aggregationWindowEndTime = field("aggregationWindowEndTime")
    aggregationLastRefreshedDateTime = field("aggregationLastRefreshedDateTime")

    @cached_property
    def aggregatedUtterancesSummaries(self):  # pragma: no cover
        return AggregatedUtterancesSummary.make_many(
            self.boto3_raw_data["aggregatedUtterancesSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAggregatedUtterancesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAggregatedUtterancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeHints:
    boto3_raw_data: "type_defs.RuntimeHintsTypeDef" = dataclasses.field()

    slotHints = field("slotHints")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuntimeHintsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuntimeHintsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentLevelSlotResolutionTestResultItem:
    boto3_raw_data: "type_defs.IntentLevelSlotResolutionTestResultItemTypeDef" = (
        dataclasses.field()
    )

    intentName = field("intentName")
    multiTurnConversation = field("multiTurnConversation")

    @cached_property
    def slotResolutionResults(self):  # pragma: no cover
        return SlotResolutionTestResultItem.make_many(
            self.boto3_raw_data["slotResolutionResults"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IntentLevelSlotResolutionTestResultItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentLevelSlotResolutionTestResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentOverrideOutput:
    boto3_raw_data: "type_defs.IntentOverrideOutputTypeDef" = dataclasses.field()

    name = field("name")
    slots = field("slots")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntentOverrideOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentOverride:
    boto3_raw_data: "type_defs.IntentOverrideTypeDef" = dataclasses.field()

    name = field("name")
    slots = field("slots")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntentOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntentOverrideTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTestSetDiscrepancyReportRequest:
    boto3_raw_data: "type_defs.CreateTestSetDiscrepancyReportRequestTypeDef" = (
        dataclasses.field()
    )

    testSetId = field("testSetId")

    @cached_property
    def target(self):  # pragma: no cover
        return TestSetDiscrepancyReportResourceTarget.make_one(
            self.boto3_raw_data["target"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTestSetDiscrepancyReportRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTestSetDiscrepancyReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTestSetDiscrepancyReportResponse:
    boto3_raw_data: "type_defs.CreateTestSetDiscrepancyReportResponseTypeDef" = (
        dataclasses.field()
    )

    testSetDiscrepancyReportId = field("testSetDiscrepancyReportId")
    creationDateTime = field("creationDateTime")
    testSetId = field("testSetId")

    @cached_property
    def target(self):  # pragma: no cover
        return TestSetDiscrepancyReportResourceTarget.make_one(
            self.boto3_raw_data["target"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTestSetDiscrepancyReportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTestSetDiscrepancyReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTestSetDiscrepancyReportResponse:
    boto3_raw_data: "type_defs.DescribeTestSetDiscrepancyReportResponseTypeDef" = (
        dataclasses.field()
    )

    testSetDiscrepancyReportId = field("testSetDiscrepancyReportId")
    testSetId = field("testSetId")
    creationDateTime = field("creationDateTime")

    @cached_property
    def target(self):  # pragma: no cover
        return TestSetDiscrepancyReportResourceTarget.make_one(
            self.boto3_raw_data["target"]
        )

    testSetDiscrepancyReportStatus = field("testSetDiscrepancyReportStatus")
    lastUpdatedDataTime = field("lastUpdatedDataTime")

    @cached_property
    def testSetDiscrepancyTopErrors(self):  # pragma: no cover
        return TestSetDiscrepancyErrors.make_one(
            self.boto3_raw_data["testSetDiscrepancyTopErrors"]
        )

    testSetDiscrepancyRawOutputUrl = field("testSetDiscrepancyRawOutputUrl")
    failureReasons = field("failureReasons")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTestSetDiscrepancyReportResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTestSetDiscrepancyReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportResourceSpecificationOutput:
    boto3_raw_data: "type_defs.ImportResourceSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def botImportSpecification(self):  # pragma: no cover
        return BotImportSpecificationOutput.make_one(
            self.boto3_raw_data["botImportSpecification"]
        )

    @cached_property
    def botLocaleImportSpecification(self):  # pragma: no cover
        return BotLocaleImportSpecification.make_one(
            self.boto3_raw_data["botLocaleImportSpecification"]
        )

    @cached_property
    def customVocabularyImportSpecification(self):  # pragma: no cover
        return CustomVocabularyImportSpecification.make_one(
            self.boto3_raw_data["customVocabularyImportSpecification"]
        )

    @cached_property
    def testSetImportResourceSpecification(self):  # pragma: no cover
        return TestSetImportResourceSpecificationOutput.make_one(
            self.boto3_raw_data["testSetImportResourceSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImportResourceSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportResourceSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportResourceSpecification:
    boto3_raw_data: "type_defs.ImportResourceSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def botImportSpecification(self):  # pragma: no cover
        return BotImportSpecification.make_one(
            self.boto3_raw_data["botImportSpecification"]
        )

    @cached_property
    def botLocaleImportSpecification(self):  # pragma: no cover
        return BotLocaleImportSpecification.make_one(
            self.boto3_raw_data["botLocaleImportSpecification"]
        )

    @cached_property
    def customVocabularyImportSpecification(self):  # pragma: no cover
        return CustomVocabularyImportSpecification.make_one(
            self.boto3_raw_data["customVocabularyImportSpecification"]
        )

    @cached_property
    def testSetImportResourceSpecification(self):  # pragma: no cover
        return TestSetImportResourceSpecification.make_one(
            self.boto3_raw_data["testSetImportResourceSpecification"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportResourceSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportResourceSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserTurnOutputSpecification:
    boto3_raw_data: "type_defs.UserTurnOutputSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def intent(self):  # pragma: no cover
        return UserTurnIntentOutput.make_one(self.boto3_raw_data["intent"])

    @cached_property
    def activeContexts(self):  # pragma: no cover
        return ActiveContext.make_many(self.boto3_raw_data["activeContexts"])

    transcript = field("transcript")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserTurnOutputSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserTurnOutputSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildtimeSettings:
    boto3_raw_data: "type_defs.BuildtimeSettingsTypeDef" = dataclasses.field()

    @cached_property
    def descriptiveBotBuilder(self):  # pragma: no cover
        return DescriptiveBotBuilderSpecification.make_one(
            self.boto3_raw_data["descriptiveBotBuilder"]
        )

    @cached_property
    def sampleUtteranceGeneration(self):  # pragma: no cover
        return SampleUtteranceGenerationSpecification.make_one(
            self.boto3_raw_data["sampleUtteranceGeneration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuildtimeSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuildtimeSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuntimeSettings:
    boto3_raw_data: "type_defs.RuntimeSettingsTypeDef" = dataclasses.field()

    @cached_property
    def slotResolutionImprovement(self):  # pragma: no cover
        return SlotResolutionImprovementSpecification.make_one(
            self.boto3_raw_data["slotResolutionImprovement"]
        )

    @cached_property
    def nluImprovement(self):  # pragma: no cover
        return NluImprovementSpecification.make_one(
            self.boto3_raw_data["nluImprovement"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuntimeSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuntimeSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestExecutionsResponse:
    boto3_raw_data: "type_defs.ListTestExecutionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def testExecutions(self):  # pragma: no cover
        return TestExecutionSummary.make_many(self.boto3_raw_data["testExecutions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestExecutionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageGroupOutput:
    boto3_raw_data: "type_defs.MessageGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def message(self):  # pragma: no cover
        return MessageOutput.make_one(self.boto3_raw_data["message"])

    @cached_property
    def variations(self):  # pragma: no cover
        return MessageOutput.make_many(self.boto3_raw_data["variations"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MessageGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtteranceSpecification:
    boto3_raw_data: "type_defs.UtteranceSpecificationTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    sessionId = field("sessionId")
    channel = field("channel")
    mode = field("mode")
    conversationStartTime = field("conversationStartTime")
    conversationEndTime = field("conversationEndTime")
    utterance = field("utterance")
    utteranceTimestamp = field("utteranceTimestamp")
    audioVoiceDurationMillis = field("audioVoiceDurationMillis")
    utteranceUnderstood = field("utteranceUnderstood")
    inputType = field("inputType")
    outputType = field("outputType")
    associatedIntentName = field("associatedIntentName")
    associatedSlotName = field("associatedSlotName")
    intentState = field("intentState")
    dialogActionType = field("dialogActionType")
    botResponseAudioVoiceId = field("botResponseAudioVoiceId")
    slotsFilledInSession = field("slotsFilledInSession")
    utteranceRequestId = field("utteranceRequestId")

    @cached_property
    def botResponses(self):  # pragma: no cover
        return UtteranceBotResponse.make_many(self.boto3_raw_data["botResponses"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UtteranceSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UtteranceSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageGroup:
    boto3_raw_data: "type_defs.MessageGroupTypeDef" = dataclasses.field()

    @cached_property
    def message(self):  # pragma: no cover
        return Message.make_one(self.boto3_raw_data["message"])

    @cached_property
    def variations(self):  # pragma: no cover
        return Message.make_many(self.boto3_raw_data["variations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MessageGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MessageGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLogSettingsOutput:
    boto3_raw_data: "type_defs.ConversationLogSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def textLogSettings(self):  # pragma: no cover
        return TextLogSetting.make_many(self.boto3_raw_data["textLogSettings"])

    @cached_property
    def audioLogSettings(self):  # pragma: no cover
        return AudioLogSetting.make_many(self.boto3_raw_data["audioLogSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConversationLogSettingsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLogSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversationLogSettings:
    boto3_raw_data: "type_defs.ConversationLogSettingsTypeDef" = dataclasses.field()

    @cached_property
    def textLogSettings(self):  # pragma: no cover
        return TextLogSetting.make_many(self.boto3_raw_data["textLogSettings"])

    @cached_property
    def audioLogSettings(self):  # pragma: no cover
        return AudioLogSetting.make_many(self.boto3_raw_data["audioLogSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConversationLogSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversationLogSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTestSetGenerationResponse:
    boto3_raw_data: "type_defs.DescribeTestSetGenerationResponseTypeDef" = (
        dataclasses.field()
    )

    testSetGenerationId = field("testSetGenerationId")
    testSetGenerationStatus = field("testSetGenerationStatus")
    failureReasons = field("failureReasons")
    testSetId = field("testSetId")
    testSetName = field("testSetName")
    description = field("description")

    @cached_property
    def storageLocation(self):  # pragma: no cover
        return TestSetStorageLocation.make_one(self.boto3_raw_data["storageLocation"])

    @cached_property
    def generationDataSource(self):  # pragma: no cover
        return TestSetGenerationDataSourceOutput.make_one(
            self.boto3_raw_data["generationDataSource"]
        )

    roleArn = field("roleArn")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTestSetGenerationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTestSetGenerationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTestSetGenerationResponse:
    boto3_raw_data: "type_defs.StartTestSetGenerationResponseTypeDef" = (
        dataclasses.field()
    )

    testSetGenerationId = field("testSetGenerationId")
    creationDateTime = field("creationDateTime")
    testSetGenerationStatus = field("testSetGenerationStatus")
    testSetName = field("testSetName")
    description = field("description")

    @cached_property
    def storageLocation(self):  # pragma: no cover
        return TestSetStorageLocation.make_one(self.boto3_raw_data["storageLocation"])

    @cached_property
    def generationDataSource(self):  # pragma: no cover
        return TestSetGenerationDataSourceOutput.make_one(
            self.boto3_raw_data["generationDataSource"]
        )

    roleArn = field("roleArn")
    testSetTags = field("testSetTags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartTestSetGenerationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTestSetGenerationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetGenerationDataSource:
    boto3_raw_data: "type_defs.TestSetGenerationDataSourceTypeDef" = dataclasses.field()

    @cached_property
    def conversationLogsDataSource(self):  # pragma: no cover
        return ConversationLogsDataSource.make_one(
            self.boto3_raw_data["conversationLogsDataSource"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestSetGenerationDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetGenerationDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranscriptFilter:
    boto3_raw_data: "type_defs.TranscriptFilterTypeDef" = dataclasses.field()

    @cached_property
    def lexTranscriptFilter(self):  # pragma: no cover
        return LexTranscriptFilter.make_one(self.boto3_raw_data["lexTranscriptFilter"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TranscriptFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranscriptFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketTranscriptSourceOutput:
    boto3_raw_data: "type_defs.S3BucketTranscriptSourceOutputTypeDef" = (
        dataclasses.field()
    )

    s3BucketName = field("s3BucketName")
    transcriptFormat = field("transcriptFormat")

    @cached_property
    def pathFormat(self):  # pragma: no cover
        return PathFormatOutput.make_one(self.boto3_raw_data["pathFormat"])

    @cached_property
    def transcriptFilter(self):  # pragma: no cover
        return TranscriptFilterOutput.make_one(self.boto3_raw_data["transcriptFilter"])

    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3BucketTranscriptSourceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketTranscriptSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QnAIntentConfigurationOutput:
    boto3_raw_data: "type_defs.QnAIntentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataSourceConfiguration(self):  # pragma: no cover
        return DataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["dataSourceConfiguration"]
        )

    @cached_property
    def bedrockModelConfiguration(self):  # pragma: no cover
        return BedrockModelSpecification.make_one(
            self.boto3_raw_data["bedrockModelConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QnAIntentConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QnAIntentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QnAIntentConfiguration:
    boto3_raw_data: "type_defs.QnAIntentConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def dataSourceConfiguration(self):  # pragma: no cover
        return DataSourceConfiguration.make_one(
            self.boto3_raw_data["dataSourceConfiguration"]
        )

    @cached_property
    def bedrockModelConfiguration(self):  # pragma: no cover
        return BedrockModelSpecification.make_one(
            self.boto3_raw_data["bedrockModelConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QnAIntentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QnAIntentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportsResponse:
    boto3_raw_data: "type_defs.ListExportsResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")

    @cached_property
    def exportSummaries(self):  # pragma: no cover
        return ExportSummary.make_many(self.boto3_raw_data["exportSummaries"])

    localeId = field("localeId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSlotTypeResponse:
    boto3_raw_data: "type_defs.CreateSlotTypeResponseTypeDef" = dataclasses.field()

    slotTypeId = field("slotTypeId")
    slotTypeName = field("slotTypeName")
    description = field("description")

    @cached_property
    def slotTypeValues(self):  # pragma: no cover
        return SlotTypeValueOutput.make_many(self.boto3_raw_data["slotTypeValues"])

    @cached_property
    def valueSelectionSetting(self):  # pragma: no cover
        return SlotValueSelectionSetting.make_one(
            self.boto3_raw_data["valueSelectionSetting"]
        )

    parentSlotTypeSignature = field("parentSlotTypeSignature")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    creationDateTime = field("creationDateTime")

    @cached_property
    def externalSourceSetting(self):  # pragma: no cover
        return ExternalSourceSetting.make_one(
            self.boto3_raw_data["externalSourceSetting"]
        )

    @cached_property
    def compositeSlotTypeSetting(self):  # pragma: no cover
        return CompositeSlotTypeSettingOutput.make_one(
            self.boto3_raw_data["compositeSlotTypeSetting"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSlotTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSlotTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSlotTypeResponse:
    boto3_raw_data: "type_defs.DescribeSlotTypeResponseTypeDef" = dataclasses.field()

    slotTypeId = field("slotTypeId")
    slotTypeName = field("slotTypeName")
    description = field("description")

    @cached_property
    def slotTypeValues(self):  # pragma: no cover
        return SlotTypeValueOutput.make_many(self.boto3_raw_data["slotTypeValues"])

    @cached_property
    def valueSelectionSetting(self):  # pragma: no cover
        return SlotValueSelectionSetting.make_one(
            self.boto3_raw_data["valueSelectionSetting"]
        )

    parentSlotTypeSignature = field("parentSlotTypeSignature")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def externalSourceSetting(self):  # pragma: no cover
        return ExternalSourceSetting.make_one(
            self.boto3_raw_data["externalSourceSetting"]
        )

    @cached_property
    def compositeSlotTypeSetting(self):  # pragma: no cover
        return CompositeSlotTypeSettingOutput.make_one(
            self.boto3_raw_data["compositeSlotTypeSetting"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSlotTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSlotTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSlotTypeResponse:
    boto3_raw_data: "type_defs.UpdateSlotTypeResponseTypeDef" = dataclasses.field()

    slotTypeId = field("slotTypeId")
    slotTypeName = field("slotTypeName")
    description = field("description")

    @cached_property
    def slotTypeValues(self):  # pragma: no cover
        return SlotTypeValueOutput.make_many(self.boto3_raw_data["slotTypeValues"])

    @cached_property
    def valueSelectionSetting(self):  # pragma: no cover
        return SlotValueSelectionSetting.make_one(
            self.boto3_raw_data["valueSelectionSetting"]
        )

    parentSlotTypeSignature = field("parentSlotTypeSignature")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def externalSourceSetting(self):  # pragma: no cover
        return ExternalSourceSetting.make_one(
            self.boto3_raw_data["externalSourceSetting"]
        )

    @cached_property
    def compositeSlotTypeSetting(self):  # pragma: no cover
        return CompositeSlotTypeSettingOutput.make_one(
            self.boto3_raw_data["compositeSlotTypeSetting"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSlotTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSlotTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputSessionStateSpecification:
    boto3_raw_data: "type_defs.InputSessionStateSpecificationTypeDef" = (
        dataclasses.field()
    )

    sessionAttributes = field("sessionAttributes")

    @cached_property
    def activeContexts(self):  # pragma: no cover
        return ActiveContext.make_many(self.boto3_raw_data["activeContexts"])

    @cached_property
    def runtimeHints(self):  # pragma: no cover
        return RuntimeHints.make_one(self.boto3_raw_data["runtimeHints"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InputSessionStateSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputSessionStateSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSlotTypeRequest:
    boto3_raw_data: "type_defs.CreateSlotTypeRequestTypeDef" = dataclasses.field()

    slotTypeName = field("slotTypeName")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    description = field("description")
    slotTypeValues = field("slotTypeValues")

    @cached_property
    def valueSelectionSetting(self):  # pragma: no cover
        return SlotValueSelectionSetting.make_one(
            self.boto3_raw_data["valueSelectionSetting"]
        )

    parentSlotTypeSignature = field("parentSlotTypeSignature")

    @cached_property
    def externalSourceSetting(self):  # pragma: no cover
        return ExternalSourceSetting.make_one(
            self.boto3_raw_data["externalSourceSetting"]
        )

    compositeSlotTypeSetting = field("compositeSlotTypeSetting")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSlotTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSlotTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSlotTypeRequest:
    boto3_raw_data: "type_defs.UpdateSlotTypeRequestTypeDef" = dataclasses.field()

    slotTypeId = field("slotTypeId")
    slotTypeName = field("slotTypeName")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    description = field("description")
    slotTypeValues = field("slotTypeValues")

    @cached_property
    def valueSelectionSetting(self):  # pragma: no cover
        return SlotValueSelectionSetting.make_one(
            self.boto3_raw_data["valueSelectionSetting"]
        )

    parentSlotTypeSignature = field("parentSlotTypeSignature")

    @cached_property
    def externalSourceSetting(self):  # pragma: no cover
        return ExternalSourceSetting.make_one(
            self.boto3_raw_data["externalSourceSetting"]
        )

    compositeSlotTypeSetting = field("compositeSlotTypeSetting")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSlotTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSlotTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentLevelSlotResolutionTestResults:
    boto3_raw_data: "type_defs.IntentLevelSlotResolutionTestResultsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return IntentLevelSlotResolutionTestResultItem.make_many(
            self.boto3_raw_data["items"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IntentLevelSlotResolutionTestResultsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentLevelSlotResolutionTestResultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DialogStateOutput:
    boto3_raw_data: "type_defs.DialogStateOutputTypeDef" = dataclasses.field()

    @cached_property
    def dialogAction(self):  # pragma: no cover
        return DialogAction.make_one(self.boto3_raw_data["dialogAction"])

    @cached_property
    def intent(self):  # pragma: no cover
        return IntentOverrideOutput.make_one(self.boto3_raw_data["intent"])

    sessionAttributes = field("sessionAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DialogStateOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DialogStateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DialogState:
    boto3_raw_data: "type_defs.DialogStateTypeDef" = dataclasses.field()

    @cached_property
    def dialogAction(self):  # pragma: no cover
        return DialogAction.make_one(self.boto3_raw_data["dialogAction"])

    @cached_property
    def intent(self):  # pragma: no cover
        return IntentOverride.make_one(self.boto3_raw_data["intent"])

    sessionAttributes = field("sessionAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DialogStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DialogStateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeImportResponse:
    boto3_raw_data: "type_defs.DescribeImportResponseTypeDef" = dataclasses.field()

    importId = field("importId")

    @cached_property
    def resourceSpecification(self):  # pragma: no cover
        return ImportResourceSpecificationOutput.make_one(
            self.boto3_raw_data["resourceSpecification"]
        )

    importedResourceId = field("importedResourceId")
    importedResourceName = field("importedResourceName")
    mergeStrategy = field("mergeStrategy")
    importStatus = field("importStatus")
    failureReasons = field("failureReasons")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeImportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportResponse:
    boto3_raw_data: "type_defs.StartImportResponseTypeDef" = dataclasses.field()

    importId = field("importId")

    @cached_property
    def resourceSpecification(self):  # pragma: no cover
        return ImportResourceSpecificationOutput.make_one(
            self.boto3_raw_data["resourceSpecification"]
        )

    mergeStrategy = field("mergeStrategy")
    importStatus = field("importStatus")
    creationDateTime = field("creationDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerativeAISettings:
    boto3_raw_data: "type_defs.GenerativeAISettingsTypeDef" = dataclasses.field()

    @cached_property
    def runtimeSettings(self):  # pragma: no cover
        return RuntimeSettings.make_one(self.boto3_raw_data["runtimeSettings"])

    @cached_property
    def buildtimeSettings(self):  # pragma: no cover
        return BuildtimeSettings.make_one(self.boto3_raw_data["buildtimeSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerativeAISettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerativeAISettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FulfillmentStartResponseSpecificationOutput:
    boto3_raw_data: "type_defs.FulfillmentStartResponseSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    delayInSeconds = field("delayInSeconds")

    @cached_property
    def messageGroups(self):  # pragma: no cover
        return MessageGroupOutput.make_many(self.boto3_raw_data["messageGroups"])

    allowInterrupt = field("allowInterrupt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FulfillmentStartResponseSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FulfillmentStartResponseSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FulfillmentUpdateResponseSpecificationOutput:
    boto3_raw_data: "type_defs.FulfillmentUpdateResponseSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    frequencyInSeconds = field("frequencyInSeconds")

    @cached_property
    def messageGroups(self):  # pragma: no cover
        return MessageGroupOutput.make_many(self.boto3_raw_data["messageGroups"])

    allowInterrupt = field("allowInterrupt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FulfillmentUpdateResponseSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FulfillmentUpdateResponseSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptSpecificationOutput:
    boto3_raw_data: "type_defs.PromptSpecificationOutputTypeDef" = dataclasses.field()

    @cached_property
    def messageGroups(self):  # pragma: no cover
        return MessageGroupOutput.make_many(self.boto3_raw_data["messageGroups"])

    maxRetries = field("maxRetries")
    allowInterrupt = field("allowInterrupt")
    messageSelectionStrategy = field("messageSelectionStrategy")
    promptAttemptsSpecification = field("promptAttemptsSpecification")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptSpecificationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseSpecificationOutput:
    boto3_raw_data: "type_defs.ResponseSpecificationOutputTypeDef" = dataclasses.field()

    @cached_property
    def messageGroups(self):  # pragma: no cover
        return MessageGroupOutput.make_many(self.boto3_raw_data["messageGroups"])

    allowInterrupt = field("allowInterrupt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseSpecificationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StillWaitingResponseSpecificationOutput:
    boto3_raw_data: "type_defs.StillWaitingResponseSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def messageGroups(self):  # pragma: no cover
        return MessageGroupOutput.make_many(self.boto3_raw_data["messageGroups"])

    frequencyInSeconds = field("frequencyInSeconds")
    timeoutInSeconds = field("timeoutInSeconds")
    allowInterrupt = field("allowInterrupt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StillWaitingResponseSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StillWaitingResponseSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUtteranceAnalyticsDataResponse:
    boto3_raw_data: "type_defs.ListUtteranceAnalyticsDataResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")

    @cached_property
    def utterances(self):  # pragma: no cover
        return UtteranceSpecification.make_many(self.boto3_raw_data["utterances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListUtteranceAnalyticsDataResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUtteranceAnalyticsDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FulfillmentStartResponseSpecification:
    boto3_raw_data: "type_defs.FulfillmentStartResponseSpecificationTypeDef" = (
        dataclasses.field()
    )

    delayInSeconds = field("delayInSeconds")

    @cached_property
    def messageGroups(self):  # pragma: no cover
        return MessageGroup.make_many(self.boto3_raw_data["messageGroups"])

    allowInterrupt = field("allowInterrupt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FulfillmentStartResponseSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FulfillmentStartResponseSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FulfillmentUpdateResponseSpecification:
    boto3_raw_data: "type_defs.FulfillmentUpdateResponseSpecificationTypeDef" = (
        dataclasses.field()
    )

    frequencyInSeconds = field("frequencyInSeconds")

    @cached_property
    def messageGroups(self):  # pragma: no cover
        return MessageGroup.make_many(self.boto3_raw_data["messageGroups"])

    allowInterrupt = field("allowInterrupt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FulfillmentUpdateResponseSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FulfillmentUpdateResponseSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptSpecification:
    boto3_raw_data: "type_defs.PromptSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def messageGroups(self):  # pragma: no cover
        return MessageGroup.make_many(self.boto3_raw_data["messageGroups"])

    maxRetries = field("maxRetries")
    allowInterrupt = field("allowInterrupt")
    messageSelectionStrategy = field("messageSelectionStrategy")
    promptAttemptsSpecification = field("promptAttemptsSpecification")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseSpecification:
    boto3_raw_data: "type_defs.ResponseSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def messageGroups(self):  # pragma: no cover
        return MessageGroup.make_many(self.boto3_raw_data["messageGroups"])

    allowInterrupt = field("allowInterrupt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResponseSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StillWaitingResponseSpecification:
    boto3_raw_data: "type_defs.StillWaitingResponseSpecificationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def messageGroups(self):  # pragma: no cover
        return MessageGroup.make_many(self.boto3_raw_data["messageGroups"])

    frequencyInSeconds = field("frequencyInSeconds")
    timeoutInSeconds = field("timeoutInSeconds")
    allowInterrupt = field("allowInterrupt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StillWaitingResponseSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StillWaitingResponseSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotAliasResponse:
    boto3_raw_data: "type_defs.CreateBotAliasResponseTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botAliasName = field("botAliasName")
    description = field("description")
    botVersion = field("botVersion")
    botAliasLocaleSettings = field("botAliasLocaleSettings")

    @cached_property
    def conversationLogSettings(self):  # pragma: no cover
        return ConversationLogSettingsOutput.make_one(
            self.boto3_raw_data["conversationLogSettings"]
        )

    @cached_property
    def sentimentAnalysisSettings(self):  # pragma: no cover
        return SentimentAnalysisSettings.make_one(
            self.boto3_raw_data["sentimentAnalysisSettings"]
        )

    botAliasStatus = field("botAliasStatus")
    botId = field("botId")
    creationDateTime = field("creationDateTime")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBotAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotAliasResponse:
    boto3_raw_data: "type_defs.DescribeBotAliasResponseTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botAliasName = field("botAliasName")
    description = field("description")
    botVersion = field("botVersion")
    botAliasLocaleSettings = field("botAliasLocaleSettings")

    @cached_property
    def conversationLogSettings(self):  # pragma: no cover
        return ConversationLogSettingsOutput.make_one(
            self.boto3_raw_data["conversationLogSettings"]
        )

    @cached_property
    def sentimentAnalysisSettings(self):  # pragma: no cover
        return SentimentAnalysisSettings.make_one(
            self.boto3_raw_data["sentimentAnalysisSettings"]
        )

    @cached_property
    def botAliasHistoryEvents(self):  # pragma: no cover
        return BotAliasHistoryEvent.make_many(
            self.boto3_raw_data["botAliasHistoryEvents"]
        )

    botAliasStatus = field("botAliasStatus")
    botId = field("botId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def parentBotNetworks(self):  # pragma: no cover
        return ParentBotNetwork.make_many(self.boto3_raw_data["parentBotNetworks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBotAliasResponse:
    boto3_raw_data: "type_defs.UpdateBotAliasResponseTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botAliasName = field("botAliasName")
    description = field("description")
    botVersion = field("botVersion")
    botAliasLocaleSettings = field("botAliasLocaleSettings")

    @cached_property
    def conversationLogSettings(self):  # pragma: no cover
        return ConversationLogSettingsOutput.make_one(
            self.boto3_raw_data["conversationLogSettings"]
        )

    @cached_property
    def sentimentAnalysisSettings(self):  # pragma: no cover
        return SentimentAnalysisSettings.make_one(
            self.boto3_raw_data["sentimentAnalysisSettings"]
        )

    botAliasStatus = field("botAliasStatus")
    botId = field("botId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBotAliasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBotAliasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketTranscriptSource:
    boto3_raw_data: "type_defs.S3BucketTranscriptSourceTypeDef" = dataclasses.field()

    s3BucketName = field("s3BucketName")
    transcriptFormat = field("transcriptFormat")

    @cached_property
    def pathFormat(self):  # pragma: no cover
        return PathFormat.make_one(self.boto3_raw_data["pathFormat"])

    @cached_property
    def transcriptFilter(self):  # pragma: no cover
        return TranscriptFilter.make_one(self.boto3_raw_data["transcriptFilter"])

    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3BucketTranscriptSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3BucketTranscriptSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranscriptSourceSettingOutput:
    boto3_raw_data: "type_defs.TranscriptSourceSettingOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3BucketTranscriptSource(self):  # pragma: no cover
        return S3BucketTranscriptSourceOutput.make_one(
            self.boto3_raw_data["s3BucketTranscriptSource"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TranscriptSourceSettingOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranscriptSourceSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserTurnInputSpecification:
    boto3_raw_data: "type_defs.UserTurnInputSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def utteranceInput(self):  # pragma: no cover
        return UtteranceInputSpecification.make_one(
            self.boto3_raw_data["utteranceInput"]
        )

    requestAttributes = field("requestAttributes")

    @cached_property
    def sessionState(self):  # pragma: no cover
        return InputSessionStateSpecification.make_one(
            self.boto3_raw_data["sessionState"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserTurnInputSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserTurnInputSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportRequest:
    boto3_raw_data: "type_defs.StartImportRequestTypeDef" = dataclasses.field()

    importId = field("importId")
    resourceSpecification = field("resourceSpecification")
    mergeStrategy = field("mergeStrategy")
    filePassword = field("filePassword")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotLocaleRequest:
    boto3_raw_data: "type_defs.CreateBotLocaleRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    nluIntentConfidenceThreshold = field("nluIntentConfidenceThreshold")
    description = field("description")

    @cached_property
    def voiceSettings(self):  # pragma: no cover
        return VoiceSettings.make_one(self.boto3_raw_data["voiceSettings"])

    @cached_property
    def generativeAISettings(self):  # pragma: no cover
        return GenerativeAISettings.make_one(
            self.boto3_raw_data["generativeAISettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBotLocaleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotLocaleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotLocaleResponse:
    boto3_raw_data: "type_defs.CreateBotLocaleResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeName = field("localeName")
    localeId = field("localeId")
    description = field("description")
    nluIntentConfidenceThreshold = field("nluIntentConfidenceThreshold")

    @cached_property
    def voiceSettings(self):  # pragma: no cover
        return VoiceSettings.make_one(self.boto3_raw_data["voiceSettings"])

    botLocaleStatus = field("botLocaleStatus")
    creationDateTime = field("creationDateTime")

    @cached_property
    def generativeAISettings(self):  # pragma: no cover
        return GenerativeAISettings.make_one(
            self.boto3_raw_data["generativeAISettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBotLocaleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotLocaleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotLocaleResponse:
    boto3_raw_data: "type_defs.DescribeBotLocaleResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    localeName = field("localeName")
    description = field("description")
    nluIntentConfidenceThreshold = field("nluIntentConfidenceThreshold")

    @cached_property
    def voiceSettings(self):  # pragma: no cover
        return VoiceSettings.make_one(self.boto3_raw_data["voiceSettings"])

    intentsCount = field("intentsCount")
    slotTypesCount = field("slotTypesCount")
    botLocaleStatus = field("botLocaleStatus")
    failureReasons = field("failureReasons")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    lastBuildSubmittedDateTime = field("lastBuildSubmittedDateTime")

    @cached_property
    def botLocaleHistoryEvents(self):  # pragma: no cover
        return BotLocaleHistoryEvent.make_many(
            self.boto3_raw_data["botLocaleHistoryEvents"]
        )

    recommendedActions = field("recommendedActions")

    @cached_property
    def generativeAISettings(self):  # pragma: no cover
        return GenerativeAISettings.make_one(
            self.boto3_raw_data["generativeAISettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeBotLocaleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotLocaleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBotLocaleRequest:
    boto3_raw_data: "type_defs.UpdateBotLocaleRequestTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    nluIntentConfidenceThreshold = field("nluIntentConfidenceThreshold")
    description = field("description")

    @cached_property
    def voiceSettings(self):  # pragma: no cover
        return VoiceSettings.make_one(self.boto3_raw_data["voiceSettings"])

    @cached_property
    def generativeAISettings(self):  # pragma: no cover
        return GenerativeAISettings.make_one(
            self.boto3_raw_data["generativeAISettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBotLocaleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBotLocaleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBotLocaleResponse:
    boto3_raw_data: "type_defs.UpdateBotLocaleResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    localeName = field("localeName")
    description = field("description")
    nluIntentConfidenceThreshold = field("nluIntentConfidenceThreshold")

    @cached_property
    def voiceSettings(self):  # pragma: no cover
        return VoiceSettings.make_one(self.boto3_raw_data["voiceSettings"])

    botLocaleStatus = field("botLocaleStatus")
    failureReasons = field("failureReasons")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")
    recommendedActions = field("recommendedActions")

    @cached_property
    def generativeAISettings(self):  # pragma: no cover
        return GenerativeAISettings.make_one(
            self.boto3_raw_data["generativeAISettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBotLocaleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBotLocaleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FulfillmentUpdatesSpecificationOutput:
    boto3_raw_data: "type_defs.FulfillmentUpdatesSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    active = field("active")

    @cached_property
    def startResponse(self):  # pragma: no cover
        return FulfillmentStartResponseSpecificationOutput.make_one(
            self.boto3_raw_data["startResponse"]
        )

    @cached_property
    def updateResponse(self):  # pragma: no cover
        return FulfillmentUpdateResponseSpecificationOutput.make_one(
            self.boto3_raw_data["updateResponse"]
        )

    timeoutInSeconds = field("timeoutInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FulfillmentUpdatesSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FulfillmentUpdatesSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotSummary:
    boto3_raw_data: "type_defs.SlotSummaryTypeDef" = dataclasses.field()

    slotId = field("slotId")
    slotName = field("slotName")
    description = field("description")
    slotConstraint = field("slotConstraint")
    slotTypeId = field("slotTypeId")

    @cached_property
    def valueElicitationPromptSpecification(self):  # pragma: no cover
        return PromptSpecificationOutput.make_one(
            self.boto3_raw_data["valueElicitationPromptSpecification"]
        )

    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlotSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlotSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionalBranchOutput:
    boto3_raw_data: "type_defs.ConditionalBranchOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["condition"])

    @cached_property
    def nextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["nextStep"])

    @cached_property
    def response(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(self.boto3_raw_data["response"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConditionalBranchOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionalBranchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultConditionalBranchOutput:
    boto3_raw_data: "type_defs.DefaultConditionalBranchOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def nextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["nextStep"])

    @cached_property
    def response(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(self.boto3_raw_data["response"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DefaultConditionalBranchOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultConditionalBranchOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaitAndContinueSpecificationOutput:
    boto3_raw_data: "type_defs.WaitAndContinueSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def waitingResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["waitingResponse"]
        )

    @cached_property
    def continueResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["continueResponse"]
        )

    @cached_property
    def stillWaitingResponse(self):  # pragma: no cover
        return StillWaitingResponseSpecificationOutput.make_one(
            self.boto3_raw_data["stillWaitingResponse"]
        )

    active = field("active")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WaitAndContinueSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaitAndContinueSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FulfillmentUpdatesSpecification:
    boto3_raw_data: "type_defs.FulfillmentUpdatesSpecificationTypeDef" = (
        dataclasses.field()
    )

    active = field("active")

    @cached_property
    def startResponse(self):  # pragma: no cover
        return FulfillmentStartResponseSpecification.make_one(
            self.boto3_raw_data["startResponse"]
        )

    @cached_property
    def updateResponse(self):  # pragma: no cover
        return FulfillmentUpdateResponseSpecification.make_one(
            self.boto3_raw_data["updateResponse"]
        )

    timeoutInSeconds = field("timeoutInSeconds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FulfillmentUpdatesSpecificationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FulfillmentUpdatesSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionalBranch:
    boto3_raw_data: "type_defs.ConditionalBranchTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def condition(self):  # pragma: no cover
        return Condition.make_one(self.boto3_raw_data["condition"])

    @cached_property
    def nextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["nextStep"])

    @cached_property
    def response(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["response"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionalBranchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionalBranchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultConditionalBranch:
    boto3_raw_data: "type_defs.DefaultConditionalBranchTypeDef" = dataclasses.field()

    @cached_property
    def nextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["nextStep"])

    @cached_property
    def response(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["response"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefaultConditionalBranchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultConditionalBranchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaitAndContinueSpecification:
    boto3_raw_data: "type_defs.WaitAndContinueSpecificationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def waitingResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["waitingResponse"])

    @cached_property
    def continueResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["continueResponse"])

    @cached_property
    def stillWaitingResponse(self):  # pragma: no cover
        return StillWaitingResponseSpecification.make_one(
            self.boto3_raw_data["stillWaitingResponse"]
        )

    active = field("active")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WaitAndContinueSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WaitAndContinueSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBotAliasRequest:
    boto3_raw_data: "type_defs.CreateBotAliasRequestTypeDef" = dataclasses.field()

    botAliasName = field("botAliasName")
    botId = field("botId")
    description = field("description")
    botVersion = field("botVersion")
    botAliasLocaleSettings = field("botAliasLocaleSettings")
    conversationLogSettings = field("conversationLogSettings")

    @cached_property
    def sentimentAnalysisSettings(self):  # pragma: no cover
        return SentimentAnalysisSettings.make_one(
            self.boto3_raw_data["sentimentAnalysisSettings"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBotAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBotAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBotAliasRequest:
    boto3_raw_data: "type_defs.UpdateBotAliasRequestTypeDef" = dataclasses.field()

    botAliasId = field("botAliasId")
    botAliasName = field("botAliasName")
    botId = field("botId")
    description = field("description")
    botVersion = field("botVersion")
    botAliasLocaleSettings = field("botAliasLocaleSettings")
    conversationLogSettings = field("conversationLogSettings")

    @cached_property
    def sentimentAnalysisSettings(self):  # pragma: no cover
        return SentimentAnalysisSettings.make_one(
            self.boto3_raw_data["sentimentAnalysisSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBotAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBotAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTestSetGenerationRequest:
    boto3_raw_data: "type_defs.StartTestSetGenerationRequestTypeDef" = (
        dataclasses.field()
    )

    testSetName = field("testSetName")

    @cached_property
    def storageLocation(self):  # pragma: no cover
        return TestSetStorageLocation.make_one(self.boto3_raw_data["storageLocation"])

    generationDataSource = field("generationDataSource")
    roleArn = field("roleArn")
    description = field("description")
    testSetTags = field("testSetTags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartTestSetGenerationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTestSetGenerationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranscriptSourceSetting:
    boto3_raw_data: "type_defs.TranscriptSourceSettingTypeDef" = dataclasses.field()

    @cached_property
    def s3BucketTranscriptSource(self):  # pragma: no cover
        return S3BucketTranscriptSource.make_one(
            self.boto3_raw_data["s3BucketTranscriptSource"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranscriptSourceSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranscriptSourceSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeBotRecommendationResponse:
    boto3_raw_data: "type_defs.DescribeBotRecommendationResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botRecommendationStatus = field("botRecommendationStatus")
    botRecommendationId = field("botRecommendationId")
    failureReasons = field("failureReasons")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def transcriptSourceSetting(self):  # pragma: no cover
        return TranscriptSourceSettingOutput.make_one(
            self.boto3_raw_data["transcriptSourceSetting"]
        )

    @cached_property
    def encryptionSetting(self):  # pragma: no cover
        return EncryptionSetting.make_one(self.boto3_raw_data["encryptionSetting"])

    @cached_property
    def botRecommendationResults(self):  # pragma: no cover
        return BotRecommendationResults.make_one(
            self.boto3_raw_data["botRecommendationResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeBotRecommendationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeBotRecommendationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBotRecommendationResponse:
    boto3_raw_data: "type_defs.StartBotRecommendationResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botRecommendationStatus = field("botRecommendationStatus")
    botRecommendationId = field("botRecommendationId")
    creationDateTime = field("creationDateTime")

    @cached_property
    def transcriptSourceSetting(self):  # pragma: no cover
        return TranscriptSourceSettingOutput.make_one(
            self.boto3_raw_data["transcriptSourceSetting"]
        )

    @cached_property
    def encryptionSetting(self):  # pragma: no cover
        return EncryptionSetting.make_one(self.boto3_raw_data["encryptionSetting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartBotRecommendationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBotRecommendationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBotRecommendationResponse:
    boto3_raw_data: "type_defs.UpdateBotRecommendationResponseTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    botRecommendationStatus = field("botRecommendationStatus")
    botRecommendationId = field("botRecommendationId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def transcriptSourceSetting(self):  # pragma: no cover
        return TranscriptSourceSettingOutput.make_one(
            self.boto3_raw_data["transcriptSourceSetting"]
        )

    @cached_property
    def encryptionSetting(self):  # pragma: no cover
        return EncryptionSetting.make_one(self.boto3_raw_data["encryptionSetting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateBotRecommendationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBotRecommendationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserTurnResult:
    boto3_raw_data: "type_defs.UserTurnResultTypeDef" = dataclasses.field()

    @cached_property
    def input(self):  # pragma: no cover
        return UserTurnInputSpecification.make_one(self.boto3_raw_data["input"])

    @cached_property
    def expectedOutput(self):  # pragma: no cover
        return UserTurnOutputSpecification.make_one(
            self.boto3_raw_data["expectedOutput"]
        )

    @cached_property
    def actualOutput(self):  # pragma: no cover
        return UserTurnOutputSpecification.make_one(self.boto3_raw_data["actualOutput"])

    @cached_property
    def errorDetails(self):  # pragma: no cover
        return ExecutionErrorDetails.make_one(self.boto3_raw_data["errorDetails"])

    endToEndResult = field("endToEndResult")
    intentMatchResult = field("intentMatchResult")
    slotMatchResult = field("slotMatchResult")
    speechTranscriptionResult = field("speechTranscriptionResult")

    @cached_property
    def conversationLevelResult(self):  # pragma: no cover
        return ConversationLevelResultDetail.make_one(
            self.boto3_raw_data["conversationLevelResult"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserTurnResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserTurnResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserTurnSpecification:
    boto3_raw_data: "type_defs.UserTurnSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def input(self):  # pragma: no cover
        return UserTurnInputSpecification.make_one(self.boto3_raw_data["input"])

    @cached_property
    def expected(self):  # pragma: no cover
        return UserTurnOutputSpecification.make_one(self.boto3_raw_data["expected"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserTurnSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserTurnSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSlotsResponse:
    boto3_raw_data: "type_defs.ListSlotsResponseTypeDef" = dataclasses.field()

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    intentId = field("intentId")

    @cached_property
    def slotSummaries(self):  # pragma: no cover
        return SlotSummary.make_many(self.boto3_raw_data["slotSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListSlotsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSlotsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionalSpecificationOutput:
    boto3_raw_data: "type_defs.ConditionalSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    active = field("active")

    @cached_property
    def conditionalBranches(self):  # pragma: no cover
        return ConditionalBranchOutput.make_many(
            self.boto3_raw_data["conditionalBranches"]
        )

    @cached_property
    def defaultBranch(self):  # pragma: no cover
        return DefaultConditionalBranchOutput.make_one(
            self.boto3_raw_data["defaultBranch"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConditionalSpecificationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionalSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubSlotValueElicitationSettingOutput:
    boto3_raw_data: "type_defs.SubSlotValueElicitationSettingOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def promptSpecification(self):  # pragma: no cover
        return PromptSpecificationOutput.make_one(
            self.boto3_raw_data["promptSpecification"]
        )

    @cached_property
    def defaultValueSpecification(self):  # pragma: no cover
        return SlotDefaultValueSpecificationOutput.make_one(
            self.boto3_raw_data["defaultValueSpecification"]
        )

    @cached_property
    def sampleUtterances(self):  # pragma: no cover
        return SampleUtterance.make_many(self.boto3_raw_data["sampleUtterances"])

    @cached_property
    def waitAndContinueSpecification(self):  # pragma: no cover
        return WaitAndContinueSpecificationOutput.make_one(
            self.boto3_raw_data["waitAndContinueSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SubSlotValueElicitationSettingOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubSlotValueElicitationSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionalSpecification:
    boto3_raw_data: "type_defs.ConditionalSpecificationTypeDef" = dataclasses.field()

    active = field("active")

    @cached_property
    def conditionalBranches(self):  # pragma: no cover
        return ConditionalBranch.make_many(self.boto3_raw_data["conditionalBranches"])

    @cached_property
    def defaultBranch(self):  # pragma: no cover
        return DefaultConditionalBranch.make_one(self.boto3_raw_data["defaultBranch"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConditionalSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionalSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubSlotValueElicitationSetting:
    boto3_raw_data: "type_defs.SubSlotValueElicitationSettingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def promptSpecification(self):  # pragma: no cover
        return PromptSpecification.make_one(self.boto3_raw_data["promptSpecification"])

    @cached_property
    def defaultValueSpecification(self):  # pragma: no cover
        return SlotDefaultValueSpecification.make_one(
            self.boto3_raw_data["defaultValueSpecification"]
        )

    @cached_property
    def sampleUtterances(self):  # pragma: no cover
        return SampleUtterance.make_many(self.boto3_raw_data["sampleUtterances"])

    @cached_property
    def waitAndContinueSpecification(self):  # pragma: no cover
        return WaitAndContinueSpecification.make_one(
            self.boto3_raw_data["waitAndContinueSpecification"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SubSlotValueElicitationSettingTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubSlotValueElicitationSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetTurnResult:
    boto3_raw_data: "type_defs.TestSetTurnResultTypeDef" = dataclasses.field()

    @cached_property
    def agent(self):  # pragma: no cover
        return AgentTurnResult.make_one(self.boto3_raw_data["agent"])

    @cached_property
    def user(self):  # pragma: no cover
        return UserTurnResult.make_one(self.boto3_raw_data["user"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestSetTurnResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetTurnResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TurnSpecification:
    boto3_raw_data: "type_defs.TurnSpecificationTypeDef" = dataclasses.field()

    @cached_property
    def agentTurn(self):  # pragma: no cover
        return AgentTurnSpecification.make_one(self.boto3_raw_data["agentTurn"])

    @cached_property
    def userTurn(self):  # pragma: no cover
        return UserTurnSpecification.make_one(self.boto3_raw_data["userTurn"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TurnSpecificationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TurnSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentClosingSettingOutput:
    boto3_raw_data: "type_defs.IntentClosingSettingOutputTypeDef" = dataclasses.field()

    @cached_property
    def closingResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["closingResponse"]
        )

    active = field("active")

    @cached_property
    def nextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["nextStep"])

    @cached_property
    def conditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["conditional"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntentClosingSettingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentClosingSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostDialogCodeHookInvocationSpecificationOutput:
    boto3_raw_data: (
        "type_defs.PostDialogCodeHookInvocationSpecificationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def successResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["successResponse"]
        )

    @cached_property
    def successNextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["successNextStep"])

    @cached_property
    def successConditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["successConditional"]
        )

    @cached_property
    def failureResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["failureResponse"]
        )

    @cached_property
    def failureNextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["failureNextStep"])

    @cached_property
    def failureConditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["failureConditional"]
        )

    @cached_property
    def timeoutResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["timeoutResponse"]
        )

    @cached_property
    def timeoutNextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["timeoutNextStep"])

    @cached_property
    def timeoutConditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["timeoutConditional"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PostDialogCodeHookInvocationSpecificationOutputTypeDef"
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
                "type_defs.PostDialogCodeHookInvocationSpecificationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostFulfillmentStatusSpecificationOutput:
    boto3_raw_data: "type_defs.PostFulfillmentStatusSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def successResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["successResponse"]
        )

    @cached_property
    def failureResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["failureResponse"]
        )

    @cached_property
    def timeoutResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["timeoutResponse"]
        )

    @cached_property
    def successNextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["successNextStep"])

    @cached_property
    def successConditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["successConditional"]
        )

    @cached_property
    def failureNextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["failureNextStep"])

    @cached_property
    def failureConditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["failureConditional"]
        )

    @cached_property
    def timeoutNextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["timeoutNextStep"])

    @cached_property
    def timeoutConditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["timeoutConditional"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PostFulfillmentStatusSpecificationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostFulfillmentStatusSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpecificationsOutput:
    boto3_raw_data: "type_defs.SpecificationsOutputTypeDef" = dataclasses.field()

    slotTypeId = field("slotTypeId")

    @cached_property
    def valueElicitationSetting(self):  # pragma: no cover
        return SubSlotValueElicitationSettingOutput.make_one(
            self.boto3_raw_data["valueElicitationSetting"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpecificationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpecificationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentClosingSetting:
    boto3_raw_data: "type_defs.IntentClosingSettingTypeDef" = dataclasses.field()

    @cached_property
    def closingResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["closingResponse"])

    active = field("active")

    @cached_property
    def nextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["nextStep"])

    @cached_property
    def conditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(self.boto3_raw_data["conditional"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntentClosingSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentClosingSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostDialogCodeHookInvocationSpecification:
    boto3_raw_data: "type_defs.PostDialogCodeHookInvocationSpecificationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def successResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["successResponse"])

    @cached_property
    def successNextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["successNextStep"])

    @cached_property
    def successConditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(
            self.boto3_raw_data["successConditional"]
        )

    @cached_property
    def failureResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["failureResponse"])

    @cached_property
    def failureNextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["failureNextStep"])

    @cached_property
    def failureConditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(
            self.boto3_raw_data["failureConditional"]
        )

    @cached_property
    def timeoutResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["timeoutResponse"])

    @cached_property
    def timeoutNextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["timeoutNextStep"])

    @cached_property
    def timeoutConditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(
            self.boto3_raw_data["timeoutConditional"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PostDialogCodeHookInvocationSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostDialogCodeHookInvocationSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostFulfillmentStatusSpecification:
    boto3_raw_data: "type_defs.PostFulfillmentStatusSpecificationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def successResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["successResponse"])

    @cached_property
    def failureResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["failureResponse"])

    @cached_property
    def timeoutResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["timeoutResponse"])

    @cached_property
    def successNextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["successNextStep"])

    @cached_property
    def successConditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(
            self.boto3_raw_data["successConditional"]
        )

    @cached_property
    def failureNextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["failureNextStep"])

    @cached_property
    def failureConditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(
            self.boto3_raw_data["failureConditional"]
        )

    @cached_property
    def timeoutNextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["timeoutNextStep"])

    @cached_property
    def timeoutConditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(
            self.boto3_raw_data["timeoutConditional"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PostFulfillmentStatusSpecificationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostFulfillmentStatusSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Specifications:
    boto3_raw_data: "type_defs.SpecificationsTypeDef" = dataclasses.field()

    slotTypeId = field("slotTypeId")

    @cached_property
    def valueElicitationSetting(self):  # pragma: no cover
        return SubSlotValueElicitationSetting.make_one(
            self.boto3_raw_data["valueElicitationSetting"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpecificationsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SpecificationsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBotRecommendationRequest:
    boto3_raw_data: "type_defs.StartBotRecommendationRequestTypeDef" = (
        dataclasses.field()
    )

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    transcriptSourceSetting = field("transcriptSourceSetting")

    @cached_property
    def encryptionSetting(self):  # pragma: no cover
        return EncryptionSetting.make_one(self.boto3_raw_data["encryptionSetting"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartBotRecommendationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartBotRecommendationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtteranceLevelTestResultItem:
    boto3_raw_data: "type_defs.UtteranceLevelTestResultItemTypeDef" = (
        dataclasses.field()
    )

    recordNumber = field("recordNumber")

    @cached_property
    def turnResult(self):  # pragma: no cover
        return TestSetTurnResult.make_one(self.boto3_raw_data["turnResult"])

    conversationId = field("conversationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UtteranceLevelTestResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UtteranceLevelTestResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSetTurnRecord:
    boto3_raw_data: "type_defs.TestSetTurnRecordTypeDef" = dataclasses.field()

    recordNumber = field("recordNumber")

    @cached_property
    def turnSpecification(self):  # pragma: no cover
        return TurnSpecification.make_one(self.boto3_raw_data["turnSpecification"])

    conversationId = field("conversationId")
    turnNumber = field("turnNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestSetTurnRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSetTurnRecordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DialogCodeHookInvocationSettingOutput:
    boto3_raw_data: "type_defs.DialogCodeHookInvocationSettingOutputTypeDef" = (
        dataclasses.field()
    )

    enableCodeHookInvocation = field("enableCodeHookInvocation")
    active = field("active")

    @cached_property
    def postCodeHookSpecification(self):  # pragma: no cover
        return PostDialogCodeHookInvocationSpecificationOutput.make_one(
            self.boto3_raw_data["postCodeHookSpecification"]
        )

    invocationLabel = field("invocationLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DialogCodeHookInvocationSettingOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DialogCodeHookInvocationSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FulfillmentCodeHookSettingsOutput:
    boto3_raw_data: "type_defs.FulfillmentCodeHookSettingsOutputTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")

    @cached_property
    def postFulfillmentStatusSpecification(self):  # pragma: no cover
        return PostFulfillmentStatusSpecificationOutput.make_one(
            self.boto3_raw_data["postFulfillmentStatusSpecification"]
        )

    @cached_property
    def fulfillmentUpdatesSpecification(self):  # pragma: no cover
        return FulfillmentUpdatesSpecificationOutput.make_one(
            self.boto3_raw_data["fulfillmentUpdatesSpecification"]
        )

    active = field("active")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FulfillmentCodeHookSettingsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FulfillmentCodeHookSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubSlotSettingOutput:
    boto3_raw_data: "type_defs.SubSlotSettingOutputTypeDef" = dataclasses.field()

    expression = field("expression")
    slotSpecifications = field("slotSpecifications")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubSlotSettingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubSlotSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DialogCodeHookInvocationSetting:
    boto3_raw_data: "type_defs.DialogCodeHookInvocationSettingTypeDef" = (
        dataclasses.field()
    )

    enableCodeHookInvocation = field("enableCodeHookInvocation")
    active = field("active")

    @cached_property
    def postCodeHookSpecification(self):  # pragma: no cover
        return PostDialogCodeHookInvocationSpecification.make_one(
            self.boto3_raw_data["postCodeHookSpecification"]
        )

    invocationLabel = field("invocationLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DialogCodeHookInvocationSettingTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DialogCodeHookInvocationSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FulfillmentCodeHookSettings:
    boto3_raw_data: "type_defs.FulfillmentCodeHookSettingsTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @cached_property
    def postFulfillmentStatusSpecification(self):  # pragma: no cover
        return PostFulfillmentStatusSpecification.make_one(
            self.boto3_raw_data["postFulfillmentStatusSpecification"]
        )

    @cached_property
    def fulfillmentUpdatesSpecification(self):  # pragma: no cover
        return FulfillmentUpdatesSpecification.make_one(
            self.boto3_raw_data["fulfillmentUpdatesSpecification"]
        )

    active = field("active")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FulfillmentCodeHookSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FulfillmentCodeHookSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubSlotSetting:
    boto3_raw_data: "type_defs.SubSlotSettingTypeDef" = dataclasses.field()

    expression = field("expression")
    slotSpecifications = field("slotSpecifications")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubSlotSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubSlotSettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UtteranceLevelTestResults:
    boto3_raw_data: "type_defs.UtteranceLevelTestResultsTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return UtteranceLevelTestResultItem.make_many(self.boto3_raw_data["items"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UtteranceLevelTestResultsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UtteranceLevelTestResultsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestSetRecordsResponse:
    boto3_raw_data: "type_defs.ListTestSetRecordsResponseTypeDef" = dataclasses.field()

    @cached_property
    def testSetRecords(self):  # pragma: no cover
        return TestSetTurnRecord.make_many(self.boto3_raw_data["testSetRecords"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestSetRecordsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestSetRecordsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitialResponseSettingOutput:
    boto3_raw_data: "type_defs.InitialResponseSettingOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def initialResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["initialResponse"]
        )

    @cached_property
    def nextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["nextStep"])

    @cached_property
    def conditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["conditional"]
        )

    @cached_property
    def codeHook(self):  # pragma: no cover
        return DialogCodeHookInvocationSettingOutput.make_one(
            self.boto3_raw_data["codeHook"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InitialResponseSettingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitialResponseSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentConfirmationSettingOutput:
    boto3_raw_data: "type_defs.IntentConfirmationSettingOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def promptSpecification(self):  # pragma: no cover
        return PromptSpecificationOutput.make_one(
            self.boto3_raw_data["promptSpecification"]
        )

    @cached_property
    def declinationResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["declinationResponse"]
        )

    active = field("active")

    @cached_property
    def confirmationResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["confirmationResponse"]
        )

    @cached_property
    def confirmationNextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["confirmationNextStep"])

    @cached_property
    def confirmationConditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["confirmationConditional"]
        )

    @cached_property
    def declinationNextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["declinationNextStep"])

    @cached_property
    def declinationConditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["declinationConditional"]
        )

    @cached_property
    def failureResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["failureResponse"]
        )

    @cached_property
    def failureNextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["failureNextStep"])

    @cached_property
    def failureConditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["failureConditional"]
        )

    @cached_property
    def codeHook(self):  # pragma: no cover
        return DialogCodeHookInvocationSettingOutput.make_one(
            self.boto3_raw_data["codeHook"]
        )

    @cached_property
    def elicitationCodeHook(self):  # pragma: no cover
        return ElicitationCodeHookInvocationSetting.make_one(
            self.boto3_raw_data["elicitationCodeHook"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IntentConfirmationSettingOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentConfirmationSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotCaptureSettingOutput:
    boto3_raw_data: "type_defs.SlotCaptureSettingOutputTypeDef" = dataclasses.field()

    @cached_property
    def captureResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["captureResponse"]
        )

    @cached_property
    def captureNextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["captureNextStep"])

    @cached_property
    def captureConditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["captureConditional"]
        )

    @cached_property
    def failureResponse(self):  # pragma: no cover
        return ResponseSpecificationOutput.make_one(
            self.boto3_raw_data["failureResponse"]
        )

    @cached_property
    def failureNextStep(self):  # pragma: no cover
        return DialogStateOutput.make_one(self.boto3_raw_data["failureNextStep"])

    @cached_property
    def failureConditional(self):  # pragma: no cover
        return ConditionalSpecificationOutput.make_one(
            self.boto3_raw_data["failureConditional"]
        )

    @cached_property
    def codeHook(self):  # pragma: no cover
        return DialogCodeHookInvocationSettingOutput.make_one(
            self.boto3_raw_data["codeHook"]
        )

    @cached_property
    def elicitationCodeHook(self):  # pragma: no cover
        return ElicitationCodeHookInvocationSetting.make_one(
            self.boto3_raw_data["elicitationCodeHook"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotCaptureSettingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotCaptureSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitialResponseSetting:
    boto3_raw_data: "type_defs.InitialResponseSettingTypeDef" = dataclasses.field()

    @cached_property
    def initialResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["initialResponse"])

    @cached_property
    def nextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["nextStep"])

    @cached_property
    def conditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(self.boto3_raw_data["conditional"])

    @cached_property
    def codeHook(self):  # pragma: no cover
        return DialogCodeHookInvocationSetting.make_one(self.boto3_raw_data["codeHook"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InitialResponseSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InitialResponseSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntentConfirmationSetting:
    boto3_raw_data: "type_defs.IntentConfirmationSettingTypeDef" = dataclasses.field()

    @cached_property
    def promptSpecification(self):  # pragma: no cover
        return PromptSpecification.make_one(self.boto3_raw_data["promptSpecification"])

    @cached_property
    def declinationResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(
            self.boto3_raw_data["declinationResponse"]
        )

    active = field("active")

    @cached_property
    def confirmationResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(
            self.boto3_raw_data["confirmationResponse"]
        )

    @cached_property
    def confirmationNextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["confirmationNextStep"])

    @cached_property
    def confirmationConditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(
            self.boto3_raw_data["confirmationConditional"]
        )

    @cached_property
    def declinationNextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["declinationNextStep"])

    @cached_property
    def declinationConditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(
            self.boto3_raw_data["declinationConditional"]
        )

    @cached_property
    def failureResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["failureResponse"])

    @cached_property
    def failureNextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["failureNextStep"])

    @cached_property
    def failureConditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(
            self.boto3_raw_data["failureConditional"]
        )

    @cached_property
    def codeHook(self):  # pragma: no cover
        return DialogCodeHookInvocationSetting.make_one(self.boto3_raw_data["codeHook"])

    @cached_property
    def elicitationCodeHook(self):  # pragma: no cover
        return ElicitationCodeHookInvocationSetting.make_one(
            self.boto3_raw_data["elicitationCodeHook"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntentConfirmationSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntentConfirmationSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotCaptureSetting:
    boto3_raw_data: "type_defs.SlotCaptureSettingTypeDef" = dataclasses.field()

    @cached_property
    def captureResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["captureResponse"])

    @cached_property
    def captureNextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["captureNextStep"])

    @cached_property
    def captureConditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(
            self.boto3_raw_data["captureConditional"]
        )

    @cached_property
    def failureResponse(self):  # pragma: no cover
        return ResponseSpecification.make_one(self.boto3_raw_data["failureResponse"])

    @cached_property
    def failureNextStep(self):  # pragma: no cover
        return DialogState.make_one(self.boto3_raw_data["failureNextStep"])

    @cached_property
    def failureConditional(self):  # pragma: no cover
        return ConditionalSpecification.make_one(
            self.boto3_raw_data["failureConditional"]
        )

    @cached_property
    def codeHook(self):  # pragma: no cover
        return DialogCodeHookInvocationSetting.make_one(self.boto3_raw_data["codeHook"])

    @cached_property
    def elicitationCodeHook(self):  # pragma: no cover
        return ElicitationCodeHookInvocationSetting.make_one(
            self.boto3_raw_data["elicitationCodeHook"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotCaptureSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotCaptureSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestExecutionResultItems:
    boto3_raw_data: "type_defs.TestExecutionResultItemsTypeDef" = dataclasses.field()

    @cached_property
    def overallTestResults(self):  # pragma: no cover
        return OverallTestResults.make_one(self.boto3_raw_data["overallTestResults"])

    @cached_property
    def conversationLevelTestResults(self):  # pragma: no cover
        return ConversationLevelTestResults.make_one(
            self.boto3_raw_data["conversationLevelTestResults"]
        )

    @cached_property
    def intentClassificationTestResults(self):  # pragma: no cover
        return IntentClassificationTestResults.make_one(
            self.boto3_raw_data["intentClassificationTestResults"]
        )

    @cached_property
    def intentLevelSlotResolutionTestResults(self):  # pragma: no cover
        return IntentLevelSlotResolutionTestResults.make_one(
            self.boto3_raw_data["intentLevelSlotResolutionTestResults"]
        )

    @cached_property
    def utteranceLevelTestResults(self):  # pragma: no cover
        return UtteranceLevelTestResults.make_one(
            self.boto3_raw_data["utteranceLevelTestResults"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestExecutionResultItemsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestExecutionResultItemsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntentResponse:
    boto3_raw_data: "type_defs.CreateIntentResponseTypeDef" = dataclasses.field()

    intentId = field("intentId")
    intentName = field("intentName")
    description = field("description")
    parentIntentSignature = field("parentIntentSignature")

    @cached_property
    def sampleUtterances(self):  # pragma: no cover
        return SampleUtterance.make_many(self.boto3_raw_data["sampleUtterances"])

    @cached_property
    def dialogCodeHook(self):  # pragma: no cover
        return DialogCodeHookSettings.make_one(self.boto3_raw_data["dialogCodeHook"])

    @cached_property
    def fulfillmentCodeHook(self):  # pragma: no cover
        return FulfillmentCodeHookSettingsOutput.make_one(
            self.boto3_raw_data["fulfillmentCodeHook"]
        )

    @cached_property
    def intentConfirmationSetting(self):  # pragma: no cover
        return IntentConfirmationSettingOutput.make_one(
            self.boto3_raw_data["intentConfirmationSetting"]
        )

    @cached_property
    def intentClosingSetting(self):  # pragma: no cover
        return IntentClosingSettingOutput.make_one(
            self.boto3_raw_data["intentClosingSetting"]
        )

    @cached_property
    def inputContexts(self):  # pragma: no cover
        return InputContext.make_many(self.boto3_raw_data["inputContexts"])

    @cached_property
    def outputContexts(self):  # pragma: no cover
        return OutputContext.make_many(self.boto3_raw_data["outputContexts"])

    @cached_property
    def kendraConfiguration(self):  # pragma: no cover
        return KendraConfiguration.make_one(self.boto3_raw_data["kendraConfiguration"])

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    creationDateTime = field("creationDateTime")

    @cached_property
    def initialResponseSetting(self):  # pragma: no cover
        return InitialResponseSettingOutput.make_one(
            self.boto3_raw_data["initialResponseSetting"]
        )

    @cached_property
    def qnAIntentConfiguration(self):  # pragma: no cover
        return QnAIntentConfigurationOutput.make_one(
            self.boto3_raw_data["qnAIntentConfiguration"]
        )

    @cached_property
    def qInConnectIntentConfiguration(self):  # pragma: no cover
        return QInConnectIntentConfiguration.make_one(
            self.boto3_raw_data["qInConnectIntentConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIntentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIntentResponse:
    boto3_raw_data: "type_defs.DescribeIntentResponseTypeDef" = dataclasses.field()

    intentId = field("intentId")
    intentName = field("intentName")
    description = field("description")
    parentIntentSignature = field("parentIntentSignature")

    @cached_property
    def sampleUtterances(self):  # pragma: no cover
        return SampleUtterance.make_many(self.boto3_raw_data["sampleUtterances"])

    @cached_property
    def dialogCodeHook(self):  # pragma: no cover
        return DialogCodeHookSettings.make_one(self.boto3_raw_data["dialogCodeHook"])

    @cached_property
    def fulfillmentCodeHook(self):  # pragma: no cover
        return FulfillmentCodeHookSettingsOutput.make_one(
            self.boto3_raw_data["fulfillmentCodeHook"]
        )

    @cached_property
    def slotPriorities(self):  # pragma: no cover
        return SlotPriority.make_many(self.boto3_raw_data["slotPriorities"])

    @cached_property
    def intentConfirmationSetting(self):  # pragma: no cover
        return IntentConfirmationSettingOutput.make_one(
            self.boto3_raw_data["intentConfirmationSetting"]
        )

    @cached_property
    def intentClosingSetting(self):  # pragma: no cover
        return IntentClosingSettingOutput.make_one(
            self.boto3_raw_data["intentClosingSetting"]
        )

    @cached_property
    def inputContexts(self):  # pragma: no cover
        return InputContext.make_many(self.boto3_raw_data["inputContexts"])

    @cached_property
    def outputContexts(self):  # pragma: no cover
        return OutputContext.make_many(self.boto3_raw_data["outputContexts"])

    @cached_property
    def kendraConfiguration(self):  # pragma: no cover
        return KendraConfiguration.make_one(self.boto3_raw_data["kendraConfiguration"])

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def initialResponseSetting(self):  # pragma: no cover
        return InitialResponseSettingOutput.make_one(
            self.boto3_raw_data["initialResponseSetting"]
        )

    @cached_property
    def qnAIntentConfiguration(self):  # pragma: no cover
        return QnAIntentConfigurationOutput.make_one(
            self.boto3_raw_data["qnAIntentConfiguration"]
        )

    @cached_property
    def qInConnectIntentConfiguration(self):  # pragma: no cover
        return QInConnectIntentConfiguration.make_one(
            self.boto3_raw_data["qInConnectIntentConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIntentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIntentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIntentResponse:
    boto3_raw_data: "type_defs.UpdateIntentResponseTypeDef" = dataclasses.field()

    intentId = field("intentId")
    intentName = field("intentName")
    description = field("description")
    parentIntentSignature = field("parentIntentSignature")

    @cached_property
    def sampleUtterances(self):  # pragma: no cover
        return SampleUtterance.make_many(self.boto3_raw_data["sampleUtterances"])

    @cached_property
    def dialogCodeHook(self):  # pragma: no cover
        return DialogCodeHookSettings.make_one(self.boto3_raw_data["dialogCodeHook"])

    @cached_property
    def fulfillmentCodeHook(self):  # pragma: no cover
        return FulfillmentCodeHookSettingsOutput.make_one(
            self.boto3_raw_data["fulfillmentCodeHook"]
        )

    @cached_property
    def slotPriorities(self):  # pragma: no cover
        return SlotPriority.make_many(self.boto3_raw_data["slotPriorities"])

    @cached_property
    def intentConfirmationSetting(self):  # pragma: no cover
        return IntentConfirmationSettingOutput.make_one(
            self.boto3_raw_data["intentConfirmationSetting"]
        )

    @cached_property
    def intentClosingSetting(self):  # pragma: no cover
        return IntentClosingSettingOutput.make_one(
            self.boto3_raw_data["intentClosingSetting"]
        )

    @cached_property
    def inputContexts(self):  # pragma: no cover
        return InputContext.make_many(self.boto3_raw_data["inputContexts"])

    @cached_property
    def outputContexts(self):  # pragma: no cover
        return OutputContext.make_many(self.boto3_raw_data["outputContexts"])

    @cached_property
    def kendraConfiguration(self):  # pragma: no cover
        return KendraConfiguration.make_one(self.boto3_raw_data["kendraConfiguration"])

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def initialResponseSetting(self):  # pragma: no cover
        return InitialResponseSettingOutput.make_one(
            self.boto3_raw_data["initialResponseSetting"]
        )

    @cached_property
    def qnAIntentConfiguration(self):  # pragma: no cover
        return QnAIntentConfigurationOutput.make_one(
            self.boto3_raw_data["qnAIntentConfiguration"]
        )

    @cached_property
    def qInConnectIntentConfiguration(self):  # pragma: no cover
        return QInConnectIntentConfiguration.make_one(
            self.boto3_raw_data["qInConnectIntentConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIntentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIntentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotValueElicitationSettingOutput:
    boto3_raw_data: "type_defs.SlotValueElicitationSettingOutputTypeDef" = (
        dataclasses.field()
    )

    slotConstraint = field("slotConstraint")

    @cached_property
    def defaultValueSpecification(self):  # pragma: no cover
        return SlotDefaultValueSpecificationOutput.make_one(
            self.boto3_raw_data["defaultValueSpecification"]
        )

    @cached_property
    def promptSpecification(self):  # pragma: no cover
        return PromptSpecificationOutput.make_one(
            self.boto3_raw_data["promptSpecification"]
        )

    @cached_property
    def sampleUtterances(self):  # pragma: no cover
        return SampleUtterance.make_many(self.boto3_raw_data["sampleUtterances"])

    @cached_property
    def waitAndContinueSpecification(self):  # pragma: no cover
        return WaitAndContinueSpecificationOutput.make_one(
            self.boto3_raw_data["waitAndContinueSpecification"]
        )

    @cached_property
    def slotCaptureSetting(self):  # pragma: no cover
        return SlotCaptureSettingOutput.make_one(
            self.boto3_raw_data["slotCaptureSetting"]
        )

    @cached_property
    def slotResolutionSetting(self):  # pragma: no cover
        return SlotResolutionSetting.make_one(
            self.boto3_raw_data["slotResolutionSetting"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SlotValueElicitationSettingOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotValueElicitationSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlotValueElicitationSetting:
    boto3_raw_data: "type_defs.SlotValueElicitationSettingTypeDef" = dataclasses.field()

    slotConstraint = field("slotConstraint")

    @cached_property
    def defaultValueSpecification(self):  # pragma: no cover
        return SlotDefaultValueSpecification.make_one(
            self.boto3_raw_data["defaultValueSpecification"]
        )

    @cached_property
    def promptSpecification(self):  # pragma: no cover
        return PromptSpecification.make_one(self.boto3_raw_data["promptSpecification"])

    @cached_property
    def sampleUtterances(self):  # pragma: no cover
        return SampleUtterance.make_many(self.boto3_raw_data["sampleUtterances"])

    @cached_property
    def waitAndContinueSpecification(self):  # pragma: no cover
        return WaitAndContinueSpecification.make_one(
            self.boto3_raw_data["waitAndContinueSpecification"]
        )

    @cached_property
    def slotCaptureSetting(self):  # pragma: no cover
        return SlotCaptureSetting.make_one(self.boto3_raw_data["slotCaptureSetting"])

    @cached_property
    def slotResolutionSetting(self):  # pragma: no cover
        return SlotResolutionSetting.make_one(
            self.boto3_raw_data["slotResolutionSetting"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlotValueElicitationSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlotValueElicitationSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestExecutionResultItemsResponse:
    boto3_raw_data: "type_defs.ListTestExecutionResultItemsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def testExecutionResults(self):  # pragma: no cover
        return TestExecutionResultItems.make_one(
            self.boto3_raw_data["testExecutionResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTestExecutionResultItemsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestExecutionResultItemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSlotResponse:
    boto3_raw_data: "type_defs.CreateSlotResponseTypeDef" = dataclasses.field()

    slotId = field("slotId")
    slotName = field("slotName")
    description = field("description")
    slotTypeId = field("slotTypeId")

    @cached_property
    def valueElicitationSetting(self):  # pragma: no cover
        return SlotValueElicitationSettingOutput.make_one(
            self.boto3_raw_data["valueElicitationSetting"]
        )

    @cached_property
    def obfuscationSetting(self):  # pragma: no cover
        return ObfuscationSetting.make_one(self.boto3_raw_data["obfuscationSetting"])

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    intentId = field("intentId")
    creationDateTime = field("creationDateTime")

    @cached_property
    def multipleValuesSetting(self):  # pragma: no cover
        return MultipleValuesSetting.make_one(
            self.boto3_raw_data["multipleValuesSetting"]
        )

    @cached_property
    def subSlotSetting(self):  # pragma: no cover
        return SubSlotSettingOutput.make_one(self.boto3_raw_data["subSlotSetting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSlotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSlotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSlotResponse:
    boto3_raw_data: "type_defs.DescribeSlotResponseTypeDef" = dataclasses.field()

    slotId = field("slotId")
    slotName = field("slotName")
    description = field("description")
    slotTypeId = field("slotTypeId")

    @cached_property
    def valueElicitationSetting(self):  # pragma: no cover
        return SlotValueElicitationSettingOutput.make_one(
            self.boto3_raw_data["valueElicitationSetting"]
        )

    @cached_property
    def obfuscationSetting(self):  # pragma: no cover
        return ObfuscationSetting.make_one(self.boto3_raw_data["obfuscationSetting"])

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    intentId = field("intentId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def multipleValuesSetting(self):  # pragma: no cover
        return MultipleValuesSetting.make_one(
            self.boto3_raw_data["multipleValuesSetting"]
        )

    @cached_property
    def subSlotSetting(self):  # pragma: no cover
        return SubSlotSettingOutput.make_one(self.boto3_raw_data["subSlotSetting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSlotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSlotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSlotResponse:
    boto3_raw_data: "type_defs.UpdateSlotResponseTypeDef" = dataclasses.field()

    slotId = field("slotId")
    slotName = field("slotName")
    description = field("description")
    slotTypeId = field("slotTypeId")

    @cached_property
    def valueElicitationSetting(self):  # pragma: no cover
        return SlotValueElicitationSettingOutput.make_one(
            self.boto3_raw_data["valueElicitationSetting"]
        )

    @cached_property
    def obfuscationSetting(self):  # pragma: no cover
        return ObfuscationSetting.make_one(self.boto3_raw_data["obfuscationSetting"])

    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    intentId = field("intentId")
    creationDateTime = field("creationDateTime")
    lastUpdatedDateTime = field("lastUpdatedDateTime")

    @cached_property
    def multipleValuesSetting(self):  # pragma: no cover
        return MultipleValuesSetting.make_one(
            self.boto3_raw_data["multipleValuesSetting"]
        )

    @cached_property
    def subSlotSetting(self):  # pragma: no cover
        return SubSlotSettingOutput.make_one(self.boto3_raw_data["subSlotSetting"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSlotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSlotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntentRequest:
    boto3_raw_data: "type_defs.CreateIntentRequestTypeDef" = dataclasses.field()

    intentName = field("intentName")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    description = field("description")
    parentIntentSignature = field("parentIntentSignature")

    @cached_property
    def sampleUtterances(self):  # pragma: no cover
        return SampleUtterance.make_many(self.boto3_raw_data["sampleUtterances"])

    @cached_property
    def dialogCodeHook(self):  # pragma: no cover
        return DialogCodeHookSettings.make_one(self.boto3_raw_data["dialogCodeHook"])

    fulfillmentCodeHook = field("fulfillmentCodeHook")
    intentConfirmationSetting = field("intentConfirmationSetting")
    intentClosingSetting = field("intentClosingSetting")

    @cached_property
    def inputContexts(self):  # pragma: no cover
        return InputContext.make_many(self.boto3_raw_data["inputContexts"])

    @cached_property
    def outputContexts(self):  # pragma: no cover
        return OutputContext.make_many(self.boto3_raw_data["outputContexts"])

    @cached_property
    def kendraConfiguration(self):  # pragma: no cover
        return KendraConfiguration.make_one(self.boto3_raw_data["kendraConfiguration"])

    initialResponseSetting = field("initialResponseSetting")
    qnAIntentConfiguration = field("qnAIntentConfiguration")

    @cached_property
    def qInConnectIntentConfiguration(self):  # pragma: no cover
        return QInConnectIntentConfiguration.make_one(
            self.boto3_raw_data["qInConnectIntentConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIntentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIntentRequest:
    boto3_raw_data: "type_defs.UpdateIntentRequestTypeDef" = dataclasses.field()

    intentId = field("intentId")
    intentName = field("intentName")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    description = field("description")
    parentIntentSignature = field("parentIntentSignature")

    @cached_property
    def sampleUtterances(self):  # pragma: no cover
        return SampleUtterance.make_many(self.boto3_raw_data["sampleUtterances"])

    @cached_property
    def dialogCodeHook(self):  # pragma: no cover
        return DialogCodeHookSettings.make_one(self.boto3_raw_data["dialogCodeHook"])

    fulfillmentCodeHook = field("fulfillmentCodeHook")

    @cached_property
    def slotPriorities(self):  # pragma: no cover
        return SlotPriority.make_many(self.boto3_raw_data["slotPriorities"])

    intentConfirmationSetting = field("intentConfirmationSetting")
    intentClosingSetting = field("intentClosingSetting")

    @cached_property
    def inputContexts(self):  # pragma: no cover
        return InputContext.make_many(self.boto3_raw_data["inputContexts"])

    @cached_property
    def outputContexts(self):  # pragma: no cover
        return OutputContext.make_many(self.boto3_raw_data["outputContexts"])

    @cached_property
    def kendraConfiguration(self):  # pragma: no cover
        return KendraConfiguration.make_one(self.boto3_raw_data["kendraConfiguration"])

    initialResponseSetting = field("initialResponseSetting")
    qnAIntentConfiguration = field("qnAIntentConfiguration")

    @cached_property
    def qInConnectIntentConfiguration(self):  # pragma: no cover
        return QInConnectIntentConfiguration.make_one(
            self.boto3_raw_data["qInConnectIntentConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIntentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIntentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSlotRequest:
    boto3_raw_data: "type_defs.CreateSlotRequestTypeDef" = dataclasses.field()

    slotName = field("slotName")
    valueElicitationSetting = field("valueElicitationSetting")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    intentId = field("intentId")
    description = field("description")
    slotTypeId = field("slotTypeId")

    @cached_property
    def obfuscationSetting(self):  # pragma: no cover
        return ObfuscationSetting.make_one(self.boto3_raw_data["obfuscationSetting"])

    @cached_property
    def multipleValuesSetting(self):  # pragma: no cover
        return MultipleValuesSetting.make_one(
            self.boto3_raw_data["multipleValuesSetting"]
        )

    subSlotSetting = field("subSlotSetting")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateSlotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSlotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSlotRequest:
    boto3_raw_data: "type_defs.UpdateSlotRequestTypeDef" = dataclasses.field()

    slotId = field("slotId")
    slotName = field("slotName")
    valueElicitationSetting = field("valueElicitationSetting")
    botId = field("botId")
    botVersion = field("botVersion")
    localeId = field("localeId")
    intentId = field("intentId")
    description = field("description")
    slotTypeId = field("slotTypeId")

    @cached_property
    def obfuscationSetting(self):  # pragma: no cover
        return ObfuscationSetting.make_one(self.boto3_raw_data["obfuscationSetting"])

    @cached_property
    def multipleValuesSetting(self):  # pragma: no cover
        return MultipleValuesSetting.make_one(
            self.boto3_raw_data["multipleValuesSetting"]
        )

    subSlotSetting = field("subSlotSetting")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateSlotRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSlotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
