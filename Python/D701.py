from collections import deque

queue = deque()

n = int(input())

for i in range(n):
    operation = input().split()
    if operation[0] == "PUSH":
        queue.append(int(operation[1]))
    elif operation[0] == "FRONT":
        if len(queue) == 0:
            print("Empty")
        else:
            print(queue[0])
    elif operation[0] == "POP":
        if len(queue) == 0:
            print("Cannot pop")
        else:
            queue.popleft()
    elif operation[0] == "SIZE":
        print(len(queue))
