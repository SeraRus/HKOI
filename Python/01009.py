while True:
    try:
        Sentence = input()
        Sentence = ''.join([c for c in Sentence if c.isalpha() or c.isspace()])
        print(Sentence)
    except EOFError:
        break
