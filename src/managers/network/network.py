from utils.logger.logger import Logger
from .network_properties import NetworkProperties

class Network:
    """
    Network class used as the data structure for the network of fibrin under tension.
    """
    # INITIALIZES NETWORK
    def __init__(self, **kwargs):
        """
        Initializes the Network.
        """
        Logger.log(f"start Network __init__(self)")
        self.properties = NetworkProperties(**kwargs)
        
        Logger.log("===== Network Properties =====")
        
        Logger.log("Nodes:")
        for node in self.properties.nodes:
            Logger.log(f"{node.properties.node_properties}")
        
        Logger.log("Edges:")
        for edge in self.properties.edges:
            Logger.log(f"{edge.properties.edge_properties}")

        Logger.log("Meta Properties:")
        for key, value in self.properties.meta_network_properties.items():
            Logger.log(f"{key}: {value}")
        
        Logger.log("==============================")

        Logger.log(f"end Network __init__(self)")

        # ADDS A NODE TO THE NETWORK
    def add_node(self, node):
        """
        Adds a node to the network.
        
        :param node: The node to be added.
        """
        Logger.log(f"Start Network.add_node(self, node={node})")
        # Implementation goes here
        Logger.log(f"End Network.add_node(self, node={node})")
    
    # REMOVES A NODE FROM THE NETWORK
    def remove_node(self, node):
        """
        Removes a node and all associated edges from the network.
        
        :param node: The node to be removed.
        """
        Logger.log(f"Start Network.remove_node(self, node={node})")
        # Implementation goes here
        Logger.log(f"End Network.remove_node(self, node={node})")
    
    # RETURNS ALL NODES IN THE NETWORK
    def get_nodes(self):
        """
        Returns all nodes in the network.
        """
        Logger.log("Start Network.get_nodes(self)")
        # Implementation goes here
        Logger.log("End Network.get_nodes(self)")
    
    # ADDS AN EDGE BETWEEN TWO NODES
    def add_edge(self, node_a, node_b):
        """
        Adds an edge between two nodes.
        
        :param node_a: The first node.
        :param node_b: The second node.
        """
        Logger.log(f"Start Network.add_edge(self, node_a={node_a}, node_b={node_b})")
        # Implementation goes here
        Logger.log(f"End Network.add_edge(self, node_a={node_a}, node_b={node_b})")
    
    # REMOVES AN EDGE BETWEEN TWO NODES
    def remove_edge(self, node_a, node_b):
        """
        Removes the edge between two nodes.
        
        :param node_a: The first node.
        :param node_b: The second node.
        """
        Logger.log(f"Start Network.remove_edge(self, node_a={node_a}, node_b={node_b})")
        # Implementation goes here
        Logger.log(f"End Network.remove_edge(self, node_a={node_a}, node_b={node_b})")

    
    # RETURNS ALL EDGES IN THE NETWORK
    def get_edges(self):
        """
        Returns all edges in the network as a list of tuples.
        """
        Logger.log("Start Network.get_edges(self)")
        # Implementation goes here
        Logger.log("End Network.get_edges(self)")

    # UPDATES A NETWORK PROPERTY
    def update_property(self, key, value):
        """
        Updates a network property with the given key and value.
        
        :param key: The property name.
        :param value: The new value for the property.
        """
        Logger.log(f"Start Network.update_property(self, key={key}, value={value})")
        # Implementation goes here
        Logger.log(f"End Network.update_property(self, key={key}, value={value})")
    
    # RETURNS A SPECIFIC NETWORK PROPERTY
    def get_property(self, key):
        """
        Returns the value of a specified network property.
        
        :param key: The property name.
        """
        Logger.log(f"Start Network.get_property(self, key={key})")
        # Implementation goes here
        Logger.log(f"End Network.get_property(self, key={key})")
    
    # REMOVES A NETWORK PROPERTY
    def remove_property(self, key):
        """
        Removes a specified network property.
        
        :param key: The property name to be removed.
        """
        Logger.log(f"Start Network.remove_property(self, key={key})")
        # Implementation goes here
        Logger.log(f"End Network.remove_property(self, key={key})")
    
    # RETURNS NEIGHBORS OF A GIVEN NODE
    def get_neighbors(self, node):
        """
        Returns the neighbors of a given node.
        
        :param node: The node whose neighbors are to be retrieved.
        """
        Logger.log(f"Start Network.get_neighbors(self, node={node})")
        # Implementation goes here
        Logger.log(f"End Network.get_neighbors(self, node={node})")
    
    # FINDS SHORTEST PATH BETWEEN TWO NODES USING BFS
    def find_shortest_path(self, start_node, end_node):
        """
        Finds the shortest path between two nodes using BFS.
        
        :param start_node: The starting node.
        :param end_node: The target node.
        """
        Logger.log(f"Start Network.find_shortest_path(self, start_node={start_node}, end_node={end_node})")
        # Implementation goes here
        Logger.log(f"End Network.find_shortest_path(self, start_node={start_node}, end_node={end_node})")
    
