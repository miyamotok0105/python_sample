# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#http://www.tkdocs.com/tutorial/grid.html
#-------------------------------------------------------------------------------
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
from time import sleep
import numpy as np
import os
import io
import glob
import random
import cv2

root = Tk()

content = tk.Frame(root, bg='blue')
frame = tk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100, bg='green')
namelbl = tk.Label(content, text="Name", bg="red")
name = tk.Entry(content, bg="yellow")

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(True)
twovar.set(False)
threevar.set(True)

one = tk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = tk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = tk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = tk.Button(content, text="Okay")
cancel = tk.Button(content, text="Cancel")
test1 = tk.Button(content, text="test1")

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=3, row=0, columnspan=2)
name.grid(column=3, row=1, columnspan=2)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)
test1.grid(column=5, row=3)


root.mainloop()

