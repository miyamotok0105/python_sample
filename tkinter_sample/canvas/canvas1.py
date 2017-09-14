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


root = tk.Tk()
c = tk.Canvas(root, width = 400, height = 400)
c.pack()

imagepath = "../../img/hari.jpeg"
img = Image.open(imagepath)
tkimg = ImageTk.PhotoImage(img)

print(img)

c.create_image(0, 0, image = tkimg, anchor=NW)

root.mainloop()
