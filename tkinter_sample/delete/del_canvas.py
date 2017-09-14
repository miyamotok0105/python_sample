from Tkinter import *

class PokerGame(object):
    def __init__(self):
        self.run()

    def run(self):
        self.root = Tk()
        self.root.title("PyPoker")
        self.root.geometry("1280x720")
        #self.width = 1280
        #self.height = 720
        #self.canvas = Canvas(self.root, width = self.width, height = self.height)
        #self.canvas.pack()

        self.drawStartScreen()
        self.root.mainloop()

    def drawStartScreen(self): 
        self.bgImage = PhotoImage(file = '../../img/hari.jpeg')

        self.bgLabel = Label(self.root, image = self.bgImage)
        self.bgLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        self.btnPlay = Button(self.root, text = "Play", command = self.playGame)
        self.btnPlay.place(relheight = 0.1, relwidth = 0.1, relx = 0.5, rely = 0.4, anchor = CENTER)

        self.btnInstructions = Button(self.root, text = "How To Play", command = self.showInstructions)
        self.btnInstructions.place(relheight = 0.1, relwidth = 0.1, relx = 0.5, rely = 0.5, anchor = CENTER)

    def playGame(self):
        self.redrawAll()

    def showInstructions(self):
        self.redrawAll()

    def redrawAll(self):
        print "trying to delete all"
        self.btnPlay.place_forget()
        self.btnInstructions.place_forget()
        self.bgLabel.place_forget()

PokerGame()
