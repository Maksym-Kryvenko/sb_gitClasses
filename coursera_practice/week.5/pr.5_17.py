num_str = input()

new_list = list(map(int, list(num_str.split())))

for i in range(1, len(new_list)):
    if new_list[i] > new_list[i-1]:
        print(new_list[i], end=' ')
