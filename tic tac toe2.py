import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_active = True
        
        self.setup_board()
    
    def setup_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", width=10, height=4, command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    
    def make_move(self, row, col):
        if self.board[row][col] == "" and self.game_active:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.game_active = False
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif self.is_board_full():
                self.game_active = False
                messagebox.showinfo("Game Over", "the fail in this game")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_move()
    
    def computer_move(self):
        available_moves = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
        if available_moves:
            row, col = random.choice(available_moves)
            self.make_move(row, col)
    
    def check_winner(self):
        for i in range(3):
            # Check rows and columns
            if all(self.board[i][j] == self.current_player for j in range(3)) or all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(3)) or all(self.board[i][2-i] == self.current_player for i in range(3)):
            return True
        return False
    
    def is_board_full(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_active = True
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
    
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    reset_button = tk.Button(root, text="Reset", command=game.reset_game)
    reset_button.grid(row=3, column=0, columnspan=3)
    root.mainloop()
