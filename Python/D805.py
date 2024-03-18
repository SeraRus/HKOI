n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
for _ in range(m):
    mLine = list(map(int, input().split()))
    listA = array[mLine[0]-1:mLine[1]]
    listB = array[mLine[2]-1:mLine[3]]
    mLine = sorted(listA+listB)
    print(*mLine)
