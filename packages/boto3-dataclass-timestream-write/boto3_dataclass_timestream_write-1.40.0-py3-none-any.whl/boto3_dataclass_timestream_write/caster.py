# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_timestream_write import type_defs as bs_td


class TIMESTREAM_WRITECaster:

    def create_batch_load_task(
        self,
        res: "bs_td.CreateBatchLoadTaskResponseTypeDef",
    ) -> "dc_td.CreateBatchLoadTaskResponse":
        return dc_td.CreateBatchLoadTaskResponse.make_one(res)

    def create_database(
        self,
        res: "bs_td.CreateDatabaseResponseTypeDef",
    ) -> "dc_td.CreateDatabaseResponse":
        return dc_td.CreateDatabaseResponse.make_one(res)

    def create_table(
        self,
        res: "bs_td.CreateTableResponseTypeDef",
    ) -> "dc_td.CreateTableResponse":
        return dc_td.CreateTableResponse.make_one(res)

    def delete_database(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_table(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_batch_load_task(
        self,
        res: "bs_td.DescribeBatchLoadTaskResponseTypeDef",
    ) -> "dc_td.DescribeBatchLoadTaskResponse":
        return dc_td.DescribeBatchLoadTaskResponse.make_one(res)

    def describe_database(
        self,
        res: "bs_td.DescribeDatabaseResponseTypeDef",
    ) -> "dc_td.DescribeDatabaseResponse":
        return dc_td.DescribeDatabaseResponse.make_one(res)

    def describe_endpoints(
        self,
        res: "bs_td.DescribeEndpointsResponseTypeDef",
    ) -> "dc_td.DescribeEndpointsResponse":
        return dc_td.DescribeEndpointsResponse.make_one(res)

    def describe_table(
        self,
        res: "bs_td.DescribeTableResponseTypeDef",
    ) -> "dc_td.DescribeTableResponse":
        return dc_td.DescribeTableResponse.make_one(res)

    def list_batch_load_tasks(
        self,
        res: "bs_td.ListBatchLoadTasksResponseTypeDef",
    ) -> "dc_td.ListBatchLoadTasksResponse":
        return dc_td.ListBatchLoadTasksResponse.make_one(res)

    def list_databases(
        self,
        res: "bs_td.ListDatabasesResponseTypeDef",
    ) -> "dc_td.ListDatabasesResponse":
        return dc_td.ListDatabasesResponse.make_one(res)

    def list_tables(
        self,
        res: "bs_td.ListTablesResponseTypeDef",
    ) -> "dc_td.ListTablesResponse":
        return dc_td.ListTablesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def update_database(
        self,
        res: "bs_td.UpdateDatabaseResponseTypeDef",
    ) -> "dc_td.UpdateDatabaseResponse":
        return dc_td.UpdateDatabaseResponse.make_one(res)

    def update_table(
        self,
        res: "bs_td.UpdateTableResponseTypeDef",
    ) -> "dc_td.UpdateTableResponse":
        return dc_td.UpdateTableResponse.make_one(res)

    def write_records(
        self,
        res: "bs_td.WriteRecordsResponseTypeDef",
    ) -> "dc_td.WriteRecordsResponse":
        return dc_td.WriteRecordsResponse.make_one(res)


timestream_write_caster = TIMESTREAM_WRITECaster()
