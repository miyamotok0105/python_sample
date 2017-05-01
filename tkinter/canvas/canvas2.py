# -*- coding: utf-8 -*-
from __future__ import division
try:
    import tkinter as tk # for python 3
    from tkinter import messagebox
    import tkinter.ttk as ttk
except:
    import Tkinter as tk # for python 2
    import tkMessageBox as messagebox
    from Tkinter import *
    import ttk
from PIL import Image, ImageTk

root = Tk()
root.geometry('500x500+100+100')

imagepath = "../../img/hari.jpeg"
img = Image.open(imagepath)
tkimg = ImageTk.PhotoImage(img)


canvas = Canvas(root, width = 500, height = 400, bg = 'white')
canvas.pack
imageFinal = canvas.create_image(300, 300, image = tkimg, anchor=NW)

def move():
    canvas.move(imageFinal, 0, 22)  
    canvas.update()

button = Button(text = 'move', height = 3, width = 10, command = move)
button.pack(side = 'bottom', padx = 5, pady = 5)

root.mainloop()
