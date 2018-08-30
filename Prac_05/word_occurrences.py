word_bank = {}
text = input("Text:")
words = text.split()
for word in words:
    word_bank[word] = word_bank.get(word, 0) + 1  # Reference: Silde 18
words = list(word_bank.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_bank[word]))
