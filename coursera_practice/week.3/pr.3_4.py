price = float(input())

wp = int(price)
print(wp, int(float('{0:.2f}'.format(price - wp))*100))
