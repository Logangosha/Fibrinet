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
        self.submit_view_request("cli")  

        Logger.log("end SystemControllerInterface__init__(self)")



    # HANDLES NETWORK INPUT
    def input_network(self, input_data):
        """
        Handles network input data.
        
        :param input_data: file path received as system input.
        """
        
        Logger.log(f"start input_network(self, {input_data})")
        self.network_manager.set_network(self.input_manager.get_network(input_data))
        Logger.log(f"end input_network(self, input_data)")


    # MODIFIES NETWORK CONFIGURATION IF STATE ALLOWS
    def modify_network(self, modification_request):
        """
        Modifies network configuration if the network is loaded.
        
        :param modification_request: Request containing network modification details.
        :raises StateTransitionError: If the network is not loaded.
        """
        

        Logger.log(f"start modify_network(self, {modification_request})")
        if self.state.network_loaded:
            Logger.log("Network modification request processed.")
            pass
        else:
            Logger.log("StateTransitionError: Cannot modify network, network not loaded.", Logger.LogPriority.ERROR)
            raise StateTransitionError()
        Logger.log(f"end modify_network(self, modification_request)")
        


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
    def submit_view_request(self, view_request):
        """
         Submits a view request to the view manager.
        
        :param view_request: Type of view requested (e.g., CLI, etc.).
        """
        
        Logger.log(f"start submit_view_request(self, {view_request})")
        self.view_manager.handle_view_request(view_request, self)
        Logger.log(f"end submit_view_request(self, view_request)")


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


        
