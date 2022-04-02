str_in = input()

first = str_in.find('f')
second = str_in[::-1].find('f')
second = len(str_in) - second - 1

if first != -1 and second != -1 and second != first:
    print(first, second)
elif first != -1 and second != -1 and second == first:
    print(first)
