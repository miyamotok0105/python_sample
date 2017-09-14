# random circles in Tkinter
# a left mouse double click will idle action for 5 seconds
# modified vegaseat's code from:
# http://www.daniweb.com/software-development/python/code/216626
import random as rn
import time
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
def idle_5sec(event=None):
    """freeze the action for 5 seconds"""
    root.title("Idle for 5 seconds")
    time.sleep(5)
    root.title("Happy Circles ...")
# create the window form
root = tk.Tk()
# window title text
root.title("Happy Circles (click on window to idle for 5 seconds)")
# set width and height
w = 640
h = 480
# create the canvas for drawing
cv = tk.Canvas(width=w, height=h, bg='black')
cv.pack()
# endless loop to draw the random circles
while True:
    # random center (x,y) and radius r
    x = rn.randint(0, w)
    y = rn.randint(0, h)
    r = rn.randint(5, 50)
    # pick a random color
    # Tkinter color format is "#rrggbb"
    color = '#' + "".join("%02x"%rn.randrange(256) for x in range(3))
    # now draw the circle
    cv.create_oval(x, y, x+r, y+r, fill=color)
    # update the window
    root.update()
    # bind left mouse double click, idle for 5 seconds
    cv.bind('<Double-1>', idle_5sec)
# start the program's event loop
root.mainloop()
