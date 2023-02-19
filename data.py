from tkinter import *
# from test import ModifyFlashcardPage
"""
		self.frame = Frame(self.root,bg="red")
		label1 = Label(self.frame, text="Vocabulary",font=('Arial 15 bold'),bg="red")
		label2 = Label(self.frame, text="20 card",font=('Arial 15 bold'),bg="red")
		label1.pack(padx=30, pady=30)
		label2.pack(padx=30, pady=30)
		self.frame.grid(row=0,column=0,padx=30,pady=30)
"""
def init():
	global flashcards
	global reminder
	reminder = []
	flashcards = []
# flashcards = []
# allCards = {}

def clear_frame(root):
	for widgets in root.winfo_children():
		widgets.destroy()

class Card:
	def __init__(self, word, translation, color):
		self.word = word
		self.translation = translation
		self.color = color

class CardData:
	def __init__(self, info, trans=None,  flashcard=None) -> None:
		self.info = info
		self.trans = trans
		self.flashcard = flashcard
	
	def __str__(self) -> str:
		return f"info:{self.info}, trans: {self.trans}"



class FlashCardData:
	def __init__(self,name, color, cards=[]) -> None:
		self.name = name
		self.color = color
		self.cards = cards
		self.progress = []
		self.reminder = []

	def append(self, card):
		self.cards.append(card)

	def __len__(self):
		return len(self.cards)
	
	def __str__(self) -> str:
		s = f"name:{self.name}, color:{self.color}, nbr:{len(self.cards)}: "
		for card in self.cards:
			s += f"{card} ,"
		s += "Progress: "
		for card in self.progress:
			s += f"{card} ,"
		return s



class FlashCard(Frame):
	def __init__(self, root,bg, name,row,column) -> None:
		super().__init__(root,bg=bg,width=200,height=200)
		self.name = name
		self.nbr = 0
		self.cards = []
		label1 = Label(self, text=name,font=('Arial 15 bold'),bg="red")
		label2 = Label(self, text=f"{len(self.cards)} card",font=('Arial 15 bold'),bg="red")
		label1.pack(padx=30, pady=30)
		label2.pack(padx=30, pady=30)
		self.grid(row=row,column=column,padx=30,pady=30)
		self.pack_propagate(0)
