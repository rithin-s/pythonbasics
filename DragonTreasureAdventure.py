import turtle
import random
TotalScore =0

#setting the screen
Rithin = turtle.Screen()
Rithin.title("                                                                                DragonTreasureHunter")
Rithin.setup(width=700, height=700)
Rithin.listen()

#making the turtles
player = turtle.Turtle()
Treasure = turtle.Turtle()
Dragon1 = turtle.Turtle()
Dragon2 = turtle.Turtle()
Dragon3 = turtle.Turtle()
LevelTracker = turtle.Turtle()

player.shape("turtle")
player.color("green")
player.shapesize(1)
player.penup()

Treasure.shape("square")
Treasure.color("yellow")
Treasure.penup()
Treasure.hideturtle()
treasure_found = False

Dragon1.shape("square")
Dragon1.color("red")
Dragon1.penup()
dragon_awake = False

Dragon2.shape("classic")
Dragon2.shapesize(2)
Dragon2.color("red")
Dragon2.penup()

Dragon3.shape("triangle")
Dragon3.color("red")
Dragon3.penup()

LevelTracker.color("blue")
LevelTracker.shape("square")
LevelTracker.penup()
LevelTracker.hideturtle()
LevelTracker.goto(-325, 325)

#setting the starting screen
def starting_screen():
    Rithin.bgcolor("white")
    player.hideturtle()
    Treasure.hideturtle()
    Dragon1.hideturtle()
    Dragon2.hideturtle()
    Dragon3.hideturtle()
    player.pencolor("black")
    player.goto(-345, 250)
    player.write("Controls: Up arrow - up",font = 5)
    player.forward(55)
    player.right(90)
    player.forward(20)
    player.write("Down arrow - down",font = 5)
    player.forward(20)
    player.write("Left arrow - left",font = 5)
    player.forward(20)
    player.write("Right arrow - right",font = 5)
    player.forward(20)
    player.write("Q - restart",font = 5)
    player.forward(20)
    player.write("M - drawing",font = 5)
    player.forward(20)
    player.write("N - no drawing",font = 5)
    player.forward(20)
    player.write("1 - pause",font = 5)
    player.forward(20)
    player.write("2 - resume",font = 5)
    player.forward(20)
    player.write("0 - exit",font = 5)
    player.goto(-100,250)
    player.write("Rules:",font = 5)
    player.forward(30)
    player.write("1.Do not go next to the red.They are dragons and will eat you.",font = 5)
    player.forward(20)
    player.write("2.Find the hidden treasure on the screen.",font = 5)
    player.forward(20)
    player.write("3.Use the controls to move around.",font = 5)
    player.forward(20)
    player.write("4.Each Treasure gives 10 points.",font = 5)
    player.forward(20)
    player.write("5.After finding 1 Treasure, restart.",font = 5)
    player.goto(-100,-100)
    player.write("If you get -50 points, you lose the game.",font = 5)
    player.forward(20)
    player.write("Get 100 points to win!",font = 5)
    player.forward(20)
    player.write("Press Q to start",font = 5)
    player.left(90)

#setting the positions of the turtles
def position():
    a = random.randint(-250, 250)
    b = random.randint(-250, 250)
    Dragon1.goto(a, b)
    c = random.randint(-250, 250)
    d = random.randint(-250, 250)
    Dragon2.goto(c, d)
    e = random.randint(-250, 250)
    f = random.randint(-250, 250)
    Dragon3.goto(e, f)
    g = random.randint(-250, 250)
    h = random.randint(-250, 250)
    player.goto(g, h)
    i = random.randint(-250, 250)
    j = random.randint(-250, 250)
    Treasure.goto(i, j)

#the score
score = 0

#check if we are eaten by the dragon 1
def eaten1():
    global TotalScore, score
    if player.distance(Dragon1) < 50:
        player.hideturtle()
        Dragon2.hideturtle()
        Dragon3.hideturtle()
        Rithin.bgcolor("red")
        Dragon1.goto(0, 0)
        Dragon1.pencolor("black")
        Dragon1.write("You were eaten by Dragon1.",font = 5)
        Dragon1.goto(0, 50)
        score = TotalScore - 10
        LevelTracker.clear()
        LevelTracker.write(score,font = 5)
        TotalScore = score
        Treasure.showturtle()
        #we lose if our score is -50
        if TotalScore == -50:
            player.hideturtle()
            Dragon1.hideturtle()
            Dragon2.hideturtle()
            Rithin.bgcolor("red")
            Dragon3.goto(0, -30)
            Dragon3.pencolor("black")
            Dragon3.write("Your score is too low. You have lost the game.", font=5)
            Dragon3.goto(0, 50)
            stop_controls2()

#check if we are eaten bt the dragon 2
def eaten2():
    global TotalScore, score
    if player.distance(Dragon2) < 50:
        player.hideturtle()
        Dragon1.hideturtle()
        Dragon3.hideturtle()
        Rithin.bgcolor("red")
        Dragon2.goto(0, 0)
        Dragon2.pencolor("black")
        Dragon2.write("You were eaten by Dragon2.",font = 5)
        Dragon2.goto(0, 50)
        score = TotalScore - 10
        LevelTracker.clear()
        LevelTracker.write(score, font = 5)
        TotalScore = score
        Treasure.showturtle()
        #we lose if our score is -50
        if TotalScore == -50:
            player.hideturtle()
            Dragon1.hideturtle()
            Dragon2.hideturtle()
            Rithin.bgcolor("red")
            Dragon3.goto(0, -30)
            Dragon3.pencolor("black")
            Dragon3.write("Your score is too low. You have lost the game.", font=5)
            Dragon3.goto(0, 50)
            stop_controls2()

