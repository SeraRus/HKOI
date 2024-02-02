llist = []
s, f = tuple(map(int, input().split()))
for x in map(int, input().split()):
    llist.append([x])
n = list(map(int, input().split()))
for x in range(0, s):
    llist[x].append(n[x])
x, y = tuple(map(int, input().split()))
if y == 0:
    print(len(llist)+1)
    print("%d %d"%(x, f))
    print(-1)
else:
    clls = llist[f-1]
    cele = f
    for n in range(y-1):
        cele = clls[1]
        clls = llist[cele-1]
    ocl = clls[1]
    clls[1] = len(llist)+1
    llist.append([x, ocl])
    print(f)
    print("%d %d"%tuple(llist[-1]))
    print("%d %d %d"%(cele, llist[cele-1][0], llist[cele-1][1]))
