data = []
with open("C:\\Users\\maks1\\Desktop\\SB classes\\Intro to DS\\11\\words_freq.txt", 'r', encoding='utf8') as fin:
    for i in fin:
        freq, item = i.strip().split()
        data.append((int(freq), item))

data.sort(reverse=True)
for i in data[0:10]:
    print(i[0], i[1])
