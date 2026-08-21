import turtle
rithin = turtle.Turtle()
turtle.screensize(1000,1000)
turtle.Screen().bgcolor("black")
rithin.color("yellow")
rithin.shape("turtle")
rithin.speed(50)
rithin.hideturtle()
def Sun():
    rithin.dot(100,"red")
def Mercury():
    rithin.pendown()
    rithin.circle(100)
    rithin.dot(30,"grey")
def Venus():
    rithin.penup()
    rithin.circle(150,203)
    rithin.pendown()
    rithin.circle(150)
    rithin.dot(35,"orange")
def Earth():
    rithin.penup()
    rithin.circle(200,192)
    rithin.pendown()
    rithin.circle(200)
    rithin.dot(40,"blue")
def Mars():
    rithin.penup()
    rithin.circle(250,122)
    rithin.pendown()
    rithin.circle(250)
    rithin.dot(45,"red")
def Jupiter():
    rithin.penup()
    rithin.circle(300,203)
    rithin.pendown()
    rithin.circle(300)
    rithin.dot(60,"orange")
def Saturn():
    rithin.penup()
    rithin.circle(350,195)
    rithin.pendown()
    rithin.circle(350)
    rithin.dot(50,"orange")
    rithin.penup()
    rithin.forward(55)
    rithin.left(90)
    rithin.color("orange")
    rithin.pendown()
    rithin.circle(50)
    rithin.left(270)
    rithin.penup()
    rithin.back(55)
    rithin.pendown()
    rithin.color("black")
def Uranus():
    rithin.penup()
    rithin.circle(400,123)
    rithin.pendown()
    rithin.circle(400)
    rithin.dot(50,"blue")
def Neptune():
    rithin.penup()
    rithin.circle(450,123)
    rithin.pendown()
    rithin.circle(450)
    rithin.dot(45,"blue")

def distance_of_planets():
    rithin.penup()
    rithin.right(90)
    rithin.forward(100)
    rithin.left(90)


Sun()
distance_of_planets()

Mercury()
distance_of_planets()

Venus()
distance_of_planets()

Earth()
distance_of_planets()

Mars()
distance_of_planets()

Jupiter()
distance_of_planets()

Saturn()
distance_of_planets()

Uranus()
distance_of_planets()

Neptune()
rithin.color("blue")

turtle.Screen().exitonclick()
