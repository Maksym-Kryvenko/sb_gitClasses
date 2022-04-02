in_list = list(map(int, input().split()))
unique = []

for value in in_list:
    if in_list.count(value) == 1:
        unique.append(value)

print(*unique)
