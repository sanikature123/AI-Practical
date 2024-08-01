import tkinter as tk
from tkinter import Canvas

class TowerOfHanoi:
    def __init__(self, master, n):
        self.master = master
        self.n = n
        self.canvas = Canvas(master, width=600, height=400)
        self.canvas.pack()
        self.pegs = [[], [], []]
        self.pieces = {}
        self.selected_piece = None
        self.selected_peg = None
        self.create_pegs()
        self.create_pieces()
        self.canvas.bind("<Button-1>", self.on_click)

    def create_pegs(self):
        peg_width = 10
        peg_height = 200
        peg_distance = 200
        for i in range(3):
            x1 = i * peg_distance + peg_distance // 2 - peg_width // 2
            y1 = 400 - peg_height
            x2 = x1 + peg_width
            y2 = 400
            self.canvas.create_rectangle(x1, y1, x2, y2, fill='black')

    def create_pieces(self):
        piece_height = 20
        max_piece_width = 120
        min_piece_width = 40
        peg_distance = 200
        for i in range(self.n, 0, -1):
            piece_width = min_piece_width + (max_piece_width - min_piece_width) * (i - 1) // (self.n - 1)
            x1 = peg_distance // 2 - piece_width // 2
            y1 = 400 - 20 - piece_height * (self.n - i)
            x2 = x1 + piece_width
            y2 = y1 + piece_height
            piece = self.canvas.create_rectangle(x1, y1, x2, y2, fill='red', tags=f"piece_{i}")
            self.pegs[0].append(piece)
            self.pieces[piece] = (0, i)

    def on_click(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        tags = self.canvas.gettags(item)
        if "piece" in tags[0]:
            self.select_piece(item[0])
        else:
            self.move_piece_to_peg(event.x)

    def select_piece(self, piece):
        if self.selected_piece:
            self.canvas.itemconfig(self.selected_piece, outline='')
        self.selected_piece = piece
        self.canvas.itemconfig(piece, outline='blue', width=2)
        peg, _ = self.pieces[piece]
        self.selected_peg = peg

    def move_piece_to_peg(self, x):
        if not self.selected_piece:
            return
        target_peg = x // 200
        if target_peg == self.selected_peg or (self.pegs[target_peg] and self.pieces[self.pegs[target_peg][-1]][1] < self.pieces[self.selected_piece][1]):
            self.canvas.itemconfig(self.selected_piece, outline='')
            self.selected_piece = None
            return

        piece = self.selected_piece
        self.pegs[self.selected_peg].remove(piece)
        self.pegs[target_peg].append(piece)
        self.pieces[piece] = (target_peg, self.pieces[piece][1])

        piece_height = 20
        x1 = target_peg * 200 + 200 // 2 - (self.canvas.bbox(piece)[2] - self.canvas.bbox(piece)[0]) // 2
        y1 = 400 - 20 - piece_height * len(self.pegs[target_peg])
        x2 = x1 + (self.canvas.bbox(piece)[2] - self.canvas.bbox(piece)[0])
        y2 = y1 + piece_height
        self.canvas.coords(piece, x1, y1, x2, y2)
        self.canvas.itemconfig(self.selected_piece, outline='')
        self.selected_piece = None

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tower of Hanoi")
    game = TowerOfHanoi(root, 4)
    root.mainloop()
