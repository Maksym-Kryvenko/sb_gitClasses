A = int(input())
B = int(input())
while A > B:
    if A % 2 != 0 or A // 2 < B:
        A -= 1
        print('-1')
    if A // 2 >= B:
        A = A // 2
        print(':2')
