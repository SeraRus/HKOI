numbersStudents = input()
teamAMembers = list(map(int, input().split(" ")))
teamBMembers = list(map(int, input().split(" ")))

teamAMembers.sort()
winTurn = 0

for i in teamBMembers:
    for u in range(len(teamAMembers)):
        if teamAMembers[u] > i:
            winTurn += 1
            teamAMembers.pop(u)
            break

print(winTurn)
