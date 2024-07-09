N, K = map(int, input().split())
An = list(map(int, input().split()))

An.sort()

for _ in range(K):
    diff_delete_min = An[-1] - An[1]
    diff_delete_max = An[-2] - An[0]
    if (diff_delete_max < diff_delete_min):
        An.remove(An[-1])
    else:
        An.remove(An[0])


print(An[-1] - An[0])
