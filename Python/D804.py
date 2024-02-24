input()
First = list(map(int, input().split(" ")))
Second = list(map(int, input().split(" ")))
Temp1 = []


while len(First) != 0 and len(Second) != 0:
    if First[0] < Second[0]:
        Temp1.append(First.pop(0))
    else:
        Temp1.append(Second.pop(0))

if len(First) != 0:
    Temp1 += First
else:
    Temp1 += Second

print(*Temp1, sep=' ')
