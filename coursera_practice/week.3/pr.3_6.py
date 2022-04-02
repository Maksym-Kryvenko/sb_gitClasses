P = int(input())
X = int(input())
Y = int(input())

s = (X + Y / 100) * (1 + P / 100)
print(int(s), int(float('{0:.2f}'.format((s - int(s)) * 100))))
