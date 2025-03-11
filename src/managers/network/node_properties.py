from utils.logger.logger import Logger

class NodeProperties:
    """
    NodeProperties class is the container for the node's properties.
    """
    # NODEPROPERTIES INITIALIZATION
    def __init__(self, node_data):
        """
        Initializes the NodeProperties instance
        """
        # ATTRIBUTES FOUND IN INPUT
        self.N_ID = None
        self.N_X = None
        self.N_Y = None
        Logger.log(f"start NodeProperties __init__(self, {node_data})")
        self.node_properties = {}
        for key, value in node_data.items():
            setattr(self, key, value)
            self.node_properties[key] = value
            Logger.log(f"NodeProperties attribute added {key}={value}")
        Logger.log(f"end NodeProperties __init__(self, node_data)")