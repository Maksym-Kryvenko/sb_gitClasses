f_in = open('input.7_14.txt', 'r', encoding='utf8')

qty = tuple()
dict_count = dict()
for row in f_in:
    for word in row.strip().split():
        if word in dict_count.keys():
            qty += tuple(str(dict_count[word]))
            dict_count[word] += 1
        else:
            qty += tuple(str(0))
            dict_count[word] = 1

print(*qty)
