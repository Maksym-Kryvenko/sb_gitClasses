a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

delta = a*d - c*b
d1 = e*d - f*b
d2 = a*f - c*e
x = d1/delta
y = d2/delta

print(x, y)
