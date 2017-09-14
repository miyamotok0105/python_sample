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
import platform


class ScrollingArea(object):
    OS = platform.system()
    
    def __init__(self, root, factor = 2):
        
        self.activeArea = None
        
        if type(factor) == int:
            self.factor = factor
        else:
            raise Exception("Factor must be an integer.")

        if self.OS == "Linux" :
            root.bind_all('<4>', self.onMouseWheel,  add='+')
            root.bind_all('<5>', self.onMouseWheel,  add='+')
        else:
            # Windows and MacOS
            root.bind_all("<MouseWheel>", self.onMouseWheel,  add='+')

    def onMouseWheel(self,event):
        if self.activeArea:
            self.activeArea.onMouseWheel(event)

    def mouseWheel_bind(self, widget):
        self.activeArea = widget

    def mouseWheel_unbind(self):
        self.activeArea = None

    def build_function_onMouseWheel(self, widget, orient, factor = 1):
        view_command = getattr(widget, orient+'view')
        
        if self.OS == 'Linux':
            def onMouseWheel(event):
                if event.num == 4:
                    view_command("scroll",(-1)*factor,"units" )
                elif event.num == 5:
                    view_command("scroll",factor,"units" ) 
                
        elif self.OS == 'Windows':
            def onMouseWheel(event):        
                view_command("scroll",(-1)*int((event.delta/120)*factor),"units" ) 
        
        elif self.OS == 'Darwin':
            def onMouseWheel(event):        
                view_command("scroll",event.delta,"units" )             
        
        return onMouseWheel
        

    def add_scrolling(self, scrollingArea, xscrollbar=None, yscrollbar=None):
        if yscrollbar:
            scrollingArea.configure(xscrollcommand=xScrollbar.set)
            yscrollbar['command']=scrollingArea.yview

        if xscrollbar:
            scrollingArea.configure(yscrollcommand=yScrollbar.set)
            xscrollbar['command']=scrollingArea.xview
        
        scrollingArea.bind('<Enter>',lambda event: self.mouseWheel_bind(scrollingArea))
        scrollingArea.bind('<Leave>', lambda event: self.mouseWheel_unbind())

        if xscrollbar and not hasattr(xscrollbar, 'onMouseWheel'):
            xscrollbar.onMouseWheel = self.build_function_onMouseWheel(scrollingArea,'x', self.factor)

        if yscrollbar and not hasattr(yscrollbar, 'onMouseWheel'):
            yscrollbar.onMouseWheel = self.build_function_onMouseWheel(scrollingArea,'y', self.factor)

        main_scrollbar = yscrollbar or xscrollbar
        
        if main_scrollbar:
            scrollingArea.onMouseWheel = main_scrollbar.onMouseWheel

        for scrollbar in (xscrollbar, yscrollbar):
            if scrollbar:
                scrollbar.bind('<Enter>', lambda event, scrollbar=scrollbar: self.mouseWheel_bind(scrollbar) )
                scrollbar.bind('<Leave>', lambda event: self.mouseWheel_unbind())

if __name__== '__main__':
    root = tk.Tk()

    xScrollbar = ttk.Scrollbar(root, orient=tk.HORIZONTAL)
    xScrollbar.grid(row=1, column=0, sticky= "ew")

    yScrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL)
    yScrollbar.grid(row=0, column=1,sticky="ns")

    canvas1 = tk.Canvas(root, width=300, height=100, highlightthickness=0)
    
    canvas1.grid(row=0, column=0, sticky=tk.NSEW)
    
    frameWindows= tk.Frame(canvas1)
    frameWindows.pack()

    for i in range(20):
        rowFrame = tk.Frame(frameWindows)
        rowFrame.pack()
        for j in range(8):
            tk.Label(rowFrame, text="Label %s, %s" % (str(i), str(j))).pack(side=tk.LEFT)

    canvas1.create_window(0, 0, window=frameWindows, anchor='nw')

    canvas1.update_idletasks()

    canvas1['scrollregion'] = (0,0,frameWindows.winfo_reqwidth(), frameWindows.winfo_reqheight())
    
    ScrollingArea(root).add_scrolling(canvas1, xscrollbar=xScrollbar, yscrollbar=yScrollbar)

    root.mainloop()


