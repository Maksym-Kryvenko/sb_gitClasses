qty = int(input())

if qty in (1, 21, 31, 41, 51, 61, 71, 81, 91):
    print(qty, 'korova')
elif 2 <= qty <= 4 or 22 <= qty <= 24 or 32 <= qty <= 34 or 42 <= qty <= 44:
    print(qty, 'korovy')
elif 62 <= qty <= 64 or 72 <= qty <= 74 or 82 <= qty <= 84:
    print(qty, 'korovy')
elif 52 <= qty <= 54 or 92 <= qty <= 94:
    print(qty, 'korovy')
else:
    print(qty, 'korov')
