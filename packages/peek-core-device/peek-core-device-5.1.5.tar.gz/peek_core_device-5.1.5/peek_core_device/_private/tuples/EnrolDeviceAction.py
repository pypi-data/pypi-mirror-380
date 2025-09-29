from vortex.Tuple import TupleField
from vortex.Tuple import addTupleType
from vortex.TupleAction import TupleActionABC

from peek_core_device._private.PluginNames import deviceTuplePrefix


@addTupleType
class EnrolDeviceAction(TupleActionABC):
    __tupleType__ = deviceTuplePrefix + "EnrolDeviceAction"

    description: str = TupleField()
    deviceId: str = TupleField()
    deviceType: str = TupleField()
    appVersion: str = TupleField()

    mdmDeviceName: str = TupleField()
    mdmDeviceSerialNumber: str = TupleField()
    mdmDeviceAssetId: str = TupleField()
    mdmDeviceAllocatedTo: str = TupleField()
