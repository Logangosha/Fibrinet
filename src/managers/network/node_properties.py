from utils.logger.logger import Logger

class NodeProperties:
    """
    NodeProperties class is the container for the node's properties.
    """
    # NodeProperties INITIALIZATION
    def __init__(self, node_data):
        """
        Initializes the NodeProperties instance
        """
        Logger.log(f"start NodeProperties __init__(self, {node_data})")
        self.node_properties = {}
        for key, value in node_data.items():
            setattr(self, key, value)
            self.node_properties[key] = value
            Logger.log(f"NodeProperties attribute added {key}={value}")
        Logger.log(f"end NodeProperties __init__(self, node_data)")