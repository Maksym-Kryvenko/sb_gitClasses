A = int(input())
B = int(input())
N = int(input())

total_price = (A*100 + B) * N
A_new = total_price // 100
B_new = total_price % 100
print(A_new, B_new)
