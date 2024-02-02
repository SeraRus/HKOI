from collections import Counter

numbers = []
for _ in range(int(input())):
    numbers.append(float(input()))

counter = Counter(numbers)
modes = counter.most_common()
max_count = modes[0][1]
modes = [num for num, count in modes if count == max_count]
sorted_modes = sorted(modes)

for num in sorted_modes:
    print(format(num, "6.2f"))
