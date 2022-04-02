def is_un_l1(x, y):
    return y <= -x


def is_up_l1(x, y):
    return y >= -x


def is_un_l2(x, y):
    return y <= 2*x + 2


def is_up_l2(x, y):
    return y >= 2*x + 2


def is_in_c(x, y):
    return (x+1)**2 + (y-1)**2 <= 4


def is_out_of_c(x, y):
    return (x + 1) ** 2 + (y - 1) ** 2 >= 4


def is_point_in_area(x, y):
    if is_up_l1(x, y) and is_up_l2(x, y) and is_in_c(x, y):
        return 'YES'
    elif is_un_l1(x, y) and is_un_l2(x, y) and is_out_of_c(x, y):
        return 'YES'
    return 'NO'


print(is_point_in_area(float(input()), float(input())))
