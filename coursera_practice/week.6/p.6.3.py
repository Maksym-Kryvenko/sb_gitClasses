# список из размера диска и кол-ва пользователей
a = list(map(int, input().split()))
# пустой список, он нам пригодится
b = list()
# извлекаем размер диска из списка
s = a[0]
# извлекаем количество пользователей из списка
n = a[1]
# две переменные - счетчик
i = 0
y = 0
# суммарный объем данных пользователей
Sum = 0
# интересующее нас количество пользователей
Users = 0
while i != n:
    c = int(input())
    b.append(c)
    i += 1
for d in b:
    if d > s:
        b.remove(d)
# отсортируем наш список b
e = sorted(b)
# посчитаем, данные скольких пользователей заархивирует админ
while y != len(e):
    Sum += e[y]
    y += 1
    Users += 1
    if Sum >= s:
        Users -= 1
        break
print(Users)
