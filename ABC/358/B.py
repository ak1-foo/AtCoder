N, A = map(int, input().split())
T = list(map(int, input().split()))

current_time = 0
for i in range(N):
    if current_time >= T[i]: # already come
        current_time += A
    else:
        current_time = T[i] + A # not come yet

    print(current_time)
