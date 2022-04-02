def kvadrat(counter):
    n = int(input())
    if n != 0:
        counter = kvadrat(counter)
        if (int(n ** 0.5)) ** 2 == n:
            print(n)
            return counter + 1
        return counter
    return 0


if kvadrat(0) == 0:
    print(0)
