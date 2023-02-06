import tkinter as tk
from tkinter import *
from tkinter import messagebox
# from debug import printBoard
from functools import partial
from data import FlashCard

class App:
	def __init__(self):
		self.root = tk.Tk()
		self.root.bind('<Control-c>', self.destroy)
		self.root.bind('<Control-d>', self.destroy)
		self.root.title("Flash Cards")
		self.width, self.height = (600, 600)
		self.root.geometry(f"{self.width}x{self.height}")
		card = FlashCard(self.root,bg="red",name="Vocabulary",row=0,column=0)
		card1 = FlashCard(self.root,bg="red",name="Math",row=0,column=1)

	def destroy(self, event):
		self.root.destroy()	

	def run(self):
		self.root.mainloop()

if __name__ == "__main__":
	try:
		app = App()
		app.run()
	except Exception as e:
		print(e)
	except (KeyboardInterrupt, EOFError):
		print("app ended\n")