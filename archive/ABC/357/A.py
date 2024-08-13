N, M = map(int, input().split())
hands = list(map(int, input().split()))

cleaned_man = 0
for hand in hands:
    if M >= hand:
        M -= hand
        cleaned_man += 1
    else:
        break

print(cleaned_man)
