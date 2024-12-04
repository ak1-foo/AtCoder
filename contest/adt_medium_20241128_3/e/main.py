N = int(input())
S = input()

encoded = []
count = 0
pre_c = ""
for c in S:
    if c == pre_c:
        count += 1
    else:
        if pre_c:
            encoded.append((pre_c, count))
        pre_c = c
        count = 1
encoded.append((pre_c, count))

encoded.sort(key=lambda x: x[1], reverse=True)
encoded.sort(key=lambda x: x[0])


ans = 0
pre_c = ""
for e in encoded:
    if pre_c == e[0]:
        continue

    ans += e[1]
    pre_c = e[0]

print(ans)
