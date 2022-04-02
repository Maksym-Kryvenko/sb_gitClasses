list_AB = int(input()), int(input())
A, B = sorted(list_AB)

for i in range(A, B+1):
    if str(i)[0:2] == (str(i)[3] + str(i)[2]):
        print(i)
