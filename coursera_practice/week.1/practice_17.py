v = int(input())
t = int(input())

dist = ((v*t)**2)**0.5
rest = ((109 - dist)**2)**0.5
print(int(rest % 109))
