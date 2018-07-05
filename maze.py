import pyb
import lcd160cr
from math import sqrt # so we don't need to resolve math.sqrt on every loop iteration later
from random import randint, randrange

lcd = lcd160cr.LCD160CR('X')
accel = pyb.Accel()

def make_filled_maze(w, h):

    visited = []

    ver = []
    hor = []

    for y in range(0, h, 20):
        for x in range(0, w, 20):
            ver.append((x, y, x, y+20))

    for x in range(0, w, 20):
        for y in range(0, h, 20):
            hor.append((x, y, x+20, y))


    print (len(hor), len(ver), len(visited))

    def walk(x, y):
        print ((x, y))


        def shuffle(liste):
            new_liste = []

            for i in range(len(liste)):
                p = randint(0, len(liste)-1)
                new_liste.append(liste[p])
                del liste[p]

            return new_liste


        d = [(x - 20, y), (x, y + 20), (x + 20, y), (x, y - 20)]
        d = shuffle(d)

        besetzteNachbarn = 0

        for (xx, yy) in d:


            if (xx, yy) in visited:
                besetzteNachbarn += 1
                if besetzteNachbarn > 3:
                    letzterX = visited[-1][0]
                    letzterY = visited[-1][1]
                    print (visited)
                    visited[0] = visited[-1]
                    print (visited)
                    visited.pop()
                    print (visited)

                    walk(letzterX, letzterY)

                continue

            if xx < 0 or yy < 0 or yy > h or xx > w:
                besetzteNachbarn += 1
                if besetzteNachbarn > 3:
                    letzterX = visited[-1][0]
                    letzterY = visited[-1][1]
                    print (visited)
                    visited[0] = visited[-1]
                    print (visited)
                    visited.pop()
                    print (visited)

                continue

            if xx == x+20:

                print (x+10, y-10, x+10, y+10)
                try:
                    ver.remove((x+10, y-10, x+10, y+10))
                except ValueError:
                    break

            if xx == x-20:
                print ((x-10, y-10, x-10, y+10))
                try:
                    ver.remove((x-10, y-10, x-10, y+10))
                except ValueError:
                    break

            if yy == y+20:

                print ((x-10, y+10, x+10, y+10))
                try:
                    hor.remove((x-10, y+10, x+10, y+10))
                except ValueError:
                    break

            if yy == y-20:

                print (x-10, y-10, x+10, y-10)
                try:
                    hor.remove((x-10, y-10, x+10, y-10))
                except ValueError:
                    break



            visited.append((x, y))
            print (xx, yy , "xx,yy")
            print (len(hor), len(ver), len(visited))
            walk(xx, yy)

        for i in ver:
            lcd.line(i[0], i[1], i[2], i[3])

        for i in hor:
            lcd.line(i[0], i[1], i[2], i[3])

        lcd.line(w, 0, w, h)
        lcd.line(0, h, w, h)


    walk(randrange(30, w-30, 20), randrange(30, h-30, 20))

    print (len(hor), len(ver), len(visited))


fg = lcd.rgb(255, 255, 255)
bg = lcd.rgb(0, 0, 0)
fill = lcd.rgb(255, 255, 255)

lcd.set_pen(fg, bg)
lcd.erase()

make_filled_maze(120, 140)
