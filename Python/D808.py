exet = 0
input()
a = list(map(int, input().split()))


def lomuto(b, l, r):
    global exet
    exet += r - l + 1
    if l >= r:
        return
    a = b
    p = a[r]
    i = l
    for j in range(l, r):
        if a[j] <= p:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[r], a[i] = a[i], a[r]
    return i

def rlom(n, l, r):
    i = lomuto(n, l, r)
    if i is None:
        return
    rlom(n, l, i-1)
    rlom(n, i+1, r)


rlom(a, 0, len(a) - 1)
print(' '.join(map(str, a)))
print(exet)
