from turtle import *
from random import randint
speed()
penup()
goto(-140, 140)

for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        backward(160)
        left(90)
        forward(20)

    ruby = Turtle()
    ruby.color("red")
    ruby.shape('turtle')
    ruby.penup()
    ruby.goto(-160,100)
    ruby.pendown()
    for turn in range(10):
        ruby.right(36)

    lily = Turtle()
    lily.color('blue')
    lily.shape('turtle')
    lily.penup()
    lily.goto(-160,70)
    lily.pendown()
    for turn in range(72):
        lily.left(5)

    tooga = Turtle()
    tooga.color('green')
    tooga.shape('turtle')
    tooga.penup()
    tooga.goto(-160,40)
    tooga.pendown()
    for turn in range(60):
        tooga.right(6)

    juju = Turtle()
    juju.color('orange')
    juju.shape('turtle')
    juju.penup()
    juju.goto(-160,10)
    juju.pendown()
    for turn in range(30):
        juju.left(12) 

    for turn in range(100):
        ruby.forward(randint(1,5))
        lily.forward(randint(1,5))
        tooga.forward(randint(1,5))
        juju.forward(randint(1,5))                      