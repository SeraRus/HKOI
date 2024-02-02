heights = input().split()


heights = [int(h) for h in heights]


with open("chart.txt", "w") as file:
    file.write("+-------------------------+\n")

    for i in range(10):
        file.write("| ")
        for j in range(6):
            if heights[j] >= 10 - i:
                file.write("### ")
            else:
                file.write("    ")
        file.write("|\n")

    file.write("+-------------------------+\n")
