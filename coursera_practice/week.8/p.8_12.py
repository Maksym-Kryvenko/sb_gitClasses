# Перед началом тараканьих бегов всем болельщикам было предложено сделать по две ставки на результаты бегов.
# Каждая ставка имеет вид "Таракан №A придет раньше, чем таракан №B". Организаторы бегов решили выяснить,
# могут ли тараканы прийти в таком порядке, чтобы у каждого болельщика сыграла ровно одна ставка из двух
# (то есть чтобы ровно одно из двух утверждений каждого болельщика оказалось верным).
# Считается, что никакие два таракана не могут прийти к финишу одновременно.

import itertools
import operator

print(next(map(lambda a:
               ' '.join(map(str, a[0])),
               filter(lambda a: all(map(lambda b: operator.xor(
                   *map(lambda c: c in itertools.combinations(a[0], 2), b, )),
                   a[1])), (
                   lambda a, b: zip(itertools.permutations(a),
                                    itertools.repeat(b)))(
                   *(lambda k, n: (range(1, k + 1),
                                   tuple(map(lambda i: (i[:2], i[2:]),
                                             map(lambda _: tuple(
                                                 map(int, input().split())),
                                                 range(n)))))
                     )(*map(int, input().split()))))), 0))
