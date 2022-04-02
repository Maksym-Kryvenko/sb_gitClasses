f_in = open('input.7_17.txt', 'r', encoding='utf8')

words = dict()
for row in f_in:
    row_clean = row.strip().split()
    for word in row_clean:
        words[word] = words.get(word, 0) + 1

print(sorted(words, key=lambda item: (-words[item], item))[0])
