import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.colorchooser import askcolor
from data import *
from functools import partial
from create import CreateFlashcardPage, CreateCardPage
from modify import ModifyCardPage, ModifyFlashcardPage
from render import FlashCardRender, ShowProgressPage
from time import sleep
# from data import
import data
from tkinter import messagebox
from gtts import gTTS
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time
import pickle

data.init()


def leftClick(controller, flashcard, e):
	print("event", e)
	print("control", controller)
	print("flash", flashcard)
	print("left")
	DisplayFlashcardPage.set_flashcard(flash=flashcard)
	controller.show_frame("DisplayFlashcardPage")


cards = [
	CardData("je", "I"),
	CardData("quoi", "what"),
	CardData("veux", "want"),
	CardData("merci", "thank you"),
	CardData("tous", "all"),
	CardData("autre", "other"),
]
flashcard1 = FlashCardData("Vocabulary", "#ff00ff", cards)
flashcard2 = FlashCardData("Math", "#ff00ff", cards[:])
flashcard3 = FlashCardData("Physics", "#ff00ff", cards[:])
flashcard4 = FlashCardData("gym", "#ff00ff", cards[:])
flashcard5 = FlashCardData("Tec", "#ff00ff", cards[:])
flashcard6 = FlashCardData("english", "#ff00ff", cards[:])
flashcard7 = FlashCardData("test", "#ff00ff", cards[:])

data.flashcards = data.flashcards + \
	[flashcard1, flashcard2, flashcard3, flashcard4,
		flashcard5, flashcard6, flashcard7]
data.reminder = [(time.time(),"Test"),(time.time(),"Game"),(time.time(),"Fear")]

def open_popup(win, text):
   top= Toplevel(win)
   top.geometry("200x200")
   top.title("Reminder")
   label = Label(top, text= text, font=('Mistral 18 bold'))
   label.pack()

class CardRender(Frame):
	def __init__(self, root, cardData, flashcard) -> None:
		super().__init__(root)
		self.cardData = cardData
		self.flashcard = flashcard
		self.card_frame = Frame(self, bg="#b1ddc6")
		card_frame1 = Frame(self.card_frame)
		frensh = Label(card_frame1, text="Frensh", font=('Arial 15 bold'))
		word = Label(card_frame1, text=cardData.info, font=('Arial 15 bold'))
		self.card_frame.pack(fill=BOTH, expand=1)
		frensh.pack(padx=50, pady=50)
		word.pack(padx=50, pady=50)
		card_frame1.pack(expand=1)
		self.yes = Button(self.card_frame, text="YES", command=self.add)
		self.no = Button(self.card_frame, text="NO", command=self.nof)
		self.yes.pack(side=RIGHT)
		self.no.pack(side=LEFT)
		self.pack(fill=BOTH, expand=1)
		# flashcard.
		# self.pack()

	def nof(self):
		self.flashcard.reminder.append((self.cardData, time.time()))

	def add(self):
		print("add")
		# if
		self.yes.config(state=tk.DISABLED)
		lst = self.flashcard.progress[-1]
		lst[0] = lst[0] + 1


