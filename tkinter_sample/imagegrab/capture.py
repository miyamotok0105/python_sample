from tkinter import *
from PIL import ImageGrab
root = Tk()
cv = Canvas(root)

cv.pack()

cv.create_rectangle(10,10,50,50)
#cv.create_line([0, 10, 10, 10], fill='green')

cv.update()
#print(root.winfo_width())

def getter(widget):
    x=root.winfo_rootx()+widget.winfo_x()
    print(x)
    y=root.winfo_rooty()+widget.winfo_y()
    print(y)
    x1=x+widget.winfo_width()
    print(x1)
    y1=y+widget.winfo_height()
    print(y1)
    ImageGrab.grab().crop((x,y,x1,y1)).save("em.jpg")

getter(cv)
root.mainloop()
