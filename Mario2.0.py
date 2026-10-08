import turtle

mario = turtle.Turtle()
mario.shape("turtle")
mario.shapesize(1.5)
mario.color("red")
mario.penup()
mario.hideturtle()

screen1 = turtle.Screen()
screen1.title("                                                                                                                                   Mario 2.0")
screen1.listen()
screen1.setup(1000, 792, 250, 0)
screen1.bgcolor("sky blue")

shift = False
control = False
move_right = True
move_left = True


def shift_true():
    global shift
    shift = True


def shift_false():
    global shift
    shift = False


def control_true():
    global control
    control = True


def control_false():
    global control
    control = False


def jump():
    global control, shift, y
    y = mario.ycor()
    if shift:
        mario.sety(y + 150)

    elif control:
        mario.sety(y + 100)

    else:
        mario.sety(y + 20)
    gravity()
    wall_collision_backward()
    wall_collision_forward()


def start_front():
    global move_right, life, currentscreen
    load_screens()
    wall_collision_forward()
    if move_right:
        mario.forward(10)
        if currentscreen == 2:
            enemy1_loss()
            enemy2_loss()
            enemy3_loss()
            enemy4_loss()
            enemy5_loss()
            enemy6_loss()
        elif currentscreen == 3:
            if mario.distance(run_enemy) > 40:
                pass
            else:
                life = life - 1
                if life == 0:
                    loss_screen()
                else:
                    mario.color("yellow")
                    mario.color("red")
                    mario.setpos(-480, -200)
                    tracker.clear()
                    tracker.goto(0, 300)
                    tracker.write("Lives = " + str(life), font=("Arial", 20, "bold"))
        elif currentscreen == 4:
            flag_hoist()
    else:
        stop_front()


def stop_front():
    mario.forward(0)
    load_screens()
    wall_collision_forward()
    gravity()


def start_back():
    global move_left, life, currentscreen
    wall_collision_backward()
    if move_left:
        mario.back(10)
        if currentscreen == 2:
            enemy1_loss()
            enemy2_loss()
            enemy3_loss()
            enemy4_loss()
            enemy5_loss()
            enemy6_loss()
        elif currentscreen == 3:
            if mario.distance(run_enemy) > 40:
                pass
            else:
                life = life - 1
                if life == 0:
                    loss_screen()
                else:
                    mario.color("yellow")
                    mario.color("red")
                    mario.setpos(-480, -200)
                    tracker.clear()
                    tracker.goto(0, 300)
                    tracker.write("Lives = " + str(life), font=("Arial", 20, "bold"))
        elif currentscreen == 4:
            flag_hoist()
    else:
        stop_back()


def stop_back():
    mario.backward(0)
    load_screens()
    wall_collision_backward()
    gravity()

def bye():
    screen1.bye()

def start():
    mario.goto(-450, -200)
    load_screens()

def controls1():
    screen1.onkeypress(shift_true, "Shift_L")
    screen1.onkeyrelease(shift_false, "Shift_L")
    screen1.onkeypress(control_true, "Control_L")
    screen1.onkeyrelease(control_false, "Control_L")
    screen1.onkeypress(jump, "Up")
    screen1.onkeypress(start_back, "Left")
    screen1.onkeyrelease(stop_back, "Left")
    screen1.onkeypress(start_front, "Right")
    screen1.onkeyrelease(stop_front, "Right")
    screen1.onkeyrelease(bye, "0")
    screen1.onkeyrelease(start, "q")


controls1()

maker1 = turtle.Turtle()
maker1.hideturtle()
maker1.penup()
maker1.pencolor("green")
maker1.speed(0)
maker1.goto(-500, -200)


def wall_collision_backward():
    global move_left, move_right, currentscreen
    try:
        if mario.ycor() < floor:
            if currentscreen == 1 or currentscreen == 3 or currentscreen == 4:
                for a in floor1X:
                    b = floor1X.index(a)
                    if not move_right:
                        move_left = True
                    elif b % 2 == 1 and mario.xcor() == a:
                        move_left = False
                        move_right = True
            elif currentscreen == 2:
                for a in floor2X:
                    if mario.xcor() <= a:
                        move_left = False
        else:
            move_left = True
    except:
        print("Error in finding wall backwards")


