S = input()

count = 0
for i, s in enumerate(S):
    if i == 0:
        continue

    if s == "|":
        print(count, end=" ")
        count = 0
    elif s == "-":
        count += 1
