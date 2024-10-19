N, C = map(int, input().split())
T = list(map(int, input().split()))

count = 0
pre_time = -1
for i in range(N):
    if i == 0:
        count += 1
        pre_time = T[i]
    elif T[i] - pre_time >= C:
        count += 1
        pre_time = T[i]

print(count)
