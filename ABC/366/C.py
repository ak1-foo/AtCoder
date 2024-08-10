query_num = int(input())

Q = [list(map(int, input().split())) for _ in range(query_num)]

balls = {}
for q in Q:
    if q[0] == 1:
        balls[q[1]] = balls.get(q[1], 0) + 1
    elif q[0] == 2:
        balls[q[1]] -= 1
        if balls[q[1]] == 0:
            del balls[q[1]]
    elif q[0] == 3:
        print(len(balls))
