with open('number.in','r') as f:
    s=f.read()

s = list(s)
count = 0
for i in s:
    if i == "1":
        count += 1

with open('number.out','w+') as f:
    f.write(str(count))
