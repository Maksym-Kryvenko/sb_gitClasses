N = int(input())
myList = []

for i in range(N):
    surname, score = input().split()
    myList.append((score, surname))


def key_int(a):
    return int(a[0])


myList.sort(key=key_int, reverse=True)

for participant in myList:
    print(participant[1])
