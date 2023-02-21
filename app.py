from create import CreateFlashcardPage, CreateCardPage
from data import *
from functools import partial
from gtts import gTTS
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from modify import ModifyCardPage, ModifyFlashcardPage
from multiprocessing import Process
from pydub import AudioSegment
from render import FlashCardRender, ShowProgressPage
from threading import Thread
from time import sleep
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.colorchooser import askcolor
import asyncio
import data
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle
import time
import tkinter as tk
import winsound

data.init()


def _clear(canvas):
    for item in canvas.get_tk_widget().find_all():
        canvas.get_tk_widget().delete(item)


def leftClick(controller, flashcard, e):
    DisplayFlashcardPage.set_flashcard(flash=flashcard)
    controller.show_frame("DisplayFlashcardPage")


def playsound(filename, e):
    winsound.PlaySound(filename, winsound.SND_ASYNC)
    sleep(10)


def open_popup(win, text):
    top = Toplevel(win)
    top.geometry("200x200")
    top.title("Reminder")
    label = Label(top, text=text, font=("Arial 15 bold"))
    label.pack()


class CardRender(Frame):
    def __init__(self, parent, controller, cardData, flashcard) -> None:
        super().__init__(parent)
        self.cardData = cardData
        self.flashcard = flashcard
        self.card_frame = Frame(self, bg="#b1ddc6")
        self.card_frame1 = Frame(self.card_frame)
        self.frensh = Label(self.card_frame1, text="Frensh", font=("Arial 15 bold"))
        self.word = Label(self.card_frame1, text=cardData.info, font=("Arial 15 bold"))
        self.yes = Button(self.card_frame, text="YES", command=self.add)
        self.no = Button(self.card_frame, text="NO", command=self.nof)

        self.english = Label(self.card_frame1, text="English", font=("Arial 15 bold"))
        self.trans = Label(
            self.card_frame1, text=cardData.trans, font=("Arial 15 bold")
        )

    def showTrans(self):
        self.frensh.pack_forget()
        self.word.pack_forget()
        self.card_frame.pack(fill=BOTH, expand=1)
        self.english.pack(padx=50, pady=50)
        self.trans.pack(padx=50, pady=50)
        # self.card_frame1.pack(expand=1)
        self.yes.pack(side=RIGHT)
        self.no.pack(side=LEFT)
        self.pack(fill=BOTH, expand=1)

    def nof(self):
        self.no.config(state=tk.DISABLED)
        data.reminder.append(
            (self.cardData, datetime.datetime.now() + datetime.timedelta(days=1))
        )

    def show(self):
        self.card_frame.pack(fill=BOTH, expand=1)
        self.frensh.pack(padx=50, pady=50)
        self.word.pack(padx=50, pady=50)
        self.card_frame1.pack(expand=1)
        self.pack(fill=BOTH, expand=1)

    def add(self):
        self.yes.config(state=tk.DISABLED)
        data.reminder.append(
            (self.cardData, datetime.datetime.now() + datetime.timedelta(days=7))
        )
        data.reminder.append(
            (self.cardData, datetime.datetime.now() + datetime.timedelta(days=30))
        )
        lst = self.flashcard.progress[-1]
        lst[0] = lst[0] + 1


