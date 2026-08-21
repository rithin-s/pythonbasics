import turtle

mario = turtle.Turtle()
mario.shape("turtle")
mario.shapesize(1.5)
mario.color("red")
mario.penup()
mario.setpos(-450, -200)

screen1 = turtle.Screen()
screen1.title("                                                                                                                                   Mario 2.0")
screen1.listen()
screen1.setup(1000, 792, 250, 0)

fshift = False
fcontrol = False
move_right = True
move_left = True

def fshift_true():
    gravity()
    global fshift
    fshift = True


def fshift_false():
    gravity()
    global fshift
    fshift = False


def fcontrol_true():
    gravity()
    global fcontrol
    fcontrol = True


def fcontrol_false():
    gravity()
    global fcontrol
    fcontrol = False


def jump():
    print(mario.ycor())
    global fcontrol, fshift, y
    y = mario.ycor()
    if fshift:
        mario.sety(y + 150)

    elif fcontrol:
        mario.sety(y + 100)

    else:
        mario.sety(y + 20)
    gravity()
    wall_collision_backward()
    wall_collision_forward()


def fall():
    print(mario.ycor())
    global fcontrol, fshift
    y = mario.ycor()
    if fshift:
        mario.sety(y - 150)

    elif fcontrol:
        mario.sety(y - 100)

    else:
        mario.sety(y - 20)
    gravity()


def start_front():
    global move_right
    print(mario.xcor())
    print("start front")
    wall_collision_forward()
    if move_right:
        mario.forward(10)
    else:
        stop_front()


def stop_front():
    mario.forward(0)
    wall_collision_forward()
    gravity()


def start_back():
    global move_left
    print(mario.xcor())
    print("start back")
    wall_collision_backward()
    if move_left:
        mario.back(10)
    else:
        stop_back()


def stop_back():
    mario.backward(0)
    wall_collision_backward()
    gravity()


def controls1():
    screen1.onkeypress(fshift_true, "Shift_L")
    screen1.onkeyrelease(fshift_false, "Shift_L")
    screen1.onkeypress(fcontrol_true, "Control_R")
    screen1.onkeyrelease(fcontrol_false, "Control_R")
    screen1.onkey(jump, "Up")
    screen1.onkey(fall, "Down")
    screen1.onkeypress(start_back, "Left")
    screen1.onkeyrelease(stop_back, "Left")
    screen1.onkeypress(start_front, "Right")
    screen1.onkeyrelease(stop_front, "Right")


controls1()

maker1 = turtle.Turtle()
maker1.hideturtle()
maker1.penup()
maker1.pencolor("green")
maker1.speed(0)
maker1.goto(-500, -200)

def wall_collision_forward():
    global wall, move_right
    if mario.ycor() < floor:
        for a in floor1X:
            b = floor1X.index(a)
            c = b % 2
            wall = c + 1
            if not wall % 2 == 0:
                if mario.xcor() <= floor1X[wall]:
                    move_right = False
                elif mario.xcor() != wall:
                    move_right = True
                else:
                    move_right = True
            print("Wall : ", floor1X[wall])
    else:
        move_right = True

def wall_collision_backward():
    global wall, move_left
    if mario.ycor() < floor:
        for a in floor1X:
            b = floor1X.index(a)
            wall = b % 2
            if mario.xcor() >= floor1X[wall]:
                move_left = False
            elif mario.xcor() != wall:
                move_left = True
            else:
                move_left = True
        print("Wall : ", floor1X[wall])
    else:
        move_left = True

    #ONE WAY TO DO IT (BUT NEEDS LOOPS)
    #if mario.xcor() >= floor1X[1] and mario.xcor() < floor1X[2]:
        #mario.setx(floor1X[1])
    #if mario.xcor() >= floor1X[1] and mario.xcor() < floor1X[2]:
        #mario.setx(floor1X[2])


floor1X = [-480 ,-400, -350, -250, -200, 0, 70, 200, 260, 320, 380, 440, 500]
floor1H = [0, 100, 0, 150, 0, 150, 0, 20, 40, 60, 80, 100]


floor = -200
h = 0

def find_floorY():
    print("findfloorY function start")
    global floor1X, floor1H, x, h, ind, floor
    x = mario.xcor()
    try:
        for coord in floor1X:
            if x >= coord:
                floor = -200
                ind = floor1X.index(coord)
                h = floor1H[ind]
                floor = floor + h

    except:
        print("error in finding floor")
    print("findfloorY function end")

    #if x >= floor1X[0] and x <= floor1X[1]:ONE WAY TO DO IT(BUT USE LOOPS)
        #h = floor1H[1]
        #y = y - h
        #return y


def gravity():
    print("gravity function start")
    try:
        find_floorY()
        global floor, y
        y = mario.ycor()
        print("Floor: ", floor)
        while y > floor:
            if mario.ycor() > floor:
                mario.sety(y - 5)
            else:
                mario.sety(floor)
    except:
        print("error in gravity function")
    print("gravity funtion end")


def screen1obstacles():
    maker1.pendown()
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


def screen2obstacles():
    maker1.penup()
    maker1.setpos(-500, -100)
    maker1.pendown()
    maker1.goto(-500, -100)
    maker1.goto(-500, -120)
    maker1.goto(-440, -120)
    maker1.goto(-440, -140)
    maker1.goto(-380, -140)
    maker1.goto(-380, -160)
    maker1.goto(-320, -160)
    maker1.goto(-320, -180)
    maker1.goto(240, -180)
    maker1.goto(240, -200)
    maker1.goto(400, -200)
    maker1.goto(400, -100)
    maker1.goto(450, -100)
    maker1.goto(450, -200)
    maker1.goto(500, -200)


currentscreen = 0


def loadscreen1():
    global currentscreen
    print("loadscreen1 function start")
    try:
        mario.setpos(-450, -200)
        global currentscreen
        currentscreen == 1
        print("current screen :", currentscreen)
        screen1obstacles()

    except:
        print("error in load screen 1 function")
    print("loadscreen1 function end")


def loadscreen2():
    print("loadscreen2 function start")
    try:
        mario.hideturtle()
        mario.setpos(-480, -115)
        mario.showturtle()
        global currentscreen
        currentscreen == 2
        print("current screen :", currentscreen)
        maker1.clear()
        screen2obstacles()

    except:
        print("error in load screen 2 function")
    print("loadscreen2 function end")


def loadscreens():
    print("loadscreens function ")
    try:
        global currentscreen
        if currentscreen == 0 and mario.xcor() <= -450:
            loadscreen1()
        elif currentscreen == 1 and mario.xcor() >= 460:
            loadscreen2()

    except:
        print("error in load screens function")
    print("loadscreens function end")


loadscreens()

turtle.done()
