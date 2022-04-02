a, b, c, d, e = [], [], [], [], 0
for i in range(8):
    l, r = map(int, input().split())
    a.append(l), b.append(r), c.append(a[i] - b[i]), d.append(a[i] + b[i])
    if b.count(b[i]) != 1 or a.count(a[i]) != 1 or (
            c.count(c[i]) != 1 or d.count(d[i]) != 1):
        print('Yes')
        e = 0
        break
    else:
        e = 1
if e:
    print('No')
