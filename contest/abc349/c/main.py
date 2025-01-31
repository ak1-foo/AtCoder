S = input()
T = input()

mode = 3
if T[2] == "X":
    mode = 2

current = 0
for s in S:
    if s.upper() == T[current]:
        current += 1

    if current == mode:
        print("Yes")
        exit()

print("No")
