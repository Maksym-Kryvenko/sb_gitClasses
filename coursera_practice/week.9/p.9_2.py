from sys import stdin
from copy import deepcopy


class Matrix:

    def __init__(self, input_list):
        self.new_list = deepcopy(input_list)

    def __str__(self):
        all_strings = ''
        for element in self.new_list:
            string = '\t'.join([str(i) for i in element])
            all_strings += string + '\n'
        return all_strings[:-1]

    def size(self):
        return len(self.new_list), len(self.new_list[0])

    def __add__(self, other):
        new_input_list = []
        for i in range(len(self.new_list)):
            line = list(map(lambda x, y: x + y, self.new_list[i],
                            other.new_list[i]))
            new_input_list.append(line)
        return Matrix(new_input_list)

    def __mul__(self, other):
        all_strings = ''
        for element in self.new_list:
            string = '\t'.join([str(other * i) for i in element])
            all_strings += string + '\n'
        return all_strings[:-1]

    def __rmul__(self, other):
        return Matrix.__mul__(self, other)


exec(stdin.read())
