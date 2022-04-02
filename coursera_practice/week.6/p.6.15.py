# count lowest price for delivery list of people
fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

# distance
dist = list(map(int, fin.readline().split()))
# rate of taxi
rate = list(map(int, fin.readline().split()))

fin.close()

dist.sort()
rate.sort(reverse=True)

total_price = 0
for r, d in zip(rate, dist):
    total_price += r * d

print(str(total_price), file=fout)

fout.close()
