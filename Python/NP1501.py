with open('coin.in', 'r') as f:
    K = int(f.readline())

cout = 0
cnt = 1
day = 0

while True:
    if day >= K:
        break
    cout += cnt*cnt
    day += cnt
    cnt += 1

ext = day - K
cout -= ext * (cnt-1)

with open('coin.out', 'w') as f:
    f.write(str(cout))
