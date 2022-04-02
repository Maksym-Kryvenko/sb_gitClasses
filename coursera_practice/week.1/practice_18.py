N = int(input())

minutes = N // 60
hours = minutes // 60 % 24
minutes = (N - hours*60*60) // 60
a = minutes % 60 // 10
b = minutes % 60 % 10
c = N % 60 // 10
d = N % 60 % 10

print(hours, str(a) + str(b), str(c) + str(d), sep=':')
