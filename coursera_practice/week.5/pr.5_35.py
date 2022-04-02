N = list(map(int, input().split()))

N_min = N[0]
N_max = N[0]

for value in N:
    if value > N_max:
        N_max = value
    elif value < N_min:
        N_min = value

Max_N = N.index(N_max)
Min_N = N.index(N_min)
N[Max_N], N[Min_N] = N[Min_N], N[Max_N]

print(*N)
