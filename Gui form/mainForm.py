#-*- coding : utf8 -*-
# /usr/bin/env python
from tkinter import *

class mainFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()
 
    def createWidgets(self):
        self.displayText = Label(self, text = "something happened")
        self.displayText.pack()

if __name__ == '__main__':
    root = Tk()
    app = mainFrame(root)
    app.mainloop()
	

