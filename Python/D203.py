s = int(input())
n = 1
t = 0
t2 = 0
while t != 100:
  if t2 == 10:
    print("")
    t2 = 0
  else:
    pass
  t2=t2+1
  if n % s == 0:
    print("Clap ",end = "")
  else:
    n1=str(n)
    s1=str(s)
    if s1 in n1:
      print("Clap ",end = "")
    else:
      print(f"{n} ",end = "")
  t=t+1
  n=n+1
