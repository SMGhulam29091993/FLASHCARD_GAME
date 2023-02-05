from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

try:
    data = pd.read_csv("data/words_to learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def english_card():
    global current_card
    canvas.itemconfig(canv_title, text="English", fill="white")
    canvas.itemconfig(canv_name, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=c_back)


def french_word():
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(data_dict)
    canvas.itemconfig(canv_title, text="French", fill="black")
    canvas.itemconfig(canv_name, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=c_front)
    flip_time = window.after(3000, english_card)
    print(current_card)


def unknowm_words():
    data_dict.remove(current_card)
    data_csv = pd.DataFrame(data_dict)
    data_csv.to_csv("data/words_to learn.csv", index=False)
    french_word()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_time = window.after(3000, english_card)

right_pic = PhotoImage(file="./images/right.png")
wrong_pic = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
c_back = PhotoImage(file="./images/card_back.png")
c_front = PhotoImage(file="./images/card_front.png")
card_image = canvas.create_image(400, 263, image=c_front)
canv_title = canvas.create_text(400, 150, text="", font=("Aerial", 40, "italic"))
canv_name = canvas.create_text(400, 253, text="", font=("Aerial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong_pic, highlightthickness=0, bg=BACKGROUND_COLOR, command=french_word)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_pic, highlightthickness=0, bg=BACKGROUND_COLOR, command=unknowm_words)
right_button.grid(column=1, row=1)

french_word()

window.mainloop()
