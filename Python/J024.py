from statistics import mean, median, mode

n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

mean_value = round(mean(data), 3)
median_value = median(data)
mode_value = mode(data)

if isinstance(median_value, int):
    median_value = int(median_value)
else:
    median_value = round(median_value, 1)

print(format(mean_value, ".3f"))
if int(median_value) == median_value:
    print(int(median_value))
else:
    print(format(median_value, ".1f"))
print(mode_value)
