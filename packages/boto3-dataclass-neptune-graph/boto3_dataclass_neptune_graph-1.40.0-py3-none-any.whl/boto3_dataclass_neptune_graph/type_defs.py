# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_neptune_graph import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CancelExportTaskInput:
    boto3_raw_data: "type_defs.CancelExportTaskInputTypeDef" = dataclasses.field()

    taskIdentifier = field("taskIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelExportTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelExportTaskInputTypeDef"]
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
class CancelImportTaskInput:
    boto3_raw_data: "type_defs.CancelImportTaskInputTypeDef" = dataclasses.field()

    taskIdentifier = field("taskIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelImportTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelImportTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelQueryInput:
    boto3_raw_data: "type_defs.CancelQueryInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    queryId = field("queryId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelQueryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchConfiguration:
    boto3_raw_data: "type_defs.VectorSearchConfigurationTypeDef" = dataclasses.field()

    dimension = field("dimension")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VectorSearchConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorSearchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGraphSnapshotInput:
    boto3_raw_data: "type_defs.CreateGraphSnapshotInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    snapshotName = field("snapshotName")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGraphSnapshotInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGraphSnapshotInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePrivateGraphEndpointInput:
    boto3_raw_data: "type_defs.CreatePrivateGraphEndpointInputTypeDef" = (
        dataclasses.field()
    )

    graphIdentifier = field("graphIdentifier")
    vpcId = field("vpcId")
    subnetIds = field("subnetIds")
    vpcSecurityGroupIds = field("vpcSecurityGroupIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePrivateGraphEndpointInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePrivateGraphEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGraphInput:
    boto3_raw_data: "type_defs.DeleteGraphInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    skipSnapshot = field("skipSnapshot")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteGraphInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGraphInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGraphSnapshotInput:
    boto3_raw_data: "type_defs.DeleteGraphSnapshotInputTypeDef" = dataclasses.field()

    snapshotIdentifier = field("snapshotIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGraphSnapshotInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGraphSnapshotInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePrivateGraphEndpointInput:
    boto3_raw_data: "type_defs.DeletePrivateGraphEndpointInputTypeDef" = (
        dataclasses.field()
    )

    graphIdentifier = field("graphIdentifier")
    vpcId = field("vpcId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePrivateGraphEndpointInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePrivateGraphEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EdgeStructure:
    boto3_raw_data: "type_defs.EdgeStructureTypeDef" = dataclasses.field()

    count = field("count")
    edgeProperties = field("edgeProperties")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdgeStructureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EdgeStructureTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteQueryInput:
    boto3_raw_data: "type_defs.ExecuteQueryInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    queryString = field("queryString")
    language = field("language")
    parameters = field("parameters")
    planCache = field("planCache")
    explainMode = field("explainMode")
    queryTimeoutMilliseconds = field("queryTimeoutMilliseconds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecuteQueryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportFilterPropertyAttributes:
    boto3_raw_data: "type_defs.ExportFilterPropertyAttributesTypeDef" = (
        dataclasses.field()
    )

    outputType = field("outputType")
    sourcePropertyName = field("sourcePropertyName")
    multiValueHandling = field("multiValueHandling")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportFilterPropertyAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportFilterPropertyAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTaskDetails:
    boto3_raw_data: "type_defs.ExportTaskDetailsTypeDef" = dataclasses.field()

    startTime = field("startTime")
    timeElapsedSeconds = field("timeElapsedSeconds")
    progressPercentage = field("progressPercentage")
    numVerticesWritten = field("numVerticesWritten")
    numEdgesWritten = field("numEdgesWritten")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportTaskDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportTaskDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTaskSummary:
    boto3_raw_data: "type_defs.ExportTaskSummaryTypeDef" = dataclasses.field()

    graphId = field("graphId")
    roleArn = field("roleArn")
    taskId = field("taskId")
    status = field("status")
    format = field("format")
    destination = field("destination")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    parquetType = field("parquetType")
    statusReason = field("statusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportTaskSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportTaskSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportTaskInput:
    boto3_raw_data: "type_defs.GetExportTaskInputTypeDef" = dataclasses.field()

    taskIdentifier = field("taskIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExportTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportTaskInputTypeDef"]
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
class GetGraphInput:
    boto3_raw_data: "type_defs.GetGraphInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGraphInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetGraphInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphSnapshotInput:
    boto3_raw_data: "type_defs.GetGraphSnapshotInputTypeDef" = dataclasses.field()

    snapshotIdentifier = field("snapshotIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGraphSnapshotInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphSnapshotInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphSummaryInput:
    boto3_raw_data: "type_defs.GetGraphSummaryInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    mode = field("mode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGraphSummaryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphSummaryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportTaskInput:
    boto3_raw_data: "type_defs.GetImportTaskInputTypeDef" = dataclasses.field()

    taskIdentifier = field("taskIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTaskDetails:
    boto3_raw_data: "type_defs.ImportTaskDetailsTypeDef" = dataclasses.field()

    status = field("status")
    startTime = field("startTime")
    timeElapsedSeconds = field("timeElapsedSeconds")
    progressPercentage = field("progressPercentage")
    errorCount = field("errorCount")
    statementCount = field("statementCount")
    dictionaryEntryCount = field("dictionaryEntryCount")
    errorDetails = field("errorDetails")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportTaskDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTaskDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPrivateGraphEndpointInput:
    boto3_raw_data: "type_defs.GetPrivateGraphEndpointInputTypeDef" = (
        dataclasses.field()
    )

    graphIdentifier = field("graphIdentifier")
    vpcId = field("vpcId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPrivateGraphEndpointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPrivateGraphEndpointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryInput:
    boto3_raw_data: "type_defs.GetQueryInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    queryId = field("queryId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetQueryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetQueryInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeStructure:
    boto3_raw_data: "type_defs.NodeStructureTypeDef" = dataclasses.field()

    count = field("count")
    nodeProperties = field("nodeProperties")
    distinctOutgoingEdgeLabels = field("distinctOutgoingEdgeLabels")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeStructureTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodeStructureTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GraphSnapshotSummary:
    boto3_raw_data: "type_defs.GraphSnapshotSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    sourceGraphId = field("sourceGraphId")
    snapshotCreateTime = field("snapshotCreateTime")
    status = field("status")
    kmsKeyIdentifier = field("kmsKeyIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GraphSnapshotSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GraphSnapshotSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GraphSummary:
    boto3_raw_data: "type_defs.GraphSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    provisionedMemory = field("provisionedMemory")
    publicConnectivity = field("publicConnectivity")
    endpoint = field("endpoint")
    replicaCount = field("replicaCount")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    deletionProtection = field("deletionProtection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GraphSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GraphSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NeptuneImportOptions:
    boto3_raw_data: "type_defs.NeptuneImportOptionsTypeDef" = dataclasses.field()

    s3ExportPath = field("s3ExportPath")
    s3ExportKmsKeyId = field("s3ExportKmsKeyId")
    preserveDefaultVertexLabels = field("preserveDefaultVertexLabels")
    preserveEdgeIds = field("preserveEdgeIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NeptuneImportOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NeptuneImportOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportTaskSummary:
    boto3_raw_data: "type_defs.ImportTaskSummaryTypeDef" = dataclasses.field()

    taskId = field("taskId")
    source = field("source")
    roleArn = field("roleArn")
    status = field("status")
    graphId = field("graphId")
    format = field("format")
    parquetType = field("parquetType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportTaskSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportTaskSummaryTypeDef"]
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
class ListExportTasksInput:
    boto3_raw_data: "type_defs.ListExportTasksInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportTasksInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportTasksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGraphSnapshotsInput:
    boto3_raw_data: "type_defs.ListGraphSnapshotsInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGraphSnapshotsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGraphSnapshotsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGraphsInput:
    boto3_raw_data: "type_defs.ListGraphsInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGraphsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListGraphsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportTasksInput:
    boto3_raw_data: "type_defs.ListImportTasksInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportTasksInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportTasksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrivateGraphEndpointsInput:
    boto3_raw_data: "type_defs.ListPrivateGraphEndpointsInputTypeDef" = (
        dataclasses.field()
    )

    graphIdentifier = field("graphIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPrivateGraphEndpointsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrivateGraphEndpointsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateGraphEndpointSummary:
    boto3_raw_data: "type_defs.PrivateGraphEndpointSummaryTypeDef" = dataclasses.field()

    vpcId = field("vpcId")
    subnetIds = field("subnetIds")
    status = field("status")
    vpcEndpointId = field("vpcEndpointId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivateGraphEndpointSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateGraphEndpointSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueriesInput:
    boto3_raw_data: "type_defs.ListQueriesInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    maxResults = field("maxResults")
    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListQueriesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueriesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QuerySummary:
    boto3_raw_data: "type_defs.QuerySummaryTypeDef" = dataclasses.field()

    id = field("id")
    queryString = field("queryString")
    waited = field("waited")
    elapsed = field("elapsed")
    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QuerySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QuerySummaryTypeDef"]],
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
class ResetGraphInput:
    boto3_raw_data: "type_defs.ResetGraphInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    skipSnapshot = field("skipSnapshot")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResetGraphInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResetGraphInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreGraphFromSnapshotInput:
    boto3_raw_data: "type_defs.RestoreGraphFromSnapshotInputTypeDef" = (
        dataclasses.field()
    )

    snapshotIdentifier = field("snapshotIdentifier")
    graphName = field("graphName")
    provisionedMemory = field("provisionedMemory")
    deletionProtection = field("deletionProtection")
    tags = field("tags")
    replicaCount = field("replicaCount")
    publicConnectivity = field("publicConnectivity")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreGraphFromSnapshotInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreGraphFromSnapshotInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartGraphInput:
    boto3_raw_data: "type_defs.StartGraphInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartGraphInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StartGraphInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopGraphInput:
    boto3_raw_data: "type_defs.StopGraphInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopGraphInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopGraphInputTypeDef"]],
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
class UpdateGraphInput:
    boto3_raw_data: "type_defs.UpdateGraphInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    publicConnectivity = field("publicConnectivity")
    provisionedMemory = field("provisionedMemory")
    deletionProtection = field("deletionProtection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateGraphInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGraphInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelExportTaskOutput:
    boto3_raw_data: "type_defs.CancelExportTaskOutputTypeDef" = dataclasses.field()

    graphId = field("graphId")
    roleArn = field("roleArn")
    taskId = field("taskId")
    status = field("status")
    format = field("format")
    destination = field("destination")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    parquetType = field("parquetType")
    statusReason = field("statusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelExportTaskOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelExportTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelImportTaskOutput:
    boto3_raw_data: "type_defs.CancelImportTaskOutputTypeDef" = dataclasses.field()

    graphId = field("graphId")
    taskId = field("taskId")
    source = field("source")
    format = field("format")
    parquetType = field("parquetType")
    roleArn = field("roleArn")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelImportTaskOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelImportTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGraphSnapshotOutput:
    boto3_raw_data: "type_defs.CreateGraphSnapshotOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    sourceGraphId = field("sourceGraphId")
    snapshotCreateTime = field("snapshotCreateTime")
    status = field("status")
    kmsKeyIdentifier = field("kmsKeyIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGraphSnapshotOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGraphSnapshotOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePrivateGraphEndpointOutput:
    boto3_raw_data: "type_defs.CreatePrivateGraphEndpointOutputTypeDef" = (
        dataclasses.field()
    )

    vpcId = field("vpcId")
    subnetIds = field("subnetIds")
    status = field("status")
    vpcEndpointId = field("vpcEndpointId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePrivateGraphEndpointOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePrivateGraphEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGraphSnapshotOutput:
    boto3_raw_data: "type_defs.DeleteGraphSnapshotOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    sourceGraphId = field("sourceGraphId")
    snapshotCreateTime = field("snapshotCreateTime")
    status = field("status")
    kmsKeyIdentifier = field("kmsKeyIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGraphSnapshotOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGraphSnapshotOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePrivateGraphEndpointOutput:
    boto3_raw_data: "type_defs.DeletePrivateGraphEndpointOutputTypeDef" = (
        dataclasses.field()
    )

    vpcId = field("vpcId")
    subnetIds = field("subnetIds")
    status = field("status")
    vpcEndpointId = field("vpcEndpointId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePrivateGraphEndpointOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePrivateGraphEndpointOutputTypeDef"]
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
class ExecuteQueryOutput:
    boto3_raw_data: "type_defs.ExecuteQueryOutputTypeDef" = dataclasses.field()

    payload = field("payload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphSnapshotOutput:
    boto3_raw_data: "type_defs.GetGraphSnapshotOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    sourceGraphId = field("sourceGraphId")
    snapshotCreateTime = field("snapshotCreateTime")
    status = field("status")
    kmsKeyIdentifier = field("kmsKeyIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGraphSnapshotOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphSnapshotOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPrivateGraphEndpointOutput:
    boto3_raw_data: "type_defs.GetPrivateGraphEndpointOutputTypeDef" = (
        dataclasses.field()
    )

    vpcId = field("vpcId")
    subnetIds = field("subnetIds")
    status = field("status")
    vpcEndpointId = field("vpcEndpointId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPrivateGraphEndpointOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPrivateGraphEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryOutput:
    boto3_raw_data: "type_defs.GetQueryOutputTypeDef" = dataclasses.field()

    id = field("id")
    queryString = field("queryString")
    waited = field("waited")
    elapsed = field("elapsed")
    state = field("state")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetQueryOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetQueryOutputTypeDef"]],
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
class CreateGraphInput:
    boto3_raw_data: "type_defs.CreateGraphInputTypeDef" = dataclasses.field()

    graphName = field("graphName")
    provisionedMemory = field("provisionedMemory")
    tags = field("tags")
    publicConnectivity = field("publicConnectivity")
    kmsKeyIdentifier = field("kmsKeyIdentifier")

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return VectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    replicaCount = field("replicaCount")
    deletionProtection = field("deletionProtection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateGraphInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGraphInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGraphOutput:
    boto3_raw_data: "type_defs.CreateGraphOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    statusReason = field("statusReason")
    createTime = field("createTime")
    provisionedMemory = field("provisionedMemory")
    endpoint = field("endpoint")
    publicConnectivity = field("publicConnectivity")

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return VectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    replicaCount = field("replicaCount")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    sourceSnapshotId = field("sourceSnapshotId")
    deletionProtection = field("deletionProtection")
    buildNumber = field("buildNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateGraphOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGraphOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGraphOutput:
    boto3_raw_data: "type_defs.DeleteGraphOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    statusReason = field("statusReason")
    createTime = field("createTime")
    provisionedMemory = field("provisionedMemory")
    endpoint = field("endpoint")
    publicConnectivity = field("publicConnectivity")

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return VectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    replicaCount = field("replicaCount")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    sourceSnapshotId = field("sourceSnapshotId")
    deletionProtection = field("deletionProtection")
    buildNumber = field("buildNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteGraphOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGraphOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphOutput:
    boto3_raw_data: "type_defs.GetGraphOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    statusReason = field("statusReason")
    createTime = field("createTime")
    provisionedMemory = field("provisionedMemory")
    endpoint = field("endpoint")
    publicConnectivity = field("publicConnectivity")

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return VectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    replicaCount = field("replicaCount")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    sourceSnapshotId = field("sourceSnapshotId")
    deletionProtection = field("deletionProtection")
    buildNumber = field("buildNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGraphOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetGraphOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetGraphOutput:
    boto3_raw_data: "type_defs.ResetGraphOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    statusReason = field("statusReason")
    createTime = field("createTime")
    provisionedMemory = field("provisionedMemory")
    endpoint = field("endpoint")
    publicConnectivity = field("publicConnectivity")

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return VectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    replicaCount = field("replicaCount")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    sourceSnapshotId = field("sourceSnapshotId")
    deletionProtection = field("deletionProtection")
    buildNumber = field("buildNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResetGraphOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetGraphOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreGraphFromSnapshotOutput:
    boto3_raw_data: "type_defs.RestoreGraphFromSnapshotOutputTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    statusReason = field("statusReason")
    createTime = field("createTime")
    provisionedMemory = field("provisionedMemory")
    endpoint = field("endpoint")
    publicConnectivity = field("publicConnectivity")

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return VectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    replicaCount = field("replicaCount")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    sourceSnapshotId = field("sourceSnapshotId")
    deletionProtection = field("deletionProtection")
    buildNumber = field("buildNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreGraphFromSnapshotOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreGraphFromSnapshotOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartGraphOutput:
    boto3_raw_data: "type_defs.StartGraphOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    statusReason = field("statusReason")
    createTime = field("createTime")
    provisionedMemory = field("provisionedMemory")
    endpoint = field("endpoint")
    publicConnectivity = field("publicConnectivity")

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return VectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    replicaCount = field("replicaCount")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    sourceSnapshotId = field("sourceSnapshotId")
    deletionProtection = field("deletionProtection")
    buildNumber = field("buildNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartGraphOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartGraphOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopGraphOutput:
    boto3_raw_data: "type_defs.StopGraphOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    statusReason = field("statusReason")
    createTime = field("createTime")
    provisionedMemory = field("provisionedMemory")
    endpoint = field("endpoint")
    publicConnectivity = field("publicConnectivity")

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return VectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    replicaCount = field("replicaCount")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    sourceSnapshotId = field("sourceSnapshotId")
    deletionProtection = field("deletionProtection")
    buildNumber = field("buildNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopGraphOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopGraphOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGraphOutput:
    boto3_raw_data: "type_defs.UpdateGraphOutputTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    status = field("status")
    statusReason = field("statusReason")
    createTime = field("createTime")
    provisionedMemory = field("provisionedMemory")
    endpoint = field("endpoint")
    publicConnectivity = field("publicConnectivity")

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return VectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    replicaCount = field("replicaCount")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    sourceSnapshotId = field("sourceSnapshotId")
    deletionProtection = field("deletionProtection")
    buildNumber = field("buildNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateGraphOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGraphOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportFilterElementOutput:
    boto3_raw_data: "type_defs.ExportFilterElementOutputTypeDef" = dataclasses.field()

    properties = field("properties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportFilterElementOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportFilterElementOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportFilterElement:
    boto3_raw_data: "type_defs.ExportFilterElementTypeDef" = dataclasses.field()

    properties = field("properties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportFilterElementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportFilterElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportTasksOutput:
    boto3_raw_data: "type_defs.ListExportTasksOutputTypeDef" = dataclasses.field()

    @cached_property
    def tasks(self):  # pragma: no cover
        return ExportTaskSummary.make_many(self.boto3_raw_data["tasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportTasksOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportTasksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportTaskInputWaitExtra:
    boto3_raw_data: "type_defs.GetExportTaskInputWaitExtraTypeDef" = dataclasses.field()

    taskIdentifier = field("taskIdentifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExportTaskInputWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportTaskInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportTaskInputWait:
    boto3_raw_data: "type_defs.GetExportTaskInputWaitTypeDef" = dataclasses.field()

    taskIdentifier = field("taskIdentifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExportTaskInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportTaskInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphInputWaitExtraExtra:
    boto3_raw_data: "type_defs.GetGraphInputWaitExtraExtraTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGraphInputWaitExtraExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphInputWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphInputWaitExtra:
    boto3_raw_data: "type_defs.GetGraphInputWaitExtraTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGraphInputWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphInputWait:
    boto3_raw_data: "type_defs.GetGraphInputWaitTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGraphInputWaitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphSnapshotInputWaitExtra:
    boto3_raw_data: "type_defs.GetGraphSnapshotInputWaitExtraTypeDef" = (
        dataclasses.field()
    )

    snapshotIdentifier = field("snapshotIdentifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetGraphSnapshotInputWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphSnapshotInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGraphSnapshotInputWait:
    boto3_raw_data: "type_defs.GetGraphSnapshotInputWaitTypeDef" = dataclasses.field()

    snapshotIdentifier = field("snapshotIdentifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGraphSnapshotInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphSnapshotInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportTaskInputWaitExtra:
    boto3_raw_data: "type_defs.GetImportTaskInputWaitExtraTypeDef" = dataclasses.field()

    taskIdentifier = field("taskIdentifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportTaskInputWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportTaskInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportTaskInputWait:
    boto3_raw_data: "type_defs.GetImportTaskInputWaitTypeDef" = dataclasses.field()

    taskIdentifier = field("taskIdentifier")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportTaskInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportTaskInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPrivateGraphEndpointInputWaitExtra:
    boto3_raw_data: "type_defs.GetPrivateGraphEndpointInputWaitExtraTypeDef" = (
        dataclasses.field()
    )

    graphIdentifier = field("graphIdentifier")
    vpcId = field("vpcId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetPrivateGraphEndpointInputWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPrivateGraphEndpointInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPrivateGraphEndpointInputWait:
    boto3_raw_data: "type_defs.GetPrivateGraphEndpointInputWaitTypeDef" = (
        dataclasses.field()
    )

    graphIdentifier = field("graphIdentifier")
    vpcId = field("vpcId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPrivateGraphEndpointInputWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPrivateGraphEndpointInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GraphDataSummary:
    boto3_raw_data: "type_defs.GraphDataSummaryTypeDef" = dataclasses.field()

    numNodes = field("numNodes")
    numEdges = field("numEdges")
    numNodeLabels = field("numNodeLabels")
    numEdgeLabels = field("numEdgeLabels")
    nodeLabels = field("nodeLabels")
    edgeLabels = field("edgeLabels")
    numNodeProperties = field("numNodeProperties")
    numEdgeProperties = field("numEdgeProperties")
    nodeProperties = field("nodeProperties")
    edgeProperties = field("edgeProperties")
    totalNodePropertyValues = field("totalNodePropertyValues")
    totalEdgePropertyValues = field("totalEdgePropertyValues")

    @cached_property
    def nodeStructures(self):  # pragma: no cover
        return NodeStructure.make_many(self.boto3_raw_data["nodeStructures"])

    @cached_property
    def edgeStructures(self):  # pragma: no cover
        return EdgeStructure.make_many(self.boto3_raw_data["edgeStructures"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GraphDataSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GraphDataSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGraphSnapshotsOutput:
    boto3_raw_data: "type_defs.ListGraphSnapshotsOutputTypeDef" = dataclasses.field()

    @cached_property
    def graphSnapshots(self):  # pragma: no cover
        return GraphSnapshotSummary.make_many(self.boto3_raw_data["graphSnapshots"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGraphSnapshotsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGraphSnapshotsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGraphsOutput:
    boto3_raw_data: "type_defs.ListGraphsOutputTypeDef" = dataclasses.field()

    @cached_property
    def graphs(self):  # pragma: no cover
        return GraphSummary.make_many(self.boto3_raw_data["graphs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGraphsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGraphsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportOptions:
    boto3_raw_data: "type_defs.ImportOptionsTypeDef" = dataclasses.field()

    @cached_property
    def neptune(self):  # pragma: no cover
        return NeptuneImportOptions.make_one(self.boto3_raw_data["neptune"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportTasksOutput:
    boto3_raw_data: "type_defs.ListImportTasksOutputTypeDef" = dataclasses.field()

    @cached_property
    def tasks(self):  # pragma: no cover
        return ImportTaskSummary.make_many(self.boto3_raw_data["tasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportTasksOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportTasksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportTasksInputPaginate:
    boto3_raw_data: "type_defs.ListExportTasksInputPaginateTypeDef" = (
        dataclasses.field()
    )

    graphIdentifier = field("graphIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportTasksInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportTasksInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGraphSnapshotsInputPaginate:
    boto3_raw_data: "type_defs.ListGraphSnapshotsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    graphIdentifier = field("graphIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGraphSnapshotsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGraphSnapshotsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGraphsInputPaginate:
    boto3_raw_data: "type_defs.ListGraphsInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGraphsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGraphsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportTasksInputPaginate:
    boto3_raw_data: "type_defs.ListImportTasksInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportTasksInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportTasksInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrivateGraphEndpointsInputPaginate:
    boto3_raw_data: "type_defs.ListPrivateGraphEndpointsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    graphIdentifier = field("graphIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPrivateGraphEndpointsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrivateGraphEndpointsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrivateGraphEndpointsOutput:
    boto3_raw_data: "type_defs.ListPrivateGraphEndpointsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def privateGraphEndpoints(self):  # pragma: no cover
        return PrivateGraphEndpointSummary.make_many(
            self.boto3_raw_data["privateGraphEndpoints"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPrivateGraphEndpointsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrivateGraphEndpointsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueriesOutput:
    boto3_raw_data: "type_defs.ListQueriesOutputTypeDef" = dataclasses.field()

    @cached_property
    def queries(self):  # pragma: no cover
        return QuerySummary.make_many(self.boto3_raw_data["queries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListQueriesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueriesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportFilterOutput:
    boto3_raw_data: "type_defs.ExportFilterOutputTypeDef" = dataclasses.field()

    vertexFilter = field("vertexFilter")
    edgeFilter = field("edgeFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportFilterOutputTypeDef"]
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

    vertexFilter = field("vertexFilter")
    edgeFilter = field("edgeFilter")

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
class GetGraphSummaryOutput:
    boto3_raw_data: "type_defs.GetGraphSummaryOutputTypeDef" = dataclasses.field()

    version = field("version")
    lastStatisticsComputationTime = field("lastStatisticsComputationTime")

    @cached_property
    def graphSummary(self):  # pragma: no cover
        return GraphDataSummary.make_one(self.boto3_raw_data["graphSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGraphSummaryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGraphSummaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGraphUsingImportTaskInput:
    boto3_raw_data: "type_defs.CreateGraphUsingImportTaskInputTypeDef" = (
        dataclasses.field()
    )

    graphName = field("graphName")
    source = field("source")
    roleArn = field("roleArn")
    tags = field("tags")
    publicConnectivity = field("publicConnectivity")
    kmsKeyIdentifier = field("kmsKeyIdentifier")

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return VectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    replicaCount = field("replicaCount")
    deletionProtection = field("deletionProtection")

    @cached_property
    def importOptions(self):  # pragma: no cover
        return ImportOptions.make_one(self.boto3_raw_data["importOptions"])

    maxProvisionedMemory = field("maxProvisionedMemory")
    minProvisionedMemory = field("minProvisionedMemory")
    failOnError = field("failOnError")
    format = field("format")
    parquetType = field("parquetType")
    blankNodeHandling = field("blankNodeHandling")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateGraphUsingImportTaskInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGraphUsingImportTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGraphUsingImportTaskOutput:
    boto3_raw_data: "type_defs.CreateGraphUsingImportTaskOutputTypeDef" = (
        dataclasses.field()
    )

    graphId = field("graphId")
    taskId = field("taskId")
    source = field("source")
    format = field("format")
    parquetType = field("parquetType")
    roleArn = field("roleArn")
    status = field("status")

    @cached_property
    def importOptions(self):  # pragma: no cover
        return ImportOptions.make_one(self.boto3_raw_data["importOptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateGraphUsingImportTaskOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGraphUsingImportTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportTaskOutput:
    boto3_raw_data: "type_defs.GetImportTaskOutputTypeDef" = dataclasses.field()

    graphId = field("graphId")
    taskId = field("taskId")
    source = field("source")
    format = field("format")
    parquetType = field("parquetType")
    roleArn = field("roleArn")
    status = field("status")

    @cached_property
    def importOptions(self):  # pragma: no cover
        return ImportOptions.make_one(self.boto3_raw_data["importOptions"])

    @cached_property
    def importTaskDetails(self):  # pragma: no cover
        return ImportTaskDetails.make_one(self.boto3_raw_data["importTaskDetails"])

    attemptNumber = field("attemptNumber")
    statusReason = field("statusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportTaskOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportTaskInput:
    boto3_raw_data: "type_defs.StartImportTaskInputTypeDef" = dataclasses.field()

    source = field("source")
    graphIdentifier = field("graphIdentifier")
    roleArn = field("roleArn")

    @cached_property
    def importOptions(self):  # pragma: no cover
        return ImportOptions.make_one(self.boto3_raw_data["importOptions"])

    failOnError = field("failOnError")
    format = field("format")
    parquetType = field("parquetType")
    blankNodeHandling = field("blankNodeHandling")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportTaskOutput:
    boto3_raw_data: "type_defs.StartImportTaskOutputTypeDef" = dataclasses.field()

    graphId = field("graphId")
    taskId = field("taskId")
    source = field("source")
    format = field("format")
    parquetType = field("parquetType")
    roleArn = field("roleArn")
    status = field("status")

    @cached_property
    def importOptions(self):  # pragma: no cover
        return ImportOptions.make_one(self.boto3_raw_data["importOptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportTaskOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExportTaskOutput:
    boto3_raw_data: "type_defs.GetExportTaskOutputTypeDef" = dataclasses.field()

    graphId = field("graphId")
    roleArn = field("roleArn")
    taskId = field("taskId")
    status = field("status")
    format = field("format")
    destination = field("destination")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    parquetType = field("parquetType")
    statusReason = field("statusReason")

    @cached_property
    def exportTaskDetails(self):  # pragma: no cover
        return ExportTaskDetails.make_one(self.boto3_raw_data["exportTaskDetails"])

    @cached_property
    def exportFilter(self):  # pragma: no cover
        return ExportFilterOutput.make_one(self.boto3_raw_data["exportFilter"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExportTaskOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExportTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExportTaskOutput:
    boto3_raw_data: "type_defs.StartExportTaskOutputTypeDef" = dataclasses.field()

    graphId = field("graphId")
    roleArn = field("roleArn")
    taskId = field("taskId")
    status = field("status")
    format = field("format")
    destination = field("destination")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    parquetType = field("parquetType")
    statusReason = field("statusReason")

    @cached_property
    def exportFilter(self):  # pragma: no cover
        return ExportFilterOutput.make_one(self.boto3_raw_data["exportFilter"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExportTaskOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExportTaskOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExportTaskInput:
    boto3_raw_data: "type_defs.StartExportTaskInputTypeDef" = dataclasses.field()

    graphIdentifier = field("graphIdentifier")
    roleArn = field("roleArn")
    format = field("format")
    destination = field("destination")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    parquetType = field("parquetType")
    exportFilter = field("exportFilter")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExportTaskInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExportTaskInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
