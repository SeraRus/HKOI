input()
n = list(map(int, input().split(" ")))
l = False
for i in n:
    if i % 2 == 0:
        pass
    else:
        print(i)
        l = not l
        break
if not l:
    print("Goodest English")
