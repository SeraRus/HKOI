import sys
def main():
    r = sys.stdin.read()
    sto = []
    for i in r:
        if i in "{[(":
            sto.append(i)
        elif i in "}])":
            if not sto or {"}": "{", "]": "[", ")": "("}[i] != sto.pop():
                return "No"
    if not sto:
        return "Yes"
    else:
        return "No"

print(main())
