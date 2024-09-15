# WA, time over

import bisect
def find_insert_index_left(sorted_list, N):
    index = bisect.bisect_left(sorted_list, N)
    return index

def find_insert_index_right(sorted_list, N):
    index = bisect.bisect_right(sorted_list, N)
    return index

N = int(input())

location = list(map(int, input().split()))
people = list(map(int, input().split()))

info = []
for i in range(N):
    if i == 0:
        info.append({"location": location[i], "people_sum": people[i]})
    else:
        info.append({"location": location[i], "people_sum": info[i-1]['people_sum'] + people[i]})


max_location = max(location)
min_location = min(location)

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    L_location = find_insert_index_left(location, L)
    R_location = find_insert_index_right(location, R)

    if R < min_location:
        ans = 0
    elif L > max_location:
        ans = 0
    if L < min_location and R > max_location:
        ans = info[-1]["people_sum"]
    elif L < min_location:
        ans = info[R_location]["people_sum"]
    elif R > max_location:
        ans = info[R_location]["people_sum"] - info[L_location]["people_sum"]

    elif L_location == R_location:
        ans = info[L_location]["people_sum"]
    else:
        ans = info[R_location]["people_sum"] - info[L_location]["people_sum"]
    print(ans)
