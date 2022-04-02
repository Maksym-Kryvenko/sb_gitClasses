my_list = list(map(int, input().split()))
qty_max = 0
value_max = my_list[0]

for value in my_list:
    qty = my_list.count(value)
    if qty > qty_max:
        qty_max, value_max = qty, value

print(value_max)
