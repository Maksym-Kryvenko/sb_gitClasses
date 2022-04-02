listab = list(map(int, input().split()))
k = int(input())
lista = listab[:k]
listb = listab[k + 1:]
lista.extend(listb)
print(*lista, end=" ")
