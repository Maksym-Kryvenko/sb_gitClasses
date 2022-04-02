FIN = open('input_6_5.txt', 'r', encoding='utf8')

sum9, c9 = 0, 0
sum10, c10 = 0, 0
sum11, c11 = 0, 0

for line in FIN:
    line_s = list(line.split())
    # print(f'line {line_s}')
    if line_s[2] == '9':
        sum9 += int(line_s[3])
        c9 += 1
        # print('1')
    elif line_s[2] == '10':
        sum10 += int(line_s[3])
        c10 += 1
        # print('2')
    elif line_s[2] == '11':
        sum11 += int(line_s[3])
        c11 += 1
        # print('3')

FIN.close()
print(sum9/c9, sum10/c10, sum11/c11, sep=' ')
