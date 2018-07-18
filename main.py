try:
    import pyb
    import lcd160cr
    import maze
    import gameloop
    import drawCircle

except ImportError:
    pass



from math import sqrt, sin, radians
from random import randint
from time import sleep

try:
    lcd = lcd160cr.LCD160CR('X')
    accel = pyb.Accel()

except NameError:
    pass

ForbiddenY = {}#{37: range(40, 120), 42: range(40, 120)}
ForbiddenX = {}#{117: range(40, 80), 122: range(40, 80)}


if __name__ == "__main__":
    try:
        fg = lcd.rgb(255, 255, 255)
        bg = lcd.rgb(0, 0, 0)
        fill = lcd.rgb(255, 255, 255)

        lcd.set_pen(fg, bg)
        lcd.erase()

    except NameError:
        pass

    Xmax = 120
    Ymax = 140
    r = 3

    BallPosition, GoalPosition, ver, hor = maze.make_filled_maze(Xmax, Ymax)


    gameloop.GameLoop(r, BallPosition[0], BallPosition[1], Xmax, Ymax, ver, hor, GoalPosition)
