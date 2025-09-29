import logging

from twisted.internet.defer import inlineCallbacks

from peek_core_device._private.client.controllers.DeviceOnlineController import (
    DeviceOnlineController,
)
from peek_core_device._private.storage.DeclarativeBase import loadStorageTuples
from peek_core_device._private.tuples import loadPrivateTuples
from peek_core_device.tuples import loadPublicTuples
from peek_plugin_base.client.PluginClientEntryHookABC import (
    PluginClientEntryHookABC,
)
from .DeviceTupleDataObservableProxy import makeDeviceTupleDataObservableProxy
from .DeviceTupleProcessorActionProxy import makeTupleActionProcessorProxy
from .controllers.BandwidthTestController import BandwidthTestController

logger = logging.getLogger(__name__)


class ClientEntryHook(PluginClientEntryHookABC):
    def __init__(self, *args, **kwargs):
        """ " Constructor"""
        # Call the base classes constructor
        PluginClientEntryHookABC.__init__(self, *args, **kwargs)

        #: Loaded Objects, This is a list of all objects created when we start
        self._loadedObjects = []

    def load(self) -> None:
        """Load

        This will be called when the plugin is loaded, just after the db is migrated.
        Place any custom initialiastion steps here.

        """

        loadStorageTuples()

        loadPrivateTuples()
        loadPublicTuples()

        logger.debug("Loaded")

    @inlineCallbacks
    def start(self):
        """Load

        This will be called when the plugin is loaded, just after the db is migrated.
        Place any custom initialiastion steps here.

        """

        # ----------------
        # Setup Photo Resource Proxy
        # Support file downloads for device updates
        # noinspection PyTypeChecker
        proxyResource = self.createProxy()
        # Matches resource path on server
        # noinspection PyTypeChecker
        self.platform.addOfficeResource(b"device_update", proxyResource)

        # noinspection PyTypeChecker
        self.platform.addFieldResource(b"device_update", proxyResource)

        # ----------------
        # Action Processor Proxy
        self._loadedObjects.append(makeTupleActionProcessorProxy())

        # ----------------
        # Data Observable Proxy
        self._loadedObjects.append(makeDeviceTupleDataObservableProxy())

        # ----------------
        # Online Handler
        self._loadedObjects.append(DeviceOnlineController())

        # ----------------
        # Bandwidth Test Controller
        bandwidthController = BandwidthTestController()
        self._loadedObjects.append(bandwidthController)
        yield bandwidthController.start()

        # # ----------------
        # # Update Download Handler
        # self._loadedObjects.append(
        #     UpdateDownloadHandler(self.platform.fileStorageDirectory,
        #                           self.platform.peekServerHost,
        #                           self.platform.peekServerHttpPort)
        # )

        logger.debug("Started")

    @inlineCallbacks
    def stop(self):
        """Stop

        This method is called by the platform to tell the peek app to shutdown and stop
        everything it's doing
        """
        # Shutdown and dereference all objects we constructed when we started
        while self._loadedObjects:
            yield self._loadedObjects.pop().shutdown()

        logger.debug("Stopped")

    def unload(self):
        """Unload

        This method is called after stop is called, to unload any last resources
        before the PLUGIN is unlinked from the platform

        """
        logger.debug("Unloaded")
