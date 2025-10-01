# plugin.py
from typing import Any, Annotated

from fastpluggy.core.module_base import FastPluggyBaseModule
from fastpluggy.core.tools.inspect_tools import InjectDependency
from fastpluggy.core.tools.install import is_installed


def get_memory_analyzer_router():
    from .router import memory_analyzer_router
    return memory_analyzer_router


class MemoryAnalyzerPlugin(FastPluggyBaseModule):
    module_name: str = "memory_analyzer"

    module_menu_name: str = "Memory Analyzer"
    module_menu_icon: str = "fas fa-memory"
    module_menu_type: str = "main"

    module_router: Any = get_memory_analyzer_router

    def on_load_complete(
            self,
            fast_pluggy: Annotated["FastPluggy", InjectDependency],
            plugin: Annotated["PluginState", InjectDependency],
    ) -> None:
        if not is_installed('psutil'):
            plugin.add_warning("psutil is not installed. Memory analyzer will not be available.")