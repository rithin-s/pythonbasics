floor1X = [-500, -400, -350, -250, -200, 0, 70, 200, 260, 320, 380, 440, 500]
floor1H = [0, 0, 100, 0, 150, 0, 150, 0, 20, 40, 60, 80, 100]

x = -200
y = -200
floor = -200
h = 0


def find_floorY():
    global floor1X, floor1H, x, y, h, ind, floor
    for coord in floor1X:
        if x < coord:
            return

        if x > coord:
            ind = floor1X.index(coord)
            h = floor1H[ind]
            floor = floor + h
            print(floor)

        if x == coord:
            h = floor1H[ind]
            floor = floor + h
            print(floor)


# if x >= floor1X[0] and x <= floor1X[1]:ONE WAY TO DO IT(BUT USE LOOPS)
# h = floor1H[1]
# y = y - h
# return y

wall_h = -200

def wall_collision():
    global i, floor1X, floor1H, wall_h, moveright, moveleft, range, x
    for i in floor1H:
        if y >= (i + wall_h):
            moveright = True
            moveleft = True
            print (i)
        elif y < (i + wall_h):
            for j in floor1X:
                if x >= j:
                    print(x)
                    moveright = False
                    moveleft = True
                elif x <= j:
                    print(x)
                    moveright = True
                    moveleft = False

wall_collision()