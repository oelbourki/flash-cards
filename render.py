import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.colorchooser import askcolor
from data import *
from modify import ModifyFlashcardPage
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


# progress = []
# for i in range(10, 50, 5):
#     p = [np.random.randint(i//2, i), i]
#     progress.append(p)
# progress = np.array(progress)
# print(progress[:, 1])
# x = progress[:, 1]
# y = progress[:, 0]
# r = np.divide(y, x)


def _clear():
	for item in tk.canvas.get_tk_widget().find_all():
		tk.canvas.get_tk_widget().delete(item)


class ShowProgressPage(tk.Frame):
	flashcard = None

	def __init__(self, parent, controller, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.controller = controller
		self.run()

	def run(self):
		print("progress page")
		clear_frame(self)
		figure2 = plt.Figure(figsize=(5, 4), dpi=100)
		self.ax2 = figure2.add_subplot(111)
		line2 = FigureCanvasTkAgg(figure2, self)
		line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
		main_button = tk.Button(self, text="Main", command=self.main)
		if ShowProgressPage.flashcard:
			print("progress: ", ShowProgressPage.flashcard.progress)
			X = np.array(ShowProgressPage.flashcard.progress)
			x = X[:, 0]
			y = X[:, 1]
			r = np.divide(x, y)
			self.ax2.plot(np.arange(0,len(y), step=1), r)
		self.ax2.set_xlabel("Tries")
		self.ax2.set_ylabel("ratio of correct words")
		self.ax2.set_title("flash card progress chart")
		main_button.pack()

	def main(self):
		self.controller.show_frame("MainPage")

	@staticmethod
	def set_flashcard(flash):
		print("setting flashcard")
		ShowProgressPage.flashcard = flash


class FlashCardRender(Frame):
	def __init__(
			self, parent, controller, flashcard: FlashCardData, row, column
	) -> None:
		# print(type(flashcard.color))
		# print(flashcard.color)
		color = flashcard.color
		if type(flashcard.color) is tuple:
			color = flashcard.color[1]
		super().__init__(parent, bg=color, width=200, height=200)
		self.flashcard = flashcard
		self.parent = parent
		self.controller = controller
		label1 = Label(
			self, text=flashcard.name, font=("Arial 15 bold"), bg=color
		)
		label2 = Label(
			self,
			text=f"{len(flashcard)} card",
			font=("Arial 15 bold"),
			bg=color,
		)
		self.modify_button = Button(self, text="Modify", command=self.modify)
		self.show_button = Button(self, text="Progress", command=self.show)
		label1.pack(padx=30, pady=30)
		label2.pack(padx=30, pady=30)
		self.grid(row=row, column=column, padx=30, pady=30)
		self.pack_propagate(0)
		self.modify_button.pack(side=LEFT, padx=15)
		self.show_button.pack(side=RIGHT, padx=15)

	def show(self):
		# clear_frame(self)
		if len(self.flashcard.progress):
			ShowProgressPage.set_flashcard(self.flashcard)
			self.controller.show_frame("ShowProgressPage")

	def modify(self):
		print("i want to modify")
		# clear_frame(self.parent)
		print(self.flashcard)
		ModifyFlashcardPage.set_flashcard(self.flashcard)
		self.controller.show_frame("ModifyFlashcardPage")
