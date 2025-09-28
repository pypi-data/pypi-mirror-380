# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_opsworkscm import type_defs as bs_td


class OPSWORKSCMCaster:

    def associate_node(
        self,
        res: "bs_td.AssociateNodeResponseTypeDef",
    ) -> "dc_td.AssociateNodeResponse":
        return dc_td.AssociateNodeResponse.make_one(res)

    def create_backup(
        self,
        res: "bs_td.CreateBackupResponseTypeDef",
    ) -> "dc_td.CreateBackupResponse":
        return dc_td.CreateBackupResponse.make_one(res)

    def create_server(
        self,
        res: "bs_td.CreateServerResponseTypeDef",
    ) -> "dc_td.CreateServerResponse":
        return dc_td.CreateServerResponse.make_one(res)

    def describe_account_attributes(
        self,
        res: "bs_td.DescribeAccountAttributesResponseTypeDef",
    ) -> "dc_td.DescribeAccountAttributesResponse":
        return dc_td.DescribeAccountAttributesResponse.make_one(res)

    def describe_backups(
        self,
        res: "bs_td.DescribeBackupsResponseTypeDef",
    ) -> "dc_td.DescribeBackupsResponse":
        return dc_td.DescribeBackupsResponse.make_one(res)

    def describe_events(
        self,
        res: "bs_td.DescribeEventsResponseTypeDef",
    ) -> "dc_td.DescribeEventsResponse":
        return dc_td.DescribeEventsResponse.make_one(res)

    def describe_node_association_status(
        self,
        res: "bs_td.DescribeNodeAssociationStatusResponseTypeDef",
    ) -> "dc_td.DescribeNodeAssociationStatusResponse":
        return dc_td.DescribeNodeAssociationStatusResponse.make_one(res)

    def describe_servers(
        self,
        res: "bs_td.DescribeServersResponseTypeDef",
    ) -> "dc_td.DescribeServersResponse":
        return dc_td.DescribeServersResponse.make_one(res)

    def disassociate_node(
        self,
        res: "bs_td.DisassociateNodeResponseTypeDef",
    ) -> "dc_td.DisassociateNodeResponse":
        return dc_td.DisassociateNodeResponse.make_one(res)

    def export_server_engine_attribute(
        self,
        res: "bs_td.ExportServerEngineAttributeResponseTypeDef",
    ) -> "dc_td.ExportServerEngineAttributeResponse":
        return dc_td.ExportServerEngineAttributeResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def restore_server(
        self,
        res: "bs_td.RestoreServerResponseTypeDef",
    ) -> "dc_td.RestoreServerResponse":
        return dc_td.RestoreServerResponse.make_one(res)

    def start_maintenance(
        self,
        res: "bs_td.StartMaintenanceResponseTypeDef",
    ) -> "dc_td.StartMaintenanceResponse":
        return dc_td.StartMaintenanceResponse.make_one(res)

    def update_server(
        self,
        res: "bs_td.UpdateServerResponseTypeDef",
    ) -> "dc_td.UpdateServerResponse":
        return dc_td.UpdateServerResponse.make_one(res)

    def update_server_engine_attributes(
        self,
        res: "bs_td.UpdateServerEngineAttributesResponseTypeDef",
    ) -> "dc_td.UpdateServerEngineAttributesResponse":
        return dc_td.UpdateServerEngineAttributesResponse.make_one(res)


opsworkscm_caster = OPSWORKSCMCaster()
