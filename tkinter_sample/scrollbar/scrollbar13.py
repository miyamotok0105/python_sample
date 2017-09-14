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


root=Tk() 
sb=Scrollbar(root) 
sb.pack(side=LEFT,fill=Y) 
print(sb.get())
# (0.0, 0.0, 0.0, 0.0) 
# sb.set(0.0,1.0) 
# sb.get() 

root.mainloop()
