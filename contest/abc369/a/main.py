A, B = map(int, input().split())

if A == B:
    ans = 1
elif (A - B) % 2 == 0:
    ans = 3
else:
    ans = 2

print(ans)