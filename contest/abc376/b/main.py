N, Q = map(int, input().split())

L = 1
R = 2
cost = 0
for _ in range(Q):
    h, t = input().split()
    t = int(t)

    if h == 'L':
        if L < t < R:
            cost += t - L
        elif L < R < t:
            cost += L + N - t
        elif t < L < R:
            cost += L - t
        elif t < R < L:
            cost += t + N - L
        elif R < t < L:
            cost += L - t
        elif R < L < t:
            cost += t - L

        L = t

    elif h == 'R':
        if L < t < R:
            cost += R - t
        elif L < R < t:
            cost += t - R
        elif t < L < R:
            cost += t + N - R
        elif t < R < L:
            cost += R - t
        elif R < t < L:
            cost += t - R
        elif R < L < t:
            cost += R + N - t

        R = t

print(cost)
