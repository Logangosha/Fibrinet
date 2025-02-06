from src.models.observer import Observer
from utils.logger.logger import Logger

class ViewStrategy(Observer):
    """
    Base class for strategies handling different types of views in the application.
    Subclasses should implement methods to handle view requests, updates, and events.
    """

    # VIEWSTRATEGY INITILIZATION
    def __init__(self, controller):
        """
        Initializes the ViewStrategy instance and sets up the controller and Logger.
        
        Parameters:
        controller (Controller): The controller that manages the view's actions.
        """
        

        Logger.log(f"start InputManager __init__(self, {controller})")
        
        # SETTING CONTROLLER
        self.controller = controller
        
        Logger.log(f"end InputManager __init__(self, controller)")

    # HANDLES A REQUEST TO DISPLAY OR INTERACT WITH A SPECIFIC VIEW.
    def handle_view_request(self, view_request):
        """
        Handles a request to display or interact with a specific view.
        
        Parameters:
        view_request (str): The type of request related to the view.
        
        Raises:
        NotImplementedError: If not implemented in a subclass.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO HANDLE VIEW REQUESTS
        raise NotImplementedError()

    # STARTS THE VIEW, INITIALIZING NECESSARY RESOURCES OR DISPLAY MECHANISMS.
    def start_view(self):
        """
        Starts the view, initializing necessary resources or display mechanisms.
        
        Raises:
        NotImplementedError: If not implemented in a subclass.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO START THE VIEW
        raise NotImplementedError()

    # STOPS THE VIEW, RELEASING RESOURCES OR HIDING THE DISPLAY.
    def stop_view(self):
        """
        Stops the view, releasing resources or hiding the display.
        
        Raises:
        NotImplementedError: If not implemented in a subclass.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO STOP THE VIEW
        raise NotImplementedError()

    # UPDATES THE VIEW WITH NEW DATA OR CHANGES.
    def update_view(self, update):
        """
        Updates the view with new data or changes.
        
        Parameters:
        update (str): The data or changes to be reflected in the view.
        
        Raises:
        NotImplementedError: If not implemented in a subclass.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO UPDATE THE VIEW
        raise NotImplementedError()
    
    # UPDATES THE VIEW WITH NEW DATA OR CHANGES.
    def handle_view_event(self, event):
        """
        Handles events triggered in the view (e.g., user actions).
        
        Parameters:
        event (str): The event triggered by the user or system.
        
        Raises:
        NotImplementedError: If not implemented in a subclass.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO HANDLE VIEW EVENTS
        raise NotImplementedError()

    # UPDATES THE VIEW BASED ON THE EVENT TYPE AND ASSOCIATED DATA.
    def update(self, event_type, data):
        """
        Updates the view based on the event type and associated data.
        
        Parameters:
        event_type (str): The type of event that occurred.
        data (any): The data related to the event.
        
        Raises:
        NotImplementedError: If not implemented in a subclass.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO HANDLE VIEW UPDATES
        raise NotImplementedError()

    # REFRESHES THE VIEW TO SHOW NEW DATA.
    def refresh_view(self):
        """Refreshes the view to show new data."""
        # MUST BE IMPLEMENTED IN A SUBCLASS TO REFRESH THE VIEW
        raise NotImplementedError()
