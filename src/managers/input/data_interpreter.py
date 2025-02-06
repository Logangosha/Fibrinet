from utils.logger.logger import Logger
from ...models.exceptions import UnsupportedFileTypeError
from .excel_data_strategy import ExcelDataStrategy
import os

class DataInterpreter:
    """
    Interprets input data and provides a DataProcessingStrategy.
    """
    # INITIALIZES DATAINTERPRETER
    def __init__(self):
        """
        Initializes the DataInterpreter.
        """
        Logger.log(f"start DataInterpreter __init__(self)")
        Logger.log(f"end DataInterpreter __init__(self)")
    
    # GET DATA PROCESSING STRATEGY
    def get_data_processing_strategy(self, input_data):
        """
        Returns the correct data processing strategy for the input data. 

        Args:
            input_data (str): This is the file location, supplied by the user, that holds the network data.

        Raises:
            FileNotFoundError: Raised when file is not found
        """
        Logger.log(f"start get_data_processing_strategy __init__(self, {input_data})")
        # CHECK DOES FILE EXIST
        if not os.path.exists(input_data):
            Logger.log(f"File ({input_data}) Not Found")
            raise FileNotFoundError()

        file_size = os.path.getsize(input_data)
        file_name = os.path.basename(input_data)
        file_extension = os.path.splitext(input_data)[1]
        Logger.log(f"File details - Name: {file_name}, Size: {file_size} bytes, Extension: {file_extension}")

        # DETERMINE THE TYPE OF FILE INPUT DATA IS AND RETURN DATA PROCESSING STRATEGY
        if file_extension == '.xlsx':
            Logger.log("This is an Excel file.")
            Logger.log(f"end DataInterpreter __init__(self, input_data)")
            return ExcelDataStrategy()

        else:
            Logger.log(f"Unsupported file type: {file_extension}")
            raise UnsupportedFileTypeError()


        
            
