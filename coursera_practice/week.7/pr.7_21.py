# buyers - goods - qty
f_in = open('input.7_21.txt', 'r', encoding='utf8')
f_out = open('output.7_21.txt', 'w', encoding='utf8')

user_data = dict()
for row in f_in:
    el = row.strip().split()
    if el[0] in user_data.keys():
        user_data[el[0]][el[1]] = user_data[el[0]].get(el[1], 0) +\
                                  int(el[2])
    else:
        temp = dict()
        temp[el[1]] = int(el[2])
        user_data[el[0]] = temp

f_in.close()

for user in sorted(user_data):
    print(user + ':', file=f_out)
    for good in sorted(user_data[user]):
        print(good, user_data[user][good], file=f_out)

f_out.close()
