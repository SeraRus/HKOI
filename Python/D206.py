N = int(input())
print(N)
while N !=1:
  if N%2 == 0:
    N=N/2
  else:
    N=N*3+1
  print(int(N))
