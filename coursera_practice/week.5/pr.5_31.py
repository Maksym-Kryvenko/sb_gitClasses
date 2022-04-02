classmates = list(map(int, input().split()))
X = int(input())   # height Petya
ind = len(classmates) + 1

for i in classmates:
    if i < X:
        ind = classmates.index(i) + 1
        break

print(ind)
