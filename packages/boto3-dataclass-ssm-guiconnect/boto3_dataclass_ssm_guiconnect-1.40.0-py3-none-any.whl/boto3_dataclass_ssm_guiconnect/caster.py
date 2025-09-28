# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ssm_guiconnect import type_defs as bs_td


class SSM_GUICONNECTCaster:

    def delete_connection_recording_preferences(
        self,
        res: "bs_td.DeleteConnectionRecordingPreferencesResponseTypeDef",
    ) -> "dc_td.DeleteConnectionRecordingPreferencesResponse":
        return dc_td.DeleteConnectionRecordingPreferencesResponse.make_one(res)

    def get_connection_recording_preferences(
        self,
        res: "bs_td.GetConnectionRecordingPreferencesResponseTypeDef",
    ) -> "dc_td.GetConnectionRecordingPreferencesResponse":
        return dc_td.GetConnectionRecordingPreferencesResponse.make_one(res)

    def update_connection_recording_preferences(
        self,
        res: "bs_td.UpdateConnectionRecordingPreferencesResponseTypeDef",
    ) -> "dc_td.UpdateConnectionRecordingPreferencesResponse":
        return dc_td.UpdateConnectionRecordingPreferencesResponse.make_one(res)


ssm_guiconnect_caster = SSM_GUICONNECTCaster()
