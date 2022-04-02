N = int(input())

ab = N // 100
cd = N % 100
a = ab // 10
b = ab % 10
ba = int(str(b) + str(a))

print(cd - ba + 1)
