# Произведение пятых степеней ряда чисел

from sys import stdin
from functools import reduce

print(
    reduce(
        lambda a, b: a * b,
        map(
            lambda x: x**5,
            map(
                int, stdin.read().strip().split()
            )
        )
    )
)
