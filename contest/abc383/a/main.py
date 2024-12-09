N = int(input())

water = 0
pre_time = 0
for _ in range(N):
    T, V = map(int, input().split())
    water = max(water - (T - pre_time), 0)
    water += V
    pre_time = T

print(water)
