def is_ascending(x):
    i = len(x)-1
    while x[i] > x[i - 1]:
        i -= 1
    print('YES' * (not bool(i)), 'NO' * bool(i))


new_list = list(map(int, list(input().split())))

is_ascending(new_list)
