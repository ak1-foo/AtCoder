N, D = map(int, input().split())
S = input()

cookie = S.count("@")

ans = N - (cookie - D)
print(ans)
