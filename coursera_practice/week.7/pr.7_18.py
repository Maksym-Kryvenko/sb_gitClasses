f_in = open('input.7_18.txt', 'r', encoding='utf8')

words = dict()
for row in f_in:
    fit_row = row.strip().split()
    for word in fit_row:
        words[word] = words.get(word, 0) + 1

temp = sorted(words, key=lambda item: (-words[item], item))
for i in temp:
    print(i)
