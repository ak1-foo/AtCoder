N = int(input())

ans = 0
is_login = False
for _ in range(N):
    S = input()
    if S == "login":
        is_login = True
    elif S == "logout":
        is_login = False

    if (not is_login) and S == "private":
        ans += 1

print(ans)
