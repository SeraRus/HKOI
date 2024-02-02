def fast_exponentiation(B, P, M):
    result = 1

    while P > 0:
        if P % 2 == 1:
            result = (result * B) % M
        B = (B * B) % M
        P //= 2

    return result

B = int(input())
P = int(input())
M = int(input())

result = fast_exponentiation(B, P, M)
print(result)
