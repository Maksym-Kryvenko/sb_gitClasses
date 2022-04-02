NK_list = list(map(int, input().split()))
N = NK_list[0]    # qty of cagel
K = NK_list[1]    # qty of throw
set_cagel = []

for i in range(N):
    set_cagel.append('I')

# print(set_cagel)

for j in range(K):
    in_list = list(map(int, input().split()))
    for k in range((in_list[0]-1), (in_list[1])):
        set_cagel[k] = '.'
    in_list.clear()
    # print(set_cagel)

print(*set_cagel, sep='')
