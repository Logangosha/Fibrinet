from utils.logger.logger import Logger
from ...models.exceptions import InvalidInputDataError
from ..network.network import Network
import pandas as pd
from .data_processing_strategy import DataProcessingStrategy

class ExcelDataStrategy(DataProcessingStrategy):
    """
    Handles data from an excel file.
    """
    # INITIALIZES EXCELDATASTRATEGY
    def __init__(self):
        """
        Initializes the ExcelDataStrategy.
        """
        Logger.log(f"start ExcelDataStrategy __init__(self)")
        Logger.log(f"end ExcelDataStrategy __init__(self)")
    
    # PROCESS INPUT DATA.
    def process(self, input_data):
        """
        Process input data to extract network data. Returns dictionary of network data. 
        
        Parameters:
        input_data: file input by user containing network data.
        
        Raises:
        N/A
        """
        Logger.log(f"start Process __init__(self, {input_data})")

        # LOAD THE ENTIRE SHEET INTO A DATAFRAME WITHOUT ASSUMING ANY HEADER
        # THE DATAFRAME IS A TABLE THAT PANDAS WILL USE TO STORE THE EXCEL CONTENT
        df = pd.read_excel(input_data, header=None)

        # VARIABLES TO STORE THE TABLES, TRACK THE CURRENT TABLE, TRACK NUMBER OF TABLES, AND TRACK IS NEW TABLE
        tables = {}
        current_table = {}
        table_number = 0
        is_new_table = True  

        # HELPER FUNCITON
        def add_current_table_to_tables():
            if current_table:
                if table_number == 0:
                    tables['NODES'] = current_table
                elif table_number == 1:
                    tables['EDGES'] = current_table
                elif table_number == 2:
                    tables['META_NETWORK_PROPERTIES'] = current_table

        # FOR EACH ROW IN DF
        for index, row in df.iterrows():
            # IF ITS NaN THEN ITS THE DIVIDOR BETWEEN ROWS
            if pd.isna(row[0]): 
                # ADD CURRENT TABLE TO TABLES 
                add_current_table_to_tables()
                # SET IS NEW TABLE TO TRUE 
                is_new_table = True
                # SET CURRENT TABLE TO EMPTY
                current_table = {}
                # INCREMENT TABLE NUMBER
                table_number += 1
            else:
                # IF is_new_table IS TRUE THEN THE CURRENT ROW ARE THE HEADERS
                if is_new_table:  
                    # GET NON NAN VALUES AS HEADERS
                    headers = row.dropna().tolist()  

                    # FOR EACH CELL IN THE CURRENT ROW 
                    for header in headers:
                        # CREATE A NEW KEY IN CURRENT_TABLE AND MAKE THE DEFAULT VALUE A NEW EMPTY LIST
                        current_table[header] = []
                    # SET IS NEW TABLE TO FALSE
                    is_new_table = False

                # IF is_new_table IS NOT TRUE THEN THE CURRENT ROW ARE THE VALUES
                else:  
                    # LOOP THROUGHT THE ROW AND FOR EACH VALUE ADD IT TO ITS CORRESPONDING HEADER KEY
                    for i, value in enumerate(row.dropna()):
                        current_table[headers[i]].append(value)

        # ADD LAST TABLE
        add_current_table_to_tables()

        # CREATE AND RETURN NETWORK
        network = Network(**tables)
        Logger.log(f"end Process __init__(self, input_data)")
        return network
    