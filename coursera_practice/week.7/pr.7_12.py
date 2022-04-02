f_in = open('input.txt', 'r', encoding='utf8')


def clean_row(wta):
    waste = {'-', '(', ')'}
    for i in waste:
        if i in wta:
            wta = wta.replace(i, '')
    return wta


def contact_list(raw_number):
    if len(raw_number) > 7:
        return {raw_number[-7:], raw_number[-10:-7]}
    elif len(raw_number) == 7:
        return {raw_number[-7:], '495'}


key, phone_dict = 0, {}
for row in f_in:
    phone_dict[key] = contact_list(clean_row(row.strip()))
    key += 1

for key in phone_dict:
    if key == 0:
        pass
    else:
        if phone_dict[0] == phone_dict[key]:
            print('YES')
        else:
            print('NO')
