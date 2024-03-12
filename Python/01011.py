screen = [[' '] * 80 for _ in range(25)]
inputNum = int(input())
for i in range(inputNum):
    square = input()
    squareChar = square[0]
    squareXPosL, squareYPosL, squareXPosR, squareYPosR = map(int, square[1:].split())
    for u in range(squareYPosL, squareYPosR + 1):
        screen[u][squareXPosL:squareXPosR + 1] = [squareChar] * (squareXPosR - squareXPosL + 1)
    for u in range(squareYPosL + 1, squareYPosR):
        screen[u][squareXPosL + 1:squareXPosR] = [' '] * (squareXPosR - squareXPosL - 1)
for i in screen:
    print(*i, sep='')
