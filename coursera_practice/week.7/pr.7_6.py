import sys

unique_W = set()

in_F = sys.stdin.read()
in_F = in_F.split()

for i in in_F:
    unique_W.add(i)

sys.stdout.write(str(len(unique_W)))
