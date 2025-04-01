from PIL import Image, ImageDraw
from ..network.networks.base_network import BaseNetwork
from .image_export_strategy import ImageExportStrategy
import io

class PngExportStrategy(ImageExportStrategy):
    def generate_export(self, network_state_history: list[BaseNetwork]):
        """Generates PNG images for each network state and combines them into one giant image."""
        files = []
        
        # Create an image for each network state
        images = [self.create_network_image(network) for network in network_state_history]
        
        # Combine all the images into one
        if images:
            combined_img = self.combine_images_vertically(images)
            buffer = io.BytesIO()
            combined_img.save(buffer, format='PNG')
            files.append(("combined_network.png", buffer.getvalue()))
        
        return files

    def create_network_image(self, network: BaseNetwork, padding=50, scale=10):
        """Creates an image of a network state with dynamically adjusted width and height."""
        if not network.nodes:
            return Image.new("RGB", (100, 100), "white")  # Return a blank image if no nodes exist

        nodes = {node.n_id: node for node in network.nodes}
        edges = {edge.e_id: edge for edge in network.edges}

        # Determine min and max coordinates
        min_x = min(node.n_x for node in nodes.values())
        max_x = max(node.n_x for node in nodes.values())
        min_y = min(node.n_y for node in nodes.values())
        max_y = max(node.n_y for node in nodes.values())

        # Compute image dimensions with padding
        width = (max_x - min_x) * scale + 2 * padding
        height = (max_y - min_y) * scale + 2 * padding

        img = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(img)

        # Draw edges
        for edge in edges.values():
            node_from = nodes[edge.n_from]
            node_to = nodes[edge.n_to]

            x1 = (node_from.n_x - min_x) * scale + padding
            y1 = height - ((node_from.n_y - min_y) * scale + padding)  # Invert Y-coordinate
            x2 = (node_to.n_x - min_x) * scale + padding
            y2 = height - ((node_to.n_y - min_y) * scale + padding)  # Invert Y-coordinate

            draw.line((x1, y1, x2, y2), fill="black", width=3)

        # Draw nodes
        for node in nodes.values():
            x = (node.n_x - min_x) * scale + padding
            y = height - ((node.n_y - min_y) * scale + padding)  # Invert Y-coordinate

            draw.ellipse([x-5, y-5, x+5, y+5], fill="black", outline="black")

        return img
    
    def combine_images_vertically(self, image_list):
        """Combines multiple images into one vertically stacked image."""
        max_width = max(img.width for img in image_list)
        total_height = sum(img.height for img in image_list)
        
        combined_img = Image.new("RGB", (max_width, total_height), "white")  # White background
        y_offset = 0
        for img in image_list:
            combined_img.paste(img, (0, y_offset))
            y_offset += img.height
        
        return combined_img
