import math
import bisect

from sortedcontainers import SortedList

N, K = map(int, input().split())
P = list(map(int, input().split()))

P_with_idx = [(p, i) for i, p in enumerate(P)]
P_with_idx.sort(key=lambda x: x[0])
idxs = [p[1] for p in P_with_idx]

ans = math.inf
for i in range(N-K+1):
    if i == 0:
#       sorted_parts_idxs = sorted(idxs[:K])
        sorted_parts_idxs = SortedList(idxs[:K])
    else:
#       bisect.insort(sorted_parts_idxs, idxs[i+K-1])
#       sorted_parts_idxs.pop(bisect.bisect_left(sorted_parts_idxs, idxs[i-1]))
        sorted_parts_idxs.add(idxs[i+K-1])
        sorted_parts_idxs.remove(idxs[i-1])


    max_idx = sorted_parts_idxs[-1]
    min_idx = sorted_parts_idxs[0]
    ans = min(ans, max_idx - min_idx)

print(ans)
