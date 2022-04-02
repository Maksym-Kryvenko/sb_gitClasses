N = int(input())
list_card = []

for i in range(1, N):
    list_card.append(int(input()))

for j in range(1, N+1):
    if j not in list_card:
        print(j)
