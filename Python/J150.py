N = int(input())
count = 1
for i in range(N):
    for u in range(N):
        print(count, end = " ")
        count += 4
    count -= 4
    print()
