triple = int(input())

first = triple // 100
restOfTriple = triple % 100
second = restOfTriple // 10
third = restOfTriple % 10

print(first + second + third)
