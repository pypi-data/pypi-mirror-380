import logging
from typing import List

from twisted.internet.task import LoopingCall
from vortex.DeferUtil import vortexLogFailure
from vortex.PayloadEndpoint import PayloadEndpoint
from vortex.PayloadEnvelope import PayloadEnvelope
from vortex.VortexFactory import VortexFactory
from vortex.handler.TupleDataActionClient import TupleDataActionClient
from vortex.handler.TupleDataObservableProxyHandler import (
    TupleDataObservableProxyHandler,
)

from peek_core_device._private.PluginNames import deviceActionProcessorName
from peek_core_device._private.PluginNames import deviceFilt
from peek_core_device._private.PluginNames import deviceObservableName
from peek_core_device._private.tuples.UpdateDeviceOnlineAction import (
    UpdateDeviceOnlineAction,
)
from peek_plugin_base.LoopingCallUtil import peekCatchErrbackWithLogger
from peek_plugin_base.PeekVortexUtil import peekServerName

from peek_core_device.tuples.DeviceInfoTuple import DeviceInfoTuple

logger = logging.getLogger(__name__)


def makeDeviceTupleDataObservableProxy():
    return TupleDataObservableProxyHandler(
        observableName=deviceObservableName,
        proxyToVortexName=peekServerName,
        additionalFilt=deviceFilt,
    )


deviceOnlineFilt = dict(key="device.online")
deviceOnlineFilt.update(deviceFilt)


# The sender is located at:
# peek_core_device/plugin-module/_private/device-server.service.ts


class DeviceOnlineController:
    CHECK_TIME = 5.0

    def __init__(self):
        self._ep = PayloadEndpoint(deviceOnlineFilt, self._process)
        self._onlineDeviceIdsByUuid = {}

        self._loopingCall = LoopingCall(self._poll)
        self._loopingCall.start(self.CHECK_TIME, now=False)

        self._actionClient = TupleDataActionClient(
            tupleActionProcessorName=deviceActionProcessorName,
            destVortexName=peekServerName,
            additionalFilt=deviceFilt,
        )

    def shutdown(self):
        self._ep.shutdown()
        self._ep = None

        self._loopingCall.stop()

        # This is never going to send, the server needs to do it
        # self._sendOfflineForDeviceIds(self._onlineDeviceIdsByUuid.values())
        self._onlineDeviceIdsByUuid = {}

    @peekCatchErrbackWithLogger(logger)
    def _poll(self):
        try:
            onlineVortexUuids = set(VortexFactory.getRemoteVortexUuids())
            onlineDeviceVortexUuids = set(self._onlineDeviceIdsByUuid)

            devicesThatHaveGoneOffline = (
                onlineDeviceVortexUuids - onlineVortexUuids
            )

            deviceIds = []
            for vortexUuid in devicesThatHaveGoneOffline:
                deviceIds.append(self._onlineDeviceIdsByUuid.pop(vortexUuid))

            # Make sure the device hasn't come back online as a difference vortex UUID
            deviceIds = list(
                set(deviceIds) - set(self._onlineDeviceIdsByUuid.values())
            )

            self._sendOfflineForDeviceIds(deviceIds)

        except Exception as e:
            logger.exception(e)

    def _process(
        self, payloadEnvelope: PayloadEnvelope, vortexUuid: str, **kwargs
    ):
        deviceId = payloadEnvelope.filt["deviceId"]

        action = UpdateDeviceOnlineAction()
        # update ip of device
        action.deviceIp = VortexFactory.getRemoteVortexIpByUuid(
            vortexUuid=vortexUuid
        )

        if vortexUuid not in self._onlineDeviceIdsByUuid:
            # for devices that become online
            self._onlineDeviceIdsByUuid[vortexUuid] = deviceId

            action.deviceId = deviceId
            action.deviceStatus = DeviceInfoTuple.DEVICE_ONLINE

        d = self._actionClient.pushAction(action)
        d.addErrback(vortexLogFailure, logger, consumeError=True)

    def _sendOfflineForDeviceIds(self, deviceIds: List[str]):
        for deviceId in deviceIds:
            action = UpdateDeviceOnlineAction()
            action.deviceId = deviceId
            action.deviceStatus = DeviceInfoTuple.DEVICE_OFFLINE

            d = self._actionClient.pushAction(action)
            d.addErrback(vortexLogFailure, logger, consumeError=True)
