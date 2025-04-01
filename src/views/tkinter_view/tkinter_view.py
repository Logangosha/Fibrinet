import tkinter as tk
import os
from src.managers.view.view_strategy import ViewStrategy
from utils.logger.logger import Logger

class TkinterView(ViewStrategy):
    """
    A class responsible for creating and managing the Tkinter GUI for the FibriNet application.

    This class sets up the Tkinter root window, manages the appearance of different pages (e.g., input, confirm, error, export, modify),
    and handles page navigation. It defines general style settings for fonts, colors, and button images. The TkinterView is the primary
    interface that interacts with the user, presenting various views based on the application's state.

    Attributes:
        FONT_FAMILY (str): The font family used for text elements.
        HEADING_FONT_SIZE (int): The font size for headings.
        SUBHEADING_FONT_SIZE (int): The font size for subheadings.
        BG_COLOR (str): The background color of the window.
        ACTIVE_BG_COLOR (str): The background color when active.
        FG_COLOR (str): The foreground (text) color.
        ICON_BUTTON_BG (str): The background color for icon buttons.
        ICON_BUTTON_BORDER (str): The border color for icon buttons.
        icon_paths (dict): A dictionary storing paths to button images.
        button_images (dict): A dictionary storing loaded Tkinter PhotoImage objects.
        page_classes (dict): A dictionary mapping page names to their corresponding page classes.
        controller (SystemInterfaceController): The controller responsible for managing the application's state.
        root (tk.Tk): The root Tkinter window.
        running (bool): A flag indicating if the GUI is running.
        page_content (tk.Frame): The container for the current page's content.

    Methods:
        __init__(controller): Initializes the Tkinter view with the given controller and sets up the window properties.
        show_page(page_name): Displays the specified page by clearing the current view and loading the new one.
        clear_body(): Removes all widgets from the current page's container.
        start_view(): Starts the Tkinter event loop and shows the initial input page.
    """
    #GENERAL STYLE
    FONT_FAMILY = "Consolas"
    HEADING_FONT_SIZE = 45
    SUBHEADING_FONT_SIZE = 15
    BG_COLOR = "gray9"
    ACTIVE_BG_COLOR = "gray9"
    FG_COLOR = "white"
    BG_COLOR = BG_COLOR
    HEADING_COLOR = FG_COLOR
    HEADING_FONT = (FONT_FAMILY, HEADING_FONT_SIZE)
    HEADING_COLOR = FG_COLOR
    HEADING_BG = BG_COLOR
    SUBHEADING_COLOR = FG_COLOR
    SUBHEADING_FONT = (FONT_FAMILY, SUBHEADING_FONT_SIZE)
    SUBHEADING_COLOR = FG_COLOR
    SUBHEADING_BG = BG_COLOR
    ICON_BUTTON_BG = BG_COLOR
    ICON_BUTTON_BORDER = BG_COLOR
    ICON_BUTTON_HOVER_BORDER = BG_COLOR
    ICON_BUTTON_HOVER_BG = BG_COLOR

    # INITIALIZE TKINTERVIEW
    def __init__(self, controller):
        """
        Initializes the TkinterView. 
        This is the object that will contain the meta / general view properties such as controller and root. 
        Args: 
            controller: This needs to be the SystemInterfaceController. 
        """
        Logger.log(f"start TkinterView __init__(self, controller)")
        self.controller = controller
        self.running = True
        self.root = tk.Tk()
        self.root.title("FibriNet GUI")
        self.root.geometry("1000x800")
        self.root.attributes('-topmost', True)
        self.root.after(100, lambda: self.root.attributes('-topmost', False))
        self.root.focus_force()
        self.root.minsize(800, 650)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_paths = {
            "Import":os.path.join(current_dir, "images/Small_Import.png"),
            "Small_Import":os.path.join(current_dir, "images/XSmall_Import.png"),
            "Small_Left_Arrow":os.path.join(current_dir, "images/XSmall_Left_Arrow.png"),
            "X":os.path.join(current_dir, "images/Small_X.png"),
            "Small_X":os.path.join(current_dir, "images/XSmall_X.png"),
            "Small_Right_Arrow":os.path.join(current_dir, "images/XSmall_Right_Arrow.png"),
            "Export":os.path.join(current_dir, "images/Small_Export.png"),
            "Small_Export":os.path.join(current_dir, "images/XSmall_Export.png"),
            "Checkmark":os.path.join(current_dir, "images/Small_Checkmark.png")
        }
        self.button_images = {name: tk.PhotoImage(file=path) for name, path in self.image_paths.items()}
        
        from .input_confirm_page import InputConfirmPage
        from .error_page import ErrorPage
        from .export_page import ExportPage
        from .input_page import InputPage
        from .modify_page import ModifyPage
        from .export_confirm_page import ExportConfirmPage
        from .success_page import SuccessPage
        from .loading_page import LoadingPage

        self.page_classes = {
            "input": InputPage(self),
            "input_confirm": InputConfirmPage(self),
            "export_confirm": ExportConfirmPage(self),
            "error": ErrorPage(self),
            "export": ExportPage(self),
            "modify": ModifyPage(self),
            "success": SuccessPage(self),
            "loading": LoadingPage(self)
        }

        # Initialize with the input page
        self.state = 'input'
        self.page_content = tk.Frame(self.root, bg=self.BG_COLOR)
        self.page_content.pack(fill=tk.BOTH, expand=True)
        Logger.log(f"end TkinterView __init__(self, controller)")

    # SHOW PAGE
    def show_page(self, page_name):
        """
        General method to show any page. 
        
        Args: 
            page_name: this is a string of the page name .
        """
        Logger.log(f"start show_page(self, {page_name})")
        page_class = self.page_classes.get(page_name)
        if page_class:
            self.clear_body()
            page_class.show_page(self.page_content)  # Calls the show method of the page
        Logger.log(f"end show_page(self, page_name)")

    def show_error_page(self, error_message):
        """Displays the error page with a specific error message."""
        Logger.log(f"start show_error_page(self, error_message={error_message})")
        error_page = self.page_classes.get("error")
        if error_page:
            self.clear_body()
            error_page.show_page(self.page_content, error_message)
        Logger.log(f"end show_error_page(self, error_message)")

    # CLEAR BODY
    def clear_body(self):
        """
        This removes all elements in the current page.
        """
        Logger.log(f"start clear_body(self)")
        for widget in self.page_content.winfo_children():
            widget.destroy()
        Logger.log(f"end clear_body(self)")

    # START VIEW
    def start_view(self):
        """
        Starts the Tkinter view by showing the input page. 
        """
        Logger.log("start start_view(self)")
        self.show_page("input")  # Start with the input page
        self.root.mainloop()
        Logger.log(f"end start_view(self)")

    # STOP VIEW
    def stop_view(self):
        """
        Stop the Tkinter view by showing the input page. 
        """
        Logger.log("start stop_view(self)")
        self.root.quit()
        Logger.log(f"end stop_view(self)")



