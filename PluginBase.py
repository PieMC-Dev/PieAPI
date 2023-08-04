from piemc.plugin.Terminal import Terminal

class PluginBase:

    CURRENT_API_VERSION = "1.0.0"
    
    def set_logger(self, logger):
        self.logger = logger

    def on_enable(self):
        raise NotImplementedError(Terminal.red("on_enable() must be implemented in the plugin main class."))
