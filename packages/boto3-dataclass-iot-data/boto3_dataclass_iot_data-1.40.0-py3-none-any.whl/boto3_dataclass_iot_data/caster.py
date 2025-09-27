# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iot_data import type_defs as bs_td


class IOT_DATACaster:

    def delete_connection(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_thing_shadow(
        self,
        res: "bs_td.DeleteThingShadowResponseTypeDef",
    ) -> "dc_td.DeleteThingShadowResponse":
        return dc_td.DeleteThingShadowResponse.make_one(res)

    def get_retained_message(
        self,
        res: "bs_td.GetRetainedMessageResponseTypeDef",
    ) -> "dc_td.GetRetainedMessageResponse":
        return dc_td.GetRetainedMessageResponse.make_one(res)

    def get_thing_shadow(
        self,
        res: "bs_td.GetThingShadowResponseTypeDef",
    ) -> "dc_td.GetThingShadowResponse":
        return dc_td.GetThingShadowResponse.make_one(res)

    def list_named_shadows_for_thing(
        self,
        res: "bs_td.ListNamedShadowsForThingResponseTypeDef",
    ) -> "dc_td.ListNamedShadowsForThingResponse":
        return dc_td.ListNamedShadowsForThingResponse.make_one(res)

    def list_retained_messages(
        self,
        res: "bs_td.ListRetainedMessagesResponseTypeDef",
    ) -> "dc_td.ListRetainedMessagesResponse":
        return dc_td.ListRetainedMessagesResponse.make_one(res)

    def publish(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_thing_shadow(
        self,
        res: "bs_td.UpdateThingShadowResponseTypeDef",
    ) -> "dc_td.UpdateThingShadowResponse":
        return dc_td.UpdateThingShadowResponse.make_one(res)


iot_data_caster = IOT_DATACaster()
