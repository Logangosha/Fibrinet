from utils.logger.logger import Logger

class DataProcessingStrategy:
    """
    Abstract base class for data processing strategies.
    This class defines the interface for processing input data.
    """
    # INITIALIZES DATAPROCESSINGSTRATEGY
    def __init__(self):
        """
        Initializes the DataProcessingStrategy.
        """
        Logger.log(f"start DataProcessingStrategy __init__(self)")
        Logger.log(f"end DataProcessingStrategy __init__(self)")
    
    # PROCESS INPUT DATA.
    def process(self, input_data):
        """
        Process input data to extract network data.
        
        Parameters:
        input_data: file input by user containing network data.
        
        Raises:
        NotImplementedError: If not implemented in a subclass.
        """
        # MUST BE IMPLEMENTED IN A SUBCLASS TO PROCESS INPUT
        raise NotImplementedError()
