import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.colorchooser import askcolor
from data import *
from functools import partial
flashcards = []
allCards = {}


def leftClick(e):
	print("left")


class FlashCardRender(Frame):
	def __init__(self, parent, controller, flashcard: FlashCardData, row, column) -> None:
		super().__init__(parent, bg=flashcard.color, width=200, height=200)
		self.flashcard = flashcard
		self.parent = parent
		self.controller = controller
		label1 = Label(self, text=flashcard.name, font=(
			'Arial 15 bold'), bg=flashcard.color)
		label2 = Label(self, text=f"{len(flashcard)} card", font=(
			'Arial 15 bold'), bg=flashcard.color)
		self.modify_button = Button(self, text="+", command=self.modify)
		label1.pack(padx=30, pady=30)
		label2.pack(padx=30, pady=30)
		self.grid(row=row, column=column, padx=30, pady=30)
		self.pack_propagate(0)
		self.modify_button.pack()

	def modify(self):
		print("i want to modify")
		# clear_frame(self.parent)
		print(self.flashcard)
		ModifyFlashcardPage.set_flashcard(self.flashcard)
		self.controller.show_frame(ModifyFlashcardPage)


class Card:
	def __init__(self, word, translation, color):
		self.word = word
		self.translation = translation
		self.color = color


class ModifyCardPage(tk.Frame):
	flashcard = None

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.savedColor = None
		# create the form elements
		word_label = tk.Label(self, text="Word")
		self.word_entry = tk.Entry(self)
		translation_label = tk.Label(self, text="Translation")
		self.translation_entry = tk.Entry(self)
		color = tk.Button(
			self,
			text='Select a Color',
			command=self.get_color)
		# color.pack()
		# arrange the form elements on the screen
		word_label.grid(row=0, column=0, sticky="e")
		self.word_entry.grid(row=0, column=1)
		translation_label.grid(row=1, column=0, sticky="e")
		self.translation_entry.grid(row=1, column=1)
		# color.grid(row=2,column=1)
		# create a button to save the flashcard
		save_button = tk.Button(self, text="Save", command=self.save_card)
		save_button.grid(row=3, column=1, pady=10)
		reset_button = tk.Button(self, text="Reset", command=self.reset)
		reset_button.grid(row=3, column=0, pady=10)
		main_button = tk.Button(self, text="Main", command=self.main)
		main_button.grid(row=3, column=2, pady=10)
		# frame = Frame(self)
		# card_label = tk.Label(self, text="Word")
		# delete_button = tk.Button(self, text="delete", command=self.delete_card)
		# card_label.pack()
		# delete_button.pack()
		# frame.pack()

	def delete_card(self):
		pass
		# v1 = tk.IntVar()
		# c1 = tk.Checkbutton(self, text='Python',variable=v1, onvalue=1, offvalue=0, command=print_selection)
		# c1.pack()

	def main(self):
		self.controller.show_frame(MainPage)

	def reset(self):
		self.word_entry.delete(0, END)
		self.translation_entry.delete(0, END)
		self.savedColor = None

	def get_color(self):
		color = askcolor(title="Tkinter Color Chooser")
		self.savedColor = color

	def save_card(self):
		word = self.word_entry.get()
		translation = self.translation_entry.get()
		# card = Card(word, translation, self.savedColor)
		card = CardData(word)
		ModifyCardPage.flashcard.cards.append(card)
		# flashcards[-1].append(card)
		# print(flashcards[-1].cards)
		# # go back to the main page
		# self.controller.show_frame(MainPage)

	@staticmethod
	def set_flashcard(flash):
		ModifyCardPage.flashcard = flash


class CreateCardPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.savedColor = None
		# create the form elements
		word_label = tk.Label(self, text="Word")
		self.word_entry = tk.Entry(self)
		translation_label = tk.Label(self, text="Translation")
		self.translation_entry = tk.Entry(self)
		color = tk.Button(
			self,
			text='Select a Color',
			command=self.get_color)
		# color.pack()
		# arrange the form elements on the screen
		word_label.grid(row=0, column=0, sticky="e")
		self.word_entry.grid(row=0, column=1)
		translation_label.grid(row=1, column=0, sticky="e")
		self.translation_entry.grid(row=1, column=1)
		# color.grid(row=2,column=1)
		# create a button to save the flashcard
		save_button = tk.Button(self, text="Save", command=self.save_card)
		save_button.grid(row=3, column=1, pady=10)
		reset_button = tk.Button(self, text="Reset", command=self.reset)
		reset_button.grid(row=3, column=0, pady=10)
		main_button = tk.Button(self, text="Main", command=self.main)
		main_button.grid(row=3, column=2, pady=10)

	def main(self):
		self.controller.show_frame(MainPage)

	def reset(self):
		self.word_entry.delete(0, END)
		self.translation_entry.delete(0, END)
		self.savedColor = None

	def get_color(self):
		color = askcolor(title="Tkinter Color Chooser")
		self.savedColor = color

	def save_card(self):
		# get the data from the form
		word = self.word_entry.get()
		translation = self.translation_entry.get()

		# create a new Card instance
		card = Card(word, translation, self.savedColor)

		# add the card to the list of cards
		# self.controller.cards.append(card)
		flashcards[-1].append(card)
		print(flashcards[-1].cards)
		# # go back to the main page
		# self.controller.show_frame(MainPage)


