in_list = list(map(int, input().split()))
counter = 0

for i in range(len(in_list)):
    for j in range(i + 1, len(in_list)):
        if in_list[j] == in_list[i]:
            counter += 1

print(counter)
