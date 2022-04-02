f_in = open('input.7_16.txt', 'r', encoding='utf8')

votes = dict()
for row in f_in:
    state_vote = row.strip().split()
    if state_vote[0] in votes.keys():
        votes[state_vote[0]] += int(state_vote[1])
    else:
        votes[state_vote[0]] = int(state_vote[1])

for name in sorted(votes):
    print(' '.join([name, str(votes[name])]))
