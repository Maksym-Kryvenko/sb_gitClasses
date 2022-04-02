# find the 2nd res in each class
fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

results = {'9': [], '10': [], '11': []}

for row in fin:
    class_stud = row.split()[-2]
    score_stud = int(row.split()[-1])
    results[class_stud].append(score_stud)


def second_score(inpt):
    sort_list = sorted(inpt, reverse=True)
    max_st = sort_list[0]
    for val in sort_list:
        if val != max_st:
            print(str(val), end=' ', file=fout)
            break


for it in results.values():
    second_score(it)

fin.close()
fout.close()
