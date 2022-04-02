num = float(input())

n_num = int(num)
rest = num - n_num
if rest >= 0.5:
    print(n_num + 1)
else:
    print(n_num)
