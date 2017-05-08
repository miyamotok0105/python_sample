from tkinter import *

def close_window():
    root.destroy()  # destroying the main window

root = Tk()
frame = Frame(root)
frame.pack()

button = Button(frame)
button['text'] ="Good-bye."
button['command'] = close_window
button.pack()

mainloop()
