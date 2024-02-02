import math


s=input()
a = int(s.split(' ')[0])
b = int(s.split(' ')[1])
c = int(s.split(' ')[2])

delta = b**2 - 4*a*c

if delta < 0:
    print("None")
elif delta == 0:
    x = (-b + math.sqrt(delta)) / (2*a)  
    print(format(x, ".3f"))
else:
    x = (-b + math.sqrt(delta)) / (2*a)  
    y = (-b - math.sqrt(delta)) / (2*a)  
    if x < y:
        print(format(x, ".3f"))
        print(format(y, ".3f"))
    else:
        print(format(y, ".3f"))
        print(format(x, ".3f"))
