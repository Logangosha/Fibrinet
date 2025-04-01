from .data_export_strategy import DataExportStrategy
import pandas as pd
import io
from ..network.networks.base_network import BaseNetwork
from io import BytesIO
from utils.logger.logger import Logger
import time

class ExcelExportStrategy(DataExportStrategy):
    def generate_export(self, network_state_history: list[BaseNetwork]):
        """Generates 3 simple Excel files using pandas."""
        files = []

        Logger.log("Starting Excel export generation")

        # Iterate over each network in the history
        for idx, network in enumerate(network_state_history):
            Logger.log(f"Processing network: {network}")

            # Extract schema information for metadata, nodes, and edges
            nodes_data = network.get_nodes()  # List of node objects
            edges_data = network.get_edges()  # List of edge objects
            meta_data = network.get_meta_data()  # Metadata dictionary

            Logger.log(f"Number of nodes: {len(nodes_data)}")
            Logger.log(f"Number of edges: {len(edges_data)}")
            Logger.log(f"Metadata: {meta_data}")

            # Clean the nodes and edges data to exclude the 'attributes' field
            Logger.log("Cleaning nodes data (excluding 'attributes' field)")
            nodes_df = pd.DataFrame(
                [{key: value for key, value in node.get_attributes().items() if key != 'attributes'}
                 for node in nodes_data]
            )
            Logger.log(f"Processed nodes dataframe with {len(nodes_df)} rows")

            # Convert edges data to pandas DataFrame, excluding the 'attributes' field
            Logger.log("Cleaning edges data (excluding 'attributes' field)")
            edges_df = pd.DataFrame(
                [{key: value for key, value in edge.get_attributes().items() if key != 'attributes'}
                 for edge in edges_data]
            )
            Logger.log(f"Processed edges dataframe with {len(edges_df)} rows")

            # Convert metadata to DataFrame
            Logger.log("Converting metadata to dataframe")
            meta_df = pd.DataFrame(list(meta_data.items()), columns=["meta_key", "meta_value"])
            Logger.log(f"Processed metadata dataframe with {len(meta_df)} rows")

            # Create an in-memory buffer (Excel file)
            Logger.log("Creating in-memory Excel file")
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                start_row = 0

                # Write nodes data
                Logger.log(f"Writing nodes data to Excel starting at row {start_row}")
                nodes_df.to_excel(writer, index=False, startrow=start_row, sheet_name="Sheet1")
                start_row += len(nodes_df) + 2  # Add 2 empty rows after nodes

                # Write edges data
                Logger.log(f"Writing edges data to Excel starting at row {start_row}")
                edges_df.to_excel(writer, index=False, startrow=start_row, sheet_name="Sheet1")
                start_row += len(edges_df) + 2  # Add 2 empty rows after edges

                # Write metadata data
                Logger.log(f"Writing metadata data to Excel starting at row {start_row}")
                meta_df.to_excel(writer, index=False, startrow=start_row, sheet_name="Sheet1")

            # Generate unique filename with a timestamp or index to prevent overwriting
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            unique_filename = f"network_data_{timestamp}_{idx+1}.xlsx"

            # Save the file content
            file_content = buffer.getvalue()
            files.append((unique_filename, file_content))

            Logger.log(f"Excel export generated successfully for this network. Saved as {unique_filename}")

        Logger.log("Excel export generation completed")

        return files
