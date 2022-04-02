new_list = list(map(int, list(input().split())))


def eq_symbol(new):
    for i in range(1, len(new)):
        if new[i] > 0 and new[i-1] > 0:
            return print(new[i-1], new[i])
        elif new[i] < 0 and new[i-1] < 0:
            return print(new[i-1], new[i])


eq_symbol(new_list)
