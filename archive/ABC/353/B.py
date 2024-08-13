group_num, empty_seats = map(int, input().split())
groups = list(map(int, input().split()))

cnt = 0
rest_seat = empty_seats
for group in groups:
    if group <= rest_seat: # can ride
        rest_seat -= group
    else: # cannot ride
        cnt += 1
        rest_seat = empty_seats - group

# go last groups
cnt += 1

print(cnt)
