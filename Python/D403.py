from collections import Counter

def can_form_word(s_counter, word):
    word_counter = Counter(word)
    for letter, count in word_counter.items():
        if count > s_counter[letter]:
            return False
    return True

s = input().strip()
m = int(input())

s_counter = Counter(s)

for i in range(m):
    word = input().strip()
    if can_form_word(s_counter, word):
        print("Yes")
    else:
        print("No")
