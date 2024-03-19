num = input()
for ptn in range(1,101):

    if num in str(ptn):
        print("Clap", end=" ")
    elif ptn % int(num) == 0:
        print("Clap", end=" ")
    else:
        print(ptn, end=" ")

    if ptn % 10 == 0:
        print()