def wall_collision_forward():
    global move_right, currentscreen, move_left
    steps = 200
    try:
        if mario.ycor() < floor:
            if currentscreen == 1 or currentscreen == 3 or currentscreen == 4:
                for a in floor1X:
                    b = floor1X.index(a)
                    if mario.xcor() == a and currentscreen == 1:
                        if mario.xcor() >= steps:
                            move_right = False
                            move_left = True
                    elif not move_left:
                        move_right = True
                    elif b % 2:
                        move_left = True
                        move_right = False
            elif currentscreen == 2:
                move_right = True
        else:
            move_right = True
            move_left = True
    except:
        print("Error in finding wall forward")


    #ONE WAY TO DO IT (BUT NEEDS LOOPS)
    #if mario.xcor() >= floor1X[1] and mario.xcor() < floor1X[2]:
    #mario.setx(floor1X[1])
    #if mario.xcor() >= floor1X[1] and mario.xcor() < floor1X[2]:
    #mario.setx(floor1X[2])


floor1X = [-480, -400, -350, -250, -200, 0, 70, 200, 260, 320, 380, 440, 500]
floor1H = [0, 100, 0, 150, 0, 150, 0, 20, 40, 60, 80, 100]

floor2X = [-500, -440, -380, -320, -240, -180, 500]
floor2H = [100, 80, 60, 40, 20, 0]

floor3X = [-500, -400, -340, 350, 410, 500]
floor3H = [0, 100, 0, 100, 0]

floor4X = [-500, -100, 100, 500]
floor4H = [0, 200, 0]

floor = -200
h = 0


def find_floorY():
    global floor1X, floor1H, floor2X, floor2H, floor3X, floor3H,floor4X, floor4H, h, floor, currentscreen
    x = mario.xcor()
    try:
        if currentscreen == 1:
            for coord in floor1X:
                if x >= coord:
                    floor = -200
                    ind = floor1X.index(coord)
                    h = floor1H[ind]
                    floor = floor + h
        elif currentscreen == 2:
            for coord in floor2X:
                if x >= coord:
                    floor = -200
                    ind = floor2X.index(coord)
                    h = floor2H[ind]
                    floor = floor + h
        elif currentscreen == 3:
            for coord in floor3X:
                if x >= coord:
                    floor = -200
                    ind = floor3X.index(coord)
                    h = floor3H[ind]
                    floor = floor + h
        elif currentscreen == 4:
            for coord in floor4X:
                if x >= coord:
                    floor = -200
                    ind = floor4X.index(coord)
                    h = floor4H[ind]
                    floor = floor + h

    except:
        print("error in finding floor")

    #if x >= floor1X[0] and x <= floor1X[1]:ONE WAY TO DO IT(BUT USE LOOPS)
    #h = floor1H[1]
    #y = y - h
    #return y


def gravity():
    try:
        find_floorY()
        global floor, currentscreen
        while mario.ycor() > floor:
            y = mario.ycor()
            mario.sety(y - 1)

    except:
        print("error in gravity function")

life = 3

def loss_screen():
    global life, currentscreen, move_left, move_right
    if life == 0:
        enemy1.hideturtle()
        enemy2.hideturtle()
        enemy3.hideturtle()
        enemy4.hideturtle()
        enemy5.hideturtle()
        enemy6.hideturtle()
        maker1.clear()
        screen1.bgcolor("black")
        mario.goto(0, 0)
        move_left = False
        move_right = False
        currentscreen = 1
        tracker.clear()
        tracker.goto(-200, 300)
        tracker.pencolor("red")
        tracker.write("You have lost all your lives", font= ("Arial", 20, "bold"))

