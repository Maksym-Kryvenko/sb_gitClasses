# фамилия имя класс (9, 10, 11) балл (0..100)
fin = open('fin_6_9.txt', 'r', encoding='utf8')
# баллы победителей в 9, 10, 11 классах

maxList = [0] * 3
for row in fin:
    rowList = list(row.split())
    if int(rowList[3]) > maxList[int(rowList[2]) - 9]:
        maxList[int(rowList[2]) - 9] = int(rowList[3])
    # print(rowList)

print(*maxList)

fin.close()
