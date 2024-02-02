d1 = input().split(" ")
d2 = input().split(" ")

d1 = [int(x) for x in d1]
d2 = [int(x) for x in d2]

if d1 > d2:
  print("After")
elif d2 > d1:
  print("Before")
else:
  print("Same")
