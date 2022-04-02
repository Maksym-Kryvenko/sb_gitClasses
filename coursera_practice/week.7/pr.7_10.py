row = list(map(int, input().split()))

f_bus = (row[0], row[1])
s_bus = (row[2], row[3])
f_bus, s_bus = sorted(f_bus), sorted(s_bus)

f_bus_set = set(range(f_bus[0], f_bus[1]+1))
s_bus_set = set(range(s_bus[0], s_bus[1]+1))

print(len(f_bus_set.intersection(s_bus_set)))
