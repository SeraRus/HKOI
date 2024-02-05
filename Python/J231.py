Drink = int(input())
if Drink <= 3:
    DP = 15
elif Drink <= 6:
    DP = 18
elif Drink <= 8:
    DP = 20
else:
    DP = 30
ICE = input()
if ICE == "Normal":
    pass
elif ICE == "Less Ice":
    DP += 2
else:
    DP += 3
SW = input()
if SW == "100%":
    pass
elif SW == "50%":
    DP += 1
elif SW == "30%":
    DP += 2
else:
    DP += 4
Ex = int(input())
if Ex == 0:
    pass
else:
    Sp = input().split(", ")
    Sp = list(set(Sp))
    for ext in Sp:
        if ext == "Pearl" or ext == "Pudding":
            DP += 4
        elif ext == "Aloe" or ext == "Agar":
            DP += 5
        elif ext == "Grass Jelly" or ext == "Lychee Jelly" or ext == "Coffee Jelly":
            DP += 6
        else:
            DP += 7
print(DP)
