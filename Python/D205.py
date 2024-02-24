from math import sqrt

n = int(input())
print(f"{n}=", end='')
while True:
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            print(f"{i}*", end='')
            n = int(n/i)
            break
    else:
        print(n)
        break
