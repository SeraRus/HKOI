N = int(input())
Nr = N**2

Count = 1
for i in range(1, N+1):
    for u in range(1, i+1):
        print(Count, end=" ")
        Count += 1
    print()

N -= 1

for i in range(N-1):
    for u in range(N-i):
        if Count > Nr:
            break
        print(Count, end=" ")
        Count += 1
    print()

if Nr != 1:
    print(Nr)
