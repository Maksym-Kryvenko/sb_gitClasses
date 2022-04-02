fIN = open('input_6_6.txt', 'r', encoding='utf8')
fOUT = open('output_6_6.txt', 'w', encoding='utf8')

list_of_stud = []
for line in fIN:
    line_s = list(line.split())
    list_of_stud.append(line_s)
list_of_stud.sort()

for data in list_of_stud:
    print(data[0], data[1], data[3], file=fOUT)

fIN.close()
fOUT.close()