def controls_screen():
    maker1.clear()
    maker1.penup()
    maker1.goto(-400, 200)
    maker1.write("Controls :", font = ("Arial", 20, "bold"))
    maker1.goto(-380, 150)
    maker1.write("Move Forward - Right arrow", font = 10)
    maker1.goto(-380, 100)
    maker1.write("Move Backward - Left arrow", font = 10)
    maker1.goto(-380, 50)
    maker1.write("High Jump - Up arrow + Shift(left side)", font = 10)
    maker1.goto(-380, 0)
    maker1.write("Medium Jump - Up arrow + Ctrl(left side)", font = 10)
    maker1.goto(-380, -50)
    maker1.write("Low Jump - Up arrow", font = 10)
    maker1.goto(-380, -100)
    maker1.write("Exit - 0", font = 10)
    maker1.goto(0, 200)
    maker1.write("Rules :", font = ("Arial", 20, "bold"))
    maker1.goto(20, 150)
    maker1.write("Do not go next to the blue turtles, you will lose a life", font = 10)
    maker1.goto(20, 100)
    maker1.write("If you see a red flag, go next to it", font = 10)
    maker1.goto(20, 50)
    maker1.write("If you lose all your lives, you lose", font = 10)
    maker1.goto(0, -100)
    maker1.write("Press Q to start", font = ("Arial", 20, "bold"))

def screen1obstacles():
    global life
    tracker.goto(-100, 300)
    tracker.clear()
    tracker.write("Lives = " + str(life), font= ("Arial", 20, "bold"))
    maker1.clear()
    maker1.penup()
    maker1.goto(-400, -200)
    maker1.pendown()
    maker1.color("brown", "green")
    maker1.begin_fill()
    maker1.goto(-400, -200)
    maker1.goto(-400, -100)
    maker1.goto(-350, -100)
    maker1.goto(-350, -200)
    maker1.goto(-250, -200)
    maker1.goto(-250, -50)
    maker1.goto(-200, -50)
    maker1.goto(-200, -200)
    maker1.goto(0, -200)
    maker1.goto(0, -50)
    maker1.goto(70, -50)
    maker1.goto(70, -200)
    maker1.goto(200, -200)
    maker1.goto(200, -180)
    maker1.goto(260, -180)
    maker1.goto(260, -160)
    maker1.goto(320, -160)
    maker1.goto(320, -140)
    maker1.goto(380, -140)
    maker1.goto(380, -120)
    maker1.goto(440, -120)
    maker1.goto(440, -100)
    maker1.goto(500, -100)
    maker1.goto(500, -500)
    maker1.goto(-500, -500)
    maker1.goto(-500, -200)
    maker1.goto(-400, -200)
    maker1.end_fill()


def screen2obstacles():
    tracker.goto(-100, 300)
    tracker.clear()
    tracker.write("Lives = " + str(life), font=("Arial", 20, "bold"))
    maker1.clear()
    maker1.penup()
    maker1.setpos(-500, -100)
    maker1.pendown()
    maker1.begin_fill()
    maker1.setpos(-440, -100)
    maker1.setpos(-440, -120)
    maker1.setpos(-380, -120)
    maker1.setpos(-380, -140)
    maker1.setpos(-320, -140)
    maker1.setpos(-320, -160)
    maker1.setpos(-240, -160)
    maker1.setpos(-240, -180)
    maker1.setpos(-180, -180)
    maker1.setpos(-180, -200)
    maker1.setpos(500, -200)
    maker1.setpos(500, -500)
    maker1.goto(-500, -500)
    maker1.goto(-500, -100)
    maker1.end_fill()


def screen3obstacles():
    maker1.penup()
    maker1.goto(-500, -200)
    maker1.pendown()
    maker1.begin_fill()
    maker1.goto(-400, -200)
    maker1.goto(-400, -100)
    maker1.goto(-340, -100)
    maker1.goto(-340, -200)
    maker1.goto(350, -200)
    maker1.goto(350, -100)
    maker1.goto(410, -100)
    maker1.goto(410, -200)
    maker1.goto(500, -200)
    maker1.goto(500, -500)
    maker1.goto(-500, -500)
    maker1.goto(-500, -200)
    maker1.end_fill()

