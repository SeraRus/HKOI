input()
N = list(input())
dash = 0
dot = 0
for i in N:
    if i == ".":
        dot += 1
    elif i == "-":
        dash += 1
print(2*dot-dash)
