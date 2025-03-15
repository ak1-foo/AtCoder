# WA
import bisect

N = int(input())

# 10**18 = (10**6)**3
three_times = [i**3 for i in range(0, 10**6 + 1)]

for y in range(1, 10**6 + 1):
    diff = N + three_times[y]
    nearest = bisect.bisect_left(three_times, diff)

    if nearest == 10**6 + 1:
        continue
    if three_times[nearest] == diff:
        print(nearest, y)

        exit()

print(-1)
