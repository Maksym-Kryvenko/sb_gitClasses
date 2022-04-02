n = int(input())


print(n*'+___ ')
for i in range(1, n + 1):
    print(f'|{i} /', end=' ')

print()
print(n*'|__\\ ')
print(n*'|    ')
