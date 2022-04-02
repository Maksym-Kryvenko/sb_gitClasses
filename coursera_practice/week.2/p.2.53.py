listab = list(map(int, input().split()))
k = int(input())
lista = listab[:(k + 1)]
listb = listab[k + 1:]
lista.pop()
lista.extend(listb)
print(*lista, end=" ")
