# -*- coding: utf-8 -*-
#!/usr/bin/python

try:
    import tkinter as tk # for python 3
    from tkinter import messagebox
    import tkinter.ttk as ttk
except:
    import Tkinter as tk # for python 2
    import tkMessageBox as messagebox
    from Tkinter import *
    import ttk

import time


root = Tk()

h = ttk.Scrollbar(root, orient = HORIZONTAL)
v = ttk.Scrollbar(root, orient = VERTICAL)
canvas = Canvas(root, scrollregion = (0, 0, 2000, 2000), width = 600, height = 600, yscrollcommand = v.set, xscrollcommand = h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview
ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S,E))

canvas.grid(column = 0, row = 0, sticky = (N,W,E,S))
h.grid(column = 0, row = 1, sticky = (W,E))
v.grid(column = 1, row = 0, sticky = (N,S))
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)

canvas.create_rectangle((0, 0, 50, 50), fill = 'black')
canvas.create_rectangle((500, 500, 550, 550), fill = 'black')
canvas.create_rectangle((1500, 1500, 1550, 1550), fill = 'black')
canvas.create_rectangle((1000, 1000, 1050, 1050), fill = 'black')

def xy_motion(event):
    x, y = event.x, event.y

    if x < 30:        
        delta = -1
        canvas.xview('scroll', delta, 'units')

    if x > (600 - 30):
        delta = 1
        canvas.xview('scroll', delta, 'units')

    if y < 30:
        delta = -1
        canvas.yview('scroll', delta, 'units')

    if y > (600 - 30):
        delta = 1
        canvas.yview('scroll', delta, 'units')

canvas.bind('<Motion>', xy_motion)

root.mainloop()

