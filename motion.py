
try:
    import pyb
    import lcd160cr
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

def Angles(tx, ty):

    SmootherY = 0
    SmootherX = 0

    for i in range(10):
        try:

            angleY = (accel.y() + 1) * -3.75
            angleX = (accel.x() - 2 ) * 3.75

            angleY = int((angleY/5) * 5)
            angleX = int((angleX/5) * 5)

        except NameError:
            angleY = -30
            angleX = 0

        SmootherY += angleY
        SmootherX += angleX


    angleY = SmootherY/10
    angleX = SmootherX/10

    angleY = int(angleY)
    angleX = int(angleX)

    if angleY > -6 and angleY < 6:
        angleY = 0
        ty = 1

    if angleX > -6 and angleX < 6:
        angleX = 0
        tx = 1

    return angleX, angleY, tx, ty

def applyForce(angle, t):
    """Number of pixels, the ball would have travelled
    after time has passed, if angle were constant"""

    HypotheticalDistanceFrom0 = int((sin(radians(angle)) * (t*t)) /20)

    return HypotheticalDistanceFrom0

def NewPosition(HypotheticalDistanceFrom0, OldPosition, t, angle):

    t = t - 1
    HypotheticalDistanceTMinusOne = applyForce(angle, t)

    delta = HypotheticalDistanceFrom0 - HypotheticalDistanceTMinusOne

    NewOffset = (int(OldPosition + delta))

    return NewOffset
