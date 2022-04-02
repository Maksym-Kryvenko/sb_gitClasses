listAB = list(map(int, input().split()))
list_to_append = list(map(int, input().split()))       # position k, value C
k, C = list_to_append[0], list_to_append[1]

listA = listAB[:k]
listB = listAB[k:]
listA.append(C)
listA.extend(listB)
print(*listA, end=" ")
