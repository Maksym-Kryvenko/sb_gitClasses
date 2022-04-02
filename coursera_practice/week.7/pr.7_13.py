f_in = open('input.txt')

qty = int(f_in.readline())

city_data = dict()
for i in range(qty):
    raw = list(f_in.readline().strip().split())
    city_data[raw[0]] = set(raw[1:])

qty_city = int(f_in.readline())

for qty in range(qty_city):
    raw = f_in.readline().strip()
    for i, j in city_data.items():
        if raw in j:
            print(i)
