shortForm = input()
guessNum = int(input())


def guess(guess_sentence, short_form_guess):
    short_form_guess = short_form_guess.lower()
    guess_sentence = guess_sentence.lower().split(" ")
    short_form_guess = list(short_form_guess)

    if len(guess_sentence) < len(short_form_guess):
        return "No :("
    x = 0
    lis = []
    for u in range(len(guess_sentence)):
        if guess_sentence[u][0] == short_form_guess[x]:
            lis.append(u)
            x += 1
        if x > len(short_form_guess)-1:
            break

    if len(lis) < len(short_form_guess):
        return "No :("
    
    for v in lis:
        guess_sentence[v] = guess_sentence[v].capitalize()

    back = " ".join(guess_sentence)
    return back


for i in range(guessNum):
    print(guess(input(), shortForm))
