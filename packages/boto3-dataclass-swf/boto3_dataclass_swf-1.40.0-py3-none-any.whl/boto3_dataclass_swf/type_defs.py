# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_swf import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActivityTaskCancelRequestedEventAttributes:
    boto3_raw_data: "type_defs.ActivityTaskCancelRequestedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    activityId = field("activityId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ActivityTaskCancelRequestedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTaskCancelRequestedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTaskCanceledEventAttributes:
    boto3_raw_data: "type_defs.ActivityTaskCanceledEventAttributesTypeDef" = (
        dataclasses.field()
    )

    scheduledEventId = field("scheduledEventId")
    startedEventId = field("startedEventId")
    details = field("details")
    latestCancelRequestedEventId = field("latestCancelRequestedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ActivityTaskCanceledEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTaskCanceledEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTaskCompletedEventAttributes:
    boto3_raw_data: "type_defs.ActivityTaskCompletedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    scheduledEventId = field("scheduledEventId")
    startedEventId = field("startedEventId")
    result = field("result")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ActivityTaskCompletedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTaskCompletedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTaskFailedEventAttributes:
    boto3_raw_data: "type_defs.ActivityTaskFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    scheduledEventId = field("scheduledEventId")
    startedEventId = field("startedEventId")
    reason = field("reason")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ActivityTaskFailedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTaskFailedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityType:
    boto3_raw_data: "type_defs.ActivityTypeTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivityTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskList:
    boto3_raw_data: "type_defs.TaskListTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskListTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTaskStartedEventAttributes:
    boto3_raw_data: "type_defs.ActivityTaskStartedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    scheduledEventId = field("scheduledEventId")
    identity = field("identity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ActivityTaskStartedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTaskStartedEventAttributesTypeDef"]
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
class ActivityTaskTimedOutEventAttributes:
    boto3_raw_data: "type_defs.ActivityTaskTimedOutEventAttributesTypeDef" = (
        dataclasses.field()
    )

    timeoutType = field("timeoutType")
    scheduledEventId = field("scheduledEventId")
    startedEventId = field("startedEventId")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ActivityTaskTimedOutEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTaskTimedOutEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecution:
    boto3_raw_data: "type_defs.WorkflowExecutionTypeDef" = dataclasses.field()

    workflowId = field("workflowId")
    runId = field("runId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelTimerDecisionAttributes:
    boto3_raw_data: "type_defs.CancelTimerDecisionAttributesTypeDef" = (
        dataclasses.field()
    )

    timerId = field("timerId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelTimerDecisionAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelTimerDecisionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelTimerFailedEventAttributes:
    boto3_raw_data: "type_defs.CancelTimerFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    timerId = field("timerId")
    cause = field("cause")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelTimerFailedEventAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelTimerFailedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelWorkflowExecutionDecisionAttributes:
    boto3_raw_data: "type_defs.CancelWorkflowExecutionDecisionAttributesTypeDef" = (
        dataclasses.field()
    )

    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelWorkflowExecutionDecisionAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelWorkflowExecutionDecisionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelWorkflowExecutionFailedEventAttributes:
    boto3_raw_data: "type_defs.CancelWorkflowExecutionFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    cause = field("cause")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelWorkflowExecutionFailedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelWorkflowExecutionFailedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowType:
    boto3_raw_data: "type_defs.WorkflowTypeTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkflowTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloseStatusFilter:
    boto3_raw_data: "type_defs.CloseStatusFilterTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CloseStatusFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloseStatusFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteWorkflowExecutionDecisionAttributes:
    boto3_raw_data: "type_defs.CompleteWorkflowExecutionDecisionAttributesTypeDef" = (
        dataclasses.field()
    )

    result = field("result")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompleteWorkflowExecutionDecisionAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompleteWorkflowExecutionDecisionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompleteWorkflowExecutionFailedEventAttributes:
    boto3_raw_data: (
        "type_defs.CompleteWorkflowExecutionFailedEventAttributesTypeDef"
    ) = dataclasses.field()

    cause = field("cause")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CompleteWorkflowExecutionFailedEventAttributesTypeDef"
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
                "type_defs.CompleteWorkflowExecutionFailedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinueAsNewWorkflowExecutionFailedEventAttributes:
    boto3_raw_data: (
        "type_defs.ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef"
    ) = dataclasses.field()

    cause = field("cause")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef"
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
                "type_defs.ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagFilter:
    boto3_raw_data: "type_defs.TagFilterTypeDef" = dataclasses.field()

    tag = field("tag")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionFilter:
    boto3_raw_data: "type_defs.WorkflowExecutionFilterTypeDef" = dataclasses.field()

    workflowId = field("workflowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowExecutionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowTypeFilter:
    boto3_raw_data: "type_defs.WorkflowTypeFilterTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowTypeFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowTypeFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecisionTaskStartedEventAttributes:
    boto3_raw_data: "type_defs.DecisionTaskStartedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    scheduledEventId = field("scheduledEventId")
    identity = field("identity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DecisionTaskStartedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecisionTaskStartedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecisionTaskTimedOutEventAttributes:
    boto3_raw_data: "type_defs.DecisionTaskTimedOutEventAttributesTypeDef" = (
        dataclasses.field()
    )

    timeoutType = field("timeoutType")
    scheduledEventId = field("scheduledEventId")
    startedEventId = field("startedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DecisionTaskTimedOutEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecisionTaskTimedOutEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailWorkflowExecutionDecisionAttributes:
    boto3_raw_data: "type_defs.FailWorkflowExecutionDecisionAttributesTypeDef" = (
        dataclasses.field()
    )

    reason = field("reason")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FailWorkflowExecutionDecisionAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailWorkflowExecutionDecisionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordMarkerDecisionAttributes:
    boto3_raw_data: "type_defs.RecordMarkerDecisionAttributesTypeDef" = (
        dataclasses.field()
    )

    markerName = field("markerName")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RecordMarkerDecisionAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordMarkerDecisionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestCancelActivityTaskDecisionAttributes:
    boto3_raw_data: "type_defs.RequestCancelActivityTaskDecisionAttributesTypeDef" = (
        dataclasses.field()
    )

    activityId = field("activityId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestCancelActivityTaskDecisionAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestCancelActivityTaskDecisionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestCancelExternalWorkflowExecutionDecisionAttributes:
    boto3_raw_data: (
        "type_defs.RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef"
    ) = dataclasses.field()

    workflowId = field("workflowId")
    runId = field("runId")
    control = field("control")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef"
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
                "type_defs.RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleLambdaFunctionDecisionAttributes:
    boto3_raw_data: "type_defs.ScheduleLambdaFunctionDecisionAttributesTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    control = field("control")
    input = field("input")
    startToCloseTimeout = field("startToCloseTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScheduleLambdaFunctionDecisionAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleLambdaFunctionDecisionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalExternalWorkflowExecutionDecisionAttributes:
    boto3_raw_data: (
        "type_defs.SignalExternalWorkflowExecutionDecisionAttributesTypeDef"
    ) = dataclasses.field()

    workflowId = field("workflowId")
    signalName = field("signalName")
    runId = field("runId")
    input = field("input")
    control = field("control")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SignalExternalWorkflowExecutionDecisionAttributesTypeDef"
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
                "type_defs.SignalExternalWorkflowExecutionDecisionAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTimerDecisionAttributes:
    boto3_raw_data: "type_defs.StartTimerDecisionAttributesTypeDef" = (
        dataclasses.field()
    )

    timerId = field("timerId")
    startToFireTimeout = field("startToFireTimeout")
    control = field("control")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTimerDecisionAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTimerDecisionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeprecateDomainInput:
    boto3_raw_data: "type_defs.DeprecateDomainInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeprecateDomainInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeprecateDomainInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainInput:
    boto3_raw_data: "type_defs.DescribeDomainInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainConfiguration:
    boto3_raw_data: "type_defs.DomainConfigurationTypeDef" = dataclasses.field()

    workflowExecutionRetentionPeriodInDays = field(
        "workflowExecutionRetentionPeriodInDays"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainInfo:
    boto3_raw_data: "type_defs.DomainInfoTypeDef" = dataclasses.field()

    name = field("name")
    status = field("status")
    description = field("description")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailWorkflowExecutionFailedEventAttributes:
    boto3_raw_data: "type_defs.FailWorkflowExecutionFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    cause = field("cause")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FailWorkflowExecutionFailedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailWorkflowExecutionFailedEventAttributesTypeDef"]
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
class LambdaFunctionCompletedEventAttributes:
    boto3_raw_data: "type_defs.LambdaFunctionCompletedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    scheduledEventId = field("scheduledEventId")
    startedEventId = field("startedEventId")
    result = field("result")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionCompletedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionCompletedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionFailedEventAttributes:
    boto3_raw_data: "type_defs.LambdaFunctionFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    scheduledEventId = field("scheduledEventId")
    startedEventId = field("startedEventId")
    reason = field("reason")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionFailedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionFailedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionScheduledEventAttributes:
    boto3_raw_data: "type_defs.LambdaFunctionScheduledEventAttributesTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    control = field("control")
    input = field("input")
    startToCloseTimeout = field("startToCloseTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionScheduledEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionScheduledEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionStartedEventAttributes:
    boto3_raw_data: "type_defs.LambdaFunctionStartedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    scheduledEventId = field("scheduledEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionStartedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionStartedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaFunctionTimedOutEventAttributes:
    boto3_raw_data: "type_defs.LambdaFunctionTimedOutEventAttributesTypeDef" = (
        dataclasses.field()
    )

    scheduledEventId = field("scheduledEventId")
    startedEventId = field("startedEventId")
    timeoutType = field("timeoutType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaFunctionTimedOutEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaFunctionTimedOutEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MarkerRecordedEventAttributes:
    boto3_raw_data: "type_defs.MarkerRecordedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    markerName = field("markerName")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MarkerRecordedEventAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MarkerRecordedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordMarkerFailedEventAttributes:
    boto3_raw_data: "type_defs.RecordMarkerFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    markerName = field("markerName")
    cause = field("cause")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RecordMarkerFailedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordMarkerFailedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestCancelActivityTaskFailedEventAttributes:
    boto3_raw_data: (
        "type_defs.RequestCancelActivityTaskFailedEventAttributesTypeDef"
    ) = dataclasses.field()

    activityId = field("activityId")
    cause = field("cause")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestCancelActivityTaskFailedEventAttributesTypeDef"
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
                "type_defs.RequestCancelActivityTaskFailedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestCancelExternalWorkflowExecutionFailedEventAttributes:
    boto3_raw_data: (
        "type_defs.RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef"
    ) = dataclasses.field()

    workflowId = field("workflowId")
    cause = field("cause")
    initiatedEventId = field("initiatedEventId")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    runId = field("runId")
    control = field("control")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef"
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
                "type_defs.RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestCancelExternalWorkflowExecutionInitiatedEventAttributes:
    boto3_raw_data: "type_defs.RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef" = (dataclasses.field())

    workflowId = field("workflowId")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    runId = field("runId")
    control = field("control")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef"
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
                "type_defs.RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleLambdaFunctionFailedEventAttributes:
    boto3_raw_data: "type_defs.ScheduleLambdaFunctionFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    cause = field("cause")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScheduleLambdaFunctionFailedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleLambdaFunctionFailedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalExternalWorkflowExecutionFailedEventAttributes:
    boto3_raw_data: (
        "type_defs.SignalExternalWorkflowExecutionFailedEventAttributesTypeDef"
    ) = dataclasses.field()

    workflowId = field("workflowId")
    cause = field("cause")
    initiatedEventId = field("initiatedEventId")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    runId = field("runId")
    control = field("control")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SignalExternalWorkflowExecutionFailedEventAttributesTypeDef"
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
                "type_defs.SignalExternalWorkflowExecutionFailedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalExternalWorkflowExecutionInitiatedEventAttributes:
    boto3_raw_data: (
        "type_defs.SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef"
    ) = dataclasses.field()

    workflowId = field("workflowId")
    signalName = field("signalName")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    runId = field("runId")
    input = field("input")
    control = field("control")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef"
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
                "type_defs.SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLambdaFunctionFailedEventAttributes:
    boto3_raw_data: "type_defs.StartLambdaFunctionFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    scheduledEventId = field("scheduledEventId")
    cause = field("cause")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartLambdaFunctionFailedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLambdaFunctionFailedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTimerFailedEventAttributes:
    boto3_raw_data: "type_defs.StartTimerFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    timerId = field("timerId")
    cause = field("cause")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartTimerFailedEventAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTimerFailedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimerCanceledEventAttributes:
    boto3_raw_data: "type_defs.TimerCanceledEventAttributesTypeDef" = (
        dataclasses.field()
    )

    timerId = field("timerId")
    startedEventId = field("startedEventId")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimerCanceledEventAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimerCanceledEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimerFiredEventAttributes:
    boto3_raw_data: "type_defs.TimerFiredEventAttributesTypeDef" = dataclasses.field()

    timerId = field("timerId")
    startedEventId = field("startedEventId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimerFiredEventAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimerFiredEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimerStartedEventAttributes:
    boto3_raw_data: "type_defs.TimerStartedEventAttributesTypeDef" = dataclasses.field()

    timerId = field("timerId")
    startToFireTimeout = field("startToFireTimeout")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    control = field("control")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimerStartedEventAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimerStartedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionCanceledEventAttributes:
    boto3_raw_data: "type_defs.WorkflowExecutionCanceledEventAttributesTypeDef" = (
        dataclasses.field()
    )

    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkflowExecutionCanceledEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionCanceledEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionCompletedEventAttributes:
    boto3_raw_data: "type_defs.WorkflowExecutionCompletedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    result = field("result")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkflowExecutionCompletedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionCompletedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionFailedEventAttributes:
    boto3_raw_data: "type_defs.WorkflowExecutionFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    reason = field("reason")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkflowExecutionFailedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionFailedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionTerminatedEventAttributes:
    boto3_raw_data: "type_defs.WorkflowExecutionTerminatedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    childPolicy = field("childPolicy")
    reason = field("reason")
    details = field("details")
    cause = field("cause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkflowExecutionTerminatedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionTerminatedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionTimedOutEventAttributes:
    boto3_raw_data: "type_defs.WorkflowExecutionTimedOutEventAttributesTypeDef" = (
        dataclasses.field()
    )

    timeoutType = field("timeoutType")
    childPolicy = field("childPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkflowExecutionTimedOutEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionTimedOutEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActivityTypesInput:
    boto3_raw_data: "type_defs.ListActivityTypesInputTypeDef" = dataclasses.field()

    domain = field("domain")
    registrationStatus = field("registrationStatus")
    name = field("name")
    nextPageToken = field("nextPageToken")
    maximumPageSize = field("maximumPageSize")
    reverseOrder = field("reverseOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActivityTypesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActivityTypesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsInput:
    boto3_raw_data: "type_defs.ListDomainsInputTypeDef" = dataclasses.field()

    registrationStatus = field("registrationStatus")
    nextPageToken = field("nextPageToken")
    maximumPageSize = field("maximumPageSize")
    reverseOrder = field("reverseOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListDomainsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTag:
    boto3_raw_data: "type_defs.ResourceTagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowTypesInput:
    boto3_raw_data: "type_defs.ListWorkflowTypesInputTypeDef" = dataclasses.field()

    domain = field("domain")
    registrationStatus = field("registrationStatus")
    name = field("name")
    nextPageToken = field("nextPageToken")
    maximumPageSize = field("maximumPageSize")
    reverseOrder = field("reverseOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowTypesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowTypesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordActivityTaskHeartbeatInput:
    boto3_raw_data: "type_defs.RecordActivityTaskHeartbeatInputTypeDef" = (
        dataclasses.field()
    )

    taskToken = field("taskToken")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RecordActivityTaskHeartbeatInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordActivityTaskHeartbeatInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestCancelWorkflowExecutionInput:
    boto3_raw_data: "type_defs.RequestCancelWorkflowExecutionInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    workflowId = field("workflowId")
    runId = field("runId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RequestCancelWorkflowExecutionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestCancelWorkflowExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RespondActivityTaskCanceledInput:
    boto3_raw_data: "type_defs.RespondActivityTaskCanceledInputTypeDef" = (
        dataclasses.field()
    )

    taskToken = field("taskToken")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RespondActivityTaskCanceledInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RespondActivityTaskCanceledInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RespondActivityTaskCompletedInput:
    boto3_raw_data: "type_defs.RespondActivityTaskCompletedInputTypeDef" = (
        dataclasses.field()
    )

    taskToken = field("taskToken")
    result = field("result")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RespondActivityTaskCompletedInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RespondActivityTaskCompletedInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RespondActivityTaskFailedInput:
    boto3_raw_data: "type_defs.RespondActivityTaskFailedInputTypeDef" = (
        dataclasses.field()
    )

    taskToken = field("taskToken")
    reason = field("reason")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RespondActivityTaskFailedInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RespondActivityTaskFailedInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalWorkflowExecutionInput:
    boto3_raw_data: "type_defs.SignalWorkflowExecutionInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    workflowId = field("workflowId")
    signalName = field("signalName")
    runId = field("runId")
    input = field("input")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignalWorkflowExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignalWorkflowExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateWorkflowExecutionInput:
    boto3_raw_data: "type_defs.TerminateWorkflowExecutionInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    workflowId = field("workflowId")
    runId = field("runId")
    reason = field("reason")
    details = field("details")
    childPolicy = field("childPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TerminateWorkflowExecutionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateWorkflowExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UndeprecateDomainInput:
    boto3_raw_data: "type_defs.UndeprecateDomainInputTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UndeprecateDomainInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UndeprecateDomainInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionOpenCounts:
    boto3_raw_data: "type_defs.WorkflowExecutionOpenCountsTypeDef" = dataclasses.field()

    openActivityTasks = field("openActivityTasks")
    openDecisionTasks = field("openDecisionTasks")
    openTimers = field("openTimers")
    openChildWorkflowExecutions = field("openChildWorkflowExecutions")
    openLambdaFunctions = field("openLambdaFunctions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowExecutionOpenCountsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionOpenCountsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTypeInfo:
    boto3_raw_data: "type_defs.ActivityTypeInfoTypeDef" = dataclasses.field()

    @cached_property
    def activityType(self):  # pragma: no cover
        return ActivityType.make_one(self.boto3_raw_data["activityType"])

    status = field("status")
    creationDate = field("creationDate")
    description = field("description")
    deprecationDate = field("deprecationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityTypeInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTypeInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteActivityTypeInput:
    boto3_raw_data: "type_defs.DeleteActivityTypeInputTypeDef" = dataclasses.field()

    domain = field("domain")

    @cached_property
    def activityType(self):  # pragma: no cover
        return ActivityType.make_one(self.boto3_raw_data["activityType"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteActivityTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteActivityTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeprecateActivityTypeInput:
    boto3_raw_data: "type_defs.DeprecateActivityTypeInputTypeDef" = dataclasses.field()

    domain = field("domain")

    @cached_property
    def activityType(self):  # pragma: no cover
        return ActivityType.make_one(self.boto3_raw_data["activityType"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeprecateActivityTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeprecateActivityTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeActivityTypeInput:
    boto3_raw_data: "type_defs.DescribeActivityTypeInputTypeDef" = dataclasses.field()

    domain = field("domain")

    @cached_property
    def activityType(self):  # pragma: no cover
        return ActivityType.make_one(self.boto3_raw_data["activityType"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeActivityTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeActivityTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleActivityTaskFailedEventAttributes:
    boto3_raw_data: "type_defs.ScheduleActivityTaskFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def activityType(self):  # pragma: no cover
        return ActivityType.make_one(self.boto3_raw_data["activityType"])

    activityId = field("activityId")
    cause = field("cause")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScheduleActivityTaskFailedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleActivityTaskFailedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UndeprecateActivityTypeInput:
    boto3_raw_data: "type_defs.UndeprecateActivityTypeInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def activityType(self):  # pragma: no cover
        return ActivityType.make_one(self.boto3_raw_data["activityType"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UndeprecateActivityTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UndeprecateActivityTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTaskScheduledEventAttributes:
    boto3_raw_data: "type_defs.ActivityTaskScheduledEventAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def activityType(self):  # pragma: no cover
        return ActivityType.make_one(self.boto3_raw_data["activityType"])

    activityId = field("activityId")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    input = field("input")
    control = field("control")
    scheduleToStartTimeout = field("scheduleToStartTimeout")
    scheduleToCloseTimeout = field("scheduleToCloseTimeout")
    startToCloseTimeout = field("startToCloseTimeout")
    taskPriority = field("taskPriority")
    heartbeatTimeout = field("heartbeatTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ActivityTaskScheduledEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTaskScheduledEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTypeConfiguration:
    boto3_raw_data: "type_defs.ActivityTypeConfigurationTypeDef" = dataclasses.field()

    defaultTaskStartToCloseTimeout = field("defaultTaskStartToCloseTimeout")
    defaultTaskHeartbeatTimeout = field("defaultTaskHeartbeatTimeout")

    @cached_property
    def defaultTaskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["defaultTaskList"])

    defaultTaskPriority = field("defaultTaskPriority")
    defaultTaskScheduleToStartTimeout = field("defaultTaskScheduleToStartTimeout")
    defaultTaskScheduleToCloseTimeout = field("defaultTaskScheduleToCloseTimeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivityTypeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTypeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinueAsNewWorkflowExecutionDecisionAttributes:
    boto3_raw_data: (
        "type_defs.ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef"
    ) = dataclasses.field()

    input = field("input")
    executionStartToCloseTimeout = field("executionStartToCloseTimeout")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    taskPriority = field("taskPriority")
    taskStartToCloseTimeout = field("taskStartToCloseTimeout")
    childPolicy = field("childPolicy")
    tagList = field("tagList")
    workflowTypeVersion = field("workflowTypeVersion")
    lambdaRole = field("lambdaRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef"
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
                "type_defs.ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountPendingActivityTasksInput:
    boto3_raw_data: "type_defs.CountPendingActivityTasksInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CountPendingActivityTasksInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CountPendingActivityTasksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountPendingDecisionTasksInput:
    boto3_raw_data: "type_defs.CountPendingDecisionTasksInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CountPendingDecisionTasksInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CountPendingDecisionTasksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecisionTaskCompletedEventAttributes:
    boto3_raw_data: "type_defs.DecisionTaskCompletedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    scheduledEventId = field("scheduledEventId")
    startedEventId = field("startedEventId")
    executionContext = field("executionContext")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    taskListScheduleToStartTimeout = field("taskListScheduleToStartTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DecisionTaskCompletedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecisionTaskCompletedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecisionTaskScheduledEventAttributes:
    boto3_raw_data: "type_defs.DecisionTaskScheduledEventAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    taskPriority = field("taskPriority")
    startToCloseTimeout = field("startToCloseTimeout")
    scheduleToStartTimeout = field("scheduleToStartTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DecisionTaskScheduledEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecisionTaskScheduledEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PollForActivityTaskInput:
    boto3_raw_data: "type_defs.PollForActivityTaskInputTypeDef" = dataclasses.field()

    domain = field("domain")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    identity = field("identity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PollForActivityTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PollForActivityTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PollForDecisionTaskInput:
    boto3_raw_data: "type_defs.PollForDecisionTaskInputTypeDef" = dataclasses.field()

    domain = field("domain")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    identity = field("identity")
    nextPageToken = field("nextPageToken")
    maximumPageSize = field("maximumPageSize")
    reverseOrder = field("reverseOrder")
    startAtPreviousStartedEvent = field("startAtPreviousStartedEvent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PollForDecisionTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PollForDecisionTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterActivityTypeInput:
    boto3_raw_data: "type_defs.RegisterActivityTypeInputTypeDef" = dataclasses.field()

    domain = field("domain")
    name = field("name")
    version = field("version")
    description = field("description")
    defaultTaskStartToCloseTimeout = field("defaultTaskStartToCloseTimeout")
    defaultTaskHeartbeatTimeout = field("defaultTaskHeartbeatTimeout")

    @cached_property
    def defaultTaskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["defaultTaskList"])

    defaultTaskPriority = field("defaultTaskPriority")
    defaultTaskScheduleToStartTimeout = field("defaultTaskScheduleToStartTimeout")
    defaultTaskScheduleToCloseTimeout = field("defaultTaskScheduleToCloseTimeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterActivityTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterActivityTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterWorkflowTypeInput:
    boto3_raw_data: "type_defs.RegisterWorkflowTypeInputTypeDef" = dataclasses.field()

    domain = field("domain")
    name = field("name")
    version = field("version")
    description = field("description")
    defaultTaskStartToCloseTimeout = field("defaultTaskStartToCloseTimeout")
    defaultExecutionStartToCloseTimeout = field("defaultExecutionStartToCloseTimeout")

    @cached_property
    def defaultTaskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["defaultTaskList"])

    defaultTaskPriority = field("defaultTaskPriority")
    defaultChildPolicy = field("defaultChildPolicy")
    defaultLambdaRole = field("defaultLambdaRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterWorkflowTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterWorkflowTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleActivityTaskDecisionAttributes:
    boto3_raw_data: "type_defs.ScheduleActivityTaskDecisionAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def activityType(self):  # pragma: no cover
        return ActivityType.make_one(self.boto3_raw_data["activityType"])

    activityId = field("activityId")
    control = field("control")
    input = field("input")
    scheduleToCloseTimeout = field("scheduleToCloseTimeout")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    taskPriority = field("taskPriority")
    scheduleToStartTimeout = field("scheduleToStartTimeout")
    startToCloseTimeout = field("startToCloseTimeout")
    heartbeatTimeout = field("heartbeatTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ScheduleActivityTaskDecisionAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleActivityTaskDecisionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionConfiguration:
    boto3_raw_data: "type_defs.WorkflowExecutionConfigurationTypeDef" = (
        dataclasses.field()
    )

    taskStartToCloseTimeout = field("taskStartToCloseTimeout")
    executionStartToCloseTimeout = field("executionStartToCloseTimeout")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    childPolicy = field("childPolicy")
    taskPriority = field("taskPriority")
    lambdaRole = field("lambdaRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WorkflowExecutionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowTypeConfiguration:
    boto3_raw_data: "type_defs.WorkflowTypeConfigurationTypeDef" = dataclasses.field()

    defaultTaskStartToCloseTimeout = field("defaultTaskStartToCloseTimeout")
    defaultExecutionStartToCloseTimeout = field("defaultExecutionStartToCloseTimeout")

    @cached_property
    def defaultTaskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["defaultTaskList"])

    defaultTaskPriority = field("defaultTaskPriority")
    defaultChildPolicy = field("defaultChildPolicy")
    defaultLambdaRole = field("defaultLambdaRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowTypeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowTypeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTaskStatus:
    boto3_raw_data: "type_defs.ActivityTaskStatusTypeDef" = dataclasses.field()

    cancelRequested = field("cancelRequested")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivityTaskStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTaskStatusTypeDef"]
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
class PendingTaskCount:
    boto3_raw_data: "type_defs.PendingTaskCountTypeDef" = dataclasses.field()

    count = field("count")
    truncated = field("truncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PendingTaskCountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingTaskCountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Run:
    boto3_raw_data: "type_defs.RunTypeDef" = dataclasses.field()

    runId = field("runId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RunTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RunTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionCount:
    boto3_raw_data: "type_defs.WorkflowExecutionCountTypeDef" = dataclasses.field()

    count = field("count")
    truncated = field("truncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowExecutionCountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionCountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTask:
    boto3_raw_data: "type_defs.ActivityTaskTypeDef" = dataclasses.field()

    taskToken = field("taskToken")
    activityId = field("activityId")
    startedEventId = field("startedEventId")

    @cached_property
    def workflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["workflowExecution"])

    @cached_property
    def activityType(self):  # pragma: no cover
        return ActivityType.make_one(self.boto3_raw_data["activityType"])

    input = field("input")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActivityTaskTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkflowExecutionInput:
    boto3_raw_data: "type_defs.DescribeWorkflowExecutionInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def execution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["execution"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeWorkflowExecutionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkflowExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalWorkflowExecutionCancelRequestedEventAttributes:
    boto3_raw_data: (
        "type_defs.ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef"
    ) = dataclasses.field()

    @cached_property
    def workflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["workflowExecution"])

    initiatedEventId = field("initiatedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef"
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
                "type_defs.ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalWorkflowExecutionSignaledEventAttributes:
    boto3_raw_data: (
        "type_defs.ExternalWorkflowExecutionSignaledEventAttributesTypeDef"
    ) = dataclasses.field()

    @cached_property
    def workflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["workflowExecution"])

    initiatedEventId = field("initiatedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExternalWorkflowExecutionSignaledEventAttributesTypeDef"
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
                "type_defs.ExternalWorkflowExecutionSignaledEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowExecutionHistoryInput:
    boto3_raw_data: "type_defs.GetWorkflowExecutionHistoryInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def execution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["execution"])

    nextPageToken = field("nextPageToken")
    maximumPageSize = field("maximumPageSize")
    reverseOrder = field("reverseOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetWorkflowExecutionHistoryInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowExecutionHistoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionCancelRequestedEventAttributes:
    boto3_raw_data: (
        "type_defs.WorkflowExecutionCancelRequestedEventAttributesTypeDef"
    ) = dataclasses.field()

    @cached_property
    def externalWorkflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(
            self.boto3_raw_data["externalWorkflowExecution"]
        )

    externalInitiatedEventId = field("externalInitiatedEventId")
    cause = field("cause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkflowExecutionCancelRequestedEventAttributesTypeDef"
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
                "type_defs.WorkflowExecutionCancelRequestedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionSignaledEventAttributes:
    boto3_raw_data: "type_defs.WorkflowExecutionSignaledEventAttributesTypeDef" = (
        dataclasses.field()
    )

    signalName = field("signalName")
    input = field("input")

    @cached_property
    def externalWorkflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(
            self.boto3_raw_data["externalWorkflowExecution"]
        )

    externalInitiatedEventId = field("externalInitiatedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkflowExecutionSignaledEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionSignaledEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChildWorkflowExecutionCanceledEventAttributes:
    boto3_raw_data: "type_defs.ChildWorkflowExecutionCanceledEventAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def workflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["workflowExecution"])

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    initiatedEventId = field("initiatedEventId")
    startedEventId = field("startedEventId")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChildWorkflowExecutionCanceledEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChildWorkflowExecutionCanceledEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChildWorkflowExecutionCompletedEventAttributes:
    boto3_raw_data: (
        "type_defs.ChildWorkflowExecutionCompletedEventAttributesTypeDef"
    ) = dataclasses.field()

    @cached_property
    def workflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["workflowExecution"])

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    initiatedEventId = field("initiatedEventId")
    startedEventId = field("startedEventId")
    result = field("result")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChildWorkflowExecutionCompletedEventAttributesTypeDef"
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
                "type_defs.ChildWorkflowExecutionCompletedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChildWorkflowExecutionFailedEventAttributes:
    boto3_raw_data: "type_defs.ChildWorkflowExecutionFailedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def workflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["workflowExecution"])

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    initiatedEventId = field("initiatedEventId")
    startedEventId = field("startedEventId")
    reason = field("reason")
    details = field("details")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChildWorkflowExecutionFailedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChildWorkflowExecutionFailedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChildWorkflowExecutionStartedEventAttributes:
    boto3_raw_data: "type_defs.ChildWorkflowExecutionStartedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def workflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["workflowExecution"])

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    initiatedEventId = field("initiatedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChildWorkflowExecutionStartedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChildWorkflowExecutionStartedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChildWorkflowExecutionTerminatedEventAttributes:
    boto3_raw_data: (
        "type_defs.ChildWorkflowExecutionTerminatedEventAttributesTypeDef"
    ) = dataclasses.field()

    @cached_property
    def workflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["workflowExecution"])

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    initiatedEventId = field("initiatedEventId")
    startedEventId = field("startedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChildWorkflowExecutionTerminatedEventAttributesTypeDef"
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
                "type_defs.ChildWorkflowExecutionTerminatedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChildWorkflowExecutionTimedOutEventAttributes:
    boto3_raw_data: "type_defs.ChildWorkflowExecutionTimedOutEventAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def workflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["workflowExecution"])

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    timeoutType = field("timeoutType")
    initiatedEventId = field("initiatedEventId")
    startedEventId = field("startedEventId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChildWorkflowExecutionTimedOutEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChildWorkflowExecutionTimedOutEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkflowTypeInput:
    boto3_raw_data: "type_defs.DeleteWorkflowTypeInputTypeDef" = dataclasses.field()

    domain = field("domain")

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkflowTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkflowTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeprecateWorkflowTypeInput:
    boto3_raw_data: "type_defs.DeprecateWorkflowTypeInputTypeDef" = dataclasses.field()

    domain = field("domain")

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeprecateWorkflowTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeprecateWorkflowTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeWorkflowTypeInput:
    boto3_raw_data: "type_defs.DescribeWorkflowTypeInputTypeDef" = dataclasses.field()

    domain = field("domain")

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeWorkflowTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeWorkflowTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChildWorkflowExecutionDecisionAttributes:
    boto3_raw_data: "type_defs.StartChildWorkflowExecutionDecisionAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    workflowId = field("workflowId")
    control = field("control")
    input = field("input")
    executionStartToCloseTimeout = field("executionStartToCloseTimeout")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    taskPriority = field("taskPriority")
    taskStartToCloseTimeout = field("taskStartToCloseTimeout")
    childPolicy = field("childPolicy")
    tagList = field("tagList")
    lambdaRole = field("lambdaRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartChildWorkflowExecutionDecisionAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartChildWorkflowExecutionDecisionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChildWorkflowExecutionFailedEventAttributes:
    boto3_raw_data: (
        "type_defs.StartChildWorkflowExecutionFailedEventAttributesTypeDef"
    ) = dataclasses.field()

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    cause = field("cause")
    workflowId = field("workflowId")
    initiatedEventId = field("initiatedEventId")
    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    control = field("control")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartChildWorkflowExecutionFailedEventAttributesTypeDef"
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
                "type_defs.StartChildWorkflowExecutionFailedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartChildWorkflowExecutionInitiatedEventAttributes:
    boto3_raw_data: (
        "type_defs.StartChildWorkflowExecutionInitiatedEventAttributesTypeDef"
    ) = dataclasses.field()

    workflowId = field("workflowId")

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    childPolicy = field("childPolicy")
    control = field("control")
    input = field("input")
    executionStartToCloseTimeout = field("executionStartToCloseTimeout")
    taskPriority = field("taskPriority")
    taskStartToCloseTimeout = field("taskStartToCloseTimeout")
    tagList = field("tagList")
    lambdaRole = field("lambdaRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartChildWorkflowExecutionInitiatedEventAttributesTypeDef"
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
                "type_defs.StartChildWorkflowExecutionInitiatedEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartWorkflowExecutionInput:
    boto3_raw_data: "type_defs.StartWorkflowExecutionInputTypeDef" = dataclasses.field()

    domain = field("domain")
    workflowId = field("workflowId")

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    taskPriority = field("taskPriority")
    input = field("input")
    executionStartToCloseTimeout = field("executionStartToCloseTimeout")
    tagList = field("tagList")
    taskStartToCloseTimeout = field("taskStartToCloseTimeout")
    childPolicy = field("childPolicy")
    lambdaRole = field("lambdaRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartWorkflowExecutionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartWorkflowExecutionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UndeprecateWorkflowTypeInput:
    boto3_raw_data: "type_defs.UndeprecateWorkflowTypeInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UndeprecateWorkflowTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UndeprecateWorkflowTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionContinuedAsNewEventAttributes:
    boto3_raw_data: (
        "type_defs.WorkflowExecutionContinuedAsNewEventAttributesTypeDef"
    ) = dataclasses.field()

    decisionTaskCompletedEventId = field("decisionTaskCompletedEventId")
    newExecutionRunId = field("newExecutionRunId")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    childPolicy = field("childPolicy")

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    input = field("input")
    executionStartToCloseTimeout = field("executionStartToCloseTimeout")
    taskPriority = field("taskPriority")
    taskStartToCloseTimeout = field("taskStartToCloseTimeout")
    tagList = field("tagList")
    lambdaRole = field("lambdaRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkflowExecutionContinuedAsNewEventAttributesTypeDef"
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
                "type_defs.WorkflowExecutionContinuedAsNewEventAttributesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionInfo:
    boto3_raw_data: "type_defs.WorkflowExecutionInfoTypeDef" = dataclasses.field()

    @cached_property
    def execution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["execution"])

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    startTimestamp = field("startTimestamp")
    executionStatus = field("executionStatus")
    closeTimestamp = field("closeTimestamp")
    closeStatus = field("closeStatus")

    @cached_property
    def parent(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["parent"])

    tagList = field("tagList")
    cancelRequested = field("cancelRequested")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowExecutionInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionStartedEventAttributes:
    boto3_raw_data: "type_defs.WorkflowExecutionStartedEventAttributesTypeDef" = (
        dataclasses.field()
    )

    childPolicy = field("childPolicy")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    input = field("input")
    executionStartToCloseTimeout = field("executionStartToCloseTimeout")
    taskStartToCloseTimeout = field("taskStartToCloseTimeout")
    taskPriority = field("taskPriority")
    tagList = field("tagList")
    continuedExecutionRunId = field("continuedExecutionRunId")

    @cached_property
    def parentWorkflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(
            self.boto3_raw_data["parentWorkflowExecution"]
        )

    parentInitiatedEventId = field("parentInitiatedEventId")
    lambdaRole = field("lambdaRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkflowExecutionStartedEventAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionStartedEventAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowTypeInfo:
    boto3_raw_data: "type_defs.WorkflowTypeInfoTypeDef" = dataclasses.field()

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    status = field("status")
    creationDate = field("creationDate")
    description = field("description")
    deprecationDate = field("deprecationDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowTypeInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowTypeInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainDetail:
    boto3_raw_data: "type_defs.DomainDetailTypeDef" = dataclasses.field()

    @cached_property
    def domainInfo(self):  # pragma: no cover
        return DomainInfo.make_one(self.boto3_raw_data["domainInfo"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return DomainConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainInfos:
    boto3_raw_data: "type_defs.DomainInfosTypeDef" = dataclasses.field()

    @cached_property
    def domainInfos(self):  # pragma: no cover
        return DomainInfo.make_many(self.boto3_raw_data["domainInfos"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainInfosTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainInfosTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionTimeFilter:
    boto3_raw_data: "type_defs.ExecutionTimeFilterTypeDef" = dataclasses.field()

    oldestDate = field("oldestDate")
    latestDate = field("latestDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecutionTimeFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionTimeFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowExecutionHistoryInputPaginate:
    boto3_raw_data: "type_defs.GetWorkflowExecutionHistoryInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def execution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["execution"])

    reverseOrder = field("reverseOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWorkflowExecutionHistoryInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowExecutionHistoryInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActivityTypesInputPaginate:
    boto3_raw_data: "type_defs.ListActivityTypesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    registrationStatus = field("registrationStatus")
    name = field("name")
    reverseOrder = field("reverseOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListActivityTypesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActivityTypesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsInputPaginate:
    boto3_raw_data: "type_defs.ListDomainsInputPaginateTypeDef" = dataclasses.field()

    registrationStatus = field("registrationStatus")
    reverseOrder = field("reverseOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowTypesInputPaginate:
    boto3_raw_data: "type_defs.ListWorkflowTypesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")
    registrationStatus = field("registrationStatus")
    name = field("name")
    reverseOrder = field("reverseOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkflowTypesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowTypesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PollForDecisionTaskInputPaginate:
    boto3_raw_data: "type_defs.PollForDecisionTaskInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    identity = field("identity")
    reverseOrder = field("reverseOrder")
    startAtPreviousStartedEvent = field("startAtPreviousStartedEvent")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PollForDecisionTaskInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PollForDecisionTaskInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterDomainInput:
    boto3_raw_data: "type_defs.RegisterDomainInputTypeDef" = dataclasses.field()

    name = field("name")
    workflowExecutionRetentionPeriodInDays = field(
        "workflowExecutionRetentionPeriodInDays"
    )
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterDomainInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterDomainInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTypeInfos:
    boto3_raw_data: "type_defs.ActivityTypeInfosTypeDef" = dataclasses.field()

    @cached_property
    def typeInfos(self):  # pragma: no cover
        return ActivityTypeInfo.make_many(self.boto3_raw_data["typeInfos"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivityTypeInfosTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTypeInfosTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivityTypeDetail:
    boto3_raw_data: "type_defs.ActivityTypeDetailTypeDef" = dataclasses.field()

    @cached_property
    def typeInfo(self):  # pragma: no cover
        return ActivityTypeInfo.make_one(self.boto3_raw_data["typeInfo"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return ActivityTypeConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivityTypeDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivityTypeDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Decision:
    boto3_raw_data: "type_defs.DecisionTypeDef" = dataclasses.field()

    decisionType = field("decisionType")

    @cached_property
    def scheduleActivityTaskDecisionAttributes(self):  # pragma: no cover
        return ScheduleActivityTaskDecisionAttributes.make_one(
            self.boto3_raw_data["scheduleActivityTaskDecisionAttributes"]
        )

    @cached_property
    def requestCancelActivityTaskDecisionAttributes(self):  # pragma: no cover
        return RequestCancelActivityTaskDecisionAttributes.make_one(
            self.boto3_raw_data["requestCancelActivityTaskDecisionAttributes"]
        )

    @cached_property
    def completeWorkflowExecutionDecisionAttributes(self):  # pragma: no cover
        return CompleteWorkflowExecutionDecisionAttributes.make_one(
            self.boto3_raw_data["completeWorkflowExecutionDecisionAttributes"]
        )

    @cached_property
    def failWorkflowExecutionDecisionAttributes(self):  # pragma: no cover
        return FailWorkflowExecutionDecisionAttributes.make_one(
            self.boto3_raw_data["failWorkflowExecutionDecisionAttributes"]
        )

    @cached_property
    def cancelWorkflowExecutionDecisionAttributes(self):  # pragma: no cover
        return CancelWorkflowExecutionDecisionAttributes.make_one(
            self.boto3_raw_data["cancelWorkflowExecutionDecisionAttributes"]
        )

    @cached_property
    def continueAsNewWorkflowExecutionDecisionAttributes(self):  # pragma: no cover
        return ContinueAsNewWorkflowExecutionDecisionAttributes.make_one(
            self.boto3_raw_data["continueAsNewWorkflowExecutionDecisionAttributes"]
        )

    @cached_property
    def recordMarkerDecisionAttributes(self):  # pragma: no cover
        return RecordMarkerDecisionAttributes.make_one(
            self.boto3_raw_data["recordMarkerDecisionAttributes"]
        )

    @cached_property
    def startTimerDecisionAttributes(self):  # pragma: no cover
        return StartTimerDecisionAttributes.make_one(
            self.boto3_raw_data["startTimerDecisionAttributes"]
        )

    @cached_property
    def cancelTimerDecisionAttributes(self):  # pragma: no cover
        return CancelTimerDecisionAttributes.make_one(
            self.boto3_raw_data["cancelTimerDecisionAttributes"]
        )

    @cached_property
    def signalExternalWorkflowExecutionDecisionAttributes(self):  # pragma: no cover
        return SignalExternalWorkflowExecutionDecisionAttributes.make_one(
            self.boto3_raw_data["signalExternalWorkflowExecutionDecisionAttributes"]
        )

    @cached_property
    def requestCancelExternalWorkflowExecutionDecisionAttributes(
        self,
    ):  # pragma: no cover
        return RequestCancelExternalWorkflowExecutionDecisionAttributes.make_one(
            self.boto3_raw_data[
                "requestCancelExternalWorkflowExecutionDecisionAttributes"
            ]
        )

    @cached_property
    def startChildWorkflowExecutionDecisionAttributes(self):  # pragma: no cover
        return StartChildWorkflowExecutionDecisionAttributes.make_one(
            self.boto3_raw_data["startChildWorkflowExecutionDecisionAttributes"]
        )

    @cached_property
    def scheduleLambdaFunctionDecisionAttributes(self):  # pragma: no cover
        return ScheduleLambdaFunctionDecisionAttributes.make_one(
            self.boto3_raw_data["scheduleLambdaFunctionDecisionAttributes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DecisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DecisionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionDetail:
    boto3_raw_data: "type_defs.WorkflowExecutionDetailTypeDef" = dataclasses.field()

    @cached_property
    def executionInfo(self):  # pragma: no cover
        return WorkflowExecutionInfo.make_one(self.boto3_raw_data["executionInfo"])

    @cached_property
    def executionConfiguration(self):  # pragma: no cover
        return WorkflowExecutionConfiguration.make_one(
            self.boto3_raw_data["executionConfiguration"]
        )

    @cached_property
    def openCounts(self):  # pragma: no cover
        return WorkflowExecutionOpenCounts.make_one(self.boto3_raw_data["openCounts"])

    latestActivityTaskTimestamp = field("latestActivityTaskTimestamp")
    latestExecutionContext = field("latestExecutionContext")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowExecutionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowExecutionInfos:
    boto3_raw_data: "type_defs.WorkflowExecutionInfosTypeDef" = dataclasses.field()

    @cached_property
    def executionInfos(self):  # pragma: no cover
        return WorkflowExecutionInfo.make_many(self.boto3_raw_data["executionInfos"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowExecutionInfosTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowExecutionInfosTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HistoryEvent:
    boto3_raw_data: "type_defs.HistoryEventTypeDef" = dataclasses.field()

    eventTimestamp = field("eventTimestamp")
    eventType = field("eventType")
    eventId = field("eventId")

    @cached_property
    def workflowExecutionStartedEventAttributes(self):  # pragma: no cover
        return WorkflowExecutionStartedEventAttributes.make_one(
            self.boto3_raw_data["workflowExecutionStartedEventAttributes"]
        )

    @cached_property
    def workflowExecutionCompletedEventAttributes(self):  # pragma: no cover
        return WorkflowExecutionCompletedEventAttributes.make_one(
            self.boto3_raw_data["workflowExecutionCompletedEventAttributes"]
        )

    @cached_property
    def completeWorkflowExecutionFailedEventAttributes(self):  # pragma: no cover
        return CompleteWorkflowExecutionFailedEventAttributes.make_one(
            self.boto3_raw_data["completeWorkflowExecutionFailedEventAttributes"]
        )

    @cached_property
    def workflowExecutionFailedEventAttributes(self):  # pragma: no cover
        return WorkflowExecutionFailedEventAttributes.make_one(
            self.boto3_raw_data["workflowExecutionFailedEventAttributes"]
        )

    @cached_property
    def failWorkflowExecutionFailedEventAttributes(self):  # pragma: no cover
        return FailWorkflowExecutionFailedEventAttributes.make_one(
            self.boto3_raw_data["failWorkflowExecutionFailedEventAttributes"]
        )

    @cached_property
    def workflowExecutionTimedOutEventAttributes(self):  # pragma: no cover
        return WorkflowExecutionTimedOutEventAttributes.make_one(
            self.boto3_raw_data["workflowExecutionTimedOutEventAttributes"]
        )

    @cached_property
    def workflowExecutionCanceledEventAttributes(self):  # pragma: no cover
        return WorkflowExecutionCanceledEventAttributes.make_one(
            self.boto3_raw_data["workflowExecutionCanceledEventAttributes"]
        )

    @cached_property
    def cancelWorkflowExecutionFailedEventAttributes(self):  # pragma: no cover
        return CancelWorkflowExecutionFailedEventAttributes.make_one(
            self.boto3_raw_data["cancelWorkflowExecutionFailedEventAttributes"]
        )

    @cached_property
    def workflowExecutionContinuedAsNewEventAttributes(self):  # pragma: no cover
        return WorkflowExecutionContinuedAsNewEventAttributes.make_one(
            self.boto3_raw_data["workflowExecutionContinuedAsNewEventAttributes"]
        )

    @cached_property
    def continueAsNewWorkflowExecutionFailedEventAttributes(self):  # pragma: no cover
        return ContinueAsNewWorkflowExecutionFailedEventAttributes.make_one(
            self.boto3_raw_data["continueAsNewWorkflowExecutionFailedEventAttributes"]
        )

    @cached_property
    def workflowExecutionTerminatedEventAttributes(self):  # pragma: no cover
        return WorkflowExecutionTerminatedEventAttributes.make_one(
            self.boto3_raw_data["workflowExecutionTerminatedEventAttributes"]
        )

    @cached_property
    def workflowExecutionCancelRequestedEventAttributes(self):  # pragma: no cover
        return WorkflowExecutionCancelRequestedEventAttributes.make_one(
            self.boto3_raw_data["workflowExecutionCancelRequestedEventAttributes"]
        )

    @cached_property
    def decisionTaskScheduledEventAttributes(self):  # pragma: no cover
        return DecisionTaskScheduledEventAttributes.make_one(
            self.boto3_raw_data["decisionTaskScheduledEventAttributes"]
        )

    @cached_property
    def decisionTaskStartedEventAttributes(self):  # pragma: no cover
        return DecisionTaskStartedEventAttributes.make_one(
            self.boto3_raw_data["decisionTaskStartedEventAttributes"]
        )

    @cached_property
    def decisionTaskCompletedEventAttributes(self):  # pragma: no cover
        return DecisionTaskCompletedEventAttributes.make_one(
            self.boto3_raw_data["decisionTaskCompletedEventAttributes"]
        )

    @cached_property
    def decisionTaskTimedOutEventAttributes(self):  # pragma: no cover
        return DecisionTaskTimedOutEventAttributes.make_one(
            self.boto3_raw_data["decisionTaskTimedOutEventAttributes"]
        )

    @cached_property
    def activityTaskScheduledEventAttributes(self):  # pragma: no cover
        return ActivityTaskScheduledEventAttributes.make_one(
            self.boto3_raw_data["activityTaskScheduledEventAttributes"]
        )

    @cached_property
    def activityTaskStartedEventAttributes(self):  # pragma: no cover
        return ActivityTaskStartedEventAttributes.make_one(
            self.boto3_raw_data["activityTaskStartedEventAttributes"]
        )

    @cached_property
    def activityTaskCompletedEventAttributes(self):  # pragma: no cover
        return ActivityTaskCompletedEventAttributes.make_one(
            self.boto3_raw_data["activityTaskCompletedEventAttributes"]
        )

    @cached_property
    def activityTaskFailedEventAttributes(self):  # pragma: no cover
        return ActivityTaskFailedEventAttributes.make_one(
            self.boto3_raw_data["activityTaskFailedEventAttributes"]
        )

    @cached_property
    def activityTaskTimedOutEventAttributes(self):  # pragma: no cover
        return ActivityTaskTimedOutEventAttributes.make_one(
            self.boto3_raw_data["activityTaskTimedOutEventAttributes"]
        )

    @cached_property
    def activityTaskCanceledEventAttributes(self):  # pragma: no cover
        return ActivityTaskCanceledEventAttributes.make_one(
            self.boto3_raw_data["activityTaskCanceledEventAttributes"]
        )

    @cached_property
    def activityTaskCancelRequestedEventAttributes(self):  # pragma: no cover
        return ActivityTaskCancelRequestedEventAttributes.make_one(
            self.boto3_raw_data["activityTaskCancelRequestedEventAttributes"]
        )

    @cached_property
    def workflowExecutionSignaledEventAttributes(self):  # pragma: no cover
        return WorkflowExecutionSignaledEventAttributes.make_one(
            self.boto3_raw_data["workflowExecutionSignaledEventAttributes"]
        )

    @cached_property
    def markerRecordedEventAttributes(self):  # pragma: no cover
        return MarkerRecordedEventAttributes.make_one(
            self.boto3_raw_data["markerRecordedEventAttributes"]
        )

    @cached_property
    def recordMarkerFailedEventAttributes(self):  # pragma: no cover
        return RecordMarkerFailedEventAttributes.make_one(
            self.boto3_raw_data["recordMarkerFailedEventAttributes"]
        )

    @cached_property
    def timerStartedEventAttributes(self):  # pragma: no cover
        return TimerStartedEventAttributes.make_one(
            self.boto3_raw_data["timerStartedEventAttributes"]
        )

    @cached_property
    def timerFiredEventAttributes(self):  # pragma: no cover
        return TimerFiredEventAttributes.make_one(
            self.boto3_raw_data["timerFiredEventAttributes"]
        )

    @cached_property
    def timerCanceledEventAttributes(self):  # pragma: no cover
        return TimerCanceledEventAttributes.make_one(
            self.boto3_raw_data["timerCanceledEventAttributes"]
        )

    @cached_property
    def startChildWorkflowExecutionInitiatedEventAttributes(self):  # pragma: no cover
        return StartChildWorkflowExecutionInitiatedEventAttributes.make_one(
            self.boto3_raw_data["startChildWorkflowExecutionInitiatedEventAttributes"]
        )

    @cached_property
    def childWorkflowExecutionStartedEventAttributes(self):  # pragma: no cover
        return ChildWorkflowExecutionStartedEventAttributes.make_one(
            self.boto3_raw_data["childWorkflowExecutionStartedEventAttributes"]
        )

    @cached_property
    def childWorkflowExecutionCompletedEventAttributes(self):  # pragma: no cover
        return ChildWorkflowExecutionCompletedEventAttributes.make_one(
            self.boto3_raw_data["childWorkflowExecutionCompletedEventAttributes"]
        )

    @cached_property
    def childWorkflowExecutionFailedEventAttributes(self):  # pragma: no cover
        return ChildWorkflowExecutionFailedEventAttributes.make_one(
            self.boto3_raw_data["childWorkflowExecutionFailedEventAttributes"]
        )

    @cached_property
    def childWorkflowExecutionTimedOutEventAttributes(self):  # pragma: no cover
        return ChildWorkflowExecutionTimedOutEventAttributes.make_one(
            self.boto3_raw_data["childWorkflowExecutionTimedOutEventAttributes"]
        )

    @cached_property
    def childWorkflowExecutionCanceledEventAttributes(self):  # pragma: no cover
        return ChildWorkflowExecutionCanceledEventAttributes.make_one(
            self.boto3_raw_data["childWorkflowExecutionCanceledEventAttributes"]
        )

    @cached_property
    def childWorkflowExecutionTerminatedEventAttributes(self):  # pragma: no cover
        return ChildWorkflowExecutionTerminatedEventAttributes.make_one(
            self.boto3_raw_data["childWorkflowExecutionTerminatedEventAttributes"]
        )

    @cached_property
    def signalExternalWorkflowExecutionInitiatedEventAttributes(
        self,
    ):  # pragma: no cover
        return SignalExternalWorkflowExecutionInitiatedEventAttributes.make_one(
            self.boto3_raw_data[
                "signalExternalWorkflowExecutionInitiatedEventAttributes"
            ]
        )

    @cached_property
    def externalWorkflowExecutionSignaledEventAttributes(self):  # pragma: no cover
        return ExternalWorkflowExecutionSignaledEventAttributes.make_one(
            self.boto3_raw_data["externalWorkflowExecutionSignaledEventAttributes"]
        )

    @cached_property
    def signalExternalWorkflowExecutionFailedEventAttributes(self):  # pragma: no cover
        return SignalExternalWorkflowExecutionFailedEventAttributes.make_one(
            self.boto3_raw_data["signalExternalWorkflowExecutionFailedEventAttributes"]
        )

    @cached_property
    def externalWorkflowExecutionCancelRequestedEventAttributes(
        self,
    ):  # pragma: no cover
        return ExternalWorkflowExecutionCancelRequestedEventAttributes.make_one(
            self.boto3_raw_data[
                "externalWorkflowExecutionCancelRequestedEventAttributes"
            ]
        )

    @cached_property
    def requestCancelExternalWorkflowExecutionInitiatedEventAttributes(
        self,
    ):  # pragma: no cover
        return RequestCancelExternalWorkflowExecutionInitiatedEventAttributes.make_one(
            self.boto3_raw_data[
                "requestCancelExternalWorkflowExecutionInitiatedEventAttributes"
            ]
        )

    @cached_property
    def requestCancelExternalWorkflowExecutionFailedEventAttributes(
        self,
    ):  # pragma: no cover
        return RequestCancelExternalWorkflowExecutionFailedEventAttributes.make_one(
            self.boto3_raw_data[
                "requestCancelExternalWorkflowExecutionFailedEventAttributes"
            ]
        )

    @cached_property
    def scheduleActivityTaskFailedEventAttributes(self):  # pragma: no cover
        return ScheduleActivityTaskFailedEventAttributes.make_one(
            self.boto3_raw_data["scheduleActivityTaskFailedEventAttributes"]
        )

    @cached_property
    def requestCancelActivityTaskFailedEventAttributes(self):  # pragma: no cover
        return RequestCancelActivityTaskFailedEventAttributes.make_one(
            self.boto3_raw_data["requestCancelActivityTaskFailedEventAttributes"]
        )

    @cached_property
    def startTimerFailedEventAttributes(self):  # pragma: no cover
        return StartTimerFailedEventAttributes.make_one(
            self.boto3_raw_data["startTimerFailedEventAttributes"]
        )

    @cached_property
    def cancelTimerFailedEventAttributes(self):  # pragma: no cover
        return CancelTimerFailedEventAttributes.make_one(
            self.boto3_raw_data["cancelTimerFailedEventAttributes"]
        )

    @cached_property
    def startChildWorkflowExecutionFailedEventAttributes(self):  # pragma: no cover
        return StartChildWorkflowExecutionFailedEventAttributes.make_one(
            self.boto3_raw_data["startChildWorkflowExecutionFailedEventAttributes"]
        )

    @cached_property
    def lambdaFunctionScheduledEventAttributes(self):  # pragma: no cover
        return LambdaFunctionScheduledEventAttributes.make_one(
            self.boto3_raw_data["lambdaFunctionScheduledEventAttributes"]
        )

    @cached_property
    def lambdaFunctionStartedEventAttributes(self):  # pragma: no cover
        return LambdaFunctionStartedEventAttributes.make_one(
            self.boto3_raw_data["lambdaFunctionStartedEventAttributes"]
        )

    @cached_property
    def lambdaFunctionCompletedEventAttributes(self):  # pragma: no cover
        return LambdaFunctionCompletedEventAttributes.make_one(
            self.boto3_raw_data["lambdaFunctionCompletedEventAttributes"]
        )

    @cached_property
    def lambdaFunctionFailedEventAttributes(self):  # pragma: no cover
        return LambdaFunctionFailedEventAttributes.make_one(
            self.boto3_raw_data["lambdaFunctionFailedEventAttributes"]
        )

    @cached_property
    def lambdaFunctionTimedOutEventAttributes(self):  # pragma: no cover
        return LambdaFunctionTimedOutEventAttributes.make_one(
            self.boto3_raw_data["lambdaFunctionTimedOutEventAttributes"]
        )

    @cached_property
    def scheduleLambdaFunctionFailedEventAttributes(self):  # pragma: no cover
        return ScheduleLambdaFunctionFailedEventAttributes.make_one(
            self.boto3_raw_data["scheduleLambdaFunctionFailedEventAttributes"]
        )

    @cached_property
    def startLambdaFunctionFailedEventAttributes(self):  # pragma: no cover
        return StartLambdaFunctionFailedEventAttributes.make_one(
            self.boto3_raw_data["startLambdaFunctionFailedEventAttributes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HistoryEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HistoryEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowTypeDetail:
    boto3_raw_data: "type_defs.WorkflowTypeDetailTypeDef" = dataclasses.field()

    @cached_property
    def typeInfo(self):  # pragma: no cover
        return WorkflowTypeInfo.make_one(self.boto3_raw_data["typeInfo"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return WorkflowTypeConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowTypeDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowTypeDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowTypeInfos:
    boto3_raw_data: "type_defs.WorkflowTypeInfosTypeDef" = dataclasses.field()

    @cached_property
    def typeInfos(self):  # pragma: no cover
        return WorkflowTypeInfo.make_many(self.boto3_raw_data["typeInfos"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowTypeInfosTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowTypeInfosTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountClosedWorkflowExecutionsInput:
    boto3_raw_data: "type_defs.CountClosedWorkflowExecutionsInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def startTimeFilter(self):  # pragma: no cover
        return ExecutionTimeFilter.make_one(self.boto3_raw_data["startTimeFilter"])

    @cached_property
    def closeTimeFilter(self):  # pragma: no cover
        return ExecutionTimeFilter.make_one(self.boto3_raw_data["closeTimeFilter"])

    @cached_property
    def executionFilter(self):  # pragma: no cover
        return WorkflowExecutionFilter.make_one(self.boto3_raw_data["executionFilter"])

    @cached_property
    def typeFilter(self):  # pragma: no cover
        return WorkflowTypeFilter.make_one(self.boto3_raw_data["typeFilter"])

    @cached_property
    def tagFilter(self):  # pragma: no cover
        return TagFilter.make_one(self.boto3_raw_data["tagFilter"])

    @cached_property
    def closeStatusFilter(self):  # pragma: no cover
        return CloseStatusFilter.make_one(self.boto3_raw_data["closeStatusFilter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CountClosedWorkflowExecutionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CountClosedWorkflowExecutionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CountOpenWorkflowExecutionsInput:
    boto3_raw_data: "type_defs.CountOpenWorkflowExecutionsInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def startTimeFilter(self):  # pragma: no cover
        return ExecutionTimeFilter.make_one(self.boto3_raw_data["startTimeFilter"])

    @cached_property
    def typeFilter(self):  # pragma: no cover
        return WorkflowTypeFilter.make_one(self.boto3_raw_data["typeFilter"])

    @cached_property
    def tagFilter(self):  # pragma: no cover
        return TagFilter.make_one(self.boto3_raw_data["tagFilter"])

    @cached_property
    def executionFilter(self):  # pragma: no cover
        return WorkflowExecutionFilter.make_one(self.boto3_raw_data["executionFilter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CountOpenWorkflowExecutionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CountOpenWorkflowExecutionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClosedWorkflowExecutionsInputPaginate:
    boto3_raw_data: "type_defs.ListClosedWorkflowExecutionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def startTimeFilter(self):  # pragma: no cover
        return ExecutionTimeFilter.make_one(self.boto3_raw_data["startTimeFilter"])

    @cached_property
    def closeTimeFilter(self):  # pragma: no cover
        return ExecutionTimeFilter.make_one(self.boto3_raw_data["closeTimeFilter"])

    @cached_property
    def executionFilter(self):  # pragma: no cover
        return WorkflowExecutionFilter.make_one(self.boto3_raw_data["executionFilter"])

    @cached_property
    def closeStatusFilter(self):  # pragma: no cover
        return CloseStatusFilter.make_one(self.boto3_raw_data["closeStatusFilter"])

    @cached_property
    def typeFilter(self):  # pragma: no cover
        return WorkflowTypeFilter.make_one(self.boto3_raw_data["typeFilter"])

    @cached_property
    def tagFilter(self):  # pragma: no cover
        return TagFilter.make_one(self.boto3_raw_data["tagFilter"])

    reverseOrder = field("reverseOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListClosedWorkflowExecutionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClosedWorkflowExecutionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClosedWorkflowExecutionsInput:
    boto3_raw_data: "type_defs.ListClosedWorkflowExecutionsInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def startTimeFilter(self):  # pragma: no cover
        return ExecutionTimeFilter.make_one(self.boto3_raw_data["startTimeFilter"])

    @cached_property
    def closeTimeFilter(self):  # pragma: no cover
        return ExecutionTimeFilter.make_one(self.boto3_raw_data["closeTimeFilter"])

    @cached_property
    def executionFilter(self):  # pragma: no cover
        return WorkflowExecutionFilter.make_one(self.boto3_raw_data["executionFilter"])

    @cached_property
    def closeStatusFilter(self):  # pragma: no cover
        return CloseStatusFilter.make_one(self.boto3_raw_data["closeStatusFilter"])

    @cached_property
    def typeFilter(self):  # pragma: no cover
        return WorkflowTypeFilter.make_one(self.boto3_raw_data["typeFilter"])

    @cached_property
    def tagFilter(self):  # pragma: no cover
        return TagFilter.make_one(self.boto3_raw_data["tagFilter"])

    nextPageToken = field("nextPageToken")
    maximumPageSize = field("maximumPageSize")
    reverseOrder = field("reverseOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListClosedWorkflowExecutionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClosedWorkflowExecutionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpenWorkflowExecutionsInputPaginate:
    boto3_raw_data: "type_defs.ListOpenWorkflowExecutionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def startTimeFilter(self):  # pragma: no cover
        return ExecutionTimeFilter.make_one(self.boto3_raw_data["startTimeFilter"])

    @cached_property
    def typeFilter(self):  # pragma: no cover
        return WorkflowTypeFilter.make_one(self.boto3_raw_data["typeFilter"])

    @cached_property
    def tagFilter(self):  # pragma: no cover
        return TagFilter.make_one(self.boto3_raw_data["tagFilter"])

    reverseOrder = field("reverseOrder")

    @cached_property
    def executionFilter(self):  # pragma: no cover
        return WorkflowExecutionFilter.make_one(self.boto3_raw_data["executionFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOpenWorkflowExecutionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpenWorkflowExecutionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOpenWorkflowExecutionsInput:
    boto3_raw_data: "type_defs.ListOpenWorkflowExecutionsInputTypeDef" = (
        dataclasses.field()
    )

    domain = field("domain")

    @cached_property
    def startTimeFilter(self):  # pragma: no cover
        return ExecutionTimeFilter.make_one(self.boto3_raw_data["startTimeFilter"])

    @cached_property
    def typeFilter(self):  # pragma: no cover
        return WorkflowTypeFilter.make_one(self.boto3_raw_data["typeFilter"])

    @cached_property
    def tagFilter(self):  # pragma: no cover
        return TagFilter.make_one(self.boto3_raw_data["tagFilter"])

    nextPageToken = field("nextPageToken")
    maximumPageSize = field("maximumPageSize")
    reverseOrder = field("reverseOrder")

    @cached_property
    def executionFilter(self):  # pragma: no cover
        return WorkflowExecutionFilter.make_one(self.boto3_raw_data["executionFilter"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOpenWorkflowExecutionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOpenWorkflowExecutionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RespondDecisionTaskCompletedInput:
    boto3_raw_data: "type_defs.RespondDecisionTaskCompletedInputTypeDef" = (
        dataclasses.field()
    )

    taskToken = field("taskToken")

    @cached_property
    def decisions(self):  # pragma: no cover
        return Decision.make_many(self.boto3_raw_data["decisions"])

    executionContext = field("executionContext")

    @cached_property
    def taskList(self):  # pragma: no cover
        return TaskList.make_one(self.boto3_raw_data["taskList"])

    taskListScheduleToStartTimeout = field("taskListScheduleToStartTimeout")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RespondDecisionTaskCompletedInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RespondDecisionTaskCompletedInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecisionTask:
    boto3_raw_data: "type_defs.DecisionTaskTypeDef" = dataclasses.field()

    taskToken = field("taskToken")
    startedEventId = field("startedEventId")

    @cached_property
    def workflowExecution(self):  # pragma: no cover
        return WorkflowExecution.make_one(self.boto3_raw_data["workflowExecution"])

    @cached_property
    def workflowType(self):  # pragma: no cover
        return WorkflowType.make_one(self.boto3_raw_data["workflowType"])

    @cached_property
    def events(self):  # pragma: no cover
        return HistoryEvent.make_many(self.boto3_raw_data["events"])

    nextPageToken = field("nextPageToken")
    previousStartedEventId = field("previousStartedEventId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DecisionTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DecisionTaskTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class History:
    boto3_raw_data: "type_defs.HistoryTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return HistoryEvent.make_many(self.boto3_raw_data["events"])

    nextPageToken = field("nextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HistoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HistoryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
