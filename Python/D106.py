n=input()
n="0"+n
if n[-2]=="1":
  print(f"{int(n)}th")
elif n[-1]=="1":
  print(f"{int(n)}st")
elif n[-1]=="2":
  print(f"{int(n)}nd")
elif n[-1]=="3":
  print(f"{int(n)}rd")
else:
  print(f"{int(n)}th")
