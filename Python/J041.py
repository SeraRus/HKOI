import math

allSum = []
for i in range(int(input())):
    Sum = list(map(int, input().split(" ")))
    Sum = Sum[0] + Sum[1]
    allSum.append(Sum)
print(math.lcm(*allSum))
