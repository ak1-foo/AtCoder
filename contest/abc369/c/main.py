N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(1)
    exit()

A_diff = [A[i+1]-A[i] for i in range(N-1)]

# A_diffを圧縮する
A_compressed = []
count = 1
for i in range(len(A_diff)-1):
    if A_diff[i] == A_diff[i+1]:
        count += 1
    else:
        A_compressed.append({'num': A_diff[i], 'count': count})
        count = 1
A_compressed.append({'num': A_diff[-1], 'count': count})


# (1,1), (2,2) など、同じ数字の組み合わせ
num_pattern = N

# 1のとき、+1
# 2のとき、+3
# 3のとき、+6
# nのとき、+n*(n+1)//2
for i in range(len(A_compressed)):
    num_pattern += A_compressed[i]['count'] * (A_compressed[i]['count']+1) // 2

print(num_pattern)