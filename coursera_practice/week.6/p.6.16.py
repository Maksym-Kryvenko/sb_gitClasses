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

total_votes = sum(votes_dic.values())
for key in votes_dic.keys():
    # qty of party should be > 7%
    if votes_dic[key]/total_votes >= 0.07:
        print(key)
