from data import CardData, clear_frame
from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
import data
import tkinter as tk


class ModifyCardPage(tk.Frame):
    flashcard = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.savedColor = None
        self.run()

    def run(self):
        clear_frame(self)
        word_label = tk.Label(self, text="Word")
        self.word_entry = tk.Entry(self)
        translation_label = tk.Label(self, text="Translation")
        self.translation_entry = tk.Entry(self)
        color = tk.Button(self, text="Select a Color", command=self.get_color)
        word_label.grid(row=0, column=0, sticky="e")
        self.word_entry.grid(row=0, column=1)
        translation_label.grid(row=1, column=0, sticky="e")
        self.translation_entry.grid(row=1, column=1)
        save_button = tk.Button(self, text="Save", command=self.save_card)
        save_button.grid(row=3, column=1, pady=10)
        reset_button = tk.Button(self, text="Reset", command=self.reset)
        reset_button.grid(row=3, column=0, pady=10)
        main_button = tk.Button(self, text="Main", command=self.main)
        main_button.grid(row=3, column=2, pady=10)

        if ModifyCardPage.flashcard:
            nbr = len(ModifyCardPage.flashcard)
            self.buttons = []
            i = 0
            j = 0
            while i < nbr:
                card = ModifyCardPage.flashcard.cards[i]
                button = tk.Button(
                    self, text=str(card), command=partial(self.delete_card, i)
                )
                if i % 5 == 0:
                    j = j + 1
                button.grid(row=3 + j, column=i % 4)
                i = i + 1

    def delete_card(self, i):
        ModifyCardPage.flashcard.cards.pop(i)
        for button in self.buttons:
            button.forget_grid()
        self.run()

    def main(self):
        self.controller.show_frame("MainPage")

    def reset(self):
        self.word_entry.delete(0, END)
        self.translation_entry.delete(0, END)
        self.savedColor = None

    def get_color(self):
        color = askcolor(title="Tkinter Color Chooser")
        self.savedColor = color[1]

    def save_card(self):
        word = self.word_entry.get()
        translation = self.translation_entry.get()
        card = CardData(word)
        ModifyCardPage.flashcard.cards.append(card)
        self.run()

    @staticmethod
    def set_flashcard(flash):
        ModifyCardPage.flashcard = flash


class ModifyFlashcardPage(tk.Frame):
    flashcard = None

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.savedColor = None
        self.controller = controller
        self.name_label = tk.Label(self, text="Nom du flashcard:")
        self.name_entry = tk.Entry(self)
        self.color = tk.Button(self, text="Select a Color", command=self.get_color)
        self.create_button = tk.Button(self, text="Modify", command=self.modify_card)
        self.delete_button = tk.Button(self, text="Delete", command=self.delete)
        self.modify_button = tk.Button(
            self, text="Modify cards", command=self.modify_cards
        )
        main_button = tk.Button(self, text="Main", command=self.main)

        self.name_label.pack()
        self.name_entry.pack()
        self.color.pack()
        self.create_button.pack()
        self.delete_button.pack()

        self.modify_button.pack()
        main_button.pack()

    def main(self):
        self.controller.show_frame("MainPage")

    def show(self):
        pass

    def delete(self):
        data.flashcards.remove(ModifyFlashcardPage.flashcard)
        self.controller.show_frame("MainPage")

    def get_color(self):
        color = askcolor(title="Tkinter Color Chooser")
        self.savedColor = color[1]

    def modify_card(self):
        ModifyFlashcardPage.flashcard.name = self.name_entry.get()
        if self.savedColor:
            ModifyFlashcardPage.flashcard.color = self.savedColor
            self.savedColor = None
        # self.controller.show_frame(CreateCardPage)

    def modify_cards(self):
        ModifyCardPage.set_flashcard(ModifyFlashcardPage.flashcard)
        self.controller.show_frame("ModifyCardPage")

    @staticmethod
    def set_flashcard(flash):
        ModifyFlashcardPage.flashcard = flash
