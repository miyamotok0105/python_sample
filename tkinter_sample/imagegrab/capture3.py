import sys
from Tkinter import *
import Tkinter
from PIL import Image, ImageTk 
from PIL import Image, ImageTk, ImageGrab

canvas = Tkinter.Canvas(width=1600, height=1400)
canvas.create_line(0, 0, 1600, 1400, fill="red", width=10)
canvas.pack()
canvas.update()
# get window location
x0 = canvas.winfo_rootx()
y0 = canvas.winfo_rooty()
x1 = x0 + canvas.winfo_reqwidth()
y1 = y0 + canvas.winfo_reqheight()

im = ImageGrab.grab((20,20, x1,y1))
print "X1 : ",x1," Y1: ",y1

im.show()
im.save("1.png", "PNG")

root = Tk()
root.mainloop()
