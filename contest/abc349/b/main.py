from collections import Counter, defaultdict

S = input()

count = defaultdict(list)
for k, v in sorted(Counter(S).items(), key=lambda x: x[1]):
    count[v].append(k)

for v in count.values():
    if len(v) != 0 and len(v) != 2:
        print("No")
        exit()

print("Yes")
