str = input()
target = input()
targetLength = len(target)
count = 0

for i in range(len(str) - targetLength + 1):
    substring = str[i:i+targetLength]
    if substring == target:
        count += 1

print(count)
