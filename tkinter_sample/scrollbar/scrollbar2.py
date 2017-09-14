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


class scrollTxtArea:
	def __init__(self,root):
		frame=Frame(root)
		frame.pack()
		self.textPad(frame)
		return

	def textPad(self,frame):
		#add a frame and put a text area into it
		textPad=Frame(frame)
		self.text=Text(textPad,height=50,width=90)
		
		# add a vertical scroll bar to the text area
		scroll=Scrollbar(textPad)
		self.text.configure(yscrollcommand=scroll.set)
		
		#pack everything
		self.text.pack(side=LEFT)
		scroll.pack(side=RIGHT,fill=Y)
		textPad.pack(side=TOP)
		return
def main():
	root = Tk()
	foo=scrollTxtArea(root)
	root.title('TextPad With a Vertical Scroll Bar')
	root.mainloop()
main()


