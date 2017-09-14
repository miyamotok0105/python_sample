# USAGE
# tkinter_test.py

# import the necessary packages
import cv2
import math
import numpy as np
import tkFileDialog
from Tkinter import *
from PIL import Image
from PIL import ImageTk

size = (400, 400)

init = True

def select_image():
	# grab a reference to the image panels
	global panelA, panelB, path
	global init

	if init == True:
		path = tkFileDialog.askopenfilename()
		init = False

	# ensure a file path was selected
	if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(path)
		image = cv2.resize(image, (size[0], size[1]))
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		edged = cv2.Canny(gray, 50, 100)

		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		#------------------------------------------------------
		minLineLength=100
		lines= cv2.HoughLines(edged, 100, math.pi/180.0, 200, np.array([]), 0, 0)
		# lines = cv2.HoughLinesP(image=edged,rho=1,theta=math.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)

		# a,b,c = lines.shape
		# for i in range(a):
		#     cv2.line(gray, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)

		a,b,c = lines.shape
		print(len(lines))
		line_len = 600
		for i in range(a):
		    rho = lines[i][0][0]
		    theta = lines[i][0][1]
		    a = math.cos(theta)
		    b = math.sin(theta)
		    x0, y0 = a*rho, b*rho
		    pt1 = ( int(x0+line_len*(-b)), int(y0+line_len*(a)) )
		    pt2 = ( int(x0-line_len*(-b)), int(y0-line_len*(a)) )
		    cv2.line(image, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

		#------------------------------------------------------

		# convert the images to PIL format...
		image = Image.fromarray(image)
		edged = Image.fromarray(edged)

		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		edged = ImageTk.PhotoImage(edged)

		# if the panels are None, initialize them
		if panelA is None or panelB is None:
			# the first panel will store our original image
			panelA = Label(image=image, width=size[0], height=size[1])
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)

			# while the second panel will store the edge map
			panelB = Label(image=edged, width=size[0], height=size[1])
			panelB.image = edged
			panelB.pack(side="right", padx=10, pady=10)

		# otherwise, update the image panels
		else:
			# update the pannels
			panelA.configure(image=image, width=size[0], height=size[1])
			panelB.configure(image=edged, width=size[0], height=size[1])
			panelA.image = image
			panelB.image = edged

		
# def test_image():
# 	# grab a reference to the image panels
# 	global panelA, panelB


# 	# ensure a file path was selected
# 	if len(path) > 0:
# 		# load the image from disk, convert it to grayscale, and detect
# 		# edges in it
# 		image = cv2.imread(path)
# 		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 		edged = cv2.Canny(gray, var1.get(), var2.get())

# 		# OpenCV represents images in BGR order; however PIL represents
# 		# images in RGB order, so we need to swap the channels
# 		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 		#------------------------------------------------------
# 		minLineLength=100
# 		lines= cv2.HoughLines(edged, 100, math.pi/180.0, 200, np.array([]), 0, 0)
# 		# lines = cv2.HoughLinesP(image=edged,rho=1,theta=math.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)

# 		# a,b,c = lines.shape
# 		# for i in range(a):
# 		#     cv2.line(gray, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)

# 		a,b,c = lines.shape
# 		print(len(lines))
# 		line_len = 600
# 		for i in range(a):
# 		    rho = lines[i][0][0]
# 		    theta = lines[i][0][1]
# 		    a = math.cos(theta)
# 		    b = math.sin(theta)
# 		    x0, y0 = a*rho, b*rho
# 		    pt1 = ( int(x0+line_len*(-b)), int(y0+line_len*(a)) )
# 		    pt2 = ( int(x0-line_len*(-b)), int(y0-line_len*(a)) )
# 		    cv2.line(image, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)
		
# 		#------------------------------------------------------

# 		# convert the images to PIL format...
# 		image = Image.fromarray(image)
# 		edged = Image.fromarray(edged)

# 		# ...and then to ImageTk format
# 		image = ImageTk.PhotoImage(image)
# 		edged = ImageTk.PhotoImage(edged)

# 		# if the panels are None, initialize them
# 		if panelA is None or panelB is None:
# 			# the first panel will store our original image
# 			panelA = Label(image=image, width=size[0], height=size[1])
# 			panelA.image = image
# 			panelA.pack(side="left", padx=10, pady=10)

# 			# while the second panel will store the edge map
# 			panelB = Label(image=edged, width=size[0], height=size[1])
# 			panelB.image = edged
# 			panelB.pack(side="right", padx=10, pady=10)

# 		# otherwise, update the image panels
# 		else:
# 			# update the pannels
# 			panelA.configure(image=image, width=size[0], height=size[1])
# 			panelB.configure(image=edged, width=size[0], height=size[1])
# 			panelA.image = image
# 			panelB.image = edged





# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None

def sel():
   selection = "Value = " + str(var1.get())
   label.config(text = selection)


btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

#canny
label1 = Label(root)
label1.config(text = "Canny:")
label1.pack(side="left")

var1 = DoubleVar()
scale = Scale(root,  variable = var1, from_=0, to=1500)
scale.pack(side="left")

var2 = DoubleVar()
scale = Scale(root,  variable = var2, from_=0, to=1500)
scale.pack(side="left")

#HoughLinesP


button = Button(root, text="change", command=select_image)
button.pack(side="left")

label = Label(root)
label.pack()

# kick off the GUI
root.mainloop()

