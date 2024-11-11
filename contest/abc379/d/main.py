from collections import deque

Q = int(input())

plants = deque()
for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        plants.append(0)
    elif query[0] == 2:
        for i in range(len(plants)):
            plants[i] += query[1]
    elif query[0] == 3:
        ans = 0
        for _ in range(len(plants)):
            p = plants.popleft()
            if p >= query[1]:
                ans += 1
            else:
                plants.appendleft(p)  # 左側に戻す
                break
        print(ans)
