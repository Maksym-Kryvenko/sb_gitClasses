import math

x = float(input())
n, list_num = 0, []

while x != 0:
    list_num.append(x)
    x = float(input())
    n += 1

s = sum(list_num) / n
top_sum = 0
for i in list_num:
    top_sum += (i - s)**2

top_sum = math.sqrt(top_sum/(n-1))
print(top_sum)
