from VictorOS.services.plugins.plugin import Plugin

class PluginManager:

    def __init__(self):
        self._providers = []

    def register(self, provider):
        self._providers.append(
            Plugin(provider)
        )

    def all(self):
        return [
            plugin.provider
            for plugin in self._providers
            if plugin.enabled
        ]

    def disable(self, name):

        for plugin in self._providers:

            manifest = plugin.provider.get_manifest()

            if manifest.name == name:

                plugin.enabled = False

    def enable(self, name):

        for plugin in self._providers:

            manifest = plugin.provider.get_manifest()

            if manifest.name == name:

                plugin.enabled = True
        
    def installed(self):

        return self._providers