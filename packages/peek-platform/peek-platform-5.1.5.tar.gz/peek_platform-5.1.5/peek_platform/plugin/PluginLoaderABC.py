import gc
import logging
import os
import sys
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
from collections import defaultdict
from importlib.util import find_spec
from typing import Optional
from typing import Tuple
from typing import Type

from jsoncfg.value_mappers import require_array
from jsoncfg.value_mappers import require_string
from twisted.internet.defer import maybeDeferred
from vortex.DeferUtil import vortexLogFailure

from peek_platform import PeekPlatformConfig
from twisted.internet.defer import inlineCallbacks

from peek_platform.subproc_plugin_init.plugin_subproc.plugin_subproc_platform_config_tuple import (
    PluginSubprocPlatformConfigTuple,
)
from peek_platform.subproc_plugin_init.plugin_subproc.plugin_subproc_vortex_msg_tuple import (
    PluginSubprocVortexMsgTuple,
)
from peek_platform.subproc_plugin_init.plugin_subproc.plugin_subproc_vortex_payload_envelope_tuple import (
    PluginSubprocVortexPayloadEnvelopeTuple,
)
from peek_plugin_base.PluginCommonEntryHookABC import PluginCommonEntryHookABC
from peek_plugin_base.PluginPackageFileConfig import PluginPackageFileConfig
from vortex.PayloadIO import PayloadIO
from vortex.Tuple import registeredTupleNames
from vortex.Tuple import removeTuplesForTupleNames
from vortex.Tuple import tupleForTupleName
from vortex.TupleAction import TupleGenericAction
from vortex.TupleAction import TupleUpdateAction
from vortex.TupleSelector import TupleSelector
from vortex.VortexUtil import _DebounceArgsTuple
from vortex.rpc.RPC import _VortexRPCArgTuple
from vortex.rpc.RPC import _VortexRPCResultTuple

from peek_plugin_base.simple_subproc.simple_subproc_task_call_tuple import (
    SimpleSubprocTaskCallTuple,
)
from peek_plugin_base.simple_subproc.simple_subproc_task_constructor_tuple import (
    SimpleSubprocTaskConstructorTuple,
)
from peek_plugin_base.simple_subproc.simple_subproc_task_result_tuple import (
    SimpleSubprocTaskResultTuple,
)
from peek_worker_service.peek_worker_tuples import PeekWorkerTaskArgsTuple
from peek_worker_service.peek_worker_tuples import PeekWorkerTaskResultTuple
from peek_worker_service.peek_worker_tuples import PeekWorkerTaskStartTuple

logger = logging.getLogger(__name__)

# This doesn't do anything, but it makes sure it's imported before any plugins import it.
TupleSelector()
TupleUpdateAction()
TupleGenericAction()
_VortexRPCResultTuple()
_VortexRPCArgTuple()
_DebounceArgsTuple()
SimpleSubprocTaskResultTuple()
SimpleSubprocTaskCallTuple()
SimpleSubprocTaskConstructorTuple()
PluginSubprocPlatformConfigTuple()
PluginSubprocVortexMsgTuple()
PluginSubprocVortexPayloadEnvelopeTuple()
PeekWorkerTaskArgsTuple()
PeekWorkerTaskStartTuple()
PeekWorkerTaskResultTuple()

corePlugins = [
    "peek_core_email",
    "peek_core_device",
    "peek_core_search",
    "peek_core_user",
    "peek_core_docdb",
    "peek_core_screen",
]


