with open('title.in', 'r') as f:
    title = f.readline().strip()

title_length = str(len(title.replace(" ", "")))

with open('title.out', 'w') as f:
    f.write(title_length)
