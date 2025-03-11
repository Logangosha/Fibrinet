from utils.logger.logger import Logger

class EdgeProperties:
    """
    EdgeProperties class is the container for the edge's properties.
    """
    # EDGEPROPERTIES INITIALIZATION
    def __init__(self, edge_data):
        """
        Initializes the EdgeProperties instance
        """
        Logger.log(f"start EdgeProperties __init__(self, {edge_data})")

        # ATTRIBUTES FOUND IN INPUT
        self.E_ID = None
        self.N_FROM = None
        self.N_TO = None
        
        # DYNAMICALY SET ATTRIBUTES BASED ON INPUT
        # LIST TO STORE PROPERTIES
        self.edge_properties = {}
        # FOR EACH KEY AND VALUE IN ITEMS SET THE ATTRIBUTE AND STORE THE PROPERTY
        for key, value in edge_data.items():
            setattr(self, key, value)
            self.edge_properties[key] = value
            Logger.log(f"EdgeProperty attribute added {key}={value}")
        Logger.log(f"end EdgeProperties __init__(self, edge_data)")