input()
array = list(map(int, input().split()))
middle = array[-1]
i = 0
for j in range(0, len(array)):
    if array[j] <= middle:
        array[i], array[j] = array[j], array[i]
        i += 1
print(*array)
