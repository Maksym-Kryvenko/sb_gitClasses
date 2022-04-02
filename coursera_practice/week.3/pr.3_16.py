str_in = input()

first = str_in.find('h')
second = str_in[::-1].find('h')
second = len(str_in) - second - 1

str_in = str_in.replace(str_in[first:(second+1)], '')
print(str_in)
