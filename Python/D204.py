levels = input()
levels = int(int(levels) / 2)
levels2 = levels
reverse = []
for i in range(levels + 1):
    temp = f'{" " * levels}#'
    temp = list(temp)
    temp[levels2] = "#"
    temp = "".join(temp)
    print(temp)
    levels += 1
    levels2 -= 1
    reverse.append(temp)
del reverse[-1]
reverse.reverse()
for m in reverse:
    print(m)
