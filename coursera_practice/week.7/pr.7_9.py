f_IN = open('input.txt', 'r', encoding='utf8')

studs = int(f_IN.readline())  # qty of students
list_lang = []
for i in range(studs):
    qty_lang = int(f_IN.readline())
    new_set = set()
    for j in range(qty_lang):
        new_set.add(f_IN.readline().strip())
    list_lang.append(new_set)

f_IN.close()

every = set(list_lang[0])
some_all = set(list_lang[0])

for i in list_lang[1:]:
    every &= i
    some_all |= i

print(len(every), *sorted(every), sep='\n')
print(len(some_all), *sorted(some_all), sep='\n')