def screen4obstacles():
    maker1.penup()
    maker1.goto(-500, -200)
    maker1.pendown()
    maker1.begin_fill()
    maker1.goto(-100, -200)
    maker1.goto(-100, 0)
    maker1.goto(100, 0)
    maker1.goto(100, -200)
    maker1.goto(500, -200)
    maker1.goto(500, -500)
    maker1.goto(-500, -500)
    maker1.goto(-500, -200)
    maker1.end_fill()
    maker1.penup()
    maker1.goto(0, 0)
    maker1.color("black")
    maker1.pensize(3)
    maker1.pendown()
    maker1.goto(0, 150)


enemy1 = turtle.Turtle()
enemy1.shape("turtle")
enemy1.color("blue")
enemy1.shapesize(1.5)
enemy1.hideturtle()
enemy1.penup()
enemy1.goto(-100, -200)

enemy2 = turtle.Turtle()
enemy2.shape("turtle")
enemy2.color("blue")
enemy2.shapesize(1.5)
enemy2.hideturtle()
enemy2.penup()
enemy2.goto(0, -200)

enemy3 = turtle.Turtle()
enemy3.color("blue")
enemy3.shape("turtle")
enemy3.shapesize(1.5)
enemy3.hideturtle()
enemy3.penup()
enemy3.goto(100, -200)

enemy4 = turtle.Turtle()
enemy4.color("blue")
enemy4.shape("turtle")
enemy4.shapesize(1.5)
enemy4.hideturtle()
enemy4.penup()
enemy4.goto(200, -200)

enemy5 = turtle.Turtle()
enemy5.color("blue")
enemy5.shape("turtle")
enemy5.shapesize(1.5)
enemy5.hideturtle()
enemy5.penup()
enemy5.goto(300, -200)

enemy6 = turtle.Turtle()
enemy6.color("blue")
enemy6.shape("turtle")
enemy6.shapesize(1.5)
enemy6.hideturtle()
enemy6.penup()
enemy6.goto(400, -200)

run_enemy = turtle.Turtle()
run_enemy.color("blue")
run_enemy.shape("turtle")
run_enemy.shapesize(1.5)
run_enemy.hideturtle()
run_enemy.penup()
run_enemy.goto(340, -200)

flag = turtle.Turtle()
flag.color("red")
flag.shape("triangle")
flag.penup()
flag.right(180)
flag.hideturtle()
flag.shapesize(2)
flag.goto(-10, 0)

tracker = turtle.Turtle()
tracker.color("blue")
tracker.hideturtle()
tracker.penup()
tracker.goto(0, 300)

def enemy1_loss():
    global life
    if mario.distance(enemy1) < 40:
        life = life - 1
        if life == 0:
            loss_screen()
        else:
            mario.color("yellow")
            mario.color("red")
            mario.setpos(-480, -95)
            tracker.clear()
            tracker.goto(-100, 300)
            tracker.write("Lives = " + str(life), font= ("Arial", 20, "bold"))

def enemy2_loss():
    global life
    if mario.distance(enemy2) < 40:
        life = life - 1
        if life == 0:
            loss_screen()
        else:
            mario.color("yellow")
            mario.color("red")
            mario.setpos(-480, -95)
            tracker.clear()
            tracker.goto(0, 300)
            tracker.write("Lives = " + str(life), font= ("Arial", 20, "bold"))


def enemy3_loss():
    global life
    if mario.distance(enemy3) < 40:
        life = life - 1
        if life == 0:
            loss_screen()
        else:
            mario.color("yellow")
            mario.color("red")
            mario.setpos(-480, -95)
            tracker.clear()
            tracker.goto(0, 300)
            tracker.write("Lives = " + str(life), font= ("Arial", 20, "bold"))


