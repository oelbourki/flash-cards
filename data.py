from tkinter import *
"""
		self.frame = Frame(self.root,bg="red")
		label1 = Label(self.frame, text="Vocabulary",font=('Arial 15 bold'),bg="red")
		label2 = Label(self.frame, text="20 card",font=('Arial 15 bold'),bg="red")
		label1.pack(padx=30, pady=30)
		label2.pack(padx=30, pady=30)
		self.frame.grid(row=0,column=0,padx=30,pady=30)
"""
class Card:
	def __init__(self, question, yes) -> None:
		self.question = question
		self.yes = yes

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
