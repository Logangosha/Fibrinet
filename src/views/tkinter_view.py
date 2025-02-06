import tkinter as tk
from src.managers.view.view_strategy import ViewStrategy
from utils.logger.logger import Logger

class TkinterView(ViewStrategy):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GUI View")

    def start_view(self):
        print("Starting Tkinter GUI...")
        self.root.mainloop()

    def stop_view(self):
        print("Stopping Tkinter GUI...")
        self.root.destroy()

    def update_view(self, update):
        print(f"GUI Update: {update}")

    def handle_view_event(self, event):
        print(f"Handling GUI event: {event}")

    def update(self, event_type, data):
        print(f"GUI received event: {event_type}, Data: {data}")

    def refresh_view(self):
        print("Refreshing GUI...")
