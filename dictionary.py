from tkinter import *
import sys
import re
import time
st = time.monotonic()
win = Tk()
win.title('Phan tich cam xuc')
#function
def inputFile():
   
      


#create Labels
Label(win, text = "Put some words here:").grid(row = 1, column = 0, sticky = W)
#create Buttons
Button(win, text = 'Submit', command = inputFile, width = 6).grid(row = 3, column = 0, sticky = W)
Button(win, text = "Quit", command = win.quit).grid(row = 12, column = 0,padx = 5, pady = 5, sticky = W)
#create entry boxes
textentry = Entry(win, width = 80, bg = 'white')
textentry.grid(row = 2, column = 0, sticky = W)


#create text boxes
text1 = Text(win, width = 60, height = 2, wrap = WORD, background = "white")
text1.grid(row = 5, column = 0, columnspan = 2, sticky = W)

text2 = Text(win, width = 60, height = 2, wrap = WORD, background = "white")
text2.grid(row = 7, column = 0, columnspan = 2, sticky = W)

text3 = Text(win, width = 60, height = 2, wrap = WORD, background = "white")
text3.grid(row = 9, column = 0, columnspan = 2, sticky = W)

win.mainloop()