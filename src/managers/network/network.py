from utils.logger.logger import Logger
from .network_properties import NetworkProperties

class Network:
    """
    Network class used as the data structure for the network of fibrin under tension.
    """
    # INITIALIZES NETWORK
    def __init__(self, **kwargs):
        """
        Initializes the Network.
        """
        Logger.log(f"start Network __init__(self)")
        self.properties = NetworkProperties(**kwargs)
        
        Logger.log("===== Network Properties =====")
        
        Logger.log("Nodes:")
        for node in self.properties.nodes:
            Logger.log(f"{node.properties.node_properties}")
        
        Logger.log("Edges:")
        for edge in self.properties.edges:
            Logger.log(f"{edge.properties.edge_properties}")

        Logger.log("Meta Properties:")
        for key, value in self.properties.meta_network_properties.items():
            Logger.log(f"{key}: {value}")
        
        Logger.log("==============================")

        Logger.log(f"end Network __init__(self)")
    
