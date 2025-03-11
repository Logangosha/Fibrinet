# error_page.py
from utils.logger.logger import Logger 
import tkinter as tk
from .tkinter_view import TkinterView

class ErrorPage(TkinterView):
    def __init__(self, view):
        self.view = view
        self.BG_COLOR = view.BG_COLOR
        self.FG_COLOR = view.FG_COLOR
        self.button_images = view.button_images
        self.PAGE_HEADING_FONT = view.HEADING_FONT
        self.PAGE_HEADING_BG = view.HEADING_BG
        self.PAGE_SUBHEADING_FONT = view.SUBHEADING_FONT
        self.PAGE_SUBHEADING_BG = view.SUBHEADING_BG

    def show_page(self, container):
        """Displays the Error Page"""
        center_frame = tk.Frame(container, bg=self.BG_COLOR)
        center_frame.pack(expand=True)

        self.error_heading = tk.Label(
            center_frame,
            foreground=self.FG_COLOR,
            font=self.PAGE_HEADING_FONT,
            background=self.PAGE_HEADING_BG,
            text="Error"
        )
        self.error_heading.pack(pady=(20, 10))

        self.error_message = tk.Label(
            center_frame,
            foreground=self.FG_COLOR,
            font=self.PAGE_SUBHEADING_FONT,
            background=self.PAGE_SUBHEADING_BG,
            text="An error occurred. Please try again later.",
            wraplength=450,
            justify="center"
        )
        self.error_message.pack(pady=(0, 20))

        self.retry_button = tk.Button(
            center_frame,
            image=self.button_images["Small_Left_Arrow"],
            bg=self.view.ICON_BUTTON_BG,
            border="0",
            cursor="hand2",
            command=self.view.show_input_page,
            activebackground=self.view.ACTIVE_BG_COLOR
        )
        self.retry_button.pack(pady=20)
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# import os
# from src.managers.view.view_strategy import ViewStrategy
# from utils.logger.logger import Logger

# class TkinterView(ViewStrategy):
#     """
#     """

#     # GENERAL STYLE
#     FONT_FAMILY = "Consolas"
#     HEADING_FONT_SIZE = 45
#     SUBHEADING_FONT_SIZE = 15
#     BG_COLOR = "gray9"
#     ACTIVE_BG_COLOR = "gray9"
#     FG_COLOR = "white"

#     # INPUT PAGE STYLES
#     PAGE_BG_COLOR = BG_COLOR

#     PAGE_HEADING_COLOR = FG_COLOR
#     PAGE_HEADING_FONT = (FONT_FAMILY, HEADING_FONT_SIZE)
#     PAGE_HEADING_COLOR = FG_COLOR
#     PAGE_HEADING_BG = BG_COLOR

#     PAGE_SUBHEADING_COLOR = FG_COLOR
#     PAGE_SUBHEADING_FONT = (FONT_FAMILY, SUBHEADING_FONT_SIZE)
#     PAGE_SUBHEADING_COLOR = FG_COLOR
#     PAGE_SUBHEADING_BG = BG_COLOR
    
#     ICON_BUTTON_BG = BG_COLOR
#     ICON_BUTTON_BORDER = BG_COLOR
#     ICON_BUTTON_HOVER_BORDER = BG_COLOR
#     ICON_BUTTON_HOVER_BG = BG_COLOR

#     # MODIFY PAGE STYLE
#     CANVAS_BG_COLOR = "grey90"
#     ACTION_BAR_BG_COLOR = BG_COLOR
#     INFO_BAR_BG_COLOR = "gray11"


#     def __init__(self, controller):
#         """
#         """
#         self.controller = controller
#         self.running = True
#         self.root = tk.Tk()
#         self.root.title("FibriNet GUI")
#         self.root.geometry("800x650")
#         self.root.attributes('-topmost', True)
#         self.root.after(100, lambda: self.root.attributes('-topmost', False))
#         self.root.focus_force()
#         self.root.minsize(800, 650)

#         current_dir = os.path.dirname(os.path.abspath(__file__))
#         self.image_paths = {
#             "Import":os.path.join(current_dir, "images/Import.png"),
#             "Small_Import":os.path.join(current_dir, "images/Small_Import.png"),
#             "Small_Left_Arrow":os.path.join(current_dir, "images/Small_Left_Arrow.png"),
#             "X":os.path.join(current_dir, "images/X.png"),
#             "Small_X":os.path.join(current_dir, "images/Small_X.png"),
#             "Small_Right_Arrow":os.path.join(current_dir, "images/Small_Right_Arrow.png"),
#             "Small_Export":os.path.join(current_dir, "images/Small_Export.png"),
#             "Checkmark":os.path.join(current_dir, "images/Checkmark.png")
#         }

