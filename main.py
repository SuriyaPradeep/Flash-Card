from tkinter import *
import pandas as pd
import random

# --------------------------------READING FILE-------------------------------- #
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
    data = data.to_dict(orient="records")
else:
    data = data.to_dict(orient="records")


# --------------------------------GENERATING RANDOM WORDS-------------------------------- #
def generate_words():
    # noinspection PyGlobalUndefined
    global time, random_word
    wrong_btn.config(state="disabled")
    right_btn.config(state="disabled")
    try:
        random_word = random.choice(data)
    except IndexError:
        canvas.itemconfig(canvas_image, image=french_photo)
        canvas.itemconfig(title_text, text='Congrats!!!', fill='black')
        canvas.itemconfig(word_text, text='You Have Completed the Flashcard!!!', fill='black',
                          font=("Ariel", 30, "bold"))
    else:
        canvas.itemconfig(canvas_image, image=french_photo)
        canvas.itemconfig(title_text, text='French', fill='black')
        canvas.itemconfig(word_text, text=random_word['French'], fill='black')
        time = window.after(3000, english_words)  # It can call function and pass a parameter


def english_words():
    window.after_cancel(time)
    wrong_btn.config(state="normal")
    right_btn.config(state="normal")
    canvas.itemconfig(canvas_image, image=english_photo)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=random_word['English'], fill='white')


def guessed():
    data.remove(random_word)
    data1 = pd.DataFrame(data)
    data1.to_csv('data/words_to_learn.csv', index=False)
    generate_words()


# --------------------------------CONSTANTS-------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# --------------------------------UI-------------------------------- #
# Main window
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
french_photo = PhotoImage(file='images/card_front.png')
english_photo = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=french_photo)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text='Words', font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# wrong btn
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=generate_words)
# relief used to hide borders in the button
wrong_btn.grid(row=1, column=0, pady=50)

# right btn
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=guessed)
right_btn.grid(row=1, column=1, pady=50)

generate_words()
window.mainloop()
