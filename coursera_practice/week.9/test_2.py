f_in = open('input.txt', 'r', encoding='utf8')
data = dict()
num = 0

for row in f_in:
    num += 1
    elms = row.strip().split()
    for e in range(len(elms)):
        data[str(num)+str(e+1)] = elms[e]

print(data)

data_T = dict()

for i in data.keys():
    index = str(i[1] + i[0])
    data_T[index] = data[i]

data_Tm = sorted(data_T.items())
print(data_Tm)
