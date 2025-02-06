class SystemState:
    """
    Represents the current state of the system, tracking various flags and the active view.
    """

    # INITIALIZES THE SYSTEM STATE WITH DEFAULT VALUES.
    def __init__(self):
        """
        Initializes the system's state attributes such as network status and the current view.
        """
        self.network_loaded = False          
        self.network_modified = False  
        self.current_view = None
