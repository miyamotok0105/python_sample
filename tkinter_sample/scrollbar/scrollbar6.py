# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
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


bg_color = "#d3d3d3"

top = tk.Tk()
top.configure( bg = bg_color)
top.title("Comparatore")

master = tk.Frame( top, bg = 'green', height = 58, width = 590)
master.grid( row = 2, column = 0, sticky = "wesn", padx = 10  )

tab_space = tk.Canvas( master, bg = 'red', highlightthickness = 0, width = 400, height = 600, scrollregion=(0, 0, 2000, 780))
tab_space.grid( row = 0, column = 0)

imagepath = "../../img/hari.jpeg"
img = Image.open(imagepath)
tkimg = ImageTk.PhotoImage(img)

print(img)
tab_space.create_image(0, 0, image = tkimg, anchor=NW)

scrollY = tk.Scrollbar ( master, bg = bg_color, bd = 4, activebackground = bg_color, orient = "vertical")
scrollY.grid( row = 0, column = 1, sticky = "nswe")

scrollY.configure( command = tab_space.yview)
tab_space.configure(yscrollcommand = scrollY.set )


tk.mainloop()






