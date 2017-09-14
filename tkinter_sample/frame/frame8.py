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

root = tk.Tk()
root.configure( bg = bg_color)
root.title("Comparatore")

logo_canvas = tk.Canvas( root,  bg = "black", highlightthickness = 0, height = 58, width = 1200 )
logo_canvas.grid( row = 0, column = 0, ipadx = 0, ipady=0, sticky = "nw")
# bg_label = tk.Label( root, bg = bg_color )
# bg_label.grid( row = 1, column = 0, sticky = "nesw")
# select_text = tk.Label( bg_label, text = " Selezionare il numero di macchine da confrontare: ", 
#         font = ("verdana", 16), bg = bg_color)
# select_text.grid( row = 0, column = 0, sticky = "nsew")

background_space = tk.Frame( root, bg = 'green', height = 58, width = 590)
background_space.grid( row = 2, column = 0, sticky = "wesn", padx = 10  )

tab_space1 = tk.Canvas( background_space, bg = 'red', highlightthickness = 0, width = 400, height = 600, scrollregion=(0, 0, 2000, 780))
tab_space1.grid( row = 0, column = 0)

imagepath = "../../img/hari.jpeg"
img = Image.open(imagepath)
tkimg = ImageTk.PhotoImage(img)

print(img)
tab_space1.create_image(0, 0, image = tkimg, anchor=NW)

scrollY = tk.Scrollbar ( background_space, bg = bg_color, bd = 4, activebackground = bg_color, orient = "vertical")
scrollY.grid( row = 0, column = 1, sticky = "nswe")
scrollY.configure( command = tab_space1.yview)
tab_space1.configure(yscrollcommand = scrollY.set )

#-----------------------
tab_space2 = tk.Canvas( background_space, bg = 'yellow', highlightthickness = 0, width = 100, height = 600, scrollregion=(0, 0, 2000, 780))
tab_space2.grid( row = 0, column = 2)

tab_space2_label1 = tk.Label( tab_space2, bg = bg_color , anchor=NW, text = "label1")
tab_space2_label1.grid( row = 0, column = 0)

tab_space2_label2 = tk.Label( tab_space2, bg = bg_color , anchor=NW, text = "label1")
tab_space2_label2.grid( row = 1, column = 0)

#-----------------------
tab_space3 = tk.Canvas( background_space, bg = 'pink', highlightthickness = 0, width = 100, height = 600, scrollregion=(0, 0, 2000, 780))
tab_space3.grid( row = 0, column = 3)


tk.mainloop()








