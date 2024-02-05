import sys

sys.set_int_max_str_digits(1000000)

N = input()

digits = list(N)

smallest = sorted(digits)

for i in range(len(smallest)):
    if smallest[i] != '0':
        index = i
        break

smallest[0], smallest[index] = smallest[index], smallest[0]

smallest = ''.join(smallest)


largest = ''.join(sorted(digits, reverse=True))

print(largest)
print(smallest)
