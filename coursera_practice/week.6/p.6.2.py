N = int(input()) - 3  # size of shoes
avail_sizes = sorted(list(map(int, input().split())))
counter = 0

for value in avail_sizes:
    if value >= N and (value - N) >= 3:
        counter += 1
        N = value

print(counter)
