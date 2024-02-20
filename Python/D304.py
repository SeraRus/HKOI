word = input()
show = ['_'] * len(word)
word = list(word)
while True:
    guess = input()
    for i in range(len(word)):
        if guess == word[i]:
            show[i] = guess
    print(''.join(show))
    if word == show:
        break
