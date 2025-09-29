import logging
from datetime import datetime
from typing import List
from uuid import uuid4

import pytz
from peek_core_device._private.server.controller.NotifierController import (
    NotifierController,
)
from peek_core_device._private.storage.DeviceInfoTable import DeviceInfoTable
from peek_core_device._private.storage.Setting import AUTO_ENROLLMENT
from peek_core_device._private.storage.Setting import globalSetting
from peek_core_device._private.tuples.EnrolDeviceAction import EnrolDeviceAction
from peek_core_device._private.tuples.UpdateEnrollmentAction import (
    UpdateEnrollmentAction,
)
from sqlalchemy.exc import IntegrityError
from twisted.internet.defer import Deferred
from vortex.DeferUtil import deferToThreadWrapWithLogger
from vortex.Tuple import Tuple
from vortex.TupleAction import TupleActionABC

from peek_core_device.tuples.DeviceInfoTuple import DeviceInfoTuple

logger = logging.getLogger(__name__)


class EnrollmentController:
    def __init__(
        self, dbSessionCreator, notifierController: NotifierController
    ):
        self._dbSessionCreator = dbSessionCreator
        self._notifierController = notifierController

    def shutdown(self):
        pass

    def processTupleAction(self, tupleAction: TupleActionABC) -> List[Tuple]:
        if isinstance(tupleAction, EnrolDeviceAction):
            return self._processDeviceEnrolment(tupleAction)

        if isinstance(tupleAction, UpdateEnrollmentAction):
            return self._processAdminUpdateEnrolment(tupleAction)

    @deferToThreadWrapWithLogger(logger)
    def _processDeviceEnrolment(self, action: EnrolDeviceAction) -> List[Tuple]:
        """Process Device Enrolment

        :rtype: Deferred
        """
        ormSession = self._dbSessionCreator()
        try:
            # There should only be one item that exists if it exists.
            existing = (
                ormSession.query(DeviceInfoTable)
                .filter(DeviceInfoTable.deviceId == action.deviceId)
                .all()
            )

            if existing:
                return [e.toTuple() for e in existing]

            deviceInfo = DeviceInfoTable()
            deviceInfo.description = action.description
            deviceInfo.deviceId = action.deviceId
            deviceInfo.deviceType = action.deviceType
            deviceInfo.deviceToken = str(uuid4())
            deviceInfo.createdDate = datetime.now(pytz.utc)
            deviceInfo.appVersion = "0.0.0"
            deviceInfo.isEnrolled = globalSetting(ormSession, AUTO_ENROLLMENT)

            # TODO, Move these to their own tuple
            deviceInfo.lastOnline = datetime.now(pytz.utc)
            deviceInfo.deviceStatus = DeviceInfoTuple.DEVICE_ONLINE

            deviceInfo.mdmDeviceName = action.mdmDeviceName
            deviceInfo.mdmDeviceSerialNumber = action.mdmDeviceSerialNumber
            deviceInfo.mdmDeviceAssetId = action.mdmDeviceAssetId
            deviceInfo.mdmDeviceAllocatedTo = action.mdmDeviceAllocatedTo

            ormSession.add(deviceInfo)
            ormSession.commit()

            self._notifierController.notifyDeviceInfo(
                deviceId=deviceInfo.deviceId
            )

            ormSession.refresh(deviceInfo)
            ormSession.expunge_all()
            return [deviceInfo.toTuple()]

        except IntegrityError as e:
            if "DeviceInfo_deviceId_key" in str(e):
                raise Exception("A device with that identifier already exists")

            if "DeviceInfo_description_key" in str(e):
                raise Exception("A device with that description already exists")

            raise

        finally:
            # Always close the session after we create it
            ormSession.close()

    @deferToThreadWrapWithLogger(logger)
    def _processAdminUpdateEnrolment(
        self, action: UpdateEnrollmentAction
    ) -> List[Tuple]:
        """Process Admin Update

        :rtype: Deferred
        """
        session = self._dbSessionCreator()
        try:
            deviceInfo = (
                session.query(DeviceInfoTable)
                .filter(DeviceInfoTable.id == action.deviceInfoId)
                .one()
            )

            deviceId = deviceInfo.deviceId

            if action.remove:
                session.delete(deviceInfo)
            else:
                deviceInfo.isEnrolled = not action.unenroll

            session.commit()

            self._notifierController.notifyDeviceInfo(
                deviceId=deviceId, forceUpdate=True
            )

            return []

        finally:
            # Always close the session after we create it
            session.close()
