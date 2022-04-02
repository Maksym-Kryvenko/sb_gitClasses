list_N = list(map(int, input().split()))

new_list = [list_N.pop()]

for value in list_N:
    new_list.append(value)

print(*new_list)
