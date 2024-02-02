L = []
LIFO = []
n = int(input())
counter = 1
while counter <= n:
    L.append(input())
    counter += 1

for item in L:
    if len(item) > 5:
        LIFO.append(item[5:])
    elif item == "SIZE":
        print(len(LIFO))
    elif item == "TOP":
        if len(LIFO) == 0:
            print("Empty")
        else:
            print(LIFO[-1])
    elif item == "POP":
        if len(LIFO) == 0:
            print("Cannot pop")
        else:
            del LIFO[-1]

