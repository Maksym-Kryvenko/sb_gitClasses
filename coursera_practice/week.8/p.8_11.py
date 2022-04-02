# Выведите все простые на отрезке [2;n].

import math

print(
    *([2] + list(
        filter(
            lambda x: all(
                map(
                    lambda y: x % y != 0,
                    range(3, round(math.sqrt(x)) + 1, 2)
                )
            ),
            range(3, int(input()) + 1, 2))
        )
      )
)
