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


exec(stdin.read())
