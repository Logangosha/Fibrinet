from utils.logger.logger import Logger
from .edge_properties import EdgeProperties

class Edge:
    """
    Edge class is the data structure representing an edge in the network.
    """
    # EDGE INITIALIZATION
    def __init__(self, edge_data):
        """
        Initializes the Edge instance
        """
        Logger.log(f"start Edge __init__(self)")
        self.properties = EdgeProperties(edge_data)
        Logger.log(f"end Edge __init__(self)")