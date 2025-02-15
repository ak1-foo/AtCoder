import re

N = int(input())
S = input()

idx_1 = [match.start() for match in re.finditer(r"1", S)]

tmp = [idx_1[i] - i for i in range(len(idx_1))]
median = sorted(tmp)[len(idx_1) // 2]

ans = sum(abs(tmp[i] - median) for i in range(len(idx_1)))

print(ans)
