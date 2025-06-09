from utils.logger.logger import Logger
from .degradation_engine_strategy import DegradationEngineStrategy
from ..networks.network_2d import Network2D
import copy
import numpy as np

class TwoDimensionalSpringForceDegradationEngineWithoutBiomechanics(DegradationEngineStrategy):
    """
    Degrades a 2D spring network by removing edges or nodes and recalculating equilibrium
    based on Hooke's Law, without considering biological forces.
    """

    def degrade_edge(self, network: Network2D, edge_id):
        Logger.log(f"start degrade_edge(self, network, {edge_id})")

        # Step 1: Copy the network to avoid in-place changes
        degraded_network = copy.deepcopy(network)

        # Step 2: Remove the specified edge
        degraded_network.remove_edge(edge_id)

        # Step 3: Relax the network to restore equilibrium
        self.relax_network(degraded_network)

        Logger.log(f"end degrade_edge(self, network, {edge_id})")
        return degraded_network

    def degrade_node(self, network: Network2D, node_id):
        Logger.log(f"start degrade_node(self, network, {node_id})")

        # Step 1: Deep copy the network
        degraded_network = copy.deepcopy(network)

        # Step 2: Remove the node
        degraded_network.remove_node(node_id)

        # Step 3: Remove all edges connected to that node
        connected_edges = [
            edge.get_id() for edge in degraded_network.get_edges()
            if edge.n_from == node_id or edge.n_to == node_id
        ]
        for eid in connected_edges:
            degraded_network.remove_edge(eid)

        # Step 4: Relax the network to find new equilibrium
        self.relax_network(degraded_network)

        Logger.log(f"end degrade_node(self, network, {node_id})")
        return degraded_network

    def relax_network(self, network: Network2D):
        """
        Applies a physics-based relaxation method using Hooke's Law to update node positions.
        """
        Logger.log(f"start 2dwithoutbio relax_network(self, network={network})")
        iterations = 1000
        alpha = 0.01
        tolerance = 1e-5
        # LOOP FOR A MAXIMUM NUMBER OF ITERATIONS TO RELAX THE NETWORK
        for _ in range(iterations):
            # COMPUTE THE FORCES ON EACH NODE USING HOOKE'S LAW
            forces = self.compute_node_forces(network)
            max_force = 0.0  # INITIALIZE THE MAX FORCE TO ZERO

            # ITERATE OVER ALL NODES IN THE NETWORK
            for node in network.get_nodes():
                # SKIP NODES THAT ARE FIXED IN PLACE
                if getattr(node, 'is_fixed', False):
                    continue

                # GET THE FORCE VECTOR FOR THE CURRENT NODE
                force = forces[node.get_id()]
                # UPDATE THE MAXIMUM FORCE VALUE
                max_force = max(max_force, np.linalg.norm(force))

                # UPDATE NODE POSITION IN THE DIRECTION OF THE FORCE (GRADIENT DESCENT STYLE)
                node.n_x += alpha * force[0]
                node.n_y += alpha * force[1]

            # IF MAXIMUM FORCE IS BELOW THE TOLERANCE, STOP EARLY (CONVERGENCE REACHED)
            if max_force < tolerance:
                break
        Logger.log(f"end 2dwithoutbio relax_network(self, network={network})")

    def compute_node_forces(self, network: Network2D):
        """
        Computes net spring force on each node using Hooke's law.
        """
        # INITIALIZE ZERO FORCE VECTORS FOR ALL NODES
        forces = {node.get_id(): np.array([0.0, 0.0]) for node in network.get_nodes()}
        # GET SPRING STIFFNESS CONSTANT (DEFAULT TO 1.0 IF NOT SPECIFIED)
        k = network.meta_data.get("spring_stiffness_constant", 1.0)

        # LOOP OVER ALL EDGES TO COMPUTE SPRING FORCES
        for edge in network.get_edges():
            # GET NODE OBJECTS FOR BOTH ENDS OF THE EDGE
            n_from = network.get_node_by_id(edge.n_from)
            n_to = network.get_node_by_id(edge.n_to)

            # GET POSITION VECTORS FOR BOTH NODES
            p_from = np.array([n_from.n_x, n_from.n_y])
            p_to = np.array([n_to.n_x, n_to.n_y])

            # COMPUTE VECTOR AND LENGTH BETWEEN NODES
            vector = p_to - p_from
            length = np.linalg.norm(vector)

            # SKIP ZERO-LENGTH EDGES TO AVOID DIVISION BY ZERO
            if length == 0:
                continue

            # COMPUTE UNIT VECTOR FROM n_from TO n_to
            unit_vector = vector / length
            # GET REST LENGTH OF SPRING (DEFAULT TO CURRENT LENGTH IF NOT PROVIDED)
            rest_length = getattr(edge, "rest_length", length)

            # COMPUTE SPRING FORCE USING HOOKE’S LAW: F = -k * (x - x₀)
            force_magnitude = k * (length - rest_length)
            force = force_magnitude * unit_vector

            # APPLY EQUAL AND OPPOSITE FORCES TO THE TWO CONNECTED NODES
            forces[n_from.get_id()] += force
            forces[n_to.get_id()] -= force

        # RETURN DICTIONARY OF FORCE VECTORS FOR EACH NODE
        return forces


    def get_edge_rest_lengths(self, network: Network2D):
        """
        Returns a list of rest lengths for all edges.
        """
        return [edge.rest_length for edge in network.get_edges()]
