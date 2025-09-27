# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotevents_data import type_defs as bs_td


class IOTEVENTS_DATACaster:

    def batch_acknowledge_alarm(
        self,
        res: "bs_td.BatchAcknowledgeAlarmResponseTypeDef",
    ) -> "dc_td.BatchAcknowledgeAlarmResponse":
        return dc_td.BatchAcknowledgeAlarmResponse.make_one(res)

    def batch_delete_detector(
        self,
        res: "bs_td.BatchDeleteDetectorResponseTypeDef",
    ) -> "dc_td.BatchDeleteDetectorResponse":
        return dc_td.BatchDeleteDetectorResponse.make_one(res)

    def batch_disable_alarm(
        self,
        res: "bs_td.BatchDisableAlarmResponseTypeDef",
    ) -> "dc_td.BatchDisableAlarmResponse":
        return dc_td.BatchDisableAlarmResponse.make_one(res)

    def batch_enable_alarm(
        self,
        res: "bs_td.BatchEnableAlarmResponseTypeDef",
    ) -> "dc_td.BatchEnableAlarmResponse":
        return dc_td.BatchEnableAlarmResponse.make_one(res)

    def batch_put_message(
        self,
        res: "bs_td.BatchPutMessageResponseTypeDef",
    ) -> "dc_td.BatchPutMessageResponse":
        return dc_td.BatchPutMessageResponse.make_one(res)

    def batch_reset_alarm(
        self,
        res: "bs_td.BatchResetAlarmResponseTypeDef",
    ) -> "dc_td.BatchResetAlarmResponse":
        return dc_td.BatchResetAlarmResponse.make_one(res)

    def batch_snooze_alarm(
        self,
        res: "bs_td.BatchSnoozeAlarmResponseTypeDef",
    ) -> "dc_td.BatchSnoozeAlarmResponse":
        return dc_td.BatchSnoozeAlarmResponse.make_one(res)

    def batch_update_detector(
        self,
        res: "bs_td.BatchUpdateDetectorResponseTypeDef",
    ) -> "dc_td.BatchUpdateDetectorResponse":
        return dc_td.BatchUpdateDetectorResponse.make_one(res)

    def describe_alarm(
        self,
        res: "bs_td.DescribeAlarmResponseTypeDef",
    ) -> "dc_td.DescribeAlarmResponse":
        return dc_td.DescribeAlarmResponse.make_one(res)

    def describe_detector(
        self,
        res: "bs_td.DescribeDetectorResponseTypeDef",
    ) -> "dc_td.DescribeDetectorResponse":
        return dc_td.DescribeDetectorResponse.make_one(res)

    def list_alarms(
        self,
        res: "bs_td.ListAlarmsResponseTypeDef",
    ) -> "dc_td.ListAlarmsResponse":
        return dc_td.ListAlarmsResponse.make_one(res)

    def list_detectors(
        self,
        res: "bs_td.ListDetectorsResponseTypeDef",
    ) -> "dc_td.ListDetectorsResponse":
        return dc_td.ListDetectorsResponse.make_one(res)


iotevents_data_caster = IOTEVENTS_DATACaster()
