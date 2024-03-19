dist = [
    "01232343451",
    "10121232342",
    "21012123231",
    "32103214322",
    "21230121233",
    "32121012122",
    "43212103213",
    "32341230124",
    "43232121013",
    "54323212104",
    "12123234340"
]

s = input()
location = 5
moves = 0
for c in s:
    if c == '0' and location not in [0, 1, 4, 7]:
        moves += int(dist[location][10])
        location = 10
    elif c == '0':
        moves += int(dist[location][0])
        location = 0
    else:
        moves += int(dist[location][int(c)])
        location = int(c)
        
print(moves)
