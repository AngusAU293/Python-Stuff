
from tkinter import *
from turtle import *
def resetGraphics():
    reset()
def drawSquare():
    reset()
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
def drawTree():
    reset()
    penup()
    forward(-600)
    pendown()
    forward(900)
    penup()
    forward(-400)
    left(90)
    pendown()
    forward(100)
    right(90)
    forward(300)
    penup()
    left(180)
    forward(300)
    pendown()
    forward(300)
    penup()
    left(180)
    forward(300)
    left(90)
    pendown()
    forward(100)
    right(90)
    forward(200)
    penup()
    left(180)
    forward(200)
    pendown()
    forward(200)
    penup()
    right(180)
    forward(200)
    left(90)
    pendown()
    forward(100)
    right(90)
    forward(100)
    penup()
    left(180)
    forward(100)
    pendown()
    forward(100)
window = Tk()
drawTreeButton = Button(window, text='Draw a Tree', command=drawTree)
drawSquareButton = Button(window, text='Draw a Square', command=drawSquare)
resetButton = Button(window, text='Reset', command=resetGraphics)
resetButton.pack()
drawSquareButton.pack()
drawTreeButton.pack()
