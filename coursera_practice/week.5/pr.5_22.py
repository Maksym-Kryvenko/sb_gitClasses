num_str = input()

new_list = list(map(int, list(num_str.split())))
positive_list = []


for i in new_list:
    if i > 0:
        positive_list.append(i)
print(min(positive_list))
