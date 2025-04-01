from .base_edge import BaseEdge

class Edge2D(BaseEdge):
    schema = BaseEdge.get_schema().union({"n_from", "n_to"})