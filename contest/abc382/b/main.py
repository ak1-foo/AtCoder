N, D = map(int, input().split())
S = input()

cookie_index = [i for i, s in enumerate(S) if s == "@"]

remain_cookie_idx = cookie_index[:-D]

remain_cookie = []
for i in range(N):
    if i in remain_cookie_idx:
        remain_cookie.append("@")
    else:
        remain_cookie.append(".")

ans = "".join(remain_cookie)
print(ans)
