Time = input()
TimeHour, TimeMinute = map(int, Time.split(" "))
TZone = input()
CZone = input()

TSetZone = {"PST": ["-", 8, 0], "MST": ["-", 7, 0], "EST": ["-", 5, 0],
            "GMT": ["+", 0, 0], "MSK": ["+", 3, 0], "IST": ["+", 5, 30],
            "NPT": ["+", 5, 45], "HKT": ["+", 8, 0], "JST": ["+", 9, 0],
            "ACDT": ["+", 10, 30]}

if TSetZone[TZone][0] == "+":
    TimeHour -= TSetZone[TZone][1]
    TimeMinute -= TSetZone[TZone][2]
else:
    TimeHour += TSetZone[TZone][1]
    TimeMinute += TSetZone[TZone][2]

if TSetZone[CZone][0] == "+":
    TimeHour += TSetZone[CZone][1]
    TimeMinute += TSetZone[CZone][2]
else:
    TimeHour -= TSetZone[CZone][1]
    TimeMinute -= TSetZone[CZone][2]

if TimeMinute < 0:
    TimeMinute += 60
    TimeHour -= 1

if TimeMinute >= 60:
    TimeMinute -= 60
    TimeHour += 1

if TimeHour < 0:
    TimeHour += 24

if TimeHour >= 24:
    TimeHour -= 24

if TimeMinute < 10:
    TimeMinute = f"0{str(TimeMinute)}"

if TimeHour < 10:
    TimeHour = f"0{str(TimeHour)}"

print(f"{TimeHour} {TimeMinute}")
