import math


f = open("pencil.in")
pencilRequired = int(f.readline())

p1 = f.readline().split()
p2 = f.readline().split()
p3 = f.readline().split()

pn1 = math.ceil(pencilRequired/int(p1[0]))
pn2 = math.ceil(pencilRequired/int(p2[0]))
pn3 = math.ceil(pencilRequired/int(p3[0]))

pr1 = int(p1[1])*pn1
pr2 = int(p2[1])*pn2
pr3 = int(p3[1])*pn3

costs = [pr1, pr2, pr3]

sorted_costs = sorted(costs)

with open('pencil.out', 'w') as f_out:
    f_out.write(str(sorted_costs[0]) + '\n')
