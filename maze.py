try:
    import pyb
    import lcd160cr
except ImportError:
    pass

from random import randint, randrange

try:
    lcd = lcd160cr.LCD160CR('X')
    accel = pyb.Accel()

except NameError:
    pass



def shuffle(liste):
    new_liste = []

    for i in range(len(liste)):
        p = randint(0, len(liste)-1)
        new_liste.append(liste[p])
        del liste[p]

    return new_liste

def make_filled_maze(w, h):

    """generates a grid of vertical and horizontal walls"""

    visited = []
    CellCenters = []

    ver = []
    hor = []

    # generate vertical walls
    for y in range(0, h, 20):
        for x in range(0, w, 20):
            ver.append((x, y, x, y+20))

    # generate horizontal walls
    for x in range(0, w, 20):
        for y in range(0, h, 20):
            hor.append((x, y, x+20, y))

    # generate list with coordinates of cell centers
    for x in range(10, w, 20):
        for y in range(10, h, 20):
            CellCenters.append((x,y))
    print ('1', x,y)

    def walk(x, y):

        """walks through the grid, deleting walls to create a maze."""

        #print ('xy', x,y)

        visited.append((x, y))

        NeighborCells = [(x - 20, y), (x, y + 20), (x + 20, y), (x, y - 20)]
        NeighborCells = shuffle(NeighborCells)
        #print (NeighborCells, x, y)

        besetzteNachbarn = 0

        for (xx, yy) in NeighborCells:
            #print("xx, yy", xx, yy)

            if len(CellCenters) == len(visited):
                # print("visitd", len(visited))
                # print("CellCenters", len(CellCenters))
                #print ("Langen gleich")
                break

            elif besetzteNachbarn == 4:
                #print ("Nachbarschaft zu!")
                letzterX = visited[-1][0]
                letzterY = visited[-1][1]

                visited[0] = visited[-1]

                visited.pop()


                walk(letzterX, letzterY)

            elif (xx, yy) not in CellCenters:
                besetzteNachbarn += 1
                #print ("not on List")
                continue

            elif (xx, yy) in visited:
                besetzteNachbarn += 1
                #print ("already in List")
                continue


            elif xx == x+20:

                try:
                    ver.remove((x+10, y-10, x+10, y+10))
                except ValueError:
                    #print ("ValueError")
                    continue

            elif xx == x-20:
                try:
                    ver.remove((x-10, y-10, x-10, y+10))
                except ValueError:
                    #print ((x,y), (x-10, y-10, x-10, y+10))
                    #print ("ValueError")
                    continue

            elif yy == y+20:

                try:
                    hor.remove((x-10, y+10, x+10, y+10))
                except ValueError:
                    #print ((x,y), (x-10, y+10, x+10, y+10))
                    #print ("ValueError")
                    continue

            elif yy == y-20:

                try:
                    hor.remove((x-10, y-10, x+10, y-10))
                except ValueError:
                    #print ("ValueError")
                    #print ((x,y), (x-10, y-10, x+10, y-10))
                    continue



            # lcd.erase()
            # for i in ver:
            #     lcd.line(i[0], i[1], i[2], i[3])
            #
            # for i in hor:
            #     lcd.line(i[0], i[1], i[2], i[3])

            walk(xx, yy)





    RandomStartCell = CellCenters[randint(0, len(CellCenters))]
    walk(RandomStartCell[0], RandomStartCell[1])

    #print ("visited", visited)
    return RandomStartCell, visited[-11], ver, hor

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

    a, b, ver, hor = make_filled_maze(Xmax, Ymax)

    try:
        lcd.erase()
        for i in ver:
            lcd.line(i[0], i[1], i[2], i[3])

        for i in hor:
            lcd.line(i[0], i[1], i[2], i[3])


        lcd.line(Xmax, 0, Xmax, Ymax)
        lcd.line(0, Ymax, Xmax, Ymax)

    except NameError:
        pass
