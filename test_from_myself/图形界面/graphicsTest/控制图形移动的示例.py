from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

def moveRectangle(event):
    if event.keysym == "Up":
        canvas.move(1, 0, -5)
    if event.keysym == "Down":
        canvas.move(1, 0, 5)
    if event.keysym == "Left":
        canvas.move(1, -5, 0)
    if event.keysym == "Right":
        canvas.move(1, 5, 0)

canvas.create_rectangle(10, 10, 50, 50, fill="red")
canvas.bind_all("<KeyPress-Up>", moveRectangle)
canvas.bind_all("<KeyPress-Down>", moveRectangle)
canvas.bind_all("<KeyPress-Left>", moveRectangle)
canvas.bind_all("<KeyPress-Right>", moveRectangle)

tk.mainloop()