P = int(input())
X = int(input())
Y = int(input())
K = int(input())
s = (X*100 + Y)

for i in range(K):
    s = s + int(s * (P / 100))
print(int(s // 100), int(s % 100))
