N, L = map(int, input().split())
d = list(map(int, input().split()))

# set location
location = [-1] * N
location_num = [0] * L
for i in range(N):
    if i == 0:
        location[i] = 0
    else:
        location[i] = (location[i - 1] + d[i - 1]) % L

    location_num[location[i]] += 1


# can make a triangle?
if L % 3 != 0:
    print(0)
    exit()

# count
ans = 0
for i in range(L // 3):
    ans += (
        location_num[i]
        * location_num[(i + L // 3) % L]
        * location_num[(i + 2 * L // 3) % L]
    )

print(ans)
