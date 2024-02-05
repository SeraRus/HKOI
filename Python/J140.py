N = int(input())
for i in range(1, N+1):
    Fir = i**2
    print(Fir, end = " ")
    for u in range(N-1):
        Fir += i
        print(Fir, end = " ")
    print()
