import math

num = int(input())
factors = []
for_times = int(math.sqrt(num))
for i in range(for_times + 1)[1:]:
    if num % i == 0:
        factors.append(i)
        t = int(num / i)
        if not t == i:
            factors.append(t)
factors.sort()
print(*factors, sep='\n')
