# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_keyspaces import type_defs as bs_td


class KEYSPACESCaster:

    def create_keyspace(
        self,
        res: "bs_td.CreateKeyspaceResponseTypeDef",
    ) -> "dc_td.CreateKeyspaceResponse":
        return dc_td.CreateKeyspaceResponse.make_one(res)

    def create_table(
        self,
        res: "bs_td.CreateTableResponseTypeDef",
    ) -> "dc_td.CreateTableResponse":
        return dc_td.CreateTableResponse.make_one(res)

    def create_type(
        self,
        res: "bs_td.CreateTypeResponseTypeDef",
    ) -> "dc_td.CreateTypeResponse":
        return dc_td.CreateTypeResponse.make_one(res)

    def delete_type(
        self,
        res: "bs_td.DeleteTypeResponseTypeDef",
    ) -> "dc_td.DeleteTypeResponse":
        return dc_td.DeleteTypeResponse.make_one(res)

    def get_keyspace(
        self,
        res: "bs_td.GetKeyspaceResponseTypeDef",
    ) -> "dc_td.GetKeyspaceResponse":
        return dc_td.GetKeyspaceResponse.make_one(res)

    def get_table(
        self,
        res: "bs_td.GetTableResponseTypeDef",
    ) -> "dc_td.GetTableResponse":
        return dc_td.GetTableResponse.make_one(res)

    def get_table_auto_scaling_settings(
        self,
        res: "bs_td.GetTableAutoScalingSettingsResponseTypeDef",
    ) -> "dc_td.GetTableAutoScalingSettingsResponse":
        return dc_td.GetTableAutoScalingSettingsResponse.make_one(res)

    def get_type(
        self,
        res: "bs_td.GetTypeResponseTypeDef",
    ) -> "dc_td.GetTypeResponse":
        return dc_td.GetTypeResponse.make_one(res)

    def list_keyspaces(
        self,
        res: "bs_td.ListKeyspacesResponseTypeDef",
    ) -> "dc_td.ListKeyspacesResponse":
        return dc_td.ListKeyspacesResponse.make_one(res)

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

    def list_types(
        self,
        res: "bs_td.ListTypesResponseTypeDef",
    ) -> "dc_td.ListTypesResponse":
        return dc_td.ListTypesResponse.make_one(res)

    def restore_table(
        self,
        res: "bs_td.RestoreTableResponseTypeDef",
    ) -> "dc_td.RestoreTableResponse":
        return dc_td.RestoreTableResponse.make_one(res)

    def update_keyspace(
        self,
        res: "bs_td.UpdateKeyspaceResponseTypeDef",
    ) -> "dc_td.UpdateKeyspaceResponse":
        return dc_td.UpdateKeyspaceResponse.make_one(res)

    def update_table(
        self,
        res: "bs_td.UpdateTableResponseTypeDef",
    ) -> "dc_td.UpdateTableResponse":
        return dc_td.UpdateTableResponse.make_one(res)


keyspaces_caster = KEYSPACESCaster()
