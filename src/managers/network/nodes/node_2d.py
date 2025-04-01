from .base_node import BaseNode

class Node2D(BaseNode):
    schema = BaseNode.get_schema().union({"n_x", "n_y"})