N, M = input().split()
# qty of cubes in each person
c_Ann, c_Boria = [], []

for i in range(int(N)):
    c_Ann.append(int(input()))
for i in range(int(M)):
    c_Boria.append(int(input()))

intersection = set(c_Ann) & set(c_Boria)
print(len(intersection))
print(*sorted(list(intersection)))

uniq_Ann = set(c_Ann) - intersection
print(len(uniq_Ann))
print(*sorted(list(uniq_Ann)))

uniq_Boria = set(c_Boria) - intersection
print(len(uniq_Boria))
print(*sorted(list(uniq_Boria)))
