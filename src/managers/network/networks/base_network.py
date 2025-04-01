from utils.logger.logger import Logger

class BaseNetwork:
    """
    Represents a network containing nodes, edges, and metadata.
    """

    def __init__(self, nodes=None, edges=None, meta_data=None, schema=None):
        """
        Initializes the network with nodes, edges, and metadata.

        Params:
            nodes: List of nodes in the network (default: empty list).
            edges: List of edges in the network (default: empty list).
            meta_data: Dictionary containing additional metadata (default: empty dict).
            schema: Dictionary defining the schema (default: empty dict).
        """
        Logger.log(f"start BaseNetwork __init__(self, {nodes}, {edges}, {meta_data}, {schema})")
        # INITIALIZE NETWORK PROPERTIES
        self.nodes = nodes or []
        self.edges = edges or []
        self.meta_data = meta_data or {}
        self.schema = schema or {}

        Logger.log("===== Network Properties =====")

        # LOG NODES INFORMATION
        Logger.log("Nodes:")
        for node in self.nodes:
            Logger.log(f"{node.__dict__}")

        # LOG EDGES INFORMATION
        Logger.log("Edges:")
        for edge in self.edges:
            Logger.log(f"{edge.__dict__}")

        # LOG META DATA INFORMATION
        Logger.log("Meta Properties:")
        for key, value in self.meta_data.items():
            Logger.log(f"{key}: {value}")

        Logger.log("==============================")
        Logger.log("end BaseNetwork __init__(self, nodes, edges, meta_data, schema)")


    def get_nodes(self):
        """
        Returns the list of nodes in the network.
        """
        return self.nodes

    def get_edges(self):
        """
        Returns the list of edges in the network.
        """
        return self.edges

    def get_meta_data(self):
        """
        Returns the metadata dictionary of the network.
        """
        return self.meta_data

    def add_node(self, node):
        """
        Adds a node to the network.

        Params:
            node: The node object to add.
        """
        # ADD NODE TO NETWORK
        self.nodes.append(node)

    def remove_node(self, node_id):
        """
        Removes a node from the network by its ID.

        Params:
            node_id: The ID of the node to remove.
        """
        # REMOVE NODE BY FILTERING OUT MATCHING NODE ID
        self.nodes = [node for node in self.nodes if node.get_id() != node_id]

    def add_edge(self, edge):
        """
        Adds an edge to the network.

        Params:
            edge: The edge object to add.
        """
        # ADD EDGE TO NETWORK
        self.edges.append(edge)

    def remove_edge(self, edge_id):
        """
        Removes an edge from the network by its ID.

        Params:
            edge_id: The ID of the edge to remove.
        """
        # REMOVE EDGE BY FILTERING OUT MATCHING EDGE ID
        self.edges = [edge for edge in self.edges if edge.get_id() != edge_id]

    def get_node_by_id(self, node_id):
        """
        Retrieves a node by its ID.

        Params:
            node_id: The ID of the node to find.

        Returns:
            The node object if found, otherwise None.
        """
        # SEARCH FOR NODE BY ID
        for node in self.nodes:
            if node.get_id() == node_id:
                return node
        return None

    def get_edge_by_id(self, edge_id):
        """
        Retrieves an edge by its ID.

        Params:
            edge_id: The ID of the edge to find.

        Returns:
            The edge object if found, otherwise None.
        """
        # SEARCH FOR EDGE BY ID
        for edge in self.edges:
            if edge.get_id() == edge_id:
                return edge
        return None
