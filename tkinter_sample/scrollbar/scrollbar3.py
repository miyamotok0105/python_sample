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

root = Tk()

text1 = Text(root, height=20, width=30)
photo=PhotoImage(file='../../img/hari.jpeg')
text1.insert(END,'\n')
text1.image_create(END, image=photo)

text1.pack(side=LEFT)

text2 = Text(root, height=20, width=50)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042', 
						font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
text2.insert(END,'\nWilliam Shakespeare\n', 'big')
quote = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
"""
text2.insert(END, quote, 'color')
text2.insert(END, 'follow-up\n', 'follow')
text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
