my_list = list(map(int, input().split()))

# non zero left
zero = my_list.count(0)
l_list = len(my_list)
l_list_def = l_list
i = 0

while l_list > (l_list_def - zero):
    if my_list[i] == 0:
        my_list.pop(i)
        i -= 1
    l_list = len(my_list)
    i += 1

for j in range(zero):
    my_list.append(0)

print(*my_list)
