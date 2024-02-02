s=input()
li=s.split(' ')
for i in range(len(li)):
    li[i]=int(li[i])
print(li[0]|li[1])
print(li[0]&li[1])
print(li[0]^li[1])
print(~li[0])
