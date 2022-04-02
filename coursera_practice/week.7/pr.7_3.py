first = set(map(int, input().split()))
second = set(map(int, input().split()))

print(*sorted(list(first.intersection(second))))


# or

print(*sorted(set(input().split()) & set(input().split()), key=int))

# or

print(*sorted(set(map(int, input().split())) & set(map(int, input().split()))))
