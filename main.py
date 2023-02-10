import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from data import Card, CardData
# from debug import printBoard
from functools import partial
from data import FlashCard

flashcards = []
allCards = {}


def leftClick(e):
    print("left")


class CreateFlashcardPage(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller
        self.name_label = tk.Label(self, text="Nom du flashcard:")
        self.name_entry = tk.Entry(self)
        self.color_label = tk.Label(self, text="Couleur:")
        self.color_entry = tk.Entry(self)
        self.create_button = tk.Button(
            self, text="Créer", command=self.create_card)

        self.name_label.pack()
        self.name_entry.pack()
        self.color_label.pack()
        self.color_entry.pack()
        self.create_button.pack()

    def create_card(self):
        # Code pour la création de la carte ici
        pass


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.bind('<Control-c>', self.destroy)
        self.root.bind('<Control-d>', self.destroy)
        self.root.title("Flash Cards")
        self.width, self.height = (550, 600)
        self.root.resizable(False, False)
        self.root.geometry(f"{self.width}x{self.height}")
        main_frame = Frame(self.root)
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

        self.flashCards = []
        for i in range(10):
            card = FlashCard(second_frame, bg="red",
                             name="Vocabulary", row=i, column=0)
            card1 = FlashCard(second_frame, bg="red",
                              name="Math", row=i, column=1)
            card.bind("<Button-1>", leftClick)
            self.flashCards.append(card)
            self.flashCards.append(card1)
        # add.pack()

        framex = Frame(self.root)
        add = Button(framex, text="+", command=lambda e: e)
        add.pack(side=LEFT)
        framex.pack(side=RIGHT)
        framex.tkraise()
        # self.clear_frame(self.root)
        cards = [CardData("boulout"), CardData("test"), CardData("war"), CardData("idea"),
                 CardData("game"), CardData("titw")]
        # Creat class that manages everything
        # while True:
        # self.clear_frame(self.root)
        # cardsGui = []
        # for card in cards:
        # 	cardsGui.append(Card(self.root, cards[0]))
        # frame = CreateFlashcardPage(self.root,self.root)
        # frame.pack()
        # frame.tkraise()
        # framex = Frame(self.root)
        # add = Button(framex, text="+",command=lambda e:e)
        # add.pack(side=LEFT)
        # framex.pack(side=RIGHT)
        # framex.tkraise()

    def clear_frame(self, root):
        for widgets in root.winfo_children():
            widgets.destroy()

    def destroy(self, event):
        self.root.destroy()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

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
