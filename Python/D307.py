L1 = input()
L2 = input()
L3 = input()

if L1 == "XXX" or L2 == "XXX" or L3 == "XXX":
  print("X wins")
elif L1 == "OOO" or L2 == "OOO" or L3 == "OOO":
  print("O wins")
elif L1[0]=="X" and L2[0]=="X" and L3[0]=="X":
  print("X wins")
elif L1[1]=="X" and L2[1]=="X" and L3[1]=="X":
  print("X wins")
elif L1[2]=="X" and L2[2]=="X" and L3[2]=="X":
  print("X wins")
elif L1[0]=="O" and L2[0]=="O" and L3[0]=="O":
  print("O wins")
elif L1[1]=="O" and L2[1]=="O" and L3[1]=="O":
  print("O wins")
elif L1[2]=="O" and L2[2]=="O" and L3[2]=="O":
  print("O wins")
elif L1[0]=="O" and L2[1]=="O" and L3[2]=="O":
  print("O wins")
elif L1[2]=="O" and L2[1]=="O" and L3[0]=="O":
  print("O wins")
elif L1[0]=="X" and L2[1]=="X" and L3[2]=="X":
  print("X wins")
elif L1[2]=="X" and L2[1]=="X" and L3[0]=="X":
  print("X wins")
elif "." in L1 or "." in L2 or "." in L3:
  print("Not ended")
else:
  print("Draw")
