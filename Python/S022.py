inputNumbers = int(input())
numbers = []
for i in range(inputNumbers):
    numbers.append(int(input()))
numbers.sort()
addition = 0
while len(numbers) != 1:
    num1 = numbers.pop(0)
    num2 = numbers.pop(0)
    numbers.append(num1 + num2)
    addition += num1 + num2
    numbers.sort()
print(addition)
