# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_networkflowmonitor import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class MonitorLocalResource:
    boto3_raw_data: "type_defs.MonitorLocalResourceTypeDef" = dataclasses.field()

    type = field("type")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitorLocalResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitorLocalResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitorRemoteResource:
    boto3_raw_data: "type_defs.MonitorRemoteResourceTypeDef" = dataclasses.field()

    type = field("type")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitorRemoteResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitorRemoteResourceTypeDef"]
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
class DeleteMonitorInput:
    boto3_raw_data: "type_defs.DeleteMonitorInputTypeDef" = dataclasses.field()

    monitorName = field("monitorName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMonitorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMonitorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteScopeInput:
    boto3_raw_data: "type_defs.DeleteScopeInputTypeDef" = dataclasses.field()

    scopeId = field("scopeId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteScopeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteScopeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMonitorInput:
    boto3_raw_data: "type_defs.GetMonitorInputTypeDef" = dataclasses.field()

    monitorName = field("monitorName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMonitorInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetMonitorInputTypeDef"]],
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
class GetQueryResultsMonitorTopContributorsInput:
    boto3_raw_data: "type_defs.GetQueryResultsMonitorTopContributorsInputTypeDef" = (
        dataclasses.field()
    )

    monitorName = field("monitorName")
    queryId = field("queryId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryResultsMonitorTopContributorsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryResultsMonitorTopContributorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsWorkloadInsightsTopContributorsDataInput:
    boto3_raw_data: (
        "type_defs.GetQueryResultsWorkloadInsightsTopContributorsDataInputTypeDef"
    ) = dataclasses.field()

    scopeId = field("scopeId")
    queryId = field("queryId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryResultsWorkloadInsightsTopContributorsDataInputTypeDef"
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
                "type_defs.GetQueryResultsWorkloadInsightsTopContributorsDataInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadInsightsTopContributorsDataPoint:
    boto3_raw_data: "type_defs.WorkloadInsightsTopContributorsDataPointTypeDef" = (
        dataclasses.field()
    )

    timestamps = field("timestamps")
    values = field("values")
    label = field("label")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkloadInsightsTopContributorsDataPointTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadInsightsTopContributorsDataPointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsWorkloadInsightsTopContributorsInput:
    boto3_raw_data: (
        "type_defs.GetQueryResultsWorkloadInsightsTopContributorsInputTypeDef"
    ) = dataclasses.field()

    scopeId = field("scopeId")
    queryId = field("queryId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryResultsWorkloadInsightsTopContributorsInputTypeDef"
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
                "type_defs.GetQueryResultsWorkloadInsightsTopContributorsInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadInsightsTopContributorsRow:
    boto3_raw_data: "type_defs.WorkloadInsightsTopContributorsRowTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    localSubnetId = field("localSubnetId")
    localAz = field("localAz")
    localVpcId = field("localVpcId")
    localRegion = field("localRegion")
    remoteIdentifier = field("remoteIdentifier")
    value = field("value")
    localSubnetArn = field("localSubnetArn")
    localVpcArn = field("localVpcArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkloadInsightsTopContributorsRowTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadInsightsTopContributorsRowTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStatusMonitorTopContributorsInput:
    boto3_raw_data: "type_defs.GetQueryStatusMonitorTopContributorsInputTypeDef" = (
        dataclasses.field()
    )

    monitorName = field("monitorName")
    queryId = field("queryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryStatusMonitorTopContributorsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryStatusMonitorTopContributorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStatusWorkloadInsightsTopContributorsDataInput:
    boto3_raw_data: (
        "type_defs.GetQueryStatusWorkloadInsightsTopContributorsDataInputTypeDef"
    ) = dataclasses.field()

    scopeId = field("scopeId")
    queryId = field("queryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryStatusWorkloadInsightsTopContributorsDataInputTypeDef"
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
                "type_defs.GetQueryStatusWorkloadInsightsTopContributorsDataInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStatusWorkloadInsightsTopContributorsInput:
    boto3_raw_data: (
        "type_defs.GetQueryStatusWorkloadInsightsTopContributorsInputTypeDef"
    ) = dataclasses.field()

    scopeId = field("scopeId")
    queryId = field("queryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryStatusWorkloadInsightsTopContributorsInputTypeDef"
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
                "type_defs.GetQueryStatusWorkloadInsightsTopContributorsInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetScopeInput:
    boto3_raw_data: "type_defs.GetScopeInputTypeDef" = dataclasses.field()

    scopeId = field("scopeId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetScopeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetScopeInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesMetadata:
    boto3_raw_data: "type_defs.KubernetesMetadataTypeDef" = dataclasses.field()

    localServiceName = field("localServiceName")
    localPodName = field("localPodName")
    localPodNamespace = field("localPodNamespace")
    remoteServiceName = field("remoteServiceName")
    remotePodName = field("remotePodName")
    remotePodNamespace = field("remotePodNamespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KubernetesMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorsInput:
    boto3_raw_data: "type_defs.ListMonitorsInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    monitorStatus = field("monitorStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitorSummary:
    boto3_raw_data: "type_defs.MonitorSummaryTypeDef" = dataclasses.field()

    monitorArn = field("monitorArn")
    monitorName = field("monitorName")
    monitorStatus = field("monitorStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonitorSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonitorSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScopesInput:
    boto3_raw_data: "type_defs.ListScopesInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListScopesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListScopesInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScopeSummary:
    boto3_raw_data: "type_defs.ScopeSummaryTypeDef" = dataclasses.field()

    scopeId = field("scopeId")
    status = field("status")
    scopeArn = field("scopeArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeSummaryTypeDef"]],
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
class TraversedComponent:
    boto3_raw_data: "type_defs.TraversedComponentTypeDef" = dataclasses.field()

    componentId = field("componentId")
    componentType = field("componentType")
    componentArn = field("componentArn")
    serviceName = field("serviceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TraversedComponentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TraversedComponentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopQueryMonitorTopContributorsInput:
    boto3_raw_data: "type_defs.StopQueryMonitorTopContributorsInputTypeDef" = (
        dataclasses.field()
    )

    monitorName = field("monitorName")
    queryId = field("queryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopQueryMonitorTopContributorsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopQueryMonitorTopContributorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopQueryWorkloadInsightsTopContributorsDataInput:
    boto3_raw_data: (
        "type_defs.StopQueryWorkloadInsightsTopContributorsDataInputTypeDef"
    ) = dataclasses.field()

    scopeId = field("scopeId")
    queryId = field("queryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopQueryWorkloadInsightsTopContributorsDataInputTypeDef"
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
                "type_defs.StopQueryWorkloadInsightsTopContributorsDataInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopQueryWorkloadInsightsTopContributorsInput:
    boto3_raw_data: "type_defs.StopQueryWorkloadInsightsTopContributorsInputTypeDef" = (
        dataclasses.field()
    )

    scopeId = field("scopeId")
    queryId = field("queryId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopQueryWorkloadInsightsTopContributorsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopQueryWorkloadInsightsTopContributorsInputTypeDef"]
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
    tags = field("tags")

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
class TargetId:
    boto3_raw_data: "type_defs.TargetIdTypeDef" = dataclasses.field()

    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetIdTypeDef"]]
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
class CreateMonitorInput:
    boto3_raw_data: "type_defs.CreateMonitorInputTypeDef" = dataclasses.field()

    monitorName = field("monitorName")

    @cached_property
    def localResources(self):  # pragma: no cover
        return MonitorLocalResource.make_many(self.boto3_raw_data["localResources"])

    scopeArn = field("scopeArn")

    @cached_property
    def remoteResources(self):  # pragma: no cover
        return MonitorRemoteResource.make_many(self.boto3_raw_data["remoteResources"])

    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMonitorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMonitorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMonitorInput:
    boto3_raw_data: "type_defs.UpdateMonitorInputTypeDef" = dataclasses.field()

    monitorName = field("monitorName")

    @cached_property
    def localResourcesToAdd(self):  # pragma: no cover
        return MonitorLocalResource.make_many(
            self.boto3_raw_data["localResourcesToAdd"]
        )

    @cached_property
    def localResourcesToRemove(self):  # pragma: no cover
        return MonitorLocalResource.make_many(
            self.boto3_raw_data["localResourcesToRemove"]
        )

    @cached_property
    def remoteResourcesToAdd(self):  # pragma: no cover
        return MonitorRemoteResource.make_many(
            self.boto3_raw_data["remoteResourcesToAdd"]
        )

    @cached_property
    def remoteResourcesToRemove(self):  # pragma: no cover
        return MonitorRemoteResource.make_many(
            self.boto3_raw_data["remoteResourcesToRemove"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMonitorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMonitorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMonitorOutput:
    boto3_raw_data: "type_defs.CreateMonitorOutputTypeDef" = dataclasses.field()

    monitorArn = field("monitorArn")
    monitorName = field("monitorName")
    monitorStatus = field("monitorStatus")

    @cached_property
    def localResources(self):  # pragma: no cover
        return MonitorLocalResource.make_many(self.boto3_raw_data["localResources"])

    @cached_property
    def remoteResources(self):  # pragma: no cover
        return MonitorRemoteResource.make_many(self.boto3_raw_data["remoteResources"])

    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMonitorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMonitorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScopeOutput:
    boto3_raw_data: "type_defs.CreateScopeOutputTypeDef" = dataclasses.field()

    scopeId = field("scopeId")
    status = field("status")
    scopeArn = field("scopeArn")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateScopeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScopeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMonitorOutput:
    boto3_raw_data: "type_defs.GetMonitorOutputTypeDef" = dataclasses.field()

    monitorArn = field("monitorArn")
    monitorName = field("monitorName")
    monitorStatus = field("monitorStatus")

    @cached_property
    def localResources(self):  # pragma: no cover
        return MonitorLocalResource.make_many(self.boto3_raw_data["localResources"])

    @cached_property
    def remoteResources(self):  # pragma: no cover
        return MonitorRemoteResource.make_many(self.boto3_raw_data["remoteResources"])

    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMonitorOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMonitorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStatusMonitorTopContributorsOutput:
    boto3_raw_data: "type_defs.GetQueryStatusMonitorTopContributorsOutputTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryStatusMonitorTopContributorsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryStatusMonitorTopContributorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStatusWorkloadInsightsTopContributorsDataOutput:
    boto3_raw_data: (
        "type_defs.GetQueryStatusWorkloadInsightsTopContributorsDataOutputTypeDef"
    ) = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryStatusWorkloadInsightsTopContributorsDataOutputTypeDef"
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
                "type_defs.GetQueryStatusWorkloadInsightsTopContributorsDataOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryStatusWorkloadInsightsTopContributorsOutput:
    boto3_raw_data: (
        "type_defs.GetQueryStatusWorkloadInsightsTopContributorsOutputTypeDef"
    ) = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryStatusWorkloadInsightsTopContributorsOutputTypeDef"
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
                "type_defs.GetQueryStatusWorkloadInsightsTopContributorsOutputTypeDef"
            ]
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

    tags = field("tags")

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
class StartQueryMonitorTopContributorsOutput:
    boto3_raw_data: "type_defs.StartQueryMonitorTopContributorsOutputTypeDef" = (
        dataclasses.field()
    )

    queryId = field("queryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartQueryMonitorTopContributorsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQueryMonitorTopContributorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryWorkloadInsightsTopContributorsDataOutput:
    boto3_raw_data: (
        "type_defs.StartQueryWorkloadInsightsTopContributorsDataOutputTypeDef"
    ) = dataclasses.field()

    queryId = field("queryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartQueryWorkloadInsightsTopContributorsDataOutputTypeDef"
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
                "type_defs.StartQueryWorkloadInsightsTopContributorsDataOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryWorkloadInsightsTopContributorsOutput:
    boto3_raw_data: (
        "type_defs.StartQueryWorkloadInsightsTopContributorsOutputTypeDef"
    ) = dataclasses.field()

    queryId = field("queryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartQueryWorkloadInsightsTopContributorsOutputTypeDef"
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
                "type_defs.StartQueryWorkloadInsightsTopContributorsOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMonitorOutput:
    boto3_raw_data: "type_defs.UpdateMonitorOutputTypeDef" = dataclasses.field()

    monitorArn = field("monitorArn")
    monitorName = field("monitorName")
    monitorStatus = field("monitorStatus")

    @cached_property
    def localResources(self):  # pragma: no cover
        return MonitorLocalResource.make_many(self.boto3_raw_data["localResources"])

    @cached_property
    def remoteResources(self):  # pragma: no cover
        return MonitorRemoteResource.make_many(self.boto3_raw_data["remoteResources"])

    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMonitorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMonitorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScopeOutput:
    boto3_raw_data: "type_defs.UpdateScopeOutputTypeDef" = dataclasses.field()

    scopeId = field("scopeId")
    status = field("status")
    scopeArn = field("scopeArn")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateScopeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScopeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsMonitorTopContributorsInputPaginate:
    boto3_raw_data: (
        "type_defs.GetQueryResultsMonitorTopContributorsInputPaginateTypeDef"
    ) = dataclasses.field()

    monitorName = field("monitorName")
    queryId = field("queryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryResultsMonitorTopContributorsInputPaginateTypeDef"
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
                "type_defs.GetQueryResultsMonitorTopContributorsInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsWorkloadInsightsTopContributorsDataInputPaginate:
    boto3_raw_data: "type_defs.GetQueryResultsWorkloadInsightsTopContributorsDataInputPaginateTypeDef" = (dataclasses.field())

    scopeId = field("scopeId")
    queryId = field("queryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryResultsWorkloadInsightsTopContributorsDataInputPaginateTypeDef"
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
                "type_defs.GetQueryResultsWorkloadInsightsTopContributorsDataInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsWorkloadInsightsTopContributorsInputPaginate:
    boto3_raw_data: (
        "type_defs.GetQueryResultsWorkloadInsightsTopContributorsInputPaginateTypeDef"
    ) = dataclasses.field()

    scopeId = field("scopeId")
    queryId = field("queryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryResultsWorkloadInsightsTopContributorsInputPaginateTypeDef"
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
                "type_defs.GetQueryResultsWorkloadInsightsTopContributorsInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorsInputPaginate:
    boto3_raw_data: "type_defs.ListMonitorsInputPaginateTypeDef" = dataclasses.field()

    monitorStatus = field("monitorStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScopesInputPaginate:
    boto3_raw_data: "type_defs.ListScopesInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListScopesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScopesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsWorkloadInsightsTopContributorsDataOutput:
    boto3_raw_data: (
        "type_defs.GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef"
    ) = dataclasses.field()

    unit = field("unit")

    @cached_property
    def datapoints(self):  # pragma: no cover
        return WorkloadInsightsTopContributorsDataPoint.make_many(
            self.boto3_raw_data["datapoints"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef"
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
                "type_defs.GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsWorkloadInsightsTopContributorsOutput:
    boto3_raw_data: (
        "type_defs.GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def topContributors(self):  # pragma: no cover
        return WorkloadInsightsTopContributorsRow.make_many(
            self.boto3_raw_data["topContributors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef"
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
                "type_defs.GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMonitorsOutput:
    boto3_raw_data: "type_defs.ListMonitorsOutputTypeDef" = dataclasses.field()

    @cached_property
    def monitors(self):  # pragma: no cover
        return MonitorSummary.make_many(self.boto3_raw_data["monitors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMonitorsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMonitorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListScopesOutput:
    boto3_raw_data: "type_defs.ListScopesOutputTypeDef" = dataclasses.field()

    @cached_property
    def scopes(self):  # pragma: no cover
        return ScopeSummary.make_many(self.boto3_raw_data["scopes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListScopesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListScopesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitorTopContributorsRow:
    boto3_raw_data: "type_defs.MonitorTopContributorsRowTypeDef" = dataclasses.field()

    localIp = field("localIp")
    snatIp = field("snatIp")
    localInstanceId = field("localInstanceId")
    localVpcId = field("localVpcId")
    localRegion = field("localRegion")
    localAz = field("localAz")
    localSubnetId = field("localSubnetId")
    targetPort = field("targetPort")
    destinationCategory = field("destinationCategory")
    remoteVpcId = field("remoteVpcId")
    remoteRegion = field("remoteRegion")
    remoteAz = field("remoteAz")
    remoteSubnetId = field("remoteSubnetId")
    remoteInstanceId = field("remoteInstanceId")
    remoteIp = field("remoteIp")
    dnatIp = field("dnatIp")
    value = field("value")

    @cached_property
    def traversedConstructs(self):  # pragma: no cover
        return TraversedComponent.make_many(self.boto3_raw_data["traversedConstructs"])

    @cached_property
    def kubernetesMetadata(self):  # pragma: no cover
        return KubernetesMetadata.make_one(self.boto3_raw_data["kubernetesMetadata"])

    localInstanceArn = field("localInstanceArn")
    localSubnetArn = field("localSubnetArn")
    localVpcArn = field("localVpcArn")
    remoteInstanceArn = field("remoteInstanceArn")
    remoteSubnetArn = field("remoteSubnetArn")
    remoteVpcArn = field("remoteVpcArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitorTopContributorsRowTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitorTopContributorsRowTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryMonitorTopContributorsInput:
    boto3_raw_data: "type_defs.StartQueryMonitorTopContributorsInputTypeDef" = (
        dataclasses.field()
    )

    monitorName = field("monitorName")
    startTime = field("startTime")
    endTime = field("endTime")
    metricName = field("metricName")
    destinationCategory = field("destinationCategory")
    limit = field("limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartQueryMonitorTopContributorsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQueryMonitorTopContributorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryWorkloadInsightsTopContributorsDataInput:
    boto3_raw_data: (
        "type_defs.StartQueryWorkloadInsightsTopContributorsDataInputTypeDef"
    ) = dataclasses.field()

    scopeId = field("scopeId")
    startTime = field("startTime")
    endTime = field("endTime")
    metricName = field("metricName")
    destinationCategory = field("destinationCategory")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartQueryWorkloadInsightsTopContributorsDataInputTypeDef"
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
                "type_defs.StartQueryWorkloadInsightsTopContributorsDataInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryWorkloadInsightsTopContributorsInput:
    boto3_raw_data: (
        "type_defs.StartQueryWorkloadInsightsTopContributorsInputTypeDef"
    ) = dataclasses.field()

    scopeId = field("scopeId")
    startTime = field("startTime")
    endTime = field("endTime")
    metricName = field("metricName")
    destinationCategory = field("destinationCategory")
    limit = field("limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartQueryWorkloadInsightsTopContributorsInputTypeDef"
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
                "type_defs.StartQueryWorkloadInsightsTopContributorsInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetIdentifier:
    boto3_raw_data: "type_defs.TargetIdentifierTypeDef" = dataclasses.field()

    @cached_property
    def targetId(self):  # pragma: no cover
        return TargetId.make_one(self.boto3_raw_data["targetId"])

    targetType = field("targetType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsMonitorTopContributorsOutput:
    boto3_raw_data: "type_defs.GetQueryResultsMonitorTopContributorsOutputTypeDef" = (
        dataclasses.field()
    )

    unit = field("unit")

    @cached_property
    def topContributors(self):  # pragma: no cover
        return MonitorTopContributorsRow.make_many(
            self.boto3_raw_data["topContributors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetQueryResultsMonitorTopContributorsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryResultsMonitorTopContributorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetResource:
    boto3_raw_data: "type_defs.TargetResourceTypeDef" = dataclasses.field()

    @cached_property
    def targetIdentifier(self):  # pragma: no cover
        return TargetIdentifier.make_one(self.boto3_raw_data["targetIdentifier"])

    region = field("region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateScopeInput:
    boto3_raw_data: "type_defs.CreateScopeInputTypeDef" = dataclasses.field()

    @cached_property
    def targets(self):  # pragma: no cover
        return TargetResource.make_many(self.boto3_raw_data["targets"])

    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateScopeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateScopeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetScopeOutput:
    boto3_raw_data: "type_defs.GetScopeOutputTypeDef" = dataclasses.field()

    scopeId = field("scopeId")
    status = field("status")
    scopeArn = field("scopeArn")

    @cached_property
    def targets(self):  # pragma: no cover
        return TargetResource.make_many(self.boto3_raw_data["targets"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetScopeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetScopeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScopeInput:
    boto3_raw_data: "type_defs.UpdateScopeInputTypeDef" = dataclasses.field()

    scopeId = field("scopeId")

    @cached_property
    def resourcesToAdd(self):  # pragma: no cover
        return TargetResource.make_many(self.boto3_raw_data["resourcesToAdd"])

    @cached_property
    def resourcesToDelete(self):  # pragma: no cover
        return TargetResource.make_many(self.boto3_raw_data["resourcesToDelete"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateScopeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScopeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
