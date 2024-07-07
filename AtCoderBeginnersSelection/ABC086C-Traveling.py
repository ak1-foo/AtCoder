def get_distance(p1, p2):
    return abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

def is_reachable(p1, p2):
    time_remain = abs(p1[0] - p2[0])
    rest_time = time_remain - get_distance(p1, p2)
    # 間に合うか
    if rest_time < 0:
        return False
    # 目的地周辺で右往左往できるか
    if rest_time % 2 != 0:
        return False

    return True

N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

# 初期値から第1目的地まで
if ( is_reachable([0, 0, 0], l[0]) == False ):
    print('No')
    exit()

for i in range(N-1):
    if (is_reachable(l[i], l[i+1]) == False):
        print('No')
        exit()

print('Yes')
