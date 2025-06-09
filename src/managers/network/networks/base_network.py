from utils.logger.logger import Logger
from ..nodes.base_node import BaseNode 
from ..edges.base_edge import BaseEdge 

class BaseNetwork:
    """
    Represents a network containing nodes, edges, and metadata.
    """

    allowed_node_type = BaseNode
    allowed_edge_type = BaseEdge
    
    def __init__(self, nodes=None, edges=None, meta_data=None, schema=None):
        """
        Initializes the network with nodes, edges, and metadata.

        Params:
            nodes (list): List of node objects (default: empty list).
            edges (list): List of edge objects (default: empty list).
            meta_data (dict): Metadata dictionary (default: empty dict).
            schema (dict): Schema dict defining allowed keys and types (default: empty dict).
        """
        Logger.log(f"start BaseNetwork __init__(self, {nodes}, {edges}, {meta_data}, {schema})")

        # INITIALIZE NETWORK PROPERTIES
        self.nodes = nodes or []
        self.edges = edges or []
        self.meta_data = meta_data or {}
        self.schema = schema or {
            "meta_data": [],
            "meta_data_types": {},
            "node_attributes": self.allowed_node_type.get_schema(),
            "edge_attributes": self.allowed_edge_type.get_schema(),
        }

        # LOG NETWORK CONTENTS
        Logger.log("===== Network Properties =====")
        Logger.log("Nodes:")
        for node in self.nodes:
            Logger.log(f"{node.__dict__}")
        Logger.log("Edges:")
        for edge in self.edges:
            Logger.log(f"{edge.__dict__}")
        Logger.log("Meta Properties:")
        for key, value in self.meta_data.items():
            Logger.log(f"{key}: {value}")
        Logger.log("==============================")
        Logger.log("end BaseNetwork __init__(self, nodes, edges, meta_data, schema)")

    def safe_cast(self, value, expected_type):
        """
        Attempts to cast the value to the expected type.

        Params:
            value: The value to cast.
            expected_type: The type to cast the value to.

        Returns:
            The casted value.

        Raises:
            ValueError: If casting fails.
        """
        # HANDLE BOOLEAN SPECIAL CASE
        try:
            if expected_type == bool:
                return str(value).strip().lower() in ["true", "1", "yes"]
            return expected_type(value)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid value: '{value}' is not of type {expected_type.__name__}")

    def get_nodes(self):
        """Returns the list of nodes in the network."""
        return self.nodes

    def get_edges(self):
        """Returns the list of edges in the network."""
        return self.edges

    def get_meta_data(self):
        """Returns the metadata dictionary of the network."""
        return self.meta_data

    def add_meta_data(self, key, value):
        """
        Adds a new metadata entry with type checking.

        Params:
            key (str): Metadata key.
            value: Metadata value.

        Raises:
            ValueError: If key is not allowed or value is of wrong type.
        """
        # VALIDATE KEY AGAINST SCHEMA
        if key not in self.schema.get("meta_data", []):
            raise ValueError(f"Meta data key '{key}' is not allowed by the schema.")
        
        # GET EXPECTED TYPE OR FALLBACK TO VALUE TYPE
        expected_type = self.schema.get("meta_data_types", {}).get(key, type(value))

        # CAST VALUE TO EXPECTED TYPE
        value = self.safe_cast(value, expected_type)

        # ADD META DATA IF KEY NOT PRESENT
        if key not in self.meta_data:
            self.meta_data[key] = value
            Logger.log(f"Meta data added: {key} = {value}")
        else:
            Logger.log(f"Meta data key '{key}' already exists. Use update_meta_data to change it.")

    def update_meta_data(self, key, value):
        """
        Updates existing metadata entry with type checking.

        Params:
            key (str): Metadata key.
            value: New metadata value.

        Raises:
            ValueError: If key is not allowed or value is of wrong type.
        """
        # VALIDATE KEY AGAINST SCHEMA
        if key not in self.schema.get("meta_data", []):
            raise ValueError(f"Meta data key '{key}' is not allowed by the schema.")

        # GET EXPECTED TYPE OR FALLBACK TO VALUE TYPE
        expected_type = self.schema.get("meta_data_types", {}).get(key, type(value))

        # CAST VALUE TO EXPECTED TYPE
        value = self.safe_cast(value, expected_type)

        # UPDATE META DATA VALUE
        self.meta_data[key] = value
        Logger.log(f"Meta data updated: {key} = {value}")

    def remove_meta_data(self, key):
        """
        Removes metadata entry if it exists.

        Params:
            key (str): Metadata key to remove.
        """
        if key in self.meta_data:
            del self.meta_data[key]
            Logger.log(f"Meta data removed: {key}")
        else:
            Logger.log(f"Meta data key '{key}' not found.")

    def get_meta_data_keys(self):
        """Returns a list of metadata keys."""
        return list(self.meta_data.keys())

    def add_node(self, node):
        """
        Adds a node to the network.

        Params:
            node (BaseNode): Node object to add.
        """
        Logger.log(f"start network add_node(self, {node})")
        if self.get_node_by_id(node.get_id()) is not None:
            raise ValueError(f"Node with ID '{node.get_id()}' already exists in the network.")
        # ADD NODE TO NETWORK
        self.nodes.append(node)
        Logger.log("end network add_node(self, node)")

    def remove_node(self, node_id):
        """
        Removes a node by ID.

        Params:
            node_id: The ID of the node to remove.
        """
        # FILTER OUT NODE BY ID
        self.nodes = [node for node in self.nodes if node.get_id() != node_id]

    def add_edge(self, edge):
        """
        Adds an edge to the network after validating it connects valid nodes.
        Ensures 'n_from' and 'n_to' are present, exist in the network, and are not the same.

        Params:
            edge (BaseEdge): The edge instance to add.

        Raises:
            ValueError: If 'n_from' or 'n_to' is missing, invalid, or identical.
        """
        Logger.log("start add_edge()")

        # ENSURE EDGE IS NOT ALREADY IN NETWORK
        if self.get_edge_by_id(edge.get_id()) is not None:
            raise ValueError(f"Edge with ID '{edge.get_id()}' already exists in the network.")

        # ENSURE EDGE HAS REQUIRED ATTRIBUTES
        if not hasattr(edge, "n_from") or not hasattr(edge, "n_to"):
            Logger.log("Edge is missing 'n_from' or 'n_to'")
            raise ValueError("Edge must have 'n_from' and 'n_to' attributes.")

        # CHECK THAT 'n_from' AND 'n_to' ARE DIFFERENT
        if edge.n_from == edge.n_to:
            Logger.log(f"Invalid edge: 'n_from' ({edge.n_from}) and 'n_to' are the same")
            raise ValueError("'n_from' and 'n_to' cannot be the same node.")

        # ENSURE REFERENCED NODES EXIST IN NETWORK
        if self.get_node_by_id(edge.n_from) is None:
            Logger.log(f"Invalid 'n_from' reference: {edge.n_from} not found.")
            raise ValueError(f"'n_from' value {edge.n_from} does not exist in network.")

        if self.get_node_by_id(edge.n_to) is None:
            Logger.log(f"Invalid 'n_to' reference: {edge.n_to} not found.")
            raise ValueError(f"'n_to' value {edge.n_to} does not exist in network.")

        # ADD EDGE TO NETWORK
        self.edges.append(edge)
        Logger.log(f"Edge successfully added: {edge.n_from} -> {edge.n_to}")
        Logger.log("end add_edge()")



    def remove_edge(self, edge_id):
        """
        Removes an edge by ID.

        Params:
            edge_id: The ID of the edge to remove.
        """
        # FILTER OUT EDGE BY ID
        self.edges = [edge for edge in self.edges if edge.get_id() != edge_id]

    def get_node_by_id(self, node_id):
        """
        Retrieves a node by ID.

        Params:
            node_id: The ID of the node to find.

        Returns:
            BaseNode or None: Found node or None if not found.
        """
        for node in self.nodes:
            if node.get_id() == node_id:
                return node
        return None

    def get_edge_by_id(self, edge_id):
        """
        Retrieves an edge by ID.

        Params:
            edge_id: The ID of the edge to find.

        Returns:
            BaseEdge or None: Found edge or None if not found.
        """
        for edge in self.edges:
            if edge.get_id() == edge_id:
                return edge
        return None
    
    def log_network(self):
        """Logs the current state of the network: nodes, edges, and metadata."""
        Logger.log("===== Network State =====")
        
        Logger.log("Nodes:")
        for node in self.nodes:
            Logger.log(f"{node.__dict__}")
        
        Logger.log("Edges:")
        for edge in self.edges:
            Logger.log(f"{edge.__dict__}")
        
        Logger.log("Meta Data:")
        for key, value in self.meta_data.items():
            Logger.log(f"{key}: {value}")
        
        Logger.log("=========================")

