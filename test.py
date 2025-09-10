import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed('fastest')

def square():
    for i in range(4):
        t.forward(200)
        t.left(90)

square()

for i in range(72):
    square()
    t.left(5)

t.left(2.5)

for i in range(72):
    square()
    t.left(5)

turtle.done()