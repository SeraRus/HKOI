import math

cyan, magenta, yellow, black, red, green, blue = map(int, input().split(" "))

cmBlue = cyan + magenta
myRed = magenta + yellow
cyGreen = cyan + yellow

cmyBlack = cyan + magenta + yellow
rgbBlack = red + green + blue
crBlack = cyan + red * 2
mgBlack = magenta + green * 2
ybBlack = yellow + blue * 2

threeBlack = [cmyBlack, rgbBlack, crBlack, mgBlack, ybBlack]
threeBlack.sort()
threeBlack = threeBlack[0]

if cmBlue > blue * 2:
    cmBlue = blue * 2
if myRed > red * 2:
    myRed = red * 2
if cyGreen > green * 2:
    cyGreen = green * 2
if threeBlack > black * 3:
    threeBlack = black * 3

num, colour = input().split(" ")
num = int(num)
if colour == "red":
    if math.ceil(num / 2) * myRed < (num // 2) * myRed + (num % 2) * red:
        print(math.ceil(num / 2) * myRed)
    else:
        print((num // 2) * myRed + (num % 2) * red)
elif colour == "blue":
    if math.ceil(num / 2) * cmBlue < (num // 2) * cmBlue + (num % 2) * blue:
        print(math.ceil(num / 2) * cmBlue)
    else:
        print((num // 2) * cmBlue + (num % 2) * blue)
elif colour == "green":
    if math.ceil(num / 2) * cyGreen < (num // 2) * cyGreen + (num % 2) * green:
        print(math.ceil(num / 2) * cyGreen)
    else:
        print((num // 2) * cyGreen + (num % 2) * green)
elif colour == "black":
    if math.ceil(num / 3) * threeBlack < (num // 3) * threeBlack + (num % 3) * black:
        print(math.ceil(num / 3) * threeBlack)
    else:
        print((num // 3) * threeBlack + (num % 3) * black)
else:
    print(locals().get(colour) * num)
