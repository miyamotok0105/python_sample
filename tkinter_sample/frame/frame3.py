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



root=tk.Tk()
f1 = tk.Frame(width=200, height=200, background="red")
f2 = tk.Frame(width=100, height=100, background="blue")

f1.pack(fill="both", expand=True, padx=20, pady=20)
f2.pack(fill="both", expand=True, padx=20, pady=20)
# f2.place(in_=f1, anchor="c", relx=.5, rely=.5)

root.mainloop()

