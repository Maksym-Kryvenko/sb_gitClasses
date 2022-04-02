f_in = open('input.txt', 'r', encoding='utf-8')
k = int(f_in.readline())

in_list = []
for row in f_in:
    a_splt = row.split()
    po1 = int(a_splt[-3])
    po2 = int(a_splt[-2])
    po3 = int(a_splt[-1])
    if po1 >= 40 and po2 >= 40 and po3 >= 40:
        in_list.append(po1 + po2 + po3)

f_in.close()

in_list.sort(reverse=True)

f_out = open('output.txt', 'w', encoding='utf-8')

if len(in_list) <= k or k == 0:
    print(0, file=f_out)
else:
    if in_list[k - 1] == in_list[k]:
        d = k - 1
        while d > 0 and in_list[d - 1] == in_list[d]:
            d = d - 1
        if d == 0:
            print(1, file=f_out)
        else:
            print(in_list[d - 1], file=f_out)
    else:
        print(in_list[k - 1], file=f_out)

f_out.close()
