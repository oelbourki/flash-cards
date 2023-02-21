from tkinter import *


def init():
    global flashcards
    global reminder
    reminder = []
    flashcards = []


def clear_frame(root):
    for widgets in root.winfo_children():
        widgets.destroy()


class Card:
    def __init__(self, word, translation, color):
        self.word = word
        self.translation = translation
        self.color = color


class CardData:
    def __init__(self, info, trans=None, flashcard=None) -> None:
        self.info = info
        self.trans = trans
        self.flashcard = flashcard

    def __str__(self) -> str:
        return f"info:{self.info}, trans: {self.trans}"


class FlashCardData:
    def __init__(self, name, color, cards=[]) -> None:
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
