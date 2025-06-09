from utils.logger.logger import Logger

class DegradationEngineStrategy():
    """
    Base class for strategies handling different degradation engines.
    Subclasses should implement methods to handle degrate_network(action).
    """

    # DEGRADATION ENGINE STRATEGY INITILIZATION
    def __init__(self):
        """
        Initializes the DegradationEngineStrategy instance and sets up the controller.
        """
        Logger.log("start DegradationEngineStrategy__init__(self)")
        Logger.log("end DegradationEngineStrategy__init__(self)")

    # DEGRADE EDGE
    def degrade_edge(self, network, edge_id):
        """
        Degrades specified network edge.

        Params: 
            network: network object to be degraded. 
            edge_id: id of edge to be degraded.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO DEGRADE EDGE
        raise NotImplementedError()
    
    # DEGRADE NODE
    def degrade_node(self, network, node_id):
        """
        Degrades specified network node.

        Params: 
            network: network object to be degraded.
            node_id: id of node to be degraded.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO DEGRADE NODE
        raise NotImplementedError()
    
    # RELAX NETWORK
    def relax_network(self, network):
        """
        Relaxes the specified network.

        Params: 
            network: network object to be relaxed.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO RELAX NETWORK
        raise NotImplementedError()
