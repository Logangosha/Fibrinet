from utils.logger.logger import Logger
from .data_interpreter import DataInterpreter
from ...models.exceptions import InvalidInputDataError

class InputManager:
    """
    Handles input management for the system.
    """
    # INITIALIZES INPUTMANAGER
    def __init__(self):
        """
        Initializes the InputManager.
        """
        Logger.log(f"start InputManager __init__(self)")
        self.data_interpreter = DataInterpreter()
        Logger.log(f"end InputManager __init__(self)")

    # GET NETWORK FROM INPUT DATA
    def get_network(self, input_data):
        """
        Gets network data from input data.

        Args:
            input_data (str): This is the file location, supplied by the user, that holds the network data.

        Raises:
            InvalidInputDataError: If the data cannot be validated by the data_processing_strategy.
        """
        Logger.log(f"start get_network __init__(self, {input_data})")
        # GET DATA PROCESSING STRATEGY FROM INPUT DATA
        data_processing_strategy = self.data_interpreter.get_data_processing_strategy(input_data)
        # VALIDATE DATA
        if data_processing_strategy.validate(input_data):
            Logger.log(f"end get_network __init__(self, input_data)")
            return data_processing_strategy.parse(input_data)
        else:
            raise InvalidInputDataError()
