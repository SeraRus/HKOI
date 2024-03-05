def app():
    global route
    route.append([])
    route[-1].extend(pos)
    if maze[pos[0]+1][pos[1]] == '#':
        route[-1].append(False)
    else:
        route[-1].append(True)
    if maze[pos[0]][pos[1]+1] == '#':
        route[-1].append(False)
    else:
        route[-1].append(True)


finishPos = list(map(int, input().split(' ')))
finishPos[0] -= 1
finishPos[1] -= 1
maze = [list(input()) for _ in range(finishPos[0]+1)]
maze.append(['#'] * (finishPos[1]+1))
for i in maze:
    i.append('#')
routeSE = []
route = []
pos = [0, 0]
app()
while pos != finishPos:
    if route[-1][2]:
        pos[0] += 1
        app()
        routeSE.append('S')
    elif route[-1][3]:
        pos[1] += 1
        app()
        routeSE.append('E')
    else:
        del route[-1]
        if routeSE.pop(-1) == 'S':
            route[-1][2] = False
            pos[0] -= 1
        else:
            route[-1][3] = False
            pos[1] -= 1
print(*routeSE, sep='')
