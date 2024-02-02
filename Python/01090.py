ioTimes = int(input())
school = {}
for i in range(ioTimes):
    name = input()
    if name not in school:
        school[name] = True
        print("in")
    else:
        del school[name]
        print("out")
