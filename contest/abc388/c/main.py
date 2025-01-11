import bisect

N = input()
A = list(map(int, input().split()))
A.sort()

ans = 0
for lower in A:
    ans += bisect.bisect_right(A, lower / 2)

print(ans)
