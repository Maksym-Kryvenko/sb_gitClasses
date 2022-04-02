num_str = input()

new_list = map(int, list(num_str.split()))
j = 0

j = [j+1 for i in new_list if i > 0]
print(len(j))
