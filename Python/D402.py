N = int(input())
products = {}
for i in range(N):
    code, price = input().split()
    products[code] = float(price)

M = int(input())
total_price = 0
for i in range(M):
    code = input()
    total_price += products[code]

print("{:.1f}".format(total_price))
