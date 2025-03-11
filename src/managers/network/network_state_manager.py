from utils.logger.logger import Logger
from .network import Network

class NetworkStateManager:
    """
    Manages network state history, allowing for undo and redo functionality.
    """
    # INITIALIZES THE NETWORKSTATEMANAGER
    def __init__(self):
        """
        Initializes the NetworkStateManager with an empty network state history and default settings.
        """
        Logger.log(f"start NetworkStateManager__init__")
        self.network_state_history = []       # LIST TO STORE NETWORK STATE HISTORY
        self.current_state = None             # CURRENT ACTIVE NETWORK STATE
        self.current_network_state_index = 0  # INDEX OF THE CURRENT NETWORK STATE IN HISTORY
        self.undo_disabled = False            # FLAG TO ENABLE/DISABLE UNDO
        self.redo_disabled = False            # FLAG TO ENABLE/DISABLE REDO
        Logger.log(f"end NetworkStateManager__init__")

    # ADDS NEW NETWORK STATE
    def add_new_network_state(self, network_state: Network):
        """
        Adds a new network state to the history and updates the current network state.
        Disables redo functionality since a new network state invalidates future states.

        :param network_state: The new network state to be added.
        """
        Logger.log(f"start add_new_state({network_state})")
        
        # SLICE THE NETWORK STATE HISTORY TO INCLUDE ITEMS FROM CURRENT NETWORK STATE INDEX AND BACK
        self.network_state_history = self.network_state_history[:self.current_network_state_index + 1]

        # ADD NEW NETWORK STATE TO HISTORY
        self.network_state_history.append(network_state)

        # SET NEW NETWORK STATE AS CURRENT NETWORK STATE
        self.current_state = network_state

        # UPDATE CURRENT NETWORK STATE INDEX TO LAST INDEX OF HISTORY
        self.current_network_state_index = len(self.network_state_history) - 1

        # ENABLE UNDO FUNCTIONALITY
        self.undo_disabled = False

        # DISABLE REDO FUNCTIONALITY
        self.redo_disabled = True
        Logger.log("end add_new_state")

    # UNDO LAST NETWORK STATE
    def undo_last_network_state(self):
        """
        Reverts to the previous NETWORK STATE if undo is available.
        """
        Logger.log("start undo_last_state()")
        
        # CHECK IF UNDO IS DISABLED OR AT INITIAL NETWORK STATE
        if self.undo_disabled or self.current_network_state_index == 0:
            return
        
        # MOVE TO PREVIOUS NETWORK STATE
        self.current_network_state_index -= 1
        self.current_state = self.network_state_history[self.current_network_state_index]

        # ENABLE REDO FUNCTIONALITY
        self.redo_disabled = False

        # DISABLE UNDO IF AT INITIAL NETWORK STATE
        if self.current_network_state_index == 0:
            self.undo_disabled = True
        
        Logger.log("end undo_last_state")

    # REDO LAST NETWORK STATE
    def redo_last_network_state(self):
        """
        Moves forward to the next network state if redo is available.
        """
        Logger.log("start redo_last_network_state()")
        
        # CHECK IF REDO IS DISABLED OR AT LAST RECORDED NETWORK STATE
        if self.redo_disabled or self.current_network_state_index >= len(self.network_state_history) - 1:
            return
        
        # MOVE TO NEXT NETWORK STATE
        self.current_network_state_index += 1
        self.current_state = self.network_state_history[self.current_network_state_index]

        # ENABLE UNDO FUNCTIONALITY
        self.undo_disabled = False

        # DISABLE REDO IF AT LAST NETWORK STATE IN HISTORY
        if self.current_network_state_index == len(self.network_state_history) - 1:
            self.redo_disabled = True
        
        Logger.log("end redo_last_network_state")
