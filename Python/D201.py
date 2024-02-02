Times = int(input())
if Times == 0:
  print(0)
elif Times == 1:
  print(1)
else:
  Times = Times - 1
  OldNumber = 0
  NewNumber = 1
  for i in range(Times):
  	PrintNumber = OldNumber + NewNumber
  	OldNumber = NewNumber
  	NewNumber = PrintNumber
  print(PrintNumber)