#check if we are eaten by the dragon 3
def eaten3():
    global TotalScore
    if player.distance(Dragon3) < 50:
        player.hideturtle()
        Dragon1.hideturtle()
        Dragon2.hideturtle()
        Rithin.bgcolor("red")
        Dragon3.goto(0, 0)
        Dragon3.pencolor("black")
        Dragon3.write("You were eaten by Dragon3.",font = 5)
        Dragon3.goto(0, 50)
        score = TotalScore - 10
        LevelTracker.clear()
        LevelTracker.write(score, font = 5)
        TotalScore = score
        Treasure.showturtle()
        # we lose if our score is -50
        if TotalScore == -50 :
            player.hideturtle()
            Dragon1.hideturtle()
            Dragon2.hideturtle()
            Rithin.bgcolor("red")
            Dragon3.goto(0, -30)
            Dragon3.pencolor("black")
            Dragon3.write("Your score is too low. You have lost the game.",font = 5)
            Dragon3.goto(0, 50)
            stop_controls2()

#check if we found the treasure
def won():
    global TotalScore, score
    if player.distance(Treasure) < 50:
        player.hideturtle()
        Dragon1.hideturtle()
        Dragon2.hideturtle()
        Dragon3.hideturtle()
        Treasure.showturtle()
        Treasure.goto(0, 0)
        Rithin.bgcolor("yellow")
        Treasure.pencolor("black")
        Treasure.write("You won and got the Treasure !!!",font = 5)
        Treasure.goto(0, 50)
        score = TotalScore +  10
        LevelTracker.clear()
        LevelTracker.write(score, font = 5)
        TotalScore = score
    #we win the game if the score is 100
    if TotalScore == 100:
        player.hideturtle()
        Dragon1.hideturtle()
        Dragon2.hideturtle()
        Dragon3.hideturtle()
        Treasure.showturtle()
        Treasure.goto(0, -50)
        Rithin.bgcolor("yellow")
        Treasure.pencolor("black")
        Treasure.write("You got all of the Treasures. You win!!!",font = 5)
        Treasure.goto(0, 50)
        stop_controls2()

#to pause the game
def pause():
    player.pencolor("green")
    player.write("The game is paused")
    stop_controls1()

#to resume if we have paused the game
def resume():
    player.clear()
    controls()

#to restart if we found the treasure or eaten by the dragon
def restart():
    player.clear()
    Treasure.clear()
    Dragon1.clear()
    Dragon2.clear()
    Dragon3.clear()
    Dragon1.showturtle()
    Dragon2.showturtle()
    Dragon3.showturtle()
    player.showturtle()
    Treasure.hideturtle()
    Rithin.bgcolor("black")
    position()
    controls()
    player.pencolor("green")


y = player.ycor()
x = player.xcor()
#wrap
def wrap():
    global x, y
    if player.xcor() > 325:
        player.goto(-325, y)
    if player.xcor() < -325:
        player.goto(325, y)
    if player.ycor() > 325:
        player.goto(x, -325)
    if player.ycor() < -325:
        player.goto(x, 325)

#controls
def move_down():
    global x, y
    x = player.xcor()
    y = player.ycor()
    player.sety(y - 20)
    eaten1()
    eaten2()
    eaten3()
    won()
    wrap()


def move_left():
    global x, y
    x = player.xcor()
    y = player.ycor()
    player.backward(30)
    eaten1()
    eaten2()
    eaten3()
    won()
    wrap()


def move_right():
    global x, y
    x = player.xcor()
    y = player.ycor()
    player.forward(30)
    eaten1()
    eaten2()
    eaten3()
    won()
    wrap()


def move_up():
    global x, y
    x = player.xcor()
    y = player.ycor()
    player.sety(y + 20)
    eaten1()
    eaten2()
    eaten3()
    won()
    wrap()

#to stop drawing
def penup():
    player.penup()

#to draw
def pendown():
    player.pendown()

#to clear the player's drawing
def clear():
    player.clear()

#to  exit the game screen
def exit():
    Rithin.bye()

#to stop the controls(needed for pause)
def stop_controls1():
    Rithin.onkey(None, "Down")
    Rithin.onkey(None, "Left")
    Rithin.onkey(None, "Right")
    Rithin.onkey(None, "Up")
    Rithin.onkey(None, "n")
    Rithin.onkey(None, "m")

#to stop ALL the controls(if our score is too low)
def stop_controls2():
    Rithin.onkey(None, "Down")
    Rithin.onkey(None, "Left")
    Rithin.onkey(None, "Right")
    Rithin.onkey(None, "Up")
    Rithin.onkey(None, "n")
    Rithin.onkey(None, "m")
    Rithin.onkey(None, "1")
    Rithin.onkey(None, "2")
    Rithin.onkey(None, "q")

#the controls
def controls():
    Rithin.onkeypress(move_down, "Down")
    Rithin.onkeypress(move_left, "Left")
    Rithin.onkeypress(move_right, "Right")
    Rithin.onkeypress(move_up, "Up")
    Rithin.onkeyrelease(penup, "n")
    Rithin.onkeyrelease(pendown, "m")
    Rithin.onkeyrelease(pause, "1")
    Rithin.onkeyrelease(resume, "2")
    Rithin.onkeyrelease(clear,"a")

def main():
    Rithin.onkeyrelease(restart, "q")
    Rithin.onkeyrelease(exit, "0")
    starting_screen()
    Rithin.exitonclick()

if __name__ == "__main__":
    main()