#         self.button_images = {name: tk.PhotoImage(file=path) for name, path in self.image_paths.items()}

#         # Initialize state to 'input'
#         self.state = 'input'

#         # Main Frame
#         self.page_content = tk.Frame(self.root, bg=self.BG_COLOR)
#         self.page_content.pack(fill=tk.BOTH, expand=True)

#         self.current_page = None
#         self.network_data = None

#     def show_input_page(self):
#         """
#         """
#         self.clear_body()
#         self.current_page = "input"
#         Logger.log("Showing Input Page")

#         # Create a wrapper frame to center content
#         center_frame = tk.Frame(self.page_content, bg=self.BG_COLOR)
#         center_frame.pack(expand=True)  # Expands to fill available space

#         self.input_heading = tk.Label(
#             center_frame,
#             foreground=self.FG_COLOR,
#             font=self.PAGE_HEADING_FONT,
#             background=self.PAGE_HEADING_BG,
#             text="FibriNet GUI"
#         )
#         self.input_heading.pack(pady=(20, 10))  # Add some spacing

#         self.input_subheading = tk.Label(
#             center_frame,
#             foreground=self.FG_COLOR,
#             font=self.PAGE_SUBHEADING_FONT,
#             background=self.PAGE_SUBHEADING_BG,
#             text="Please import network data to begin. Data files must be .xlsx. (press button below)",
#             wraplength=450,
#             justify="center"
#         )
#         self.input_subheading.pack(pady=(0, 20))  # Adjust padding

#         self.upload_file_icon_button = tk.Button(
#             center_frame,
#             image=self.button_images["Import"],
#             bg=self.ICON_BUTTON_BG,
#             border="0",
#             cursor="hand2",
#             command=self.on_upload_file_icon_button_click,
#             padx=10,
#             pady=10,
#             activebackground=self.ACTIVE_BG_COLOR
#         )
#         self.upload_file_icon_button.pack(pady=20)  # Adds some padding around the button


#     def on_upload_file_icon_button_click(self):
#         """
#         """
#         Logger.log(f"start on_upload_file_icon_button_click" )
#         # OPEN FILE EXPLORER 
#         file_path = filedialog.askopenfilename(
#         title="Select a Network Data File",
#         filetypes=[("Excel Files", "*.xlsx")]
#         )

#         if file_path:  # If user selected a file
#             Logger.log(f"File selected: {file_path}")

#             # Store the selected file path
#             self.network_data = file_path

#             # Transition to a confirmation page (implement show_confirm_page)
#             self.show_confirm_page()
#         else:
#             Logger.log("No file selected.")
#         # IF FILE SELECTED THEN CHANGE TO CONFIRM PAGE
#         Logger.log(f"end on_upload_file_icon_button_click" )

#     def show_confirm_page(self):
#         """
#         """
#         self.clear_body()
#         self.current_page = "confirm"
#         Logger.log("Showing Confirm Page")

#         # Create a wrapper frame to center content
#         center_frame = tk.Frame(self.page_content, bg=self.BG_COLOR)
#         center_frame.pack(expand=True)

#         # Heading Label
#         self.confirm_heading = tk.Label(
#             center_frame,
#             foreground=self.FG_COLOR,
#             font=self.PAGE_HEADING_FONT,
#             background=self.PAGE_HEADING_BG,
#             text="Correct File?"
#         )
#         self.confirm_heading.pack(pady=(20, 10))

#         # Subheading Label (Displays Selected File Path)
#         self.confirm_subheading = tk.Label(
#             center_frame,
#             foreground=self.FG_COLOR,
#             font=self.PAGE_SUBHEADING_FONT,
#             background=self.PAGE_SUBHEADING_BG,
#             text=self.network_data if self.network_data else "No file selected.",
#             wraplength=450,
#             justify="center"
#         )
#         self.confirm_subheading.pack(pady=(0, 20))

#         # Button Frame to hold both buttons side by side
#         button_frame = tk.Frame(center_frame, bg=self.BG_COLOR)
#         button_frame.pack(pady=30)

