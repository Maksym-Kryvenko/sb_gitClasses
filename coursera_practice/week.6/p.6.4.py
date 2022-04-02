def second(q):
    return q[1]


nsel = int(input())  # вводим количество селений
a = list(map(int, input().split()))  # вводим расстояния до селений
a1 = []
for i in range(nsel):
    # создаем новый список селений для сортировки по расстояниям
    # i-порядкойвый номер селения, a[i]-расстояние,
    # 3-е измерение списка для расстояний до бомбоубежищ
    a1.append([i, a[i], 0])
a1.sort(key=second)  # сортируем по расстояниям
mbomb = int(input())
b = list(map(int, input().split()))
b1 = []
for i in range(mbomb):
    # создаем новый список селений для сортировки по расстояниям
    # i-порядкойвый номер убежища, b[i]-расстояние
    b1.append([i, b[i]])   # сортируем по расстояниям
b1.sort(key=second)

j = 0
for i in range(nsel):
    rasst = abs(a1[i][1] - b1[j][1])
    # расстояние от текущего селения до убежища
    # сравниваем расстояние от текущего селения до убежищ
    # усли убежища не закончились и
    # расстояние до следующего убежища меньше
    while j < len(b1)-1 and \
            rasst > abs(a1[i][1] - b1[j+1][1]):
        j += 1
        rasst = abs(a1[i][1] - b1[j][1])
        # запоминаем минимальное расстояние
    else:
        a1[i][2] = b1[j][0] + 1
        # записываем номер убещища, до которого минимальное расстоние

a1.sort()  # сортируем обратно по порядку
# первоначального ввода селений (по их порядковому номеру)
i = 0
for i in range(0, nsel):
    print(a1[i][2], end=' ')