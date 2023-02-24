from data import FlashCardData, CardData
from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
import data
import tkinter as tk


class CreateCardPage(tk.Frame):
    flashcard = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.savedColor = None

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

    def main(self):
        self.controller.show_frame("MainPage")

    def reset(self):
        self.word_entry.delete(0, END)
        self.translation_entry.delete(0, END)
        self.savedColor = None

    def get_color(self):
        color = askcolor(title="Tkinter Color Chooser")
        self.savedColor = color

    @staticmethod
    def set_flashcard(flash):
        CreateCardPage.flashcard = flash

    def save_card(self):
        try:
            word = self.word_entry.get()
            translation = self.translation_entry.get()
            card = CardData(word)
            CreateCardPage.flashcard.cards.append(card)
            # print("---------")
        except Exception as e:
            print(e)


class CreateFlashcardPage(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.savedColor = None
        self.controller = controller
        self.name_label = tk.Label(self, text="Nom du flashcard:")
        self.name_entry = tk.Entry(self)
        self.color = tk.Button(self, text="Select a Color", command=self.get_color)
        self.create_button = tk.Button(self, text="Create", command=self.create_card)
        self.name_label.pack()
        self.name_entry.pack()
        self.color.pack()
        self.create_button.pack()
        createCardPage = CreateCardPage(parent=self, controller=controller)
        createCardPage.pack()

    def get_color(self):
        color = askcolor(title="Tkinter Color Chooser")
        self.savedColor = color

    def create_card(self):
        flashcard = FlashCardData(self.name_entry.get(), color=self.savedColor)
        data.flashcards.append(flashcard)
        CreateCardPage.set_flashcard(flash=flashcard)
        # self.controller.show_frame("CreateCardPage")
