from abc import ABC, abstractmethod
from ..network.networks.base_network import BaseNetwork

class ExportStrategy(ABC):
    @abstractmethod
    def generate_export(self, network_state_history: list[BaseNetwork]):
        """
        Export the data to a file location (implemented by concrete strategies).
        """
        pass
