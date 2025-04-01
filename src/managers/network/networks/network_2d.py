from utils.logger.logger import Logger
from ..nodes.node_2d import Node2D
from ..edges.edge_2d import Edge2D
from .base_network import BaseNetwork

class Network2D(BaseNetwork):
    schema = {
        "meta_data": ["network_size", "total_tension", "type"],
        "node_attributes": Node2D.get_schema(),
        "edge_attributes": Edge2D.get_schema(),
    }

    def __init__(self, data):
        Logger.log(f"start Network2D __init__(self, {data})")
        meta_data = data.get("meta_data", {})
        nodes = data.get("nodes", []) 
        edges = data.get("edges", [])
        super().__init__(nodes=nodes, edges=edges, meta_data=meta_data, schema=Network2D.schema) # Pass the nodes and edges to the base class
        Logger.log(f"end Network2D __init__(self, {data})")