from utils.logger.logger import Logger
from .edge import Edge
from .node import Node
class NetworkProperties:
    """
    NetworkProperties class used as the container for the network properties.
    """
    # INITIALIZES NETWORKPROPERTIES
    def __init__(self, **kwargs):
        """
        Initializes the NetworkProperties.
        """
        Logger.log(f"start NetworkProperties __init__(self)")
        self.nodes = []
        self.edges = []
        self.meta_network_properties = {}

        # EXTRACTS NODE DATA AND CREATES NODE OBJECTS
        if 'NODES' in kwargs:
            # GET NODE KEYS (N_ID, N_X, ...)
            node_keys = kwargs['NODES'].keys()
            # ZIP FUNCTION TAKES A VALUE FROM EACH NODE ATTRIBUTE AND COMBINES IT INTO ONE CONTAINER (VALUES)
            # THEN WE ZIP NODE KEYS AND VALUES TO A DICTIONARY 
            node_dicts = [dict(zip(node_keys, values)) for values in zip(*kwargs['NODES'].values())]
            # FOR EACH NODE DATA IN THIS DICTIONARY WE MAKE A NEW NODE AND ADD IT TO NODES 
            self.nodes = [Node(node_data) for node_data in node_dicts]

         # EXTRACTS EDGE DATA AND CREATES EDGE OBJECTS
        if 'EDGES' in kwargs:
            # GET EDGE KEYS (E_ID, E_TO, ...)
            edge_keys = kwargs['EDGES'].keys()
            # ZIP FUNCTION TAKES A VALUE FROM EACH EDGE ATTRIBUTE AND COMBINES IT INTO ONE CONTAINER (VALUES)
            # THEN WE ZIP EDGE KEYS AND VALUES TO A DICTIONARY
            edge_dicts = [dict(zip(edge_keys, values)) for values in zip(*kwargs['EDGES'].values())]
            # FOR EACH EDGE DATA IN THIS DICTIONARY WE MAKE A NEW EDGE AND ADD IT TO EDGES 
            self.edges = [Edge(edge_data) for edge_data in edge_dicts]

        # EXTRACT AND SET NETWORK PROPERTIES DYNAMICLY
        if 'META_NETWORK_PROPERTIES' in kwargs:
            meta_data = kwargs['META_NETWORK_PROPERTIES']
            keys = meta_data.get('META_NET_PROP', [])
            values = meta_data.get('META_NET_PROP_VALUE', [])
            
            for key, value in zip(keys, values):
                setattr(self, key, value)  
                self.meta_network_properties[key] = value
                Logger.log(f"Adding META_NETWORK_PROPERTY {key}: {value}")

        Logger.log(f"end NetworkProperties __init__(self)")