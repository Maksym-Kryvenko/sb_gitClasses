n = int(input())
# количество клавиш на клавиатуре.
allowQTYList = list(map(int, input().split()))
# количество нажатий,выдерживаемых i-ой клавишей.
k = int(input())
# общее количество нажатий клавиш
pressOrderList = list(map(int, input().split()))
# последовательность нажатых клавиш.

for value in pressOrderList:
    allowQTYList[value-1] -= 1
    # print(cntMarks)
for value in allowQTYList:
    if value < 0:
        print('YES')
    else:
        print('NO')

# Программа должна вывести n строк,
# содержащих информацию об исправности клавиш
# Если i-я клавиша сломалась,
# то i-ая строка должна содержать слово YES,
# если же клавиша работоспособна — слово NO.