#         # Cancel Button (Left Side)
#         self.cancel_button = tk.Button(
#             button_frame,
#             image=self.button_images["X"],
#             bg=self.ICON_BUTTON_BG,
#             cursor="hand2",
#             border="0",
#             command=self.show_input_page,  # Go back to input page
#             activebackground=self.ACTIVE_BG_COLOR
#         )
#         self.cancel_button.pack(side=tk.LEFT, padx=60)  

#         # Confirm Button (Right Side)
#         self.confirm_button = tk.Button(
#             button_frame,
#             image=self.button_images["Checkmark"],
#             bg=self.ICON_BUTTON_BG,
#             cursor="hand2",
#             border="0",
#             command=self.on_confirm_file,
#             activebackground=self.ACTIVE_BG_COLOR
#         )
#         self.confirm_button.pack(side=tk.RIGHT, padx=60)  



#     def on_confirm_file(self):
#         """
#         """
#         Logger.log(f"File confirmed: {self.network_data}")
#         self.show_modify_page()  # Move to modify page


#     def show_modify_page(self):
#         """
#         """
#         self.clear_body()
#         self.current_page = "modify"
#         Logger.log("Showing Modify Page")

#         # Create a frame for the canvas (expands to fill available space)
#         canvas_frame = tk.Frame(self.page_content, bg=self.CANVAS_BG_COLOR)
#         canvas_frame.pack(fill=tk.BOTH, expand=True)
        
#         # Create the canvas
#         self.canvas = tk.Canvas(
#             canvas_frame,
#             bg=self.CANVAS_BG_COLOR,  # Set canvas background
#             highlightthickness=0
#         )
#         self.canvas.pack(fill=tk.BOTH, expand=True)  # Fill available space
        
#         # Create the toolbar frame (fixed height, stuck to bottom)
#         toolbar_height = 120  # Set toolbar height
#         toolbar_frame = tk.Frame(self.page_content, bg=self.BG_COLOR, height=toolbar_height)
#         toolbar_frame.pack(fill=tk.X, side=tk.BOTTOM)  # Stick to the bottom
#         toolbar_frame.pack_propagate(False)  # Prevent shrinking

#         # Create the action bar (Left - 70%)
#         action_bar = tk.Frame(toolbar_frame, bg=self.ACTION_BAR_BG_COLOR, height=toolbar_height)
#         action_bar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         # Create a frame inside action_bar to hold buttons
#         button_frame = tk.Frame(action_bar, bg=self.BG_COLOR)
#         button_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centered placement

#         # Create buttons and place them horizontally
#         for name, img in self.button_images.items():
#             if name in ["Checkmark", "X", "Import"]:
#                 continue
#             btn = tk.Button(
#                 button_frame,
#                 image=img,
#                 bg=self.ICON_BUTTON_BG,
#                 cursor="arrow",
#                 border=0,
#                 state=tk.DISABLED,
#                 activebackground=self.ACTIVE_BG_COLOR
#             )
#             if name in ["Small_Import"]:
#                 btn.config(state=tk.ACTIVE, cursor="hand2")

#             btn.pack(side=tk.LEFT, padx=15)  # Horizontal placement

#         # Create the info bar (Right - 30%)
#         info_bar = tk.Frame(toolbar_frame, bg=self.INFO_BAR_BG_COLOR, height=toolbar_height)
#         info_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

#         # Dynamically adjust layout on window resize
#         def update_toolbar_sizes(event):
#             """
#             """
#             new_width = event.width
#             action_bar.config(width=int(0.65 * new_width))
#             info_bar.config(width=int(0.35 * new_width))

#         toolbar_frame.bind("<Configure>", update_toolbar_sizes)

#     def show_export_page(self):
#         """
#         """
#         self.clear_body()
#         self.current_page = "export"
#         Logger.log("Showing Export Page")
        
#     def show_help(self):
#         """
#         """
#         messagebox.showinfo("Help", "Instructions on how to use the app...")
            
#     def load_network_data(self, file_path):
#         """
#         """
#         Logger.log(f"Loading data from {file_path}")
#         return {"data": "network_data_here"}

#     def on_canvas_click(self, event):
#         """
#         """
#         Logger.log(f"Canvas clicked at ({event.x}, {event.y})")

#     def export_data(self):
#         """
#         """
#         Logger.log("Exporting Network Data...")

#     def clear_body(self):
#         """
#         """
#         for widget in self.page_content.winfo_children():
#             widget.destroy()

#     def start_view(self):
#         """
#         """
#         Logger.log("Starting Tkinter GUI...")
#         self.show_input_page()  # Initial page
#         self.root.mainloop()


