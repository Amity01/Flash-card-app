from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
import pandas,random
#----------------------------Pick words-------------------------------
def flip_card():
    global new_dict
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{new_dict['English']}", fill="white")


def new_card():
    global new_dict, timer
    window.after_cancel(timer)
    new_dict = random.choice(to_learn)
    french_word = new_dict["French"]
    english_word = new_dict["English"]
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{french_word}", fill="black")
    timer = window.after(3000, flip_card)


def is_known():
    global new_dict
    to_learn.remove(new_dict)
    data1 = pandas.DataFrame(to_learn)
    data1.to_csv("data/words_to_learn.csv",index=False)
    new_card()
#-----------------------------UI--------------------------------------

new_dict = {}
try:
    data =pandas.read_csv("data/words_to_learn.csv")
except:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(height=526, width=800)
card_front = PhotoImage(file="images/card_front.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 25, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 50, "italic"))
canvas.grid(row=0, column=0, pady=20, columnspan=2)

timer = window.after(3000, flip_card)
new_card()

right_image = PhotoImage(file="images/right.png")
right_button =Button(image=right_image, command=is_known, bd=0, highlightthickness=0)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button =Button(image=wrong_image, command=new_card, bd=0, highlightthickness=0)
wrong_button.grid(row=1, column=1)















window.mainloop()