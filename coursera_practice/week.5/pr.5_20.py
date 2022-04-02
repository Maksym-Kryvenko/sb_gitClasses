new_list = list(map(int, list(input().split())))


def bigger_neigh(new, j=0):
    for i in range(1, len(new)-1):
        if new[i-1] < new[i] > new[i+1]:
            j += 1
    return j


print(bigger_neigh(new_list))
