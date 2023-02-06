import tkinter as tk
from tkinter import messagebox
# from debug import printBoard
from functools import partial


class TicTacToe:
	def __init__(self):
		self.root = tk.Tk()
		self.root.bind('<Control-c>', self.destroy)
		self.root.bind('<Control-d>', self.destroy)
		self.root.title("Morpion")
		self.width, self.height = (600, 600)
		self.root.geometry(f"{self.width}x{self.height}")
		self.player = "X"
		self.buttons = [[tk.Button() for _ in range(3)] for _ in range(3)]
		self.exit = tk.Button()
		self.exit.config(width=5, height=2)
		self.exit.grid(row=3, column=1)
		self.exit.config(text="exit", command = self.root.destroy)
		for i in range(3):
			for j in range(3):
				self.buttons[i][j].config(width=25, height=10)
				self.buttons[i][j].grid(row=i, column=j)
				self.buttons[i][j].config(text='', command=partial(self.button_clicked,i, j))
	def destroy(self, event):
		self.root.destroy()	
	def button_clicked(self, i, j):
		self.buttons[i][j].config(text=self.player, state=tk.DISABLED)
		if self.check_for_win(i, j):
			self.root.after(1000, self.root.destroy)
			messagebox.showinfo("Tic-Tac-Toe", f"Player {self.player} wins!")
		elif self.check_for_tie():
			self.root.after(1000, self.root.destroy)
			messagebox.showinfo("Tic-Tac-Toe", "Tie Game!")
		else:
			self.player = "X" if self.player == "O" else "O"

	def check_for_win(self, row, col):
		myrow = [self.buttons[row][j].cget("text") == self.player for j in range(3)]
		mycol = [self.buttons[i][col].cget("text") == self.player for i in range(3)]
		diag1 = [self.buttons[i][i].cget("text") == self.player for i in range(3)]
		diag2 = [self.buttons[2][0].cget("text") == self.player,
				self.buttons[1][1].cget("text") == self.player,
				self.buttons[0][2].cget("text") == self.player]
		return all(mycol) or all(mycol) or all(diag1) or all(diag2)

	def check_for_tie(self):
		return all(self.buttons[i][j].cget("state") == tk.DISABLED for i in range(3) for j in range(3))

	def run(self):
		self.root.mainloop()

if __name__ == "__main__":
	try:
		game = TicTacToe()
		game.run()
	except Exception as e:
		print(e)
	except (KeyboardInterrupt, EOFError):
		print("Game ended\n")