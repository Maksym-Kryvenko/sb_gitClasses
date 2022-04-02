N = list(map(int, input().split()))

N_max_1 = N[0]
N_max_2 = N[0]
N_min_1 = N[0]
N_min_2 = N[0]

for value in N:
    if value > N_max_1:
        N_max_2 = N_max_1
        N_max_1 = value
    elif value > N_max_2:
        N_max_2 = value

for value in N:
    if value < N_min_1:
        N_min_2 = N_min_1
        N_min_1 = value
    elif value < N_min_2:
        N_min_2 = value

if N_max_2 * N_max_1 > N_min_2 * N_min_1:
    print(N_max_2, N_max_1)
elif N_max_2 * N_max_1 < N_min_2 * N_min_1:
    print(N_min_1, N_min_2)
