in_line = list(map(int, input().split()))

uniq = {in_line[0], }
print('NO')

for i in in_line[1:]:
    if i not in uniq:
        uniq.add(i)
        print('NO')
    else:
        print('YES')
