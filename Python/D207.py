import math
s=input()
s=s.split(' ')
num1=int(s[0])
num2=int(s[1])
print(math.gcd(num1,num2))
print(int(num1*num2/math.gcd(num1,num2)))
