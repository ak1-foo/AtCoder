N = int(input())
A = list(map(int, input().split()))

big_sum = sum(A) ** 2
sum_same_ij = sum([a**2 for a in A])

ans = (big_sum - sum_same_ij) // 2
print(ans)
