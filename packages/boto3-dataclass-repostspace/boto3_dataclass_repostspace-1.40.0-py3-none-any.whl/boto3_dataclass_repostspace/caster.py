# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_repostspace import type_defs as bs_td


class REPOSTSPACECaster:

    def batch_add_channel_role_to_accessors(
        self,
        res: "bs_td.BatchAddChannelRoleToAccessorsOutputTypeDef",
    ) -> "dc_td.BatchAddChannelRoleToAccessorsOutput":
        return dc_td.BatchAddChannelRoleToAccessorsOutput.make_one(res)

    def batch_add_role(
        self,
        res: "bs_td.BatchAddRoleOutputTypeDef",
    ) -> "dc_td.BatchAddRoleOutput":
        return dc_td.BatchAddRoleOutput.make_one(res)

    def batch_remove_channel_role_from_accessors(
        self,
        res: "bs_td.BatchRemoveChannelRoleFromAccessorsOutputTypeDef",
    ) -> "dc_td.BatchRemoveChannelRoleFromAccessorsOutput":
        return dc_td.BatchRemoveChannelRoleFromAccessorsOutput.make_one(res)

    def batch_remove_role(
        self,
        res: "bs_td.BatchRemoveRoleOutputTypeDef",
    ) -> "dc_td.BatchRemoveRoleOutput":
        return dc_td.BatchRemoveRoleOutput.make_one(res)

    def create_channel(
        self,
        res: "bs_td.CreateChannelOutputTypeDef",
    ) -> "dc_td.CreateChannelOutput":
        return dc_td.CreateChannelOutput.make_one(res)

    def create_space(
        self,
        res: "bs_td.CreateSpaceOutputTypeDef",
    ) -> "dc_td.CreateSpaceOutput":
        return dc_td.CreateSpaceOutput.make_one(res)

    def delete_space(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deregister_admin(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_channel(
        self,
        res: "bs_td.GetChannelOutputTypeDef",
    ) -> "dc_td.GetChannelOutput":
        return dc_td.GetChannelOutput.make_one(res)

    def get_space(
        self,
        res: "bs_td.GetSpaceOutputTypeDef",
    ) -> "dc_td.GetSpaceOutput":
        return dc_td.GetSpaceOutput.make_one(res)

    def list_channels(
        self,
        res: "bs_td.ListChannelsOutputTypeDef",
    ) -> "dc_td.ListChannelsOutput":
        return dc_td.ListChannelsOutput.make_one(res)

    def list_spaces(
        self,
        res: "bs_td.ListSpacesOutputTypeDef",
    ) -> "dc_td.ListSpacesOutput":
        return dc_td.ListSpacesOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def register_admin(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def send_invites(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_space(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


repostspace_caster = REPOSTSPACECaster()
