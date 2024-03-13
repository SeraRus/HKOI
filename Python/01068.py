numbers = []
for i in range(int(input())):
    numbers.append(list(map(int, input().split())))
    numbers[-1].append(numbers[-1][0]**2 + numbers[-1][1]**2)
numbers = sorted(numbers, key=lambda x: x[-1])
for i in numbers:
    print(i[0], i[1])
