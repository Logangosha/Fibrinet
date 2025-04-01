import tkinter as tk
from tkinter import filedialog
import os
import re

def get_files_with_extension():
    """Gets files with the specified extension and displays their names or contents recursively."""
    directory = directory_entry.get()
    extension = extension_entry.get()
    output_text.delete(1.0, tk.END)

    if not directory or not extension:
        output_text.insert(tk.END, "Please select a directory and enter a file extension.")
        return

    try:
        all_contents = ""
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(extension.lower()):
                    file_path = os.path.join(root, file)
                    if just_filenames_var.get():  # Check if the checkbox for filenames is selected
                        file_name = os.path.basename(file_path)  # Get just the file name
                        all_contents += f"{file_name}\n"
                    else:
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                contents = f.read()
                                if remove_whitespace_var.get():  # Check if checkbox is selected
                                    contents = re.sub(r'\s+', '', contents)  # remove whitespace
                                all_contents += f"\n--- {file_path} ---\n{contents}\n"
                        except UnicodeDecodeError:
                            all_contents += f"\n--- {file_path} ---\nCannot decode file (likely not text).\n"
                        except FileNotFoundError:
                            all_contents += f"\n--- {file_path} ---\nFile not found.\n"
        output_text.insert(tk.END, all_contents)
    except FileNotFoundError:
        output_text.insert(tk.END, "Directory not found.")
    except Exception as e:
        output_text.insert(tk.END, f"An error occurred: {e}")

def browse_directory():
    """Opens a directory selection dialog and updates the directory entry."""
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

# Create the main window
root = tk.Tk()
root.title("Recursive File Content Extractor")

# Directory selection
directory_label = tk.Label(root, text="Directory:")
directory_label.grid(row=0, column=0, sticky="w")

directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# File extension input
extension_label = tk.Label(root, text="File Extension:")
extension_label.grid(row=1, column=0, sticky="w")

extension_entry = tk.Entry(root, width=10)
extension_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Remove whitespace checkbox
remove_whitespace_var = tk.BooleanVar()
remove_whitespace_checkbox = tk.Checkbutton(root, text="Remove Whitespace", variable=remove_whitespace_var)
remove_whitespace_checkbox.grid(row=2, column=0, columnspan=2, pady=5)

# Show just filenames checkbox
just_filenames_var = tk.BooleanVar()
just_filenames_checkbox = tk.Checkbutton(root, text="Show Just Filenames", variable=just_filenames_var)
just_filenames_checkbox.grid(row=2, column=2, pady=5)

# Extract button
extract_button = tk.Button(root, text="Extract Contents", command=get_files_with_extension)
extract_button.grid(row=3, column=1, pady=10)

# Output text area
output_text = tk.Text(root, height=20, width=80)
output_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Scrollbar
scrollbar = tk.Scrollbar(root, command=output_text.yview)
scrollbar.grid(row=4, column=3, sticky="ns")
output_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
# We have these files left: system_controller.py
# EACH FUNCTION NEEDS DOCSTRING, COMMENTS, and LOGGS. 
# FIRST Do a smell test for each and get an idea of where each is at. 
# data_export_strategy.py
# excel_export_strategy.py
# export_manager.py
# export_request_interpreter.py
# export_strategy.py
# image_export_strategy.py
# png_export_strategy.py
# data_processing_strategy.py
# excel_data_strategy.py
# input_data_interpreter.py
# input_manager.py
# network_factory.py
# network_manager.py
# network_state_manager.py
# degradation_engine_strategy.py
# no_physics.py
# base_edge.py
# edge_2d.py
# base_network.py
# network_2d.py
# base_node.py
# node_2d.py
# view_manager.py
# view_request_interpreter.py
# view_strategy.py
# exceptions.py
# system_state.py
# cli_view.py
# error_page.py
# export_confirm_page.py
# export_page.py
# input_confirm_page.py
# input_page.py
# loading_page.py
# modify_page.py
# success_page.py
# tkinter_view.py
# canvas_manager.py
# toolbar_manager.py