n = int(input().strip())  # max num that could be desired

req_set = set()  # set with possible answer

for i in range(1, n+1):
    req_set.add(str(i))

# try to find list, which
# insist required num
guess = input()  # try to guess
while guess.strip() != 'HELP':
    guess = set(guess.split())
    if len(req_set & guess) > len(req_set) // 2:
        print("YES")
        req_set &= guess
    elif len(req_set & guess) <= len(req_set) // 2:
        print('NO')
        req_set -= guess
    guess = input()  # try to guess

req_set = list(map(int, req_set))
print(*sorted(req_set))
