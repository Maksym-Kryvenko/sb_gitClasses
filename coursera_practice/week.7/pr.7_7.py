n = int(input().strip())  # max num that could be desired

req_set = set()  # set with possible answer

for i in range(1, n+1):
    req_set.add(str(i))

# try to find list, which
# insist required num
guess = input()  # try to guess
while guess != 'HELP':
    guess = set(guess.split())
    answer = input()  # answer is it in list
    if len(guess) == 1 and answer == "YES":
        req_set = guess
        break
    elif answer == "YES":
        req_set &= guess
    elif answer == "NO":
        req_set -= guess
    guess = input()  # try to guess

print(*sorted(req_set))
