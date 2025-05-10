import tkinter as tk
from tkinter import messagebox
import heapq

# Sample graph representing roads between locations
graph = {
    'pu_gate': {'A_block': 1, 'Greenzy': 2},
    'A_block': {'pu_gate': 1, 'Greenzy': 2, 'L_block': 3},
    'Greenzy': {'pu_gate': 2, 'A_block': 1, 'L_block': 1, 'CV_block': 2},
    'L_block': {'A_block': 2, 'Greenzy': 1, 'CV_block': 1, 'ATAL': 4},
    'CV_block': {'Greenzy': 2, 'L_block': 1, 'ATAL': 3},
    'ATAL': {'L_block': 4, 'CV_block': 3}
}

# Dijkstra's Algorithm to find the shortest path
def dijkstra(graph, start, end):
    pq = [(0, start)]  # Priority queue: (cost, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            return path, distances[end]

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return None, float('inf')

# GUI Application
class ShortestPathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("City Shortest Path Finder")
        self.root.geometry("400x400")

        # Title
        tk.Label(root, text="Shortest Path Finder", font=("Arial", 16, "bold")).pack(pady=10)

        # Dropdowns for selecting locations
        self.start_label = tk.Label(root, text="Start Location:")
        self.start_label.pack()
        self.start_var = tk.StringVar(root)
        self.start_menu = tk.OptionMenu(root, self.start_var, *graph.keys())
        self.start_menu.pack()

        self.end_label = tk.Label(root, text="End Location:")
        self.end_label.pack()
        self.end_var = tk.StringVar(root)
        self.end_menu = tk.OptionMenu(root, self.end_var, *graph.keys())
        self.end_menu.pack()

        # Button to calculate shortest path
        self.calculate_btn = tk.Button(root, text="Find Shortest Path", command=self.find_shortest_path)
        self.calculate_btn.pack(pady=10)

        # Output Label
        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def find_shortest_path(self):
        start = self.start_var.get()
        end = self.end_var.get()

        if not start or not end:
            messagebox.showerror("Error", "Please select both start and end locations.")
            return

        path, distance = dijkstra(graph, start, end)

        if path:
            self.result_label.config(text=f"Shortest Path: {' → '.join(path)}\nDistance: {distance}")
        else:
            self.result_label.config(text="No path found!")

# Running the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ShortestPathApp(root)
    root.mainloop()
