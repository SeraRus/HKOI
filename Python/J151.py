n, m = map(int, input().split())

if m > 1000000 or m < -1000000:
    for i in range(1, (n + 1) // 2):
        print(i, -i, end=' ')
else:
    for i in range(1, (n + 1) // 2):
        print(i + 2000000, -i - 2000000, end=' ')

if n % 2 == 0:
    if m == 0:
        print("-99999999 99999999")
    else:
        print("0", m)
else:
    print(m)
