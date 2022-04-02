def min_divisor(n):
    divisor = 1
    while divisor <= n**0.5:
        divisor += 1
        if n % divisor == 0:
            return divisor
    return n


print(min_divisor(int(input())))
