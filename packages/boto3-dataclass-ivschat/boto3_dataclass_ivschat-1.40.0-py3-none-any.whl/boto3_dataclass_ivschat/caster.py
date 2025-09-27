# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ivschat import type_defs as bs_td


class IVSCHATCaster:

    def create_chat_token(
        self,
        res: "bs_td.CreateChatTokenResponseTypeDef",
    ) -> "dc_td.CreateChatTokenResponse":
        return dc_td.CreateChatTokenResponse.make_one(res)

    def create_logging_configuration(
        self,
        res: "bs_td.CreateLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.CreateLoggingConfigurationResponse":
        return dc_td.CreateLoggingConfigurationResponse.make_one(res)

    def create_room(
        self,
        res: "bs_td.CreateRoomResponseTypeDef",
    ) -> "dc_td.CreateRoomResponse":
        return dc_td.CreateRoomResponse.make_one(res)

    def delete_logging_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_message(
        self,
        res: "bs_td.DeleteMessageResponseTypeDef",
    ) -> "dc_td.DeleteMessageResponse":
        return dc_td.DeleteMessageResponse.make_one(res)

    def delete_room(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_logging_configuration(
        self,
        res: "bs_td.GetLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.GetLoggingConfigurationResponse":
        return dc_td.GetLoggingConfigurationResponse.make_one(res)

    def get_room(
        self,
        res: "bs_td.GetRoomResponseTypeDef",
    ) -> "dc_td.GetRoomResponse":
        return dc_td.GetRoomResponse.make_one(res)

    def list_logging_configurations(
        self,
        res: "bs_td.ListLoggingConfigurationsResponseTypeDef",
    ) -> "dc_td.ListLoggingConfigurationsResponse":
        return dc_td.ListLoggingConfigurationsResponse.make_one(res)

    def list_rooms(
        self,
        res: "bs_td.ListRoomsResponseTypeDef",
    ) -> "dc_td.ListRoomsResponse":
        return dc_td.ListRoomsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def send_event(
        self,
        res: "bs_td.SendEventResponseTypeDef",
    ) -> "dc_td.SendEventResponse":
        return dc_td.SendEventResponse.make_one(res)

    def update_logging_configuration(
        self,
        res: "bs_td.UpdateLoggingConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateLoggingConfigurationResponse":
        return dc_td.UpdateLoggingConfigurationResponse.make_one(res)

    def update_room(
        self,
        res: "bs_td.UpdateRoomResponseTypeDef",
    ) -> "dc_td.UpdateRoomResponse":
        return dc_td.UpdateRoomResponse.make_one(res)


ivschat_caster = IVSCHATCaster()
