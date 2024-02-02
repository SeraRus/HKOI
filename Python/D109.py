x = int(input())
bn = [1000, 500, 100, 50, 20, 10]
for i in bn:
    while x >= i:
        print(i)
        x -= i
