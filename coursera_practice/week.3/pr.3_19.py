row = input()

aim = row.find(' ')
row = row[(aim+1):] + row[aim] + row[:aim]
print(row)
