import math
n=int(input())
Square=bool((int(math.sqrt(n))*int(math.sqrt(n)))==n)
Triangular=bool(math.fmod(((math.sqrt(8*n+1)-1)/2),1.0)==0.0)
if Square and Triangular:
    print("Both")
elif Square:
    print("Square")
elif Triangular:
    print("Triangular")
else:
    print("Neither")
