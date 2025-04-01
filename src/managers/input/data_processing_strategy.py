from utils.logger.logger import Logger
from abc import ABC, abstractmethod

class DataProcessingStrategy(ABC):
    """
    Abstract base class for data processing strategies.
    This class defines the interface for processing input data.
    """
    
    # PROCESS INPUT DATA.
    @abstractmethod
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
