from math import sqrt
n=int(input())
print ("%d=" %n , end = '')
while 1:
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            print('%d*'%i,end='')
            n=int(n/i)
            break
    else:
        print(n)
        break
