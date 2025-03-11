from src.managers.input.input_manager import InputManager
from src.managers.view.view_manager import ViewManager
from src.managers.export.export_manager import ExportManager
from src.managers.network.network_manager import NetworkManager
from utils.logger.logger import Logger
from utils.logger.local_file_strategy import LocalFileStrategy
from src.models.system_state import SystemState
from src.models.exceptions import StateTransitionError

class SystemControllerInterface:
    """
    Main controller interface responsible for managing system components such as input, view, export, 
    network, and logging. Ensures proper state transitions and handles requests.
    """
    # INITIALIZES SYSTEM CONTROLLER AND MANAGERS
    def __init__(self):
        """
        Initializes the system controller and its managers.
        Sets up the default Logger and CLI view.
        """

        # INITIALIZES MANAGERS
        Logger.log("start SystemControllerInterface__init__(self)")
        self.input_manager = InputManager()
        self.view_manager = ViewManager(self)
        self.export_manager = ExportManager()
        self.network_manager = NetworkManager()
        self.state = SystemState()
        
        Logger.log("SystemControllerInterface initialized.")
        
        # SUBMITS DEFAULT CLI VIEW REQUEST
        Logger.log("Submiting default cli view request")
        self.initiate_view("cli")  

        Logger.log("end SystemControllerInterface__init__(self)")

    # HANDLES NETWORK INPUT
    def input_network(self, input_data):
        """
        Handles network input data.
        
        :param input_data: file path received as system input.
        """
        
        Logger.log(f"start input_network(self, {input_data})")
        try: 
            Logger.log("Setting network from input_manager network")
            self.network_manager.set_network(self.input_manager.get_network(input_data))
            self.network_manager.state_manager.add_new_network_state(self.network_manager.network)
        except Exception as ex: raise ex
        Logger.log(f"Is a network loaded? {bool(self.network_manager.network)}")
        if self.network_manager.network:
            Logger.log("Setting system state to network loaded true")
            self.state.network_loaded = True
        
        Logger.log(f"end input_network(self, input_data)")     
    
    # DEGRADES A SPECIFIED NETWORK EDGE IF STATE ALLOWS
    def degrade_edge(self, edge_id):
        """
        Degrades a specified network edge if the network is loaded.
        
        :param edge: The edge to be degraded.
        :raises StateTransitionError: If the network is not loaded.
        """
        
        Logger.log(f"start degrade_edge(self, {edge_id})")
        if self.state.network_loaded:
            self.network_manager.degrade_edge(edge_id)
        else:
            Logger.log("StateTransitionError: Cannot modify network, network not loaded.", Logger.LogPriority.ERROR)
            raise StateTransitionError()
        Logger.log(f"end degrade_edge(self, {edge_id})")

    # DEGRADES A SPECIFIED NETWORK NODE IF STATE ALLOWS
    def degrade_node(self, node_id):
        """
        Degrades a specified network node if the network is loaded.
        
        :param node: The node to be degraded.
        :raises StateTransitionError: If the network is not loaded.
        """
        
        Logger.log(f"start degrade_node(self, {node_id})")
        if self.state.network_loaded:
            self.network_manager.degrade_node(node_id)
        else:
            Logger.log("StateTransitionError: Cannot modify network, network not loaded.", Logger.LogPriority.ERROR)
            raise StateTransitionError()
        Logger.log(f"end degrade_node(self, {node_id})")

    # UNDOES THE LAST NETWORK DEGRADATION IF STATE ALLOWS
    def undo_degradation(self):
        """
        Undoes the last degradation applied to the network if the network is loaded.
        
        :raises StateTransitionError: If the network is not loaded.
        """
        
        Logger.log(f"start undo_degradation(self)")
        if self.state.network_loaded:
            self.network_manager.undo_degradation()
        else:
            Logger.log("StateTransitionError: Cannot modify network, network not loaded.", Logger.LogPriority.ERROR)
            raise StateTransitionError()
        Logger.log(f"end undo_degradation(self)")

    # REDOES THE LAST NETWORK DEGRADATION IF STATE ALLOWS
    def redo_degradation(self):
        """
        Redoes the last degradation applied to the network if the network is loaded.
        
        :raises StateTransitionError: If the network is not loaded.
        """
        
        Logger.log(f"start redo_degradation(self)")

        if self.state.network_loaded:
            self.network_manager.redo_degradation()
        else:
            Logger.log("StateTransitionError: Cannot modify network, network not loaded.", Logger.LogPriority.ERROR)
            raise StateTransitionError()
        Logger.log(f"end redo_degradation(self)")

    # MODIFIES NETWORK PROPERTIES IF STATE ALLOWS
    def modify_network_properties(self, network_properties):
        """
        Modifies the properties of the network if the network is loaded.
        
        :param network_properties: Dictionary containing network property modifications.
        :raises StateTransitionError: If the network is not loaded.
        """
        
        Logger.log(f"start modify_network_properties(self, {network_properties})")
        if self.state.network_loaded:
            self.network_manager.redo_degradation(network_properties)
        else:
            Logger.log("StateTransitionError: Cannot modify network, network not loaded.", Logger.LogPriority.ERROR)
            raise StateTransitionError()
        Logger.log(f"end modify_network_properties(self, {network_properties})")


     # MODIFIES NETWORK PROPERTIES IF STATE ALLOWS
    
    # SETS DEGRADATION ENGINE STRATEGY
    def set_degradation_engine_strategy(self, degradation_engine_strategy):
        """
        Sets degradation engine strategy of network manager. 
        
        :param degradation_engine_strategy: Concrete strategy instance of DegradationEngineStrategy
        :raises StateTransitionError: If the network is not loaded.
        """
        
        Logger.log(f"start set_degradation_engine_strategy(self, {degradation_engine_strategy})")
        self.network_manager.set_degradation_engine_strategy(degradation_engine_strategy)
        Logger.log(f"end set_degradation_engine_strategy(self, {degradation_engine_strategy})")

    # EXPORTS DATA IF NETWORK IS LOADED AND MODIFIED
    def export_data(self, export_request):
        """
        Exports data if the network is loaded and has been modified.
        
        :param export_request: Request specifying export details.
        :raises StateTransitionError: If the state is invalid for export.
        """
        

        Logger.log(f"start export_data(self, {export_request})")
        if self.state.network_loaded and self.state.network_modified:
            Logger.log("Export request processed successfully.")
            pass
        else:
            Logger.log("StateTransitionError: Cannot export data, invalid state.", Logger.LogPriority.ERROR)
            raise StateTransitionError()
        Logger.log(f"end export_data(self, export_request)")

    # SUBMITS A VIEW REQUEST TO THE VIEW MANAGER
    def initiate_view(self, view):
        """
         Submits a view request to the view manager.
        
        :param view: Type of view requested (e.g., CLI, etc.).
        """
        
        Logger.log(f"start initiate_view(self, {view})")
        self.view_manager.initiate_view_strategy(view, self)
        Logger.log(f"end initiate_view(self, view)")

    # CONFIGURES Logger BASED ON PROVIDED SETTINGS
    def configure_Logger(self, enabled, **kwargs):
        """
        Configures the Logger with a specified storage strategy.
        
        :param kwargs: Dictionary containing storage strategy option and details.
        :raises ValueError: If storage strategy is invalid.
        """
        

        Logger.log(f"start configure_Logger(self, {enabled}, {kwargs})")
        if enabled: Logger.enable_logging()
        else: Logger.disable_logging()
        storage_strategy = kwargs.get("storage_strategy", None)
        if storage_strategy is not None:
            if storage_strategy == "file":
                file_location = kwargs.get("file_location", None)
                if not file_location:
                    raise ValueError("file_location must be provided for 'file' storage strategy.")
                
                # SETS FILE-BASED LOGGING STRATEGY
                Logger.set_log_storage_strategy(LocalFileStrategy(file_location))
                Logger.log(f"Logger set to file storage at {file_location}.")
        else:
            # DEFAULT ONLY ENABLES / DISABLES CURRENT LOGGING STRATEGY
            pass
        Logger.log(f"end configure_Logger(self, **kwargs)")


        
