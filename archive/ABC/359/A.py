N = int(input())
Sn = [input() for _ in range(N)]

cnt = 0
for i in range(N):
    if Sn[i] == "Takahashi":
        cnt += 1

print(cnt)
