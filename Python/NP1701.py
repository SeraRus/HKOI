with open('score.in','r') as f:
    s=list(map(int, f.read().split(" ")))

with open('score.out','w+') as f:
    f.write(str(round(a*0.2+b*0.3+c*0.5)))
