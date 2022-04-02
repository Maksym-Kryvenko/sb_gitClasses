list_N = list(map(int, input().split()))
unique = []

for i in list_N:
    if i not in unique:
        unique.append(i)

print(len(unique))
