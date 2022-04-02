f_IN = open('input.7_15.txt', 'r', encoding='utf8')
pairs_qty = int(f_IN.readline())

pairs = dict()
for i in range(pairs_qty):
    pairs[i] = f_IN.readline().split()

word = f_IN.readline().strip()

f_IN.close()

for j in pairs.values():
    if word in j and j[0] != j[1]:
        print(*set(j) - {word})
    elif word in j and j[0] == j[1]:
        print(*set(j))
