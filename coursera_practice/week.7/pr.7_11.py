f_IN = open('input.txt', 'r', encoding='utf8')

# qty days in year and qty of parties
days, parties = list(map(int, f_IN.readline().split()))

data_parties = set()  # meeting days of parties

for i in range(parties):
    f_day, d_step = list(map(int, (f_IN.readline().split())))
    data_parties |= set(range(f_day, days+1, d_step))

f_IN.close()

# weekdays during year
weekdays = set(range(6, days+1, 7)) | set(range(7, days+1, 7))

print(len(data_parties - weekdays))
