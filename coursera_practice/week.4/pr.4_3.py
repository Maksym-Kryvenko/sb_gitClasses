def distance(x1, y1, x2, y2, x3, y3):
    a = ((x1-x2)**2 + (y1-y2)**2)**0.5
    b = ((x1-x3)**2 + (y1-y3)**2)**0.5
    c = ((x3-x2)**2 + (y3-y2)**2)**0.5
    return a + b + c


print(distance(float(input()), float(input()),
               float(input()), float(input()),
               float(input()), float(input())))
