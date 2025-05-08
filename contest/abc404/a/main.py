S = input()

for i in range(ord("a"), ord("z") + 1):
    c = chr(i)
    if c not in S:
        print(c)
        break
