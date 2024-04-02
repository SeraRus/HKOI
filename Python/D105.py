d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))

if d1 > d2:
  print("After")
elif d2 > d1:
  print("Before")
else:
  print("Same")
