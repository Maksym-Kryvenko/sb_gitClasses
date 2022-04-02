l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())
l1, w1 = max(l1, w1), min(l1, w1)
l2, w2 = max(l2, w2), min(l2, w2)
lc, wc = max(lc, wc), min(lc, wc)
if h1 > hc or h2 > hc or l1 > lc or l2 > lc or w1 > wc or w2 > wc:
    print('NO')  # ящик не пролезает хотя бы по одному размеру
elif l1 + l2 <= lc or w1 + w2 <= wc or h1 + h2 <= hc:
    print('YES')              # можно поставить оба вдоль или один на другой
elif l1 + w2 <= lc and (l2 <= wc or l1 <= wc):    # один вдоль, другой поперек
    print('YES')
elif w1 + w2 <= lc and l1 <= wc and l2 <= wc:
    print('YES')                    # оба поперек
else:                    # ящик не пролезает хотя бы по одному размеру
    print('NO')
