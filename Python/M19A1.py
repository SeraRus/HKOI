d = input().split(" ")
del d[0]
del d[1]
if int(d[0], 8) == int(d[1]):
    print("April's Fool")
elif int(d[0], 8) > int(d[1]):
    print("Halloween")
else:
    print("Christmas")
