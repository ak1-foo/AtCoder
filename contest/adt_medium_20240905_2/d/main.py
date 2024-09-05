import math
N = int(input())

max_k = math.floor(math.log2(N))
tmp = 1
for i in range(max_k + 1):
    if tmp * 2 <= N:
        tmp *= 2
    else:
        print(i)
        exit()
