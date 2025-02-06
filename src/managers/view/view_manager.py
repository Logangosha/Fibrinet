from src.managers.view.view_request_interpreter import ViewRequestInterpreter
from utils.logger.logger import Logger

# MANAGES VIEW REQUESTS AND CONTROLS VIEW STRATEGY
class ViewManager:
    """Handles view requests by selecting and managing the appropriate view strategy."""

    def __init__(self, controller):
        """
        Initializes the ViewManager with a ViewRequestInterpreter.

        Args:
            controller: An instance of the SystemControllerInterface.
        """
        

        Logger.log(f"start ViewManager __init__(self, {controller})")
        
        self.view_request_interpreter = ViewRequestInterpreter()
        self.view_strategy = None

        Logger.log(f"end ViewManager __init__(self, controller)")

    # HANDLES INCOMING VIEW REQUESTS
    def handle_view_request(self, view_request, controller):
        """
        Processes a view request by selecting and managing the appropriate view strategy.

        Args:
            view_request (str): The type of view requested (e.g., "CLI" or "Tkinter").
            controller: The controller instance that interacts with the selected view.

        Raises:
            ValueError: If the view request is invalid.
        """
        

        Logger.log(f"start handle_view_request(self, {view_request})")

        # STOPS CURRENT VIEW STRATEGY IF ACTIVE
        if self.view_strategy:
            Logger.log("Stopping current view strategy before switching.")
            self.view_strategy.stop_view()  
        
        # SELECTS A NEW VIEW STRATEGY
        self.view_strategy = self.view_request_interpreter.get_view_strategy(view_request, controller)
        Logger.log(f"Selected view strategy: {self.view_strategy}")

        # STARTS NEW VIEW STRATEGY
        Logger.log("Starting new view strategy.")
        self.view_strategy.start_view()
        
        Logger.log(f"end handle_view_request(self, {view_request})")
