def min4(a, b, c, d):
    list4 = [a, b, c, d]
    res_min = list4[0]
    for i in range(len(list4) - 1):
        res_min_cur = min(list4[i], list4[i + 1])
        res_min = min(res_min, res_min_cur)
    return res_min


print(min4(int(input()), int(input()),
           int(input()), int(input())))
