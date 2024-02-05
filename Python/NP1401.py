with open('count.in', 'r') as f:
    n = int(f.readline())
    num_list = set(map(int, f.readline().split()))

count = len(set(a+b for a in num_list for b in num_list if a!=b).intersection(num_list))

with open('count.out', 'w') as f:
    f.write(str(count))
