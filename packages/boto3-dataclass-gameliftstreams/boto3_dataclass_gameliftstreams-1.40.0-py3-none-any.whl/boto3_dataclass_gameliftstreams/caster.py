# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_gameliftstreams import type_defs as bs_td


class GAMELIFTSTREAMSCaster:

    def add_stream_group_locations(
        self,
        res: "bs_td.AddStreamGroupLocationsOutputTypeDef",
    ) -> "dc_td.AddStreamGroupLocationsOutput":
        return dc_td.AddStreamGroupLocationsOutput.make_one(res)

    def associate_applications(
        self,
        res: "bs_td.AssociateApplicationsOutputTypeDef",
    ) -> "dc_td.AssociateApplicationsOutput":
        return dc_td.AssociateApplicationsOutput.make_one(res)

    def create_application(
        self,
        res: "bs_td.CreateApplicationOutputTypeDef",
    ) -> "dc_td.CreateApplicationOutput":
        return dc_td.CreateApplicationOutput.make_one(res)

    def create_stream_group(
        self,
        res: "bs_td.CreateStreamGroupOutputTypeDef",
    ) -> "dc_td.CreateStreamGroupOutput":
        return dc_td.CreateStreamGroupOutput.make_one(res)

    def create_stream_session_connection(
        self,
        res: "bs_td.CreateStreamSessionConnectionOutputTypeDef",
    ) -> "dc_td.CreateStreamSessionConnectionOutput":
        return dc_td.CreateStreamSessionConnectionOutput.make_one(res)

    def delete_application(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_stream_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_applications(
        self,
        res: "bs_td.DisassociateApplicationsOutputTypeDef",
    ) -> "dc_td.DisassociateApplicationsOutput":
        return dc_td.DisassociateApplicationsOutput.make_one(res)

    def get_application(
        self,
        res: "bs_td.GetApplicationOutputTypeDef",
    ) -> "dc_td.GetApplicationOutput":
        return dc_td.GetApplicationOutput.make_one(res)

    def get_stream_group(
        self,
        res: "bs_td.GetStreamGroupOutputTypeDef",
    ) -> "dc_td.GetStreamGroupOutput":
        return dc_td.GetStreamGroupOutput.make_one(res)

    def get_stream_session(
        self,
        res: "bs_td.GetStreamSessionOutputTypeDef",
    ) -> "dc_td.GetStreamSessionOutput":
        return dc_td.GetStreamSessionOutput.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsOutputTypeDef",
    ) -> "dc_td.ListApplicationsOutput":
        return dc_td.ListApplicationsOutput.make_one(res)

    def list_stream_groups(
        self,
        res: "bs_td.ListStreamGroupsOutputTypeDef",
    ) -> "dc_td.ListStreamGroupsOutput":
        return dc_td.ListStreamGroupsOutput.make_one(res)

    def list_stream_sessions(
        self,
        res: "bs_td.ListStreamSessionsOutputTypeDef",
    ) -> "dc_td.ListStreamSessionsOutput":
        return dc_td.ListStreamSessionsOutput.make_one(res)

    def list_stream_sessions_by_account(
        self,
        res: "bs_td.ListStreamSessionsByAccountOutputTypeDef",
    ) -> "dc_td.ListStreamSessionsByAccountOutput":
        return dc_td.ListStreamSessionsByAccountOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def remove_stream_group_locations(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_stream_session(
        self,
        res: "bs_td.StartStreamSessionOutputTypeDef",
    ) -> "dc_td.StartStreamSessionOutput":
        return dc_td.StartStreamSessionOutput.make_one(res)

    def terminate_stream_session(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_application(
        self,
        res: "bs_td.UpdateApplicationOutputTypeDef",
    ) -> "dc_td.UpdateApplicationOutput":
        return dc_td.UpdateApplicationOutput.make_one(res)

    def update_stream_group(
        self,
        res: "bs_td.UpdateStreamGroupOutputTypeDef",
    ) -> "dc_td.UpdateStreamGroupOutput":
        return dc_td.UpdateStreamGroupOutput.make_one(res)


gameliftstreams_caster = GAMELIFTSTREAMSCaster()
