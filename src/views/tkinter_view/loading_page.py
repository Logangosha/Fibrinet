import random
import tkinter as tk
from .tkinter_view import TkinterView

class LoadingPage(TkinterView):
    def __init__(self, view):
        self.view = view
        self.BG_COLOR = view.BG_COLOR
        self.FG_COLOR = view.FG_COLOR
        self.PAGE_HEADING_FONT = view.HEADING_FONT
        self.PAGE_HEADING_BG = view.HEADING_BG
        self.PAGE_SUBHEADING_FONT = view.SUBHEADING_FONT
        self.PAGE_SUBHEADING_BG = view.SUBHEADING_BG

    def show_page(self, container):
        """Displays a loading page with a loading message"""
        # Spinner parameters
        self.spinner_index = 0
        self.spinner_frames = [".", "..", "...", " "]  # Spinner frames
        self.spinner_labels = []  # List to hold the spinner labels
        center_frame = tk.Frame(container, bg=self.BG_COLOR)
        center_frame.pack(expand=True)

        # Heading
        self.loading_heading = tk.Label(
            center_frame,
            foreground=self.FG_COLOR,
            font=self.PAGE_HEADING_FONT,
            background=self.PAGE_HEADING_BG,
            text="Processing Data..."
        )
        self.loading_heading.pack(pady=(20, 10))

        # Subheading
        self.loading_message = tk.Label(
            center_frame,
            foreground=self.FG_COLOR,
            font=self.PAGE_SUBHEADING_FONT,
            background=self.PAGE_SUBHEADING_BG,
            text="Please wait while processing.",
            wraplength=450,
            justify="center"
        )
        self.loading_message.pack(pady=(0, 20))

        # Spinner Frame
        self.spinner_frame = tk.Frame(center_frame, bg=self.BG_COLOR)
        self.spinner_frame.pack(pady=(20, 0))

        # Add 3 spinner frames
        for i in range(3):
            spinner_label = tk.Label(
                self.spinner_frame,
                foreground=self.FG_COLOR,
                font=("Courier", 24),
                background=self.BG_COLOR,
                text=" "
            )
            spinner_label.grid(row=0, column=i, padx=10)
            self.spinner_labels.append(spinner_label)

        # Start the spinner animation
        self.animate_spinner()

    def animate_spinner(self):
        """Randomly change spinner frames"""
        for i, label in enumerate(self.spinner_labels):
            # Randomly choose a frame for each spinner
            label.config(text=random.choice(self.spinner_frames))
        # Repeat the animation after a short delay
        self.spinner_frame.after(300, self.animate_spinner)
