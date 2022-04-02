f_in = open('input.7_19.txt', 'r', encoding='utf8')
f_out = open('output.7_19.txt', 'w', encoding='utf8')

votes = dict()
for row in f_in:
    cleaned = row.strip()
    votes[cleaned] = votes.get(cleaned, 0) + 1

f_in.close()


def l_sort(item):
    return -votes[item]


if (max(votes.values()) / sum(votes.values())) > 0.5:
    print(sorted(votes.keys(), key=l_sort)[0], file=f_out)
else:
    print(sorted(votes.keys(), key=l_sort)[0], file=f_out)
    print(sorted(votes.keys(), key=l_sort)[1], file=f_out)

f_out.close()
