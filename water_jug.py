import tkinter as tk
from tkinter import messagebox

class WaterJugVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Jug Problem Visualization")

        self.capacityA = 4  # Capacity of jug A
        self.capacityB = 3  # Capacity of jug B
        self.target = 2     # Target amount of water

        self.jugA = 0
        self.jugB = 0

        # Create canvas for drawing
        self.canvas = tk.Canvas(root, width=400, height=300, bg='white')
        self.canvas.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack(pady=10)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_simulation)
        self.reset_button.pack(pady=10)

        self.draw_jugs()

    def draw_jugs(self):
        self.canvas.delete("all")

        # Draw jug A
        x1, y1, x2, y2 = 50, 50, 150, 200
        self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='lightblue')
        self.canvas.create_text((x1 + x2) / 2, y1 + 10, text=f'Jug A ({self.capacityA}L)', font=('Helvetica', 10))
        self.canvas.create_text((x1 + x2) / 2, y2 - 10, text=f'{self.jugA}L', font=('Helvetica', 12))
        
        # Draw jug B
        x1, y1, x2, y2 = 250, 50, 350, 200
        self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='lightblue')
        self.canvas.create_text((x1 + x2) / 2, y1 + 10, text=f'Jug B ({self.capacityB}L)', font=('Helvetica', 10))
        self.canvas.create_text((x1 + x2) / 2, y2 - 10, text=f'{self.jugB}L', font=('Helvetica', 12))

    def start_simulation(self):
        # Example sequence of operations for demo
        steps = [
            ('fill', 'A'), ('pour', 'A', 'B'), ('empty', 'B'), ('pour', 'A', 'B'),
            ('fill', 'A'), ('pour', 'A', 'B')
        ]
        self.execute_steps(steps)

    def execute_steps(self, steps):
        for step in steps:
            if step[0] == 'fill':
                if step[1] == 'A':
                    self.jugA = self.capacityA
                elif step[1] == 'B':
                    self.jugB = self.capacityB
            elif step[0] == 'empty':
                if step[1] == 'A':
                    self.jugA = 0
                elif step[1] == 'B':
                    self.jugB = 0
            elif step[0] == 'pour':
                from_jug = step[1]
                to_jug = step[2]
                if from_jug == 'A' and to_jug == 'B':
                    transfer_amount = min(self.jugA, self.capacityB - self.jugB)
                    self.jugA -= transfer_amount
                    self.jugB += transfer_amount
                elif from_jug == 'B' and to_jug == 'A':
                    transfer_amount = min(self.jugB, self.capacityA - self.jugA)
                    self.jugB -= transfer_amount
                    self.jugA += transfer_amount
            self.draw_jugs()
            self.root.update()
            self.root.after(1000)  # Wait for 1 second

    def reset_simulation(self):
        self.jugA = 0
        self.jugB = 0
        self.draw_jugs()

# Create the Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    app = WaterJugVisualizer(root)
    root.mainloop()
