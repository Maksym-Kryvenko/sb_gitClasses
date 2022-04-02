str_in = input()

first = str_in.find('h')
second = str_in[::-1].find('h')
second = len(str_in) - second - 1

str_in_new = str_in[(first+1):second]
medium = str_in_new.replace('h', 'H')
print(str_in[0:(first+1)] + medium + str_in[second:])
