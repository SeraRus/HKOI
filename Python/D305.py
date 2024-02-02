hkIDs = input()
hkID = list(hkIDs)
if len(hkID) == 7:
    hkID.insert(0, 36)
else:
    hkID[0] = ord(hkID[0]) - 55
hkID[1] = ord(hkID[1]) - 55
hkID = list(map(int, hkID))
s = 11-(9*hkID[0]+8*hkID[1]+7*hkID[2]+6*hkID[3]+5*hkID[4]+4*hkID[5]+3*hkID[6]+2*hkID[7]) % 11
if s == 11:
    print(f"{hkIDs}(0)")
elif s == 10:
    print(f"{hkIDs}(A)")
else:
    print(f"{hkIDs}({s})")
