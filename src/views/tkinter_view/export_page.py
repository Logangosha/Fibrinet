# export_page.py
from utils.logger.logger import Logger 
import tkinter as tk
from .tkinter_view import TkinterView

class ExportPage(TkinterView):
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
        """Displays the Export Page"""
        center_frame = tk.Frame(container, bg=self.BG_COLOR)
        center_frame.pack(expand=True)

        self.export_heading = tk.Label(
            center_frame,
            foreground=self.FG_COLOR,
            font=self.PAGE_HEADING_FONT,
            background=self.PAGE_HEADING_BG,
            text="Export Data"
        )
        self.export_heading.pack(pady=(20, 10))

        self.export_message = tk.Label(
            center_frame,
            foreground=self.FG_COLOR,
            font=self.PAGE_SUBHEADING_FONT,
            background=self.PAGE_SUBHEADING_BG,
            text="You can now export the network data (press the button below).",
            wraplength=450,
            justify="center"
        )
        self.export_message.pack(pady=(0, 20))

        self.export_button = tk.Button(
            center_frame,
            image=self.button_images["Small_Export"],
            bg=self.view.ICON_BUTTON_BG,
            border="0",
            cursor="hand2",
            command=self.view.export_data,
            activebackground=self.view.ACTIVE_BG_COLOR
        )
        self.export_button.pack(pady=20)
