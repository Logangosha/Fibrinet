from utils.logger.logger import Logger
from .networks.base_network import BaseNetwork

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
        self.undo_disabled = True             # FLAG TO ENABLE/DISABLE UNDO
        self.redo_disabled = True             # FLAG TO ENABLE/DISABLE REDO
        self.export_disabled = True           # FLAG TO ENABLE/DISABLE EXPORT
        Logger.log(f"end NetworkStateManager__init__")

    # ADDS NEW NETWORK STATE
    def add_new_network_state(self, network_state: BaseNetwork):
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
        self.undo_disabled = len(self.network_state_history) <= 1

        # DISABLE REDO FUNCTIONALITY
        self.redo_disabled = True
        
        # ENABLE EXPORT IF MORE THAN ONE STATE EXISTS
        self.export_disabled = len(self.network_state_history) <= 1

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
        
        # ENABLE EXPORT IF MORE THAN ONE STATE EXISTS
        self.export_disabled = len(self.network_state_history) <= 1

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

        # ENABLE EXPORT IF MORE THAN ONE STATE EXISTS
        self.export_disabled = len(self.network_state_history) <= 1
        
        Logger.log("end redo_last_network_state")

    # RETURNS THE BASE NETWORK STATE IN THE HISTORY
    def get_base_network_state(self):
        """
        Returns the base network state in the history (position 0).
        """
        Logger.log("start get_base_network_state()")
        
        # RETURN THE BASE STATE IF IT EXISTS
        if self.network_state_history:
            base_state = self.network_state_history[0]
            Logger.log("end get_base_network_state")
            return base_state
        
        Logger.log("end get_base_network_state - no states in history")
        return None  # Return None if there are no states in history
    
    def reset_network_state(self):
        """
        Resets the network state manager, clearing the history and setting the current state to None.
        """
        Logger.log("start reset_network_state()")
        
        # Clear the network state history
        self.network_state_history = []
        
        # Reset the current state and network state index
        self.current_state = None
        self.current_network_state_index = 0
        
        # Re-enable or disable flags based on reset state
        self.undo_disabled = True
        self.redo_disabled = True
        self.export_disabled = True
        
        Logger.log("end reset_network_state()")

