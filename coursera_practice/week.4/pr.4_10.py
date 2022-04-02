def is_prime(a):
    i = 2
    if a == 1:
        return True
    else:
        while i <= a**0.5:
            if a % i == 0:
                return False
            else:
                i = i + 1
        return True


if is_prime(int(input())):
    print('YES')
else:
    print('NO')
