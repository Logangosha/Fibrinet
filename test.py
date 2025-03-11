import tkinter as tk

class CanvasPlayground:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Canvas Playground")
        self.root.geometry("800x600")

        # Create a Canvas
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Button-3>", self.on_right_click)

        # Store object references
        self.objects = {}
        self.node_positions = {}

        # Example data
        self.nodes = {
            1: (100, 500),
            2: (300, 300),
            3: (300, 100),
            4: (500, 500)
        }

        self.edges = [
            (1, 2),
            (2, 3),
            (2, 4)
        ]

        # Create objects
        self.draw_graph()

    def draw_graph(self):
        """Draws edges first, then nodes on the canvas."""
        for node_id, (x, y) in self.nodes.items():
            self.node_positions[node_id] = (x, y)

        for node_from, node_to in self.edges:
            x1, y1 = self.node_positions[node_from]
            x2, y2 = self.node_positions[node_to]
            self.create_line(x1, y1, x2, y2, "red")

        for node_id, (x, y) in self.nodes.items():
            self.create_circle(x, y, 20, "blue", node_id)

    def create_circle(self, x, y, radius, color, node_id):
        """Creates a circle on the canvas and makes it clickable."""
        circle = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline=color, tags="circle")
        self.objects[circle] = {"type": "circle", "color": color, "node_id": node_id}

    def create_line(self, x1, y1, x2, y2, color):
        """Creates a line on the canvas and makes it clickable."""
        line = self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2, tags="line")
        self.objects[line] = {"type": "line", "color": color}

    def on_click(self, event):
        """
        Triggered when the mouse is clicked. Highlights the clicked object.
        """
        clicked = self.canvas.find_closest(event.x, event.y)
        if clicked:
            item_id = clicked[0]
            if item_id in self.objects:
                obj_type = self.objects[item_id]["type"]
                original_color = self.objects[item_id]["color"]

                if obj_type == "circle":
                    current_color = self.canvas.itemcget(item_id, "outline")
                    new_color = "yellow" if current_color != "yellow" else original_color
                    self.canvas.itemconfig(item_id, outline=new_color)

                elif obj_type == "line":
                    current_color = self.canvas.itemcget(item_id, "fill")
                    new_color = "yellow" if current_color != "yellow" else original_color
                    self.canvas.itemconfig(item_id, fill=new_color)
                    
                print(f"Clicked on {obj_type} at ({event.x}, {event.y})")

    def on_right_click(self, event):
        """Triggered when the right mouse button is clicked. Removes the clicked object."""
        clicked = self.canvas.find_closest(event.x, event.y)
        if clicked:
            item_id = clicked[0]
            if item_id in self.objects:
                del self.objects[item_id]  # Remove from dictionary
                self.canvas.delete(item_id)  # Remove from canvas
                print(f"Removed object at ({event.x}, {event.y})")

if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasPlayground(root)
    root.mainloop()
