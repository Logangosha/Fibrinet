from utils.logger.logger import Logger

class EdgeProperties:
    """
    EdgeProperties class is the container for the edge's properties.
    """
    # EdgeProperties INITIALIZATION
    def __init__(self, edge_data):
        """
        Initializes the EdgeProperties instance
        """
        Logger.log(f"start EdgeProperties __init__(self, {edge_data})")
        self.edge_properties = {}
        for key, value in edge_data.items():
            setattr(self, key, value)
            self.edge_properties[key] = value
            Logger.log(f"EdgeProperty attribute added {key}={value}")
        Logger.log(f"end EdgeProperties __init__(self, edge_data)")