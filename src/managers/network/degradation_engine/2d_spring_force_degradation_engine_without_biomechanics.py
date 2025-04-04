from utils.logger.logger import Logger
from .degradation_engine_strategy import DegradationEngineStrategy
import copy

class TwoDimensionalSpringForceDegradationEngineWithoutBiomechanics(DegradationEngineStrategy):
    """
    Degrades the network by removing edges and nodes without considering physics.
    """

    def degrade_edge(self, network, edge_id):
        """
        Creates a degraded version of the network without the specified edge.

        Params:
            network: network object to be degraded.
            edge_id: id of edge to be removed.

        Returns:
            A new Network object with the specified edge removed.
        """
        Logger.log(f"start degrade_edge(self, network, {edge_id})")
        Logger.log(f"end degrade_edge(self, network, {edge_id})")
        return network

    def degrade_node(self, network, node_id):
        """
        Creates a degraded version of the network without the specified node and its associated edges.

        Params:
            network: network object to be degraded.
            node_id: id of node to be removed.

        Returns:
            A new Network object with the specified node and its edges removed.
        """
        Logger.log(f"start degrade_node(self, network, {node_id})")
        Logger.log(f"end degrade_node(self, network, {node_id})")
        return network
