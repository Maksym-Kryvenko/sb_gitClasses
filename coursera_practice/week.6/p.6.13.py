# max qty of stud from list of school
fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

listOfSchool = []
for row in fin:
    listOfSchool.append(int(row.split()[-2]))

allSchool = [0] * 100

for school in listOfSchool:
    allSchool[school] += 1

maxRes = max(allSchool)

for i in range(len(allSchool)):
    if allSchool[i] == maxRes:
        print(str(i), end=' ', file=fout)

fin.close()
fout.close()
