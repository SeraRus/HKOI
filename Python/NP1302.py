with open('expr.in', 'r') as f:
    expression = f.readline().strip()
nums = []
ops = []
i = 0
while i < len(expression):
    if expression[i].isdigit():
        j = i
        while j < len(expression) and expression[j].isdigit():
            j += 1
        nums.append(int(expression[i:j]))
        i = j
    elif expression[i] == '+':
        ops.append(expression[i])
        i += 1
    elif expression[i] == '*':
        j = i + 1
        while j < len(expression) and expression[j].isdigit():
            j += 1
        nums.append(nums.pop() * int(expression[i+1:j]))
        i = j
result = nums[0]
for i in range(len(ops)):
    if ops[i] == '+':
        result += nums[i+1]
    else:
        result *= nums[i+1]
with open('expr.out', 'w') as f:
    f.write(str(result)[-4:])
