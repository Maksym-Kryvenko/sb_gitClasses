# Контрольная по ударениям
f_in = open('input.txt', 'r', encoding='utf8')

error = 0
dictionary = set()
dictionary_low = set()
n = int(f_in.readline())
for i in range(n):
    line = f_in.readline().strip()
    dictionary.add(line)
    dictionary_low.add(line.lower())
line = f_in.readline().strip().split()
for word in line:
    if word not in dictionary:
        if word.lower() in dictionary_low:
            error += 1
        else:
            k = 0
            for x in word:
                if x.isupper():
                    k += 1
            if k != 1:
                error += 1
print(error)

# в словах, которых нет в словаре
# он будет считать, что Петя поставил ударения правильно
# если в этом слове Петей поставлено ровно одно ударение

# Оказалось, что в некоторых словах ударение может быть поставлено больше
# чем одним способом. Вася решил, что в этом случае если то
# как Петя поставил ударение, соответствует одному из приведенных
# в словаре вариантов, он будет засчитывать это как правильную
# расстановку ударения, а если не соответствует, то как ошибку
