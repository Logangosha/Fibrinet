from utils.logger.logger import Logger
from .node_properties import NodeProperties

class Node:
    """
    Node class is the data structure representing a node in the network.
    """
    # NODE INITIALIZATION
    def __init__(self, node_data):
        """
        Initializes the Node instance
        """
        Logger.log(f"start Node __init__(self)")
        self.properties = NodeProperties(node_data)
        Logger.log(f"end Node __init__(self)")