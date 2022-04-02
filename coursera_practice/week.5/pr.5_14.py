num_str = input()

new_list = map(int, list(num_str.split()))

[print(i, end=' ') for i in new_list if i % 2 == 0]
