numberOfInput = int(input())
char = []
for i in range(numberOfInput):
    temp = input()
    equalPos = temp.find('=')
    if temp[:equalPos] not in char:
        char.append(temp[:equalPos])
    exec(f"{temp[:equalPos]} = eval(temp[equalPos+1:])")
char = sorted(char)
for i in char:
    print(f"{i}={eval(i)}")
