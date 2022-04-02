# фамилия имя класс (9, 10, 11) балл (0..100)
fin = open('input.txt', 'r', encoding='utf8')
# баллы победителей в 9, 10, 11 классах

maxList = [0] * 3

marks9 = []  # list of marks for 9 class
marks10 = []
marks11 = []

for row in fin:
    rowList = list(row.split())
    if int(rowList[3]) > maxList[int(rowList[2]) - 9]:
        maxList[int(rowList[2]) - 9] = int(rowList[3])  # define max

    if int(rowList[2]) == 9:
        marks9.append(int(rowList[3]))
    elif int(rowList[2]) == 10:
        marks10.append(int(rowList[3]))
    elif int(rowList[2]) == 11:
        marks11.append(int(rowList[3]))

marks = [marks9, marks10, marks11]


def total_amount(x, maxim):
    return x.count(maxim)


for val, maxus in zip(marks, maxList):
    print(total_amount(val, maxus), end=' ')


fin.close()
