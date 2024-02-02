ab = ["a","b","c","d","e","f","g","h"]
pt1 = input()
x1 = int(ab.index(pt1[:1])+1)
y1 = int(pt1[-1:])
pt2 = input()
x2 = int(ab.index(pt2[:1])+1)
y2 = int(pt2[-1:])
l1 = abs(x1 - x2)
l2 = abs(y1 - y2)
if l1 > l2:
  print(l1)
else:
  print(l2)
