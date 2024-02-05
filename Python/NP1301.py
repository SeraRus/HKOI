 with open('count.in', 'r') as f:
    n, x = f.readline().split()
n = int(n)
count = 0
for i in range(1, n+1):
    p = list(str(i))
    for u in p:
        if u == x:
            count += 1
        
        
with open('count.out', 'w') as f:
    f.write(str(count))
