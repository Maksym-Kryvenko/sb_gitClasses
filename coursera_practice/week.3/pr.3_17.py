str_in = input()

first = str_in.find('h')
second = str_in[::-1].find('h')
second = len(str_in) - second - 1

req_row = 2 * str_in[(first+1):second]
str_in = str_in.replace(str_in[(first+1):second], req_row)
print(str_in)
