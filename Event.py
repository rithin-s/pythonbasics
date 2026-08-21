import turtle
rithin = turtle.Turtle()
Rithin = turtle.Screen()
Rithin.listen()
def move_up():
    rithin.left(90)
    rithin.forward(50)
    rithin.right(90)
def move_down():
    rithin.right(90)
    rithin.forward(50)
    rithin.left(90)
def move_left():
    rithin.backward(50)
def move_right():
    rithin.forward(50)
Rithin.onkey(move_up,"Up")
Rithin.onkey(move_down,"Down")
Rithin.onkey(move_left,"Left")
Rithin.onkey(move_right,"Right")
Rithin.exitonclick()