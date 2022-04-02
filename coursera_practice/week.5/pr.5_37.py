in_list = list(map(int, input().split()))
max0 = in_list.pop(in_list.index(max(in_list)))
min1 = in_list.pop(in_list.index(min(in_list)))
min2 = min(in_list)
max1 = in_list.pop(in_list.index(max(in_list)))
if len(in_list) > 0:
    max2 = max(in_list)
else:
    max2 = min1
if max1 * max2 * max0 >= min1 * min2 * max0:
    print(max2, max1, max0)
else:
    print(min1, min2, max0)
