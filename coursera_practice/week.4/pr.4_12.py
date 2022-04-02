def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        a_res = 1
        for i in range(n):
            a_res *= a
        return a_res
    else:
        a_res = 1
        for i in range(abs(n)):
            a_res *= (1/a)
        return a_res


print(power(float(input()), int(input())))
