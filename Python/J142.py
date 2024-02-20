freeGemMin = 0
payGemMin = 0
freeGemMax = 0
payGemMax = 0
eventTimes = int(input())
for i in range(eventTimes):
    temp = input().split(' ')
    if temp[0] == '1':
        payGemMin += int(temp[1])
        payGemMax += int(temp[1])
    elif temp[0] == '2':
        freeGemMin += int(temp[1])
        freeGemMax += int(temp[1])
    elif temp[0] == '3':
        freeGemMax -= int(temp[1])
        if freeGemMax < 0:
            payGemMax += freeGemMax
            freeGemMax = 0
        payGemMin -= int(temp[1])
        if payGemMin < 0:
            freeGemMin += payGemMin
            payGemMin = 0
    else:
        print(payGemMax, payGemMin)