class DisplayFlashcardPage(tk.Frame):
    flashcard = None

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller
        self.frame = Frame(self.parent)
        main_button = tk.Button(self, text="Main", command=self.main)
        main_button.pack()

    def main(self):
        self.controller.show_frame("MainPage")

    def run(self):
        flashcard = DisplayFlashcardPage.flashcard
        if DisplayFlashcardPage.flashcard:
            nbr = len(DisplayFlashcardPage.flashcard)
            if nbr == 0:
                nbr = 1
            flashcard.progress.append([0, nbr])
            language = "fr"
            cardfs = []
            path = "./sounds/"
            funcs = []
            for j in range(nbr):
                cardd = DisplayFlashcardPage.flashcard.cards[j]
                s = "fr" + str(flashcard.name) + str(cardd.info) + str(cardd.trans)
                filename = f"{s}{j}"
                file = f"{path}{filename}"
                if not os.path.isfile(file + ".wav"):
                    speech = gTTS(text=cardd.info, lang=language, slow=True)
                    speech.save(f"{file}.mp3")
                    audio = AudioSegment.from_mp3(f"{file}.mp3")
                    audio.export(f"{file}.wav", format="wav")
                cardf = CardRender(self, self.controller, cardd, flashcard)
                cardfs.append(cardf)
            TIME = 5000
            j = 0
            processs = []
            for i, cardf in enumerate(cardfs):
                s = (
                    "fr"
                    + str(flashcard.name)
                    + str(cardf.cardData.info)
                    + str(cardf.cardData.trans)
                )
                filename = f"{s}{i}"
                file = f"{path}{filename}"
                self.after((j) * TIME, cardf.show)
                p = Thread(target=playsound, args=(file, (j) * TIME))
                self.after((j) * TIME, p.start)
                processs.append(p)
                self.after((j + 1) * TIME, cardf.showTrans)
                self.after((j + 2) * TIME, cardf.destroy)
                j += 2

    @staticmethod
    def set_flashcard(flash):
        DisplayFlashcardPage.flashcard = flash


class MainPage(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller
        self.main_frame = Frame(self)
        self.main_frame.pack(fill=BOTH, expand=1)
        self.my_canvas = Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.my_scrollbar = ttk.Scrollbar(
            self.main_frame, orient=VERTICAL, command=self.my_canvas.yview
        )
        self.my_scrollbar.pack(side=RIGHT, fill=Y)
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind(
            "<Configure>",
            lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")),
        )
        self.second_frame = Frame(self.my_canvas)
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")
        self.framex = Frame(self)
        self.run()
        rems = []
        for rem in data.reminder:
            if datetime.datetime.now() > rem[1]:
                open_popup(self.controller, rem[0])
            else:
                rems.append(rem)
        data.reminder = rems

    def run(self):
        clear_frame(self.second_frame)
        clear_frame(self.framex)
        nbr = len(data.flashcards)
        j = -1
        i = 0
        while i < nbr:
            if i % 2 == 0:
                j = j + 1
            flashcard = data.flashcards[i]
            card = FlashCardRender(
                self.second_frame, self.controller, flashcard, row=j, column=i % 2
            )
            card.bind("<Button-1>", partial(leftClick, self.controller, flashcard))
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
            ShowProgressPage,
        ):
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, cont, flashcard=None):
        frame = self.frames[cont]
        if cont == "MainPage":
            self.frames[cont] = MainPage(parent=self.container, controller=self)
            frame = self.frames[cont]
            frame.grid(row=0, column=0, sticky="nsew")
        if cont in (
            "MainPage",
            "ModifyCardPage",
            "DisplayFlashcardPage",
            "ShowProgressPage",
        ):
            frame.run()
        if flashcard:
            frame.set_flashcard(flashcard)
        frame.tkraise()


def save_data():
    file_name = "flashcards.pkl"
    with open(file_name, "wb") as file:
        pickle.dump(data.flashcards, file)
        print(f'Object successfully saved to "{file_name}"')
    file_name = "reminder.pkl"
    with open(file_name, "wb") as file:
        pickle.dump(data.reminder, file)
        print(f'Object successfully saved to "{file_name}"')


def load_data():
    file_name = "flashcards.pkl"
    with open(file_name, "rb") as file:
        data.flashcards = pickle.load(file)
        print(f'Object successfully loaded to "{file_name}"')
    file_name = "reminder.pkl"
    with open(file_name, "rb") as file:
        data.reminder = pickle.load(file)
        print(f'Object successfully loaded to "{file_name}"')


if __name__ == "__main__":
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

    data.flashcards = data.flashcards + [
        flashcard1,
        flashcard2,
        flashcard3,
        flashcard4,
        flashcard5,
        flashcard6,
        flashcard7,
    ]
    data.reminder = []
    load_data()
    app = Application()
    try:
        app.mainloop()
        save_data()
    except Exception as e:
        save_data()
        print(e)
