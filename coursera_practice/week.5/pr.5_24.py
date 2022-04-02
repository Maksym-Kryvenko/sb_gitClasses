num_str = input()

new_list = list(num_str.split())

for i in range(len(new_list)-1, -1, -1):
    print(new_list[i], end=' ')
