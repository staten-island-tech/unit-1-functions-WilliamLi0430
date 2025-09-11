import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed('fastest')

def square(x, y):
    for i in range(4):
        t.forward(200)
        t.left(90)

def doubleSquares(iRange): 
    length = 25 
    for i in range(iRange): 
        square(length, 90) 
        length = length * 2 
doubleSquares(5)

turtle.done()