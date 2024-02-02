word = input()
a = ' '
ws = a.join(word)
wsl = ws.split(' ')
udl = ["_"for value in range(1, len(word)+1)]
pos = 0
while wsl != udl:
  pos = 0
  s = input()
  for c in wsl:
    if s == c:
      udl[pos] = s
    pos += 1
  for b in udl:
      print(b,end="")
  print("")
