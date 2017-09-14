# -*- coding: utf-8 -*-
from __future__ import division
try:
    import tkinter as tk # for python 3
    from tkinter import messagebox
    import tk.ttk as ttk
except:
    import Tkinter as tk # for python 2
    import tkMessageBox as messagebox
    from Tkinter import *
    import ttk
import table, string
from PIL import Image, ImageTk
from functions import *
# from functions import *

bg_color = "#d3d3d3"
first_table = True

# MODEL: Functions to handle the main processing of the program in
# response to user interaction
def create_tables():
    global tab, first_table, tab_space, mbtext
    select = choice.get()
    choices = [ 1, 2, 3, 4, 5]
    mbtext.set( str( choices[select])) # resetting the number in the menubutton
    if not first_table:
        # cleaning the canvas
        t.destroy()
        comp_space.destroy()
    # space to display the objects
    master = tk.Frame( top, bg = 'green')
    master.grid( row = 2, column = 0, sticky = "wesn", padx = 10  )

    # space for the table:
    tab_space = tk.Canvas( master, bg = 'red', highlightthickness = 0, height = 600, scrollregion=(0, 0, 2000, 780))
    tab_space.grid( row = 0, column = 0)

    # creating the table...
    tab = table.CompTable( tab_space, columns = choices[select]+1 )
    tab.first_set()
    tab_space.create_window(0, 0, anchor = "nw", window = tab)

    # and the scrollbar:
    scrollY = tk.Scrollbar ( master, bg = bg_color, bd = 4, activebackground = bg_color, orient = "vertical")
    scrollY.grid( row = 0, column = 1, sticky = "nswe")

    #binding canvas and scrollbar together
    scrollY.configure( command = tab_space.yview)
    tab_space.configure(yscrollcommand = scrollY.set )

# VIEW: Setup the widgets

# The main window
top = tk.Tk()
top.configure( bg = bg_color)
top.title("Comparatore")

# logo_frame/canvas - using a Canvas object to load images
logo_canvas = tk.Canvas( top,  bg = bg_color, highlightthickness = 0, height = 58, width = 590 )
logo_canvas.grid( row = 0, column = 0, ipadx = 0, ipady=0, sticky = "nw")


# background
bg_label = tk.Label( top, bg = bg_color )
bg_label.grid( row = 1, column = 0, sticky = "nesw")

# menu to handle how many items we are using
select_text = tk.Label( bg_label, text = " Selezionare il numero di macchine da confrontare: ", 
        font = ("verdana", 16), bg = bg_color)
select_text.grid( row = 0, column = 0, sticky = "nsew")

mbtext = tk.StringVar()
mbtext.set("")
how_many_mb = tk.Menubutton( bg_label, textvariable = mbtext, relief= "raised", bg = bg_color)
how_many_mb.menu = tk.Menu( how_many_mb, tearoff = 0)
how_many_mb["menu"] = how_many_mb.menu
how_many_mb.grid( row = 0, column = 1, sticky = "nsew", padx = 4, ipadx = 18)

# CONTROLLER
choice = tk.IntVar()
how_many_mb.menu.add_radiobutton( label = "1", variable = choice, value = 0, command = create_tables)
how_many_mb.menu.add_radiobutton( label = "2", variable = choice, value = 1, command = create_tables)
how_many_mb.menu.add_radiobutton( label = "3", variable = choice, value = 2, command = create_tables)
how_many_mb.menu.add_radiobutton( label = "4", variable = choice, value = 3, command = create_tables)
how_many_mb.menu.add_radiobutton( label = "5", variable = choice, value = 4, command = create_tables)


##
tk.mainloop()

