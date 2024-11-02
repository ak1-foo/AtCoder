N = int(input())

schedule = []
for _ in range(N):
    schedule.append(list(map(int, input().split())))

Q = int(input())
for _ in range(Q):
    t, d = map(int, input().split())
    t -= 1
    if d % schedule[t][0] == schedule[t][1]:
        ans = d
    elif d % schedule[t][0] <= schedule[t][1]:
        ans = d + (schedule[t][1] - d % schedule[t][0])
    else:
        ans = d + (schedule[t][0] - d % schedule[t][0]) + schedule[t][1]
    print(ans)
