# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_timestream_influxdb import type_defs as bs_td


class TIMESTREAM_INFLUXDBCaster:

    def create_db_cluster(
        self,
        res: "bs_td.CreateDbClusterOutputTypeDef",
    ) -> "dc_td.CreateDbClusterOutput":
        return dc_td.CreateDbClusterOutput.make_one(res)

    def create_db_instance(
        self,
        res: "bs_td.CreateDbInstanceOutputTypeDef",
    ) -> "dc_td.CreateDbInstanceOutput":
        return dc_td.CreateDbInstanceOutput.make_one(res)

    def create_db_parameter_group(
        self,
        res: "bs_td.CreateDbParameterGroupOutputTypeDef",
    ) -> "dc_td.CreateDbParameterGroupOutput":
        return dc_td.CreateDbParameterGroupOutput.make_one(res)

    def delete_db_cluster(
        self,
        res: "bs_td.DeleteDbClusterOutputTypeDef",
    ) -> "dc_td.DeleteDbClusterOutput":
        return dc_td.DeleteDbClusterOutput.make_one(res)

    def delete_db_instance(
        self,
        res: "bs_td.DeleteDbInstanceOutputTypeDef",
    ) -> "dc_td.DeleteDbInstanceOutput":
        return dc_td.DeleteDbInstanceOutput.make_one(res)

    def get_db_cluster(
        self,
        res: "bs_td.GetDbClusterOutputTypeDef",
    ) -> "dc_td.GetDbClusterOutput":
        return dc_td.GetDbClusterOutput.make_one(res)

    def get_db_instance(
        self,
        res: "bs_td.GetDbInstanceOutputTypeDef",
    ) -> "dc_td.GetDbInstanceOutput":
        return dc_td.GetDbInstanceOutput.make_one(res)

    def get_db_parameter_group(
        self,
        res: "bs_td.GetDbParameterGroupOutputTypeDef",
    ) -> "dc_td.GetDbParameterGroupOutput":
        return dc_td.GetDbParameterGroupOutput.make_one(res)

    def list_db_clusters(
        self,
        res: "bs_td.ListDbClustersOutputTypeDef",
    ) -> "dc_td.ListDbClustersOutput":
        return dc_td.ListDbClustersOutput.make_one(res)

    def list_db_instances(
        self,
        res: "bs_td.ListDbInstancesOutputTypeDef",
    ) -> "dc_td.ListDbInstancesOutput":
        return dc_td.ListDbInstancesOutput.make_one(res)

    def list_db_instances_for_cluster(
        self,
        res: "bs_td.ListDbInstancesForClusterOutputTypeDef",
    ) -> "dc_td.ListDbInstancesForClusterOutput":
        return dc_td.ListDbInstancesForClusterOutput.make_one(res)

    def list_db_parameter_groups(
        self,
        res: "bs_td.ListDbParameterGroupsOutputTypeDef",
    ) -> "dc_td.ListDbParameterGroupsOutput":
        return dc_td.ListDbParameterGroupsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_db_cluster(
        self,
        res: "bs_td.UpdateDbClusterOutputTypeDef",
    ) -> "dc_td.UpdateDbClusterOutput":
        return dc_td.UpdateDbClusterOutput.make_one(res)

    def update_db_instance(
        self,
        res: "bs_td.UpdateDbInstanceOutputTypeDef",
    ) -> "dc_td.UpdateDbInstanceOutput":
        return dc_td.UpdateDbInstanceOutput.make_one(res)


timestream_influxdb_caster = TIMESTREAM_INFLUXDBCaster()
