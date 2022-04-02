from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, object, other):
        self.matrix1 = object
        self.matrix2 = other


class Matrix:
    @staticmethod
    def transposed(obj):
        return Matrix([[obj.arr[j][i] for j in range(len(obj.arr))]
                       for i in range(len(obj.arr[0]))])

    def __init__(self, arr):
        self.arr = deepcopy(arr)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, line)) for line in self.arr)

    def __add__(self, other):
        if len(self.arr) == len(other.arr):
            return Matrix([[self.arr[i][j]+other.arr[i][j]
                            for j in range(len(self.arr[0]))]
                           for i in range(len(self.arr))])
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([list(map(
                lambda x: x * other, self.arr[i]))
                for i in range(len(self.arr))])
        elif isinstance(other, Matrix):
            if self.size()[1] != other.size()[0]:
                raise MatrixError(self, other)
            return Matrix(
                list(map(
                    lambda x: list(
                        map(
                            lambda y: sum(map(
                                lambda z: z[0] * z[1],
                                zip(x, y))
                            ),
                            zip(*other.arr))),
                    zip(*Matrix.transposed(self).arr))
                )
            )

    __rmul__ = __mul__

    def transpose(self):
        self.arr = [[self.arr[j][i] for j in range(len(self.arr))]
                    for i in range(len(self.arr[0]))]
        return Matrix(self.arr)

    def size(self):
        return (len(self.arr), len(self.arr[0]))


exec(stdin.read())
