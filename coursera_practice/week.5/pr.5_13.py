num_str = input()

new_list = list(num_str.split())

for i in range(0, len(new_list), 2):
    print(new_list[i], end=' ')
