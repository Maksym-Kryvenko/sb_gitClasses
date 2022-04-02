row = input()
if row[-1] == ' ':
    row = row.replace(row[-1], '', 1)
print(row.count(' ') + 1)
