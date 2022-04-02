# По заданному на входе числу 0≤n≤2000 выведите последовательность факториалов:
# 0!,1!,2!,…,n!

from math import factorial

print(
    *map(
        lambda x: factorial(x),
        range(
            int(input()) + 1
        )
    )
)

# 2 variant
# print(1, *accumulate(range(1, int(input()) + 1), lambda x, y: x * y))

# 3 variant
# print(*map(lambda x: reduce(lambda a, z: a * z, range(1, x + 1), 1), range(int(input()) + 1)))
