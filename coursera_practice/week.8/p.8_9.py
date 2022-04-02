# По данному числу N выведите все перестановки чисел от 1 до N в лексикографическом порядке.

import itertools
import functools

print(
    *map(
        lambda x: functools.reduce(
            lambda a, b: str(a) + str(b), x
        ),
        itertools.permutations(
            map(
                int,
                range(1, int(input()) + 1)
            )
        )
    ),
    sep='\n'
)

# 2 var
# print(*map(''.join, permutations(map(str, range(1, int(input()) + 1)))), sep='\n')

# 3 var
# list(map(lambda x: print(*x, sep=""), permutations(range(1, int(input())+1))))