def enemy4_loss():
    global life
    if mario.distance(enemy4) < 40:
        life = life - 1
        if life == 0:
            loss_screen()
        else:
            mario.color("yellow")
            mario.color("red")
            mario.setpos(-480, -95)
            tracker.clear()
            tracker.goto(0, 300)
            tracker.write("Lives = " + str(life), font= ("Arial", 20, "bold"))


def enemy5_loss():
    global life
    if mario.distance(enemy5) < 40:
        life = life - 1
        if life == 0:
            loss_screen()
        else:
            mario.color("yellow")
            mario.color("red")
            mario.setpos(-480, -95)
            tracker.clear()
            tracker.goto(0, 300)
            tracker.write("Lives = " + str(life), font= ("Arial", 20, "bold"))

def enemy6_loss():
    global life
    if mario.distance(enemy6) < 40:
        life = life - 1
        if life == 0:
            loss_screen()
        else:
            mario.color("yellow")
            mario.color("red")
            mario.setpos(-480, -95)
            tracker.clear()
            tracker.goto(0, 300)
            tracker.write("Lives = " + str(life), font= ("Arial", 20, "bold"))

def flag_hoist():
    global currentscreen
    if currentscreen == 4:
        if mario.distance(flag) <= 50:
            while flag.ycor() < 150:
                flag.sety(flag.ycor() + 1)
            else:
                tracker.color("yellow")
                tracker.goto(-300, 300)
                tracker.write("You have won the challenge !! Press 0 to exit", font= ("Arial", 20, "bold"))

currentscreen = 0


def enemy_run():
    global life, currentscreen
    while currentscreen == 3:
        if run_enemy.xcor() == 340:
            run_enemy.left(180)
            while run_enemy.xcor() > -330:
                run_enemy.setx(run_enemy.xcor() - 1)
        elif run_enemy.xcor() == -330:
            run_enemy.right(180)
            while run_enemy.xcor() != 340:
                run_enemy.setx(run_enemy.xcor() + 1)

def loadscreen1():
    global currentscreen
    try:
        mario.setpos(-450, -200)
        mario.showturtle()
        currentscreen = 1
        screen1obstacles()

    except:
        print("error in load screen 1 function")


def loadscreen2():
    try:
        mario.hideturtle()
        mario.setpos(-480, -95)
        mario.showturtle()
        global currentscreen
        currentscreen = 2
        maker1.clear()
        screen2obstacles()
        enemy1.showturtle()
        enemy2.showturtle()
        enemy3.showturtle()
        enemy4.showturtle()
        enemy5.showturtle()
        enemy6.showturtle()

    except:
        print("error in load screen 2 function")

def loadscreen3():
    global currentscreen
    currentscreen = 3
    mario.hideturtle()
    mario.setpos(-480, -200)
    mario.showturtle()
    maker1.clear()
    screen3obstacles()
    enemy1.hideturtle()
    enemy2.hideturtle()
    enemy3.hideturtle()
    enemy4.hideturtle()
    enemy5.hideturtle()
    enemy6.hideturtle()
    run_enemy.showturtle()
    enemy_run()

def loadscreen4():
    global currentscreen
    currentscreen = 4
    mario.hideturtle()
    mario.goto(-480, -200)
    mario.showturtle()
    maker1.clear()
    screen4obstacles()
    flag.showturtle()
    flag_hoist()
    tracker.clear()
    tracker.hideturtle()
    tracker.color("yellow")
    run_enemy.hideturtle()

def load_screens():
    try:
        global currentscreen
        if currentscreen == 0 and mario.xcor() <= -450:
            loadscreen1()
        elif currentscreen == 1 and mario.xcor() > 470:
            loadscreen2()
        elif currentscreen == 2 and mario.xcor() > 470:
            loadscreen3()
        elif currentscreen == 3 and mario.xcor() > 470:
            loadscreen4()

    except:
        print("error in load screens function")

controls_screen()

turtle.done()
