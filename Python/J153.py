a = input()
b = input()
x = len(a)
y = len(b)
overtype = 0
deleted = 0
result = ""

for i in range(y):
    if b[i] == 'D':
        deleted += 1
    elif b[i] == 'I':
        overtype = 1 - overtype
    else:
        result += b[i]
        deleted += overtype

if deleted < x:
    result += a[deleted:]

print(result)
