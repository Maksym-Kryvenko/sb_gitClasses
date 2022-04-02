n = int(input())
fact_sum = 0

for i in range(1, n+1):
    k = 1
    for j in range(1, i+1):
        k *= j
    fact_sum += k

print(fact_sum)
