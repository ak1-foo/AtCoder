M = int(input())

Ai = []
for n in range(1, 20+1):
    for a in range(10, -1, -1):
        if M >= 3 ** a:
            M -= 3 ** a
            Ai.append(a)
            break

Ai = Ai[::-1]
print(len(Ai))
print(*Ai)
