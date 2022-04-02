list_N = list(map(int, input().split()))

l_list_N = len(list_N)

if l_list_N % 2 == 0:
    for i in range(1, l_list_N, 2):
        list_N[i-1], list_N[i] = list_N[i], list_N[i-1]
else:
    last = list_N.pop()
    for i in range(1, l_list_N, 2):
        list_N[i-1], list_N[i] = list_N[i], list_N[i-1]
    list_N.append(last)

print(*list_N)
