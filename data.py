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
class CardData:
	def __init__(self, info) -> None:
		self.info = info
	
	def __str__(self) -> str:
		return f"info:{self.info}"

class Card(Frame):
	def __init__(self,root, cardData) -> None:
		super().__init__(root)
		# self.question = question
		# self.yes = yes
		card_frame = Frame(self,bg="#b1ddc6")
		card_frame1 = Frame(card_frame)
		frensh = Label(card_frame1, text="Frensh",font=('Arial 15 bold'))
		word = Label(card_frame1, text=cardData.info,font=('Arial 15 bold'))
		card_frame.pack(fill=BOTH, expand=1)
		frensh.pack(padx=50,pady=50)
		word.pack(padx=50,pady=50)
		card_frame1.pack(expand=1)
		yes = Button(card_frame, text="YES",command=lambda e:e)
		no = Button(card_frame, text="NO",command=lambda e:e)
		yes.pack(side=RIGHT)
		no.pack(side=LEFT)
		self.pack(fill=BOTH, expand=1)

class FlashCardData:
	def __init__(self,name, color, cards=[]) -> None:
		self.name = name
		self.color = color
		self.cards = cards
	
	def append(self, card):
		self.cards.append(card)

	def __len__(self):
		return len(self.cards)
	
	def __str__(self) -> str:
		return f"name:{self.name}, color:{self.color}, nbr:{len(self.cards)}"



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
