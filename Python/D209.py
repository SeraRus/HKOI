n = int(input())
s = input()
s = s.split(' ')
s = list(map(int, s))
y = 0


def check():
    global n, s, y
    for x in s:
        if 100 < x < 50000:
            y += 1
        else:
            pass
    if y != n:
        return 0
    
    if len(s) != len(set(s)):
        return 0
    
    if s != sorted(s):
        return 0
    
    return 1


if check():
    print("Valid")
else:
    print("Invalid")
