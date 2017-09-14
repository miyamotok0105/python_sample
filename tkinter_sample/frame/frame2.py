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


base=tk.Tk()  #this is the main frame
root=tk.Frame(base)  #Really this is not necessary -- the other widgets could be attached to "base", but I've added it to demonstrate putting a frame in a frame.
root.grid(row=0,column=0)
scoreboard=tk.Frame(root, bg="blue")
scoreboard.grid(row=0,column=0,columnspan=2)

###
#Code to add stuff to scoreboard ...
# e.g. 
###
scorestuff=tk.Label(scoreboard,text="Here is the scoreboard", bg="blue")
scorestuff.grid(row=0,column=0)
#End scoreboard

#Start cards.
cards=tk.Frame(root, bg="red")
cards.grid(row=1,column=0)
###
# Code to add pitcher and batter cards
###
clabel=tk.Label(cards,text="Stuff to add cards here", bg="red")
clabel.grid(row=0,column=0)
#end cards

#Offense/Defense frames....
offense=tk.Frame(root)
offense.grid(row=1,column=1)
offense.isgridded=True #Dynamically add "isgridded" attribute.
offense_label=tk.Label(offense,text="Offense is coolest")
offense_label.grid(row=0,column=0)

defense=tk.Frame(root)
defense.isgridded=False
defense_label=tk.Label(defense,text="Defense is coolest")
defense_label.grid(row=0,column=0)

def switchOffenseDefense():
    print "Called"
    if(offense.isgridded):
        offense.isgridded=False
        offense.grid_forget()
        defense.isgridded=True
        defense.grid(row=1,column=1)
    else:
        defense.isgridded=False
        defense.grid_forget()
        offense.isgridded=True
        offense.grid(row=1,column=1)


switch_button=tk.Button(root,text="Switch",command=switchOffenseDefense)
switch_button.grid(row=2,column=1)

root.mainloop()
