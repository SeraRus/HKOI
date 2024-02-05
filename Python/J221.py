busRoute = input()
busRoute = list(busRoute)
ptA = False
ptD = False
if busRoute[0].isalpha():
    ptA = busRoute.pop(0)
if busRoute[-1].isalpha():
    ptD = busRoute.pop(-1)
ptBC = "".join(busRoute).rjust(3, " ")
ptB = ptBC[0]
ptC = ptBC[1]


def bus_pt_a(pt):
    if not pt:
        return "Normal"
    elif pt == "A":
        return "Airport"
    elif pt == "B":
        return "Border"
    elif pt == "N":
        return "Overnight"
    else:
        return False


def bus_pt_b(pt):
    if pt == " ":
        return "Normal"
    elif pt == "1":
        return "Cross River"
    elif pt == "2":
        return "Air-conditioned"
    elif pt == "3":
        return "Holiday"
    else:
        return False


def bus_pt_c(pt):
    if pt in " 012":
        return "Downtown"
    elif pt in "34":
        return "West District"
    elif pt == "7":
        return "North District"
    elif pt == "9":
        return "East District"
    else:
        return False


def bus_pt_d(pt):
    if not pt:
        return "Normal"
    if pt in "ABC":
        return "Normal"
    elif pt == "P":
        return "Peak Hour"
    elif pt == "S":
        return "Special"
    elif pt == "X":
        return "Express"
    else:
        return False


ptA = bus_pt_a(ptA)
ptB = bus_pt_b(ptB)
ptC = bus_pt_c(ptC)
ptD = bus_pt_d(ptD)


def out_put(a, b, c, d):
    if a == "Overnight" and d == "Peak Hour":
        return "Invalid"
    if b == "Holiday" and d == "Peak Hour":
        return "Invalid"
    if not a or not b or not c or not d:
        return "Invalid"
    if a == b == d == "Normal":
        return f"{c} Normal"
    lis = [c, b, d, a]
    lis = [string for string in lis if string != "Normal"]
    op = ""
    for u in lis:
        op += f"{u} "
    op = op[:-1]
    return op


print(out_put(ptA, ptB, ptC, ptD))
