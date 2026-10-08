import turtle
import random

#setting the screen
screen = turtle.Screen()
screen.title("                                                                                   Star Catcher")
screen.setup(width=700, height=700)
screen.listen()

#setting the turtle for player
player = turtle.Turtle()
player.hideturtle()
player.shape("square")
player.shapesize(stretch_wid=1, stretch_len=4)
player.color("green")
player.penup()
player.goto(0, -250)

#setting the star to catch
star = turtle.Turtle()
star.hideturtle()
star.shape("turtle")
star.color("gold")
star.penup()
star.goto(random.randint(-280, 280), 200)
star.right(90)

#score display
score_d = turtle.Turtle()
score_d.hideturtle()
score_d.color("blue")
score_d.penup()
score_d.goto(0, 250)
score_d.pendown()

#lives display
lives_d = turtle.Turtle()
lives_d.hideturtle()
lives_d.shape("triangle")
lives_d.color("blue")
lives_d.penup()
lives_d.goto(0, 210)
lives_d.pendown()

#setting up the variables
lives = 3
score = 0
star_speed = 5
game = True


def starting_screen():
    #displays the controls and rules
    screen.bgcolor("white")
    star.hideturtle()
    player.hideturtle()
    star.pencolor("black")
    star.goto(-300, 300)
    star.write("Controls :", font=5)
    star.forward(20)
    star.write("1.Move right - Right arrow / D", font=5)
    star.forward(20)
    star.write("2.Move left - Left arrow / A", font=5)
    star.forward(20)
    star.write("3.Pause - 1", font=5)
    star.forward(20)
    star.write("4.Resume - 2", font=5)
    star.forward(20)
    star.write("5.Restart - 3", font=5)
    star.goto(10, 300)
    star.write("Rules:", font=5)
    star.forward(20)
    star.write("1.Catch the golden turtle", font=5)
    star.forward(20)
    star.write("2.You have 3 lives", font=5)
    star.forward(20)
    star.write("3.If you miss, you lose 1 life", font=5)
    star.goto(20, 200)
    star.write("Press 0 to start", font=5)
    controls()


def start():
    #start the game
    global left, right
    star.clear()
    screen.bgcolor("black")
    star.showturtle()
    player.showturtle()
    game_loop()
    controls()
    left = True
    right = True


def lost():
    #check if we lost the game
    if lives == 0:
        star.hideturtle()
        pause()
        screen.bgcolor("red")
        star.goto(0, 0)
        star.pencolor("black")
        star.write("You Lost All Your Lives", font=("Arial", 20, "bold"))
        stop_controls()


def check_catch():
    #check if we caught or missed the star
    global score, lives
    speed_increase()
    lives_d.write("Lives = " + str(lives), font=("Arial", 24, "bold"))
    score_d.write("Score = " + str(score), font=("Arial", 24, "bold"))
    #check if we caught the star
    if star.distance(player) <= 50:
        score = score + 10
        score_d.clear()
        score_d.write("Score = " + str(score), font=("Arial", 24, "bold"))
        star.setposition(random.randint(-280, 280), 200)
    #check if we missed the star
    if star.ycor() < -300:
        lives = lives - 1
        lives_d.clear()
        screen.bgcolor("red")
        screen.bgcolor("black")
        lives_d.write("Lives = " + str(lives), font=("Arial", 24, "bold"))
        star.setposition(random.randint(-280, 280), 200)

def speed_increase():
    #to increase the speed of the star every time the score is a multiple of 20
    global star_speed, score
    if score % 20 == 0:
        star_speed = star_speed + 10


def game_loop():
    #to make the star come down
    global game, star_speed
    speed_increase()
    if game:
        while game:
            star.speed(star_speed)
            star.forward(10)
            lost()
            if check_catch():
                star.goto(random.randint(-280, 280), 200)
                break
    else:
        game = False

left = True
right = True


def move_left():
    #to move left
    if left:
        player.backward(20)
    #wrap
    if player.xcor() < -290:
        player.goto(280, -250)
        check_catch()
        speed_increase()


def move_right():
    #to move right
    if right:
        player.forward(20)
    #wrap
    if player.xcor() > 290:
        player.goto(-280, -250)
        check_catch()
        speed_increase()


def pause():
    #to pause the game
    global game, left, right
    game = False
    left = False
    right = False
    star.pencolor("red")
    star.write("game pause")
    stop_controls()


def resume():
    #to resume the game
    global game
    game = True
    controls()
    game_loop()
    star.pencolor("black")
    star.clear()


def controls():
    #the controls of the game
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")
    screen.onkey(start, "0")
    screen.onkey(pause, "1")
    screen.onkey(resume, "2")
    screen.onkey(restart, "3")


def stop_controls():
    #to stop the controls(needed for pause)
    screen.onkey(None, "Left" or "a")
    screen.onkey(None, "Right" or "d")
    screen.onkey(None, "0")
    screen.onkey(None, "1")
    screen.onkey(resume, "2")
    screen.onkey(restart, "3")


def restart():
    # to restart the game if we lost all lives
    global score, lives, star_speed
    score = 0
    lives = 3
    star_speed = 3
    player.clear()
    lives_d.clear()
    score_d.clear()
    player.goto(0, -250)
    start()
    check_catch()
    game_loop()
    controls()
    resume()


def main():
    starting_screen()
    turtle.done()


if __name__ == "__main__":
    main()
    
