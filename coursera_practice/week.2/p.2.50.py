n = int(input())
n3 = 0
n2 = n
n1 = 0
quantity_min = 1
quantity = 1
pocet = 0
while n != 0:
    n1 = n2
    n2 = n3
    n3 = n
    if n1 < n2 > n3:
        if pocet == 1:
            quantity_min = quantity
        elif quantity_min >= quantity and pocet > 1:
            quantity_min = quantity
        quantity = 1
        pocet += 1
    else:
        quantity += 1
    n = int(input())
if pocet > 1:
    print(quantity_min)
else:
    print(0)
