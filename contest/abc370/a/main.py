L, R = map(int, input().split())

if L == 1 and R == 0:
    ans = 'Yes'
elif L == 0 and R == 1:
    ans = 'No'
else:
    ans = 'Invalid'

print(ans)
