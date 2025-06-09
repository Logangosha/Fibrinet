from ..network.networks.base_network import BaseNetwork

class ExportStrategy():
    def generate_export(self, network_state_history: list[BaseNetwork]):
        """
        Export the data to a file location (implemented by concrete strategies).
        """
        pass
