fTH = int(input())
fTM = int(input())
fTS = int(input())

sTH = int(input())
sTM = int(input())
sTS = int(input())

dif = (sTH*60*60 + sTM*60 + sTS) - (fTH*60*60 + fTM*60 + fTS)
print(dif)
