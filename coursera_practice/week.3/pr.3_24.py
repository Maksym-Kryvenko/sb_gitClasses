row = input()

row_new = ''
for i in range(len(row)-1):
    row_new += row[i] + '*'

print(row_new+row[-1])
