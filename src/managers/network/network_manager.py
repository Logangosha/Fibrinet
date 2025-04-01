from utils.logger.logger import Logger
from .degradation_engine.no_physics import NoPhysics
from .network_state_manager import NetworkStateManager

class NetworkManager:
    """
    Manages network operations and handles logging related to network events.
    """
    # NETWORKMANAGER INITIALIZATION
    def __init__(self):
        """
        Initializes the NetworkManager instance
        """
        Logger.log(f"start NetworkManager __init__(self)")
        self.network = None
        self.state_manager = NetworkStateManager()
        self.degradation_engine_strategy = NoPhysics()
        Logger.log(f"end NetworkManager __init__(self)")

    # SET NETWORK
    def set_network(self, network):
        """
        Sets the network attribtue to network. 

        Args: 
        network: this is a Network object. 
        """
        Logger.log(f"start set_network(self, {network})")
        self.network = network
        Logger.log(f"end set_network_(self, network)")

    # GET BASE NETWORK
    def get_base_network(self):
        """
        Gets the network attribtue.  
        """
        Logger.log(f"start set_network(self)")
        Logger.log(f"end set_network_(self, network)")
        return self.state_manager.get_base_network_state()
    
    # GET LATEST NETWORK
    def get_network(self):
        """
        Gets the latest network attribtue from network state manager.  
        """
        Logger.log(f"start set_network(self)")
        Logger.log(f"end set_network_(self, network)")
        return self.network

    # DEGRADE EDGE
    def degrade_edge(self, edge_id):
        """  
        """
        Logger.log(f"start degrade_edge(self, {edge_id})")
        self.network = self.degradation_engine_strategy.degrade_edge(self.network, edge_id)
        self.state_manager.add_new_network_state(self.network)
        Logger.log(f"end degrade_edge(self, edge_id)")

    # DEGRADE NODE
    def degrade_node(self, node_id):
        """  
        """
        Logger.log(f"start degrade_node(self, {node_id})")
        self.network = self.degradation_engine_strategy.degrade_node(self.network, node_id)
        self.state_manager.add_new_network_state(self.network)
        Logger.log(f"end degrade_node(self, node_id)")

    # UNDO DEGRADATION
    def undo_degradation(self):
        """ 
        """
        Logger.log(f"start undo_degradation(self)")
        self.state_manager.undo_last_network_state()
        self.network = self.state_manager.current_state
        Logger.log(f"end undo_degradation(self)")

    # REDO DEGRADATION
    def redo_degradation(self):
        """ 
        """
        Logger.log(f"start redo_degradation(self)")
        self.state_manager.redo_last_network_state()
        self.network = self.state_manager.current_state
        Logger.log(f"end redo_degradation(self)")

    # MODIFY NETWORK PROPERTIES
    def modify_network_properties(self, network_properties):
        """
        """
        Logger.log(f"start modify_network_properties(self, {network_properties})")
        Logger.log(f"end modify_network_properties(self, network_properties)")

    # SET DEGRADATION ENGINE STRATEGY
    def set_degradation_engine_strategy(self, degradation_engine_strategy):
        """
        """
        Logger.log(f"start set_degradation_engine_strategy(self, {degradation_engine_strategy})")
        if degradation_engine_strategy:
            self.degradation_engine_strategy = degradation_engine_strategy
        Logger.log(f"end set_degradation_engine_strategy(self, degradation_engine_strategy)")

    # RESET NETWORK STATE
    def reset_network_state_manager(self):
        """
        Resets the network state manager and clears the history.
        """
        Logger.log(f"start reset_network_state(self)")
        self.state_manager.reset_network_state()
        Logger.log(f"end reset_network_state(self)")