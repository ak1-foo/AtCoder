S = list(input())

count = 0
prev = "o"
for s in S:
    if s == prev:
        count += 1
    prev = s

if S[-1] == "i":
    count += 1

print(count)