class MainPage(tk.Frame):
	def __init__(self, parent, controller, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.controller = controller

		main_frame = Frame(self)
		# main_frame = self.pare
		main_frame.pack(fill=BOTH, expand=1)

		my_canvas = Canvas(main_frame)
		my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

		my_scrollbar = ttk.Scrollbar(
			main_frame, orient=VERTICAL, command=my_canvas.yview)
		my_scrollbar.pack(side=RIGHT, fill=Y)

		my_canvas.configure(yscrollcommand=my_scrollbar.set)
		my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
			scrollregion=my_canvas.bbox("all")))

		second_frame = Frame(my_canvas)
		my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

		# self.flashCards = []
		cards = [CardData("boulout"), CardData("test"), CardData("war"), CardData("idea"),
				 CardData("game"), CardData("titw")]
		flashcard1 = FlashCardData("Vocabulary", '#ff00ff', cards)
		flashcard2 = FlashCardData("Math", '#ff00ff', cards[:])
		flashcards.append([flashcard1, flashcard2])
		for i in range(10):
			card = FlashCardRender(second_frame, self.controller, flashcard1,
								   row=i, column=0)
			card1 = FlashCardRender(second_frame, self.controller, flashcard2,
									row=i, column=1)
			card.bind("<Button-1>", leftClick)
			# self.flashCards.append(card)
			# self.flashCards.append(card1)
		# add.pack()

		framex = Frame(self)
		add = Button(framex, text="+", command=self.create_flashcard)
		add.pack(side=LEFT)
		framex.pack(side=RIGHT)
		framex.tkraise()
		# self.create_button = tk.Button(
		#     self, text="+", command=self.create_flashcard)
		# self.create_button.pack()

	def create_flashcard(self):
		self.controller.show_frame(CreateFlashcardPage)


def clear_frame(root):
	for widgets in root.winfo_children():
		widgets.destroy()


class ModifyFlashcardPage(tk.Frame):
	flashcard = None

	def __init__(self, parent, controller, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.savedColor = None
		self.controller = controller
		self.name_label = tk.Label(self, text="Nom du flashcard:")
		self.name_entry = tk.Entry(self)
		self.color = tk.Button(
			self,
			text='Select a Color',
			command=self.get_color)
		self.create_button = tk.Button(
			self, text="Modify", command=self.modify_card)
		self.modify_button = tk.Button(
			self, text="Modify cards", command=self.modify_cards)
		self.name_label.pack()
		self.name_entry.pack()
		self.color.pack()
		self.create_button.pack()
		self.modify_button.pack()

	def get_color(self):
		color = askcolor(title="Tkinter Color Chooser")
		self.savedColor = color

	def modify_card(self):
		ModifyFlashcardPage.flashcard.name = self.name_entry.get()
		ModifyFlashcardPage.flashcard.color = self.savedColor
		print(ModifyFlashcardPage.flashcard)
		# self.controller.show_frame(CreateCardPage)

	def modify_cards(self):
		# ModifyFlashcardPage.flashcard.name = self.name_entry.get()
		# ModifyFlashcardPage.flashcard.color = self.savedColor
		ModifyCardPage.set_flashcard(ModifyFlashcardPage.flashcard)
		self.controller.show_frame(ModifyCardPage)

	@staticmethod
	def set_flashcard(flash):
		print("setting flashcard")
		ModifyFlashcardPage.flashcard = flash


class CreateFlashcardPage(tk.Frame):
	def __init__(self, parent, controller, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.savedColor = None
		self.controller = controller
		self.name_label = tk.Label(self, text="Nom du flashcard:")
		self.name_entry = tk.Entry(self)
		# self.color_label = tk.Label(self, text="Couleur:")
		# self.color_entry = tk.Entry(self)
		self.color = tk.Button(
			self,
			text='Select a Color',
			command=self.get_color)
		self.create_button = tk.Button(
			self, text="Créer", command=self.create_card)

		self.name_label.pack()
		self.name_entry.pack()
		# self.color_label.pack()
		# self.color_entry.pack()
		self.color.pack()
		self.create_button.pack()

	def get_color(self):
		color = askcolor(title="Tkinter Color Chooser")
		self.savedColor = color

	def create_card(self):
		# Code pour la création de la carte ici
		flashcard = FlashCardData(self.name_entry.get(), color=self.savedColor)
		flashcards.append(flashcard)

		self.controller.show_frame(CreateCardPage)


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
		for F in (MainPage, CreateFlashcardPage, CreateCardPage, ModifyFlashcardPage, ModifyCardPage):
			# print(F)
			# CreateFlashcardPage
			frame = F(parent=self.container, controller=self)
			self.frames[F] = frame
			# frame.pack()
			frame.grid(row=0, column=0, sticky="nsew")

		# print("-----")
		self.show_frame(MainPage)

	def show_frame(self, cont, flashcard=None):
		# print(self.frames)
		# self.frames[cont] = cont(self.container, self)
		frame = self.frames[cont]
		print(frame)
		if flashcard:
			frame.set_flashcard(flashcard)
		frame.tkraise()


if __name__ == "__main__":
	app = Application()
	app.mainloop()
