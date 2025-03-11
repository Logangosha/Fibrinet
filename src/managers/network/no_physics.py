from utils.logger.logger import Logger
from .degradation_engine_strategy import DegradationEngineStrategy
from .network import Network
import copy

class NoPhysics(DegradationEngineStrategy):
    # DEGRADE EDGE
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
        
        # Create a copy of the network
        new_network = copy.deepcopy(network)
        
        # Remove the edge with the specified ID
        new_network.properties.edges = [edge for edge in new_network.properties.edges if edge.properties.E_ID != edge_id]

         # Remove nodes that no longer have any edges connected to them
        connected_node_ids = {edge.properties.N_TO for edge in new_network.properties.edges}.union(
            {edge.properties.N_FROM for edge in new_network.properties.edges})
        new_network.properties.nodes = [node for node in new_network.properties.nodes if node.properties.N_ID in connected_node_ids]
        
        Logger.log(f"end degrade_edge(self, network, {edge_id})")
        return new_network
    
    # DEGRADE NODE
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
        
        # Create a copy of the network
        new_network = copy.deepcopy(network)
        
        # Remove the node with the specified ID
        new_network.properties.nodes = [node for node in new_network.properties.nodes if node.properties.N_ID != node_id]
        
        # Remove edges connected to the removed node
        new_network.properties.edges = [edge for edge in new_network.properties.edges if edge.properties.N_TO != node_id and edge.properties.N_FROM != node_id]
        
        # Remove nodes that no longer have any edges connected to them
        connected_node_ids = {edge.properties.N_TO for edge in new_network.properties.edges}.union(
            {edge.properties.N_FROM for edge in new_network.properties.edges})
        new_network.properties.nodes = [node for node in new_network.properties.nodes if node.properties.N_ID in connected_node_ids]
        
        Logger.log(f"end degrade_node(self, network, {node_id})")
        return new_network
