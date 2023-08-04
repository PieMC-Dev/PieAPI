import importlib.util
import json
import os
from piemc.plugin.PluginBase import PluginBase
from piemc.plugin.Terminal import Terminal

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load_plugins(self):
        for root, dirs, files in os.walk("plugins"):
            for file in files:
                if file == "plugin.json":
                    plugin_folder = os.path.basename(root)
                    plugin_path = os.path.join(root, file)
                    with open(plugin_path) as f:
                        plugin_info = json.load(f)
                        if "main" in plugin_info:
                            main_module = plugin_info["main"]
                            module_path = os.path.join(root, main_module + ".py")
                            if os.path.exists(module_path):
                                self.load_plugin(plugin_folder, module_path, plugin_info)

    def load_plugin(self, plugin_folder, module_path, plugin_info):
        spec = importlib.util.spec_from_file_location(plugin_folder, module_path)
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)
        if hasattr(plugin_module, "Main"):
            main_class = getattr(plugin_module, "Main")
            if issubclass(main_class, PluginBase):
                plugin_instance = main_class()
                plugin_instance.set_logger(PluginBase.logger)
                api_version = plugin_info.get("api", PluginBase.CURRENT_API_VERSION)
                if PluginBase.CURRENT_API_VERSION <= api_version <= "1.0.0":
                    self.plugins[plugin_folder] = plugin_instance
                    plugin_name = plugin_info.get("name", "Unknown Plugin")
                    plugin_version = plugin_info.get("version", "Unknown Version")
                    plugin_instance.logger.info(Terminal.blue(f"Loading plugin '{plugin_name}' v{plugin_version}"))
                    plugin_instance.on_enable()
                    plugin_instance.logger.info(Terminal.blue(f"Enabling plugin '{plugin_name}' v{plugin_version}"))
                else:
                    plugin_name = plugin_info.get("name", "Unknown Plugin")
                    plugin_instance.logger.warning(Terminal.red(
                        f"{plugin_name} API version {api_version} is not compatible with the API: "
                        f"{PluginBase.CURRENT_API_VERSION}. Please update the plugin."
                    ))
    def get_plugin(self, plugin_name):
        return self.plugins.get(plugin_name, None)
