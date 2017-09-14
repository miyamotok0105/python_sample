# -*- coding: utf-8 -*-
try:
    import tkinter as tk # for python 3
    from tkinter import messagebox
    import tkinter.ttk as ttk
except:
    import Tkinter as tk # for python 2
    import tkMessageBox as messagebox
    from Tkinter import *
    import ttk
    

def main():
    root = Tk()
    frame = Frame(root)

    canvas = Canvas(frame, width=400, height=400, scrollregion=(0, 0, 800, 800))
    xscroll = Scrollbar(frame, orient=HORIZONTAL, command=canvas.xview)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+E+W+S)

    canvas.bind("<ButtonPress-1>", lambda e: canvas.scan_mark(e.x, e.y))
    canvas.bind("<B1-Motion>", lambda e: canvas.scan_dragto(e.x, e.y, gain=1))

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid(sticky=N+E+W+S)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()


if __name__ == '__main__':
    main()

