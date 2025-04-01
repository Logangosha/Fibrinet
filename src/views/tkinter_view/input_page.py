from utils.logger.logger import Logger 
import tkinter as tk
from tkinter import filedialog
from .tkinter_view import TkinterView

class InputPage(TkinterView):
    """
    A class that represents the input page in the FibriNet GUI application.

    This class handles the display of the input page, which prompts the user to upload a network data file (.xlsx format).
    It inherits from `TkinterView` and customizes the appearance and functionality of the input page. The page includes a heading,
    subheading, and a file upload button that opens the file explorer for the user to select a data file.

    Attributes:
        BG_COLOR (str): The background color of the page, inherited from the parent view.
        FG_COLOR (str): The foreground (text) color of the page, inherited from the parent view.
        button_images (dict): A dictionary of button images used on the page, inherited from the parent view.
        PAGE_HEADING_FONT (tuple): The font settings for the page heading.
        PAGE_HEADING_BG (str): The background color for the page heading.
        PAGE_SUBHEADING_FONT (tuple): The font settings for the page subheading.
        PAGE_SUBHEADING_BG (str): The background color for the page subheading.
        view (TkinterView): The parent view that manages the overall GUI and state.

    Methods:
        __init__(view): Initializes the input page with the provided view, setting up page styles and attributes.
        show_page(container): Displays the content of the input page within the provided container.
        on_upload_file_icon_button_click(): Opens the file explorer for the user to select a network data file, and transitions to the confirm page.
    """
    # INITALIZE INPUT PAGE
    def __init__(self, view):
        """
        Initializes the InputPage with the provided view.
        
        Args:
            view (TkinterView): The parent TkinterView instance managing the GUI.
        """
        Logger.log(f"start __init__(self, {view})")
        self.view = view

        # INPUT PAGE STYLES
        self.BG_COLOR = view.BG_COLOR
        self.FG_COLOR = view.FG_COLOR
        self.button_images = view.button_images
        self.PAGE_HEADING_FONT = view.HEADING_FONT
        self.PAGE_HEADING_BG = view.HEADING_BG
        self.PAGE_SUBHEADING_FONT = view.SUBHEADING_FONT
        self.PAGE_SUBHEADING_BG = view.SUBHEADING_BG
        Logger.log("end __init__(self, view)")

    # SHOW PAGE
    def show_page(self, container):
        """
        Displays the Input Page with heading, subheading, and a file upload button.
        
        Args:
            container (tk.Frame): The container frame where the page content will be added.
        """
        Logger.log(f"start show_page(self, {container})")
        center_frame = tk.Frame(container, bg=self.BG_COLOR)
        center_frame.pack(expand=True)

        self.input_heading = tk.Label(
            center_frame,
            foreground=self.FG_COLOR,
            font=self.PAGE_HEADING_FONT,
            background=self.PAGE_HEADING_BG,
            text="FibriNet GUI"
        )
        self.input_heading.pack(pady=(20, 10))

        self.input_subheading = tk.Label(
            center_frame,
            foreground=self.FG_COLOR,
            font=self.PAGE_SUBHEADING_FONT,
            background=self.PAGE_SUBHEADING_BG,
            text="Please import network data to begin. Data files must be .xlsx. (press button below)",
            wraplength=450,
            justify="center"
        )
        self.input_subheading.pack(pady=(0, 20))

        self.upload_file_icon_button = tk.Button(
            center_frame,
            image=self.button_images["Import"],
            bg=self.view.ICON_BUTTON_BG,
            border="0",
            cursor="hand2",
            command=self.on_upload_file_icon_button_click,
            padx=10,
            pady=10,
            activebackground=self.view.ACTIVE_BG_COLOR
        )
        self.upload_file_icon_button.pack(pady=20)
        Logger.log("end show_page(self, container)")

    # ON UPLOAD FILE ICON BUTTON CLICK
    def on_upload_file_icon_button_click(self):
        """
        Opens the file explorer for the user to select a network data file (.xlsx).
        If a file is selected, stores the file path and transitions to the confirmation page.
        If no file is selected, logs a message indicating that no file was chosen.
        """
        Logger.log(f"start on_upload_file_icon_button_click") 
        file_path = filedialog.askopenfilename(
            title="Select a Network Data File",
            filetypes=[("Excel Files", "*.xlsx")]
        )
        if file_path: 
            Logger.log(f"File selected: {file_path}")
            self.view.selected_file = file_path
            self.view.show_page("input_confirm")
        else:
            Logger.log("No file selected.")
        Logger.log(f"end on_upload_file_icon_button_click")

