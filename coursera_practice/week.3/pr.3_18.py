str_in = input()

first = str_in.find('f')
second = str_in.find('f', (first+1))

if first != -1 and second != -1:
    print(second)
elif first != -1 and second == -1:
    print(-1)
elif first == -1:
    print(-2)
