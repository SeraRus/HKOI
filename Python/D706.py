from collections import deque

n = int(input())
q = deque()
for i in range(n):
    op = input().split()
    if op[0] == 'PUSH':
        if len(q) < 10000:
            q.append(int(op[1]))
    elif op[0] == 'FRONT':
        if len(q) > 0:
            print(q[0])
        else:
            print('Empty')
    elif op[0] == 'POP':
        if len(q) > 0:
            q.popleft()
        else:
            print('Cannot pop')
    elif op[0] == 'SIZE':
        print(len(q))
