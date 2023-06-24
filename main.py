BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
from random import *




def next_word():
    df = pd.read_csv('data/french_words.csv')
    datas = df.to_dict()

    rand_number = randint(0, 100)
    french_word = datas["French"][rand_number]
    english_word = datas["English"][rand_number]

    flash_card.itemconfigure(title, text="French")
    flash_card.itemconfigure(word, text=french_word)


window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

old_img = PhotoImage(file='images/card_front.png')
new_img = PhotoImage(file='images/card_back.png')
no_img = PhotoImage(file='images/wrong.png')
yes_img = PhotoImage(file='images/right.png')


flash_card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

flash_card.create_image(400, 263, image=old_img)
flash_card.grid(column=1, row=1, columnspan=2)
title = flash_card.create_text(400, 150, text="", fill='black', font=("Ariel", 40, "italic"))
word = flash_card.create_text(400, 263, text="", fill='black', font=("Ariel", 60, 'bold'))


no_button = Button(image=no_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_word)
no_button.grid(column=1, row=2)

yes_button = Button(image=yes_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_word)
yes_button.grid(column=2, row=2,)

next_word()
window.mainloop()

