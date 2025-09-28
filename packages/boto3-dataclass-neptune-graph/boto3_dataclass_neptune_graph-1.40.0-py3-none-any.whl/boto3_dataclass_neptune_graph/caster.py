# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_neptune_graph import type_defs as bs_td


class NEPTUNE_GRAPHCaster:

    def cancel_export_task(
        self,
        res: "bs_td.CancelExportTaskOutputTypeDef",
    ) -> "dc_td.CancelExportTaskOutput":
        return dc_td.CancelExportTaskOutput.make_one(res)

    def cancel_import_task(
        self,
        res: "bs_td.CancelImportTaskOutputTypeDef",
    ) -> "dc_td.CancelImportTaskOutput":
        return dc_td.CancelImportTaskOutput.make_one(res)

    def cancel_query(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_graph(
        self,
        res: "bs_td.CreateGraphOutputTypeDef",
    ) -> "dc_td.CreateGraphOutput":
        return dc_td.CreateGraphOutput.make_one(res)

    def create_graph_snapshot(
        self,
        res: "bs_td.CreateGraphSnapshotOutputTypeDef",
    ) -> "dc_td.CreateGraphSnapshotOutput":
        return dc_td.CreateGraphSnapshotOutput.make_one(res)

    def create_graph_using_import_task(
        self,
        res: "bs_td.CreateGraphUsingImportTaskOutputTypeDef",
    ) -> "dc_td.CreateGraphUsingImportTaskOutput":
        return dc_td.CreateGraphUsingImportTaskOutput.make_one(res)

    def create_private_graph_endpoint(
        self,
        res: "bs_td.CreatePrivateGraphEndpointOutputTypeDef",
    ) -> "dc_td.CreatePrivateGraphEndpointOutput":
        return dc_td.CreatePrivateGraphEndpointOutput.make_one(res)

    def delete_graph(
        self,
        res: "bs_td.DeleteGraphOutputTypeDef",
    ) -> "dc_td.DeleteGraphOutput":
        return dc_td.DeleteGraphOutput.make_one(res)

    def delete_graph_snapshot(
        self,
        res: "bs_td.DeleteGraphSnapshotOutputTypeDef",
    ) -> "dc_td.DeleteGraphSnapshotOutput":
        return dc_td.DeleteGraphSnapshotOutput.make_one(res)

    def delete_private_graph_endpoint(
        self,
        res: "bs_td.DeletePrivateGraphEndpointOutputTypeDef",
    ) -> "dc_td.DeletePrivateGraphEndpointOutput":
        return dc_td.DeletePrivateGraphEndpointOutput.make_one(res)

    def execute_query(
        self,
        res: "bs_td.ExecuteQueryOutputTypeDef",
    ) -> "dc_td.ExecuteQueryOutput":
        return dc_td.ExecuteQueryOutput.make_one(res)

    def get_export_task(
        self,
        res: "bs_td.GetExportTaskOutputTypeDef",
    ) -> "dc_td.GetExportTaskOutput":
        return dc_td.GetExportTaskOutput.make_one(res)

    def get_graph(
        self,
        res: "bs_td.GetGraphOutputTypeDef",
    ) -> "dc_td.GetGraphOutput":
        return dc_td.GetGraphOutput.make_one(res)

    def get_graph_snapshot(
        self,
        res: "bs_td.GetGraphSnapshotOutputTypeDef",
    ) -> "dc_td.GetGraphSnapshotOutput":
        return dc_td.GetGraphSnapshotOutput.make_one(res)

    def get_graph_summary(
        self,
        res: "bs_td.GetGraphSummaryOutputTypeDef",
    ) -> "dc_td.GetGraphSummaryOutput":
        return dc_td.GetGraphSummaryOutput.make_one(res)

    def get_import_task(
        self,
        res: "bs_td.GetImportTaskOutputTypeDef",
    ) -> "dc_td.GetImportTaskOutput":
        return dc_td.GetImportTaskOutput.make_one(res)

    def get_private_graph_endpoint(
        self,
        res: "bs_td.GetPrivateGraphEndpointOutputTypeDef",
    ) -> "dc_td.GetPrivateGraphEndpointOutput":
        return dc_td.GetPrivateGraphEndpointOutput.make_one(res)

    def get_query(
        self,
        res: "bs_td.GetQueryOutputTypeDef",
    ) -> "dc_td.GetQueryOutput":
        return dc_td.GetQueryOutput.make_one(res)

    def list_export_tasks(
        self,
        res: "bs_td.ListExportTasksOutputTypeDef",
    ) -> "dc_td.ListExportTasksOutput":
        return dc_td.ListExportTasksOutput.make_one(res)

    def list_graph_snapshots(
        self,
        res: "bs_td.ListGraphSnapshotsOutputTypeDef",
    ) -> "dc_td.ListGraphSnapshotsOutput":
        return dc_td.ListGraphSnapshotsOutput.make_one(res)

    def list_graphs(
        self,
        res: "bs_td.ListGraphsOutputTypeDef",
    ) -> "dc_td.ListGraphsOutput":
        return dc_td.ListGraphsOutput.make_one(res)

    def list_import_tasks(
        self,
        res: "bs_td.ListImportTasksOutputTypeDef",
    ) -> "dc_td.ListImportTasksOutput":
        return dc_td.ListImportTasksOutput.make_one(res)

    def list_private_graph_endpoints(
        self,
        res: "bs_td.ListPrivateGraphEndpointsOutputTypeDef",
    ) -> "dc_td.ListPrivateGraphEndpointsOutput":
        return dc_td.ListPrivateGraphEndpointsOutput.make_one(res)

    def list_queries(
        self,
        res: "bs_td.ListQueriesOutputTypeDef",
    ) -> "dc_td.ListQueriesOutput":
        return dc_td.ListQueriesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def reset_graph(
        self,
        res: "bs_td.ResetGraphOutputTypeDef",
    ) -> "dc_td.ResetGraphOutput":
        return dc_td.ResetGraphOutput.make_one(res)

    def restore_graph_from_snapshot(
        self,
        res: "bs_td.RestoreGraphFromSnapshotOutputTypeDef",
    ) -> "dc_td.RestoreGraphFromSnapshotOutput":
        return dc_td.RestoreGraphFromSnapshotOutput.make_one(res)

    def start_export_task(
        self,
        res: "bs_td.StartExportTaskOutputTypeDef",
    ) -> "dc_td.StartExportTaskOutput":
        return dc_td.StartExportTaskOutput.make_one(res)

    def start_graph(
        self,
        res: "bs_td.StartGraphOutputTypeDef",
    ) -> "dc_td.StartGraphOutput":
        return dc_td.StartGraphOutput.make_one(res)

    def start_import_task(
        self,
        res: "bs_td.StartImportTaskOutputTypeDef",
    ) -> "dc_td.StartImportTaskOutput":
        return dc_td.StartImportTaskOutput.make_one(res)

    def stop_graph(
        self,
        res: "bs_td.StopGraphOutputTypeDef",
    ) -> "dc_td.StopGraphOutput":
        return dc_td.StopGraphOutput.make_one(res)

    def update_graph(
        self,
        res: "bs_td.UpdateGraphOutputTypeDef",
    ) -> "dc_td.UpdateGraphOutput":
        return dc_td.UpdateGraphOutput.make_one(res)


neptune_graph_caster = NEPTUNE_GRAPHCaster()
