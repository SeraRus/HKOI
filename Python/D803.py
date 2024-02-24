input()
bol = 0
nums = list(map(int, input().split(" ")))
print(nums[0])
sortedList = [nums.pop(0)]
for i in range(len(nums)):
    temp = nums.pop(0)
    for u in range(len(sortedList)):
        if temp <= sortedList[u]:
            sortedList.insert(u, temp)
            bol += 1
            break
    if bol == 0:
        sortedList.append(temp)
    print(*sortedList, end='\n')
    bol = 0
