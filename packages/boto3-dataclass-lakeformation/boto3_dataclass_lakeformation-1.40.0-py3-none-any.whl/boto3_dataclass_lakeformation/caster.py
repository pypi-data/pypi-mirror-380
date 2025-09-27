# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_lakeformation import type_defs as bs_td


class LAKEFORMATIONCaster:

    def add_lf_tags_to_resource(
        self,
        res: "bs_td.AddLFTagsToResourceResponseTypeDef",
    ) -> "dc_td.AddLFTagsToResourceResponse":
        return dc_td.AddLFTagsToResourceResponse.make_one(res)

    def assume_decorated_role_with_saml(
        self,
        res: "bs_td.AssumeDecoratedRoleWithSAMLResponseTypeDef",
    ) -> "dc_td.AssumeDecoratedRoleWithSAMLResponse":
        return dc_td.AssumeDecoratedRoleWithSAMLResponse.make_one(res)

    def batch_grant_permissions(
        self,
        res: "bs_td.BatchGrantPermissionsResponseTypeDef",
    ) -> "dc_td.BatchGrantPermissionsResponse":
        return dc_td.BatchGrantPermissionsResponse.make_one(res)

    def batch_revoke_permissions(
        self,
        res: "bs_td.BatchRevokePermissionsResponseTypeDef",
    ) -> "dc_td.BatchRevokePermissionsResponse":
        return dc_td.BatchRevokePermissionsResponse.make_one(res)

    def commit_transaction(
        self,
        res: "bs_td.CommitTransactionResponseTypeDef",
    ) -> "dc_td.CommitTransactionResponse":
        return dc_td.CommitTransactionResponse.make_one(res)

    def create_lake_formation_identity_center_configuration(
        self,
        res: "bs_td.CreateLakeFormationIdentityCenterConfigurationResponseTypeDef",
    ) -> "dc_td.CreateLakeFormationIdentityCenterConfigurationResponse":
        return dc_td.CreateLakeFormationIdentityCenterConfigurationResponse.make_one(
            res
        )

    def describe_lake_formation_identity_center_configuration(
        self,
        res: "bs_td.DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeLakeFormationIdentityCenterConfigurationResponse":
        return dc_td.DescribeLakeFormationIdentityCenterConfigurationResponse.make_one(
            res
        )

    def describe_resource(
        self,
        res: "bs_td.DescribeResourceResponseTypeDef",
    ) -> "dc_td.DescribeResourceResponse":
        return dc_td.DescribeResourceResponse.make_one(res)

    def describe_transaction(
        self,
        res: "bs_td.DescribeTransactionResponseTypeDef",
    ) -> "dc_td.DescribeTransactionResponse":
        return dc_td.DescribeTransactionResponse.make_one(res)

    def get_data_cells_filter(
        self,
        res: "bs_td.GetDataCellsFilterResponseTypeDef",
    ) -> "dc_td.GetDataCellsFilterResponse":
        return dc_td.GetDataCellsFilterResponse.make_one(res)

    def get_data_lake_principal(
        self,
        res: "bs_td.GetDataLakePrincipalResponseTypeDef",
    ) -> "dc_td.GetDataLakePrincipalResponse":
        return dc_td.GetDataLakePrincipalResponse.make_one(res)

    def get_data_lake_settings(
        self,
        res: "bs_td.GetDataLakeSettingsResponseTypeDef",
    ) -> "dc_td.GetDataLakeSettingsResponse":
        return dc_td.GetDataLakeSettingsResponse.make_one(res)

    def get_effective_permissions_for_path(
        self,
        res: "bs_td.GetEffectivePermissionsForPathResponseTypeDef",
    ) -> "dc_td.GetEffectivePermissionsForPathResponse":
        return dc_td.GetEffectivePermissionsForPathResponse.make_one(res)

    def get_lf_tag(
        self,
        res: "bs_td.GetLFTagResponseTypeDef",
    ) -> "dc_td.GetLFTagResponse":
        return dc_td.GetLFTagResponse.make_one(res)

    def get_lf_tag_expression(
        self,
        res: "bs_td.GetLFTagExpressionResponseTypeDef",
    ) -> "dc_td.GetLFTagExpressionResponse":
        return dc_td.GetLFTagExpressionResponse.make_one(res)

    def get_query_state(
        self,
        res: "bs_td.GetQueryStateResponseTypeDef",
    ) -> "dc_td.GetQueryStateResponse":
        return dc_td.GetQueryStateResponse.make_one(res)

    def get_query_statistics(
        self,
        res: "bs_td.GetQueryStatisticsResponseTypeDef",
    ) -> "dc_td.GetQueryStatisticsResponse":
        return dc_td.GetQueryStatisticsResponse.make_one(res)

    def get_resource_lf_tags(
        self,
        res: "bs_td.GetResourceLFTagsResponseTypeDef",
    ) -> "dc_td.GetResourceLFTagsResponse":
        return dc_td.GetResourceLFTagsResponse.make_one(res)

    def get_table_objects(
        self,
        res: "bs_td.GetTableObjectsResponseTypeDef",
    ) -> "dc_td.GetTableObjectsResponse":
        return dc_td.GetTableObjectsResponse.make_one(res)

    def get_temporary_glue_partition_credentials(
        self,
        res: "bs_td.GetTemporaryGluePartitionCredentialsResponseTypeDef",
    ) -> "dc_td.GetTemporaryGluePartitionCredentialsResponse":
        return dc_td.GetTemporaryGluePartitionCredentialsResponse.make_one(res)

    def get_temporary_glue_table_credentials(
        self,
        res: "bs_td.GetTemporaryGlueTableCredentialsResponseTypeDef",
    ) -> "dc_td.GetTemporaryGlueTableCredentialsResponse":
        return dc_td.GetTemporaryGlueTableCredentialsResponse.make_one(res)

    def get_work_unit_results(
        self,
        res: "bs_td.GetWorkUnitResultsResponseTypeDef",
    ) -> "dc_td.GetWorkUnitResultsResponse":
        return dc_td.GetWorkUnitResultsResponse.make_one(res)

    def get_work_units(
        self,
        res: "bs_td.GetWorkUnitsResponseTypeDef",
    ) -> "dc_td.GetWorkUnitsResponse":
        return dc_td.GetWorkUnitsResponse.make_one(res)

    def list_data_cells_filter(
        self,
        res: "bs_td.ListDataCellsFilterResponseTypeDef",
    ) -> "dc_td.ListDataCellsFilterResponse":
        return dc_td.ListDataCellsFilterResponse.make_one(res)

    def list_lf_tag_expressions(
        self,
        res: "bs_td.ListLFTagExpressionsResponseTypeDef",
    ) -> "dc_td.ListLFTagExpressionsResponse":
        return dc_td.ListLFTagExpressionsResponse.make_one(res)

    def list_lf_tags(
        self,
        res: "bs_td.ListLFTagsResponseTypeDef",
    ) -> "dc_td.ListLFTagsResponse":
        return dc_td.ListLFTagsResponse.make_one(res)

    def list_lake_formation_opt_ins(
        self,
        res: "bs_td.ListLakeFormationOptInsResponseTypeDef",
    ) -> "dc_td.ListLakeFormationOptInsResponse":
        return dc_td.ListLakeFormationOptInsResponse.make_one(res)

    def list_permissions(
        self,
        res: "bs_td.ListPermissionsResponseTypeDef",
    ) -> "dc_td.ListPermissionsResponse":
        return dc_td.ListPermissionsResponse.make_one(res)

    def list_resources(
        self,
        res: "bs_td.ListResourcesResponseTypeDef",
    ) -> "dc_td.ListResourcesResponse":
        return dc_td.ListResourcesResponse.make_one(res)

    def list_table_storage_optimizers(
        self,
        res: "bs_td.ListTableStorageOptimizersResponseTypeDef",
    ) -> "dc_td.ListTableStorageOptimizersResponse":
        return dc_td.ListTableStorageOptimizersResponse.make_one(res)

    def list_transactions(
        self,
        res: "bs_td.ListTransactionsResponseTypeDef",
    ) -> "dc_td.ListTransactionsResponse":
        return dc_td.ListTransactionsResponse.make_one(res)

    def remove_lf_tags_from_resource(
        self,
        res: "bs_td.RemoveLFTagsFromResourceResponseTypeDef",
    ) -> "dc_td.RemoveLFTagsFromResourceResponse":
        return dc_td.RemoveLFTagsFromResourceResponse.make_one(res)

    def search_databases_by_lf_tags(
        self,
        res: "bs_td.SearchDatabasesByLFTagsResponseTypeDef",
    ) -> "dc_td.SearchDatabasesByLFTagsResponse":
        return dc_td.SearchDatabasesByLFTagsResponse.make_one(res)

    def search_tables_by_lf_tags(
        self,
        res: "bs_td.SearchTablesByLFTagsResponseTypeDef",
    ) -> "dc_td.SearchTablesByLFTagsResponse":
        return dc_td.SearchTablesByLFTagsResponse.make_one(res)

    def start_query_planning(
        self,
        res: "bs_td.StartQueryPlanningResponseTypeDef",
    ) -> "dc_td.StartQueryPlanningResponse":
        return dc_td.StartQueryPlanningResponse.make_one(res)

    def start_transaction(
        self,
        res: "bs_td.StartTransactionResponseTypeDef",
    ) -> "dc_td.StartTransactionResponse":
        return dc_td.StartTransactionResponse.make_one(res)

    def update_table_storage_optimizer(
        self,
        res: "bs_td.UpdateTableStorageOptimizerResponseTypeDef",
    ) -> "dc_td.UpdateTableStorageOptimizerResponse":
        return dc_td.UpdateTableStorageOptimizerResponse.make_one(res)


lakeformation_caster = LAKEFORMATIONCaster()
