from utils.logger.logger import Logger

class DataProcessingStrategy:
    """
    Abstract base class for data processing strategies.
    This class defines the interface for validating and parsing input data.
    """
    # INITIALIZES DATAPROCESSINGSTRATEGY
    def __init__(self):
        """
        Initializes the DataProcessingStrategy.
        """
        Logger.log(f"start DataProcessingStrategy __init__(self)")
        Logger.log(f"end DataProcessingStrategy __init__(self)")

    # VALIDATES INPUT DATA.
    def validate(self, input_data):
        """
        Validates input data to match expected format.
        
        Parameters:
        input_data: file input by user containing network data.
        
        Raises:
        NotImplementedError: If not implemented in a subclass.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO VALIDATE INPUT
        raise NotImplementedError()
    
    # PARSES INPUT DATA.
    def parse(self, input_data):
        """
        Parses input data to extract network data.
        
        Parameters:
        input_data: file input by user containing network data.
        
        Raises:
        NotImplementedError: If not implemented in a subclass.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO PARSE INPUT
        raise NotImplementedError()