class DisplayFlashcardPage(tk.Frame):
	flashcard = None

	def __init__(self, parent, controller, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.controller = controller

	def run(self):
		flashcard = DisplayFlashcardPage.flashcard
		if DisplayFlashcardPage.flashcard:
			nbr = len(DisplayFlashcardPage.flashcard)
			flashcard.progress.append([0, nbr])
			language = "en"
			cardfs = []
			for j in range(nbr):
				cardd = DisplayFlashcardPage.flashcard.cards[j]
				speech = gTTS(text=cardd.info, lang=language, slow=True)
				speech.save(f'{j}.mp3')
				cardf = CardRender(self.controller, cardd, flashcard)
				cardfs.append(cardf)

			for i, cardf in enumerate(cardfs):
				print("hererrrrr")
				self.after((i + 1) * 5000, cardf.pack)
				self.after((i + 1) * 5000 + 1000, cardf.show)
				self.after((i + 2) * 5000, cardf.destroy)
		self.controller.show_frame("MainPage")

	@staticmethod
	def set_flashcard(flash):
		print("setting flashcard")
		DisplayFlashcardPage.flashcard = flash


class MainPage(tk.Frame):
	def __init__(self, parent, controller, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.controller = controller
		main_frame = Frame(self)
		main_frame.pack(fill=BOTH, expand=1)
		my_canvas = Canvas(main_frame)
		my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
		my_scrollbar = ttk.Scrollbar(
			main_frame, orient=VERTICAL, command=my_canvas.yview
		)
		my_scrollbar.pack(side=RIGHT, fill=Y)
		my_canvas.configure(yscrollcommand=my_scrollbar.set)
		my_canvas.bind(
			"<Configure>",
			lambda e: my_canvas.configure(
				scrollregion=my_canvas.bbox("all")),
		)
		self.second_frame = Frame(my_canvas)
		my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")
		self.framex = Frame(self)
		self.run()
		# messagebox.showinfo("reminder", "this waht")
		# open_popup(self.controller)
		for rem in data.reminder:
			if time.time() > rem[0]:
				open_popup(self.controller, rem[1])

	def run(self):
		clear_frame(self.second_frame)
		clear_frame(self.framex)

		nbr = len(data.flashcards)
		print("number of fa:", nbr)

		j = -1
		i = 0
		while i < nbr:
			if i % 2 == 0:
				j = j + 1
			flashcard = data.flashcards[i]
			# print(i,"row:",i,"col:",i%2, flashcard)
			card = FlashCardRender(
				self.second_frame, self.controller, flashcard, row=j, column=i % 2
			)
			card.bind("<Button-1>", partial(leftClick,
					  self.controller, flashcard))
			i = i + 1
		add = Button(self.framex, text="+", command=self.create_flashcard)
		add.pack(side=LEFT)
		self.framex.pack(side=RIGHT)
		self.framex.tkraise()

	def create_flashcard(self):
		self.controller.show_frame("CreateFlashcardPage")


class Application(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title("Flash Cards")
		self.width, self.height = (550, 600)
		self.resizable(False, False)
		self.geometry(f"{self.width}x{self.height}")
		self.container = tk.Frame(self)
		self.container.pack(side="top", fill="both", expand=True)
		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (
				MainPage,
				CreateFlashcardPage,
				CreateCardPage,
				ModifyFlashcardPage,
				ModifyCardPage,
				DisplayFlashcardPage,
				ShowProgressPage
		):
			print(F.__name__)
			frame = F(parent=self.container, controller=self)
			self.frames[F.__name__] = frame
			# frame.pack()
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("MainPage")

	def show_frame(self, cont, flashcard=None):
		frame = self.frames[cont]
		if cont in ("MainPage", "ModifyCardPage", "DisplayFlashcardPage"):
			frame.run()
		if flashcard:
			frame.set_flashcard(flashcard)
		frame.tkraise()

def save_data():
	file_name = 'flashcards.pkl'
	with open(file_name, 'wb') as file:
		pickle.dump(data.flashcards, file)
		print(f'Object successfully saved to "{file_name}"')
	file_name = 'reminder.pkl'
	with open(file_name, 'wb') as file:
		pickle.dump(data.reminder, file)
		print(f'Object successfully saved to "{file_name}"')

def load_data():
	file_name = 'flashcards.pkl'
	with open(file_name, 'wb') as file:
		data.flashcards = pickle.load(file)
		print(f'Object successfully loaded to "{file_name}"')
	file_name = 'reminder.pkl'
	with open(file_name, 'wb') as file:
		data.reminder = pickle.load(file)
		print(f'Object successfully loaded to "{file_name}"')

if __name__ == "__main__":
	app = Application()
	try:
		app.mainloop()
	except Exception as e:
		save_data()
		print(e)
