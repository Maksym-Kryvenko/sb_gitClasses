num_str = input()

new_list = list(map(int, list(num_str.split())))
j, k = new_list[0], 0


for i in range(len(new_list)):
    if new_list[i] > j:
        j, k = new_list[i], i
print(j, k)
