a, b, c, d = int(input()), int(input()), int(input()), int(input())
if d > b and (a + b + c + d) % 2 == 0 and (d - b) ** 2 >= (a - c) ** 2:
    print('YES')
else:
    print('NO')
