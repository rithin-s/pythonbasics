import turtle

mario = turtle.Turtle()
mario.shape("turtle")
mario.shapesize(1.5)
mario.color("red")
mario.penup()
mario.setpos(-450,-200)

def jump():
    mario.left(90)
    mario.forward(100)
    mario.right(90)

def mini_jump():
    mario.left(90)
    mario.forward(20)
    mario.right(90)

def front():
    mario.forward(20)

def back():
    mario.backward(20)

def controls1():
    screen1.onkeypress(jump,"space")
    screen1.onkeypress(back,"Left")
    screen1.onkeypress(front,"Right")
    screen1.onkeypress(mini_jump,"Up")

screen1 = turtle.Screen()
screen1.listen()
screen1.setup(1000,792,250,0)

maker1 = turtle.Turtle()
maker1.hideturtle()
maker1.pencolor("green")
maker1.speed("fastest")
maker1.penup()
maker1.goto(-500,-200)

def screen1obstacles():
    maker1.pendown()
    maker1.goto(-400,-200)
    maker1.goto(-400,-100)
    maker1.goto(-350,-100)
    maker1.goto(-350,-200)
    maker1.goto(-250,-200)
    maker1.goto(-250,-50)
    maker1.goto(-200,-50)
    maker1.goto(-200,-200)
    maker1.goto(0,-200)
    maker1.goto(0,-50)
    maker1.goto(70,-50)
    maker1.goto(70,-200)
    maker1.goto(200,-200)
    maker1.goto(200,-180)
    maker1.goto(260,-180)
    maker1.goto(260,-160)
    maker1.goto(320,-160)
    maker1.goto(320,-140)
    maker1.goto(380,-140)
    maker1.goto(380,-120)
    maker1.goto(440,-120)
    maker1.goto(440,-100)
    maker1.goto(500,-100)


controls1()
screen1obstacles()

screen2 = turtle.Screen()

maker2 = turtle.Turtle()
maker2.color("black")
maker2.speed("fastest")
maker2.penup()
maker2.hideturtle()
maker2.goto(-400,-200)


def screen2obstacles():
    maker2.pendown()
    maker2.goto(-400,-200)


if mario.xcor() >= 400:
    screen2obstacles()



screen3 = turtle.Screen()
screen4 = turtle.Screen()


turtle.done()

