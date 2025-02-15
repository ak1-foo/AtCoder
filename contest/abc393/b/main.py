import re

S = input()

A_idx = [m.start() for m in re.finditer(r"A", S)]
B_idx = [m.start() for m in re.finditer(r"B", S)]
C_idx = [m.start() for m in re.finditer(r"C", S)]

ans = 0
for a in A_idx:
    for b in B_idx:
        for c in C_idx:
            if a < b < c and b - a == c - b:
                ans += 1


print(ans)
