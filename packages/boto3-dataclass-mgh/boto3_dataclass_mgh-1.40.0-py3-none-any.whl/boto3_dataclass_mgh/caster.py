# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_mgh import type_defs as bs_td


class MGHCaster:

    def describe_application_state(
        self,
        res: "bs_td.DescribeApplicationStateResultTypeDef",
    ) -> "dc_td.DescribeApplicationStateResult":
        return dc_td.DescribeApplicationStateResult.make_one(res)

    def describe_migration_task(
        self,
        res: "bs_td.DescribeMigrationTaskResultTypeDef",
    ) -> "dc_td.DescribeMigrationTaskResult":
        return dc_td.DescribeMigrationTaskResult.make_one(res)

    def list_application_states(
        self,
        res: "bs_td.ListApplicationStatesResultTypeDef",
    ) -> "dc_td.ListApplicationStatesResult":
        return dc_td.ListApplicationStatesResult.make_one(res)

    def list_created_artifacts(
        self,
        res: "bs_td.ListCreatedArtifactsResultTypeDef",
    ) -> "dc_td.ListCreatedArtifactsResult":
        return dc_td.ListCreatedArtifactsResult.make_one(res)

    def list_discovered_resources(
        self,
        res: "bs_td.ListDiscoveredResourcesResultTypeDef",
    ) -> "dc_td.ListDiscoveredResourcesResult":
        return dc_td.ListDiscoveredResourcesResult.make_one(res)

    def list_migration_task_updates(
        self,
        res: "bs_td.ListMigrationTaskUpdatesResultTypeDef",
    ) -> "dc_td.ListMigrationTaskUpdatesResult":
        return dc_td.ListMigrationTaskUpdatesResult.make_one(res)

    def list_migration_tasks(
        self,
        res: "bs_td.ListMigrationTasksResultTypeDef",
    ) -> "dc_td.ListMigrationTasksResult":
        return dc_td.ListMigrationTasksResult.make_one(res)

    def list_progress_update_streams(
        self,
        res: "bs_td.ListProgressUpdateStreamsResultTypeDef",
    ) -> "dc_td.ListProgressUpdateStreamsResult":
        return dc_td.ListProgressUpdateStreamsResult.make_one(res)

    def list_source_resources(
        self,
        res: "bs_td.ListSourceResourcesResultTypeDef",
    ) -> "dc_td.ListSourceResourcesResult":
        return dc_td.ListSourceResourcesResult.make_one(res)


mgh_caster = MGHCaster()
