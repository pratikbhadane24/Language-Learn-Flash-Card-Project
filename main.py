from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


try:
    data = pandas.read_csv("data/my_words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def is_known():
    words_to_learn.remove(current_card)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/my_words_to_learn.csv", index=False)

    next_card()


# Screen and Canvas
window = Tk()
window.title("Learn with Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(0, 0)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800,)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
button = Button(image=card_front_img, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="", font=("Fira Code", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
cross_btn = Button(image=cross_image, command=next_card)
cross_btn.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
tick_btn = Button(image=tick_image, command=is_known)
tick_btn.grid(row=1, column=1)


next_card()

canvas.mainloop()
