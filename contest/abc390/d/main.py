# TLE
N = int(input())
A = list(map(int, input().split()))
A.sort()

A = tuple(A)  # set() に入れるため

queue = {A}
seen = {A}

while queue:  # dfs
    current = queue.pop()

    for i in range(len(current)):
        for j in range(i + 1, len(current)):
            new = list(current)
            new[j] += current[i]
            new.pop(i)
            new = tuple(sorted(new))

            if new not in seen:
                seen.add(new)
                queue.add(new)

ans = set()
for pattern in seen:
    result = 0
    for p in pattern:
        result ^= p
    ans.add(result)

print(len(ans))