class PluginLoaderABC(metaclass=ABCMeta):
    _instance = None

    def __new__(cls, *args, **kwargs):
        assert (
            cls._instance is None
        ), "PluginServerLoader is a singleton, don't construct it"
        cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self._loadedPlugins = {}
        self._loadedSubprocessGroups = {}

        self._vortexEndpointInstancesByPluginName = defaultdict(list)
        self._vortexTupleNamesByPluginName = defaultdict(list)

    @abstractproperty
    def _entryHookFuncName(self) -> str:
        """Entry Hook Func Name.
        Protected property
        :return: EG  "peekLogicEntryHook"

        """

    @abstractproperty
    def _entryHookClassType(self):
        """Entry Hook Class Type
        Protected property
        :return: EG  PluginLogicEntryHookABC

        """

    @abstractproperty
    def _platformServiceNames(self) -> [str]:
        """Platform Service Name
        Protected property
        :return: one or more of "logic", "worker", "agent", "client", "storage"

        """

    def pluginEntryHook(self, pluginName) -> Optional[PluginCommonEntryHookABC]:
        """Plugin Entry Hook

        Returns the loaded plugin entry hook for the plugin name.

        :param pluginName: The name of the plugin to load

        :return: An instance of the plugin entry hook

        """
        return self._loadedPlugins.get(pluginName)

    @inlineCallbacks
    def loadPlugin(self, pluginName):
        # Until we implement dynamic loading and unloading of plugins
        # make sure we don't load them twice, because we don't yet
        # support it.

        from peek_platform import PeekPlatformConfig

        if pluginName in self._loadedPlugins:
            raise Exception(
                "Plugin %s is already loaded, check config.json" % pluginName
            )

        try:
            self.unloadPlugin(pluginName)

            # Make note of the initial registrations for this plugin
            endpointInstancesBefore = set(PayloadIO().endpoints)
            tupleNamesBefore = set(registeredTupleNames())

            modSpec = find_spec(pluginName)
            if not modSpec:
                raise Exception(
                    "Failed to find package %s,"
                    " is the python package installed?" % pluginName
                )

            PluginPackage = modSpec.loader.load_module()

            pluginRootDir = os.path.dirname(PluginPackage.__file__)

            # Load up the plugin package info
            pluginPackageJson = PluginPackageFileConfig(pluginRootDir)
            pluginVersion = pluginPackageJson.config.plugin.version(
                require_string
            )
            pluginRequiresService = pluginPackageJson.config.requiresServices(
                require_array
            )

            # Make sure the service is required
            # Storage and Server are loaded at the same time, hence the intersection
            if not set(pluginRequiresService) & set(self._platformServiceNames):
                logger.debug(
                    "%s does not require %s, Skipping load",
                    pluginName,
                    self._platformServiceNames,
                )
                return

            configForService = pluginPackageJson.configForService(
                PeekPlatformConfig.componentName
            )

            # Get the entry hook class from the package
            entryHookGetter = getattr(
                PluginPackage, str(self._entryHookFuncName)
            )

            subprocessGroup = configForService.subprocessGroup(None)
            runInSubprocess = (
                subprocessGroup and not PeekPlatformConfig.isPluginSubprocess
            )

            RealEntryHookClass = entryHookGetter() if entryHookGetter else None

            if not RealEntryHookClass:
                logger.warning(
                    "Skipping load for %s, %s.%s is missing or returned None",
                    pluginName,
                    pluginName,
                    self._entryHookFuncName,
                )
                return

            if not issubclass(RealEntryHookClass, self._entryHookClassType):
                raise Exception(
                    "%s load error, Excpected %s, received %s"
                    % (pluginName, self._entryHookClassType, RealEntryHookClass)
                )

            # Are we going to run this plugin in a subprocess?
            if False:  # runInSubprocess:
                pass
                """
                from peek_platform.subproc_plugin_init.plugin_subproc_parent_main import (
                    PluginSubprocParentMain,
                )

                # We can run multiple plugins in one group
                # Have we already created this group?
                if subprocessGroup in self._loadedSubprocessGroups:
                    subprocParentMain = self._loadedSubprocessGroups[
                        subprocessGroup
                    ]
                else:
                    # Else, create it.
                    subprocParentMain = PluginSubprocParentMain(subprocessGroup)
                    self._loadedSubprocessGroups[
                        subprocessGroup
                    ] = subprocParentMain

                # Return the subprocParentMain, it has a __call__ method
                # to simulate the plugin class constructor
                EntryHookClass = subprocParentMain
                """

            else:
                EntryHookClass = RealEntryHookClass

            ### Perform the loading of the plugin
            yield self._loadPluginThrows(
                pluginName,
                EntryHookClass,
                pluginRootDir,
                tuple(pluginRequiresService),
            )

            yield self._setupStaticWebResourcesForPlugin(
                RealEntryHookClass, pluginName
            )

            # Make sure the version we have recorded is correct
            # JJC Disabled, this is just spamming the config file at the moment
            # PeekPlatformConfig.config.setPluginVersion(pluginName, pluginVersion)

            # Make note of the final registrations for this plugin
            self._vortexEndpointInstancesByPluginName[pluginName] = list(
                set(PayloadIO().endpoints) - endpointInstancesBefore
            )

            self._vortexTupleNamesByPluginName[pluginName] = list(
                set(registeredTupleNames()) - tupleNamesBefore
            )

            self.sanityCheckServerPlugin(pluginName)

        except Exception as e:
            logger.error("Failed to load plugin %s", pluginName)
            logger.exception(e)

    @abstractmethod
    def _loadPluginThrows(
        self,
        pluginName: str,
        EntryHookClass: Type[PluginCommonEntryHookABC],
        pluginRootDir: str,
        requiresService: Tuple[str, ...],
    ) -> None:
        """Load Plugin (May throw Exception)

        This method is called to perform the load of the module.

        :param pluginName: The name of the Peek App, eg "plugin_noop"
        :param EntryHookClass: The plugin entry hook class to construct.
        :param pluginRootDir: The directory of the plugin package,
         EG dirname(plugin_noop.__file__)

        """

    @inlineCallbacks
    def _setupStaticWebResourcesForPlugin(
        self, RealEntryHookClass, pluginName: str
    ):
        """Setup Static Web Resources For Plugin

        If this is running in a subprocess, we need to call this method on the
        actual plugin, not PluginSubprocParentMain
        """
        loadedPlugin = self._loadedPlugins[pluginName]

        yield RealEntryHookClass.setupStaticWebResources(loadedPlugin._platform)

    @inlineCallbacks
    def unloadPlugin(self, pluginName: str):
        oldLoadedPlugin = self._loadedPlugins.get(pluginName)

        if not oldLoadedPlugin:
            return

        del oldLoadedPlugin

        # Remove the registered endpoints
        for endpoint in self._vortexEndpointInstancesByPluginName[pluginName]:
            PayloadIO().remove(endpoint)
        del self._vortexEndpointInstancesByPluginName[pluginName]

        # Remove the registered tuples
        removeTuplesForTupleNames(
            self._vortexTupleNamesByPluginName[pluginName]
        )
        del self._vortexTupleNamesByPluginName[pluginName]

        yield self._unloadPluginPackage(pluginName)

    def listPlugins(self):
        def pluginTest(name):
            if not name.startswith("plugin_"):
                return False
            return os.path.isdir(os.path.join(self._pluginPath, name))

        plugins = os.listdir(self._pluginPath)
        plugins = list(filter(pluginTest, plugins))
        return plugins

    # ---------------
    # Core Plugins

    @inlineCallbacks
    def loadCorePlugins(self):
        for pluginName in corePlugins:
            yield self.loadPlugin(pluginName)

    @inlineCallbacks
    def startCorePlugins(self):
        # Start the Plugin
        for pluginName in corePlugins:
            if pluginName not in self._loadedPlugins:
                continue

            yield self._tryStart(pluginName)

    @inlineCallbacks
    def stopCorePlugins(self):
        # Start the Plugin
        for pluginName in corePlugins:
            if pluginName not in self._loadedPlugins:
                continue

            yield self._tryStop(pluginName)

    def unloadCorePlugins(self):
        for pluginName in corePlugins:
            if pluginName in self._loadedPlugins:
                self.unloadPlugin(pluginName)

    # ---------------
    # Optional Plugins

    @inlineCallbacks
    def loadOptionalPlugins(self):
        for pluginName in PeekPlatformConfig.config.pluginsEnabled:
            if pluginName.startswith("peek_core"):
                raise Exception("Core plugins can not be configured")
            yield self.loadPlugin(pluginName)

    @inlineCallbacks
    def startOptionalPlugins(self):
        # Start the Plugin
        for pluginName in PeekPlatformConfig.config.pluginsEnabled:
            if pluginName not in self._loadedPlugins:
                continue

            yield self._tryStart(pluginName)

    @inlineCallbacks
    def stopOptionalPlugins(self):
        # Start the Plugin
        for pluginName in reversed(PeekPlatformConfig.config.pluginsEnabled):
            if pluginName not in self._loadedPlugins:
                continue

            yield self._tryStop(pluginName)

    def unloadOptionalPlugins(self):
        for pluginName in reversed(PeekPlatformConfig.config.pluginsEnabled):
            if pluginName in self._loadedPlugins:
                self.unloadPlugin(pluginName)

        remainingOptionalPlugins = list(
            filter(lambda n: not n.startswith("peek_core"), self._loadedPlugins)
        )

        if remainingOptionalPlugins:
            logger.debug(remainingOptionalPlugins)
            raise Exception("Some plugins are still loaded")

    # ---------------
    # Standalone Plugins

    @inlineCallbacks
    def loadStandalonePlugin(self, pluginName: str):
        yield self.loadPlugin(pluginName)

    @inlineCallbacks
    def startStandalonePlugin(self, pluginName: str):
        yield self._tryStart(pluginName)

    @inlineCallbacks
    def stopStandalonePlugin(self, pluginName: str):
        yield self._tryStop(pluginName)

    @inlineCallbacks
    def unloadStandalonePlugin(self, pluginName: str):
        yield self.unloadPlugin(pluginName)

    # ---------------
    # Util methods Plugins

    @inlineCallbacks
    def _tryStart(self, pluginName):
        plugin = self._loadedPlugins[pluginName]
        try:
            yield plugin.start()

        except Exception as e:
            logger.error(
                "An exception occurred while starting plugin %s,"
                " starting continues" % pluginName
            )
            logger.exception(e)

    @inlineCallbacks
    def _tryStop(self, pluginName):
        plugin = self._loadedPlugins[pluginName]
        try:
            yield plugin.stop()

        except Exception as e:
            logger.error(
                "An exception occurred while stopping plugin %s,"
                " stopping continues" % pluginName
            )
            logger.exception(e)

    @inlineCallbacks
    def _unloadPluginPackage(self, pluginName):
        oldLoadedPlugin = self._loadedPlugins.get(pluginName)

        # Stop and remove the Plugin
        del self._loadedPlugins[pluginName]

        try:
            yield oldLoadedPlugin.unload()

        except Exception as e:
            logger.error(
                "An exception occured while unloading plugin %s,"
                " unloading continues" % pluginName
            )
            logger.exception(e)

        # Unload the packages
        loadedSubmodules = [
            modName
            for modName in list(sys.modules.keys())
            if modName.startswith("%s." % pluginName)
        ]

        for modName in loadedSubmodules:
            del sys.modules[modName]

        if pluginName in sys.modules:
            del sys.modules[pluginName]

        gc.collect()

        # pypy doesn't have getrefcount
        # ("oldLoadedPlugin" in this method and the call to getrefcount) == 2 references
        if hasattr(sys, "getrefcount") and sys.getrefcount(oldLoadedPlugin) > 2:
            logger.warning(
                "Old references to %s still exist, count = %s",
                pluginName,
                sys.getrefcount(oldLoadedPlugin),
            )

        del oldLoadedPlugin
        gc.collect()
        # Now there should be no references.

    def sanityCheckServerPlugin(self, pluginName):
        """Sanity Check Plugin

        This method ensures that all the things registed for this plugin are
        prefixed by it's pluginName, EG plugin_noop
        """

        # All endpoint filters must have the 'plugin' : 'plugin_name' in them
        for endpoint in self._vortexEndpointInstancesByPluginName[pluginName]:
            filt = endpoint.filt
            if "plugin" not in filt and filt["plugin"] != pluginName:
                raise Exception(
                    "Payload endpoint does not contain 'plugin':'%s'\n%s"
                    % (pluginName, filt)
                )

        # all tuple names must start with their pluginName
        for tupleName in self._vortexTupleNamesByPluginName[pluginName]:
            TupleCls = tupleForTupleName(tupleName)
            if not tupleName.startswith(
                pluginName
            ) and not tupleName.startswith("vortex._"):
                raise Exception(
                    "Tuple name does not start with '%s', %s (%s)"
                    % (pluginName, tupleName, TupleCls.__name__)
                )

    def notifyOfPluginVersionUpdate(self, pluginName, pluginVersion):
        logger.info(
            "Received PLUGIN update for %s version %s",
            pluginName,
            pluginVersion,
        )
        return self.loadPlugin(pluginName)
