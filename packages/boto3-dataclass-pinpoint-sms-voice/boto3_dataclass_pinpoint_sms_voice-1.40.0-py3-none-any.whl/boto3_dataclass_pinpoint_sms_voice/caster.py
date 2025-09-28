# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_pinpoint_sms_voice import type_defs as bs_td


class PINPOINT_SMS_VOICECaster:

    def get_configuration_set_event_destinations(
        self,
        res: "bs_td.GetConfigurationSetEventDestinationsResponseTypeDef",
    ) -> "dc_td.GetConfigurationSetEventDestinationsResponse":
        return dc_td.GetConfigurationSetEventDestinationsResponse.make_one(res)

    def list_configuration_sets(
        self,
        res: "bs_td.ListConfigurationSetsResponseTypeDef",
    ) -> "dc_td.ListConfigurationSetsResponse":
        return dc_td.ListConfigurationSetsResponse.make_one(res)

    def send_voice_message(
        self,
        res: "bs_td.SendVoiceMessageResponseTypeDef",
    ) -> "dc_td.SendVoiceMessageResponse":
        return dc_td.SendVoiceMessageResponse.make_one(res)


pinpoint_sms_voice_caster = PINPOINT_SMS_VOICECaster()
