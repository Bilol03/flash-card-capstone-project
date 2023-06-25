BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
from random import *

num = 0

df = pd.read_csv('data/french_words.csv')
datas = df.to_dict(orient="records")
data = {}
learned_word_list = []


def next_word():
    global data, id_window
    window.after_cancel(id_window)

    data = choice(datas)

    flash_card.itemconfigure(card_img, image=old_img)
    flash_card.itemconfigure(title, text="French")
    flash_card.itemconfigure(word, text=data['French'])
    id_window = window.after(3000, back_card)


def back_card():
    global data
    flash_card.itemconfigure(card_img, image=new_img)
    flash_card.itemconfigure(title, text="English")
    flash_card.itemconfigure(word, text=data["English"])


def learned_words():
    global data, learned_word_list
    learned_word_list.append(data)
    data_frame = pd.DataFrame(learned_word_list)
    data_frame.to_csv('data/learned_words.csv', index=False)
    datas.remove(data)
    df = pd.DataFrame(datas)
    df.to_csv('data/french_words.csv', index=False)
    next_word()

window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
id_window = window.after(3000, back_card)

old_img = PhotoImage(file='images/card_front.png')
new_img = PhotoImage(file='images/card_back.png')
no_img = PhotoImage(file='images/wrong.png')
yes_img = PhotoImage(file='images/right.png')


flash_card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_img = flash_card.create_image(400, 263, image=old_img)
flash_card.grid(column=1, row=1, columnspan=2)
title = flash_card.create_text(400, 150, text="", fill='black', font=("Ariel", 40, "italic"))
word = flash_card.create_text(400, 263, text="", fill='black', font=("Ariel", 60, 'bold'))


no_button = Button(image=no_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_word)
no_button.grid(column=1, row=2)

yes_button = Button(image=yes_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=learned_words)
yes_button.grid(column=2, row=2,)

next_word()
window.mainloop()

