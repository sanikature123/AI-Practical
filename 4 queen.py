import tkinter as tk
from tkinter import messagebox

class FourQueenGame:
    def __init__(self, root):
        self.root = root
        self.root.title("4 Queen Game")
        
        self.board_size = 4
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        
        self.queens_placed = 0
        
        self.setup_board()
    
    def setup_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                button = tk.Button(self.root, width=8, height=4, command=lambda r=row, c=col: self.place_queen(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    
    def place_queen(self, row, col):
        if self.board[row][col] == 1:
            self.board[row][col] = 0
            self.buttons[row][col].config(text="")
            self.queens_placed -= 1
        else:
            if self.is_valid_move(row, col):
                self.board[row][col] = 1
                self.buttons[row][col].config(text="Q")
                self.queens_placed += 1
                if self.queens_placed == 4 and self.check_win():
                    messagebox.showinfo("Congratulations", "You placed all 4 queens correctly!")
            else:
                messagebox.showwarning("Invalid Move", "Queens cannot attack each other!")
    
    def is_valid_move(self, row, col):
        for r in range(self.board_size):
            for c in range(self.board_size):
                if self.board[r][c] == 1:
                    if r == row or c == col or abs(r - row) == abs(c - col):
                        return False
        return True
    
    def check_win(self):
        queens = [(r, c) for r in range(self.board_size) for c in range(self.board_size) if self.board[r][c] == 1]
        for i in range(len(queens)):
            for j in range(i+1, len(queens)):
                if self.is_attacking(queens[i], queens[j]):
                    return False
        return True
    
    def is_attacking(self, q1, q2):
        r1, c1 = q1
        r2, c2 = q2
        return r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2)

if __name__ == "__main__":
    root = tk.Tk()
    game = FourQueenGame(root)
    root.mainloop()
