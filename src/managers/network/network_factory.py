from utils.logger.logger import Logger

# TYPES OF NETWORKS
from .networks.network_2d import Network2D

# TYPES OF NODES
from .nodes.node_2d import Node2D

# TYPES OF EDGES
from .edges.edge_2d import Edge2D

class NetworkFactory:
    """
    A factory class that creates networks, nodes, and edges based on the provided data.
    It registers network types, node types, and edge types, and is responsible for creating networks
    with the appropriate nodes and edges by matching the data schema.
    """
    # DICTIONARY TO STORE REGISTERED NETWORK TYPES
    _network_types = {}
    # DICTIONARY TO STORE REGISTERED NODE TYPES
    _node_types = {}
    # DICTIONARY TO STORE REGISTERED EDGE TYPES
    _edge_types = {}

    @classmethod
    def register_network_type(cls, network_type, network_class):
        """
        Registers a network type with its corresponding network class.

        :param network_type: The type of the network (e.g., "2D").
        :param network_class: The class associated with the network type.
        """
        # LOGGING THE REGISTRATION OF NETWORK TYPE
        Logger.log(f"Registering network type '{network_type}' with class {network_class}")
        cls._network_types[network_type] = network_class

    @classmethod
    def register_node_type(cls, network_type, node_class):
        """
        Registers a node type with its corresponding node class.

        :param network_type: The type of the network (e.g., "2D").
        :param node_class: The class associated with the node type.
        """
        # LOGGING THE REGISTRATION OF NODE TYPE
        Logger.log(f"Registering node type '{network_type}' with class {node_class}")
        cls._node_types[network_type] = node_class

    @classmethod
    def register_edge_type(cls, network_type, edge_class):
        """
        Registers an edge type with its corresponding edge class.

        :param network_type: The type of the network (e.g., "2D").
        :param edge_class: The class associated with the edge type.
        """
        # LOGGING THE REGISTRATION OF EDGE TYPE
        Logger.log(f"Registering edge type '{network_type}' with class {edge_class}")
        cls._edge_types[network_type] = edge_class

    @classmethod
    def create_network(cls, data: dict):
        """
        Creates a network based on the provided data and matches the schema to the registered types.

        :param data: The data containing information about nodes, edges, and schema for the network.
        :return: The created network object based on the data and schema.
        :raises ValueError: If no matching network type is found or schema mismatch occurs.
        """
        Logger.log(f"start create_network(self, {data})")

        # ITERATE THROUGH REGISTERED NETWORK TYPES TO FIND A MATCHING ONE
        for network_type, network_class in cls._network_types.items():
            if cls._matches_schema(data, network_class.schema):
                # LOGGING MATCHING NETWORK TYPE FOUND
                Logger.log(f"Found matching network type '{network_type}'")

                nodes = []
                node_data = data.get("nodes", {})

                if node_data:
                    # LOGGING PROCESSING NODE DATA
                    Logger.log("Processing node data...")
                    node_list = []
                    keys = list(node_data.keys())
                    for i in range(len(node_data[keys[0]])):
                        node_dict = {key: node_data[key][i] for key in keys}
                        node_list.append(node_dict)
                    
                    for node in node_list:
                        node_class = cls._node_types.get(network_type)
                        if node_class:
                            nodes.append(node_class(node))
                        else:
                            raise ValueError(f"No matching node type found for network type: {network_type}")
                data["nodes"] = nodes  # REPLACE ORIGINAL DATA WITH Node2D OBJECTS

                edges = []
                edge_data = data.get("edges", {})
                
                if edge_data:
                    # LOGGING PROCESSING EDGE DATA
                    Logger.log("Processing edge data...")
                    edge_list = []
                    keys = list(edge_data.keys())
                    for i in range(len(edge_data[keys[0]])):
                        edge_dict = {key: edge_data[key][i] for key in keys}
                        edge_list.append(edge_dict)
                    
                    for edge in edge_list:
                        edge_class = cls._edge_types.get(network_type)
                        if edge_class:
                            edges.append(edge_class(edge))
                        else:
                            raise ValueError(f"No matching edge type found for network type: {network_type}")
                data["edges"] = edges  # REPLACE ORIGINAL DATA WITH Edge2D OBJECTS

                # CREATE THE NETWORK USING THE CLASS FOUND
                network = network_class(data) 
                Logger.log(f"Network created successfully: {network}")
                Logger.log("start create_network(self, data)")

                return network

        raise ValueError("No matching network type found.")

    @classmethod
    def _matches_schema(cls, data:dict, schema):
        """
        Matches the provided data with the schema.

        :param data: The data to be validated against the schema.
        :param schema: The schema to match the data against.
        :return: True if the data matches the schema, False otherwise.
        """
        Logger.log(f"start _matches_schema(self, {data})")

        meta_data = data.get("meta_data", {})
        nodes = data.get("nodes", {})
        edges = data.get("edges", {})

        # CHECKING META_DATA
        Logger.log("Checking meta_data...")
        for attr in schema.get("meta_data", []):
            if attr not in meta_data:
                # LOGGING MISSING META_DATA ATTRIBUTE
                Logger.log(f"meta_data: Attribute '{attr}' not found in data. Schema mismatch.")
                return False
            else:
                # LOGGING FOUND META_DATA ATTRIBUTE
                Logger.log(f"meta_data: Attribute '{attr}' found.")
        # LOGGING META_DATA CHECK COMPLETE
        Logger.log("meta_data check complete.")

        # CHECKING NODES
        if nodes:
            Logger.log("Checking nodes...")
            keys = list(nodes.keys())
            for i in range(len(nodes[keys[0]])):
                node = {key: nodes[key][i] for key in keys}
                for attr in schema.get("node_attributes", []):
                    if attr not in node:
                        # LOGGING MISSING NODE ATTRIBUTE
                        Logger.log(f"nodes: Attribute '{attr}' not found in node {node}. Schema mismatch.")
                        return False
                    else:
                        # LOGGING FOUND NODE ATTRIBUTE
                        Logger.log(f"nodes: Attribute '{attr}' found in node {node}.")
            # LOGGING NODES CHECK COMPLETE
            Logger.log("nodes check complete.")
        else:
            # LOGGING NO NODES FOUND
            Logger.log("No nodes found in data.")

        # CHECKING EDGES
        if edges:
            Logger.log("Checking edges...")
            keys = list(edges.keys())
            for i in range(len(edges[keys[0]])):
                edge = {key: edges[key][i] for key in keys}
                for attr in schema.get("edge_attributes", []):
                    if attr not in edge:
                        # LOGGING MISSING EDGE ATTRIBUTE
                        Logger.log(f"edges: Attribute '{attr}' not found in edge {edge}. Schema mismatch.")
                        return False
                    else:
                        # LOGGING FOUND EDGE ATTRIBUTE
                        Logger.log(f"edges: Attribute '{attr}' found in edge {edge}.")
            # LOGGING EDGES CHECK COMPLETE
            Logger.log("edges check complete.")
        else:
            # LOGGING NO EDGES FOUND
            Logger.log("No edges found in data.")

        # LOGGING SCHEMA MATCH SUCCESSFUL
        Logger.log("Schema matching successful.")
        Logger.log("end _matches_schema(self, data)")
        return True

# REGISTER NETWORK, NODE, AND EDGE TYPES
Logger.log(f"Registering types with factory...)")
NetworkFactory.register_network_type("2D", Network2D)
NetworkFactory.register_node_type("2D", Node2D)
NetworkFactory.register_edge_type("2D", Edge2D)
