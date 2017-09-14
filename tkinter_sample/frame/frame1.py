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
COLORS = ['red', 'blue', 'yellow', 'pink', 'cyan', 'green', 'orange', 'black']
SIZE = 826, 1169
print("w " + str(SIZE[0]))
print("h " + str(SIZE[1]))

class LabelTool():

    def __init__(self, master):
        # set up the main frame
        self.root = master
        self.root.title("LabelTool")
        self.root.configure(background='black')

        self.logo_canvas = tk.Canvas( self.root,  bg = "blue", highlightthickness = 0, height = 58, width = 590 )
        self.logo_canvas.grid( row = 0, column = 0, ipadx = 0, ipady=0, sticky = "nw")

        self.background_space = tk.Frame( self.root, bg = 'green', height = 58, width = 590)
        self.background_space.grid( row = 2, column = 0, sticky = "wesn", padx = 10  )

        self.tab_space = tk.Canvas( self.background_space, bg = 'red', highlightthickness = 0, width = 400, height = 600, scrollregion=(0, 0, 2000, 780))
        self.tab_space.grid( row = 0, column = 0)

        imagepath = "../../img/hari.jpeg"
        self.img = Image.open(imagepath)
        self.tkimg = ImageTk.PhotoImage(self.img)

        print(self.img)
        self.tab_space.create_image(0, 0, image = self.tkimg, anchor=NW)

        scrollY = tk.Scrollbar ( self.background_space, bg = bg_color, bd = 4, activebackground = bg_color, orient = "vertical")
        scrollY.grid( row = 0, column = 1, sticky = "nswe")

        scrollY.configure( command = self.tab_space.yview)
        self.tab_space.configure(yscrollcommand = scrollY.set )

        # main panel for labeling
        # vscrollbar = Scrollbar(root,orient=VERTICAL)
        # vscrollbar.grid(row=0, column=5, sticky=N+S)
        # hscrollbar = Scrollbar(root,orient=HORIZONTAL)
        # hscrollbar.grid(row=10, column=0, sticky=E+W)

        # self.mainPanel = Frame(self.root, bg="red")
        # self.mainPanel.grid(row=0, column=0, sticky=N+W)
        # self.mainPanel.pack()

        # self.mainPanel = Canvas(self.root, cursor='tcross', bg="red")
        # self.mainPanel.grid(row=0, column=0, sticky=N+W)
        # self.mainPanel.pack(fill=BOTH)
        #     ,
        #     yscrollcommand=vscrollbar.set,
        #     xscrollcommand=hscrollbar.set)
        # vscrollbar.config(command=self.mainPanel.yview)
        # hscrollbar.config(command=self.mainPanel.xview)
        
        # self.op_frame = Frame(self.mainPanel, bg="green")
        # self.op_frame.grid(row=0, column=0, sticky=N+W)
        # self.op_frame.pack()
        # self.subPanel = Canvas(self.op_frame, cursor='tcross', bg="yellow")
        # # self.subPanel.grid(row = 0, column = 0, rowspan = 7, sticky = W+N)
        # self.subPanel.grid(row=1, column=1, sticky=W+E)

        # self.frame = Frame(self.mainPanel, bg="blue")
        # self.frame.grid(row=0, column=1, sticky=N+W)
        # self.frame.pack(expand=1)
        # self.root.resizable(width = FALSE, height = FALSE)

        # self.mainPanel.update_idletasks()
        # self.op_frame.update_idletasks()




if __name__ == '__main__':
    root = tk.Tk()
    tool = LabelTool(root)


    tk.mainloop()








