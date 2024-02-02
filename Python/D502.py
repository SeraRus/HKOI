with open('weather.txt', 'r') as f:
    lines = f.readlines()
    temps = []
    for line in lines:
        temp = int(line.split()[-2])
        temps.append(temp)
    print(min(temps), max(temps))
