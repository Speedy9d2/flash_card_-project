from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
result = {}

# ---------------------------- DATA SETUP ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
    result = data.to_dict(orient="records")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    result = original_data.to_dict(orient="records")


# ---------------------------- FUNCTIONS SETUP ------------------------------- #
def check_click():
    global current_card
    current_card = random.choice(result)
    canvas.itemconfig(language_title, text='French', fill='black')
    canvas.itemconfig(the_word, text=current_card['French'], fill='black')
    canvas.itemconfig(canvas_image, image=white_img)
    window.after(3000, func=flip_card)


def known_cards():
    result.remove(current_card)
    new_data = pandas.DataFrame(result)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    check_click()


def flip_card():
    canvas.itemconfig(language_title, text='English', fill='white')
    canvas.itemconfig(the_word, text=current_card['English'], fill='white')
    canvas.itemconfig(canvas_image, image=back_img)


# ---------------------------- UI SETUP ------------------------------- #

# Window UI
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card)

# Canvas UI
canvas = Canvas(width=800, height=526, highlightthickness=0)
white_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=white_img)
language_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
the_word = canvas.create_text(400, 250, text="", font=("Ariel", 40, "bold italic"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons UI
check_mark = PhotoImage(file="images/right.png")
check_button = Button(image=check_mark, highlightthickness=0, command=known_cards)
check_button.grid(row=1, column=1)

wrong_mark = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_mark, highlightthickness=0, command=check_click)
wrong_button.grid(row=1, column=0)

check_click()
window.mainloop()
