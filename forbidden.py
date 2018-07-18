def makeForbidenPlaces(ver, hor):

    ForbiddenY = {}
    ForbiddenX = {}

    print ("ver", ver)
    print ("hor", hor)

    for i in range(len(hor)):
        if hor[i][1] in ForbiddenX:
            for j in range(hor[i][0], hor[i][2]):
                ForbiddenX[hor[i][1]].append(j)

        else:
            ForbiddenX[hor[i][1]] = []
            for j in range(hor[i][0], hor[i][2]):
                ForbiddenX[hor[i][1]].append(j)



    for i in range(len(ver)):
        if ver[i][0] in ForbiddenY:
            for j in range(ver[i][1], ver[i][3]):
                ForbiddenY[ver[i][0]].append(j)
        else:
            ForbiddenY[ver[i][0]] = []
            for j in range(ver[i][1], ver[i][3]):
                ForbiddenY[ver[i][0]].append(j)

    print ("ForbiddenX", ForbiddenX)
    print ("ForbiddenY", ForbiddenY)

    return ForbiddenX, ForbiddenY
