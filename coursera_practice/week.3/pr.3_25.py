row = input()

for i in range(len(row)):
    if i == 0:
        row = row.replace(row[i], '', 1)
    elif i % 3 == 0:
        i -= 1
        row = row.replace(row[i], '', 1)
print(row)
