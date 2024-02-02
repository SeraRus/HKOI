sidesOfPolygon = int(input())
point = []
for i in range(sidesOfPolygon):
    point.append(list(map(int, input().split(" "))))
point.append(point[0])
plus = 0
for i in range(sidesOfPolygon):
    plus += point[i][0] * point[i+1][1]
    plus -= point[i+1][0] * point[i][1]
plus /= 2
print(plus)
