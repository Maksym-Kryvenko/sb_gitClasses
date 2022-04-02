s = input()
s1 = s[::3]
i = 0
while i < len(s1):
    s = s.replace(s1[i], '', 1)
    i = i + 1
print(s)
