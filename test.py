import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed('fastest')

def square():
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)

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

def circlesquare():
    for i in range(72):
        square()
        t.left(5)
circlesquare()


turtle.done()