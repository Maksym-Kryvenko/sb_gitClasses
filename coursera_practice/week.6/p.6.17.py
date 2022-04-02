f_in = open('input.txt', 'r', encoding='utf8')
f_out = open('output.txt', 'w', encoding='utf8')

votes_dic = {}
f_in.readline()
for row in f_in:  # list of parties
    row_spl = row.split()
    if row_spl[-1] != 'VOTES:':
        votes_dic[row.strip()] = 0
    else:
        break

for row in f_in:  # qty votes per parties
    for key in votes_dic.keys():
        if row.strip() == key:
            votes_dic[key] += 1


def key_qty(a):
    return -a[1]  # a - tuple return(-a[1], a[0])


list_from_dic = []
for i, j in votes_dic.items():
    list_from_dic.append([i, j])    # make it tuple

list_from_dic.sort()
list_from_dic.sort(key=key_qty)  # if solve via tuple - use one sort

for i in list_from_dic:
    print(i[0], file=f_out)
