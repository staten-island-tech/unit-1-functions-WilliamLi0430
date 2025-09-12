import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed('fastest')

def star(x):
    for i in range(5):
        t.forward(x)
        t.left(144)

def doubleSquares(length): 
    length = 5 
    for i in range(60):
        star(length)
        length += 5
        t.right(5)
doubleSquares(5)

turtle.done()