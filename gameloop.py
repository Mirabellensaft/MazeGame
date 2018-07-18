
try:
    import pyb
    import lcd160cr
except ImportError:
    pass

from math import sqrt, sin, radians
from random import randint
from time import sleep

# gamefiles
import forbidden
import collisions
import motion
import drawCircle

try:
    lcd = lcd160cr.LCD160CR('X')
    accel = pyb.Accel()

except NameError:
    pass


def DrawGame(r, dx, dy, ver, hor, Xmax, Ymax, GoalPosition):
    """r = radius of the circle
    dx and dy are offset of the center in x and y direction
    so the circle's center is not at 0,0"""

    dy = int(dy)
    dx = int(dx)

    for x in range(0, r):

        if x/(sqrt(r**2-x**2)) < 1:
            y = round(sqrt(r**2-x**2))

            try:
                lcd.erase()
            except NameError:
                pass

            try:
                lcd.dot(dx + x, dy - y) #1
                lcd.dot(dx + y, dy - x) #2
                lcd.dot(dx + y, dy + x) #3
                lcd.dot(dx + x, dy + y) #4
                lcd.dot(dx - x, dy + y) #5
                lcd.dot(dx - y, dy + x) #6
                lcd.dot(dx - y, dy - x) #7
                lcd.dot(dx - x, dy - y) #8

                for i in ver:
                    lcd.line(i[0], i[1], i[2], i[3])

                for i in hor:
                    lcd.line(i[0], i[1], i[2], i[3])

                lcd.line(Xmax, 0, Xmax, Ymax)
                lcd.line(0, Ymax, Xmax, Ymax)

                drawCircle.DrawCircle(10, GoalPosition[0], GoalPosition[1])

            except NameError:
                pass

                #print("CircleCoordinates", dy, dx)
                # print(dx + x, dy - y) #1
                # print(dx + y, dy - x) #2
                # print(dx + y, dy + x) #3
                # print(dx + x, dy + y) #4
                # print(dx - x, dy + y) #5
                # print(dx - y, dy + x) #6
                # print(dx - y, dy - x) #7
                # print(dx - x, dy - y) #8



def isinGoal(dx, dy, gr, gx, gy):

    """Checks, if coordinates of ball are within the goal"""

    if dx in range(gx-gr, gx+gr) and dy in range(gy-gr, gy+gr):
        inCircle = True
    else:
        inCircle = False
    #print (inCircle)
    return inCircle





def GameLoop(r, dx, dy, Xmax, Ymax, ver, hor, GoalPosition):
    """Draws a circle with new coodinates in every loop"""

    OldPositionY = dy
    OldPositionX = dx
    AngleOldY = 10
    AngleOldX = 10
    ty = 1
    tx = 1

    ForbiddenX, ForbiddenY = forbidden.makeForbidenPlaces(ver, hor)

    while True:

        ty += 1
        tx += 1

        angleX, angleY, tx, ty = motion.Angles(tx, ty)

        ty = collisions.ChangeOfDirectionDetector(angleY, AngleOldY, ty)
        tx = collisions.ChangeOfDirectionDetector(angleX, AngleOldX, tx)

        #print ("times", tx, ty)

        HypotheticalDistanceFrom0Y = motion.applyForce(angleY, ty)
        HypotheticalDistanceFrom0X = motion.applyForce(angleX, tx)

        #print ("angleY", angleY)
        #print ("angleX", angleX)


        NewPositionY = motion.NewPosition(HypotheticalDistanceFrom0Y, OldPositionY, ty, angleY)
        NewPositionX = motion.NewPosition(HypotheticalDistanceFrom0X, OldPositionX, tx, angleX)

        ty,  NewPositionY = collisions.CollisionDetector(OldPositionY, NewPositionY, ty, Ymax, r, NewPositionX, ForbiddenX)
        tx,  NewPositionX = collisions.CollisionDetector(OldPositionX, NewPositionX, tx, Xmax, r, NewPositionY, ForbiddenY)

        DrawGame(r, NewPositionX, NewPositionY, ver, hor, Xmax, Ymax, GoalPosition)
        # #print("CircleCoordinates", r, NewPositionX, NewPositionY)


        OldPositionY = NewPositionY
        OldPositionX = NewPositionX

        if angleX != 0:
            AngleOldX = angleX

        if angleY != 0:
            AngleOldY = angleY

        sleep(0.04)
        #sleep(0.5)

if __name__ == "__main__":

    ver = []
    hor = []

    try:
        fg = lcd.rgb(255, 255, 255)
        bg = lcd.rgb(0, 0, 0)
        fill = lcd.rgb(255, 255, 255)

        lcd.set_pen(fg, bg)
        lcd.erase()

    except NameError:
        pass

    GameLoop(3, 20, 110, 120, 159, ver, hor, [10,  10])
