from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Learn with Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(0,0)


canvas = Canvas(height=526, width=800,)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
button = Button(image=card_front_img, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400,150, text="Title", font=("Fira Code", 40, "italic"))
canvas.create_text(400,263, text="Word", font=("Fira Code", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
cross_btn = Button(image=cross_image)
cross_btn.config(highlightthickness=0)
cross_btn.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
tick_btn = Button(image=tick_image)
tick_btn.grid(row=1, column=1)



canvas.mainloop()