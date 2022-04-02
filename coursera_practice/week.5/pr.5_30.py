N = int(input())    # list length
list_N = list(map(int, input().split()))
list_N = list_N[:N]
x = int(input())   # value to search
n_closer = list_N[0]

for number in list_N:
    if abs(x - number) < abs(x - n_closer):
        n_closer = number      # closest number

print(n_closer)
