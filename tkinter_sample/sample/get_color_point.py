from tkinter import *
from PIL import ImageTk, Image
import os
import numpy as np

img = Image.open("1.jpg")
scale = 0.4
h = int(img.size[0] * scale)
w = int(img.size[1] * scale)
img = img.resize((h, w))
img_array = np.asarray(img)

from tkinter import *

root = Tk()  # create a window

frame = Frame(root)  # define upper frame
middleframe = Frame(root)  # define middle frame
exitFrame = Frame(root)  # define exit frame
frame.pack()  # pack the frame
middleframe.pack()  # pack the subframe
exitFrame.pack(side='bottom')  # pack the exit frame

# function that closes the GUI
def close_window():
    root.destroy()

# img = PhotoImage(file="myimage.png")  # load the image
# img = PhotoImage(img)  # load the image
img = ImageTk.PhotoImage(img)
canvas = Canvas(frame, width=img.width(), height=img.height(), borderwidth=0)
canvas.grid(row=0, column=0)
canvas.create_image(0, 0, image=img, anchor=NW)

# make the user select some points
x_Coordinates = []  # list for storing x-axis coordinates
y_Coordinates = []  # list for storing y-axis coordinates
clicks = 0

def create_circle(canvas, x, y, radius, **kwargs):
    return canvas.create_oval(x-radius, y-radius, x+radius, y+radius, **kwargs)

def countClicks():
    global clicks

    clicks += 1
    # if the user has selected 2 points, add a button that closes the window
    if clicks == 2:
        # link the closing function to the button
        exit_button = Button(exitFrame, state="normal", text="Done!",
                             command=close_window)
        exit_button.grid(row=2, column=0, pady=5)  # set button position with "grid"

def selectPoints():  # function called when user clicks the button "select two points"
    # link the function to the left-mouse-click event
    canvas.bind("<Button 1>", saveCoordinates)
    # link closing function to the button
    exit_button = Button (exitFrame, state="disabled", text="Done!",
                          command=close_window)
    exit_button.grid(row=2, column=0, pady=5)  # set button position with "grid"
    button_select_points.config(state="disabled") # switch button state to "disabled"

def saveCoordinates(event): # function called when left-mouse-button is clicked
    x_coordinate = event.x  # save x and y coordinates selected by the user
    y_coordinate = event.y
    print("x:", event.x, " y:", event.y)
    print(img_array.shape)
    print(img_array[event.y-1:event.y, event.x-1:event.x])
    x_Coordinates.append(x_coordinate)
    y_Coordinates.append(y_coordinate)
    # Display a small dot showing position of point.
    create_circle(canvas, x_coordinate, y_coordinate, radius=3, fill='red')
    countClicks()

# insert button and link it to "selectPoints"
button_select_points = Button(middleframe, text="select two points",
                              command=selectPoints)
button_select_points.grid(row=1, column=0, pady=5)

root.mainloop()  # keep the GUI open
