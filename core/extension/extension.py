from core.extension.extensible import ModuleExtension, ExtensionModule
from core.external_data_tool.base import ExternalDataTool
from core.moderation.base import Moderation


class Extension:
    __module_extensions: dict[str, dict[str, ModuleExtension]] = {}
    module_classes = {
        ExtensionModule.MODERATION: Moderation,
        ExtensionModule.EXTERNAL_DATA_TOOL: ExternalDataTool
    }
