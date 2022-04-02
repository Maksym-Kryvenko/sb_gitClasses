N = int(input())

N_new = N % (24*60)
Hours = N_new // 60
Minutes = N_new % 60

print(Hours, Minutes)
