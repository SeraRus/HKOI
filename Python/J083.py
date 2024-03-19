n = int(input())
sum = 0
k = 1

for i in range(59):
    sum += n // (k * 2) * k
    if n % (k * 2) >= k:
        sum += n % k + 1
    k *= 2

print(sum)
